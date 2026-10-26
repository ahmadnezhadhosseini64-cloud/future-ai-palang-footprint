# CURRENT-079 — Master–Rahm–Child bridge and initial-model validation

- Stable ID: HAIF-CURRENT-079-MASTER-RAHM-CHILD-BRIDGE-20261026
- Production ID: HAIF-C079
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EXECUTION REQUIRED
- Current root: [POINT-0/032](./GPT6-RAHM-USER-POINT-0-20261026-032-MASTER-RAHM-CHILD-INITIAL-MODEL-BRIDGE.md)
- Input/output: [IN-067](./PALANG-0.0-IN-20261026-067-MASTER-RAHM-CHILD-BRIDGE.md) → [OUT-066](./PALANG-0.0-OUT-20261026-066-MASTER-RAHM-CHILD-BRIDGE.md)
- Event: [EVT-0201](../../architecture/BEHAVIOR-TRACE/EVT-0201-MASTER-RAHM-CHILD-BRIDGE-AND-INITIAL-MODEL-VALIDATION-2026-10-26.md)
- Architecture contract: [Master–Rahm–Child cross-validation contract](../../architecture/MASTER-RAHM-CHILD/MASTER-RAHM-CHILD-CROSS-VALIDATION-CONTRACT-2026-10-26.md)
- Canonical master: [Current continuation master](../../reference/REFERENCE-DOCUMENTS/CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md)
- Initial-model mother: [Initial-model living mother](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Previous checkpoint: CURRENT-078 (preserved).

## Confirmed repository work
- Registered POINT-0/032, IN-067, OUT-066, EVT-0201 and this checkpoint.
- Added a dedicated Master–Rahm–Child cross-validation contract with test cases for interactive-project cold start, IN/OUT symmetry, provenance, reversible gap covers, candidate isolation, promotion gating, failure recovery and export/import.
- The original project is explicitly the canonical MASTER; the new initial-model project is the subordinate RAHM; validated proposals become CHILD CANDIDATES until explicit Master acceptance.
- No historic graph conflict or external-runtime gap was closed by this registration.

## Open gates
1. [x] Canonical index, integration queue, 0.0 registry and both living-mother surfaces were fetched from main and their bridge references were confirmed in the inspected snapshot; this closes only the repository-link/read-back subtask, not exact-head CI or manifest conformance.
2. Run link checks and current-head repository audit on the exact final SHA.
3. Run portable RAHM conformance and reconcile exact package digests on that same SHA.
4. Execute the validation protocol in the actual interactive project environment and capture receipts; until then its tests are NOT RUN.
5. Independently test clean-host import, persistence after restart, background/idle execution and any external storage.
6. Continue NEXT-051 graph/source/parent/collision triage; keep CURRENT-065/CURRENT-066 and EVT-0195 conflicts open.
7. Do not create NEXT-052.

## Resume action
Start by fetching this checkpoint, the bridge contract, the initial-model mother and NEXT-051. Run a focused link/read-back check; then trigger or inspect exact-HEAD CI and record the real result. After repository verification, use the test protocol in the interactive project environment. A test result without a destination receipt remains NOT RUN / NOT VERIFIED.


## Direct interactive-project execution entry
- Runbook: [INTERACTIVE-PROJECT-VALIDATION-RUNBOOK](../../architecture/MASTER-RAHM-CHILD/INTERACTIVE-PROJECT-VALIDATION-RUNBOOK.md)
- This is a ready-to-paste test protocol. Actual IPV-01 through IPV-10 results remain NOT RUN / NOT VERIFIED until the interactive destination returns direct receipts. No Child promotion has occurred.

## Canonical repository time
- [TIME-BINDING-POINT-0-032 / EVT-0201](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-POINT-0-032-EVT-0201-2026-10-26.md) contains the actual commit-time ledger for this chain; use UTC as canonical and Tehran as a derived display.
- Portable export manifest currently reports version 1.8.7; exact-final-SHA conformance and exact digest reconciliation are still OPEN. A spot-check found manifest Git blob SHA entries that do not match the fetched current blobs for the cross-validation contract/time-binding artifacts, so do not treat the package as digest-verified until a fresh conformance run reconciles them.

## Repository surface read-back — 2026-10-26
- 0.0 registry blob SHA: `0116cf5219f83c666add93e4d515a7de9079836c`.
- Canonical reference index blob SHA: `8066b70a143082ed55d5ef60ae2baedaa08f6470`.
- Main integration queue blob SHA: `fa98d0b99c61b0817a315d93fce1c72202101333`.
- Initial-model mother blob SHA: `ac13b595de485f680f0e7bb83060137a309f9421`.
- Canonical continuation mother blob SHA: `f557ec4533aeb64c3134ca8639fcc06a577f2e08`.
- These are content/blob identifiers from read-back, not commit timestamps or proof of exact-head workflow success.

## User-supplied prior-output baseline incorporated
- MASTER is the final authority for durable rules, interaction/behavior history, accepted architecture, provenance and evidence.
- RAHM is the existing initial-model package plus the intended interactive environment; extend the existing package rather than creating a parallel folder.
- CHILD remains a versioned candidate until defined tests, evidence/limitations and explicit MASTER review support acceptance.
- Repository CI and actual interactive-host tests are distinct evidence classes. The latter remains NOT RUN / NOT VERIFIED without direct destination receipts.
- Preserve failures, rejected candidates and all open graph/source/parent gaps. Covers remain reversible; no gap is closed by this architecture decision.
- Next action remains within NEXT-051: reconcile exact-current-main artifacts and package digests, run repository tests against the final SHA, then execute the interactive runbook in the actual destination and capture receipts.
