#!/usr/bin/env python3
"""
MM3 domain critic — public scores from first principles only (rules + corpus).

- **Scoring:** Each invariant uses `corpus_keywords` against HeroesHandbook.md (or index
  fallback). `model_keywords` in rules are **not** used for `overall_score` (they are
  hints for humans / optional gap analysis).

- **Gold reference (optional):** With `--gold-map`, the critic may **read** the reference
  map to produce a **private** `private_gap_analysis` block (why a candidate may diverge).
  That block is **never** merged into `recommendations` and must not be fed to the builder
  or orchestrator plans — use `sanitize_critic_for_downstream()` or read only the keys
  returned by `public_critic_view()`.

Environment:
  CRITIC_GOLD_MAP — optional default path to gold reference markdown (orchestrator may set).
"""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULES = ROOT / "rules" / "mm3_domain_critic.json"
DEFAULT_GOLD_MAP = ROOT / "docs" / "reference" / "mm3-map-model-solution-reference.md"
CTX = ROOT / "test" / "mm3" / "context"
INDEX = CTX / "context_index.json"
HANDBOOK = ROOT / "test" / "mm3" / "docs" / "HeroesHandbook.md"


def _read_text(p: Path, limit: int | None = None) -> str:
    if not p.is_file():
        return ""
    t = p.read_text(encoding="utf-8", errors="replace")
    if limit and len(t) > limit:
        return t[:limit]
    return t


def _score_invariant_corpus_only(inv: dict, corpus_text: str) -> dict:
    """First-principles score: corpus_keywords vs handbook/index only."""
    ck = inv.get("corpus_keywords") or []
    corpus_hits = sum(1 for k in ck if k and re.search(re.escape(k), corpus_text, re.I))
    cscore = min(1.0, corpus_hits / max(len(ck), 1)) if ck else 0.0
    combined = cscore
    status = "pass" if combined >= 0.4 else "warn" if combined >= 0.15 else "fail"
    return {
        "id": inv["id"],
        "severity": inv.get("severity", "medium"),
        "summary": inv.get("summary", ""),
        "status": status,
        "score": round(combined, 3),
        "corpus_keyword_hits": corpus_hits,
        "scoring_basis": "corpus_only",
    }


def _private_gap_analysis(
    rules: dict,
    gold_text: str,
    candidate_text: str,
) -> dict:
    """
    Critic-only: compare reference map to candidate using rule keywords.
    Does not affect overall_score. Not for builder/planner consumption.
    """
    gaps: list[dict] = []
    for inv in rules.get("invariants", []):
        mids = inv.get("model_keywords") or []
        for k in mids:
            if not k:
                continue
            if k in gold_text and k not in candidate_text:
                gaps.append({"invariant_id": inv["id"], "term": k})
    return {
        "visibility": "critic_only",
        "do_not_feed_builder_or_planner": True,
        "summary": "Reference map contains these invariant-related terms not found in candidate (diagnostic only).",
        "reference_terms_missing_in_candidate": gaps[:80],
    }


def public_critic_view(result: dict) -> dict:
    """Subset safe for orchestrator plans, remote planner, and builder-facing logs."""
    out = {k: v for k, v in result.items() if k != "private_gap_analysis"}
    return out


def run_critic(
    *,
    candidate_model_paths: list[Path],
    pipeline_ok: bool,
    gold_map_path: Path | None,
) -> dict:
    rules = json.loads(RULES.read_text(encoding="utf-8"))
    corpus_text = _read_text(HANDBOOK, limit=1_200_000)
    if not corpus_text:
        corpus_text = _read_text(INDEX, limit=400_000)

    invariants = []
    scores = []
    for inv in rules.get("invariants", []):
        r = _score_invariant_corpus_only(inv, corpus_text)
        invariants.append(r)
        scores.append(r["score"])

    overall = sum(scores) / max(len(scores), 1) if scores else 0.0
    if not pipeline_ok:
        overall *= 0.5

    rec: list[str] = []
    for r in invariants:
        if r["status"] == "fail":
            rec.append(f"Corpus alignment weak for: {r['id']} — {r['summary'][:120]}")
    if not pipeline_ok:
        rec.append("Fix pipeline (audit / heuristics / validate) before trusting scores.")
    rec.extend((rules.get("notes_for_automated_critic") or [])[:3])

    result: dict = {
        "schema_version": "2",
        "evaluation_mode": "corpus_first_principles",
        "overall_score": round(min(1.0, overall), 3),
        "pipeline_ok": pipeline_ok,
        "invariants": invariants,
        "recommendations": rec,
    }

    gold_text = ""
    if gold_map_path and gold_map_path.is_file():
        gold_text = _read_text(gold_map_path, limit=500_000)

    candidate_text = ""
    for mp in candidate_model_paths:
        if mp.is_file():
            candidate_text += "\n" + _read_text(mp, limit=500_000)

    if gold_text.strip() and candidate_text.strip():
        result["private_gap_analysis"] = _private_gap_analysis(rules, gold_text, candidate_text)
    elif gold_text.strip():
        result["private_gap_analysis"] = {
            "visibility": "critic_only",
            "do_not_feed_builder_or_planner": True,
            "summary": "Gold reference read; no candidate --model provided — no term-level gap list.",
        }

    return result


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument(
        "--model",
        action="append",
        default=[],
        metavar="PATH",
        help="Optional builder **candidate** map (repeatable). Used only for private_gap_analysis vs --gold-map, not for scoring.",
    )
    ap.add_argument(
        "--gold-map",
        type=Path,
        default=None,
        metavar="PATH",
        help="Optional gold reference markdown (default: env CRITIC_GOLD_MAP or docs/reference/mm3-map-model-solution-reference.md). Never affects overall_score.",
    )
    ap.add_argument(
        "--pipeline-ok",
        action="store_true",
        help="Mark pipeline as green for scoring multiplier",
    )
    ap.add_argument("--json-out", type=Path, help="Write full critic JSON (includes private_gap_analysis when present)")
    ap.add_argument(
        "--json-out-public",
        type=Path,
        help="Optional: write sanitized JSON (no private_gap_analysis) for downstream tools",
    )
    args = ap.parse_args()

    gold = args.gold_map
    if gold is None:
        env_g = os.environ.get("CRITIC_GOLD_MAP", "").strip()
        gold = Path(env_g) if env_g else DEFAULT_GOLD_MAP

    paths = [Path(p) for p in args.model]
    out = run_critic(candidate_model_paths=paths, pipeline_ok=args.pipeline_ok, gold_map_path=gold)

    pub = public_critic_view(out)
    print("overall_score:", pub["overall_score"])
    print("pipeline_ok:", pub["pipeline_ok"])
    print("evaluation_mode:", pub.get("evaluation_mode"))
    for inv in pub["invariants"]:
        print(f"  {inv['id']}: {inv['status']} ({inv['score']})")
    if "private_gap_analysis" in out:
        print("(private_gap_analysis present — omit from planner/builder)")

    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(out, indent=2), encoding="utf-8")
        print("Wrote", args.json_out)
    if args.json_out_public:
        args.json_out_public.parent.mkdir(parents=True, exist_ok=True)
        args.json_out_public.write_text(json.dumps(pub, indent=2), encoding="utf-8")
        print("Wrote public view", args.json_out_public)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
