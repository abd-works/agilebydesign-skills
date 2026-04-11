# Pipeline Process

Four steps: **convert → draft spec → chunk → embed**

---

## Example

Documents in `D:/content/Training_2025/`:

```text
slides/
  onboarding.pptx
policies/
  remote-work.pdf
```

Run:

```bash
python skills/abd-context-to-memory/scripts/index_memory.py --path "D:/content/Training_2025"
```

After convert:

```text
D:/content/Training_2025/
  markdown/
    slides/onboarding.md
    policies/remote-work.md
```

After spec draft (review this file before continuing):

```text
D:/content/Training_2025/
  context_chunking_spec.yaml   ← edit boundaries, taxonomy, defaults
```

After chunk + embed:

```text
D:/content/Training_2025/
  memory/
    slides/onboarding__slide_01.md   ← front matter: chunk_id, evidence_type, modeling_kind
    slides/onboarding__slide_02.md
    policies/remote-work__section_00.md
    chunk_index.json
    rag/
      index.faiss
      metadata.json
```

---

## Options

```bash
# Full pipeline (convert → draft spec → chunk → embed)
python index_memory.py --path <source>

# Skip convert (markdown already exists)
python index_memory.py --path <source> --skip-convert

# Skip spec draft (spec already reviewed and present)
python index_memory.py --path <source> --skip-spec

# Skip both convert and spec draft
python index_memory.py --path <source> --skip-convert --skip-spec

# Rebuild FAISS index from existing chunks
python index_memory.py --path <source> --rebuild

# Draft spec only (no chunking or embedding)
python draft_chunking_spec.py --path <source>
```

---

## Chunking rules

Without a spec (`context_chunking_spec.yaml` absent):
- **PowerPoint**: one chunk per slide (`__slide_01.md`, `__slide_02.md`, …)
- **Long prose** (>200 lines): split at `#` / `##` headings (`__section_00.md`, …)
- **Short files**: one chunk, no suffix

With a spec (drafted or edited by a human):
- `section_boundaries` regexes control where new chunks begin
- `splitting.split_on_heading_level` controls heading split depth
- `splitting.min_chunk_chars` / `max_chunk_chars` control size limits
- Each chunk gets YAML front matter with `evidence_type` and `modeling_kind` from `defaults`

---

## Chunking spec (`context_chunking_spec.yaml`)

Drafted automatically by `draft_chunking_spec.py` from actual source structure. Minimum sections:

| Section | Purpose |
|---------|---------|
| `section_boundaries` | Regexes that start a new major unit (chapter, section) |
| `splitting` | Size limits, table handling, heading split level |
| `defaults` | Fallback `evidence_type` / `modeling_kind` labels |
| `taxonomy` | Closed-world allowed values (enforced by validators) |

**Human review recommended** before running the chunk step. Once accepted, re-run with `--skip-spec`.

---

## Supported input formats

`.pdf`, `.pptx`, `.docx`, `.xlsx`, `.xls`, `.html`, `.htm`, `.txt`, `.csv`, `.json`, `.xml`

---

## When something fails

- Wrong or missing path → convert/chunk exits with an error message
- Unsupported file type → that file is skipped; others still run
- RAG/embed → needs `OPENAI_API_KEY` and `requirements-rag.txt` installed
- Spec YAML parse error → warning printed, chunking falls back to heuristics
