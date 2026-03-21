#!/usr/bin/env python3
"""Emit context_bundle_manifest.json with SHA-256 of key artifacts."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CTX = ROOT / "test" / "mm3" / "context"
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

    payload = {
        "schema_version": "v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "context_root": str(CTX.relative_to(ROOT)).replace("\\", "/"),
        "artifacts": artifacts,
    }
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print("Wrote", OUT)


if __name__ == "__main__":
    main()
