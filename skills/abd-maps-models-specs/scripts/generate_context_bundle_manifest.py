#!/usr/bin/env python3
"""Emit context_bundle_manifest.json with SHA-256 of key artifacts."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CTX = ROOT / "test" / "mm3" / "context"
PHASE2 = ROOT / "test" / "mm3" / "phase2"
PHASE3 = ROOT / "test" / "mm3" / "phase3"
OUT = CTX / "context_bundle_manifest.json"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    files = [
        CTX / "context_index.json",
        CTX / "modeling_kind_sidecar.json",
        CTX / "phase0_audit_metrics.json",
    ]
    artifacts: dict[str, object] = {}
    for p in files:
        if p.is_file():
            rel = p.relative_to(CTX).as_posix()
            artifacts[rel] = {"sha256": sha256_file(p), "bytes": p.stat().st_size}
        else:
            artifacts[p.name] = {"missing": True}

    phase2_artifacts: dict[str, object] = {}
    for name in (
        "mm3_terms_layer.json",
        "mm3_mechanisms.json",
        "mm3_candidate_queue.json",
        "phase2_build_summary.json",
    ):
        p = PHASE2 / name
        if p.is_file():
            rel = f"test/mm3/phase2/{name}"
            phase2_artifacts[rel] = {
                "sha256": sha256_file(p),
                "bytes": p.stat().st_size,
            }

    phase3_artifacts: dict[str, object] = {}
    p3 = PHASE3 / "mm3_story_map.json"
    if p3.is_file():
        phase3_artifacts["test/mm3/phase3/mm3_story_map.json"] = {
            "sha256": sha256_file(p3),
            "bytes": p3.stat().st_size,
        }

    payload = {
        "schema_version": "v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "context_root": str(CTX.relative_to(ROOT)).replace("\\", "/"),
        "artifacts": artifacts,
        "phase2": phase2_artifacts if phase2_artifacts else None,
        "phase3": phase3_artifacts if phase3_artifacts else None,
    }
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print("Wrote", OUT)


if __name__ == "__main__":
    main()
