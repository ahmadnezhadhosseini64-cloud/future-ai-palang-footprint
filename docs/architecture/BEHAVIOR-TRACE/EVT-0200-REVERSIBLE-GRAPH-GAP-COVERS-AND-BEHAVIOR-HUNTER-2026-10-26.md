# EVT-0200 — Reversible graph-gap covers and Behavior Hunter

- Stable ID: `HAIF-EVT-0200-REVERSIBLE-GRAPH-GAP-COVERS-20261026`
- Production ID: `HAIF-EVT-0200`
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / COVERED-NOT-CLOSED
- Root: [POINT-0/031](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-031-REVERSIBLE-GRAPH-GAP-COVERS-AND-BEHAVIOR-HUNTER.md)
- Input/output: [IN-066](../../0.0/anchors/PALANG-0.0-IN-20261026-066-REVERSIBLE-GRAPH-GAP-COVERS-AND-BEHAVIOR-HUNTER.md) → [OUT-065](../../0.0/anchors/PALANG-0.0-OUT-20261026-065-REVERSIBLE-GRAPH-GAP-COVERS-AND-BEHAVIOR-HUNTER.md)
- Checkpoint: [CURRENT-078](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-078-REVERSIBLE-GRAPH-GAP-COVERS.md)
- Register: [GAP-COVER-REGISTER](./GAP-COVER-REGISTER-2026-10-26.md)
- Queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Intent

The user makes this turn a new POINT-0 and next work 0.0. Put temporary covers over graph, source/provenance and parent-edge gaps. Each cover remains reversible; all underlying gaps remain OPEN, ACTIVE, LIVING, retrievable and in Behavior Hunter scope.

## Cover contract

- `COVERED / DEFERRED` lowers immediate priority; it does not alter truth status.
- Preserve stable key, source location, evidence, competing candidates, uncertainty, timestamps and reopening trigger.
- Never convert missing evidence into a positive assertion. Never resolve duplicate EVT-0195 or CURRENT-065/CURRENT-066 by inference.
- “فعلاً کنار بگذار / ببند برای الان” means COVERED / DEFERRED with underlying OPEN.
- Permanent closure requires evidence, acceptance criteria and independent read-back; this event closes nothing.

## Behavior Hunter observation contract

On each available repository scan or CI run, inspect:
1. New, changed or deleted graph/source/parent records.
2. Broken relative links and orphaned anchors.
3. Duplicate stable/production/event IDs and conflicting current pointers.
4. Missing provenance, ambiguous parent candidates and timestamp conflicts.
5. Covered gaps disappearing from indexes, boot contract or export manifest.
6. Exact-head test/package evidence tied to a different SHA than current main.
7. Host-import claims without a direct destination receipt.

For every finding preserve source, observed output, evidence, uncertainty, failed checks, action and reopening trigger. Monitoring is scan/event-driven; do not claim continuously running background observation without a real scheduler/runtime receipt.

## Gates retained OPEN

CURRENT-065/CURRENT-066 pointer ambiguity; duplicate EVT-0195 collision; historic graph census and semantic reconciliation; Issues #20/#21; independent clean-host import and cold-start reconstruction; Buffer/Persistent Memory/Library/Dropbox evidence; always-on/background execution proof.

## Acceptance boundary

This event registers cover governance and monitoring criteria. It does not claim full graph reconciliation or independent host import. Continue existing NEXT-051 from CURRENT-078.

## Time rule

UTC is canonical; Asia/Tehran is derived (+03:30). Repository registration time comes from actual Git commit metadata for this final content. Workflow time is separate evidence.