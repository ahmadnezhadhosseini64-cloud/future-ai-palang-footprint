# EVT-0214 — POINT-0/040, CURRENT-089 and EVT-0213 Collision

- Stable ID: HAIF-EVT-0214-POINT040-CURRENT089-EVT0213-COLLISION-20261027
- Production ID: HAIF-EVT0214-COLLISION-20261027
- Version: 1.0.0
- Status: REGISTERED / OPEN / IDENTITY COLLISION / RECONCILIATION REQUIRED
- Trigger: two separately created handoff chains were discovered on main after the new-host preparation request.
- Active queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Collision candidates — preserve both, select neither by inference

### Candidate A — Initial Model New-Host Handoff
- Root: [POINT-0/040 — New-Host Handoff](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261027-040-INITIAL-MODEL-NEW-HOST-HANDOFF.md)
- Checkpoint: [CURRENT-089 — New-Host Handoff](../../0.0/anchors/PALANG-0.0-CURRENT-20261027-089-INITIAL-MODEL-NEW-HOST-HANDOFF.md)
- Event: [EVT-0213 — New-Host Handoff](./EVT-0213-INITIAL-MODEL-NEW-HOST-HANDOFF-2026-10-27.md)
- Bootstrap: [NEW-HOST-BOOTSTRAP-2026-10-27](../مدل%20اولیه%20AI/NEW-HOST-BOOTSTRAP-2026-10-27.md)
- Root stable ID: HAIF-POINT-0-040-INITIAL-MODEL-NEW-HOST-HANDOFF-20261027
- Root Production ID: HAIF-P040-20261027

### Candidate B — Initial Model Transfer and Architecture Hard Audit
- Root: [POINT-0/040 — Transfer and Hard Audit](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261027-040-INITIAL-MODEL-TRANSFER-AND-ARCHITECTURE-HARD-AUDIT.md)
- Checkpoint: [CURRENT-089 — Transfer Execution](../../0.0/anchors/PALANG-0.0-CURRENT-20261027-089-INITIAL-MODEL-TRANSFER-EXECUTION.md)
- Event: [EVT-0213 — Transfer and Hard Audit](./EVT-0213-POINT-0-040-INITIAL-MODEL-TRANSFER-AND-HARD-AUDIT-2026-10-27.md)
- Bootstrap: [Initial Model Host Transfer Bootstrap](../../portable/RAHM/INITIAL-MODEL-HOST-TRANSFER-BOOTSTRAP-2026-10-27.md)
- Host prompt: [HOST-BOOTSTRAP-PROMPT](../../portable/RAHM/HOST-BOOTSTRAP-PROMPT-2026-10-27.md)
- Root stable ID: HAIF-POINT-0-040-INITIAL-MODEL-TRANSFER-HARD-AUDIT-20261027
- Root Production ID: HAIF-P040-20261027

## Observed collision facts

1. Both root files claim POINT-0/040 and Production ID HAIF-P040-20261027, but their Stable IDs, paths and contents differ.
2. Two checkpoint files both claim CURRENT-089 but have different Stable IDs, paths and scopes.
3. Two event files both claim EVT-0213 and Production ID HAIF-EVT0213-20261027, but have different Stable IDs, paths and contents.
4. Both bootstrap documents target new-host transfer, but have different paths and are not byte-identical.
5. The portable manifest currently includes Candidate B's root/checkpoint/event and portable boot files. This is evidence of manifest inclusion only; it is not, by itself, sufficient to adjudicate identity or authority.
6. Candidate A's files remain preserved. No deletion, renumbering, silent merge or unsupported canonical selection is authorized by this event.

## Required reconciliation under NEXT-051

1. Compare commit provenance, actual creation/last-change timestamps, automation receipts, declared IDs, source-path authority and references for both candidates.
2. Inspect the registration orchestrator and duplicate-ID gates to determine why two competing short identifiers were issued for one user request.
3. Determine whether Candidate A is an auxiliary interaction record and Candidate B the canonical transfer registration, or whether both must remain separate linked artifacts. Make this decision only from authoritative provenance and the existing registration contract.
4. If a canonical mapping is evidenced, preserve the non-canonical artifact as a collision/alias record; never erase it.
5. Read back the root, checkpoint, event, time binding, mother, indexes, integration queue and manifest after any reconciliation.
6. Run Living Architecture Audit and Portable RAHM Conformance on the same exact final main SHA. Any Evidence Gate commit after the tests creates a new unverified HEAD until tested.

## Status boundary

No candidate is declared the winner by this event. CURRENT-065/CURRENT-066 remains a separate unresolved pointer conflict. NEXT-051 remains the only active queue; do not create NEXT-052. Real independent-host acceptance, restart persistence and external destination proof remain separate gates.
