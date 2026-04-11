---
name: abd-context-to-memory
description: >-
  Converts documents (PDF, PPTX, DOCX, XLSX, etc.) to markdown, drafts a
  structure-based chunking spec (chunking strategy), chunks with evidence labels,
  and embeds into a local FAISS vector store for semantic search. Supports an
  explicit strategy pass: review and accept `context_chunking_spec.yaml` before
  chunking when quality matters. Use when the user wants to "add to memory",
  "convert and chunk", "ingest content for agent", "refresh memory", "strategy
  pass", "use memory", or process a folder of documents for AI agent context.
  If the user does not mention strategy, the agent should ask whether a
  chunking strategy pass is desired before assuming the default one-shot pipeline.
  Topic/output folder: set CONTENT_MEMORY_ROOT, pass --path to scripts, or cd to
  the corpus folder; not bot WORKING_AREA or MCP workspace.
license: MIT
metadata:
  author: agilebydesign
  version: "2.3.10"
---

# abd-context-to-memory

Convert sources to **Markdown**, **draft a chunking spec** (boundaries, splits, taxonomy), **chunk** into `memory/` with YAML labels when a spec is present, and optionally **embed** into **FAISS** (Facebook AI Similarity Search) under `memory/rag/` for semantic search.

**Steps:**

1. **Convert to Markdown** — Core converter (MarkItDown, etc.) → `markdown/`; then built-in **post-processors** where applicable (e.g. PDF cleanup). **Structural decomposition belongs here** (and in corpus scripts), not in the chunker: headings, sections, tables. If structure is still wrong (no sections), **agents choose** the best next fix—optional deps, env flags, or a **bespoke** script under `<topic_root>/scripts/`. **Assess** headings/subheadings; **report** if bad; **implement, run, repeat**. **Last resort:** AI **semantic** pass—what sentences belong together, **topics** / **sub-topics**, inject structure, **complete one pass**, **re-review**. → [content/parts/library/convert-to-markdown.md](content/parts/library/convert-to-markdown.md), [content/parts/process.md](content/parts/process.md). PDF detail → [content/parts/library/pdf-extraction-advanced.md](content/parts/library/pdf-extraction-advanced.md).
2. **Structural scan + draft chunking spec** — **`markdown/structural_scan_report.*`** (assess converted structure first) **and**, when no spec exists yet, **`memory/context_chunking_spec.yaml`** (boundaries, splits, defaults) for chunking. **Taxonomy** is filled **per corpus** by AI or human. See [content/parts/library/chunking-spec.md](content/parts/library/chunking-spec.md).
3. **Chunk** — **Splits** Markdown per spec → `memory/` with front matter (`evidence_type`, `chunk_type`) when spec exists; it does not invent manuscript structure. Optional `chunk_inputs` in the YAML limits which `.md` files are chunked (e.g. ignore `archive/` backups). **After chunking, agents must verify** chunk count and split quality; if the run is wrong (e.g. a single giant chunk), **fix markdown / preprocessing and/or the spec and re-run**—do not stop at “you should edit the YAML” without iterating.
4. **Embed** — Vector index under **your** `<source_folder>/memory/rag/`; query with `search_memory.py --rag` pointing at that folder.

**Folder layout** → [content/parts/library/output.md](content/parts/library/output.md). **Bespoke post-processors** (corpus scripts that rewrite `markdown/` when the default convert is not enough): **`<topic_root>/scripts/`**—not inside the skill. See [content/parts/library/convert-to-markdown.md](content/parts/library/convert-to-markdown.md) and [content/parts/process.md](content/parts/process.md) (*Corpus preprocess scripts*).

## When to Activate

- User asks to "add content to memory" or "refresh memory"
- Wants to convert a folder of documents for agent context
- Mentions "convert and chunk", "ingest for agent", or "memory pipeline"
- Mentions **strategy pass**, **chunking strategy**, or **review the spec** — follow [content/parts/library/chunking-spec.md](content/parts/library/chunking-spec.md) and [content/parts/process.md](content/parts/process.md)
- **Semantic search:** "use memory", "search memory", … — run `search_memory.py "<query>"` and inject results

