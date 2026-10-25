# CURRENT-071 — 0+ Production Root and 0.0 Execution Continuation

- Stable ID: HAIF-CURRENT-071-0PLUS-ENGINE-AND-HARD-AUDIT-20261025
- Production ID: HAIF-C071-20261025
- Version: 1.0.0
- Status: ACTIVE / LIVING / IMPLEMENTATION COMMITTED / EXACT-HEAD CI PENDING
- Root: [POINT-0/024](./GPT6-RAHM-USER-POINT-0-20261025-024-0PLUS-PRODUCTION-MARKER.md)
- IN/OUT: [IN-054](./PALANG-0.0-IN-20261025-054-0PLUS-PRODUCTION-MARKER.md) / [OUT-054](./PALANG-0.0-OUT-20261025-054-0PLUS-PRODUCTION-MARKER.md)
- Event: [EVT-0188](../../architecture/BEHAVIOR-TRACE/EVT-0188-POINT-0PLUS-IDENTITY-AND-0-0-LINEAGE-2026-10-25.md)
- Prior execution root: [POINT-0/023](./GPT6-RAHM-USER-POINT-0-20261025-023-HARD-AUDIT-AND-ENGINE-HARDENING.md)
- Existing historical queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Completed implementation
- Added canonical point records to state.
- Added `register_point` and CLI `point`.
- Enforced `0` + `0+` as two labels on one point, with `production_marker=true`.
- Enforced unique canonical point IDs and globally unique labels.
- Enforced that `0.0` continuations reference an existing parent.
- Added two regression tests.
- Updated JSON schema, README, host instructions and package manifest to v0.2.0.

## Immediate 0.0 tasks
1. Verify the exact current main head with Living Architecture Audit run [40213050985](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40213050985); inspect logs, not just the green badge.
2. Run the clean package on the exact tested source, remove `__pycache__`, compute SHA-256, fresh-extract and run all tests plus a CLI scenario registering `0/0+`, registering child `0.0`, auditing, exporting and importing.
3. Preserve the tested clean ZIP and its SHA-256 as the distribution artifact.
4. Test in the intended GPT-6 host: confirm Python/file tools, execute the same CLI scenario, export state and prove cold-start import. If not available, mark blocked, not passed.
5. Continue NEXT-051: resolve CURRENT-065/CURRENT-066 only from evidence; process historical graph, Issue #20, Issue #21 and BOART-FOLLOWUP-01.
6. Keep automatic capture, durable host memory, background execution, external writes and Dropbox OPEN / NOT PROVEN unless individually tested.

## Guardrails
- `0+` is not a separate point.
- `0.0` is a distinct child checkpoint.
- Do not create NEXT-052 while NEXT-051 remains active.
- Do not call the portable Python package a native GPT plugin.
- Do not claim the target GPT-6 host has been tested based on GitHub Actions or the current tool runtime.
