#!/usr/bin/env python3
"""Deterministic, provenance-aware architecture insight candidate extractor.

Outputs hypotheses only. It does not execute tests, verify remote evidence,
capture live host interactions, or mutate MASTER.
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

VALID_RESULTS = {"PASS", "FAIL", "BLOCKED", "NOT RUN"}
DOMAINS = {
    "architecture": "architecture structure and component boundaries",
    "interface": "interfaces and adapters",
    "schema": "schemas and data contracts",
    "provenance": "identifiers, timestamps, anchors, and evidence provenance",
    "recovery": "continuity, restart recovery, and resume pointers",
    "verification": "test quality, evidence gates, and destination-state honesty",
    "interaction": "user interaction and output quality",
    "automation": "automation, CI, and observability",
    "privacy": "privacy, security, and data minimization",
    "patterns": "reusable patterns, anti-patterns, and regression coverage",
    "documentation": "documentation and recovery instructions",
}
REQUIRED_FIELDS = ("event_id", "stable_id", "version", "test_id", "test_result", "architecture_domain", "observation")
PLACEHOLDER_PREFIXES = ("example:", "fixture:", "mock:", "placeholder:", "todo:")


def _nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def _validate_evidence(evidence, result, source_mode):
    issues = []
    if not isinstance(evidence, list):
        return ["evidence_must_be_list"]
    if result == "PASS" and not evidence:
        issues.append("pass_without_evidence")
    for index, item in enumerate(evidence):
        prefix = "evidence[{0}]".format(index)
        if not isinstance(item, dict):
            issues.append(prefix + "_must_be_object")
            continue
        for key in ("type", "locator"):
            if not _nonempty(item.get(key)):
                issues.append(prefix + "_missing_" + key)
        if source_mode == "production" and any(
            str(item.get("locator", "")).strip().lower().startswith(p)
            for p in PLACEHOLDER_PREFIXES
        ):
            issues.append(prefix + "_placeholder_locator_not_allowed_in_production")
        if source_mode == "production" and result == "PASS":
            for key in ("execution_id", "source_sha"):
                if not _nonempty(item.get(key)):
                    issues.append(prefix + "_missing_" + key)
    return issues


def extract(record, line_no, source_mode="production"):
    issues = []
    if source_mode not in ("production", "fixture"):
        return {"line": line_no, "status": "REJECTED_INPUT", "issues": ["invalid_source_mode"]}
    for key in REQUIRED_FIELDS:
        if not _nonempty(record.get(key)):
            issues.append("required_field_missing:" + key)
    result = str(record.get("test_result", "")).strip().upper()
    if result not in VALID_RESULTS:
        issues.append("invalid_test_result")
    domain = record.get("architecture_domain")
    if domain not in DOMAINS:
        issues.append("unknown_architecture_domain:" + str(domain))
    issues.extend(_validate_evidence(record.get("evidence", []), result, source_mode))
    counterexamples = record.get("counterexamples", [])
    if not isinstance(counterexamples, list) or any(not isinstance(x, str) for x in counterexamples):
        issues.append("counterexamples_must_be_list_of_strings")
    if issues:
        return {"line": line_no, "status": "REJECTED_INPUT", "issues": sorted(set(issues))}

    if result == "PASS":
        kind = "PATTERN_CANDIDATE"
        question = "Which invariant or design choice made this exact test pass, and what independent cases could establish generality?"
    elif result == "FAIL":
        kind = "REGRESSION_OR_ANTIPATTERN_CANDIDATE"
        question = "What root cause or counterexample does this failure reveal, and which regression test should preserve it?"
    elif result == "BLOCKED":
        kind = "ARCHITECTURE_GAP_CANDIDATE"
        question = "Which missing interface, permission, destination, or observability capability caused the block?"
    else:
        kind = "EVIDENCE_GAP_CANDIDATE"
        question = "What evidence source or execution step is required before this case can be verified?"

    source_event = record["event_id"].strip()
    test_id = record["test_id"].strip()
    stable = record["stable_id"].strip()
    identity = source_event + "::" + test_id
    digest = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:16]
    is_fixture = source_mode == "fixture"
    return {
        "insight_id": "INS-" + digest,
        "source_event_id": source_event,
        "source_test_id": test_id,
        "source_stable_id": stable,
        "source_version": record["version"].strip(),
        "source_mode": "FIXTURE_ONLY" if is_fixture else "PRODUCTION_CANDIDATE",
        "test_result": result,
        "kind": kind,
        "architecture_domain": domain,
        "domain_description": DOMAINS[domain],
        "observation": record["observation"].strip(),
        "design_question": question,
        "evidence": record.get("evidence", []),
        "counterexamples": counterexamples,
        "confidence": "UNASSESSED",
        "status": "DEMONSTRATION_ONLY" if is_fixture else "PROPOSED",
        "promotion": "NONE_FIXTURE_ONLY" if is_fixture else "OWNER_REVIEW_REQUIRED",
        "master_mutation": False,
        "source_line": line_no,
    }


def generate(path, source_mode="production"):
    proposals, rejected, parse_errors = [], [], []
    seen = set()
    duplicate_ids = []
    for line_no, raw in enumerate(pathlib.Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            record = json.loads(raw)
            if not isinstance(record, dict):
                rejected.append({"line": line_no, "status": "REJECTED_INPUT", "issues": ["record_must_be_object"]})
                continue
            item = extract(record, line_no, source_mode=source_mode)
            if item.get("status") == "REJECTED_INPUT":
                rejected.append(item)
                continue
            identity = (item["source_event_id"], item["source_test_id"])
            if identity in seen:
                duplicate_ids.append({
                    "line": line_no,
                    "source_event_id": identity[0],
                    "source_test_id": identity[1],
                    "status": "DUPLICATE_REJECTED",
                })
                continue
            seen.add(identity)
            proposals.append(item)
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            parse_errors.append({"line": line_no, "error": str(exc)})
    return {
        "generator": "PALANG-ARCHITECTURE-INSIGHT-CANDIDATES-1.1.0",
        "source": str(path),
        "source_mode": "FIXTURE_ONLY" if source_mode == "fixture" else "PRODUCTION_CANDIDATE",
        "records_proposed": len(proposals),
        "records_rejected": len(rejected),
        "duplicate_records_rejected": len(duplicate_ids),
        "parse_errors": parse_errors,
        "proposals": proposals,
        "rejected": rejected,
        "duplicates": duplicate_ids,
        "governance": "Candidates are hypotheses, not verified findings. Fixture-mode outputs are demonstration-only. Production PASS requires evidence type, resolvable locator, execution_id, and source_sha; no automatic MASTER mutation.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--source-mode", choices=("production", "fixture"), default="production")
    args = parser.parse_args()
    try:
        report = generate(args.input, source_mode=args.source_mode)
    except FileNotFoundError:
        print("input file not found: " + args.input, file=sys.stderr)
        return 2
    pathlib.Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(args.output).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("records_proposed", "records_rejected", "duplicate_records_rejected", "parse_errors")}, ensure_ascii=False))
    return 1 if report["parse_errors"] or report["records_rejected"] or report["duplicate_records_rejected"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
