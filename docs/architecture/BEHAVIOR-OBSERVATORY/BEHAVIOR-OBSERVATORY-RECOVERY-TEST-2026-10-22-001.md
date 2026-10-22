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
- Status before execution: PLANNED
- Repository registration time: to be filled from actual commit metadata; never substitute message time.
- Test execution time: UNKNOWN until a timestamp is supplied by an execution log; do not invent.
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

## 4. Execution result
- Reference retrieval performed: pending actual retrieval.
- Criterion results: pending.
- Overall: NOT RUN.
- Evidence: pending repository fetch result and content checks.
- Failure handling: any missing criterion remains OPEN and is added to the integration queue; do not alter the expected criteria merely to manufacture a pass.

## 5. Decision-record boundary
This record documents the test objective, method, evidence, rule applied, observed result, limitations and correction path. It does not attempt to reproduce private chain-of-thought. Hidden internal reasoning is not available as a factual transcript and must not be invented. The project's behavior-study goal is met through observable action traces and concise, evidence-grounded decision records.

## 6. Recovery command
"Open the standalone Behavior Observatory reference. Reconstruct the goal, rules, architecture placement, observation schema, verification gates, current evidence state and next actions using that file alone. Record each criterion as PASS/PARTIAL/FAIL with evidence, then resume unresolved work without asserting unverified storage."
