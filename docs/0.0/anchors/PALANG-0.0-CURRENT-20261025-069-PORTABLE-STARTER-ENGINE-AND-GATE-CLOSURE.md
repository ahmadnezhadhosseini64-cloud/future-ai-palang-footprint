# CURRENT-069 — Portable Starter Engine and CURRENT-068 Gate Closure

- Stable ID: HAIF-CURRENT-069-PORTABLE-STARTER-ENGINE-20261025
- Production ID: HAIF-C069-20261025
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EXECUTION REQUIRED
- Root: [POINT-0/022](./GPT6-RAHM-USER-POINT-0-20261025-022-PORTABLE-STARTER-ENGINE.md)
- IN: [IN-052](./PALANG-0.0-IN-20261025-052-PORTABLE-STARTER-ENGINE.md)
- OUT: [OUT-052](./PALANG-0.0-OUT-20261025-052-PORTABLE-STARTER-ENGINE.md)
- Event: [EVT-0185](../../architecture/BEHAVIOR-TRACE/EVT-0185-PORTABLE-HAIF-GPT6-STARTER-ENGINE-2026-10-25.md)
- Previous gate: [CURRENT-068](./PALANG-0.0-CURRENT-20261025-068-INITIAL-MODEL-COMPLETION-GATE.md)
- Existing historical queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## C0 — build and test the portable engine
- [x] Add starter package in the canonical repository, not a separate project.
- [x] Add independent anchor, IN, OUT and event IDs; evidence-class boundary; hash-chain verification.
- [x] Add open-gap register whose closure requires test ID, tested revision, PASS and evidence reference.
- [x] Add Master → Child proposal and promotion gate requiring passing evidence.
- [x] Add portable bundle export/import with SHA-256 and atomic local write/read-back.
- [x] Add GPT-6 host instructions, manifest, state schema and unit tests.
- [x] Wire starter unit tests and package/schema checks into Living Architecture Audit.
- [ ] Read actual CI run and artifact after the exact package commit; no PASS may be inferred from workflow configuration.
- [ ] Fix any test failure, then re-run and inspect logs.

## C1 — make the package usable in a GPT-6 host
- [ ] Verify the exported ZIP/package artifact is present and downloadable from the workflow run.
- [ ] Verify instructions, manifest, schema and a portable state bundle can be imported without losing identity/provenance.
- [ ] Test on an independent GPT host, if a real host/import mechanism is available; otherwise record NOT RUN with blocker.
- [ ] Keep host-native memory, automatic capture, background execution and external write permissions OPEN until directly tested.

## C2 — CURRENT-068 closure, evidence by evidence
- [ ] Close only sub-gates proven complete by exact-revision evidence.
- [ ] Keep pointer adjudication CURRENT-065/CURRENT-066 unresolved until provenance and consumers are reconciled.
- [ ] Keep historical graph review, Issue #20, Issue #21 and BOART-FOLLOWUP-01 in existing NEXT-051.
- [ ] Keep hash-failure injection and independent-host persistence open unless directly tested.
- [ ] Update the living master with actual run IDs, exact SHA, artifact IDs/digests and scope.

## C3 — recovery and next execution
- [ ] On return, read this checkpoint, the living master, CURRENT-068, NEXT-051 and the latest exact-head workflow receipts.
- [ ] Resume the first executable unchecked item, not another document-writing task.
- [ ] Do not create NEXT-052; NEXT-051 remains the active historical graph queue.

## Honest acceptance boundary

The starter can be called a local executable prototype only after its tests pass on the exact revision and its portable bundle round-trip passes. It cannot be called a deployed GPT plugin unless a real GPT-host integration is implemented and tested. No background work is claimed.
