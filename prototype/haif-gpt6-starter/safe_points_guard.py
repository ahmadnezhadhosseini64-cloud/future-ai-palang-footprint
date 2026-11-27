"""Fail-closed owner gate.

Candidate-supplied booleans are NOT evidence. This module only accepts a
canonical attestation signed by a separately operated verifier. The trusted
runtime supplies two distinct pins: promoted MAIN and immutable Copy 1.
Without those pins and the verifier key, the result is BLOCKED.
"""
from __future__ import annotations

import base64
import json
import os
import subprocess
import tempfile
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


REQUIRED_TRUE = ("tests_pass", "paths_authorized", "bridge_matches")
REQUIRED_FIELDS = (
    "schema", "issuer", "repository", "main_sha", "copy1_sha",
    "main_tree_sha", "copy1_tree_sha", "copy2_base_sha", "copy2_head_sha",
    "diff_sha256", "tests_pass", "paths_authorized", "bridge_matches",
)


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
    packet: dict[str, Any], signature_b64: str, *, repository: str
) -> Verification:
    """Verify externally signed evidence; never trust candidate booleans."""
    public_key = os.environ.get("PALANG_TRUSTED_VERIFIER_PUBLIC_KEY", "")
    main_pin = os.environ.get("PALANG_GOLDEN_MAIN_SHA", "")
    copy1_pin = os.environ.get("PALANG_IMMUTABLE_COPY1_SHA", "")
    if not public_key.strip() or not main_pin.strip() or not copy1_pin.strip():
        return Verification(Gate.BLOCKED, "trusted verifier key or canonical pins are absent")

    if not isinstance(packet, dict) or any(key not in packet for key in REQUIRED_FIELDS):
        return Verification(Gate.BLOCKED, "attestation schema is incomplete")
    if packet.get("schema") != "palang.external-verification.v1":
        return Verification(Gate.BLOCKED, "unsupported attestation schema")
    if packet.get("issuer") != "palang-independent-verifier":
        return Verification(Gate.BLOCKED, "untrusted attestation issuer")
    if packet.get("repository") != repository:
        return Verification(Gate.BLOCKED, "repository identity mismatch")

    for key in (
        "main_sha", "copy1_sha", "main_tree_sha", "copy1_tree_sha",
        "copy2_base_sha", "copy2_head_sha", "diff_sha256",
    ):
        value = packet.get(key)
        if not isinstance(value, str) or not value or any(ch.isspace() for ch in value):
            return Verification(Gate.BLOCKED, f"invalid {key}")

    if packet["main_sha"] != main_pin:
        return Verification(Gate.BLOCKED, "promoted MAIN does not match its canonical pin")
    if packet["copy1_sha"] != copy1_pin:
        return Verification(Gate.BLOCKED, "immutable Copy 1 does not match its registered pin")
    if packet["main_tree_sha"] != packet["copy1_tree_sha"]:
        return Verification(Gate.BLOCKED, "MAIN and immutable Copy 1 trees differ")
    if packet["copy2_base_sha"] != copy1_pin:
        return Verification(Gate.BLOCKED, "Copy 2 is not based on immutable Copy 1")
    if not all(packet.get(key) is True for key in REQUIRED_TRUE):
        return Verification(Gate.BLOCKED, "one or more independent checks did not pass")

    if not _verify_signature(_canonical_payload(packet), signature_b64, public_key):
        return Verification(Gate.BLOCKED, "external verifier signature is invalid")
    return Verification(Gate.OWNER_REVIEW, "signed external evidence verified; owner review only")


def bridge_destination() -> str:
    """The bridge never authorizes writes or promotion."""
    return "OWNER_REVIEW_ONLY"
