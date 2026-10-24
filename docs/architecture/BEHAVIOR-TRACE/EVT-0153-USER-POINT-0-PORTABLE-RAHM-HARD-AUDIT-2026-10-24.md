# EVT-0153 — User Point 0: Portable Rahm and Architecture Hard Audit

- Event ID: EVT-0153
- Stable ID: `G6IP-RAHM-EVT-0153-20261024`
- Production ID: `G6IP-EVT-0153`
- Version: 1.0.0
- Request: make this interaction Point 0, continue at 0.0, connect the graph and hard-audit the architecture for extraction, recovery and evolution in a new AI host.
- Input: [IN-046](../../0.0/anchors/PALANG-0.0-IN-20261024-046-USER-POINT-0-PORTABLE-RAHM.md)
- Output: [OUT-045](../../0.0/anchors/PALANG-0.0-OUT-20261024-045-USER-POINT-0-PORTABLE-RAHM.md)
- User Point 0: [G6IP-RAHM-USER-POINT-0-20261024-002](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261024-002.md)
- Checkpoint: [CURRENT-053](../../0.0/anchors/PALANG-0.0-CURRENT-20261024-053-PORTABLE-RAHM-HARD-AUDIT.md)
- Next gate: [NEXT-047](../../0.0/anchors/PALANG-0.0-NEXT-20261024-047-RAHM-ARCHITECTURE-HARD-AUDIT.md)
- Previous live checkpoint: [CURRENT-052](../../0.0/anchors/PALANG-0.0-CURRENT-20261024-052-CONTINUITY-AND-RECOVERY.md)

## Observed source state
The default branch is `main`. CURRENT-052 is the latest canonical checkpoint observed and NEXT-044 is the active export/fresh-context recovery gate. The portable RAHM package includes boot instructions, architecture, host capability manifest, interaction-pair JSON Schema, evidence ledger, conformance tests, export manifest and recovery/rollback specification.

## Hard-audit findings
1. The export manifest says SHA-256 is pending and contains Git blob SHA-1 values; these are not SHA-256.
2. The schema exists, but the conformance specification says execution is NOT RUN. Existence is not validation.
3. NEXT-044 remains OPEN / NOT RUN for export creation and fresh-context reconstruction.
4. Clean-host/second-host transfer, persistence across restart and idle background execution need independent runtime evidence.
5. The repository contains multiple historical branches. A new Point 0 must be additive; CURRENT-048 remains preserved and must not silently replace the later CURRENT-052 chain.
6. The index and queue contain historical entries; their presence does not prove a complete repository-wide link audit.

## Behavioral lesson
When asked to make the current interaction Point 0 and connect every point, inspect the actual branch and newest CURRENT/NEXT first. Then add an anchor and reconcile the mother/index/queue. Do not equate a written architecture with an installed runtime or redirect to unrelated branches.

## Status boundary
This event records source inspection and findings. Tests not executed with retained evidence remain OPEN / NOT RUN. No universal AI-host compatibility or unattended continuous operation is claimed.
