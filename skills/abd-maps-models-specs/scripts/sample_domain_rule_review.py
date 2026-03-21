#!/usr/bin/env python3
"""Print sample units for manual review: domain_rule_candidate vs toc_or_nav_noise."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CTX = ROOT / "test" / "mm3" / "context"
SIDECAR = CTX / "modeling_kind_sidecar.json"
CHUNKS = CTX / "chunks"


def main() -> None:
    sc = json.loads(SIDECAR.read_text(encoding="utf-8"))
    units = sc["units"]
    by_kind: dict[str, list[str]] = {"domain_rule_candidate": [], "toc_or_nav_noise": []}
    for uid, row in units.items():
        k = row.get("modeling_kind")
        if k in by_kind:
            by_kind[k].append(uid)

    print("# Sample — domain_rule_candidate (first 12)")
    for uid in sorted(by_kind["domain_rule_candidate"])[:12]:
        rule = units[uid].get("heuristic_rule", "")
        p = CHUNKS / f"{uid}.md"
        preview = ""
        if p.is_file():
            body = p.read_text(encoding="utf-8")
            if body.startswith("---"):
                parts = body.split("---", 2)
                body = parts[2] if len(parts) >= 3 else body
            preview = body.strip().replace("\n", " ")[:160]
        print(f"- {uid}: {rule}\n  {preview}…")

    print("\n# Sample — toc_or_nav_noise from body signal (first 12 with 'body toc')")
    body_toc = [
        u
        for u in sorted(by_kind["toc_or_nav_noise"])
        if "body toc" in (units[u].get("heuristic_rule") or "")
    ]
    for uid in body_toc[:12]:
        rule = units[uid].get("heuristic_rule", "")
        p = CHUNKS / f"{uid}.md"
        preview = ""
        if p.is_file():
            body = p.read_text(encoding="utf-8")
            if body.startswith("---"):
                parts = body.split("---", 2)
                body = parts[2] if len(parts) >= 3 else body
            preview = body.strip().replace("\n", " ")[:160]
        print(f"- {uid}: {rule}\n  {preview}…")


if __name__ == "__main__":
    main()
