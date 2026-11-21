import unittest
from ai_vacuum import compute_interval, validate_behavior_event

def anchor(event, timestamp, source="host_runtime", status="OBSERVED"):
    return {"event": event, "timestamp": timestamp, "clock_source": source,
            "precision": "exact" if timestamp else "unknown", "status": status,
            "evidence_reference": "test:evidence" if timestamp else None}

class AIVacuumTests(unittest.TestCase):
    def test_computes_observed_interval(self):
        result = compute_interval(anchor("STOP","2026-11-21T10:00:00Z"),
                                  anchor("THINKING_START","2026-11-21T10:00:02.250Z"))
        self.assertEqual(result, {"status":"MEASURABLE","duration_ms":2250,"reason":None})

    def test_missing_anchor_is_unmeasurable(self):
        result = compute_interval(anchor("STOP",None,status="UNAVAILABLE"),
                                  anchor("THINKING_START","2026-11-21T10:00:02Z"))
        self.assertEqual(result["status"], "UNMEASURABLE")
        self.assertIsNone(result["duration_ms"])

    def test_negative_interval_is_clock_conflict(self):
        result = compute_interval(anchor("STOP","2026-11-21T10:00:03Z"),
                                  anchor("THINKING_START","2026-11-21T10:00:02Z"))
        self.assertEqual(result["status"], "CLOCK_CONFLICT")

    def test_different_clock_sources_are_not_compared(self):
        result = compute_interval(anchor("STOP","2026-11-21T10:00:00Z","repository_commit"),
                                  anchor("THINKING_START","2026-11-21T10:00:01Z","host_runtime"))
        self.assertEqual(result["status"], "CLOCK_CONFLICT")

    def test_private_reasoning_is_rejected(self):
        self.assertTrue(validate_behavior_event({"event_type":"TOOL_CALL_STARTED",
                                                 "timestamp":None,
                                                 "private_reasoning":"hidden"}))

    def test_unknown_timestamp_must_be_explicit(self):
        self.assertTrue(validate_behavior_event({"event_type":"REQUEST_RECEIVED"}))

if __name__ == "__main__":
    unittest.main()
