#!/usr/bin/env python3
"""Validate an owner-redacted RAHM candidate and stage it under CHILD-CANDIDATES.

This script copies only allowlisted, hashed, non-executable public-safe files.
It never contacts GitHub, pushes a branch, merges a PR, or edits the living Master.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

CANDIDATE_RE = re.compile(r"^HAIF-CANDIDATE-[0-9]{8}-[0-9]{3}$")
HOST_RE = re.compile(r"^HAIF-HOST-[0-9]{8}-[0-9]{3}$")
WORKSPACE_RE = re.compile(r"^HAIF-WORKSPACE-[0-9]{8}-[0-9]{3}$")
SOURCE_RE = re.compile(r"^ahmadnezhadhosseini64-cloud/haif-host-[A-Za-z0-9-]+$")
FILE_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,99}\.(md|json|txt|csv)$")
REQUIRED_FILES = {"proposal.md", "evidence.json", "validation.json"}
MAX_FILES = 20
MAX_FILE_BYTES = 1_048_576
MAX_TOTAL_BYTES = 5_242_880
SECRET_PATTERNS = [
    re.compile(rb"gh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(rb"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(rb"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(rb"AKIA[0-9A-Z]{16}"),
    re.compile(rb"(?i)(password|passwd|api[_-]?key|access[_-]?token)\s*[:=]\s*['\"]?[^\s'\"]{12,}"),
]


class CandidateError(ValueError):
    pass


def _safe_child(root: Path, candidate_id: str) -> Path:
    if not CANDIDATE_RE.fullmatch(candidate_id):
        raise CandidateError("INVALID_CANDIDATE_ID")
    root = root.resolve(strict=True)
    candidates_root = root / "candidates"
    if candidates_root.is_symlink() or not candidates_root.is_dir():
        raise CandidateError("CANDIDATES_DIRECTORY_MISSING_OR_SYMLINK")
    candidate = candidates_root / candidate_id
    if candidate.is_symlink() or not candidate.is_dir():
        raise CandidateError("CANDIDATE_DIRECTORY_MISSING_OR_SYMLINK")
    resolved = candidate.resolve(strict=True)
    if candidates_root.resolve(strict=True) not in resolved.parents:
        raise CandidateError("CANDIDATE_PATH_ESCAPES_SOURCE_ROOT")
    return resolved


def validate_candidate(source_root: Path, candidate_id: str) -> tuple[dict, Path, list[Path]]:
    candidate_dir = _safe_child(source_root, candidate_id)
    manifest_path = candidate_dir / "manifest.json"
    if manifest_path.is_symlink() or not manifest_path.is_file():
        raise CandidateError("MANIFEST_MISSING_OR_SYMLINK")
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CandidateError("MANIFEST_INVALID_JSON_OR_UTF8") from exc
    if not isinstance(manifest, dict):
        raise CandidateError("MANIFEST_MUST_BE_OBJECT")

    required = {
        "schema_version", "candidate_id", "host_id", "workspace_id",
        "source_repository", "source_commit_sha", "master_commit_sha",
        "source_session_id", "exported_at_utc", "owner_export_receipt",
        "owner_redaction_attestation", "owner_child_promotion_authorized",
        "owner_approval_ref", "privacy_class", "redaction_status", "files",
    }
    if set(manifest) != required:
        raise CandidateError("MANIFEST_FIELDS_MISMATCH")
    if manifest["schema_version"] != "1.0.0" or manifest["candidate_id"] != candidate_id:
        raise CandidateError("MANIFEST_VERSION_OR_CANDIDATE_ID_MISMATCH")
    if not isinstance(manifest["host_id"], str) or not HOST_RE.fullmatch(manifest["host_id"]):
        raise CandidateError("INVALID_HOST_ID")
    if not isinstance(manifest["workspace_id"], str) or not WORKSPACE_RE.fullmatch(manifest["workspace_id"]):
        raise CandidateError("INVALID_WORKSPACE_ID")
    if not isinstance(manifest["source_repository"], str) or not SOURCE_RE.fullmatch(manifest["source_repository"]):
        raise CandidateError("INVALID_SOURCE_REPOSITORY")
    for key in ("source_commit_sha", "master_commit_sha"):
        if not isinstance(manifest[key], str) or not re.fullmatch(r"[0-9a-f]{40}", manifest[key]):
            raise CandidateError(f"INVALID_{key.upper()}")
    for key in ("source_session_id", "exported_at_utc", "owner_export_receipt", "owner_approval_ref"):
        if not isinstance(manifest[key], str) or not manifest[key].strip():
            raise CandidateError(f"MISSING_{key.upper()}")
    if manifest["owner_redaction_attestation"] != "OWNER_REVIEWED_AND_REDACTED":
        raise CandidateError("OWNER_REDACTION_ATTESTATION_REQUIRED")
    if manifest["owner_child_promotion_authorized"] is not True:
        raise CandidateError("OWNER_CHILD_PROMOTION_NOT_AUTHORIZED")
    if manifest["privacy_class"] != "PUBLIC_REDACTED" or manifest["redaction_status"] != "OWNER_VERIFIED":
        raise CandidateError("PUBLIC_REDACTION_GATE_FAILED")

    entries = manifest["files"]
    if not isinstance(entries, list) or not (3 <= len(entries) <= MAX_FILES):
        raise CandidateError("FILE_COUNT_OUT_OF_RANGE")
    names: set[str] = set()
    total = 0
    verified: list[Path] = []
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != {"path", "sha256", "size_bytes"}:
            raise CandidateError("INVALID_FILE_ENTRY")
        name = entry["path"]
        if not isinstance(name, str) or not FILE_RE.fullmatch(name) or Path(name).name != name:
            raise CandidateError("UNSAFE_FILE_PATH")
        if name in names:
            raise CandidateError("DUPLICATE_FILE_PATH")
        names.add(name)
        path = candidate_dir / name
        if path.is_symlink() or not path.is_file():
            raise CandidateError("MISSING_FILE_OR_SYMLINK")
        resolved = path.resolve(strict=True)
        if candidate_dir not in resolved.parents:
            raise CandidateError("FILE_PATH_ESCAPES_CANDIDATE")
        data = path.read_bytes()
        if not isinstance(entry["size_bytes"], int) or entry["size_bytes"] != len(data):
            raise CandidateError("BYTE_COUNT_MISMATCH")
        if len(data) < 1 or len(data) > MAX_FILE_BYTES:
            raise CandidateError("FILE_SIZE_OUT_OF_RANGE")
        total += len(data)
        if total > MAX_TOTAL_BYTES:
            raise CandidateError("TOTAL_PAYLOAD_TOO_LARGE")
        digest = hashlib.sha256(data).hexdigest()
        if entry["sha256"] != digest:
            raise CandidateError("SHA256_MISMATCH")
        if any(pattern.search(data) for pattern in SECRET_PATTERNS):
            raise CandidateError("POSSIBLE_SECRET_DETECTED")
        if path.suffix.lower() == ".json":
            try:
                json.loads(data.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                raise CandidateError("INVALID_JSON_PAYLOAD") from exc
        verified.append(path)
    if not REQUIRED_FILES.issubset(names):
        raise CandidateError("REQUIRED_CANDIDATE_FILES_MISSING")

    entries_on_disk = list(candidate_dir.iterdir())
    if any(p.is_symlink() or not p.is_file() for p in entries_on_disk):
        raise CandidateError("NON_REGULAR_ENTRY_OR_SYMLINK_NOT_ALLOWED")
    actual_files = {p.name for p in entries_on_disk if p.name != "manifest.json"}
    if actual_files != names:
        raise CandidateError("UNMANIFESTED_OR_MISSING_FILES")
    return manifest, candidate_dir, verified


def stage_candidate(source_root: Path, target_root: Path, candidate_id: str) -> Path:
    manifest, source_dir, files = validate_candidate(source_root, candidate_id)
    target_root = target_root.resolve(strict=True)
    destination_parent = target_root / "docs" / "architecture" / "CHILD-CANDIDATES"
    for parent in (target_root / "docs", target_root / "docs" / "architecture", destination_parent):
        if parent.is_symlink():
            raise CandidateError("TARGET_PATH_COMPONENT_IS_SYMLINK")
    destination = destination_parent / candidate_id
    if destination.exists() or destination.is_symlink():
        raise CandidateError("CHILD_CANDIDATE_ALREADY_EXISTS")
    destination.mkdir(parents=True)
    shutil.copyfile(source_dir / "manifest.json", destination / "candidate-manifest.json")
    for source in files:
        shutil.copyfile(source, destination / source.name)
    readme = (
        f"# {candidate_id}\n\n"
        f"- Host ID: {manifest['host_id']}\n"
        f"- Workspace ID: {manifest['workspace_id']}\n"
        f"- Source repository: {manifest['source_repository']}\n"
        f"- Source commit: {manifest['source_commit_sha']}\n"
        f"- Master snapshot: {manifest['master_commit_sha']}\n"
        f"- Exported at UTC: {manifest['exported_at_utc']}\n"
        f"- Owner export receipt: {manifest['owner_export_receipt']}\n"
        f"- Owner approval reference: {manifest['owner_approval_ref']}\n"
        f"- Admission status: BOT_PR_OPEN / OWNER_REVIEW_REQUIRED\n\n"
        "This is a sanitized Child candidate only. It is not part of the living Master. "
        "No automatic merge or Master promotion is performed.\n"
    )
    (destination / "README.md").write_text(readme, encoding="utf-8")
    return destination


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--target-root", type=Path, required=True)
    parser.add_argument("--candidate-id", required=True)
    args = parser.parse_args()
    try:
        destination = stage_candidate(args.source_root, args.target_root, args.candidate_id)
    except (CandidateError, OSError) as exc:
        print(f"RAHM_PROMOTION_REJECTED={exc}")
        return 2
    print(f"RAHM_PROMOTION_VALIDATED={args.candidate_id}")
    print(f"CHILD_STAGING_PATH={destination.relative_to(args.target_root.resolve())}")
    print("MASTER_MODIFIED=false")
    print("AUTO_MERGE=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
