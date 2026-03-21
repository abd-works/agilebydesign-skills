"""Phase 0.3 spot-check: sample forward_index + compare to excluded blocks."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent

with open(ROOT / "context_index.json", encoding="utf-8") as f:
    data = json.load(f)

forward = data["forward_index"]
excluded = data.get("excluded", [])

print("=== forward_index (chunk-level) ===")
print("unit entries:", len(forward))
sample_u = list(forward.values())[0]
print("keys per unit:", sorted(sample_u.keys()))

# aggregate evidence_type / reason if present
ets, rs = Counter(), Counter()
for u in forward.values():
    ets[u.get("evidence_type") or "(missing)"] += 1
    rs[u.get("reason") or "(missing)"] += 1
print("\nevidence_type:", ets.most_common(15))
print("reason:", rs.most_common(15))
has_mk = sum(1 for u in forward.values() if u.get("modeling_kind"))
print("units with modeling_kind:", has_mk, "/", len(forward))

print("\n=== Sample forward_index rows (metadata only) ===\n")
# stratify by evidence_type
by_et = {}
for uid, u in forward.items():
    by_et.setdefault(u.get("evidence_type") or "(missing)", []).append((uid, u))

shown = 0
for et in sorted(by_et.keys(), key=str):
    for uid, u in by_et[et][:3]:
        print(f"{uid} | evidence_type={et!r} reason={u.get('reason')!r}")
        print(f"  section_path: {(u.get('section_path') or [])[:4]}...")
        print(f"  modeling_kind: {u.get('modeling_kind')!r}")
        pv = (u.get("text_preview") or u.get("preview") or "")[:180].replace("\n", " ")
        print(f"  preview: {pv!r}")
        print()
        shown += 1
        if shown >= 15:
            break
    if shown >= 15:
        break

print("=== excluded blocks (blk_*) — separate list ===")
print("excluded count:", len(excluded))
if excluded:
    et2 = Counter(b.get("evidence_type") for b in excluded)
    print("excluded evidence_type:", et2.most_common(10))
