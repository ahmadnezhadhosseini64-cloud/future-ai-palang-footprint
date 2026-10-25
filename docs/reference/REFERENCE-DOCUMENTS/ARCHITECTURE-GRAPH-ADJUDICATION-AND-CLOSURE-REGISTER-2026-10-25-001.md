# Architecture Graph Adjudication and Closure Register

- Stable ID: ARCHITECTURE-GRAPH-ADJUDICATION-AND-CLOSURE-REGISTER-2026-10-25-001
- Production ID: AGACR-20261025-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN-PARTIAL
- Current anchor: [CURRENT-061](../../0.0/anchors/PALANG-0.0-CURRENT-20261025-061-PROTOTYPE-AND-GRAPH-TRIAGE.md)
- Active queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Historical semantic adjudication source: [H0IRAR](./HISTORICAL-0.0-IDENTIFIER-AND-RELATION-ADJUDICATION-REGISTER-2026-10-21-001.md)
- Historical semantic queue snapshot: [H0SRQS](./HISTORICAL-0.0-SEMANTIC-REVIEW-QUEUE-SNAPSHOT-2026-10-21-001.md)

## Purpose
This register prevents a repeated identifier, link, timestamp, parent edge or exact-content duplicate from being treated as a proven defect—or silently dismissed—without evidence.

## Mandatory group-by-group record
Each group must carry: category, full identifier, every occurrence path, line evidence, exact content hash/commit, role of each occurrence (DEFINES / REFERENCES / MIRROR / SUPERSEDED / TRUE_IDENTITY_CONFLICT / UNRESOLVED), intended canonical identity, parent rationale, inbound/outbound reference results, UTC source and Tehran conversion if applicable, decision author/time, correction commit, read-back and regression result.

## Decision rules
1. A repeated Stable ID is a candidate group, not automatically a collision.
2. A Production ID reused across a master, queue, index or event may be a reference rather than a second definition. Source role must be established.
3. Event short numbers are not identities by themselves; full Stable ID + Production ID + title + path + lineage are required.
4. A parent link resolving to one file proves structural resolution, not semantic parent correctness.
5. A Markdown link proves navigation, not that its target is the correct semantic referent.
6. Exact-byte duplicate content is not permission to delete. Preserve both paths until role, history and inbound references justify MIRROR/ALIAS/SUPERSEDED.
7. Timestamps are compared only after source/type is classified. Repository registration UTC must come from the actual commit timestamp; Tehran is calculated from that same instant. Message/event/operation/test timestamps remain distinct evidence types.
8. Never bulk-renumber, delete, merge or close a group based only on counts.
9. Every correction requires a post-change audit and independent read-back.
10. A gate closes only with an evidence receipt; otherwise OPEN / NOT VERIFIED / BLOCKED.

## Known baseline, not a current re-audit
Historical snapshots disagree because they used different commits, source-file scopes and parsers. One snapshot reported 30 Stable ID groups, 43 Production ID groups, 7 Reference ID groups, 8 EVT short-number groups and 11 exact-content duplicate groups; a later audit reported 62 Stable ID collision groups (61 unreviewed), 88 Production ID groups, 7 Reference ID groups, 36 event-number groups, 13 ambiguous parent edges and one ambiguous timestamp. These figures must not be combined or called the current count. The current commit requires a fresh generated manifest and source-level review.

## Batch 1 disposition
- [x] Defined the adjudication contract and required evidence fields.
- [x] Preserved historic counts as separate, commit-scoped observations.
- [x] Explicitly prevented the false inference “zero missing links = semantically correct graph”.
- [ ] Re-run current graph inventory on the current commit.
- [ ] Import occurrence-level manifest/queue and adjudicate each group.
- [ ] Reconcile Stable IDs, Production IDs, Reference IDs, EVT numbers, parent edges, timestamps and exact duplicates.
- [ ] Publish per-group decisions with line evidence; retain unresolved groups in queue.

## Current result
Governance gap corrected: the project now has an explicit decision contract and non-destructive closure rules. The graph findings themselves are NOT CLOSED by creating this register. Full current occurrence-level adjudication remains OPEN / REVIEW_REQUIRED.
