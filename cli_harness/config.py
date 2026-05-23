"""Harness configuration — reads cli_harness/cli-config.json, then fallbacks."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

_PACKAGE_DIR = Path(__file__).parent

DEFAULT_CONFIG = {
    "api_key": None,
    "agent_mode": "local",
    "repo_url": None,
    "repo_ref": "main",
    "model": "composer-2.5",
    "stall_timeout_minutes": 15,
    "notification_channel": None,
    "sandbox": False,
    "mcp_allowlist": [],
    "approval_mode": "interactive",
}


def find_config_path() -> Path | None:
    candidates = [
        _PACKAGE_DIR / "cli-config.json",
        Path.home() / ".cursor" / "cli-config.json",
        Path(".cursor") / "cli.json",
    ]
    for p in candidates:
        if p.exists():
            return p
    return None


def load_config(path: Path | None = None) -> dict[str, Any]:
    if path is None:
        path = find_config_path()

    config = dict(DEFAULT_CONFIG)
    if path and path.exists():
        with open(path, encoding="utf-8") as f:
            file_config = json.load(f)
        config.update(file_config)

    env_key = os.environ.get("CURSOR_API_KEY")
    if env_key:
        config["api_key"] = env_key

    return config


def merge_engagement_overrides(base: dict[str, Any], overrides: dict[str, Any]) -> dict[str, Any]:
    merged = dict(base)
    for key in ("stall_timeout_minutes", "notification_channel", "sandbox", "mcp_allowlist",
                 "agent_mode", "repo_url", "repo_ref", "model"):
        if key in overrides and overrides[key] is not None:
            merged[key] = overrides[key]
    return merged


def save_engagement_config(war_room: Path, config: dict[str, Any]) -> Path:
    path = war_room / "harness-config.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)
    return path


def load_engagement_config(war_room: Path) -> dict[str, Any] | None:
    path = war_room / "harness-config.json"
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)
