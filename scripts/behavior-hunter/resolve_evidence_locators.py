#!/usr/bin/env python3
"""Resolve local repository evidence against an immutable SHA-256 digest.

Only repo:// locators are resolved. External URLs are explicitly unresolved;
this module does not make network requests or trust a URL's appearance.
"""
import argparse
import hashlib
import json
import os
import pathlib
import re
import sys


def resolve_locator(locator, expected_sha256, repo_root):
    if not isinstance(locator, str) or not locator.strip():
        return {"status": "UNRESOLVED", "reason": "locator_missing"}
    locator = locator.strip()
    if not locator.startswith("repo://"):
        return {"status": "UNSUPPORTED_LOCATOR", "reason": "only_repo_scheme_is_resolved"}
    if not isinstance(expected_sha256, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", expected_sha256):
        return {"status": "UNRESOLVED", "reason": "invalid_or_missing_content_sha256"}

    relative = locator[len("repo://"):]
    rel = pathlib.PurePosixPath(relative)
    if not relative or rel.is_absolute() or any(part in ("", ".", "..") for part in rel.parts):
        return {"status": "UNRESOLVED", "reason": "unsafe_relative_path"}

    root = pathlib.Path(repo_root).resolve()
    candidate = root.joinpath(*rel.parts)
    try:
        resolved = candidate.resolve(strict=True)
    except (FileNotFoundError, OSError, RuntimeError):
        return {"status": "UNRESOLVED", "reason": "file_not_found_or_unresolvable"}
    try:
        if os.path.commonpath((str(root), str(resolved))) != str(root):
            return {"status": "UNRESOLVED", "reason": "path_escapes_repository_root"}
    except ValueError:
        return {"status": "UNRESOLVED", "reason": "path_escapes_repository_root"}
    if not resolved.is_file():
        return {"status": "UNRESOLVED", "reason": "locator_not_regular_file"}

    actual = hashlib.sha256(resolved.read_bytes()).hexdigest()
    if actual.lower() != expected_sha256.lower():
        return {
            "status": "HASH_MISMATCH",
            "reason": "content_sha256_mismatch",
            "actual_sha256": actual,
            "expected_sha256": expected_sha256.lower(),
        }
    return {
        "status": "RESOLVED",
        "reason": "content_sha256_verified",
        "relative_path": resolved.relative_to(root).as_posix(),
        "content_sha256": actual,
    }


def resolve_record(record, repo_root, source_mode="production"):
    if source_mode == "fixture":
        return {
            "event_id": record.get("event_id"),
            "test_id": record.get("test_id"),
            "status": "FIXTURE_ONLY",
            "evidence": [],
            "production_claim_allowed": False,
        }
    evidence = record.get("evidence", [])
    if not isinstance(evidence, list):
        return {
            "event_id": record.get("event_id"),
            "test_id": record.get("test_id"),
            "status": "UNRESOLVED",
            "evidence": [],
            "production_claim_allowed": False,
            "reason": "evidence_must_be_list",
        }
    if str(record.get("test_result", "")).strip().upper() == "PASS" and not evidence:
        return {
            "event_id": record.get("event_id"),
            "test_id": record.get("test_id"),
            "status": "UNRESOLVED",
            "evidence": [],
            "production_claim_allowed": False,
            "reason": "pass_without_evidence",
        }
    outcomes = []
    for index, item in enumerate(evidence):
        if not isinstance(item, dict):
            outcomes.append({"index": index, "status": "UNRESOLVED", "reason": "evidence_item_must_be_object"})
            continue
        result = resolve_locator(item.get("locator"), item.get("content_sha256"), repo_root)
        outcomes.append({"index": index, **result})
    status = "RESOLVED" if outcomes and all(item["status"] == "RESOLVED" for item in outcomes) else ("NO_EVIDENCE" if not outcomes else "UNRESOLVED")
    return {
        "event_id": record.get("event_id"),
        "test_id": record.get("test_id"),
        "status": status,
        "evidence": outcomes,
        "production_claim_allowed": status == "RESOLVED",
    }


def generate(input_path, repo_root, source_mode="production"):
    records, parse_errors = [], []
    for line_no, raw in enumerate(pathlib.Path(input_path).read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            record = json.loads(raw)
            if not isinstance(record, dict):
                records.append({"line": line_no, "status": "UNRESOLVED", "reason": "record_must_be_object", "production_claim_allowed": False})
                continue
            item = resolve_record(record, repo_root, source_mode)
            item["line"] = line_no
            records.append(item)
        except json.JSONDecodeError as exc:
            parse_errors.append({"line": line_no, "error": str(exc)})
    unresolved = sum(1 for item in records if item.get("status") not in ("RESOLVED", "FIXTURE_ONLY", "NO_EVIDENCE"))
    return {
        "resolver": "PALANG-EVIDENCE-LOCATOR-RESOLVER-1.0.0",
        "source_mode": "FIXTURE_ONLY" if source_mode == "fixture" else "PRODUCTION",
        "records_read": len(records),
        "records_resolved": sum(1 for item in records if item.get("status") == "RESOLVED"),
        "records_fixture_only": sum(1 for item in records if item.get("status") == "FIXTURE_ONLY"),
        "records_unresolved": unresolved,
        "parse_errors": parse_errors,
        "records": records,
        "governance": "Only repo:// files whose bytes match the declared content_sha256 resolve. External locators are unsupported and never count as PASS. Fixture mode is demonstration-only.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--source-mode", choices=("production", "fixture"), default="production")
    args = parser.parse_args()
    try:
        report = generate(args.input, args.repo_root, args.source_mode)
    except FileNotFoundError:
        print("input file not found: " + args.input, file=sys.stderr)
        return 2
    pathlib.Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(args.output).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("records_read", "records_resolved", "records_fixture_only", "records_unresolved", "parse_errors")}, ensure_ascii=False))
    return 1 if report["records_unresolved"] or report["parse_errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
