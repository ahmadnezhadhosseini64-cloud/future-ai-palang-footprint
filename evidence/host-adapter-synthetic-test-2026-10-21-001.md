# Host Adapter Synthetic Test Evidence — 2026-10-21

- Stable ID: HOST-ADAPTER-SYNTHETIC-TEST-2026-10-21-001
- Production ID: HAST-2026-10-21-001
- Version: 1.0.0
- Test subject: scripts/host_adapter.py and scripts/test_host_adapter.py
- Test class: isolated local synthetic acceptance test
- Test execution timestamp: UNKNOWN / NOT EXPOSED by the execution tool; do not substitute commit time.
- Repository registration time: see GitHub commit metadata for this evidence file.
- Result: PASS for the implemented synthetic adapter behaviors below.

## Actual output
HOST_ADAPTER_TESTS=PASS
synthetic_ingest=PASS
authentication=PASS
durable_readback=PASS
idempotent_retry=PASS
conflicting_retry_rejected=PASS
restart_recovery=PASS
live_chatgpt_producer=NOT_TESTED
repository_write=NOT_IMPLEMENTED

## Scope
The test ran the repository's adapter/test logic in an isolated local execution environment with a temporary SQLite database and a synthetic event. It verified signed request ingestion, durable queue read-back, same-payload retry, conflicting-payload rejection, and persistence across server restart.

## Explicit non-claims
- This does not prove the ChatGPT host sends every live user/assistant message.
- This does not prove deployment on a publicly reachable or production host.
- This does not prove direct writing to GitHub; the receiver explicitly reports repository_write=NOT_IMPLEMENTED.
- This does not test Buffer, Library, Persistent Memory, or Dropbox.
- This does not replace the GitHub Actions run/artifact result, which must be independently read back.

## Next actions
1. Connect an authorized live producer to the receiver.
2. Add a separately authenticated repository writer/worker and verify GitHub read-back.
3. Test a real input/output pair, network interruption, restart, replay, and recovery of six real documents.
