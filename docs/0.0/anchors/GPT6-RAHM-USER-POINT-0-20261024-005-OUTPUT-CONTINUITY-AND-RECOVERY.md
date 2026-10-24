# User-designated Point 0 — Output Continuity, Interrupted Work and Recovery

- Stable ID: `G6IP-RAHM-USER-POINT-0-20261024-005`
- Production ID: `G6IP-USER-POINT-0-005`
- Version: 1.0.1
- Status: REGISTERED / READ-BACK VERIFIED / LIVING; full host-transfer and graph-remediation gates remain OPEN.
- Previous user Point 0: [POINT-0/004](./GPT6-RAHM-USER-POINT-0-20261024-004-TEST-HARNESS-AND-FIRST-MASTER-READINESS.md) — preserved, not overwritten.
- Previous current: [CURRENT-055](./PALANG-0.0-CURRENT-20261024-055-FIRST-MASTER-READINESS.md)
- New input: [IN-049](./PALANG-0.0-IN-20261024-049-OUTPUT-CONTINUITY-AND-RECOVERY.md)
- Assistant output: [OUT-048](./PALANG-0.0-OUT-20261024-048-OUTPUT-CONTINUITY-AND-RECOVERY.md)
- Event: [EVT-0158](../../architecture/BEHAVIOR-TRACE/EVT-0158-NO-SILENT-GAP-OUTPUT-CONTINUITY-2026-10-24.md)
- Living mother: [FIRST-LIVING-MASTER](../../portable/RAHM/FIRST-LIVING-MASTER-PORTABLE-GPT6-HAIF.md)
- Current 0.0: [CURRENT-056](./PALANG-0.0-CURRENT-20261024-056-OUTPUT-CONTINUITY-AND-RECOVERY.md)
- Next 0.0: [NEXT-050](./PALANG-0.0-NEXT-20261024-050-FULL-RECOVERY-AND-REAL-HOST-IMPORT.md)

## Purpose
This is a new, independent user-designated return anchor. It adds the user's explicit requirement that an interaction chain must not silently disappear when there is a gap between input and output. It must connect to the inherited architecture, preserve all previous branches, and continue the deterministic open work rather than replacing it with a report.

## Binding rule: NO-SILENT-GAP / INTERRUPTION CONTINUITY
1. Every material user input becomes an IN record; every substantive assistant response becomes an OUT record; actions, test results, failures and corrections become event/evidence records.
2. Before any lengthy tool-driven work, expose a useful status/output: current anchor, what is being attempted, and what remains open. Do not leave the user with a silent chat state that could be mistaken for completion or abandonment.
3. At the end of every response, state one of: COMPLETED WITH EVIDENCE; PARTIAL—OPEN ITEMS LISTED; BLOCKED WITH REASON; or CONTINUING FROM [NEXT ID]. Do not imply invisible background work.
4. If a new user message arrives while a prior NEXT is open, preserve that NEXT. Register the new message as a child input linked to the open work, reconcile priority, and resume from the deterministic next action unless the user explicitly changes scope.
5. Never treat silence, missing output, a new message, or a written record as proof that work ran or succeeded. Record interrupted/failed attempts and resume using the last read-back-verified checkpoint.
6. If exact raw conversation content is unavailable to the host, mark it MISSING and use repository-linked evidence; never reconstruct a verbatim quote from memory.
7. Each update requires version, source/provenance, independent anchor, evidence, read-back, match result, residual gaps and next action.
8. These rules govern model response behavior and recovery protocol; they do not themselves create autonomous background execution, automatic message capture, or durable host memory.

## Inherited open work
CURRENT-055 and NEXT-049 remain active in their historical branch. This point does not close or replace the 11 repository-wide missing links, 60 unreviewed stable-ID collision groups, 88 production-ID collision groups, 7 reference-ID collision groups, 36 event-number collision groups, 13 ambiguous parent edges, or the one ambiguous time reported by the latest structural audit.

## Recovery rule
On a fresh host, load the portable master and manifest; identify this Point 0 and CURRENT-056; reconstruct the open queue; confirm all historical branches; then execute NEXT-050. If any source, test receipt, or runtime capability is absent, preserve it as OPEN / NOT VERIFIED.

## Time authority
Repository registration time must be derived from the actual last-change Git commit timestamp in UTC; Asia/Tehran is a conversion of the same instant. The commit time is not represented as the exact time the user sent the message.
