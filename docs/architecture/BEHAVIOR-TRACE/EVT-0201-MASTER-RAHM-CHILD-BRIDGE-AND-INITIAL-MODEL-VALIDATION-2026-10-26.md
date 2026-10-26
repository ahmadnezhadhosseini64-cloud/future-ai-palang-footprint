# EVT-0201 — Master–Rahm–Child bridge and initial-model validation

- Event ID: EVT-0201
- Stable ID: HAIF-EVT-0201-MASTER-RAHM-CHILD-BRIDGE-20261026
- Production ID: HAIF-EVT0201
- Version: 1.0.0
- Status: REGISTERED / ACTIVE / LIVING / OPEN
- Root: [POINT-0/032](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-032-MASTER-RAHM-CHILD-INITIAL-MODEL-BRIDGE.md)
- Input/output: [IN-067](../../0.0/anchors/PALANG-0.0-IN-20261026-067-MASTER-RAHM-CHILD-BRIDGE.md) → [OUT-066](../../0.0/anchors/PALANG-0.0-OUT-20261026-066-MASTER-RAHM-CHILD-BRIDGE.md)
- Prior event: EVT-0200; prior checkpoint CURRENT-078
- Current queue: NEXT-051 only

## Observation
The user's goal clarifies a hierarchy, not two peer projects: the original project is Master; the initial-model project acts as Rahm; only evidence-validated and explicitly reviewed candidates may become Children and be returned to Master.

## Architecture decision recorded
`MASTER → RAHM → OBSERVATION → HYPOTHESIS → TEST → EVIDENCE REVIEW → CHILD CANDIDATE → MASTER DECISION`

- Preserve all source IDs, parent candidates, versions, test outputs and failed attempts.
- A reversible cover may defer work but must not close or hide the underlying gap.
- CI success proves only the tested repository commit and configured checks.
- A project-interactive or independent-host test requires a receipt from that actual destination.
- No continuous/always-on behavior is claimed without runtime evidence.

## Failure-prevention lesson
Do not drift to Dropbox or other side branches when the selected continuation is the initial-model architecture. Check the current root/checkpoint and user-stated target before choosing the next action; if a mismatch is found, record the deviation and return to the active queue without erasing the detour.

## Next
Use CURRENT-079 and the cross-validation contract to run the next source-backed, reproducible step. Keep untested gates OPEN.
