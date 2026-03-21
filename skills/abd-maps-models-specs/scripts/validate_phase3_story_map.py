#!/usr/bin/env python3
"""Validate Phase 3 story map JSON: required fields, term_refs in phase2 terms, chunk files exist."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STORY_MAP = ROOT / "test" / "mm3" / "phase3" / "mm3_story_map.json"
TERMS = ROOT / "test" / "mm3" / "phase2" / "mm3_terms_layer.json"
CHUNKS = ROOT / "test" / "mm3" / "context" / "chunks"

ANCHOR_KINDS = frozenset({"read", "write", "both"})


def main() -> int:
    if not STORY_MAP.is_file():
        print("Missing", STORY_MAP, file=sys.stderr)
        return 1
    if not TERMS.is_file():
        print("Missing terms layer", TERMS, file=sys.stderr)
        return 1

    with open(STORY_MAP, encoding="utf-8") as f:
        sm = json.load(f)
    with open(TERMS, encoding="utf-8") as f:
        terms_doc = json.load(f)
    term_ids = {t["term_id"] for t in terms_doc.get("terms", [])}

    errors: list[str] = []
    stories = 0

    for epic in sm.get("epics", []):
        eid = epic.get("epic_id", "?")
        for story in epic.get("stories", []):
            stories += 1
            sid = story.get("story_id", "?")
            for req in (
                "name",
                "primary_actor",
                "behavior",
                "anchor",
            ):
                if req not in story:
                    errors.append(f"{eid}/{sid}: missing {req}")

            anchor = story.get("anchor") or {}
            kind = anchor.get("kind")
            if kind not in ANCHOR_KINDS:
                errors.append(f"{eid}/{sid}: anchor.kind must be read|write|both, got {kind!r}")
            if kind in ("read", "both") and not (anchor.get("read") or "").strip():
                errors.append(f"{eid}/{sid}: anchor.read required for kind={kind}")
            if kind in ("write", "both") and not (anchor.get("write") or "").strip():
                errors.append(f"{eid}/{sid}: anchor.write required for kind={kind}")

            refs = story.get("term_refs") or []
            ev = story.get("evidence_chunk_ids") or []
            if not refs and not ev:
                errors.append(
                    f"{eid}/{sid}: need at least one of term_refs or evidence_chunk_ids"
                )

            for tid in refs:
                if tid not in term_ids:
                    errors.append(f"{eid}/{sid}: unknown term_id {tid!r}")

            for uid in ev:
                p = CHUNKS / f"{uid}.md"
                if not p.is_file():
                    errors.append(f"{eid}/{sid}: missing chunk {uid}.md")

    if errors:
        print("validate_phase3_story_map: FAIL", file=sys.stderr)
        for e in errors:
            print(" ", e, file=sys.stderr)
        return 1

    print(
        "validate_phase3_story_map: OK —",
        len(sm.get("epics", [])),
        "epics,",
        stories,
        "stories",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
