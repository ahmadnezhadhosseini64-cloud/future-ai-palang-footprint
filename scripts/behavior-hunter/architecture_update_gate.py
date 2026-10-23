#!/usr/bin/env python3
"""Validate architecture insight proposals and emit a safe, auditable update decision.

This gate produces a decision manifest only. It never edits canonical architecture files.
Canonical integration requires explicit owner approval plus independently verified evidence.
"""
import argparse
import hashlib
import json
from pathlib import Path

ALLOWED_STATES = {"OBSERVED", "HYPOTHESIS", "PROPOSED", "PROTOTYPED", "VERIFIED", "APPROVED", "INTEGRATED", "REJECTED"}
REQUIRED_FIELDS = {
    "insight_id", "title", "version", "originating_event_ids", "category",
    "affected_components", "observed_facts", "hypothesis", "evidence",
    "counterexamples", "proposed_change", "required_tests", "rollback_plan",
    "state", "owner_decision", "target_paths",
}
PROTECTED_PREFIXES = (
    "docs/reference/REFERENCE-DOCUMENTS/",
    "docs/architecture/",
    "docs/0.0/",
    "docs/REFERENCE_INDEX.md",
)

def validate_proposal(proposal, repo_root="."):
    root = Path(repo_root).resolve()
    errors, warnings, evidence_checked = [], [], []
    if not isinstance(proposal, dict):
        return {"status": "BLOCKED", "errors": ["proposal_must_be_json_object"], "warnings": [], "evidence_checked": []}
    missing = sorted(REQUIRED_FIELDS - set(proposal))
    if missing:
        errors.append({"code": "required_fields_missing", "fields": missing})
    state = proposal.get("state")
    if state not in ALLOWED_STATES:
        errors.append({"code": "invalid_state", "state": state, "allowed": sorted(ALLOWED_STATES)})
    for field in ("originating_event_ids", "affected_components", "observed_facts", "evidence", "counterexamples", "required_tests", "target_paths"):
        if field in proposal and not isinstance(proposal[field], list):
            errors.append({"code": "field_must_be_list", "field": field})
    for field in ("insight_id", "title", "version", "category", "hypothesis", "proposed_change", "rollback_plan"):
        if field in proposal and (not isinstance(proposal[field], str) or not proposal[field].strip()):
            errors.append({"code": "field_must_be_nonempty_string", "field": field})
    evidence = proposal.get("evidence", [])
    if isinstance(evidence, list):
        for index, item in enumerate(evidence):
            if not isinstance(item, dict):
                errors.append({"code": "evidence_entry_must_be_object", "index": index})
                continue
            locator = item.get("locator", "")
            expected = item.get("sha256", "")
            if not isinstance(locator, str) or not locator.startswith("repo://"):
                errors.append({"code": "unsupported_evidence_locator", "index": index, "locator": locator})
                continue
            relative = locator[len("repo://"):]
            target = (root / relative).resolve()
            try:
                target.relative_to(root)
            except ValueError:
                errors.append({"code": "evidence_path_escape", "index": index, "locator": locator})
                continue
            if not target.is_file():
                errors.append({"code": "evidence_file_missing", "index": index, "locator": locator})
                continue
            actual = hashlib.sha256(target.read_bytes()).hexdigest()
            if not expected or actual.lower() != str(expected).lower():
                errors.append({"code": "evidence_sha256_mismatch", "index": index, "locator": locator, "expected": expected, "actual": actual})
                continue
            evidence_checked.append({"locator": locator, "sha256": actual, "integrity": "VERIFIED"})
    if not evidence:
        errors.append({"code": "at_least_one_evidence_required"})
    if not proposal.get("observed_facts"):
        errors.append({"code": "observed_facts_required"})
    if not proposal.get("counterexamples"):
        warnings.append("counterexamples_empty_review_required")
    if not proposal.get("required_tests"):
        errors.append({"code": "required_tests_required"})
    owner_decision = proposal.get("owner_decision")
    if owner_decision not in {"PENDING", "APPROVED", "REJECTED"}:
        errors.append({"code": "invalid_owner_decision", "value": owner_decision})
    targets = proposal.get("target_paths", [])
    protected = [p for p in targets if isinstance(p, str) and (p.startswith(PROTECTED_PREFIXES))]
    if protected and not (state in {"APPROVED", "INTEGRATED"} and owner_decision == "APPROVED"):
        warnings.append("protected_architecture_targets_require_owner_approval")
    if state == "INTEGRATED" and owner_decision != "APPROVED":
        errors.append({"code": "integration_without_owner_approval"})
    if state == "INTEGRATED":
        warnings.append("integration_claim_requires_post_integration_readback_and_regression_evidence")
    if state == "APPROVED" and owner_decision != "APPROVED":
        errors.append({"code": "approved_state_without_owner_decision"})
    status = "BLOCKED" if errors else ("READY_FOR_OWNER_REVIEW" if state in {"OBSERVED", "HYPOTHESIS", "PROPOSED", "PROTOTYPED", "VERIFIED"} or owner_decision == "PENDING" else "APPROVAL_RECORDED")
    return {
        "gate": "PALANG-ARCHITECTURE-UPDATE-GATE-1.0.0",
        "status": status,
        "decision_scope": "proposal_validation_only_no_canonical_mutation",
        "insight_id": proposal.get("insight_id"),
        "state": state,
        "owner_decision": owner_decision,
        "evidence_checked": evidence_checked,
        "errors": errors,
        "warnings": warnings,
        "protected_targets": protected,
        "canonical_mutation_performed": False,
        "promotion_allowed": False,
        "required_next_actions": [
            "review evidence and counterexamples",
            "run listed tests in an isolated prototype",
            "record explicit owner decision",
            "after approved integration, rerun relevant regression tests and read back canonical files",
        ],
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    proposal = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = validate_proposal(proposal, args.repo_root)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "errors": len(result["errors"]), "evidence_verified": len(result["evidence_checked"]), "canonical_mutation_performed": False}))
    return 0 if result["status"] != "BLOCKED" else 1

if __name__ == "__main__":
    raise SystemExit(main())
