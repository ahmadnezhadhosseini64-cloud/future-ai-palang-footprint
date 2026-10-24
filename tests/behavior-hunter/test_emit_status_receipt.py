import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts" / "behavior-hunter"))
from emit_status_receipt import build_receipt

class StatusReceiptTests(unittest.TestCase):
    def test_success_receipt_has_canonical_utc_and_derived_tehran(self):
        now = datetime(2026, 10, 24, 4, 0, 0, tzinfo=timezone.utc)
        receipt = build_receipt(event_id="EVT-0131", pair_id="INT-20261024-033",
                                stage="CI_TERMINAL", status="success", run_id="123",
                                tested_sha="abc123", now=now)
        self.assertEqual(receipt["status"], "SUCCESS")
        self.assertEqual(receipt["timestamps"]["utc"], "2026-10-24T04:00:00Z")
        self.assertEqual(receipt["timestamps"]["tehran"], "2026-10-24T07:30:00+03:30")
        self.assertTrue(receipt["timestamps"]["tehran_derived_from_same_instant"])
        self.assertFalse(receipt["chat_ui_heartbeat_proven"])
        self.assertFalse(receipt["host_wide_capture_proven"])
        self.assertFalse(receipt["external_persistence_proven"])

    def test_failure_is_a_terminal_receipt_not_a_success(self):
        receipt = build_receipt(event_id="EVT-0131", pair_id="INT-20261024-033",
                                stage="CI_TERMINAL", status="failure", run_id="124",
                                tested_sha="deadbeef",
                                now=datetime(2026, 10, 24, 4, 0, tzinfo=timezone.utc))
        self.assertEqual(receipt["status"], "FAILURE")
        self.assertTrue(receipt["terminal"])

    def test_naive_timestamp_is_rejected(self):
        with self.assertRaises(ValueError):
            build_receipt(event_id="E", pair_id="P", stage="S", status="success",
                          run_id="", tested_sha="", now=datetime(2026, 10, 24))

    def test_invalid_status_is_rejected(self):
        with self.assertRaises(ValueError):
            build_receipt(event_id="E", pair_id="P", stage="S", status="running",
                          run_id="", tested_sha="")

if __name__ == "__main__":
    unittest.main()
