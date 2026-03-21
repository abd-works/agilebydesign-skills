# abd-maps-models-specs — reusable process plan

*Working plan — lives in `plan/` (transient). Long-lived reference docs belong in `docs/`.*

This plan describes a **repeatable** path from **source markdown** through **evidence**, **vocabulary layers**, **behavioral stories**, and **sparse domain types**, to a **validated** map / model / spec. It is written so principles can be **argued on merit**: each has **stated grounding** (research and established practice), not reactions to any prior attempt.

**Fixture in scope:** `skills/abd-maps-models-specs/test/mm3/` — `HeroesHandbook.md`, `context/chunks/`, `context/context_index.json`.

---

## Principles we commit to (positive)

These are **normative**: we implement the process **because** of them. If evidence shows a principle is wrong for a domain, **change the principle** (and this document)—do not silently bend the process.


| Principle                                   | Grounding (research / practice)                                                                                                                                                                                                        | What we commit to                                                                                                                                                                                                                                                                                                                                             | Outcomes we want                                                                                  | States we avoid                                                                                                                                          |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Provenance-first evidence**               | Traceability in requirements engineering (e.g. IEEE-style bidirectional trace); evidence-based methods in policy and safety-critical domains; DDD emphasis on **distilling** the model **from** the source, not inventing ahead of it. | **Two separate moves:** (1) **Evidence** ties claims to **where** they come from (`chunk_id` / anchors). (2) **Promotion** decides **what** they become—term, mechanism, story, property, enum, type, relationship—using **that layer’s** criteria. Citations are **necessary** for substantive choices; they are **not sufficient** to mint a class or edge. | Same links can support honest **layering**; traceability without **automatic** typing.            | Treating “cited here” as “therefore a `concepts[]` row”; skipping promotion because traceability already passed.                                         |
| **Behavioral description of value**         | Use-case and scenario modeling (e.g. Jacobson); story mapping (Patton); realized **through** **story maps**, **stories**, and **story specifications** (BDD-style **when/then** scenarios).                                            | **Stories** are **interactions**: primary **actor** performs an **operation** on a **subject** in the domain. **Anchor** each story: **what** state (or read model / projection) the interaction **uses** or **changes** (and name **policy/SLO** only when it is part of the spec for that story—not a separate mandatory template in *this* process). Distinguish **mutation** of authoritative domain state vs **observation**—**reads**, **pass-through**, **forward**, **query** all count; not every story implies an aggregate **write**. **When/then** still asserts something **verifiable** (including observable reads or effects). Optional secondary actors. Structure lives in the **story map**; the written **spec** is scenarios / when-then / AC on each story. | Maps that read as **capability**, not noun lists; one clear behavioral lane (map → story → spec). | Stories that are only labels, tables, or ungrounded fragments; **extra** behavioral write-ups that **duplicate** map/story/spec without a stated reason. |
| **Layered vocabulary**                      | Ontology engineering: **terms** vs **classes**; DDD **ubiquitous language** vs **model**; separation of **glossary** from **type system**.                                                                                             | **Terms** and **named mechanisms** (processes, lifecycles) live in **their own** artifacts; **domain types** are promoted **only** through the type gate—not by renaming a mention.                                                                                                                                                                           | Shared language; controlled growth of types; **distinct** promotion paths per layer.              | One-step “surface word → class” without a **separate** promotion decision.                                                                               |
| **Sparse, intentional domain types**        | Classic OO/domain modeling: types for things with **identity**, **lifecycle**, and **distinct** responsibilities (Evans, Rumbaugh-style information modeling).                                                                         | `concepts[]` holds **types** only where the problem space needs **separate** behavioral/state contracts; otherwise properties, enums, or terms.                                                                                                                                                                                                               | Small, explainable type system; composition where it fits.                                        | Unbounded type list; duplicate abstractions differing only by name.                                                                                      |
| **Justified specialization**                | Liskov substitutability: subtyping where **substitution** is meaningful in the **operations** that matter.                                                                                                                             | `extends` (or equivalent) only where specialization is **semantically** warranted and **checked** against use.                                                                                                                                                                                                                                                | Predictable hierarchies; safe generalization.                                                     | Decorative inheritance; “is-a” from layout or co-occurrence alone.                                                                                       |
| **Explicit variant representation**         | Analysis patterns: **enumeration** vs **classification hierarchy** (Fowler et al.); domain-driven choice per **family** of variation.                                                                                                  | For each variant family, record the **decision**: enum vs subtypes vs other, **before** mass property assignment.                                                                                                                                                                                                                                             | Consistent representation; fewer migration surprises.                                             | Defaulting to inheritance because it is fewer JSON fields.                                                                                               |
| **Corpus understanding before type design** | Qualitative coding / corpus profiling; information architecture of large documents.                                                                                                                                                    | **Phase 0** produces **metrics and samples** on the evidence base **before** committing to chunk/index shape or to a full type set.                                                                                                                                                                                                                           | Right grain of evidence; prioritized reading; defensible gates.                                   | Modeling before knowing what the source actually contains.                                                                                               |


