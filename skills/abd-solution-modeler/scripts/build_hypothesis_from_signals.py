#!/usr/bin/env python3
"""Phase 4: Build hypothesis.json from concept signals (concepts + registries format).

Reads concept_signals/concept_signals.json (single combined file from Phase 3)
and produces hypothesis.json with the concept-anchored structure:
- concepts: {ConceptName: {term_ids, performs, receives, states, decisions, relationships}}
- registries: {actions, decisions, states, relationships}
- concept_guidance: {priority_concepts, concept_aliases, ...} for Phase 5 evidence extraction

Phase 3 does not extract decisions, states, or relationships — those are left empty.
Phase 5 (evidence_extraction_guided) will extract them from chunks using concept_guidance.
"""
import argparse
import json
import re
import sys
from pathlib import Path

_SKILL_DIR = Path(__file__).resolve().parent.parent

# Noise terms to exclude from concepts (section headers, junk)
_NOISE_TERMS = {
    "secret origins", "chapter", "powers", "ranks", "abilities", "basics",
    "mutants", "awareness", "dexterity", "stamina", "fighting", "intellect",
    "presence", "source", "file", "heroeshandbook",
}

# Discourse adverbs and common non-concept words
_DISCOURSE_AND_JUNK = {
    "actually", "essentially", "basically", "typically", "generally",
    "simply", "really", "whenever", "when", "what", "for", "they", "this",
    "one", "like", "all", "see", "activa",  # truncation of Activation
}


def _is_noise_concept(name: str) -> bool:
    """Return True if concept name is junk (discourse, fragment, truncation)."""
    if not name or len(name) < 2 or len(name) > 80:
        return True
    n = name.strip()
    low = n.lower()
    if low in _NOISE_TERMS or low in _DISCOURSE_AND_JUNK:
        return True
    # Sentence fragments: "A Weaken", "A Summoner", "A Variable" — article + noun
    if re.match(r"^A\s+\w", n):
        return True
    if re.match(r"^An\s+\w", n):
        return True
    # "The Xxxx" — definite article + noun
    if re.match(r"^The\s+\w", n):
        return True
    # Sentence fragments: ends with " You", " The", " This"
    if n.endswith(" You") or n.endswith(" The") or n.endswith(" This"):
        return True
    # All-caps header fragments: "RANKED You", "RANKED TEAMWORK GENERAL You"
    if re.match(r"^[A-Z][A-Z0-9\s]+You$", n):
        return True
    return False


