# Autonomous orchestrator (builder / runner / critic)

## Roles

| Role | Script responsibility | What it sees |
| ---- | ---------------------- | ------------ |
| **1 — Planner** | `orchestrator_loop.py` | Writes `plans/plan_NNN.md` from **deterministic** templates or `ORCHESTRATOR_AGENT_URL`. Receives **public** critic output only (no `private_gap_analysis`). |
| **2 — Runner (builder)** | same | `phase0_audit` → `apply_modeling_kind_heuristics` → `validate` (--golden) → `generate_context_bundle_manifest`. **Does not** read `docs/reference/*` gold map. |
| **3 — Critic (evaluator)** | `critic_mm3_domain.py` | **Public score:** `rules/mm3_domain_critic.json` invariants vs **HeroesHandbook.md** (corpus / first principles). **Optional:** `--gold-map` + `--model` (candidate) add **`private_gap_analysis`** in the JSON for humans — **never** fed to planner or builder. |

## One-command loop

```bash
cd skills/abd-maps-models-specs
python scripts/orchestrator_loop.py --min-iterations 10 --max-iterations 20 --stop-on-score 0.92
```

- **`--gold-map PATH`** — default: `docs/reference/mm3-map-model-solution-reference.md` if present. Used only for **private** gap notes vs candidate; **does not change** `overall_score`.
- **`--critic-model PATH`** — optional builder **candidate** map (repeatable). Used only for private gap analysis, not for scoring.

**Horizon:** “10–20” means **iterations**, not calendar time.

## Evaluator contract

1. **`overall_score`** = corpus alignment to invariants (**no** keyword-matching against the gold map).
2. **Gold map** may be read **inside** the critic process to explain **why** a candidate diverges (`private_gap_analysis`). That block is **not** copied into `recommendations` and is **stripped** before deterministic plans and before POSTing to `ORCHESTRATOR_AGENT_URL`.
3. **Remote planner** receives the same **public** critic view as the local planner.

## Optional HTTP API

Set **`ORCHESTRATOR_AGENT_URL`**. Payload includes **sanitized** critic JSON (no `private_gap_analysis`).

## Artifacts

| Path | Purpose |
| ---- | ------- |
| `test/mm3/orchestration/critic/critic_NNN.json` | Full critic output (may include `private_gap_analysis` for human review) |
| `test/mm3/orchestration/plans/plan_NNN.md` | Planner — **public** inputs only |

## See also

- `docs/reference/README.md` — gold map / ontology (human reference, not builder input)
- `plan/PROCESS-PLAN.md`
- `docs/modeling_kind_sidecar_v1.md`
