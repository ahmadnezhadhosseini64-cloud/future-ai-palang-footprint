# NEXT-051 — Full Graph Triage and Clean-Host Recovery

- Stable ID: `G6IP-RAHM-NEXT-051-20261024`
- Production ID: `G6IP-NEXT-051`
- Version: 1.0.3
- Status: OPEN / LIVING / IN PROGRESS / NOT COMPLETE.
- Parent: [CURRENT-057](./PALANG-0.0-CURRENT-20261024-057-REPOSITORY-EXCAVATION-AND-LIVING-RECOVERY.md)
- Preserve existing gates: [NEXT-050](./PALANG-0.0-NEXT-20261024-050-FULL-RECOVERY-AND-REAL-HOST-IMPORT.md), [NEXT-049](./PALANG-0.0-NEXT-20261024-049-REAL-HOST-TRANSFER-AND-GRAPH-AUDIT.md)

## Ordered actions
1. Independently fetch/read back Point 0/006, IN-050, OUT-049, EVT-0159, CURRENT-057, NEXT-051, portable master, manifest, canonical index and main integration queue.
2. Re-run the strict portable conformance workflow after the new files and mother/index/queue changes. Reconcile exact-byte SHA-256 values and package digest from raw workflow receipts.
3. Verify relative links for the new chain and all touched mother/index/queue files; record any broken destinations individually.
4. Extend IN/OUT recovery from link/checkpoint equivalence to full canonical-state reconstruction: parent chain, versions, event IDs, evidence receipts, failure/correction pairs and every OPEN gate must match.
5. Triage the repository-wide audit one finding at a time: 11 missing links, 60 unreviewed stable-ID collision groups, 88 production-ID collision groups, 7 reference-ID collision groups, 36 event-number collision groups and 13 ambiguous parent edges. No bulk deletion or speculative renumbering.
6. Import the export package into a clean independent AI host with no prior chat context, only if a real authorized host is available. Record actual host/model, capability manifest, reconstruction result and independent read-back. CI is not a separate AI host.
7. Test a second host, persistent memory after restart, and idle/background execution only in an actual authorized runtime. Otherwise retain OPEN / NOT VERIFIED / BLOCKED.
8. Update living master, canonical index, main queue and manifest only with evidence, then independently fetch each changed file and compare.
9. Deliver a visible user-facing result at each durable milestone; do not claim background work between turns.

## Acceptance criteria
- New artifacts and updated canonical destinations pass read-back and focused link checks.
- All manifest file digests match exact bytes and the package archive hash is recorded.
- Independent IN and OUT recovery reconstruct identical canonical state and preserve all open gates.
- Clean-host import proves recovery without hidden chat context, or remains explicitly NOT RUN.
- Repository graph findings are individually adjudicated or remain open with evidence.
- No unverified item is closed.

## Always-open rule
NEXT-051 remains OPEN/LIVING until all required acceptance criteria have evidence. NEXT-049 and NEXT-050 remain open independently.


## Latest excavation recheck — run 40124425936 / 2026-10-24
- Structural audit workflow completed, but content result remains `REVIEW_REQUIRED`: 3,757 files including generated evidence; 5,564 local-link edges; 16 missing links; 62 stable-ID collision groups (61 unreviewed); 88 production-ID collision groups; 7 reference-ID collision groups; 36 event-number collision groups; 13 ambiguous parent edges; 0 decode errors.
- Strict portable conformance run [40124425568](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40124425568) passed for manifest v1.4.2: schema valid fixture 0 errors, invalid fixture rejected with 4 errors, all expected file digests matched, limited IN/OUT checkpoint-link equivalence passed; package 44 files / 221380 bytes / SHA-256 `591377d03546e6f031ee98614b1c9fbd662dba08a15bc5c68b15bd918282f501`.
- These are repository/CI results only. Full IN/OUT state reconstruction, clean/second AI-host import, actual persistence restart and idle/background execution remain OPEN / NOT VERIFIED.


## Execution ledger — actual work completed before this update
- [x] Focused read-back of Point 0/006, IN-050, OUT-049, EVT-0159, CURRENT-057, NEXT-051, portable master, manifest, canonical index and main queue; identifiers and versions checked.
- [x] Focused relative-link check across the 13 target chain/master/index/queue files: zero broken destinations.
- [x] Corrected six actual documentation links: five in the initial-model mother and one in EVT-0132.
- [x] Corrected graph-audit scope to exclude Markdown-like links embedded in Python test fixtures; prior 16 missing-link findings included 10 fixture false positives.
- [x] Added a CI gate for the latest Point 0/006 → CURRENT-057/NEXT-051 chain and master/index/queue surfaces.
- [x] Read-back verified successful writes.
- [~] Strict digest/package: pre-edit run [40124660624](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40124660624) passed 43/43 exact-byte SHA-256 entries, schema fixtures (0 errors valid / 4 errors invalid), limited IN/OUT checkpoint-link equivalence and package build (44 files / 224852 bytes / SHA-256 `475ff58474f10a4a75314c964302bac06f7ed15d47e31da1826c31bce293c50a`). Final post-edit run remains required.
- [~] Global graph triage: post-fix audit pending. Pre-fix findings were 16 link reports (6 real documentation links now fixed; 10 Python fixture false positives), 61 unreviewed stable-ID groups, 88 production-ID groups, 7 reference-ID groups, 36 event-number groups, 13 ambiguous parents and one ambiguous timestamp.

## Remaining gates — OPEN
- [ ] Final post-edit strict digest scan and package build.
- [ ] Full canonical-state reconstruction independently from IN and OUT; compare evidence, failures, corrections, versions and open gates.
- [ ] Clean independent AI-host import; CI runner transfer is not equivalent.
- [ ] Second AI-host import.
- [ ] Actual persistence restart and idle/background execution in an authorized real runtime.
- [ ] Individual adjudication of remaining global graph findings; no bulk deletion or speculative renumbering.

NEXT-051 remains OPEN/LIVING. Do not create a new NEXT merely to move the number while these acceptance gates remain unfinished.


## Latest post-fix audit receipt — run 40129104121
- [x] Repository-wide Markdown link gate: 0 missing local Markdown links across 5,564 edges; 3,805 files including generated evidence. Run: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40129104121
- [x] Latest Point 0/006 → CURRENT-057/NEXT-051 and Point 0/007 → CURRENT-058/NEXT-051 CI continuity gates passed.
- [x] Structural repository checks passed; content result remains REVIEW_REQUIRED because 62 Stable-ID collision groups (61 unreviewed), 88 Production-ID collision groups, 7 Reference-ID collision groups, 36 event-number collision groups, 13 ambiguous parent edges and one ambiguous timestamp remain.
- [x] Strict baseline run [40129104156](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40129104156) passed 50/50 SHA-256 entries, schema fixtures, limited recovery equivalence and archive build; this predates the latest updates.
- [~] New full repository IN/OUT state reconstruction verifier has been added and wired into the audit workflow; first run pending.

## Still OPEN — do not close
Full canonical-state recovery until the new verifier passes; real clean/second AI-host import; persistence restart; idle/background execution; individual adjudication of all collision, parent and timestamp findings. NEXT-051 remains active; do not create NEXT-052 while these gates remain open.