def _load_json(path: Path) -> list | dict:
    if not path.exists():
        return [] if "candidates" in path.name or "actions" in path.name else {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def _normalize_concept_name(name: str) -> str:
    """Normalize for matching: strip, collapse whitespace."""
    if not name or not isinstance(name, str):
        return ""
    return re.sub(r"\s+", " ", name.strip())


def _dep_id_to_act_id(dep_id: str) -> str:
    """Map dep_XXXX to act_XXXX."""
    if dep_id.startswith("dep_"):
        return "act_" + dep_id[4:]
    return dep_id


def _load_signals(signals_dir: Path) -> dict:
    """Load combined concept_signals.json; fall back to separate files for compatibility."""
    combined = signals_dir / "concept_signals.json"
    if combined.exists():
        return _load_json(combined) or {}
    return {
        "tf_weights": _load_json(signals_dir / "term_candidates.json"),
        "dependency_verbs": _load_json(signals_dir / "dependency_actions.json"),
        "actor_detection": _load_json(signals_dir / "actor_candidates.json"),
        "centrality": _load_json(signals_dir / "centrality_scores.json"),
    }


def _collect_chunk_ids_per_concept(signals: dict) -> dict[str, set[str]]:
    """Aggregate chunk IDs per concept from all signals that have chunk refs.

    Sources:
    - tf_weights: chunk_ids per term
    - dependency_verbs: source_chunk -> subject, object
    - definition_patterns: source_chunk -> concept
    - table_mining: source_chunk -> each header (concept)
    - enumeration_patterns: source_chunk -> parent_concept, children
    - contrast_patterns: source_chunk -> each concept
    - verb_interaction.sample_interactions: source_chunk -> subject, object
    """
    chunk_ids: dict[str, set[str]] = {}

    def _add(concept: str, cid: str) -> None:
        if not concept or not cid:
            return
        if concept not in chunk_ids:
            chunk_ids[concept] = set()
        chunk_ids[concept].add(cid)

    # tf_weights
    for t in signals.get("tf_weights", []) or []:
        if not isinstance(t, dict):
            continue
        name = _normalize_concept_name(t.get("name", ""))
        for cid in t.get("chunk_ids", []) or []:
            _add(name, cid)

    # dependency_verbs
    for d in signals.get("dependency_verbs", []) or []:
        if not isinstance(d, dict):
            continue
        cid = d.get("source_chunk", "")
        for name in (_normalize_concept_name(d.get("subject", "")), _normalize_concept_name(d.get("object", ""))):
            _add(name, cid)

    # definition_patterns
    for d in signals.get("definition_patterns", []) or []:
        if not isinstance(d, dict):
            continue
        name = _normalize_concept_name(d.get("concept", ""))
        cid = d.get("source_chunk", "")
        _add(name, cid)

    # table_mining: headers are concepts
    for t in signals.get("table_mining", []) or []:
        if not isinstance(t, dict):
            continue
        cid = t.get("source_chunk", "")
        for h in t.get("headers", []) or []:
            name = _normalize_concept_name(h if isinstance(h, str) else str(h))
            _add(name, cid)

    # enumeration_patterns: parent + children
    for e in signals.get("enumeration_patterns", []) or []:
        if not isinstance(e, dict):
            continue
        cid = e.get("source_chunk", "")
        parent = _normalize_concept_name(e.get("parent_concept", ""))
        _add(parent, cid)
        for c in e.get("children", []) or []:
            child = _normalize_concept_name(c if isinstance(c, str) else str(c))
            _add(child, cid)

    # contrast_patterns
    for c in signals.get("contrast_patterns", []) or []:
        if not isinstance(c, dict):
            continue
        cid = c.get("source_chunk", "")
        for x in c.get("concepts", []) or []:
            name = _normalize_concept_name(x if isinstance(x, str) else str(x))
            _add(name, cid)

    # verb_interaction.sample_interactions
    vi = signals.get("verb_interaction", {}) or {}
    for i in vi.get("sample_interactions", []) or []:
        if not isinstance(i, dict):
            continue
        cid = i.get("source_chunk", "")
        for key in ("subject", "object"):
            name = _normalize_concept_name(i.get(key, ""))
            _add(name, cid)

    return chunk_ids


def _build_concepts_and_registries(signals: dict) -> dict:
    """Build concepts + registries from concept signals."""
    terms = signals.get("tf_weights", [])
    deps = signals.get("dependency_verbs", [])
    actors = signals.get("actor_detection", [])

    if not isinstance(terms, list):
        terms = []
    if not isinstance(deps, list):
        deps = []
    if not isinstance(actors, list):
        actors = []

    # Collect all concept names
    concepts_set: set[str] = set()
    term_to_ids: dict[str, list[str]] = {}  # concept name -> [term_id, ...]

    for t in terms:
        if not isinstance(t, dict):
            continue
        tid = t.get("term_id", "")
        name = _normalize_concept_name(t.get("name", ""))
        if not name or not tid:
            continue
        if _is_noise_concept(name):
            continue
        concepts_set.add(name)
        term_to_ids.setdefault(name, []).append(tid)

    for a in actors:
        if not isinstance(a, dict):
            continue
        name = _normalize_concept_name(a.get("name", ""))
        if not name or _is_noise_concept(name):
            continue
        concepts_set.add(name)
        # Actors may not have term_ids; leave empty if not in terms

    for d in deps:
        if not isinstance(d, dict):
            continue
        subj = _normalize_concept_name(d.get("subject", ""))
        obj = _normalize_concept_name(d.get("object", ""))
        if subj and not _is_noise_concept(subj):
            concepts_set.add(subj)
        if obj and not _is_noise_concept(obj):
            concepts_set.add(obj)

    # Initialize concept entries (chunk_ids added later from _collect_chunk_ids_per_concept)
    index: dict[str, dict[str, list]] = {}
    for c in sorted(concepts_set):
        index[c] = {
            "term_ids": list(dict.fromkeys(term_to_ids.get(c, []))),
            "performs": [],
            "receives": [],
            "states": [],
            "decisions": [],
            "relationships": [],
        }

    # Build actions registry and link performs/receives
    actions_registry: dict[str, dict] = {}
    for d in deps:
        if not isinstance(d, dict):
            continue
        dep_id = d.get("dep_id", "")
        subj = _normalize_concept_name(d.get("subject", ""))
        obj = _normalize_concept_name(d.get("object", ""))
        pred = (d.get("predicate") or "").strip()
        raw = (d.get("raw") or "").strip()
        if not dep_id:
            continue
        act_id = _dep_id_to_act_id(dep_id)
        actions_registry[act_id] = {
            "subject": subj,
            "predicate": pred,
            "object": obj,
            "raw": raw,
        }
        if subj and subj in index:
            if act_id not in index[subj]["performs"]:
                index[subj]["performs"].append(act_id)
        if obj and obj in index:
            if act_id not in index[obj]["receives"]:
                index[obj]["receives"].append(act_id)

    return {
        "concepts": index,
        "registries": {
            "actions": actions_registry,
            "decisions": {},
            "states": {},
            "relationships": {},
        },
    }


def _build_concept_guidance(signals: dict, concepts: dict) -> dict:
    """Derive concept_guidance for Phase 5 evidence extraction."""
    terms = signals.get("tf_weights", [])
    actors = signals.get("actor_detection", [])
    centrality = signals.get("centrality", [])

    if not isinstance(terms, list):
        terms = []
    if not isinstance(actors, list):
        actors = []
    if not isinstance(centrality, list):
        centrality = []

    # Priority concepts: top terms by weighted_score, plus actors
    priority: list[str] = []
    seen = set()
    for t in sorted(terms, key=lambda x: float(x.get("weighted_score", 0)), reverse=True)[:30]:
        if not isinstance(t, dict):
            continue
        name = _normalize_concept_name(t.get("name", ""))
        if name and not _is_noise_concept(name) and name not in seen:
            priority.append(name)
            seen.add(name)
    for a in actors[:10]:
        if not isinstance(a, dict):
            continue
        name = _normalize_concept_name(a.get("name", ""))
        if name and name not in seen:
            priority.append(name)
            seen.add(name)

    # Aliases: common abbreviations (workspace can extend via concept_guidance.json)
    aliases: dict[str, list[str]] = {
        "Gamemaster": ["GM"],
        "Difficulty Class": ["DC"],
        "Strength": ["Str"],
        "Dexterity": ["Dex"],
        "Agility": ["Agi"],
        "Intellect": ["Int"],
        "Stamina": ["Con"],
        "Awareness": ["Wis"],
        "Presence": ["Cha"],
    }

    # Mechanisms and variation_axes: placeholders; AI/human can refine
    mechanisms: list[str] = []
    variation_axes: list[str] = []

    actor_names = [
        _normalize_concept_name(a.get("name", ""))
        for a in actors if isinstance(a, dict) and a.get("name")
    ]
    actor_names = [n for n in actor_names if n]

    noise_filters = list(_NOISE_TERMS)

    return {
        "priority_concepts": priority[:20],
        "concept_aliases": aliases,
        "mechanisms": mechanisms,
        "actors": actor_names,
        "variation_axes": variation_axes,
        "noise_filters": noise_filters,
        "focus_sections": [],
    }


def _render_hypothesis_md(hypothesis: dict) -> str:
    """Render hypothesis.json to markdown: full concept-anchored view per spec.

    Each concept is a section with term_ids, performs (resolved actions), receives,
    states, decisions, relationships. Actions are shown inline as Subject predicate Object.
    """
    lines = [
        "# Hypothesis",
        "",
        "Concept-anchored view of `hypothesis.json`. Each concept lists its evidence.",
        "",
    ]

    # concept_guidance (full)
    cg = hypothesis.get("concept_guidance", {})
    lines.extend(["## concept_guidance", ""])
    lines.append("**priority_concepts:**")
    for c in cg.get("priority_concepts", []):
        lines.append(f"- {c}")
    lines.append("")
    lines.append("**actors:**")
    for a in cg.get("actors", []):
        lines.append(f"- {a}")
    lines.append("")
    lines.append("**concept_aliases:**")
    for k, v in cg.get("concept_aliases", {}).items():
        lines.append(f"- {k} → {', '.join(str(x) for x in v)}")
    lines.append("")
    lines.append("**noise_filters:** " + ", ".join(str(x) for x in cg.get("noise_filters", [])))
    lines.append("")
    lines.append("---")
    lines.append("")

    # concepts: each as a full section with resolved actions
    concepts = hypothesis.get("concepts", {})
    actions_reg = hypothesis.get("registries", {}).get("actions", {})

    lines.append("## concepts")
    lines.append("")
    lines.append(f"*{len(concepts)} concepts*")
    lines.append("")

    for name, data in sorted(concepts.items()):
        term_ids = data.get("term_ids", [])
        performs = data.get("performs", [])
        receives = data.get("receives", [])
        states = data.get("states", [])
        decisions = data.get("decisions", [])
        relationships = data.get("relationships", [])

        lines.append(f"### {name}")
        lines.append("")

        chunk_ids = data.get("chunk_ids", [])
        lines.append("- **term_ids:** " + (", ".join(term_ids) if term_ids else "—"))
        lines.append("- **chunk_ids:** " + (", ".join(chunk_ids[:20]) + (" …" if len(chunk_ids) > 20 else "") if chunk_ids else "—"))
        lines.append("")

        if performs:
            lines.append("- **performs:**")
            for act_id in performs:
                a = actions_reg.get(act_id, {})
                subj = a.get("subject", "")
                pred = a.get("predicate", "")
                obj = a.get("object", "")
                raw = (a.get("raw", "") or "")[:100].replace("\n", " ")
                lines.append(f"  - `{act_id}` {subj} **{pred}** {obj}")
                if raw:
                    lines.append(f"    > {raw}...")
            lines.append("")
        else:
            lines.append("- **performs:** —")
            lines.append("")

        if receives:
            lines.append("- **receives:**")
            for act_id in receives:
                a = actions_reg.get(act_id, {})
                subj = a.get("subject", "")
                pred = a.get("predicate", "")
                obj = a.get("object", "")
                raw = (a.get("raw", "") or "")[:100].replace("\n", " ")
                lines.append(f"  - `{act_id}` {subj} **{pred}** {obj}")
                if raw:
                    lines.append(f"    > {raw}...")
            lines.append("")
        else:
            lines.append("- **receives:** —")
            lines.append("")

        lines.append("- **states:** " + (", ".join(states) if states else "—"))
        lines.append("- **decisions:** " + (", ".join(decisions) if decisions else "—"))
        lines.append("- **relationships:** " + (", ".join(str(r) for r in relationships) if relationships else "—"))
        lines.append("")

    # Appendix: actions registry
    lines.append("---")
    lines.append("")
    lines.append("## registries.actions")
    lines.append("")
    for act_id, a in sorted(actions_reg.items()):
        subj = a.get("subject", "")
        pred = a.get("predicate", "")
        obj = a.get("object", "")
        raw = (a.get("raw", "") or "")[:120].replace("\n", " ")
        lines.append(f"- **{act_id}** {subj} {pred} {obj}")
        if raw:
            lines.append(f"  `{raw}...`")
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Phase 4: Build hypothesis.json from concept signals (concepts + registries format)"
    )
    parser.add_argument(
        "--input-dir", "-i",
        help="Directory with concept signals (default: workspace solution/concept_signals)",
    )
    parser.add_argument(
        "--output", "-o",
        help="Output path for hypothesis.json (default: workspace solution/generated/hypothesis.json)",
    )
    args = parser.parse_args()

    if str(_SKILL_DIR / "scripts") not in sys.path:
        sys.path.insert(0, str(_SKILL_DIR / "scripts"))
    from _config import concept_signals_dir, hypothesis_path

    signals_dir = Path(args.input_dir).resolve() if args.input_dir else concept_signals_dir()
    out_path = Path(args.output).resolve() if args.output else hypothesis_path()

    if not signals_dir.exists():
        print(f"Concept signals dir not found: {signals_dir}", file=sys.stderr)
        sys.exit(1)

    signals = _load_signals(signals_dir)
    core = _build_concepts_and_registries(signals)
    concept_guidance = _build_concept_guidance(signals, core["concepts"])

    # Phase 4: Add chunk_ids per concept (all chunks that touch each concept)
    chunk_ids_map = _collect_chunk_ids_per_concept(signals)
    for name, data in core["concepts"].items():
        ids = chunk_ids_map.get(name, set())
        data["chunk_ids"] = sorted(ids) if ids else []

    hypothesis = {
        "concepts": core["concepts"],
        "registries": core["registries"],
        "concept_guidance": concept_guidance,
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(hypothesis, indent=2, ensure_ascii=False), encoding="utf-8")

    md_path = out_path.with_suffix(".md")
    md_path.write_text(_render_hypothesis_md(hypothesis), encoding="utf-8")

    n_concepts = len(core["concepts"])
    n_actions = len(core["registries"]["actions"])
    print(f"Built hypothesis: {n_concepts} concepts, {n_actions} actions -> {out_path}")
    print(f"Markdown render -> {md_path}")


if __name__ == "__main__":
    main()
