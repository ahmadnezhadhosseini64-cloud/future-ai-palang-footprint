#!/usr/bin/env python3
"""Deterministic, evidence-linked architecture insight candidate extractor.

This proposes ideas from structured outcomes; it does not verify tests or mutate MASTER.
"""
import argparse
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

def extract(record, line_no):
    issues = []
    for key in ("event_id", "stable_id", "test_result"):
        if not str(record.get(key, "")).strip():
            issues.append("required_field_missing:" + key)
    result = str(record.get("test_result", "")).strip().upper()
    if result not in VALID_RESULTS:
        issues.append("invalid_test_result")
    evidence = record.get("evidence", [])
    if not isinstance(evidence, list):
        issues.append("evidence_must_be_list")
        evidence = []
    if result == "PASS" and not evidence:
        issues.append("pass_without_evidence")
    if issues:
        return {"line": line_no, "status": "REJECTED_INPUT", "issues": issues}

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

    domain = record.get("architecture_domain", "architecture")
    if domain not in DOMAINS:
        return {"line": line_no, "status": "REJECTED_INPUT", "issues": ["unknown_architecture_domain:" + str(domain)]}
    source_event = str(record["event_id"])
    test_id = str(record.get("test_id", "unspecified-test"))
    stable = str(record["stable_id"])
    safe = re.sub(r"[^A-Za-z0-9-]", "-", source_event + "-" + test_id)
    return {
        "insight_id": "INS-" + safe,
        "source_event_id": source_event,
        "source_test_id": test_id,
        "source_stable_id": stable,
        "test_result": result,
        "kind": kind,
        "architecture_domain": domain,
        "domain_description": DOMAINS[domain],
        "observation": str(record.get("observation", "")),
        "design_question": question,
        "evidence": evidence,
        "counterexamples": record.get("counterexamples", []),
        "confidence": "UNASSESSED",
        "status": "PROPOSED",
        "promotion": "OWNER_REVIEW_REQUIRED",
        "master_mutation": False,
        "source_line": line_no,
    }

def generate(path):
    proposals, rejected, parse_errors = [], [], []
    for line_no, raw in enumerate(pathlib.Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            record = json.loads(raw)
            if not isinstance(record, dict):
                raise ValueError("record_must_be_object")
            item = extract(record, line_no)
            if item.get("status") == "REJECTED_INPUT":
                rejected.append(item)
            else:
                proposals.append(item)
        except Exception as exc:
            parse_errors.append({"line": line_no, "error": str(exc)})
    return {
        "generator": "PALANG-ARCHITECTURE-INSIGHT-CANDIDATES-1.0.0",
        "source": str(path),
        "records_proposed": len(proposals),
        "records_rejected": len(rejected),
        "parse_errors": parse_errors,
        "proposals": proposals,
        "rejected": rejected,
        "governance": "Candidates are hypotheses, not verified findings. No automatic MASTER mutation. Review evidence, counterexamples, risks, and regression tests.",
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    try:
        report = generate(args.input)
    except FileNotFoundError:
        print("input file not found: " + args.input, file=sys.stderr)
        return 2
    pathlib.Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(args.output).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("records_proposed", "records_rejected", "parse_errors")}, ensure_ascii=False))
    return 1 if report["parse_errors"] or report["records_rejected"] else 0

if __name__ == "__main__":
    raise SystemExit(main())
