"""Notification dispatch — pluggable backends."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


def send(channel: str | None, event: str, detail_level: str = "normal", **fields: Any) -> None:
    """Send a notification. Prints to stderr as baseline; extend for Slack/email/webhook."""
    msg = _format_message(event, detail_level, **fields)

    if channel and channel.startswith("http"):
        _send_webhook(channel, event, msg, fields)
    else:
        _send_console(msg)


def _format_message(event: str, detail_level: str, **fields: Any) -> str:
    parts = [f"[ABD Harness] {event}"]

    slot = fields.get("slot_id")
    if slot:
        parts.append(f"  Slot: {slot}")

    stage = fields.get("stage")
    if stage:
        parts.append(f"  Stage: {stage}")

    agent_id = fields.get("agent_id")
    if agent_id:
        parts.append(f"  Agent: {agent_id}")

    if detail_level == "high":
        for k, v in fields.items():
            if k not in ("slot_id", "stage", "agent_id"):
                parts.append(f"  {k}: {v}")
    else:
        reason = fields.get("reason") or fields.get("summary")
        if reason:
            parts.append(f"  {reason}")

    return "\n".join(parts)


def _send_console(msg: str) -> None:
    print(msg, file=sys.stderr)


def _send_webhook(url: str, event: str, msg: str, fields: dict) -> None:
    try:
        import urllib.request
        payload = json.dumps({"event": event, "message": msg, **fields}).encode()
        req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
        urllib.request.urlopen(req, timeout=10)
    except Exception as e:
        print(f"[ABD Harness] Webhook notification failed: {e}", file=sys.stderr)
        _send_console(msg)
