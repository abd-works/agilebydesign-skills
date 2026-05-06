"""Watchdog-based watcher for the abd-practice-pipeline.

Runs as a long-lived VSCode task launched on `folderOpen`. Watches:

  - story/**/*.md
  - **/*.drawio
  - **/*.story-graph.json

On every change, calls `pipeline.py on-edit --path <changed>`. Debounces
with a small timer so editors that write atomically (rename / save) don't
fire twice.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import threading
import time
from pathlib import Path

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer


SCRIPT_DIR = Path(__file__).resolve().parent
PIPELINE = SCRIPT_DIR / "pipeline.py"

WATCHED_SUFFIXES = (".md", ".drawio", ".story-graph.json")
DEBOUNCE_SECONDS = 0.5


class PipelineHandler(FileSystemEventHandler):
    def __init__(self, root: Path) -> None:
        self.root = root
        self._timers: dict[str, threading.Timer] = {}
        self._lock = threading.Lock()

    def _interesting(self, path: str) -> bool:
        p = Path(path)
        if not any(str(p).endswith(s) for s in WATCHED_SUFFIXES):
            return False
        # ignore dotfiles and our own outputs nested under hidden dirs
        if any(part.startswith(".") for part in p.parts):
            return False
        return True

    def _schedule(self, path: str) -> None:
        with self._lock:
            existing = self._timers.pop(path, None)
            if existing is not None:
                existing.cancel()
            timer = threading.Timer(DEBOUNCE_SECONDS, self._fire, args=[path])
            timer.daemon = True
            self._timers[path] = timer
            timer.start()

    def _fire(self, path: str) -> None:
        with self._lock:
            self._timers.pop(path, None)
        print(f"[watch] change: {path}", flush=True)
        subprocess.run(
            [sys.executable, str(PIPELINE), "--non-interactive", "on-edit", "--path", path],
            check=False,
        )

    def on_modified(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return
        if self._interesting(event.src_path):
            self._schedule(event.src_path)

    def on_created(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return
        if self._interesting(event.src_path):
            self._schedule(event.src_path)

    def on_moved(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return
        dest = getattr(event, "dest_path", None)
        if dest and self._interesting(dest):
            self._schedule(dest)


def main() -> int:
    parser = argparse.ArgumentParser(description="abd-practice-pipeline watcher")
    parser.add_argument("--root", required=True, help="Engagement root to watch")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    print(f"[watch] starting on {root}", flush=True)
    handler = PipelineHandler(root)
    observer = Observer()
    observer.schedule(handler, str(root), recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    return 0


if __name__ == "__main__":
    sys.exit(main())
