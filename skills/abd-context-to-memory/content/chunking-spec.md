# Chunking Spec (`context_chunking_spec.yaml`)

Placed beside the `--path` source folder. Drafted automatically by `draft_chunking_spec.py` from the actual structure of the markdown sources. Edit before chunking runs; re-run with `--skip-spec` once accepted.

If the spec is absent, chunking falls back to built-in heuristics and no front matter is written to chunks.

---

## Minimum sections

```yaml
section_boundaries:
  chapter_break_regex: "^CHAPTER\\s+\\d+"
  section_break_regex: "^##\\s+"
  all_caps_standalone: true

splitting:
  min_chunk_chars: 400
  max_chunk_chars: 8000
  keep_markdown_tables_intact: true
  split_on_heading_level: 2

defaults:
  evidence_type: rule
  modeling_kind: rule

taxonomy:
  evidence_type: [definition, rule, example, table, metadata_noise, mixed]
  modeling_kind: [definition, rule, example, noise, structural_only]
```

---

## Sections

| Section | Purpose |
|---------|---------|
| `section_boundaries` | Regexes that start a new major unit; controls where the emitter breaks chunks |
| `splitting` | Size limits, table handling, heading level at which to split |
| `defaults` | Fallback `evidence_type` / `modeling_kind` labels when heuristics don't fire |
| `taxonomy` | Closed-world allowed values — validators enforce these |

---

## `evidence_type` vs `modeling_kind`

Two independent axes applied per chunk when a spec is active:

| Axis | Question | Examples |
|------|----------|---------|
| `evidence_type` | What does this chunk look like in the source? (form) | `definition`, `rule`, `example`, `table`, `metadata_noise`, `mixed` |
| `modeling_kind` | How should agent work treat this chunk? (stance) | `definition`, `rule`, `example`, `noise`, `structural_only` |

They often match but diverge when form and purpose differ — e.g. a table that is normative: `evidence_type: table`, `modeling_kind: rule`.

Values are closed-world: only what `taxonomy` in the spec declares is valid.

---

## Workflow

1. Run `draft_chunking_spec.py --path <source>` — prints structural report, writes spec
2. Review and edit `context_chunking_spec.yaml`
3. Run `index_memory.py --path <source> --skip-spec` (or full pipeline — spec auto-detected if present)
