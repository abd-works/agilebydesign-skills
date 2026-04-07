"""
Full pipeline: convert → chunk → embed into local FAISS vector store.

Usage:
  python index_memory.py --path <source_folder>               # convert + chunk + embed
  python index_memory.py --path <source_folder> --skip-convert  # skip convert, chunk + embed only
  python index_memory.py --rebuild --path <source_folder>     # rebuild index from existing chunks

Chunks land in <source>/memory/. FAISS index in <source>/memory/rag/.
Run from workspace root.
"""

import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent


def run(script: str, args: list[str], cwd: Path) -> None:
    result = subprocess.run([sys.executable, str(SCRIPTS / script)] + args, cwd=str(cwd))
    if result.returncode != 0:
        print(f"ERROR: {script} failed.")
        sys.exit(1)


def main():
    args = sys.argv[1:]

    skip_convert = "--skip-convert" in args
    rebuild = "--rebuild" in args
    args = [a for a in args if a not in ("--skip-convert", "--rebuild")]

    path_idx = next((i for i, a in enumerate(args) if a == "--path"), None)
    if path_idx is None or path_idx + 1 >= len(args):
        print("Usage: python index_memory.py --path <source_folder> [--skip-convert] [--rebuild]")
        sys.exit(1)

    src = Path(args[path_idx + 1]).resolve()
    if not src.exists():
        print(f"ERROR: source folder not found: {src}")
        sys.exit(1)

    memory_dir = src / "memory"
    memory_dir.mkdir(parents=True, exist_ok=True)

    if not skip_convert:
        print(f"[1/3] Converting documents in {src} → markdown/")
        run("convert_to_markdown.py", ["--memory", str(src)], cwd=src)
    else:
        print("[1/3] Skipping convert (--skip-convert)")

    print(f"[2/3] Chunking markdown → {memory_dir}")
    run("chunk_markdown.py", ["--path", str(src), "--output", str(memory_dir)], cwd=src)

    print(f"[3/3] Embedding chunks → {memory_dir / 'rag'}")
    embed_args = ["--path", str(memory_dir)]
    if rebuild:
        embed_args.append("--replace")
    run("embed_and_index.py", embed_args, cwd=src)

    print(f"\nDone. Index: {memory_dir / 'rag'}")


if __name__ == "__main__":
    main()
