# Pipeline Process

Three steps: **convert → chunk → embed**

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

After chunk + embed:

```text
D:/content/Training_2025/
  memory/
    slides/onboarding__slide_01.md
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
# Full pipeline
python index_memory.py --path <source>

# Skip convert (markdown already exists)
python index_memory.py --path <source> --skip-convert

# Rebuild index from existing chunks
python index_memory.py --path <source> --rebuild
```

---

## Chunking rules

- **PowerPoint**: one chunk per slide (`__slide_01.md`, `__slide_02.md`, …)
- **Long prose** (>200 lines): split at `#` / `##` headings (`__section_00.md`, …)
- **Short files**: one chunk, no suffix

---

## Supported input formats

`.pdf`, `.pptx`, `.docx`, `.xlsx`, `.xls`, `.html`, `.htm`, `.txt`, `.csv`, `.json`, `.xml`

---

## When something fails

- Wrong or missing path → convert/chunk exits with an error message
- Unsupported file type → that file is skipped; others still run
- RAG/embed → needs `OPENAI_API_KEY` and `requirements-rag.txt` installed
