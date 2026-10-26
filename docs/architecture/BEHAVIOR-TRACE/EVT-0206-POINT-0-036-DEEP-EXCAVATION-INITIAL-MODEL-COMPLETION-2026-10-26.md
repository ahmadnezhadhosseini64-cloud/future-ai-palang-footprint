# EVT-0206 — Point 0/036 Deep Excavation and Initial Model Completion

- Stable ID: HAIF-EVT-0206-POINT-0-036-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION-20261026
- Production ID: HAIF-EVT0206-20261026
- Version: 1.0.0
- Status: REGISTERED / ACTIVE / LIVING / OPEN
- Root: [POINT-0/036](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-036-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md)
- IN: [IN-072](../../0.0/anchors/PALANG-0.0-IN-20261026-072-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md)
- OUT: [OUT-071](../../0.0/anchors/PALANG-0.0-OUT-20261026-071-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md)
- Current: [CURRENT-084](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-084-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md)
- Active queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Event
The user renewed the instruction to make this turn a Point 0, continue the remaining work as 0.0 checkpoints, excavate the live repository, and complete the initial model. The accepted prior finding is that declared identifier metadata must be distinguished from body references, and short event numbers cannot by themselves establish identity or parentage.

## Behavior lesson
A prior workflow risked treating reference mentions as declarations and using a global short-ID preference for source-specific parent edges. The corrective architecture is: bounded metadata-header extraction; source-path-specific parent overrides validated against actual candidates; no speculative parent selection; and explicit unresolved/ambiguous states. Preserve source files, full Stable IDs, Production IDs, hashes, and historical aliases.

## Proof boundary
Repository code, repository CI, and a portable package are not proof that an independent interactive GPT host has imported, restarted, persisted, and round-tripped the project. Those checks remain separate, OPEN gates until direct destination evidence is captured.