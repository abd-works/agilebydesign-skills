# Critic round 2 — `modeling_kind` heuristics (independent subagent)

## Verdict

Kind labels are **coarse but sensible**; **not trustworthy as hard promotion gates** in v1. **266 `domain_rule_candidate`** means “upstream said `domain-rule` and TOC exception didn’t fire”—not “validated substantive rule.” Treat v1 as **telemetry + obvious-noise triage**, not “safe to promote.”

## Critical flaws

1. **TOC handling brittle** — Dots in path/tags + `span <= 6` only for `domain-rule`. False negatives: TOC without dot leaders or span > 6. False positives: accidental dot runs.
2. **Cascade over upstream labels** — No body text; wrong `evidence_type` → wrong kind.
3. **`ambiguous_review` = 0** — No visible “needs human” bucket from uncertainty.
4. **`editorial_or_credit` toy** — Hard-coded strings; 1 hit on this book.
5. **`narrative_example` over-broad** — `document_region == examples` without content check.
6. **`domain_rule_candidate` name overpromises** — Really “default domain-rule,” not reviewed candidate.

## Fix first

1. TOC: add **content** signals (line patterns, token density), revisit `span <= 6`.
2. Force **`ambiguous_review`** when `evidence_type` missing/unknown; split **upstream-labeled** vs **heuristic** in naming or docs.
3. **Do not** use `domain_rule_candidate` as approval for promotion—only **review queue** until LLM/second pass.

## OK to ship as v1 stub?

**Yes** for exploration, counts, manual review — **if** gates do not treat buckets as approval. **No** as sole automated minting gate without LLM/re-extract.
