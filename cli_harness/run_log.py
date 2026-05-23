"""Append-only run log at delivery-war-room/run-log.jsonl."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def append(war_room: Path, event: str, **fields: Any) -> dict:
    entry = {"timestamp": _now_iso(), "event": event, **fields}
    log_path = war_room / "run-log.jsonl"
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
    return entry


def read_all(war_room: Path) -> list[dict]:
    log_path = war_room / "run-log.jsonl"
    if not log_path.exists():
        return []
    entries: list[dict] = []
    with open(log_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                entries.append(json.loads(line))
    return entries


def last_entry(war_room: Path) -> dict | None:
    entries = read_all(war_room)
    return entries[-1] if entries else None
