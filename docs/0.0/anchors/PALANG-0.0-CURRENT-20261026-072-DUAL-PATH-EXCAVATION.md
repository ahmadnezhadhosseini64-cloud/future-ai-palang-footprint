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
- [x] Path A next action and blocker are explicit: latest recorded local v0.3.0 package evidence is 13/13 tests on SHA 0d5107f (run 40214177082), but independent GPT-host import is NOT RUN because no authorized independent host/import route is available in this execution.
- [x] Path B next action and blocker are explicit: source-level pointer-scope mismatch identified; current exact-head graph audit and scope-aware parser regression remain pending.
- [ ] Unresolved host and graph gates remain open; no speculative closure or bulk renumbering.
- [x] NEXT-051 remains the active remediation queue; no NEXT-052 was created.

## Status boundary
OPEN / EXECUTION REQUIRED. Registration alone does not satisfy the acceptance criteria.

## Deep excavation receipt — 2026-10-26

### Path A — initial model construction
- Previously recorded Living Architecture Audit [40214177082](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40214177082) succeeded on tested SHA 0d5107fcb389d3ab79e03079d7c1d4d761f911a7: 13/13 tests; v0.3.0 clean package and fresh-extraction/export-import evidence are recorded in EVT-0190.
- This is the latest recorded package receipt found in the reviewed checkpoint, not a fresh run on today's post-registration HEAD. Do not represent it as exact-head validation for the new documentation commits.
- Blocker: independent GPT-host import/runtime is NOT RUN; this execution has no authorized independent host route. Host-native persistence, automatic capture, background execution and external writes remain OPEN / NOT VERIFIED.

### Path B — existing architecture remediation
- Targeted source-level read-back covered CURRENT-065, CURRENT-066, CURRENT-065 overlay manifest, recovery verifier, portable master, 0.0 registry, integration queue and reference index.
- Within the bounded overlay, manifest.current_checkpoint, verifier FILES["current"] and the portable master's top-level Current 0.0 all point to CURRENT-066.
- The append-only global registry surfaces still contain explicit old current claims such as CURRENT-023, CURRENT-039, CURRENT-064 and CURRENT-065; the newer global project chain reaches CURRENT-071 and this checkpoint CURRENT-072. The current discovery parser scans those registry lines with phrase matching, so it can mix historical/global claims with the overlay-local CURRENT-066 recovery pointer.
- This is a pointer-scope/lineage defect. Do not pick CURRENT-066 or CURRENT-072 as a universal winner: one is an overlay-local recovery pointer, the other is the global project continuation. Next fix is to define those scopes explicitly, update parser logic and regression fixtures to ignore historical append-only claims, then run a fresh exact-head audit.
- Latest previously inspected audit run [40213463189](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40213463189) completed at workflow level on tested SHA 49485c593ebd6a3d115c05ddda8e8997b3c5138e, but its graph content remains REVIEW_REQUIRED and it predates the current HEAD. A fresh exact-head audit is still required.

### Current status
- New chain registration, mother/index/queue links and targeted relative-link read-back: VERIFIED within the inspected repository surfaces.
- Full repository-wide graph audit: OPEN / NOT RUN on the current HEAD.
- Pointer scope adjudication: OPEN / AMBIGUOUS; no winner selected.
- Independent GPT host: OPEN / NOT RUN.
- NEXT-051 remains ACTIVE / LIVING. Both paths remain mandatory.
