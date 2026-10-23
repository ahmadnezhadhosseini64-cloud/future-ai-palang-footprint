#!/usr/bin/env python3
"""Validate append-only, versioned architecture change records.

The validator never edits records or canonical architecture. It checks the history
provided in JSONL and emits a review manifest.
"""
import argparse
import hashlib
import json
from pathlib import Path

ALLOWED_STATES = {"OBSERVED", "HYPOTHESIS", "PROPOSED", "PROTOTYPED", "VERIFIED", "APPROVED", "INTEGRATED", "REJECTED"}
REQUIRED = {"change_id", "version", "sequence", "state", "supersedes", "owner_decision", "source_event_ids", "evidence_refs", "target_paths", "rollback_plan", "previous_record_sha256", "record_sha256"}

def validate_records(records):
    errors, warnings = [], []
    seen_ids, seen_sequences = set(), set()
    latest_by_id = {}
    accepted = 0
    previous_hash = "GENESIS"
    for i, r in enumerate(records, start=1):
        if not isinstance(r, dict):
            errors.append({"line": i, "code": "record_not_object"})
            continue
        missing = sorted(REQUIRED - set(r))
        if missing:
            errors.append({"line": i, "code": "required_fields_missing", "fields": missing})
            continue
        cid, version, seq = r["change_id"], r["version"], r["sequence"]
        if not isinstance(cid, str) or not cid.strip():
            errors.append({"line": i, "code": "invalid_change_id"})
            continue
        if not isinstance(seq, int) or seq < 1:
            errors.append({"line": i, "code": "invalid_sequence"})
        if seq in seen_sequences:
            errors.append({"line": i, "code": "duplicate_sequence", "sequence": seq})
        seen_sequences.add(seq)
        pair = (cid, version)
        if pair in seen_ids:
            errors.append({"line": i, "code": "duplicate_change_version", "change_id": cid, "version": version})
        seen_ids.add(pair)
        if r["state"] not in ALLOWED_STATES:
            errors.append({"line": i, "code": "invalid_state", "state": r["state"]})
        if not isinstance(r["source_event_ids"], list) or not r["source_event_ids"]:
            errors.append({"line": i, "code": "source_events_required"})
        if not isinstance(r["evidence_refs"], list) or not r["evidence_refs"]:
            errors.append({"line": i, "code": "evidence_refs_required"})
        if not isinstance(r["target_paths"], list) or not r["target_paths"]:
            errors.append({"line": i, "code": "target_paths_required"})
        if not isinstance(r["rollback_plan"], str) or not r["rollback_plan"].strip():
            errors.append({"line": i, "code": "rollback_plan_required"})
        if r["owner_decision"] not in {"PENDING", "APPROVED", "REJECTED"}:
            errors.append({"line": i, "code": "invalid_owner_decision"})
        if r.get("previous_record_sha256") != previous_hash:
            errors.append({"line": i, "code": "hash_chain_link_mismatch", "expected_previous": previous_hash, "actual_previous": r.get("previous_record_sha256")})
        unhashed = {k: v for k, v in r.items() if k != "record_sha256"}
        canonical = json.dumps(unhashed, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
        actual_hash = hashlib.sha256(canonical).hexdigest()
        if r.get("record_sha256") != actual_hash:
            errors.append({"line": i, "code": "record_hash_mismatch", "expected": actual_hash, "actual": r.get("record_sha256")})
        previous_hash = actual_hash
        prior = latest_by_id.get(cid)
        if prior is None:
            if r["supersedes"] not in (None, "", []):
                errors.append({"line": i, "code": "first_version_cannot_supersede", "supersedes": r["supersedes"]})
        else:
            if r["supersedes"] != prior["version"]:
                errors.append({"line": i, "code": "version_chain_break", "expected_supersedes": prior["version"], "actual_supersedes": r["supersedes"]})
            if isinstance(seq, int) and isinstance(prior["sequence"], int) and seq <= prior["sequence"]:
                errors.append({"line": i, "code": "sequence_not_increasing"})
        if r["state"] == "INTEGRATED" and r["owner_decision"] != "APPROVED":
            errors.append({"line": i, "code": "integration_without_owner_approval"})
        if r["state"] == "APPROVED" and r["owner_decision"] != "APPROVED":
            errors.append({"line": i, "code": "approved_state_without_owner_decision"})
        latest_by_id[cid] = r
        accepted += 1
    if not records:
        errors.append({"line": 0, "code": "empty_ledger"})
    return {
        "validator": "PALANG-APPEND-ONLY-ARCHITECTURE-LEDGER-1.0.0",
        "status": "BLOCKED" if errors else "PASS",
        "records_checked": len(records),
        "records_structurally_read": accepted,
        "unique_change_versions": len(seen_ids),
        "change_streams": len(latest_by_id),
        "errors": errors,
        "warnings": warnings,
        "hash_chain_verified": not any(e["code"] in {"hash_chain_link_mismatch", "record_hash_mismatch"} for e in errors),
        "canonical_mutation_performed": False,
        "history_rewritten": False,
        "governance": "Append-only validation only; it does not approve proposals or integrate canonical architecture.",
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    records = []
    for line_no, line in enumerate(Path(args.input).read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            records.append({"_parse_error": str(exc), "_line": line_no})
    result = validate_records(records)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "records_checked": result["records_checked"], "errors": len(result["errors"]), "history_rewritten": False}))
    return 0 if result["status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