## Chunking strategy (short)

The **chunking spec** (`memory/context_chunking_spec.yaml`) is the pipeline strategy: boundaries, splitting, `defaults`, and `taxonomy`.

- **If the user does not mention strategy**, **ask once**: **strategy pass** (pause before chunking; review/edit YAML, then chunk+embed) vs **straight through** (single `index_memory.py` run). Do not assume straight-through. Details: [content/parts/process.md](content/parts/process.md).
- **Why review matters, taxonomy, `evidence_type` vs `chunk_type`, iteration after bad splits** → [content/parts/library/chunking-spec.md](content/parts/library/chunking-spec.md).

## Output / topic folder

To fix **where** converted files, chunks, and the FAISS index are written:

- Set **`CONTENT_MEMORY_ROOT`** to the folder that contains (or will contain) `markdown/`, `memory/` (chunks, **`memory/context_chunking_spec.yaml`**, **`memory/rag/`**), **or**
- Pass **`--path <folder>`** on each run, **or**
- **`cd`** to that folder before running (when env is unset, **cwd** is the topic root).

This is **not** agile_bots workspace, not MCP, not bot `WORKING_AREA`. There is nothing to “set” inside `skill-config.json` for paths—only **`engine`** metadata if needed. Resolution order for defaults: **`CONTENT_MEMORY_ROOT`** **→** **cwd** — see [content/parts/library/config.md](content/parts/library/config.md).

## Pipeline commands

Full reference (flags, pause workflow, examples): [content/parts/process.md](content/parts/process.md).

```bash
# Typical full run (always safest: explicit path)
python scripts/index_memory.py --path <source_folder>

# After CONTENT_MEMORY_ROOT or cd to corpus
python scripts/index_memory.py

# After editing an existing spec (skip re-convert + skip re-draft)
python scripts/index_memory.py --path <source_folder> --skip-convert --skip-spec

# Embeddings only from existing chunks
python scripts/index_memory.py --path <source_folder> --rebuild
```

Run from a directory where paths resolve; script paths are under `skills/abd-context-to-memory/scripts/`.

**Canonical implementation:** convert, PDF post-process (`pdf_markdown_post.py`), outline injection, and related pipeline code live **only** under this skill’s `scripts/`. Do not use or duplicate changes from other repositories as the source of truth for this pipeline.

## Semantic search

```bash
python scripts/search_memory.py "<query>" [--rag <path/to/memory/rag>] [--k 5]
```

If `--rag` is omitted, search uses `<ROOT>/memory/rag` (same `ROOT` as [config.md](content/parts/library/config.md)).

## Scope

- **One file** → `convert_to_markdown.py --file <path>` only.
- **Folder** → `index_memory.py --path <folder>` or `index_memory.py` with `CONTENT_MEMORY_ROOT` / cwd set to the corpus.

## Scripts

| Script | Purpose |
|--------|---------|
| `index_memory.py [--path <folder>]` | convert → draft spec → chunk → embed |
| `--skip-convert` / `--skip-spec` / `--rebuild` | See [content/parts/process.md](content/parts/process.md) |
| `draft_chunking_spec.py [--path <folder>]` | Reports → **`markdown/`**, spec → **`memory/`** |
| `convert_to_markdown.py --memory <folder>` \| `--file <file>` | Convert |
| `chunk_markdown.py --path <folder>` | Chunk only |
| `embed_and_index.py [--path <memory_folder>]` | Embed only (default `<ROOT>/memory`) |
| `search_memory.py "<query>"` | Search (default `--rag` `<ROOT>/memory/rag`) |

## Dependencies

```bash
pip install "markitdown[all]"
pip install -r requirements-rag.txt
# Optional: PDF bookmark outline → markdown headings during convert
pip install pymupdf
```

Set `OPENAI_API_KEY` for embedding (or configure embeddings in `_config.py`).
