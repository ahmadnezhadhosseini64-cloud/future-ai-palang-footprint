# OUT-072 — 0+ Model Acceleration Decision

- Stable ID: HAIF-OUT-072-POINT-0-036-0PLUS-MODEL-ACCELERATION-20261026
- Production ID: HAIF-OUT072-0PLUS-20261026
- Version: 1.0.0
- Status: REGISTERED / ACTIVE / LIVING / OPEN
- Root: [POINT-0/036](./GPT6-RAHM-USER-POINT-0-20261026-036-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md)
- Input: [IN-073](./PALANG-0.0-IN-20261026-073-0PLUS-MODEL-ACCELERATION.md)
- Event: [EVT-0207](../../architecture/BEHAVIOR-TRACE/EVT-0207-POINT-0-036-0PLUS-MODEL-ACCELERATION-2026-10-26.md)
- Next checkpoint: [CURRENT-085](./PALANG-0.0-CURRENT-20261026-085-0PLUS-MODEL-ACCELERATION.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Decision
1. Mark the existing POINT-0/036 as 0+ without creating a competing canonical root.
2. Keep the initial model executable: MASTER governs immutable architecture and accepted knowledge; RAHM stages, validates, hashes and exports/imports state; CHILD is a candidate instance whose promotion requires evidence and explicit gates.
3. Use reversible, provenance-preserving gap covers while the graph is being reconciled. A cover is not a false closure.
4. Keep Path A and Path B separately measurable but connected through the same event ledger, independent IN/OUT anchors, evidence manifest and master reference.
5. Preserve the two unresolved parent edges until their source/target candidates are inspected. Do not infer parents from numeric IDs.
6. Keep independent interactive-host import/restart and long-running persistence NOT RUN until actual receipts from a clean external host exist.

## Verified at last exact-head CI (main SHA 18ccbef16e5bae6e9e31879de8cf575c1c371bec)
Living Architecture Audit and Portable RAHM Conformance both passed. Local starter-engine tests (13), host-adapter tests, timestamp normalization, exact-byte package integrity and live-reference scans passed. Graph: 0 missing local links, 2 unresolved parents, 1 unreviewed Stable-ID collision group, 66 unreviewed Production-ID groups, 5 unreviewed Reference-ID groups, 3 unreviewed event-number groups, 11 exact-content duplicate groups. These are the audited counts for that SHA, not a claim about any later commit.

## Next executable work
Inspect the exact two unresolved parent edges from the audit artifact; repair only if provenance identifies a unique target. Then adjudicate the remaining production/reference/event identity groups in small batches, rerun audit and conformance on the same new SHA, and prepare the clean-host import checklist and portable package receipt.
