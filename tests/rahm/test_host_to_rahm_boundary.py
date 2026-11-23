from __future__ import annotations

import contextlib
import http.client
import importlib.util
import io
import json
import sys
import tempfile
import threading
import unittest
from http.server import ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_DIR = ROOT / "scripts" / "rahm-runtime"
sys.path.insert(0, str(RUNTIME_DIR))

from rahm_runtime import atomic_write, new_ledger
from rahm_service import _is_loopback_host, handler_for

ADAPTER_PATH = RUNTIME_DIR / "rahm_host_agent.py"
SPEC = importlib.util.spec_from_file_location("rahm_host_agent_retired", ADAPTER_PATH)
ADAPTER = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(ADAPTER)


class HostToRahmBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.ledger_path = Path(self.temp.name) / "ledger.json"
        atomic_write(self.ledger_path, new_ledger())
        self.server = ThreadingHTTPServer(
            ("127.0.0.1", 0), handler_for(self.ledger_path)
        )
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=2)
        self.temp.cleanup()

    def test_remote_ingest_endpoint_is_gone(self):
        connection = http.client.HTTPConnection("127.0.0.1", self.server.server_port)
        connection.request(
            "POST",
            "/v1/haif/ingest",
            body=json.dumps({"schema": "haif-runtime-state/1.0", "events": []}),
            headers={"Content-Type": "application/json"},
        )
        response = connection.getresponse()
        payload = json.loads(response.read().decode("utf-8"))
        connection.close()
        self.assertEqual(response.status, 410)
        self.assertEqual(payload["result"], "DISABLED")
        self.assertEqual(payload["reason"], "OWNER_MEDIATED_IMPORT_REQUIRED")

    def test_health_endpoint_remains_read_only(self):
        connection = http.client.HTTPConnection("127.0.0.1", self.server.server_port)
        connection.request("GET", "/health")
        response = connection.getresponse()
        payload = json.loads(response.read().decode("utf-8"))
        connection.close()
        self.assertEqual(response.status, 200)
        self.assertEqual(payload["result"], "PASS")
        self.assertEqual(payload["authority"], "PROPOSAL_ONLY_NO_MASTER_WRITE")

    def test_service_rejects_non_loopback_binding(self):
        self.assertTrue(_is_loopback_host("127.0.0.1"))
        self.assertTrue(_is_loopback_host("::1"))
        self.assertTrue(_is_loopback_host("localhost"))
        self.assertFalse(_is_loopback_host("0.0.0.0"))
        self.assertFalse(_is_loopback_host("192.0.2.10"))

    def test_legacy_host_adapter_is_permanently_disabled(self):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            code = ADAPTER.main(["--source", "does-not-exist.json", "--url", "https://example.invalid"])
        self.assertEqual(code, ADAPTER.DISABLED_CODE)
        self.assertIn("DISABLED_BY_POINT_0_GOLDEN", stderr.getvalue())
        self.assertIn("quarantine", stderr.getvalue().lower())


if __name__ == "__main__":
    unittest.main()
