# `modeling_kind` sidecar (v1 file, **v2** heuristics)

**Location:** `test/mm3/context/modeling_kind_sidecar.json`  
**Producer:** `scripts/apply_modeling_kind_heuristics.py` (`heuristic_version` **v2**: reads chunk **body** for dot-leader TOC / index walls, not only `section_path` + short span)  
**Validator:** `scripts/validate_modeling_kind_sidecar.py` (optional `--golden` → `modeling_kind_heuristic_golden.json`)  
**JSON Schema:** `docs/schemas/modeling_kind_sidecar.schema.json`

## Purpose

`forward_index` rows did not carry **`modeling_kind`**; Phase 0.3 concluded metadata alone cannot gate promotion. The sidecar assigns a **coarse** bucket per **`unit_id`** without editing the 52k-line `context_index.json` yet.

## Kind values (v1)

| Kind | Intent |
| ---- | ------ |
| `toc_or_nav_noise` | TOC / chapter pointer lines — **do not** mint types from appearance alone |
| `editorial_or_credit` | Front matter / credits |
| `narrative_example` | Worked examples — bind to **story** before types |
| `behavioral_interaction` | `actor-action` slices |
| `mechanic_rule` | Mechanic/process chunks |
| `variation_rule` | `variation/exception` |
| `definition_candidate` | Definitions — **term** promotion path |
| `domain_rule_candidate` | Substantive `domain-rule` text (per upstream label + TOC heuristics)—**not** approval to mint types; **review queue** only |
| `ambiguous_review` | Fallback (v1 run: **0** hits) |

Each unit entry includes `heuristic_rule` (trace of which branch fired) and optional `heuristic_version` on each unit matching the payload.

**Regression:** `test/mm3/context/modeling_kind_heuristic_golden.json` snapshots `kinds_distribution` for v2; run `python scripts/validate_modeling_kind_sidecar.py --golden` after heuristic changes (update golden when the change is intentional).

## Not done in v1

- No merge into `context_index.json`
- No LLM review of borderline **`domain_rule_candidate`**
- **`candidate_concepts[]`** not reweighted by kind

## See also

- `test/mm3/context/phase0_audit_report.md`
- `plan/PROCESS-PLAN.md` Phase 1
