# Phase 2 — Terms, mechanisms, candidate queue

Aligned with [`plan/PROCESS-PLAN.md`](../plan/PROCESS-PLAN.md) **Phase 2**. These artifacts exist **before** sparse `concepts[]` in `map-model-spec.md`.

## Artifacts (`test/mm3/phase2/`)

| File | Layer | Purpose |
| ---- | ----- | -------- |
| `mm3_terms_layer.json` | **A** | Glossary-style **terms**: label + `evidence_chunk_ids` + `modeling_kind`. Not classes. |
| `mm3_mechanisms.json` | **B** | **Named mechanisms**: grouped `mechanic_rule` units by `section_path`, each step points at a chunk. |
| `mm3_candidate_queue.json` | Queue | **`domain_rule_candidate`** rows with extractable titles (capped); **not** promoted types. |
| `phase2_build_summary.json` | — | Counts and input pointers for the last build. |

## How they are built

```bash
python scripts/build_phase2_artifacts.py
python scripts/generate_context_bundle_manifest.py   # includes phase2 hashes when present
```

Inputs: `context/context_index.json`, `context/modeling_kind_sidecar.json`, `context/chunks/unit_*.md`.

## Promotion rule (exit criterion for Phase 2)

- **`terms[]`** and **`mechanisms[]`** do **not** authorize new rows in **`concepts[]`**.
- **`candidate_queue[]`** entries move to **`concepts[]`** only through **Phase 4** — explicit promotion criteria, evidence, and reject gate (“not just a property on a broader type”).
- The **`modeling_kind` sidecar** remains **heuristic**: it informs triage; it is **not** automatic approval for typing.

## Relation to Phase 3+

Story maps (Phase 3) may **reference** terms by id or label. Domain types (Phase 4) **consume** a subset of candidates after review—not the whole queue.
