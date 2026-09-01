"""Repository-side PMA runtime bridge.

This is deliberately provider-neutral. It verifies the durable adapter store
without pretending that the store is ChatGPT Persistent Memory.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


PRODUCTION_ID = "MPGG-2026-09-01-001"
ADAPTER_ID = "PMA-2026-09-01-001"


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def payload_hash(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def write_record(store: Path, payload: dict[str, Any]) -> dict[str, Any]:
    store.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "production_id": PRODUCTION_ID,
        "adapter_id": ADAPTER_ID,
        "payload": payload,
        "payload_sha256": payload_hash(payload),
        "memory_provider_status": "UNVERIFIED / PENDING",
    }
    store.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return record


def read_back(store: Path) -> dict[str, Any]:
    return json.loads(store.read_text(encoding="utf-8"))


def verify(record: dict[str, Any], expected_payload: dict[str, Any]) -> dict[str, Any]:
    expected_hash = payload_hash(expected_payload)
    actual_hash = payload_hash(record["payload"])
    return {
        "production_id_preserved": record.get("production_id") == PRODUCTION_ID,
        "adapter_id_preserved": record.get("adapter_id") == ADAPTER_ID,
        "payload_match": actual_hash == expected_hash,
        "stored_hash_match": record.get("payload_sha256") == actual_hash,
        "repository_adapter_verified": (
            record.get("production_id") == PRODUCTION_ID
            and record.get("adapter_id") == ADAPTER_ID
            and actual_hash == expected_hash
            and record.get("payload_sha256") == actual_hash
        ),
        "chatgpt_persistent_memory_verified": False,
    }


def reconcile(result: dict[str, Any]) -> dict[str, Any]:
    if result["repository_adapter_verified"]:
        return {
            **result,
            "repository_status": "VERIFIED",
            "memory_provider_status": "UNVERIFIED / PENDING",
            "reconciliation_status": "PENDING_EXTERNAL_MEMORY_READBACK",
        }
    return {
        **result,
        "repository_status": "UNVERIFIED / PENDING",
        "memory_provider_status": "UNVERIFIED / PENDING",
        "reconciliation_status": "PENDING",
    }


def execute(store: Path, payload: dict[str, Any]) -> dict[str, Any]:
    """Run WRITE → READ-BACK → VERIFY → RECONCILE → STATUS."""
    written = write_record(store, payload)
    read = read_back(store)
    result = verify(read, written["payload"])
    return reconcile(result)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("store", type=Path)
    parser.add_argument("--payload", required=True)
    args = parser.parse_args()
    payload = json.loads(args.payload)
    print(json.dumps(execute(args.store, payload), ensure_ascii=False, indent=2))
