#!/usr/bin/env python3
"""Phase 0.1–0.2: corpus metrics + coverage for MM3 context_index.json."""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CTX = ROOT / "test" / "mm3" / "context"
INDEX = CTX / "context_index.json"
CHUNKS = CTX / "chunks"
HANDBOOK = ROOT / "test" / "mm3" / "docs" / "HeroesHandbook.md"
OUT_JSON = CTX / "phase0_audit_metrics.json"


def file_sha256(p: Path) -> str | None:
    if not p.is_file():
        return None
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    with open(INDEX, encoding="utf-8") as f:
        data = json.load(f)

    forward = data["forward_index"]
    excluded = data.get("excluded", [])
    manifest = data.get("manifest", {})

    unit_files = sorted(CHUNKS.glob("unit_*.md"))
    unit_keys = set(forward.keys())
    file_stems = {p.stem for p in unit_files}

    missing_files = sorted(unit_keys - file_stems)
    extra_files = sorted(file_stems - unit_keys)

    ets = Counter()
    reasons = Counter()
    regions = Counter()
    structural = Counter()
    mk_count = 0
    for uid, row in forward.items():
        ets[row.get("evidence_type") or "(missing)"] += 1
        reasons[row.get("reason") or "(missing)"] += 1
        regions[row.get("document_region") or "(missing)"] += 1
        structural[row.get("structural_type") or "(missing)"] += 1
        if row.get("modeling_kind"):
            mk_count += 1

    ex_ets = Counter(b.get("evidence_type") or "(missing)" for b in excluded)
    ex_reasons = Counter(b.get("reason") or "(missing)" for b in excluded)

    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "handbook_sha256": file_sha256(HANDBOOK),
        "context_index_path": str(INDEX.relative_to(ROOT)),
        "counts": {
            "forward_index_units": len(forward),
            "chunk_files_unit_md": len(unit_files),
            "excluded_blocks": len(excluded),
            "units_with_modeling_kind": mk_count,
        },
        "coverage": {
            "index_keys_without_chunk_file": missing_files[:50],
            "index_keys_without_chunk_file_count": len(missing_files),
            "chunk_files_without_index_key": extra_files[:50],
            "chunk_files_without_index_key_count": len(extra_files),
        },
        "forward_index": {
            "evidence_type": dict(ets),
            "reason": dict(reasons.most_common(20)),
            "document_region": dict(regions),
            "structural_type": dict(structural),
        },
        "excluded": {
            "evidence_type": dict(ex_ets.most_common(20)),
            "reason": dict(ex_reasons.most_common(20)),
        },
        "manifest_summary": {
            "sources": manifest.get("sources"),
            "section_counts_len": len(manifest.get("section_counts", {})),
            "evidence_type_counts": manifest.get("evidence_type_counts"),
            "total_chunks": manifest.get("total_chunks"),
            "excluded_count": manifest.get("excluded_count"),
        },
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)

    print("Wrote", OUT_JSON)
    print(json.dumps(out["counts"], indent=2))
    print("Coverage issues — missing files:", out["coverage"]["index_keys_without_chunk_file_count"])
    print("Coverage issues — extra files:", out["coverage"]["chunk_files_without_index_key_count"])


if __name__ == "__main__":
    main()
