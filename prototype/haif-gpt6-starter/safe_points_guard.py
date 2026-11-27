"""Fail-closed attestation gate for the Copy 2 -> owner review bridge.

MAIN and Copy 1 are distinct authority points and are NOT required to share a
SHA or tree. A signed receipt must bind the live refs, Copy 2 base/head, exact
diff, allowed paths, checks, verifier run, nonce and expiry. This candidate-side
code is only a verifier client; it is not an independent trust boundary.
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
import re
import subprocess
import tempfile
import time
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any


class Gate(str, Enum):
    BLOCKED = "BLOCKED"
    OWNER_REVIEW = "OWNER_REVIEW_ONLY"


@dataclass(frozen=True)
class Verification:
    gate: Gate
    reason: str


FULL_SHA = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
REQUIRED_FIELDS = (
    "schema", "issuer", "repository", "main_sha", "copy1_sha",
    "copy2_base_sha", "copy2_head_sha", "diff_sha256", "changed_paths",
    "tests_pass", "paths_authorized", "bridge_matches", "verifier_run_id",
    "issued_at", "expires_at", "nonce",
)
REQUIRED_TRUE = ("tests_pass", "paths_authorized", "bridge_matches")
DEFAULT_ALLOWED_PATHS = frozenset({
    ".github/workflows/palang-safe-copy2-validation.yml",
    ".github/workflows/palang-copy3-proposal-intake.yml",
    "prototype/haif-gpt6-starter/copy3_intake_guard.py",
    "prototype/haif-gpt6-starter/test_safe_copy3_intake_guard.py",
    "prototype/haif-gpt6-starter/ONE_MESSAGE_HOST_BOOTSTRAP_FA.md",
    "prototype/haif-gpt6-starter/UNIVERSAL_AI_HOST_ENTRY_FA.md",
    "prototype/universal-host/UNIVERSAL_AI_HOST_ENTRY_FA.md",
    "prototype/haif-gpt6-starter/test_host_entry_sync.py",
    "prototype/haif-gpt6-starter/manifest.json",
    "docs/architecture/SAFE-COPY/COPY2-OWNER-COMMAND-CONTROL-PLANE.md",
    "prototype/haif-gpt6-starter/safe_copy_audit.py",
    "prototype/haif-gpt6-starter/test_safe_copy_audit.py",
    "prototype/haif-gpt6-starter/safe_points_guard.py",
    "prototype/haif-gpt6-starter/test_safe_points_guard.py",
})


def _git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args], capture_output=True, text=True,
        check=False,
    )
    if result.returncode:
        raise ValueError(f"git command failed: {result.stderr.strip()}")
    return result.stdout.strip()


def _git_bytes(root: Path, *args: str) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(root), *args], capture_output=True, check=False,
    )
    if result.returncode:
        raise ValueError("git diff evidence could not be read")
    return result.stdout


def _canonical_payload(packet: dict[str, Any]) -> bytes:
    return json.dumps(
        packet, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def _verify_signature(payload: bytes, signature_b64: str, public_key_pem: str) -> bool:
    try:
        signature = base64.b64decode(signature_b64, validate=True)
        if not signature or not public_key_pem.strip():
            return False
        with tempfile.TemporaryDirectory(prefix="palang-attestation-") as tmp:
            root = Path(tmp)
            payload_path = root / "payload.json"
            signature_path = root / "signature.bin"
            key_path = root / "verifier-public.pem"
            payload_path.write_bytes(payload)
            signature_path.write_bytes(signature)
            key_path.write_text(public_key_pem, encoding="utf-8")
            result = subprocess.run(
                ["openssl", "dgst", "-sha256", "-verify", str(key_path),
                 "-signature", str(signature_path), str(payload_path)],
                capture_output=True, text=True, check=False,
            )
            return result.returncode == 0 and "Verified OK" in result.stdout
    except (ValueError, OSError, subprocess.SubprocessError):
        return False


def evaluate_attestation(
    packet: dict[str, Any],
    signature_b64: str,
    *,
    repo_root: Path,
    repository: str,
    allowed_paths: frozenset[str] = DEFAULT_ALLOWED_PATHS,
    now: int | None = None,
) -> Verification:
    """Verify a signed external receipt; never trust candidate-supplied PASS booleans."""
    public_key = os.environ.get("PALANG_TRUSTED_VERIFIER_PUBLIC_KEY", "")
    main_pin = os.environ.get("PALANG_GOLDEN_MAIN_SHA", "")
    copy1_pin = os.environ.get("PALANG_SAFE_COPY1_SHA", "")
    main_ref = os.environ.get("PALANG_GOLDEN_MAIN_REF", "refs/remotes/origin/main")
    copy1_ref = os.environ.get(
        "PALANG_SAFE_COPY1_REF",
        "refs/remotes/origin/palang-safe-copy-1-baseline-20261126",
    )
    if not isinstance(signature_b64, str) or not signature_b64.strip():
        return Verification(Gate.BLOCKED, "external verifier signature is missing or malformed")
    if not public_key.strip() or not FULL_SHA.fullmatch(main_pin) or not FULL_SHA.fullmatch(copy1_pin):
        return Verification(Gate.BLOCKED, "trusted verifier key or independent MAIN/Copy1 pins are absent")

    if not isinstance(packet, dict) or any(key not in packet for key in REQUIRED_FIELDS):
        return Verification(Gate.BLOCKED, "attestation schema is incomplete")
    if packet.get("schema") != "palang.external-verification.v2":
        return Verification(Gate.BLOCKED, "unsupported attestation schema")
    if packet.get("issuer") != "palang-independent-verifier":
        return Verification(Gate.BLOCKED, "untrusted attestation issuer")
    if packet.get("repository") != repository:
        return Verification(Gate.BLOCKED, "repository identity mismatch")

    for key in ("main_sha", "copy1_sha", "copy2_base_sha", "copy2_head_sha"):
        if not isinstance(packet.get(key), str) or not FULL_SHA.fullmatch(packet[key]):
            return Verification(Gate.BLOCKED, f"invalid {key}")
    if not isinstance(packet.get("diff_sha256"), str) or not SHA256.fullmatch(packet["diff_sha256"]):
        return Verification(Gate.BLOCKED, "invalid diff_sha256")
    if not all(packet.get(key) is True for key in REQUIRED_TRUE):
        return Verification(Gate.BLOCKED, "one or more independently verified checks did not pass")

    changed = packet.get("changed_paths")
    if not isinstance(changed, list) or not changed or any(not isinstance(p, str) for p in changed):
        return Verification(Gate.BLOCKED, "changed_paths is invalid")
    if changed != sorted(set(changed)) or not set(changed).issubset(allowed_paths):
        return Verification(Gate.BLOCKED, "changed paths are not an exact authorized allowlist subset")
    if not isinstance(packet.get("verifier_run_id"), str) or not packet["verifier_run_id"].strip():
        return Verification(Gate.BLOCKED, "verifier run identity is missing")
    if not isinstance(packet.get("nonce"), str) or len(packet["nonce"]) < 16:
        return Verification(Gate.BLOCKED, "one-use verifier nonce is missing")

    issued_at, expires_at = packet.get("issued_at"), packet.get("expires_at")
    if type(issued_at) is not int or type(expires_at) is not int:
        return Verification(Gate.BLOCKED, "attestation time bounds are invalid")
    current = int(time.time()) if now is None else now
    if issued_at > current + 30 or expires_at <= current or expires_at <= issued_at or expires_at - issued_at > 600:
        return Verification(Gate.BLOCKED, "attestation is expired, future-dated, or exceeds the 10-minute validity window")

    try:
        root = Path(repo_root).resolve()
        main_sha = _git(root, "rev-parse", "--verify", f"{main_ref}^{{commit}}")
        copy1_sha = _git(root, "rev-parse", "--verify", f"{copy1_ref}^{{commit}}")
        head_sha = _git(root, "rev-parse", "--verify", "HEAD^{commit}")
        if not all(FULL_SHA.fullmatch(value) for value in (main_sha, copy1_sha, head_sha)):
            return Verification(Gate.BLOCKED, "live refs did not resolve to full commit SHAs")
        if main_sha != main_pin or packet["main_sha"] != main_pin:
            return Verification(Gate.BLOCKED, "MAIN ref does not match its separately trusted pin")
        if copy1_sha != copy1_pin or packet["copy1_sha"] != copy1_pin:
            return Verification(Gate.BLOCKED, "Copy 1 ref does not match its separately trusted pin")
        if packet["copy2_base_sha"] != copy1_pin:
            return Verification(Gate.BLOCKED, "Copy 2 base is not the exact current Copy 1 SHA")
        if packet["copy2_head_sha"] != head_sha:
            return Verification(Gate.BLOCKED, "attestation is not bound to the checked-out Copy 2 HEAD")
        merge_base = _git(root, "merge-base", copy1_sha, head_sha)
        if merge_base != copy1_sha:
            return Verification(Gate.BLOCKED, "Copy 2 is stale or not descended from current Copy 1")
        actual_paths = sorted(filter(None, _git(root, "diff", "--name-only", f"{copy1_sha}...{head_sha}").splitlines()))
        if actual_paths != changed or not set(actual_paths).issubset(allowed_paths):
            return Verification(Gate.BLOCKED, "signed changed-path list does not match the live diff")
        actual_diff = _git_bytes(root, "diff", "--binary", f"{copy1_sha}...{head_sha}")
        if hashlib.sha256(actual_diff).hexdigest() != packet["diff_sha256"]:
            return Verification(Gate.BLOCKED, "signed diff digest does not match the live diff")
    except (OSError, ValueError, subprocess.SubprocessError):
        return Verification(Gate.BLOCKED, "live Git evidence could not be verified")

    if not _verify_signature(_canonical_payload(packet), signature_b64, public_key):
        return Verification(Gate.BLOCKED, "external verifier signature is invalid")
    return Verification(Gate.OWNER_REVIEW, "independent signed evidence verified; owner decision only")


def bridge_destination() -> str:
    """The bridge is review-only and has no write, merge, or promotion capability."""
    return "OWNER_REVIEW_ONLY"
