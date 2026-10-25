# EVT-0175 — CURRENT-066 Recovery Verifier Stale Checkpoint

- Stable ID: HAIF-EVT-0175-CURRENT-066-VERIFIER-STALE-CHECKPOINT-2026-10-25
- Related root: [POINT-0/015](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261025-015-OPEN-GAPS-AND-LIVING-MASTER-RECOVERY.md)
- Current checkpoint: [CURRENT-066](../../0.0/anchors/PALANG-0.0-CURRENT-20261025-066-OPEN-GAPS-AND-LIVING-MASTER-RECOVERY.md)
- Prior output: [OUT-058](../../0.0/anchors/PALANG-0.0-OUT-20261025-058-OPEN-GAPS-AND-LIVING-MASTER-RECOVERY.md)
- Failed workflow: [Living Architecture Audit run 40170056194](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40170056194)
- Status: FAILURE RECORDED; correction required; rerun pending.

## Observed failure
On commit `4b39d34e7a2c7a585d746c7bdf5494f36d7beaeb`, the IN/OUT reconstruction verifier reported `manifest_checkpoint_mismatch`: the overlay's actual checkpoint was CURRENT-066 while the verifier still asserted CURRENT-065. Both IN and OUT reconstructions were blocked for the same stale expectation, while their open-gate preservation checks passed.

## Root cause
The verifier hard-coded the old Point-0/014 → IN-058 → OUT-057 → EVT-0167 → CURRENT-065 chain and its overlay manifest checkpoint. Advancing the live checkpoint without advancing the verifier's canonical chain definitions caused a false negative against the new intended current state. This is a synchronization defect, not evidence that full external-host recovery works.

## Required correction
Update the verifier's chain paths, stable IDs, required links and recovery test ID to the CURRENT-066 chain; retain NEXT-051 and all open gates. Rerun the audit on the exact new commit. If any other stale assumptions surface, record each failure and keep the affected gates OPEN.
