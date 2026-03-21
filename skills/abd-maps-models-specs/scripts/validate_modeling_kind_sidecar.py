#!/usr/bin/env python3
"""Validate modeling_kind_sidecar.json against forward_index."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CTX = ROOT / "test" / "mm3" / "context"
INDEX = CTX / "context_index.json"
SIDECAR = CTX / "modeling_kind_sidecar.json"
GOLDEN_DEFAULT = CTX / "modeling_kind_heuristic_golden.json"

# Keep in sync with apply_modeling_kind_heuristics.py KINDS / classifier outputs
ALLOWED_KINDS = frozenset(
    {
        "toc_or_nav_noise",
        "editorial_or_credit",
        "narrative_example",
        "behavioral_interaction",
        "mechanic_rule",
        "variation_rule",
        "definition_candidate",
        "domain_rule_candidate",
        "ambiguous_review",
    }
)


def _compare_golden(sc: dict, golden_path: Path) -> tuple[bool, list[str]]:
    """Return (ok, messages) comparing kinds_distribution to golden file."""
    msgs: list[str] = []
    if not golden_path.is_file():
        return False, [f"golden file missing: {golden_path}"]
    g = json.loads(golden_path.read_text(encoding="utf-8"))
    g_ver = g.get("heuristic_version")
    s_ver = sc.get("heuristic_version")
    if g_ver and s_ver and g_ver != s_ver:
        msgs.append(f"heuristic_version mismatch: sidecar={s_ver!r} golden={g_ver!r}")
    g_dist = g.get("kinds_distribution") or {}
    s_dist = sc.get("kinds_distribution") or {}
    if not g_dist:
        return False, msgs + ["golden kinds_distribution empty"]
    all_keys = sorted(set(g_dist) | set(s_dist))
    for k in all_keys:
        gv, sv = g_dist.get(k), s_dist.get(k)
        if gv != sv:
            msgs.append(f"kinds_distribution[{k!r}]: sidecar={sv} golden={gv}")
    ok = not msgs
    return ok, msgs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--golden",
        nargs="?",
        const=str(GOLDEN_DEFAULT),
        default=None,
        metavar="PATH",
        help=f"Compare kinds_distribution to golden (default: {GOLDEN_DEFAULT.name})",
    )
    args = ap.parse_args()

    with open(INDEX, encoding="utf-8") as f:
        fwd = json.load(f)["forward_index"]
    with open(SIDECAR, encoding="utf-8") as f:
        sc = json.load(f)

    units = sc["units"] if isinstance(sc.get("units"), dict) else sc

    keys_f = set(fwd.keys())
    keys_s = set(units.keys())

    missing = sorted(keys_f - keys_s)
    extra = sorted(keys_s - keys_f)
    empty = [u for u, v in units.items() if not (v or {}).get("modeling_kind")]

    bad_kind = [
        u
        for u, v in units.items()
        if (v or {}).get("modeling_kind") not in ALLOWED_KINDS
    ]

    ok = not missing and not extra and not empty and not bad_kind
    print("forward_index:", len(keys_f))
    print("sidecar keys:", len(keys_s))
    print("missing in sidecar:", len(missing))
    print("extra in sidecar:", len(extra))
    print("empty modeling_kind:", len(empty))
    print("modeling_kind not in enum:", len(bad_kind))
    if bad_kind[:5]:
        print("sample bad:", bad_kind[:5])
    if missing[:5]:
        print("sample missing:", missing[:5])
    if extra[:5]:
        print("sample extra:", extra[:5])

    if args.golden is not None:
        gpath = Path(args.golden)
        g_ok, g_msgs = _compare_golden(sc, gpath)
        print("golden check:", gpath.name, "OK" if g_ok else "FAIL")
        for m in g_msgs[:30]:
            print(" ", m)
        if len(g_msgs) > 30:
            print(f"  ... and {len(g_msgs) - 30} more")
        ok = ok and g_ok

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
