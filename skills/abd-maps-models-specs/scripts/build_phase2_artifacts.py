#!/usr/bin/env python3
"""Phase 2 — terms layer, named mechanisms, candidate queue (not concepts[]).

Reads context_index.json + modeling_kind_sidecar.json + chunk bodies.
Writes test/mm3/phase2/*.json per plan/PROCESS-PLAN.md Phase 2.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CTX = ROOT / "test" / "mm3" / "context"
CHUNKS = CTX / "chunks"
INDEX = CTX / "context_index.json"
SIDECAR = CTX / "modeling_kind_sidecar.json"
OUT_DIR = ROOT / "test" / "mm3" / "phase2"

TERM_KINDS = frozenset(
    {"definition_candidate", "mechanic_rule", "behavioral_interaction"}
)
CANDIDATE_KIND = "domain_rule_candidate"


def read_chunk_body(uid: str) -> str:
    path = CHUNKS / f"{uid}.md"
    if not path.is_file():
        return ""
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return text.strip()


def extract_title(body: str) -> str:
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("##"):
            return s.lstrip("#").strip()[:240]
    for line in body.splitlines():
        s = line.strip()
        if s:
            return s[:240]
    return ""


def slug_label(s: str) -> str:
    s2 = re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")
    return (s2[:96] or "term").rstrip("_")


def main() -> None:
    with open(INDEX, encoding="utf-8") as f:
        idx = json.load(f)
    forward = idx["forward_index"]

    with open(SIDECAR, encoding="utf-8") as f:
        side = json.load(f)
    units_meta = side["units"]

    terms: list[dict[str, object]] = []
    seen_slugs: dict[str, int] = {}

    mechanisms_by_path: dict[tuple[str, ...], list[dict[str, object]]] = defaultdict(list)

    candidates: list[dict[str, object]] = []
    cand_limit = 80

    for uid in sorted(forward.keys(), key=lambda x: (len(x), x)):
        row = forward[uid]
        meta = units_meta.get(uid, {})
        mk = meta.get("modeling_kind", "")
        body = read_chunk_body(uid)
        title = extract_title(body)
        section_path = row.get("section_path") or []

        if mk in TERM_KINDS and title:
            base = slug_label(title)
            n = seen_slugs.get(base, 0)
            seen_slugs[base] = n + 1
            tid = f"{base}_{n}" if n else base
            terms.append(
                {
                    "term_id": tid,
                    "label": title,
                    "layer": "A",
                    "evidence_chunk_ids": [uid],
                    "section_path": section_path,
                    "modeling_kind": mk,
                    "note": "Surface vocabulary + evidence link; not a promoted domain type.",
                }
            )

        if mk == "mechanic_rule":
            mechanisms_by_path[tuple(section_path)].append(
                {
                    "order": len(mechanisms_by_path[tuple(section_path)]) + 1,
                    "label": title or uid,
                    "evidence_chunk_id": uid,
                }
            )

        if mk == CANDIDATE_KIND and len(candidates) < cand_limit and title:
            candidates.append(
                {
                    "candidate_id": f"cand_{slug_label(title)}_{uid}",
                    "proposed_label": title,
                    "rationale": "Heuristic domain_rule_candidate; requires Phase 4 promotion gate before concepts[].",
                    "evidence_chunk_ids": [uid],
                    "section_path": section_path,
                    "modeling_kind": mk,
                    "promotion_status": "queued",
                }
            )

    mechanism_list: list[dict[str, object]] = []
    for path_key, steps in sorted(
        mechanisms_by_path.items(), key=lambda x: (len(x[0]), x[0])
    ):
        name = " / ".join(path_key) if path_key else "Mechanism"
        mid = slug_label(name)[:80]
        mechanism_list.append(
            {
                "mechanism_id": f"mec_{mid}_{len(mechanism_list)}",
                "name": name,
                "layer": "B",
                "steps": sorted(steps, key=lambda s: s["order"]),
                "note": "Named process with evidence anchors; not a class diagram.",
            }
        )

    generated = datetime.now(timezone.utc).isoformat()

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    terms_payload = {
        "schema_version": "v1",
        "generated_at": generated,
        "description": "Layer A — glossary terms (not concepts[]).",
        "count": len(terms),
        "terms": terms,
    }
    (OUT_DIR / "mm3_terms_layer.json").write_text(
        json.dumps(terms_payload, indent=2), encoding="utf-8"
    )

    mech_payload = {
        "schema_version": "v1",
        "generated_at": generated,
        "description": "Layer B — named mechanisms (workflows / rule clusters with evidence).",
        "count": len(mechanism_list),
        "mechanisms": mechanism_list,
    }
    (OUT_DIR / "mm3_mechanisms.json").write_text(
        json.dumps(mech_payload, indent=2), encoding="utf-8"
    )

    cand_payload = {
        "schema_version": "v1",
        "generated_at": generated,
        "description": "Candidate queue — possible future types; do not mint concepts[] without Phase 4 gate.",
        "count": len(candidates),
        "candidates": candidates,
        "cap_note": f"Listed first {cand_limit} domain_rule_candidate units with extractable titles (deterministic order by unit_id).",
    }
    (OUT_DIR / "mm3_candidate_queue.json").write_text(
        json.dumps(cand_payload, indent=2), encoding="utf-8"
    )

    summary = {
        "schema_version": "v1",
        "generated_at": generated,
        "inputs": {
            "context_index": str(INDEX.relative_to(ROOT)).replace("\\", "/"),
            "modeling_kind_sidecar": str(SIDECAR.relative_to(ROOT)).replace("\\", "/"),
        },
        "counts": {
            "terms": len(terms),
            "mechanisms": len(mechanism_list),
            "candidates": len(candidates),
        },
    }
    (OUT_DIR / "phase2_build_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )

    print("Wrote", OUT_DIR / "mm3_terms_layer.json", "terms=", len(terms))
    print("Wrote", OUT_DIR / "mm3_mechanisms.json", "mechanisms=", len(mechanism_list))
    print("Wrote", OUT_DIR / "mm3_candidate_queue.json", "candidates=", len(candidates))


if __name__ == "__main__":
    main()
