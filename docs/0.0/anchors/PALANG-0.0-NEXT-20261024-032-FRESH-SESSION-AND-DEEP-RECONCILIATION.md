# NEXT-032 — Fresh-session recovery and deep reconciliation

- Checkpoint ID: NEXT-032
- Stable ID: PALANG-0.0-NEXT-20261024-032-FRESH-SESSION-AND-DEEP-RECONCILIATION
- Production ID: NEXT-032
- Version: 1.0.0
- Status: ACTIVE / LIVING / REPOSITORY-CI-PASS / FRESH-SESSION-OPEN
- Current pair: [IN-032](./PALANG-0.0-IN-20261024-032-LIVING-STATUS-AND-ARCHITECTURE-GROWTH.md) / [OUT-032](./PALANG-0.0-OUT-20261024-032-LIVING-STATUS-AND-ARCHITECTURE-GROWTH.md)
- Event: [EVT-0130](../../architecture/BEHAVIOR-TRACE/EVT-0130-LIVING-STATUS-ARCHITECTURE-GROWTH-DEEP-AUDIT-2026-10-24.md)
- Prior checkpoint: [NEXT-031](./PALANG-0.0-NEXT-20261024-031-LATEST-PAIR-RECOVERY-AND-STATUS-TRANSPARENCY.md)
- Canonical master: [CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE](../../reference/REFERENCE-DOCUMENTS/CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md)

## Execution order
1. Run Behavior Hunter after the complete pair-032 commit; inspect both recovery manifests and require IN-032/OUT-032, EVT-0130 and NEXT-032.
2. Re-read master, queue, TALL, indexes, event and anchors; compare required links and statuses.
3. Preserve CI failures and root causes as new append-only events; do not hide or rewrite failed runs.
4. Perform the separate ChatGPT cold-start test using the handoff prompt in EVT-0124, without giving the new session this conversation's answer key.
5. Continue Issue #19 real-document ingestion/restart acceptance, Issue #20 live capture/end-to-end recovery, and Issue #21 historical source census/semantic adjudication. Keep each independently open until proven.
6. Keep the user-facing status explicit: RUNNING, VERIFIED, BLOCKED or OPEN; state the latest durable evidence and next action.
7. Keep architecture proposals evidence-gated and owner-reviewed; never automatically mutate MASTER.

## Completion conditions
Pair 032 is recovered from both directions on the exact tested SHA; all canonical references point to the current pair; artifact manifests are downloaded and inspected; separate fresh-session recovery has its own first-response evidence; and all remaining gaps are explicitly preserved.


## Immediate corrective action — pair-032 reciprocal link
The first run failed because IN-032 lacked a direct OUT-032 link. This defect is recorded in EVT-0130. The next CI run must prove reciprocal identity and recover pair 032 from both directions. The failed run must remain preserved.


## Pair-032 CI result
Run 40060524636 succeeded on tested SHA `6936932f39d21d5af422d357ee0b41082a9f281e`; both recovery directions were inspected in artifact 12547123152 (SHA-256 `c8a8cd44292be51def96d51dc4930fcaf5a304137f901053b69c1640784209ab`). Next: perform the separate fresh-session test and continue Issues #19/#20/#21. This repository result does not close those external/runtime gaps.
