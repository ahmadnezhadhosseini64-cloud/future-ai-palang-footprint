import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from graph_identifier_roles import metadata_header, metadata_label_line


class GraphIdentifierRoleTests(unittest.TestCase):
    def test_body_reference_is_not_in_header_declaration_region(self):
        body = (
            "# Index\n"
            "- Version: 1.0.0\n"
            "\n"
            "## Navigation\n"
            "- Stable ID: OTHER-DOCUMENT-001\n"
        )
        header, count = metadata_header(body)
        self.assertIn("Version: 1.0.0", header)
        self.assertNotIn("OTHER-DOCUMENT-001", header)
        self.assertEqual(count, 3)

    def test_own_stable_id_in_header_is_retained(self):
        body = (
            "# Canonical document\n"
            "- Stable ID: DOC-STABLE-001\n"
            "- Production ID: DOC-PROD-001\n"
            "- Version: 1.0.0\n"
            "\n"
            "## References\n"
            "- Stable ID: REFERENCED-DOCUMENT-002\n"
        )
        header, count = metadata_header(body)
        self.assertIn("DOC-STABLE-001", header)
        self.assertIn("DOC-PROD-001", header)
        self.assertNotIn("REFERENCED-DOCUMENT-002", header)
        self.assertEqual(count, 5)

    def test_headingless_legacy_document_is_bounded(self):
        body = "# Legacy\n" + "\n".join(f"line {i}" for i in range(1, 60))
        header, count = metadata_header(body, max_lines=40)
        self.assertEqual(count, 40)
        self.assertEqual(len(header.splitlines()), 40)

    def test_metadata_labels_are_recognized(self):
        self.assertTrue(metadata_label_line("- Stable ID: DOC-001"))
        self.assertTrue(metadata_label_line("- Production ID / شناسهٔ تولید: PROD-001"))
        self.assertTrue(metadata_label_line("- Reference ID: REF-001"))
        self.assertFalse(metadata_label_line("- Canonical path: docs/file.md"))


if __name__ == "__main__":
    unittest.main()