**Rule (cross-cutting):** **Where** something is anchored (evidence) and **what** it is in the model (term, story, property, type, …) are **different states**. The process may reuse the same `chunk_id` in more than one layer; each layer applies its own gate.

**Rule (behavioral anchoring):** A story need not **mutate** core domain state; it must be **anchored**—**which** state or projection is **read**, **passed**, or **forwarded**, **or** **which** state is **written**, **or** **which** constraint/SLO applies. **Read** and **write** paths are both **first-class**; silence on anchor is not.

**How to attack a principle:** Bring **counterexamples** from a domain, or **citations** that the grounding does not hold; then **revise** the table and the phases below in the same edit.

---

## A. Current fixture inventory


| Asset                                 | Role                                                                                                                             |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `test/mm3/docs/HeroesHandbook.md`     | Canonical **source** markdown for the MM3 fixture (pin version when it changes).                                                 |
| `test/mm3/context/chunks/unit_*.md`   | **Evidence units** — text + stable IDs for citation.                                                                             |
| `test/mm3/context/context_index.json` | Index: **manifest** (sources, section counts) + **blocks** with `block_id`, `section_path`, `reason`, `evidence_type`, previews. |


**Phase 0** decides whether this **evidence package** satisfies the **context contract** we need, or whether **chunking and indexing** should be **redefined** from `HeroesHandbook.md` under explicit rules (same principles; fresh artifacts).

---

## Phase 0 — Context readiness audit

**Goal:** Decide whether the **current** `context_index.json` + `chunks/` **implement the context contract** we need, or whether **chunking and indexing** should be **rebuilt** from `HeroesHandbook.md` under explicit rules.

This phase is **analysis-first**. Deliverables are **documents + metrics**, not a full model.

### 0.1 Map the plumbing

1. **ID mapping** — Document how `unit_*.md` relates to `blk_*` in `context_index.json` (one-to-one, many-to-one, naming convention). If the link is implicit or missing, **record that as debt**.
2. **Coverage** — Does every chunk file appear in the index? Does every **domain-relevant** block have a chunk (or explicit exclusion)?
3. **Version pin** — Hash or date for `HeroesHandbook.md` and for the **generator** that produced the index (if known).

### 0.2 Corpus profile (quantitative)

Produce a **short report** (markdown or JSON summary):


| Metric                                      | Why it matters                                                                                                                                  |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Count of chunks / blocks by `evidence_type` | See if “noise” vs “rule” vs “example” is usable for **promotion gates**.                                                                        |
| Distribution of `reason`                    | e.g. `structural heading only`, `below_min_chunk` — assess whether chunk **grain** matches **semantic** use (definitions vs noise vs examples). |
| Section path depth / chapter spread         | For **stratified sampling** (high-signal chapters first).                                                                                       |
| % blocks flagged `metadata/noise`           | Informs whether **modeling_kind** is already there or must be **re-inferred**.                                                                  |


### 0.3 Qualitative spot-check

- Sample **N** chunks across chapters: definitions, tables, examples, rule blocks.
- Ask: **Would a modeler** know, from metadata alone, what **not** to subclass? If **no**, Stage 1 must add `modeling_kind` (or equivalent) — either **fill** from existing fields or **re-run** extraction.

### 0.4 Decision gate


| Outcome                                                                            | Action                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sufficient** — IDs stable, evidence types usable, mapping clear                  | **Adopt** current chunks + index; **extend** schema (e.g. `modeling_kind`, `modeling_priority`) in place or via sidecar JSON.                                                          |
| **Insufficient** — noisy blocks dominate, chunk/blocks misaligned, or IDs unusable | **Restart context from source**: define **chunking rules** from `HeroesHandbook.md` (heading boundaries, min size, table handling), regenerate chunks + index, **version** the bundle. |


This gate is where a **deliberate** rebuild of context happens if the audit says so.

---

## Phase 1 — Canonical context layer (after Phase 0 is accepted or rebuilt)

