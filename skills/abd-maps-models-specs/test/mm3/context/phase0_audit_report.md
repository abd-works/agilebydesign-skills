# Phase 0 — Context readiness audit (MM3 fixture)

**Generated:** 2026-03-21 (orchestrated run; metrics from `scripts/phase0_audit.py`)  
**Inputs:** `test/mm3/context/context_index.json`, `test/mm3/context/chunks/unit_*.md`, `test/mm3/docs/HeroesHandbook.md`  
**Machine-readable metrics:** `phase0_audit_metrics.json`

---

## 0.1 Map the plumbing

| Question | Answer |
| -------- | ------ |
| **Unit ID → chunk file** | `forward_index` keys (`unit_NNNNN`) map **1:1** to `chunks/unit_NNNNN.md`. **725 / 725** present; **0** orphan index keys; **0** orphan files. |
| **Unit ID → `blk_*` block** | **Not** stored on `forward_index` rows. `excluded[]` holds **1408** `blk_*` entries **separately**. Join logic is **implicit** (generator knows mapping); **debt** for tooling that expects `block_id` on every unit—documented here. |
| **`reason` on units** | **Always missing** on `forward_index` (725× `(missing)`). Reasons exist only on **`excluded`** blocks (`structural heading only`, `below_min_chunk`, **etc.**). |
| **Version pin** | `HeroesHandbook.md` **SHA-256:** `30fc51215ffe9f1e076dd0d4713868c5d770f0bdc3f2fe3b7a83b0618501fed4` (see `phase0_audit_metrics.json`). Generator identity/version not embedded in index—**unknown**. |

---

## 0.2 Corpus profile (quantitative)

Summarized from `phase0_audit_metrics.json`:

| Metric | Value | Note |
| ------ | ----- | ---- |
| Forward units | 725 | Matches manifest `total_chunks` |
| Excluded blocks | 1408 | Not given chunk files |
| `evidence_type` (forward) | definition 345, domain-rule 289, example 59, variation/exception 19, mechanic 8, actor-action 5 | Usable stratification for gates |
| `document_region` | rules 700, examples 25 | |
| `structural_type` | paragraph 717, list 8 | |
| Excluded top types | metadata/noise 1295, domain-rule 105, actor-action 8 | Noise dominates excluded list |
| Excluded top reasons | structural heading only 1270, below_min_chunk 113, out_of_scope 23 | |
| `modeling_kind` on units | **0 / 725** | Confirms Phase 0.3 verdict |

---

## 0.3 Qualitative spot-check (prior art)

See **`phase0_3_spotcheck_report.md`**.

**Verdict (unchanged):** Metadata alone does **not** tell a modeler what **not** to subclass; add **`modeling_kind`** (or equivalent) and fill via rules + review or re-extraction.

---

## 0.4 Decision gate

| Criterion | Assessment |
| --------- | ---------- |
| IDs stable, chunk/index alignment | **Yes** — full coverage |
| Evidence types usable for stratification | **Partially** — `evidence_type` is coarse; **`reason`** absent on units |
| Clear “do not promote” without extra field | **No** — **`modeling_kind` required** |

**Decision:** **Adopt** current `chunks/` + `context_index.json` **and extend** the contract with **`modeling_kind`** (sidecar JSON or in-place schema change in Phase 1). **Do not** rebuild from source unless a later audit shows generator corruption—**not** indicated here.

**Next (Phase 1 entry):** `modeling_kind_sidecar.json` (heuristic v1) + validation script; then LLM batch or rules refinement on disputed buckets.

---

## Artifacts

| File | Role |
| ---- | ---- |
| `phase0_audit_metrics.json` | Automated counts + handbook hash |
| `phase0_3_spotcheck_report.md` | Qualitative verdict |
| `_phase0_spotcheck_sample.py` | Console sample (legacy) |
| `../phase0_iterations/ITERATION_LOG.md` | Run log + critic rounds |
