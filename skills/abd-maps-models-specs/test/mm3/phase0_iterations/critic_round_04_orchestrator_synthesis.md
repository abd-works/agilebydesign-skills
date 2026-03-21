# Critic round 4 — Orchestrator synthesis (after rounds 1–3)

## Agreement across critics

1. **Keep the corpus** — 725/725 alignment and pinned handbook are a defensible foundation; no evidence to rebuild from source.
2. **`modeling_kind` (or equivalent) is blocking** for honest promotion — the audit and spot-check were already right; the sidecar is the right *shape* for Phase 1.
3. **v1 heuristics are a stub** — useful for distribution, triage, and **stopping** naive “string → class” behavior once gates consume the sidecar; **not** a substitute for LLM/re-read on borderline `domain_rule_candidate`.

## Conflicts / tension

- **Audit** wants **`reason` on every forward unit**; not implemented in this run (Phase 1 schema work).
- **Heuristic critic** wants **content-based TOC**; **Validation critic** wants **schema + golden counts** — partially addressed (enum whitelist); JSON Schema + golden snapshot deferred.

## What shipped this session

- Phase 0 **audit metrics + report** + **decision gate**
- **`modeling_kind` sidecar** (725 keys) + **validator** with **enum**
- **Docs** + **critic markdown** trail for morning review

## Single sentence for stakeholders

*We adopted the MM3 evidence package, measured it, and added a non-authoritative `modeling_kind` layer so promotion gates can eventually refuse dumb subclasses—without pretending v1 labels are reviewed truth.*
