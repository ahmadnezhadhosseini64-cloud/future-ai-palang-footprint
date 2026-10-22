# آزمون بازیابی مستقل از سند مرجع — رصدخانهٔ رفتار تعامل

## شناسنامه
- Test ID: BEHAVIOR-OBSERVATORY-RECOVERY-TEST-2026-10-22-001
- Event ID: EVT-0035
- Stable ID: PALANG-STANDALONE-REFERENCE-RECOVERY-TEST-2026-10-22-001
- Production ID: PSRRT-HAIF-2026-10-22-001
- Version: 1.0.0
- Test type: standalone-reference recovery / بازیابی از سند مستقل
- Reference under test: `docs/architecture/BEHAVIOR-OBSERVATORY/README.md`
- Anchor: `PALANG-BEHAVIOR-OBSERVATION-AND-RECOVERY-TEST-2026-10-22-001`
- Status after execution: PASS (10/10 criteria; one initial evaluator false-negative was corrected by manual inspection of the retrieved standalone reference)
- Reference initial repository commit: 4cc65aa3c1503082a48dfd67ac3686469bb17d7e at 2026-10-22T04:07:36Z = 2026-10-22 07:37:36 Asia/Tehran (UTC+03:30).
- Test execution timestamp: exact tool execution time was not exposed; UNKNOWN / UNVERIFIED.
- Read-back time: UNKNOWN if tool does not expose it.
- Time rule: UTC canonical; Tehran equivalent derived from the same instant, Asia/Tehran UTC+03:30 on 2026-10-22.

## 1. Purpose
Prove or disprove whether the independent reference alone provides enough information to recover the project's behavior-observation goal, operating rules, architecture placement, identifiers, verification status, open gaps and next actions without relying on prior chat context.

## 2. Procedure
1. Retrieve only the reference under test by its exact repository path.
2. Do not use the parent rule, interaction trace, previous conversation, or this test's own expected-result section to fill missing reference content.
3. Check each criterion below using only the retrieved reference.
4. Mark PASS only when the required fact is explicitly present and internally consistent; otherwise mark FAIL or PARTIAL and cite the missing item.
5. Record the outcome and limitations in this separate test record.
6. After recording the result, retrieve this test record and the reference again; compare expected identifiers and links.
7. External destinations remain unverified unless separately tested.

## 3. Acceptance criteria
- C1 Goal and scope of behavior observation recoverable.
- C2 Clear separation of observable human behavior, observable AI actions, and interpretations.
- C3 Explicit rule not to claim or store private chain-of-thought; operational decision records are used instead.
- C4 Architecture placement and promotion/owner-approval gates recoverable.
- C5 Stable IDs, production IDs, version, paths and related rules recoverable.
- C6 Per-interaction schema and lifecycle recoverable.
- C7 Timestamp policy and distinction between event/commit/read-back/verification times recoverable.
- C8 Destination-by-destination persistence limitations recoverable.
- C9 Open work and exact next actions recoverable.
- C10 Independent recovery can proceed without chat-only facts.

## 4. Execution result — actual independent retrieval
- Reference retrieved by exact path, with no parent rule/trace or prior conversation used to fill its content: docs/architecture/BEHAVIOR-OBSERVATORY/README.md.
- Read-back blob SHA: 363dbc6ed14118c5ae7cc5b14903cb644edf37d3.
- Retrieved length: 5,675 characters.
- C1 Goal and scope recoverable: PASS.
- C2 Human/AI observable actions and interpretations separated: PASS.
- C3 Private chain-of-thought not claimed; operational decision records specified: PASS.
- C4 Architecture placement and owner-approval promotion gate: PASS after correcting an evaluator false-negative. The retrieved text explicitly states: HAIF → Governance & Interaction → Behavior Observation → Evidence/Patterns → Controlled Proposal → Validation/Hammer → Owner Approval → Master integration. The first automated check looked for the capitalized literal “Architecture” and returned FAIL; this was a check-pattern defect, not missing reference content.
- C5 IDs/version/path/related rule recoverable: PASS.
- C6 interaction schema and lifecycle recoverable: PASS.
- C7 UTC canonical rule and distinct action/commit/read-back/verification times recoverable: PASS.
- C8 repository versus Buffer/Library/Persistent Memory/Dropbox limitations recoverable: PASS.
- C9 open work and next actions recoverable: PASS.
- C10 sufficient standalone information to reconstruct the work without chat-only facts: PASS.
- Overall result: PASS — 10/10 criteria on the retrieved reference, with the evaluator correction documented above.
- Boundary: this is a content-based standalone recovery test, not a destructive repository-loss test, and not proof of persistence in external destinations.
- Evidence of initial reference commit: 4cc65aa3c1503082a48dfd67ac3686469bb17d7e, commit time 2026-10-22T04:07:36Z = 2026-10-22 07:37:36 Asia/Tehran.
- Test file initial commit: 45289488afc6ad65e476e509a58ae2ed14a09ca6, commit time 2026-10-22T04:07:38Z = 2026-10-22 07:37:38 Asia/Tehran.
- Event EVT-0034 initial commit: 39a8e339c17f0c09dc9c326fb0b1131e171b4020, commit time 2026-10-22T04:07:41Z = 2026-10-22 07:37:41 Asia/Tehran.
- Exact read-back timestamp and test execution timestamp: not exposed by tool; UNKNOWN / UNVERIFIED.
- Failure handling: any future missing criterion remains OPEN and is added to the integration queue; criteria must not be changed to manufacture a pass.

## 5. Decision-record boundary
This record documents the test objective, method, evidence, rule applied, observed result, limitations and correction path. It does not attempt to reproduce private chain-of-thought. Hidden internal reasoning is not available as a factual transcript and must not be invented. The project's behavior-study goal is met through observable action traces and concise, evidence-grounded decision records.

## 6. Recovery command
"Open the standalone Behavior Observatory reference. Reconstruct the goal, rules, architecture placement, observation schema, verification gates, current evidence state and next actions using that file alone. Record each criterion as PASS/PARTIAL/FAIL with evidence, then resume unresolved work without asserting unverified storage."
