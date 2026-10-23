#!/usr/bin/env python3
"""Deterministic candidate-test generator for structured HAIF interaction pairs."""
import argparse, json, pathlib, re, sys

REQUIRED = ("event_id", "stable_id", "version", "input", "output")
SUCCESS_WORDS = re.compile(r"\b(PASS|VERIFIED|READ-BACK VERIFIED|REGISTERED|EXECUTED SUCCESSFULLY)\b", re.I)

def evaluate(record):
    issues = []
    for key in REQUIRED:
        value = record.get(key)
        if not isinstance(value, str) or not value.strip():
            issues.append(f"required_field_missing:{key}")
    evidence = record.get("evidence", [])
    if not isinstance(evidence, list):
        issues.append("evidence_must_be_list")
        evidence = []
    output = record.get("output", "")
    if isinstance(output, str) and SUCCESS_WORDS.search(output):
        if not evidence:
            issues.append("success_claim_without_evidence")
    destinations = record.get("destinations")
    if destinations is not None and not isinstance(destinations, dict):
        issues.append("destinations_must_be_object")
    invariants = record.get("expected_invariants", [])
    if not isinstance(invariants, list):
        issues.append("expected_invariants_must_be_list")
        invariants = []
    for inv in invariants:
        if inv == "destination_states_explicit":
            if not isinstance(destinations, dict) or not destinations:
                issues.append("invariant_failed:destination_states_explicit")
        elif inv == "resume_pointer_present":
            if not str(record.get("resume_pointer", "")).strip():
                issues.append("invariant_failed:resume_pointer_present")
        elif inv == "success_claims_have_evidence":
            if isinstance(output, str) and SUCCESS_WORDS.search(output) and not evidence:
                issues.append("invariant_failed:success_claims_have_evidence")
        elif inv == "input_present" and not str(record.get("input", "")).strip():
            issues.append("invariant_failed:input_present")
        elif inv == "output_present" and not str(record.get("output", "")).strip():
            issues.append("invariant_failed:output_present")
        elif inv not in {"destination_states_explicit","resume_pointer_present","success_claims_have_evidence","input_present","output_present"}:
            issues.append(f"unsupported_invariant:{inv}")
    return issues

def generate(path):
    records, tests, errors = [], [], []
    for line_no, raw in enumerate(pathlib.Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            rec = json.loads(raw)
            if not isinstance(rec, dict):
                raise ValueError("record_must_be_object")
            issues = evaluate(rec)
            event = str(rec.get("event_id", f"line-{line_no}"))
            tests.append({
                "test_id": f"BH-{line_no:04d}-{re.sub(r'[^A-Za-z0-9-]', '-', event)}",
                "source_event_id": event,
                "status": "CANDIDATE_FAIL" if issues else "CANDIDATE_READY",
                "execution_status": "NOT_RUN",
                "issues": issues,
                "source_line": line_no
            })
            records.append(rec)
        except Exception as exc:
            errors.append({"line": line_no, "error": str(exc)})
    return {"generator": "PALANG-BEHAVIOR-HUNTER-1.0.0",
            "source": str(path), "records_read": len(records),
            "candidate_tests_generated": len(tests), "parse_errors": errors,
            "candidate_tests": tests,
            "promotion_rule": "No candidate is PASS and no candidate auto-promotes to MASTER."}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()
    try:
        report = generate(args.input)
    except FileNotFoundError:
        print(f"input file not found: {args.input}", file=sys.stderr)
        return 2
    pathlib.Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(args.output).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("records_read","candidate_tests_generated","parse_errors")}, ensure_ascii=False))
    return 1 if report["parse_errors"] or any(t["status"] == "CANDIDATE_FAIL" for t in report["candidate_tests"]) else 0

if __name__ == "__main__":
    raise SystemExit(main())
