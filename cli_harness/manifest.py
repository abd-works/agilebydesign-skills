"""Read and query manifest.md for war room state."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


def read_manifest(war_room: Path) -> dict[str, Any]:
    """Parse the YAML block from manifest.md and return as dict."""
    manifest_path = war_room / "manifest.md"
    if not manifest_path.exists():
        raise FileNotFoundError(f"manifest.md not found in {war_room}")

    text = manifest_path.read_text(encoding="utf-8")

    yaml_blocks: list[str] = []
    in_block = False
    current: list[str] = []
    for line in text.splitlines():
        if line.strip().startswith("```yaml"):
            in_block = True
            current = []
            continue
        if line.strip() == "```" and in_block:
            in_block = False
            yaml_blocks.append("\n".join(current))
            continue
        if in_block:
            current.append(line)

    try:
        import yaml
    except ImportError:
        raise RuntimeError("pyyaml is required — pip install pyyaml")

    result: dict[str, Any] = {}
    for block in yaml_blocks:
        parsed = yaml.safe_load(block)
        if isinstance(parsed, dict):
            result.update(parsed)
    return result


def get_sizing_policy(manifest: dict[str, Any]) -> dict[str, Any]:
    return manifest.get("run_sizing_policy", {
        "stories_per_slot": 2,
        "stages_per_run": 1,
        "stall_timeout_minutes": 15,
        "notification_detail": "high",
    })


def get_checkpoint_policy(manifest: dict[str, Any]) -> str:
    return manifest.get("checkpoint_policy", "after_every_slot")


def get_slots(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    return manifest.get("slots", [])
