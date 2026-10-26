# CURRENT-072 — Dual-Path Excavation Execution

- Stable ID: HAIF-CURRENT-072-DUAL-PATH-EXCAVATION-20261026
- Production ID: HAIF-C072-20261026
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EXECUTION REQUIRED
- Root: [POINT-0/025](./GPT6-RAHM-USER-POINT-0-20261026-025-EXCAVATION-FINDINGS-DUAL-PATH.md)
- IN/OUT: [IN-061](./PALANG-0.0-IN-20261026-061-EXCAVATION-FINDINGS-DUAL-PATH.md) / [OUT-060](./PALANG-0.0-OUT-20261026-060-EXCAVATION-FINDINGS-DUAL-PATH.md)
- Event: [EVT-0191](../../architecture/BEHAVIOR-TRACE/EVT-0191-EXCAVATION-FINDINGS-DUAL-PATH-2026-10-26.md)
- Previous root/checkpoint: [POINT-0/024](./GPT6-RAHM-USER-POINT-0-20261025-024-0PLUS-PRODUCTION-MARKER.md) / [CURRENT-071](./PALANG-0.0-CURRENT-20261025-071-0PLUS-ENGINE-AND-HARD-AUDIT.md)
- Existing remediation queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Dual-path invariant
Path A and Path B are both mandatory, coordinated and separately gated. Progress in one path does not close or replace the other.

## Path A — initial model construction
- [x] Inspected exact-head Portable RAHM Conformance and Living Architecture Audit runs on SHA 2b1f44e7e956c08d8ac4fccdb23ceedf77a6513f.
- [x] Read run/job/step receipts; exact-byte and live-reference SHA-256 scans PASS; package artifact metadata read back.
- [x] Verified portable conformance on exact tested SHA: 119 package files, 77 live references, package SHA-256 8c971e3a9f17787b13da13b9ef4a2b091144dd43e7be6f9289eeeda95d9a7a7a; archive artifact 12626363984.
- [ ] Keep independent AI-host import, second-host import, host-native persistence/restart, automatic capture and background execution OPEN until directly tested in an authorized runtime.

## Path B — existing architecture remediation
- [x] Reran the graph audit on exact tested SHA 2b1f44e7e956c08d8ac4fccdb23ceedf77a6513f; raw audit artifact and run receipt retained. Content result is REVIEW_REQUIRED.
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


## Exact-head execution receipts — 2026-10-26

### Path A — portable initial model
- Portable RAHM Conformance [40266803063](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40266803063): SUCCESS on exact tested SHA 2b1f44e7e956c08d8ac4fccdb23ceedf77a6513f.
- Exact-byte manifest inventory scan: PASS. Live-reference SHA-256 scan: PASS. Package build: PASS.
- Package inventory: 119 files; 77 live references. Package archive SHA-256: 8c971e3a9f17787b13da13b9ef4a2b091144dd43e7be6f9289eeeda95d9a7a7a; size 458115 bytes.
- Package artifact ID 12626363984, artifact digest sha256:912022e4fe8ad80856e5abce2657a48f50329f41c8f766a09587a92fd1989c78. Evidence artifact ID 12626598231, digest sha256:3531a5f166a501fc91a87c4745b0608907678f0c83088be10703828f4ab386cf.
- This closes the exact-byte/package build gate for the tested SHA only. It does not close independent GPT-host import, host persistence/restart, automatic capture, background execution or external writes.

### Path B — current pointer scope and graph
- Living Architecture Audit [40266803100](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40266803100): workflow SUCCESS on the same exact tested SHA. Structural repository checks: PASS.
- Pointer discovery test ID HAIF-CURRENT-POINTER-DISCOVERY-0.2: SCOPED_CONSISTENT; overlay recovery CURRENT-066 and global project CURRENT-072 are independently consistent; winner_selected=false. No historical file was rewritten or promoted.
- Latest graph content audit remains REVIEW_REQUIRED: 1,221 text nodes scanned; 0 decode errors; 418 paths with 0.0; 62 checkpoint paths; 232 EVT files; 145 reference-document paths; 6,755 local-link edges; 0 missing local links; 63 Stable-ID collision groups (62 unreviewed); 89 Production-ID collision groups; 7 Reference-ID collision groups; 38 event-number collision groups; 11 exact-content duplicate groups; 79 declared parent edges, 0 unresolved parent edges, 13 ambiguous parent edges and 11 proposed alias edges.
- Audit artifact ID 12626229346, digest sha256:194783c03554976684397e4112fee2f6ac11b4dfdf3e93adef04d54f5b3e672c.
- The pointer-scope defect is corrected and tested. The remaining graph collision/parent findings are not solved by the parser fix and must be adjudicated individually under NEXT-051.

### Current gate summary
- [x] New point chain registered, independently read back, and connected to registry, reference index, integration queue, initial-model living mother, continuation master and HAIF architecture master.
- [x] Pointer scope separated and regression-tested on the exact tested SHA.
- [x] Portable exact-byte/package conformance passed on the exact tested SHA.
- [ ] Individual adjudication of 62 unreviewed Stable-ID groups, 89 Production-ID groups, 7 Reference-ID groups, 38 event-number groups and 13 ambiguous parent edges.
- [ ] Independent GPT-host import and real host persistence/automatic-capture/background-runtime tests.
- NEXT-051 remains OPEN / LIVING. No NEXT-052 created.
