import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts" / "behavior-hunter"))
from validate_architecture_update_ledger import validate_records

def record(**overrides):
    item = {
        "change_id": "LAUC-001",
        "version": "1.0.0",
        "sequence": 1,
        "state": "PROPOSED",
        "supersedes": None,
        "owner_decision": "PENDING",
        "source_event_ids": ["EVT-0125"],
        "evidence_refs": ["repo://evidence/fixture"],
        "target_paths": ["docs/architecture/BEHAVIOR-OBSERVATORY/example.md"],
        "rollback_plan": "Revert the isolated proposal commit and preserve the record."
    }
    item.update(overrides)
    return item

class ArchitectureUpdateLedgerTests(unittest.TestCase):
    def test_valid_first_record_passes_without_mutation(self):
        result = validate_records([record()])
        self.assertEqual(result["status"], "PASS")
        self.assertFalse(result["canonical_mutation_performed"])
        self.assertFalse(result["history_rewritten"])

    def test_append_only_version_chain_passes(self):
        result = validate_records([
            record(),
            record(version="1.1.0", sequence=2, supersedes="1.0.0")
        ])
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["change_streams"], 1)
        self.assertEqual(result["unique_change_versions"], 2)

    def test_duplicate_change_version_is_blocked(self):
        result = validate_records([record(), record(sequence=2)])
        self.assertEqual(result["status"], "BLOCKED")
        self.assertIn("duplicate_change_version", [e["code"] for e in result["errors"]])

    def test_broken_supersedes_chain_is_blocked(self):
        result = validate_records([record(), record(version="1.1.0", sequence=2, supersedes="0.9.0")])
        self.assertIn("version_chain_break", [e["code"] for e in result["errors"]])

    def test_sequence_must_increase(self):
        result = validate_records([record(), record(version="1.1.0", sequence=1, supersedes="1.0.0")])
        self.assertIn("duplicate_sequence", [e["code"] for e in result["errors"]])

    def test_integrated_requires_explicit_approval(self):
        result = validate_records([record(state="INTEGRATED", owner_decision="PENDING")])
        self.assertIn("integration_without_owner_approval", [e["code"] for e in result["errors"]])

    def test_approved_state_requires_approval_decision(self):
        result = validate_records([record(state="APPROVED", owner_decision="PENDING")])
        self.assertIn("approved_state_without_owner_decision", [e["code"] for e in result["errors"]])

    def test_missing_evidence_blocks(self):
        result = validate_records([record(evidence_refs=[])])
        self.assertIn("evidence_refs_required", [e["code"] for e in result["errors"]])

    def test_empty_ledger_blocks(self):
        result = validate_records([])
        self.assertEqual(result["status"], "BLOCKED")

if __name__ == "__main__":
    unittest.main()
