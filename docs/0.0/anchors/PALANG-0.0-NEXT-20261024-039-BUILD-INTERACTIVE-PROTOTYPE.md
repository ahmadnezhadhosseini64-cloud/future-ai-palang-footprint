# NEXT-039 — ساخت نخستین نمونهٔ تعاملی کوچک از نقطهٔ ۰.۰

- Stable ID: PALANG-NEXT-GPT6-BUILD-INTERACTIVE-PROTOTYPE-2026-10-24-039
- Production ID: G6IP-NEXT-039
- Version: 1.0.0
- Status: OPEN / ACTIVE / LIVING / SOURCE BUILT; BROWSER EXECUTION NOT VERIFIED
- Parent checkpoint: [GPT6 Point 0.0](./GPT6-INTERACTIVE-PROJECT-POINT-0.0-CHECKPOINT-2026-10-24-001.md)
- Root point: [Point 0](./GPT6-INTERACTIVE-PROJECT-POINT-0-INITIAL-ROOT-2026-10-24-001.md)
- Architecture zero: [G6IP-ARCH-ZERO-20261024-001](./PALANG-0.0-ARCHITECTURE-ZERO-20261024-001-NEW-PROJECT-ARCHITECTURE-ROOT.md)\n- Latest inherited architecture: [G6IP-IAM-20261024-001 v1.0.4](../../reference/REFERENCE-DOCUMENTS/GPT6-NEW-PROJECT-INHERITED-ARCHITECTURE-LIVING-MASTER-2026-10-24-001.md)
- GPT-6 living master: [Living master](../../reference/REFERENCE-DOCUMENTS/GPT6-INTERACTIVE-PROJECT-LIVING-MASTER-REFERENCE-2026-10-24-001.md)
- Event: [EVT-0139](../../architecture/BEHAVIOR-TRACE/EVT-0139-GPT6-POINT-0.0-CHECKPOINT-CREATION-2026-10-24.md)

## Objective
Build the smallest useful interactive prototype under the inherited HAIF governance. It must demonstrate a real user-controlled input, visible derived output, state update, and a recordable IN/OUT interaction. It must be explicitly identified as a prototype, not a complete product.

## Required contract
1. State the user problem and one narrow use case.
2. Define input types, validation, output behavior, error state, and reset/recovery behavior.
3. Specify measurable acceptance criteria before claiming PASS.
4. Link the prototype to Point 0.0, the latest architecture master, IN/OUT, event, and evidence record.
5. Store implementation/source and a runnable or inspectable artifact in the repository.
6. Verify the artifact by reading back the exact files and exercising the documented path; record actual results.
7. If runtime execution is unavailable, mark the execution test NOT RUN and provide a reproducible manual test procedure.
8. After a real artifact exists, create a separate cold-start recovery test; until then NOT RUN.
9. Preserve all previous anchors and the current architecture master history.

## Acceptance gates
- Prototype exists as a distinct artifact.
- Input changes the visible output predictably.
- Invalid input is handled and explained.
- A reset/restart path is documented.
- Evidence and repository commit time are recorded UTC-first with Tehran equivalent.
- No claim of full runtime, external persistence, or always-on background capture without independent proof.

## Current state
Point 0.0 is the active checkpoint. Prototype source: BUILT IN REPOSITORY. Browser execution: NOT RUN / NOT VERIFIED. Cold-start recovery: NOT RUN. This remains open until execution evidence is recorded.
\n\n## Architecture-zero handoff update\nResume from CURRENT-040 and architecture-zero anchor G6IP-ARCH-ZERO-20261024-001. The governing inherited architecture master is v1.0.4 and GPT-6 living master v1.3.5. Preserve IN-032/OUT-032 and EVT-0140. The prototype remains NOT BUILT until a real artifact is committed and exercised.\n

## CURRENT-061 execution receipt — prototype source committed
- Version: 1.0.2
- Source artifact: [interactive prototype](../../architecture/interactive-prototype/index.html).
- Test instructions: [prototype README](../../architecture/interactive-prototype/README.md).
- [x] Prototype source and manual test contract exist in the repository.
- [x] Source has explicit input validation, visible output, IN/OUT events, checkpoint, JSON import/export and best-effort same-browser persistence.
- [ ] Browser execution against the acceptance steps: NOT RUN / NOT VERIFIED by repository write/read-back.
- [ ] Clean-profile/cold-start recovery: NOT RUN.
- [ ] Real AI-host import, second host, cross-host persistent memory and background execution: OPEN / NOT VERIFIED.
- Decision: NEXT-039 advances from “prototype not built” to “prototype source built; execution and recovery gates open.” It is not closed.
