# چشم پلنگ شکارچی — مولد آزمون از ورودی/خروجی و دروازهٔ رشد معماری

- Stable ID: PALANG-BEHAVIOR-HUNTER-TEST-GENERATION-AND-GROWTH-GATE-2026-10-23-001
- Production ID: BHTGG-HAIF-2026-10-23-001
- Version: 1.0.0
- Owner: احمد پلنگ / Ahmad Nezhadhosseini
- Status: ACTIVE / LIVING / IMPLEMENTATION-IN-PROGRESS
- Parent: HUMAN-AI-INTERACTION-BEHAVIOR-OBSERVATORY-2026-10-22-001
- Related event: EVT-0115
- Related plan: VERIFIABLE-TEST-PLAN-FROM-EVT-0115-2026-10-23
- Canonical rule: UTC is authoritative for repository commits; Tehran is derived from the same UTC instant.
- Important boundary: a repository workflow can test structured interaction records committed to this repository. It does NOT automatically capture every live ChatGPT message unless a supported host adapter explicitly exports each permitted input/output pair.

## 1. Purpose

The Behavior Hunter / چشم پلنگ شکارچی turns observable human-AI interaction records into reproducible candidate tests. It must not stop at documentation: records enter a deterministic generator, generated tests run in an independent CI workflow, evidence is preserved, and only evidence-backed passing outcomes may become growth proposals.

## 2. Pipeline

CAPTURE IN/OUT → ANCHOR → NORMALIZE → GENERATE CANDIDATE TESTS → VALIDATE TEST DEFINITION → EXECUTE → COLLECT EVIDENCE → VERIFY RESULT → CLASSIFY → CHILD / RAHM PROPOSAL → OWNER REVIEW → MASTER PROMOTION.

- IN / ورودی: exact user request or permitted normalized representation, constraints and expected behavior.
- OUT / خروجی: assistant answer, claimed actions, tool outcomes, evidence references and explicit limitations.
- Candidate test: a test proposal generated from observable record fields. Candidate creation is not a pass.
- Independent verification: run output, exit status, generated report, source record and commit must be inspectable.
- Growth proposal: a child/branch proposal only; no automatic mutation or promotion of MASTER.

## 3. Test families derived from observable records

1. Input/output completeness: both IN and OUT exist, event IDs and source references are present.
2. Claim-to-evidence: claims such as WRITE, READ-BACK, VERIFIED, PASS or ACTIVE are checked against explicit evidence fields; unsupported success claims fail the gate.
3. Destination isolation: Repository, Library, Buffer, Persistent Memory, Dropbox and external recovery are distinct states.
4. Time provenance: UTC repository commit is canonical; Tehran is a conversion; unknown execution time remains UNKNOWN.
5. Continuity/recovery: resume pointer, parent event, next action and unresolved blockers are present.
6. Preservation: old 0.0 anchors and prior failures are retained; new records append rather than silently overwrite.
7. User correction / failure recovery: corrections and failed attempts remain visible and create regression tests.
8. Semantic mirror reconciliation: Stable ID, Version, Next Action and Destination Statuses are compared independently of total character count.

## 4. Minimum interaction record contract

Each JSONL record should contain:
- event_id, stable_id, version
- input (user IN) and output (assistant OUT)
- expected_invariants: list of machine-checkable conditions
- claims: list of claims made in OUT
- evidence: list of evidence references with type and locator
- destinations: explicit per-destination states
- parent_anchor, resume_pointer, next_action
- commit_sha and repository_commit_utc when registered
- execution_time_utc only when actually exposed by a reliable source

Do not include hidden chain-of-thought. Store a concise operational decision record, evidence, result, limitation and next action. Minimize unrelated personal or sensitive data.

## 5. Decision rules

- FAIL: a required field is missing, an explicit invariant fails, or a success claim lacks required evidence.
- BLOCKED: required source or destination cannot be accessed; do not convert it into PASS.
- NOT RUN: no execution evidence exists.
- PASS: only the exact machine-checkable test passed and its output is preserved.
- PASS does not automatically mean architecture promotion. Passing results feed a versioned CHILD / RAHM proposal for owner review.
- A successful test is not repeated unless source, implementation, deployment, dependency, evidence or risk changes.

## 6. Current implementation boundary

The repository-side generator and CI workflow validate structured interaction-pair records and create a machine-readable candidate-test manifest. This is an initial executable layer, not proof that a live host adapter is already capturing every conversation. Full live capture remains OPEN until a real adapter writes records, a read-back test retrieves them, and a fresh-session recovery test succeeds.

## 7. Required acceptance evidence

- Test generator unit tests pass in an actual CI run.
- The workflow produces an artifact/report listing generated candidate tests and their source event IDs.
- A deliberately incomplete fixture is rejected; a valid fixture yields tests without claiming they passed.
- A success claim with no evidence is blocked.
- Output is independently retrievable by workflow run/artifact or committed report.
- The master reference and integration queue point to the implementation and record the remaining host-adapter gap.

## 8. Growth path

OBSERVATION → CANDIDATE TEST → INDEPENDENT RUN → EVIDENCE REVIEW → CHILD PROPOSAL → OWNER APPROVAL → MASTER INTEGRATION.

The generator must never promote a behavioral pattern directly into MASTER. It may suggest what should grow; the evidence gate and owner decide what is allowed to grow.
