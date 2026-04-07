---
name: abd-context-to-memory
description: >-
  Converts documents (PDF, PPTX, DOCX, XLSX, etc.) to markdown, chunks them,
  and embeds into a local FAISS vector store for semantic search. Use when the
  user wants to "add to memory", "convert and chunk", "ingest content for agent",
  "refresh memory", "use memory", or process a folder of documents for AI agent context.
license: MIT
metadata:
  author: agilebydesign
  version: "2.0.0"
---

# abd-context-to-memory

Converts source documents to markdown, chunks them, and embeds into a local FAISS vector store. Three steps: **convert** → **chunk** → **embed**.

## When to Activate

- User asks to "add content to memory" or "refresh memory"
- Wants to convert a folder of documents (PDF, PPTX, DOCX, XLSX, etc.) for agent context
- Mentions "convert and chunk", "ingest for agent", or "memory pipeline"
- Has added new files and wants them processed
- **"Use memory" / semantic search:** User says "use memory", "search memory", "what does memory say about X" — run `search_memory.py "<query>"` and inject results

## Pipeline

```
python scripts/index_memory.py --path <source_folder>          # convert + chunk + embed
python scripts/index_memory.py --path <source_folder> --skip-convert  # chunk + embed only
```

That's it. Chunks land in `<source>/memory/`, the FAISS index in `<source>/memory/rag/`.

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
| `index_memory.py --path <folder>` | Full pipeline: convert → chunk → embed |
| `convert_to_markdown.py --memory <folder>` | Convert all supported files to markdown |
| `convert_to_markdown.py --file <file>` | Convert a single file |
| `chunk_markdown.py --path <folder>` | Chunk markdown into memory/ |
| `embed_and_index.py --path <folder>` | Embed chunks into local FAISS index |
| `search_memory.py "<query>"` | Semantic search over embedded chunks |

## Output Layout

```
<source_folder>/
  markdown/          # converted markdown + images
  memory/            # chunks
    rag/             # FAISS vector index
```

## Dependencies

```bash
pip install "markitdown[all]"          # convert
pip install -r requirements-rag.txt    # embed + search (faiss-cpu, openai, etc.)
```

Set `OPENAI_API_KEY` for embedding (or configure a local embedding model in `_config.py`).