**Goal:** A **single, versioned** contract for “what evidence is,” independent of map/model/spec JSON.

### 1.1 Artifacts

- `chunk-index.json` (or evolved `context_index.json`) with at minimum: `chunk_id`, `source_anchor`, `modeling_kind`, `evidence_type`, `modeling_priority`, optional `candidate_terms[]`.
- **Rules:** `example` / `narrative_aside` / `metadata/noise` **cannot** promote to `extends` or `concepts[]` without a **promotion** record.

### 1.2 Validation

- Script: every file under `chunks/` has index row; every index row has a file (or documented orphan).
- **Relationship edges** (e.g. `extends`, `inherits`) enter the model only through **explicit** steps with **stated** criteria—not from **string co-occurrence** heuristics in code.

### 1.3 Exit criteria

- Phase 0 decision documented.
- Index schema **frozen** as v1 of the **context contract** for this skill.

---

## Phase 2 — Terms & mechanisms (layers A & B)

**Goal:** Glossary and **named processes** exist **before** sparse `concepts[]`.

- **Terms** — surface vocabulary + chunk links; not classes.
- **Mechanisms** — workflows/lifecycles with steps + evidence.
- **Candidate queue** — “possible type” with rationale; **not** in `concepts[]` yet.

**Exit:** Promotion rule written: **candidate → concept** only through Phase 4 gate.

---

## Phase 3 — Story map (behavioral)

**Goal:** Epics/stories that satisfy **actor → behavior → anchor** (domain state **read** and/or **write**); alignment allows **term** references without minting types. **Query/read/forward** stories are as valid as **mutating** stories when the anchor is explicit.

**Exit:** Every story has a **clear** behavioral reading and **traceability** to concepts; no story exists solely to **match strings** in the type list. Every story states its **anchor** (read path, write path, or both)—not every story requires **mutation** of the core write model.

**Why before domain types (Phase 4)?** Short rationale for humans and for steering AI away from “types first”: [`docs/why-story-mapping-first.md`](../docs/why-story-mapping-first.md).

---

## Phase 4 — Domain types (`concepts[]`)

**Goal:** **Sparse** types; **reject gate** (“not just a property on a broader type”).

**Exit:** Type count and **per-type rationale** remain tractable for the MM3 fixture at the chosen depth.

---

## Phase 5 — Variant classification

**Goal:** Per family: **enum vs `extends`** **before** property churn.

**Exit:** Written **variant decision** per family before bulk modeling.

---

## Phase 6 — Deepen

**Goal:** Responsibilities and evidence on **approved** types only; **topological** `depends_on`.

**Exit:** Every type has **evidence** citations; citations **support** claims, they do not **auto-create** types.

---

## Phase 7 — Integrate

**Goal:** Synonyms, repointing, **drain candidate queue** into final `map-model-spec` (or split artifacts if you keep story map separate).

---

## Phase 8 — Validate & render

**Goal:** Automated checks (scanners, schema) + **rendered** reports; CI on MM3; optional **critic** checklist against the **principles table** at the top of this document.

---

## Execution order (what to do next)

1. **Run Phase 0** on the **current** `test/mm3/context/` tree — produce the **audit report** and the **keep vs rebuild** decision.
2. If **rebuild**: implement **Phase 1** from `HeroesHandbook.md` + an explicit **chunking spec** (rules **written first**, then scripts).
3. If **keep**: add **sidecar** or **migrate** `context_index.json` into the **canonical** schema with `modeling_kind` filled (LLM batch or rules + spot-check).
4. Only then: **Phase 2** onward in order.
5. **Phase 2**: run `python scripts/build_phase2_artifacts.py` — emits `test/mm3/phase2/` (terms, mechanisms, candidate queue). See [`docs/phase2_terms_and_mechanisms.md`](../docs/phase2_terms_and_mechanisms.md). Re-run `generate_context_bundle_manifest.py` to record phase2 hashes.
6. **Phase 3–8**: story map → types → variants → deepen → integrate → validate/render (per sections above).

---

## Success definition (reusable)

Another domain (another handbook) should be able to:

1. Supply **source markdown** and run **Phase 0–1** with the same **context contract**.
2. Run **2–8** such that **relationships** and **types** follow **explicit** gates and the **principles table**—not accidental **co-occurrence** or **string matching**.

---

*This file is operational **what next**. Enduring **why** and historical analysis may live in `docs/` when promoted from `plan/`. When the process stabilizes, archive or replace `plan/PROCESS-PLAN.md` with a shorter operator guide in `docs/`.*