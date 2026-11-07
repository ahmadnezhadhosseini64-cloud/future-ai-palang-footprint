# CURRENT-113 — نقطهٔ اجرای ۰.۰ برای آزمون تداوم خبر

- Stable ID: HAIF-CURRENT-113-NEWS-CONTINUITY-2026-11-07-001
- Parent root: POINT-0/062 (0+)
- Chain: POINT-0/062 → IN-101 → OUT-100 → EVT-0254 → CURRENT-113 → NEXT-051
- Version: 1.0.0
- Status: OPEN / ACTIVE / EXECUTION REQUIRED
- Timezone: Asia/Tehran
- User-message timestamp: UNKNOWN / UNVERIFIED
- Sole active queue: NEXT-051; no NEXT-052.

## Current task

Run the user-defined news workflow as a real continuity test. Retrieve and preserve its complete rules from POINT-0/062. At each user request, determine the last actually delivered report/update and the current request time; retrieve fresh sources and cover the interval without assuming missed reports or repeating unchanged stories.

## Acceptance tests

T01 instruction retrieval; T02 07:00 baseline; T03 11:00 incremental update; T04 arbitrary-time update; T05 missed-window continuity; T06 no-duplicate behavior; T07 source/time/market evidence; T08 Gonbad-e Kavus weather location; T09 restart recovery; T10 independent-host recovery.

Each test remains OPEN / NOT RUN until a real, inspectable receipt is recorded. For a failed test, preserve the failure and exact missing edge; do not silently downgrade the requirement or mark it passed.

## Next execution sequence

1. Finish cross-file registration and exact read-back.
2. Reconcile the root/checkpoint pointers in the 0.0 registry, Reference Index, Behavior Trace and Integration Queue.
3. Append the new rule and test to the existing living master without replacing its identity or history.
4. Recheck the existing 07:00 automation; do not create duplicate automation or convert manual windows into schedules without explicit instruction.
5. Execute the next available real test and preserve its sources/receipt.
6. Run a fresh-session recovery, then an independent-host recovery when the target host is available.
7. Continue all pre-existing NEXT-051 work, including package, exact-final-SHA, runtime, graph and clean-host gates.

## Evidence boundaries

Repository writes do not prove Buffer, Library, Persistent Memory, Dropbox, app automation, background monitoring or independent-host recovery. Do not claim those destinations or capabilities ACTIVE/VERIFIED without destination-specific evidence.

## Child continuation pointer — POINT-0/063
The next user-turn root is [POINT-0/063 (0+)](GPT6-RAHM-USER-POINT-0-20261107-063-GRAPH-WIDE-CONTINUITY-AND-ANCHORING.md), followed by [CURRENT-114](PALANG-0.0-CURRENT-20261107-114-GRAPH-WIDE-CONTINUITY.md) and the existing [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md). CURRENT-113 remains the historical checkpoint for POINT-0/062; no prior state is overwritten.
