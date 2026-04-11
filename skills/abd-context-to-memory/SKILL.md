---
name: abd-context-to-memory
description: >-
  Converts documents (PDF, PPTX, DOCX, XLSX, etc.) to markdown, drafts a
  structure-based chunking spec, chunks with evidence labels, and embeds into a
  local FAISS vector store for semantic search. Use when the user wants to "add
  to memory", "convert and chunk", "ingest content for agent", "refresh memory",
  "use memory", or process a folder of documents for AI agent context.
license: MIT
metadata:
  author: agilebydesign
  version: "2.0.0"
---

# abd-context-to-memory

**convert → draft spec → chunk → embed.** Turns source documents into a semantically searchable FAISS vector store, using a structure-derived chunking spec so splits and evidence labels reflect the actual shape of the content.

## When to Activate

- User asks to "add content to memory" or "refresh memory"
- Wants to convert a folder of documents (PDF, PPTX, DOCX, XLSX, etc.) for agent context
- Mentions "convert and chunk", "ingest for agent", or "memory pipeline"
- Has added new files and wants them processed
- **"Use memory" / semantic search:** User says "use memory", "search memory", "what does memory say about X" — run `search_memory.py "<query>"` and inject results

## Pipeline

### Standard (recommended)

```
python scripts/index_memory.py --path <source_folder>
```

This runs all four steps:
1. **Convert** — source docs → `markdown/`
2. **Draft spec** — structural scan of markdown → `context_chunking_spec.yaml` (AI-assisted, human review)
3. **Chunk** — apply spec → `memory/`
4. **Embed** — chunks → `memory/rag/` (FAISS)

### Skip convert (markdown already present)

```
python scripts/index_memory.py --path <source_folder> --skip-convert
```

### Skip spec draft (spec already reviewed and present)

```
python scripts/index_memory.py --path <source_folder> --skip-spec
```

### Skip both convert and spec draft

```
python scripts/index_memory.py --path <source_folder> --skip-convert --skip-spec
```

### Draft spec only (no chunking or embedding)

```
python scripts/draft_chunking_spec.py --path <source_folder>
```

## Chunking Spec (`context_chunking_spec.yaml`)

Before chunking, the pipeline drafts a **`context_chunking_spec.yaml`** in the source folder. This spec is derived by scanning the actual structure of the markdown sources and captures:

- `section_boundaries` — regexes that start new major units (chapters, sections)
- `splitting` — min/max chunk sizes, table handling, heading split level
- `defaults` — default `evidence_type` / `modeling_kind` labels for new chunks
- `taxonomy` — closed-world allowed values for `evidence_type` and `modeling_kind`

**Human review recommended:** After drafting, review `context_chunking_spec.yaml` in the source folder before running the full pipeline. Fix any misidentified boundaries, tighten taxonomy, and confirm noise exclusions. Re-run with `--skip-spec` once the spec is accepted.

If `context_chunking_spec.yaml` **already exists** in the source folder, the chunk step uses it directly — the draft step is skipped automatically.

### `evidence_type` vs `modeling_kind`

Two independent labels applied per chunk:

| Axis | Question | Examples |
|------|----------|---------|
| `evidence_type` | What does this chunk look like in the source? (form) | `definition`, `rule`, `example`, `table`, `metadata_noise`, `mixed` |
| `modeling_kind` | How should agent work treat this chunk? (stance) | `definition`, `rule`, `example`, `noise`, `structural_only` |

They often match but diverge when form and purpose differ (e.g. a table that is normative → `evidence_type: table`, `modeling_kind: rule`).

## Semantic Search

```bash
python scripts/search_memory.py "<query>" [--k 5] [--index <path_to_memory_rag>]
```

Returns top-k chunks. Inject results into your response and cite sources.

## CRITICAL: Respect User Scope

- **One file**: User says "one file", "just X.pdf" → use `--file <path>` with `convert_to_markdown.py`. Process ONLY that file.
- **Folder**: User says "folder", "everything in X" → use `--path <folder>` with `index_memory.py`.

## Scripts

Run from workspace root. Scripts in `skills/abd-context-to-memory/scripts/`.

| Script | Purpose |
|--------|---------|
| `index_memory.py --path <folder>` | Full pipeline: convert → draft spec → chunk → embed |
| `index_memory.py --path <folder> --skip-convert` | Skip convert, run draft spec → chunk → embed |
| `index_memory.py --path <folder> --skip-spec` | Skip spec draft, run convert → chunk → embed |
| `draft_chunking_spec.py --path <folder>` | Structural scan + draft `context_chunking_spec.yaml` only |
| `convert_to_markdown.py --memory <folder>` | Convert all supported files to markdown |
| `convert_to_markdown.py --file <file>` | Convert a single file |
| `chunk_markdown.py --path <folder>` | Chunk markdown into memory/ (uses spec if present) |
| `embed_and_index.py --path <folder>` | Embed chunks into local FAISS index |
| `search_memory.py "<query>"` | Semantic search over embedded chunks |

## Output Layout

```
<source_folder>/
  context_chunking_spec.yaml   # chunking rules + taxonomy (draft → review → accepted)
  markdown/                    # converted markdown + images
  memory/                      # chunks (with evidence_type / modeling_kind front matter when spec present)
    rag/                       # FAISS vector index
```

## Dependencies

```bash
pip install "markitdown[all]"          # convert
pip install -r requirements-rag.txt    # embed + search (faiss-cpu, openai, etc.)
```

Set `OPENAI_API_KEY` for embedding (or configure a local embedding model in `_config.py`).
