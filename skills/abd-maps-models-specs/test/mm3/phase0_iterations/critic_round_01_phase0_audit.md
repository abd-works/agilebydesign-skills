# Critic round 1 — Phase 0 audit (independent subagent)

## Verdict

**Phase 0 is a plumbing win, not a domain win.** Stable chunks, clean index↔disk join, pinned source hash. Metadata is **insufficient** for OO modeling without `modeling_kind`—the gate “Adopt + extend” admits that.

## Critical issues

1. **`modeling_kind`: 0 / 725** — No machine-usable promote/hold signal; downstream becomes guesswork.
2. **`reason` 100% missing on forward units** — Excluded blocks have reasons; retained units do not. No “why this chunk exists” without opening files.
3. **Excluded mass (1408) vs forward (725)** — Mostly `structural heading only` / `metadata/noise`; metrics don’t prove whether chunker is right or throwing away needed structure.
4. **`domain-rule` in excluded (105) vs forward (289)** — Same label, two paths — pipeline smell.
5. **Near-uniform `document_region` / `structural_type`** — Weak stratification.
6. **Implicit `blk_*` ↔ unit** — Documented debt; fragile for tools.
7. **No generator id/version in index** — Only content hash, not pipeline identity.

## What’s solid

- Perfect 725/725 alignment; pinned handbook SHA; honest metrics JSON; proportionate “adopt, don’t panic-rebuild” decision.

## Recommendations (prioritized)

1. Ship `modeling_kind` as first-class contract (done in v1 sidecar — **follow-up**: merge + reasons on units).
2. Emit `reason` or `retention_policy` on every forward unit.
3. Reconcile `domain-rule` forward vs excluded with a sample audit.
4. Embed `generator_id` + `generator_version` in future index builds.
5. Enrich `structural_type` / `document_region` or stop treating them as gates.
6. Document or automate `blk_*` ↔ unit join.
