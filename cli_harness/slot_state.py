"""Slot lifecycle state detection from war room files."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import NamedTuple


class SlotState(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    BLOCKED = "BLOCKED"
    FINISHED = "FINISHED"
    FAILED = "FAILED"


class SlotInfo(NamedTuple):
    slot_id: str
    state: SlotState
    running_data: dict | None = None


def _slot_ids(war_room: Path) -> list[str]:
    pattern = re.compile(r"^slot-(\d{2})-start\.md$")
    ids: list[str] = []
    for f in sorted(war_room.iterdir()):
        m = pattern.match(f.name)
        if m:
            ids.append(m.group(1))
    return ids


def get_slot_state(war_room: Path, slot_id: str) -> SlotInfo:
    start = war_room / f"slot-{slot_id}-start.md"
    finished = war_room / f"slot-{slot_id}-finished.md"
    blocked = war_room / f"slot-{slot_id}-blocked.md"
    answer = war_room / f"slot-{slot_id}-answer.md"
    running = war_room / f"slot-{slot_id}-running.json"

    if finished.exists():
        return SlotInfo(slot_id, SlotState.FINISHED)

    if blocked.exists() and not answer.exists():
        return SlotInfo(slot_id, SlotState.BLOCKED)

    running_data = None
    if running.exists():
        try:
            running_data = json.loads(running.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass

    if running_data:
        return SlotInfo(slot_id, SlotState.RUNNING, running_data)

    if start.exists():
        return SlotInfo(slot_id, SlotState.PENDING)

    return SlotInfo(slot_id, SlotState.PENDING)


def find_active_slot(war_room: Path) -> SlotInfo | None:
    for sid in _slot_ids(war_room):
        info = get_slot_state(war_room, sid)
        if info.state != SlotState.FINISHED:
            return info
    return None


def is_heartbeat_stale(running_data: dict, stall_timeout_minutes: int) -> bool:
    hb = running_data.get("last_heartbeat")
    if not hb:
        return True
    try:
        last = datetime.fromisoformat(hb)
        if last.tzinfo is None:
            last = last.replace(tzinfo=timezone.utc)
        elapsed = (datetime.now(timezone.utc) - last).total_seconds()
        return elapsed > stall_timeout_minutes * 60
    except (ValueError, TypeError):
        return True


def write_running_file(
    war_room: Path, slot_id: str, agent_id: str, run_id: str, mode: str = "local",
) -> Path:
    now = datetime.now(timezone.utc).isoformat()
    data = {
        "agent_id": agent_id,
        "run_id": run_id,
        "mode": mode,
        "started_at": now,
        "last_heartbeat": now,
    }
    path = war_room / f"slot-{slot_id}-running.json"
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path


def update_heartbeat(war_room: Path, slot_id: str) -> None:
    path = war_room / f"slot-{slot_id}-running.json"
    if not path.exists():
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    data["last_heartbeat"] = datetime.now(timezone.utc).isoformat()
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
