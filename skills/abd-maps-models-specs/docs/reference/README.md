# Reference material (gold map — human & critic-private)

Files here are **not** inputs to the **builder** or to **planner** output.

| File | Purpose |
|------|---------|
| `mm3-map-model-solution-reference.md` | Gold OO view. The **critic** may read it **only** to populate `private_gap_analysis` (optional). **Never** affects `overall_score` and **never** forwarded to the builder or orchestrator plans. |
| `mm3_target_ontology.json` | Human reference for types/relationships; not used for public scoring. |

**Public scoring** uses **only** `rules/mm3_domain_critic.json` **corpus_keywords** vs `HeroesHandbook.md` (see `docs/orchestrator.md`).
