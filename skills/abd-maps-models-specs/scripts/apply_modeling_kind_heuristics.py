#!/usr/bin/env python3
"""Phase 1 stub: assign modeling_kind to each unit via cheap heuristics (v1).

Does not mutate context_index.json — writes a sidecar for review and promotion gates.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CTX = ROOT / "test" / "mm3" / "context"
CHUNKS = CTX / "chunks"
INDEX = CTX / "context_index.json"
OUT = CTX / "modeling_kind_sidecar.json"
# Taxonomy must match ALLOWED_KINDS in validate_modeling_kind_sidecar.py

BODY_TOC_THRESHOLD = 0.45


def read_chunk_body(uid: str) -> str:
    """Markdown body after YAML frontmatter, or full file if unparseable."""
    path = CHUNKS / f"{uid}.md"
    if not path.is_file():
        return ""
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return text.strip()


def toc_nav_body_score(body: str) -> float:
    """0..1 — higher means dot-leader / index-line wall typical of TOC or nav junk."""
    if not body or len(body) < 25:
        return 0.0
    lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
    if not lines:
        return 0.0
    tocish = 0
    for line in lines:
        dots = line.count(".")
        if dots >= 6:
            tocish += 1
        elif re.search(r"\.{3,}", line):
            tocish += 1
        elif len(line) > 80 and dots >= 4 and re.search(r"\d{1,4}\s*$", line):
            tocish += 1
    score = tocish / len(lines)
    if len(lines) == 1 and len(lines[0]) > 120:
        wall = lines[0]
        if wall.count(".") >= 8:
            score = max(score, 0.9)
        elif wall.count(" ") > 40 and re.search(r"\d{2,4}", wall) and len(wall) > 200:
            score = max(score, 0.75)
    return min(1.0, float(score))


def toc_like(section_path: list, row: dict) -> bool:
    joined = " ".join(section_path or [])
    if re.search(r"\.{6,}", joined):
        return True
    tags = " ".join(row.get("retrieval_tags") or [])
    if re.search(r"\.{6,}", tags):
        return True
    return False


def editorial_like(section_path: list) -> bool:
    joined = " ".join(section_path or []).upper()
    if "THIRD EDITION" in joined:
        return True
    if "PRINTED IN" in joined or "GREEN RONIN" in joined:
        return True
    return False


def classify(uid: str, row: dict) -> tuple[str, str]:
    et = row.get("evidence_type")
    if not et:
        return "ambiguous_review", "missing evidence_type"
    et = str(et)
    sp = row.get("section_path") or []
    dr = row.get("document_region") or ""
    sl = row.get("start_line")
    el = row.get("end_line")
    span = (el - sl + 1) if isinstance(sl, int) and isinstance(el, int) else 999
    body = read_chunk_body(uid)
    bscore = toc_nav_body_score(body)
    body_note = f"body_toc_score={bscore:.2f}"

    if editorial_like(sp):
        return "editorial_or_credit", "section_path editorial"
    if dr == "examples" or et == "example":
        return "narrative_example", "examples region or evidence_type"
    if et == "actor-action":
        return "behavioral_interaction", "evidence_type"
    if et == "mechanic":
        return "mechanic_rule", "evidence_type"
    if et == "variation/exception":
        return "variation_rule", "evidence_type"
    if et == "domain-rule" and toc_like(sp, row) and span <= 6:
        return "toc_or_nav_noise", "toc pattern + short span"
    if et == "domain-rule" and bscore >= BODY_TOC_THRESHOLD:
        return "toc_or_nav_noise", f"body toc/nav pattern ({body_note})"
    if et == "domain-rule":
        return "domain_rule_candidate", "default domain-rule"
    if et == "definition" and toc_like(sp, row) and span <= 6:
        return "toc_or_nav_noise", "toc pattern + short span (definition)"
    if et == "definition" and bscore >= BODY_TOC_THRESHOLD:
        return "toc_or_nav_noise", f"body toc/nav pattern ({body_note})"
    if et == "definition":
        return "definition_candidate", "evidence_type"
    return "ambiguous_review", "no rule matched"


def main() -> None:
    with open(INDEX, encoding="utf-8") as f:
        data = json.load(f)
    forward = data["forward_index"]

    out: dict[str, dict] = {}
    kinds = Counter()
    for uid, row in sorted(forward.items()):
        kind, rule = classify(uid, row)
        kinds[kind] += 1
        out[uid] = {
            "modeling_kind": kind,
            "heuristic_rule": rule,
            "schema_version": "v1",
            "heuristic_version": "v2",
        }

    payload = {
        "schema_version": "v1",
        "heuristic_version": "v2",
        "description": "Sidecar: modeling_kind per unit_id; heuristic until LLM/re-extract pass (v2: chunk body TOC signals)",
        "kinds_distribution": dict(kinds),
        "units": out,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    print("Wrote", OUT)
    print("Distribution:", dict(kinds))


if __name__ == "__main__":
    main()
