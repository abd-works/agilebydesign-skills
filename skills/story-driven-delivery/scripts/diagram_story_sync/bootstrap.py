"""Resolve sibling skill ``scripts`` directories onto ``sys.path``.

The diagram-story-sync ecosystem assumes a monorepo layout::

    agilebydesign-skills/
        skills/
            story-driven-delivery/
                scripts/
                    diagram_story_sync/       <- this package
                story-graph-ops/scripts/      <- canonical story_graph_ops
                drawio-story-sync/scripts/
                miro-story-sync/scripts/

Backend skills (drawio-story-sync, miro-story-sync) import this package and
``story_graph_ops`` together. We auto-prepend both locations so that scripts and
tests do not need to set ``PYTHONPATH`` manually when the layout is the
default. Callers in non-default layouts should set ``PYTHONPATH`` themselves.
"""
from __future__ import annotations

import sys
from pathlib import Path


def _diagram_sync_scripts_dir() -> Path:
    """``.../story-driven-delivery/scripts`` — holds ``diagram_story_sync``."""
    return Path(__file__).resolve().parents[1]


def _story_delivery_root() -> Path:
    """``skills/story-driven-delivery`` — parent of ``scripts/``."""
    return _diagram_sync_scripts_dir().parent


def ensure_common_on_path() -> None:
    """Insert ``story-driven-delivery/scripts/`` so ``import diagram_story_sync`` works."""
    p = str(_diagram_sync_scripts_dir())
    if p not in sys.path:
        sys.path.insert(0, p)


def ensure_story_graph_ops_on_path() -> None:
    """Insert sibling ``story-graph-ops/scripts`` if present."""
    ops_scripts = _story_delivery_root() / "story-graph-ops" / "scripts"
    p = str(ops_scripts)
    if ops_scripts.is_dir() and p not in sys.path:
        sys.path.insert(0, p)


def ensure_backend_paths(backend_skill_dir: Path) -> None:
    """Insert shared ``scripts/`` plus a backend skill's ``scripts/`` and story-graph-ops.

    ``backend_skill_dir`` is expected to be the skill folder
    (e.g. ``.../story-driven-delivery/drawio-story-sync``); we add its ``scripts/`` subdirectory.
    """
    ensure_common_on_path()
    ensure_story_graph_ops_on_path()
    scripts = backend_skill_dir / "scripts"
    p = str(scripts)
    if scripts.is_dir() and p not in sys.path:
        sys.path.insert(0, p)


ensure_common_on_path()
ensure_story_graph_ops_on_path()
