"""
Engine config — **skill-config.json** → **`engine`** object (legacy: **`workspace`**).
Uses pydantic if available, else plain dict. Ported from abd-story-synthesizer (same contract).
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_engine_config_dict(skill_root: Path) -> dict[str, Any]:
    """Load flat dict for **AbdConfig** from ``skill-config.json`` → ``engine`` (or legacy ``workspace``)."""
    skill_cfg = skill_root / "skill-config.json"
    if not skill_cfg.is_file():
        return {}
    full = json.loads(skill_cfg.read_text(encoding="utf-8"))
    eng = full.get("engine")
    if isinstance(eng, dict) and eng:
        return dict(eng)
    ws = full.get("workspace")
    if isinstance(ws, dict) and ws:
        return dict(ws)
    return {}


try:
    from pydantic import BaseModel

    class AbdConfig(BaseModel):
        """Engine config: optional constraints, context_paths, scanners (see scanner_paths)."""

        constraints: list[dict] = []
        context_paths: list[str] = []
        scanners: list[str] = []

        class Config:
            extra = "ignore"

except ImportError:

    class AbdConfig:
        """Plain-dict fallback when pydantic not installed."""

        def __init__(
            self,
            constraints: list[dict] | None = None,
            context_paths: list[str] | None = None,
            scanners: list[str] | None = None,
            **_: Any,
        ):
            self.constraints = constraints or []
            self.context_paths = context_paths or []
            self.scanners = scanners or []

        @classmethod
        def model_validate(cls, data: dict[str, Any]) -> "AbdConfig":
            return cls(
                constraints=data.get("constraints", []),
                context_paths=data.get("context_paths", []),
                scanners=list(data.get("scanners") or []),
            )
