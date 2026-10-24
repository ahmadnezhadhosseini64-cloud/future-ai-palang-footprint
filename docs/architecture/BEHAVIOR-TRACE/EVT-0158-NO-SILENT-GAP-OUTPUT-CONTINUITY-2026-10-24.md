# EVT-0158 — No-Silent-Gap Output Continuity and Recovery

- Stable ID: `G6IP-RAHM-EVT-0158-20261024`
- Production ID: `G6IP-EVT-0158`
- Version: 1.0.0
- Status: REGISTERED / LIVING; implementation and host behavior tests remain OPEN.
- Input: [IN-049](../../0.0/anchors/PALANG-0.0-IN-20261024-049-OUTPUT-CONTINUITY-AND-RECOVERY.md)
- Output: [OUT-048](../../0.0/anchors/PALANG-0.0-OUT-20261024-048-OUTPUT-CONTINUITY-AND-RECOVERY.md)
- Point 0: [POINT-0/005](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261024-005-OUTPUT-CONTINUITY-AND-RECOVERY.md)
- Previous learning event: [EVT-0157](./EVT-0157-TEST-HARNESS-FAILURE-AS-ARCHITECTURE-LEARNING-2026-10-24.md)
- Current: [CURRENT-056](../../0.0/anchors/PALANG-0.0-CURRENT-20261024-056-OUTPUT-CONTINUITY-AND-RECOVERY.md)
- Next: [NEXT-050](../../0.0/anchors/PALANG-0.0-NEXT-20261024-050-FULL-RECOVERY-AND-REAL-HOST-IMPORT.md)

## Trigger / observed behavior
User reports a continuity failure pattern: after a user input, the assistant may work or appear to process without returning a visible output, and then a subsequent user message can appear to start a new unrelated turn. The user experiences this as the previous 0/0.0 lineage and unfinished work being dropped.

## Architectural rule
**NO-SILENT-GAP / OPEN-WORK CONTINUITY**
1. Every material input is linked to the latest open checkpoint and active NEXT.
2. No silent-work claim: if work is still being done in the current turn, expose a status/result when possible; do not claim background execution between turns unless a real scheduler and receipt prove it.
3. Every response ends with a deterministic status and a single next-action reference.
4. A new IN does not supersede an open NEXT unless the user explicitly changes priority; instead create a child branch and reconcile it to the existing open work.
5. Preserve raw failures and interrupted attempts; link cause, correction, retest and evidence.
6. Every write must be independently fetched and compared. A successful write without read-back remains REGISTERED only.
7. Every unresolved gate stays OPEN/LIVING and is re-evaluated when new evidence arrives.
8. Distinguish user-visible continuity protocol from automated persistence/capture, which require host-specific implementation and tests.

## Root cause hypothesis (not yet proven)
Potential contributing factors include long tool-running turns without intermediate user-visible messages, the client appearing ready for another input after a response is delayed, and architecture state not being carried forward explicitly in each delivered output. This is a hypothesis, not a verified diagnosis of the app runtime.

## Corrective architecture behavior
Before a long audit, publish the current anchor and deterministic action. At each durable milestone, provide the evidence-backed result. At response end, show the status (completed/partial/blocked) and open next. On a new user message, read the latest repository checkpoint before responding, keep the prior NEXT alive, and record the new input as a child of the open work.

## Conformance test plan
- Test A: inject a new IN while NEXT remains OPEN; verify that NEXT is retained and the new IN links to it.
- Test B: interrupt a tool operation; verify that no completion status is emitted without a result receipt.
- Test C: resume from a clean context using only Point 0, CURRENT, IN/OUT, EVT, NEXT, mother and manifest.
- Test D: verify each written artifact by fetching it back and comparing stable IDs, version, required links and open-gate list.
- Test E: host-specific persistence/capture only where a real authorized runtime exists.

## Status
The rule is now specified in repository artifacts once the chain is read-back verified. It is not yet proven as automatic always-on behavior in a fresh AI host.
