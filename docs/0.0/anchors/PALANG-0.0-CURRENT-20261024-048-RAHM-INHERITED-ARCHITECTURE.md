# CURRENT-048 — نقطهٔ جاری: رحم در معماری موروثی
- Stable ID: G6IP-RAHM-CURRENT-048-20261024
- Production ID: G6IP-CURRENT-048
- Version: 1.0.0
- Status: REGISTERED; read-back must be evidenced; runtime/transfer tests OPEN
- Parent: [CURRENT-047](./PALANG-0.0-CURRENT-20261024-047-BEHAVIOR-HUNTER-LIVING-ANCHOR.md)
- Input: [IN-040](./PALANG-0.0-IN-20261024-040-RAHM-INHERITED-ARCHITECTURE.md)
- Output: [OUT-040](./PALANG-0.0-OUT-20261024-040-RAHM-INHERITED-ARCHITECTURE.md)
- Event: [EVT-0148](../../architecture/BEHAVIOR-TRACE/EVT-0148-RAHM-INHERITED-ARCHITECTURE-AND-EXPORTABLE-RECOVERY-2026-10-24.md)
- Prior 0.0 work: [NEXT-045](./PALANG-0.0-NEXT-20261024-045-BEHAVIOR-HUNTER-TEST-AND-OPEN-GATES.md)
- Next 0.0: [NEXT-046](./PALANG-0.0-NEXT-20261024-046-RAHM-PORTABILITY-VALIDATION.md)
- RAHM boot: [RAHM_BOOT.md](../../portable/RAHM/RAHM_BOOT.md)
- RAHM architecture: [RAHM_ARCHITECTURE.md](../../portable/RAHM/RAHM_ARCHITECTURE.md)
- Inherited architecture mother: [GPT6 inherited master](../../reference/REFERENCE-DOCUMENTS/GPT6-NEW-PROJECT-INHERITED-ARCHITECTURE-LIVING-MASTER-2026-10-24-001.md)
- HAIF mother: [HAIF model mother](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)

## Governing rule
Observable user/AI interaction data can inform behavior hypotheses and architecture evolution only with provenance and evidence. Repeated observations do not automatically become validated rules. Documentation is not runtime activation; repository read-back is not host portability proof.

## Chain
CURRENT-046 → IN-039 → OUT-039 → EVT-0147 → CURRENT-047 → IN-040 → OUT-040 → EVT-0148 → CURRENT-048 → NEXT-046.

## Open gates
- RAHM export/import in a clean host and an independent second host.
- Exact-byte SHA-256 and export-manifest reconciliation.
- Positive/negative JSON Schema fixtures and interaction-pair replay.
- Complete link and duplicate-ID audit.
- Restart recovery from IN and from OUT.
- Persistent memory and idle background execution, only if an authorized runtime exists.
- Any unrun/failed item remains OPEN with its reason and recovery step.

## Recovery
Resume from NEXT-046; preserve CURRENT-047 and all earlier anchors. Do not redirect to Dropbox unless explicitly requested.