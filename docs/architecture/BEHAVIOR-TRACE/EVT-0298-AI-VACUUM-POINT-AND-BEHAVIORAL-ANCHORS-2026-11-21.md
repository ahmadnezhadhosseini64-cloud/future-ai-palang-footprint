# EVT-0298 — AI Vacuum Point and permanent behavioral anchors

- Stable ID: HAIF-EVT-0298-AI-VACUUM-POINT-2026-11-21-001
- Status: ACTIVE / LIVING / BRANCH-REGISTERED
- Root: POINT-0/077 (0++)
- Parent: CURRENT-131
- Input/output: IN-122 → OUT-121
- Current checkpoint: CURRENT-132
- Sole queue: NEXT-051
- PR: #64

## Event

The owner requested two temporal anchors around the observable gap between a stopped assistant turn and the start of the next processing cycle, named AI Vacuum Point, plus a permanent behavioral trace standard for future hosts.

## Implemented

The branch now defines STOP and THINKING_START as independent runtime events; a separate AI Vacuum interval is computed only when both observed timestamps share a comparable clock. Observable categories include request receipt, context retrieval, repository/file operations, tool calls, code/tests, validation and response lifecycle. Private chain-of-thought and secrets are expressly excluded.

## Limitations

The actual timestamps for the prior stop and current private inference start are not exposed by this interface. They remain unknown; no duration is asserted. CI/package verification and merge remain pending.
