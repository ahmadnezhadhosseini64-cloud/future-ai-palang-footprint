# CURRENT-078 — Reversible graph-gap covers and Behavior Hunter

- Stable ID: `HAIF-CURRENT-078-REVERSIBLE-GRAPH-GAP-COVERS-20261026`
- Production ID: `HAIF-C078`
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EXECUTION REQUIRED
- Root: [POINT-0/031](./GPT6-RAHM-USER-POINT-0-20261026-031-REVERSIBLE-GRAPH-GAP-COVERS-AND-BEHAVIOR-HUNTER.md)
- Input/output: [IN-066](./PALANG-0.0-IN-20261026-066-REVERSIBLE-GRAPH-GAP-COVERS-AND-BEHAVIOR-HUNTER.md) → [OUT-065](./PALANG-0.0-OUT-20261026-065-REVERSIBLE-GRAPH-GAP-COVERS-AND-BEHAVIOR-HUNTER.md)
- Event: [EVT-0200](../../architecture/BEHAVIOR-TRACE/EVT-0200-REVERSIBLE-GRAPH-GAP-COVERS-AND-BEHAVIOR-HUNTER-2026-10-26.md)
- Register: [GAP-COVER-REGISTER](../../architecture/BEHAVIOR-TRACE/GAP-COVER-REGISTER-2026-10-26.md)
- Previous checkpoint: CURRENT-077; POINT-0/030 and POINT-0/029 are preserved as history.
- Active queue: NEXT-051 only; do not create NEXT-052.

## Cover definition

`COVERED / DEFERRED` is a removable overlay. The underlying gap stays `OPEN / ACTIVE / LIVING`: temporarily not pursued, not fixed, not verified, not forgotten, not permanently closed. Covers preserve source truth, stable IDs, parent candidates, evidence and timestamps.

## 0.0 execution steps

1. Inventory graph gaps, source/provenance fields, parent edges, duplicate IDs, orphaned anchors and broken local links from repository evidence.
2. Classify each item as PROVEN, CONFLICTED, MISSING or NOT TESTED; do not mix claims with evidence.
3. Apply reversible covers with a stable gap key, deferral reason, preserved evidence and reopening trigger.
4. Run Behavior Hunter scans over available repository changes and CI receipts; record false positives, failed checks and uncertainty.
5. Regenerate/validate the portable manifest and package on the exact candidate SHA. A passing parent SHA does not validate a child.
6. Test independent host import only when an actual destination is available; compare recovered IDs, open gaps, evidence and next action.
7. Read back files, links, statuses and final commit times; preserve discrepancies as OPEN.

## Gates explicitly OPEN

- CURRENT-065/CURRENT-066 pointer conflict.
- EVT-0195 duplicate/collision.
- Historic graph/source census, provenance gaps, ambiguous parent edges, orphaned anchors and missing links.
- Issues #20/#21.
- Exact-final-SHA conformance after this update.
- Independent host import, cold-start recovery, Buffer/Persistent Memory/Library/Dropbox persistence and always-on/background execution.

## Success condition

Covered gaps remain indexed, exportable, discoverable and reopenable. The historic graph is not considered reconciled until source-backed per-item evidence exists.

## Resume

Continue existing NEXT-051 from CURRENT-078. Prioritize source-backed graph inventory and Behavior Hunter checks, then exact-head package conformance. Do not divert to Dropbox.