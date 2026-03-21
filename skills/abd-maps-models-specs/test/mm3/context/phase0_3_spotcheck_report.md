# Phase 0.3 — Qualitative spot-check (MM3 fixture)

**Date:** 2026-03-21  
**Question:** From **metadata alone**, would a modeler know **what not to subclass**?  
**Verdict:** **No** — plan for **`modeling_kind`** (or equivalent) and **re-run / enrich** extraction; **happy to get there first**.

## What we have today

### `forward_index` (725 `unit_*.md` chunks)

| Signal | Present? | Enough for “don’t subclass this”? |
|--------|----------|-----------------------------------|
| `evidence_type` | Yes — `definition`, `domain-rule`, `example`, `variation/exception`, `mechanic`, `actor-action` | **Partially** — separates broad classes, but **`domain-rule` includes TOC junk and headings** (see `unit_00015`: “ABILITY RANKS … 107” with almost no prose). |
| `reason` (e.g. `structural heading only`) | **No** on forward_index — always missing | **No** — the `excluded` / `blk_*` list has `reason`, but **units** do not. |
| `structural_type`, `noise_score`, `modeling_priority` | Yes | **Partially** — useful for **retrieval**, not a **promotion gate** (“do not mint type”). |
| `candidate_concepts[]` | Yes | **Risk** — can **suggest** tokens (`ABILITY`, `RANKS`) that are **not** types; needs **`modeling_kind`** to avoid **auto-promotion**. |
| `modeling_kind` | **None** on any of 725 units | **No** |

### `excluded` (1408 `blk_*` blocks — separate list)

- Dominated by **`metadata/noise`** (1295) with reasons like **`structural heading only`** / **`below_min_chunk`** — good for **exclusion**, but this **does not** attach to the **725** primary units in a way a modeler sees in one place without joining logic.

## Spot samples (sanity)

- **`unit_00015`** (`domain-rule`): TOC-style fragment; **high** `modeling_priority` (0.85) despite **low** semantic value for typing — **priority ≠ “safe to subclass.”**
- **`definition`** chunks include **front matter** (e.g. **THIRD EDITION**) — **definition** label alone does not mean “core domain concept.”
- **`example`** and **`actor-action`** are sparse; still need **human** or **explicit** gate for promotion.

## Conclusion (aligned with PROCESS-PLAN Phase 0.3 → 1)

1. **Answer “no”** to: *metadata alone → know what not to subclass.*  
2. **Add** `modeling_kind` (or equivalent) on the **canonical** index (forward_index / chunk-index schema).  
3. **Fill** via rules + LLM batch + spot-check, or **re-run** extraction with **`modeling_kind`** in the contract.  
4. Keep **`evidence_type`** as a **weak** signal; **`modeling_kind`** is the **explicit** promotion / non-promotion gate.

*Script used: `test/mm3/context/_phase0_spotcheck_sample.py` (refresh counts if index changes).*
