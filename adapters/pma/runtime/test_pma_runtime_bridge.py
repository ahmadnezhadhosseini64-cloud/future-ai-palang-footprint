import tempfile
from pathlib import Path

from pma_runtime_bridge import execute


def test_write_readback_verify_reconcile():
    payload = {
        "reference_record": "MPGG-2026-09-01-001",
        "adapter_specification": "PMA-2026-09-01-001",
        "status": "FINAL / ACTIVE / LIVING",
    }
    with tempfile.TemporaryDirectory() as tmp:
        result = execute(Path(tmp) / "pending-memory.json", payload)

    assert result["production_id_preserved"] is True
    assert result["adapter_id_preserved"] is True
    assert result["payload_match"] is True
    assert result["stored_hash_match"] is True
    assert result["repository_adapter_verified"] is True
    assert result["chatgpt_persistent_memory_verified"] is False
    assert result["repository_status"] == "VERIFIED"
    assert result["memory_provider_status"] == "UNVERIFIED / PENDING"
    assert result["reconciliation_status"] == "PENDING_EXTERNAL_MEMORY_READBACK"
