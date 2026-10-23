# EVT-0124 — Fresh-session recovery gate

- Event ID: EVT-0124
- Stable ID: PALANG-FRESH-SESSION-RECOVERY-GATE-2026-10-23-001
- Production ID: FSRG-HAIF-2026-10-23-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / IMPLEMENTATION-READY / TEST-NOT-RUN
- Parent: [EVT-0123](./EVT-0123-DEEP-EXCAVATION-AND-ARCHITECTURE-UPDATE-2026-10-23.md)
- Current pair: [IN-027](../../0.0/anchors/PALANG-0.0-IN-20261023-027-DEEP-EXCAVATION-ARCHITECTURE-UPDATE.md) / [OUT-027](../../0.0/anchors/PALANG-0.0-OUT-20261023-027-DEEP-EXCAVATION-ARCHITECTURE-UPDATE.md)
- Repository recovery proof: [EVT-0122](./EVT-0122-BIDIRECTIONAL-IN-OUT-RECOVERY-2026-10-23.md)
- Canonical master: [CCCMR](../../reference/REFERENCE-DOCUMENTS/CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md)
- Integration queue: [Architecture Integration Queue](../INTEGRATION-QUEUE/README.md)

## Purpose
Prove that a separate, newly opened ChatGPT conversation can reconstruct the project continuation from canonical repository artifacts, without relying on the current conversation's narrative context. This is distinct from repository unit tests and must not be marked PASS from those tests alone.

## Test procedure
1. Open a separate fresh ChatGPT conversation.
2. Provide the canonical repository URL and this event's path, then request a cold-start recovery without pasting the current conversation summary.
3. Require the fresh session to locate and read back the canonical master, NEXT-024, EVT-0122, EVT-0123, IN-027, OUT-027, the active queue, Issue #20 and Issue #21.
4. Ask it to identify the last tested SHA and CI run/artifact, state the exact scope of the bidirectional recovery proof, list unresolved gaps and name the next action.
5. Compare the result against source files and recorded evidence. Record omissions, stale links, invented claims or mismatches as findings; do not prompt it with missing answers before the first result is captured.
6. Register the fresh-session transcript/result as evidence with timestamp provenance, then independently read back the event, master, queue and 0.0 index.

## Acceptance criteria
- The separate session independently locates canonical repository sources.
- It distinguishes repository-state recovery from runtime-wide capture and external persistence.
- It reports Issue #20 and Issue #21 as OPEN and fresh-session recovery as NOT RUN until this test itself passes.
- It preserves prior 0.0 anchors and does not divert to Dropbox.
- The result, source commit, session evidence and any failure/correction are registered and read-back verified.

## Status boundary
- Repository bidirectional recovery: PASS on the specific EVT-0122 tested SHA/run.
- Fresh-session recovery: NOT RUN.
- Host-wide automatic capture and external persistence: NOT PROVEN.
- Issue #20 and Issue #21: OPEN.


## Ready-to-use handoff and successor checkpoint
- Handoff prompt: [EVT-0124 fresh-session recovery prompt](./EVT-0124-FRESH-SESSION-RECOVERY-PROMPT-2026-10-23.md). It intentionally omits the expected answer so the first response can be evaluated without coaching.
- Current continuation checkpoint: [NEXT-026](../../0.0/anchors/PALANG-0.0-NEXT-20261023-026-FRESH-SESSION-AND-END-TO-END-LEARNING.md).
- Current interaction pair: [IN-028](../../0.0/anchors/PALANG-0.0-IN-20261023-028-ACTIVATE-LIVING-ARCHITECTURE-UPDATE.md) / [OUT-028](../../0.0/anchors/PALANG-0.0-OUT-20261023-028-ACTIVATE-LIVING-ARCHITECTURE-UPDATE.md).
- Architecture-update capability CI proof: [EVT-0125](./EVT-0125-LIVING-ARCHITECTURE-UPDATE-CAPABILITY-2026-10-23.md).
