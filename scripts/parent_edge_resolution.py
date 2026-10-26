"""Evidence-governed parent-edge resolution for the historical graph builder."""


def resolve_parent_target(source_path, parent_id, candidates, canonical_preferred_paths, source_parent_overrides):
    """Return (resolution, selected_path, warning).

    Source-specific decisions outrank global preferences because short IDs can be
    reused by distinct events. An invalid source-specific override is kept
    ambiguous rather than falling back to a potentially misleading global choice.
    """
    candidates = sorted(set(candidates))
    key = (source_path, parent_id)
    if key in source_parent_overrides:
        preferred = source_parent_overrides[key]
        if preferred in candidates:
            return "SOURCE_SPECIFIC_OVERRIDE", preferred, None
        return "AMBIGUOUS", None, {
            "reason": "source_specific_override_not_in_candidates",
            "preferred_path": preferred,
            "candidate_paths": candidates,
        }

    preferred = canonical_preferred_paths.get(parent_id)
    if preferred and preferred in candidates:
        return "CANONICAL_PREFERRED_WITH_DUPLICATE_OCCURRENCES", preferred, None
    if not candidates:
        return "UNRESOLVED", None, None
    if len(candidates) == 1:
        return "UNIQUE", candidates[0], None
    return "AMBIGUOUS", None, None
