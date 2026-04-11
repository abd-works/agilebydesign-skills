# Purpose

Convert office documents (PDF, PPTX, DOCX, XLSX, etc.) to **Markdown** with a **core converter** plus **shared post-processors** where needed. Then **check** whether you got real **headings and subheadings**; if not, **tell the user**, suggest a **bespoke post-processor** under `<topic_root>/scripts/` or another fix, **run it**, and **repeat**. If the text is still a **semantic mess**, use an **AI pass** to group sentences by topic, name **sub-topics**, add structure, **finish the pass**, and **review again** before chunking.

After that: draft a **structure-based chunking spec** (`context_chunking_spec.yaml`), **chunk** into `memory/` with evidence labels when a spec exists, and **embed** into a local **FAISS** index for semantic search. Support an explicit **strategy pass** (review/edit the YAML before chunk+embed) when quality matters more than one-shot throughput.

Full pipeline order and commands: **[process.md](../process.md)**. Convert step detail: **[convert-to-markdown.md](convert-to-markdown.md)**.
