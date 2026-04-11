"""
Locate the skill root. ``scripts/<tool>.py`` lives one level below the skill root.
"""
from pathlib import Path

SKILL_ROOT: Path = Path(__file__).resolve().parents[1]
