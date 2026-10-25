# CURRENT-068 — Initial Model Completion Gate and Continuation

- Stable ID: `HAIF-CURRENT-068-INITIAL-MODEL-COMPLETION-20261025`
- Production ID: `HAIF-C068-20261025`
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EVIDENCE-BOUNDED.
- Root: [POINT-0/021](./GPT6-RAHM-USER-POINT-0-20261025-021-INITIAL-MODEL-COMPLETION-GATE.md).
- Parent history: [CURRENT-067](./PALANG-0.0-CURRENT-20261025-067-LIVE-POINTER-FAILURE-AND-RECOVERY.md), [CURRENT-066](./PALANG-0.0-CURRENT-20261025-066-OPEN-GAPS-AND-LIVING-MASTER-RECOVERY.md); neither is deleted or silently replaced.
- Event: [EVT-0184](../../architecture/BEHAVIOR-TRACE/EVT-0184-INITIAL-MODEL-COMPLETION-GATE-2026-10-25.md).
- Living mother: [HAIF Initial Model Master Reference](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md).
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md).

## Last supported baseline

EVT-0183 records successful tested-commit receipts for the date-bearing pointer-parser regression, pointer audit behavior (AMBIGUOUS with no winner), four runtime tests, schema conformance, bounded IN/OUT reconstruction equivalence, exact-byte and live-reference digest scans, and portable package generation. The cited tested revision is `383266b17d2b38a0114367877c4b9c39a6c4ef76`. These receipts are not automatically proof for the latest main after later commits.

## Execution plan — ordered, with closure criteria

### C0 — Revalidate the actual current main
- [ ] Read current main HEAD and its actual commit timestamp in UTC.
- [ ] Inspect the exact-head Living Architecture Audit and portable-conformance receipts/artifacts for that revision.
- [ ] If no run exists, trigger only through an available authorized route; otherwise leave NOT RUN.
- [ ] Record the exact SHA, run IDs, artifact IDs/digests and status. Do not reuse a nearby commit's PASS as current-head proof.

### C1 — Finish the local prototype acceptance baseline
- [ ] Inspect `prototype/haif-v0/` source, schema, tests and run guide at the same SHA.
- [ ] Ensure Anchor, IN, OUT, Event, Artifact, Evidence, Relation, Decision and Gap are represented or explicitly scoped out with a reason.
- [ ] Verify create/read-back, independent anchors, provenance retrieval, hash mismatch handling, failed-write/read-back handling, and clean-process recovery.
- [ ] Run tests; preserve failing results and warnings as evidence.
- [ ] Verify export → import → canonical-state comparison in a clean local process.
- Acceptance: automated tests pass on exact SHA, data/provenance survives round-trip, and failures do not appear as success.

### C2 — Reconcile the live checkpoint without guessing
- [ ] Compare all explicit current-pointer declarations, manifest lineage, verifier scope and actual checkpoint contents.
- [ ] Review each occurrence's role: current, historical, alias, overlay, mirror or unresolved.
- [ ] Preserve all historical files; select a canonical current pointer only with provenance and consumer compatibility evidence.
- Acceptance: one supported live pointer or a clearly documented unresolved ambiguity; no numeric-order shortcut.

### C3 — Continue historical graph triage
- [ ] Continue NEXT-051, Issue #20, Issue #21 and BOART-FOLLOWUP-01.
- [ ] Review one Stable ID / Production ID / Reference ID / EVT occurrence group or parent edge at a time.
- [ ] Record decision, evidence, rejected alternatives and lineage; do not mass-renumber or delete.
- Acceptance: each adjudicated item has an occurrence-level decision; unreviewed items remain visibly OPEN.

### C4 — Complete portability and independent-host proof
- [ ] Verify portable bundle exact-byte digest and schema.
- [ ] Run local clean-environment import/round-trip.
- [ ] Separately test import and recovery in an independent AI host; record host/version, permissions, result and limitations.
- Acceptance: successful independent-host retrieval of selected anchors, events and artifacts with matching identity and provenance. Until then: NOT PROVEN.

### C5 — Keep unimplemented platform capabilities honest
- [ ] Automatic live-message capture, host restart durability, idle/background execution and external storage remain NOT PROVEN until directly exercised.
- [ ] Buffer, Persistent Memory and Library require destination-specific read/write/read-back evidence.
- [ ] Dropbox stays OPEN / WAITING and inactive unless explicitly reopened by the user.
- Acceptance: no external destination or host-wide capability is described as active without its own evidence.

### C6 — Close the initial model baseline
- [ ] Update the living master, 0.0 registry, Reference Index, behavior-trace index, integration queue and model README from verified evidence.
- [ ] Run final exact-head structural audit and local prototype suite after the last code/documentation change.
- [ ] Read back every changed file and reconcile links/IDs/statuses.
- Acceptance: documented model + locally runnable prototype + exact-head passing tests/audit + export/import proof; external-host and historic-graph work may remain explicitly open without being misrepresented as completed.

## Preserved defects and lessons

- Prior branch-selection error: Dropbox was pursued when the active goal was initial-model architecture. Check current user intent and active queue before choosing a branch.
- Pointer parser test gap: short fixture names missed date-bearing CURRENT filenames. Use real-shape fixtures.
- Current pointer conflict: CURRENT-065/CURRENT-066 cannot be resolved by numeric order or manifest filename alone.
- Graph receipt: 63 Stable-ID collision groups (62 unreviewed), 89 Production-ID groups, 7 Reference-ID groups, 38 event-number groups and 13 ambiguous parent edges remain review work; these counts are snapshot-specific.
- Library mirror difference: source 10,479 chars vs Library 10,480, one trailing newline; unresolved until a supported independent update/read-back.
- External host, automatic capture, durable restart, background execution and external storage are not proven.
- NEXT-051 remains the active queue. No NEXT-052 is created.

## State vocabulary

`REGISTERED` means file recorded; `READ-BACK VERIFIED` means it was fetched and checked; `TEST PASS` applies only to a named tested SHA/scope; `VALIDATED` requires the relevant semantic/technical gate; `ACTIVE` describes a live operational capability only when evidence supports it; `OPEN / NOT PROVEN` remains open until acceptance evidence exists.

This checkpoint is the next worklist, not a declaration that the model is complete.
