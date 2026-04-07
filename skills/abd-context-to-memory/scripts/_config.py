"""Minimal shared config. Load OPENAI_API_KEY from .env / conf/.secrets."""
import os
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
_SKILL_ROOT = _SCRIPTS.parent
_REPO_ROOT = _SKILL_ROOT.parent.parent

try:
    from dotenv import load_dotenv

    for p in (
        _REPO_ROOT / "conf" / ".secrets",
        _REPO_ROOT / "conf" / ".env",
        _SKILL_ROOT / ".env",
        Path.cwd() / ".env",
    ):
        if p.exists():
            load_dotenv(p, override=True)
except ImportError:
    pass
