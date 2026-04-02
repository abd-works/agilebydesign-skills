# Class diagram from `map-model-spec.json`

**When:** During **process phases 4–9** (terms & mechanisms through integrate), whenever you have **materially updated** the domain model in **`map-model-spec.json`**, re-run the generator so the **class diagram file** beside your spec stays aligned with promoted concepts, modules, and **`depends_on`**.

This is **human visualization**, not validation: Phase **10** (**validate**) still relies on **`python scripts/build.py`** and rule-bound scanners.

---

## Command (skill package)

From the **abd-maps-models-specs** root (directory that contains `scripts/` and `skill-config.json`), with **`conf/abd-config.json`** pointing at the workspace that contains **`solution.conf`**:

```bash
python scripts/render_map_model_class_diagram.py
```

- **Input:** `<output_dir>/map-model-spec.json` (see [`domain-model.md`](domain-model.md) and your workspace `solution.conf`).
- **Output:** `<output_dir>/map-model-class-diagram.drawio` — **native diagrams.net XML** (same **`mxfile` / `mxCell`** stack as agile_bots story-map Draw.io), with modules, concepts, members, and **`depends_on`** edges.

**Prerequisite:** `conf/abd-config.json` must include **`agile_bots_root`** (absolute path to the **agile_bots** repo), or set environment variable **`AGILE_BOTS_ROOT`**. The skill invokes `agile_bots/scripts/render_map_model_drawio.py`.

Optional path override:

```bash
python scripts/render_map_model_class_diagram.py --output path/to/custom-name.drawio
```

Re-running the command **replaces** that file; any layout you applied in diagrams.net is **not** tracked by this skill.

---

## Open in diagrams.net

Open **`map-model-class-diagram.drawio`** in VS Code (Draw.io extension), diagrams.net desktop, or **app.diagrams.net** → **File → Open from…** — no Mermaid import step.

---

## Relationship to other tooling

- **agile_bots** **crc_bot** can emit **diagrams from `story-graph.json`** domain concepts — a **different** source than **`map-model-spec.json`**. For **this** skill’s published spec, use **`render_map_model_class_diagram.py`** so the diagram tracks **`modules_and_epics`** and **`depends_on`** in **`map-model-spec.json`** (rendered via **`synchronizers.story_io.map_model_spec_drawio`**).
- **Story graph** outline/increment diagrams from the story-bot pipeline are **not** this artifact.

---

## Cadence

| Phase slug | Process # | After you… |
|------------|-------------|------------|
| `terms-mechanisms` | 4 | Change terms/mechanisms that affect how you think about types (optional diagram; types may not exist yet). |
| `shaped-story-map` | 5 | Extend or reshape stories that drive promotion (optional). |
| `domain-types` | 6 | Add or promote **`concepts[]`** — **re-run the command** when the promoted set changes. |
| `variant-classification` | 7 | Change variant strategy affecting type shape — refresh when useful. |
| `deepen` | 8 | Add **`depends_on`**, properties, operations — **re-run** so edges and members update. |
| `integrate` | 9 | Merge or drain queue into final spec — **re-run** before handoff. |

Minimum practical habit: run the command **after** **`domain-types`** when concepts exist, and **again after `deepen` or `integrate`** when collaboration edges change.
