# Why story mapping comes before domain types

This skill orders work so that **story mapping (behavior)** lands **before** **sparse domain types** (`concepts[]`). That is intentional—not because stories are “more important” than the domain, but because of **dependency** and **failure modes** when extracting from large handbooks or similar sources.

Use this page as **user-facing context** (why we work this way) and as a **steer** for AI-assisted runs: many tool defaults jump straight to **nouns and lists**; this pipeline does not.

---

## 1. Behavior is what the source is usually about

Handbooks and narrative sources speak in **flows, situations, and outcomes**—what actors do, what changes, what is read or written. **Story mapping** is the structured way to capture that **without** first deciding which nouns are “real” types.

If you start with `concepts[]`, you tend to **label** the text instead of **grounding** behavior. You get types that **match vocabulary** but not **responsibilities**.

---

## 2. Types are a promotion decision, not the first cut

In this process, **terms** and **mechanisms** are explicit; **`concepts[]`** is **sparse** and **gated**. The story map is the layer that says: *this behavior needs a stable anchor in the model.*

You **promote** to a type when the **story** (plus evidence) justifies it—not when a word appears often.

---

## 3. Traceability and rejection

Stories give you **where** to attach evidence and **why** something deserves a type. Gates like “not just a property on a broader type” only bite when judged **against a behavioral slice**. If types are fixed first, those gates often become **cosmetic**, because the types already exist.

---

## Not a universal law

Some situations **do** sketch a domain model early (small domain, known model, workshop format). This pipeline is tuned for **extraction from messy sources** where **premature types** are the main failure mode—so **story map before sparse types** keeps the sequence: **vocabulary → mechanisms → behavior → then promote types**.

---

## See also

- **Operational phases:** `plan/PROCESS-PLAN.md` (Phase 2 → Phase 3 → Phase 4).
- **Pipeline failure modes (noun explosion, etc.):** `plan/pipeline-deep-dive.md`.
