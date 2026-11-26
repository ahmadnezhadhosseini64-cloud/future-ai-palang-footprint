import unittest
from safe_points_guard import Evidence, Gate, evaluate, bridge_destination

ANCHOR = "golden-sha"
def packet(**overrides):
    fields=dict(main_sha=ANCHOR,copy1_sha=ANCHOR,copy2_base_sha=ANCHOR,
                copy2_head_sha="safe-test-sha",tests_pass=True,
                paths_authorized=True,bridge_matches=True)
    fields.update(overrides)
    return Evidence(**fields)

class FailureFirstTests(unittest.TestCase):
    def test_valid_packet_stops_at_owner(self):
        self.assertEqual(evaluate(packet(),ANCHOR),Gate.OWNER_REVIEW)
        self.assertEqual(bridge_destination(),"OWNER_REVIEW_ONLY")
    def test_main_baseline_drift_blocks(self):
        self.assertEqual(evaluate(packet(main_sha="drift"),ANCHOR),Gate.BLOCKED)
    def test_copy1_change_blocks(self):
        self.assertEqual(evaluate(packet(copy1_sha="altered"),ANCHOR),Gate.BLOCKED)
    def test_wrong_copy2_base_blocks(self):
        self.assertEqual(evaluate(packet(copy2_base_sha="wrong"),ANCHOR),Gate.BLOCKED)
    def test_missing_head_sha_blocks(self):
        self.assertEqual(evaluate(packet(copy2_head_sha=""),ANCHOR),Gate.BLOCKED)
    def test_test_failure_blocks(self):
        self.assertEqual(evaluate(packet(tests_pass=False),ANCHOR),Gate.BLOCKED)
    def test_unauthorized_path_blocks(self):
        self.assertEqual(evaluate(packet(paths_authorized=False),ANCHOR),Gate.BLOCKED)
    def test_bridge_mismatch_blocks(self):
        self.assertEqual(evaluate(packet(bridge_matches=False),ANCHOR),Gate.BLOCKED)
    def test_empty_golden_anchor_blocks(self):
        self.assertEqual(evaluate(packet(),""),Gate.BLOCKED)
    def test_no_destination_for_main_or_copy1_write(self):
        self.assertNotIn("MAIN",bridge_destination())
        self.assertNotIn("COPY1_WRITE",bridge_destination())
if __name__=="__main__": unittest.main(verbosity=2)
