# User-designated Point 0 — Portable Rahm Architecture

- Stable ID: `G6IP-RAHM-USER-POINT-0-20261024-002`
- Production ID: `G6IP-POINT-0-RAHM-002`
- Version: 1.0.0
- Status at creation: REGISTERED; read-back pending.
- Previous canonical checkpoint: [CURRENT-052](./PALANG-0.0-CURRENT-20261024-052-CONTINUITY-AND-RECOVERY.md)
- Input: [IN-046](./PALANG-0.0-IN-20261024-046-USER-POINT-0-PORTABLE-RAHM.md)
- Output: [OUT-045](./PALANG-0.0-OUT-20261024-045-USER-POINT-0-PORTABLE-RAHM.md)
- Event: [EVT-0153](../../architecture/BEHAVIOR-TRACE/EVT-0153-USER-POINT-0-PORTABLE-RAHM-HARD-AUDIT-2026-10-24.md)
- Independent 0.0: [CURRENT-053](./PALANG-0.0-CURRENT-20261024-053-PORTABLE-RAHM-HARD-AUDIT.md)
- Next: [NEXT-047](./PALANG-0.0-NEXT-20261024-047-RAHM-ARCHITECTURE-HARD-AUDIT.md)

## Purpose
This user-designated Point 0 is additive. It preserves CURRENT-052 and every historical branch. The architecture must be exportable and reconstructable in a new AI host, with evidence, lineage, versions, failures, open gates, living mothers and deterministic next actions. Host capabilities must be separately declared and tested.

## Governing lifecycle
Human request → IN → OUT → EVT → independent anchor → living mother/index/queue → tests and evidence → Rahm review → Master promotion only after validation → export/recovery test → read-back reconciliation.

## Proof boundary
Registration is not runtime activation. Repository read-back is not export integrity. Export integrity is not clean-host recovery. One host is not proof of second-host compatibility. A written background-work specification is not an executing background service. Unrun or failed gates remain OPEN with cause and recovery step.
