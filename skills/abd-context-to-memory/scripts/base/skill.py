"""
skill — Skill runtime: load **skill-config.json** → **engine**, resolve topic root from env, assemble prompts.

Public API:
    Skill.load()               → Skill (skill root = folder with skill-config.json; topic root from CONTENT_MEMORY_ROOT only)
    Skill(path, engine=None)   → attach a skill path to an optional parent engine context
    skill.prompt(slug, form)   → str
    skill.instructions         → Instructions
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Literal

from config import AbdConfig, load_engine_config_dict
from rules import RuleSet


def _default_skill_root() -> Path:
    """Skill root = parent of ``scripts/`` (the directory that contains ``scripts/base/``)."""
    return Path(__file__).resolve().parent.parent


def _resolve_parts_dir(skill_path: Path) -> Path:
    p = skill_path / "content" / "parts"
    if (p / "process.md").is_file():
        return p
    return skill_path / "parts"


def _topic_root_from_env() -> Path | None:
    """Corpus/topic folder: CONTENT_MEMORY_ROOT env only (no skill-config path)."""
    r = os.environ.get("CONTENT_MEMORY_ROOT", "").strip()
    if not r:
        return None
    p = Path(r).expanduser()
    return p.resolve() if p.is_absolute() else (Path.cwd() / p).resolve()


# ---------------------------------------------------------------------------
# _EngineContext — topic root (env) and context_paths (passed into Instructions)
# ---------------------------------------------------------------------------

class _EngineContext:
    """Runtime context: optional topic root from CONTENT_MEMORY_ROOT + resolved context file paths."""

    def __init__(self) -> None:
        self.topic_root: Path | None = None
        self.context_paths: list[Path] = []

    def _load_context_paths(self, topic_root: Path) -> None:
        data: dict | None = None
        candidate = topic_root / "skill-config.json"
        if candidate.is_file():
            try:
                raw = json.loads(candidate.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                raw = None
            if isinstance(raw, dict):
                inner = raw.get("engine") or raw.get("workspace", raw)
                if isinstance(inner, dict) and inner.get("context_paths"):
                    data = inner
        if data is None:
            return
        for p in data.get("context_paths", []):
            path = Path(p)
            resolved = path.resolve() if path.is_absolute() else (topic_root / p).resolve()
            if resolved not in self.context_paths:
                self.context_paths.append(resolved)


# ---------------------------------------------------------------------------
# _BuildTimeContext — no topic root, used by build.py
# ---------------------------------------------------------------------------

class _BuildTimeContext(_EngineContext):
    """Minimal engine surface when generating derived built files (no topic context)."""

    topic_root = None
    context_paths: list = []


# ---------------------------------------------------------------------------
# Skill — single skill object
# ---------------------------------------------------------------------------

class Skill:
    """Represents one abd-skill.  Holds its path, config, and instruction assembler."""

    def __init__(self, path: str | Path, context: _EngineContext | None = None):
        self.path = Path(path).resolve()
        self._context: _EngineContext = context or _BuildTimeContext()
        self.rule_set = RuleSet(self.path)
        self.rule_set.load()
        self._skill_config = self._load_skill_config()
        self._operation_sections: dict[str, list[str]] = self._skill_config.get("operation_sections", {})
        self._instructions = None

    def _load_skill_config(self) -> dict:
        p = self.path / "skill-config.json"
        if not p.is_file():
            return {}
        return json.loads(p.read_text(encoding="utf-8"))

    @property
    def skill_config(self) -> dict:
        return self._skill_config

    @property
    def operation_sections(self) -> dict[str, list[str]]:
        return self._operation_sections

    @property
    def instructions(self) -> "Instructions":  # type: ignore[name-defined]
        if self._instructions is None:
            from instructions import Instructions

            self._instructions = Instructions(
                operation_sections=self._operation_sections,
                skill_path=self.path,
                context=self._context,
                skill_config=self._skill_config,
            )
        return self._instructions

    def prompt(self, slug: str, form: Literal["dynamic", "static"] = "dynamic") -> str:
        """Assemble prompt for *slug*. static reads phases/built/<slug>.md when present."""
        built = _resolve_parts_dir(self.path) / "phases" / "built" / f"{slug}.md"
        if form == "static" and built.is_file():
            return built.read_text(encoding="utf-8")
        return self.instructions.assemble_prompt(slug)

    # ------------------------------------------------------------------
    # Factory: load engine config; topic root from CONTENT_MEMORY_ROOT only
    # ------------------------------------------------------------------

    @classmethod
    def load(cls, skill_root: str | Path | None = None) -> "Skill":
        """Load skill. Topic root for live checklists / context paths = CONTENT_MEMORY_ROOT (env), else unset."""
        root = Path(skill_root).resolve() if skill_root else _default_skill_root()
        data = load_engine_config_dict(root)
        AbdConfig.model_validate(data)

        ctx = _EngineContext()
        skill_path = root.resolve()
        tr = _topic_root_from_env()
        ctx.topic_root = tr
        if ctx.topic_root:
            ctx._load_context_paths(ctx.topic_root)

        return cls(skill_path, context=ctx)
