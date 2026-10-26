# CURRENT-072 — Dual-Path Excavation Execution

- Stable ID: HAIF-CURRENT-072-DUAL-PATH-EXCAVATION-20261026
- Production ID: HAIF-C072-20261026
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EXECUTION REQUIRED
- Root: [POINT-0/025](./GPT6-RAHM-USER-POINT-0-20261026-025-EXCAVATION-FINDINGS-DUAL-PATH.md)
- IN/OUT: [IN-055](./PALANG-0.0-IN-20261026-055-EXCAVATION-FINDINGS-DUAL-PATH.md) / [OUT-055](./PALANG-0.0-OUT-20261026-055-EXCAVATION-FINDINGS-DUAL-PATH.md)
- Event: [EVT-0191](../../architecture/BEHAVIOR-TRACE/EVT-0191-EXCAVATION-FINDINGS-DUAL-PATH-2026-10-26.md)
- Previous root/checkpoint: [POINT-0/024](./GPT6-RAHM-USER-POINT-0-20261025-024-0PLUS-PRODUCTION-MARKER.md) / [CURRENT-071](./PALANG-0.0-CURRENT-20261025-071-0PLUS-ENGINE-AND-HARD-AUDIT.md)
- Existing remediation queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Dual-path invariant
Path A and Path B are both mandatory, coordinated and separately gated. Progress in one path does not close or replace the other.

## Path A — initial model construction
- [ ] Inspect latest exact-head portable-conformance and Living Architecture Audit runs and their tested SHAs.
- [ ] Read current run/job/step receipts and confirm manifest exact-byte digests, package artifact and clean-package bootstrap evidence.
- [ ] Verify the starter/runtime source and recovery state against the exact tested revision.
- [ ] Keep independent AI-host import, second-host import, host-native persistence/restart, automatic capture and background execution OPEN until directly tested in an authorized runtime.

## Path B — existing architecture remediation
- [ ] Rerun the current graph audit and retain the raw receipt; historical counts are not current counts.
- [ ] Adjudicate Stable-ID, Production-ID, Reference-ID, event-number collisions, ambiguous parent edges and timestamps individually.
- [ ] Reconcile CURRENT-065/CURRENT-066 provenance and consumers; remain AMBIGUOUS/BLOCKED until evidence decides the pointer.
- [ ] Keep Issue #20, Issue #21, BOART-FOLLOWUP-01 and all unresolved findings in NEXT-051 unless evidence justifies a documented move.

## Shared integration
- [x] Link this chain from the 0.0 registry, reference index, integration queue, living master and behavior-trace index; those files were independently fetched after writes.
- [x] Independently fetch root, IN, OUT, event, current, index, queue, 0.0 registry and mother documents; identifiers and versions matched. Relative links were checked for the new chain; a full repository-wide link audit remains pending.
- [ ] Read the exact-head workflow receipts before claiming validation.
- [x] Bind the root creation commit timestamp from Git metadata: 2026-10-26T03:52:33Z = 2026-10-26 07:22:33 Asia/Tehran; see TIME-BINDING-EVT-0191.
- [ ] Report durable milestones visibly; do not imply background execution between turns.

## Acceptance criteria
- [x] Root, IN, OUT, event and CURRENT files were independently fetched; IDs, versions and core links match.
- [x] 0.0 registry, reference index, integration queue and both living master references link to POINT-0/025 and CURRENT-072.
- [ ] Path A has a verified next action or explicit blocker.
- [ ] Path B has a verified next action or explicit blocker.
- [ ] Unresolved host and graph gates remain open; no speculative closure or bulk renumbering.
- [ ] NEXT-051 remains the active remediation queue; no NEXT-052 is created merely to renumber work.

## Status boundary
OPEN / EXECUTION REQUIRED. Registration alone does not satisfy the acceptance criteria.