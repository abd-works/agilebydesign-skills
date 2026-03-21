# Phase 3 — Behavioral story map

Aligned with [`plan/PROCESS-PLAN.md`](../plan/PROCESS-PLAN.md) **Phase 3**. Stories are **interactions** (actor → behavior → **anchor**), not a mirror of the type list in `map-model-spec.md`.

## Artifact

| Path | Purpose |
| ---- | -------- |
| `test/mm3/phase3/mm3_story_map.json` | Epics aligned to **bounded contexts** in `map-model-spec.md`; each story has `anchor` (`read` / `write` / `both`), `term_refs` into Phase 2, optional `evidence_chunk_ids`, optional `related_concept_hints` (strings only — **not** promotion). |

## Validation

```bash
python scripts/validate_phase3_story_map.py
```

Checks:

- Every story has `name`, `primary_actor`, `behavior`, `anchor` with valid `kind`.
- `anchor.read` / `anchor.write` present when required by `kind`.
- At least one of `term_refs` or `evidence_chunk_ids`.
- Each `term_id` exists in `test/mm3/phase2/mm3_terms_layer.json`.
- Each referenced `unit_*.md` exists under `test/mm3/context/chunks/`.

## Exit criterion (Phase 3)

Every story has a **clear behavioral reading** and **traceability** to glossary terms and/or evidence. **`related_concept_hints`** foreshadows Phase 4 types but does **not** create `concepts[]` rows.

## Relation to Phase 4

Promotion from **candidate queue** or **concept hints** to **`concepts[]`** uses the **Phase 4** reject gate only.
