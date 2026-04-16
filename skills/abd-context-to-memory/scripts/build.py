#!/usr/bin/env python3
"""Build AGENTS.md from content/parts (abd-skill-builder merge). Delegates to scripts/base/build.py."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

_SKILL_ROOT = Path(__file__).resolve().parent.parent
_BASE_BUILD = Path(__file__).resolve().parent / "base" / "build.py"

if __name__ == "__main__":
    subprocess.run(
        [sys.executable, str(_BASE_BUILD)],
        cwd=str(_SKILL_ROOT),
        check=True,
    )
