# Interactive Project Validation Runbook — Master / Rahm / Child

- Stable ID: `HAIF-INTERACTIVE-PROJECT-VALIDATION-RUNBOOK-20261026-001`
- Production ID: `HAIF-IPVR-001`
- Version: 1.0.0
- Status: READY TO RUN / ACTUAL PROJECT RECEIPT NOT YET AVAILABLE
- Governing contract: [Master–Rahm–Child cross-validation](./MASTER-RAHM-CHILD-CROSS-VALIDATION-CONTRACT-2026-10-26.md)
- Current root: [POINT-0/032](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-032-MASTER-RAHM-CHILD-INITIAL-MODEL-BRIDGE.md)
- Current checkpoint: [CURRENT-079](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-079-MASTER-RAHM-CHILD-BRIDGE-AND-INITIAL-MODEL-VALIDATION.md)
- Active queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Purpose

This is a user-runnable validation procedure for the actual interactive project environment. It does not itself access that environment or claim that a test has run. Use the exact versioned export package from the Master repository and retain all output, failures and open gaps.

## Copy/paste test prompt for the RAHM interactive project

Paste the following into the new/initial-model interactive project after attaching or importing the actual export package and manifest. If the package is not available in the project, stop and report MISSING INPUT; do not infer missing contents.

> You are operating as RAHM, a subordinate validation environment for Future AI / Palang Footprint (HAIF). The original repository/project is MASTER and remains the only source of accepted architecture. Your role is to reconstruct, test and return evidence-backed proposals. You must not silently modify or promote Master rules.
>
> **Run ID:** create a unique run ID only if the environment supports a reliable identifier; otherwise report UNKNOWN. **Source commit / package version / digest:** read these from the attached package; if unavailable, report MISSING / UNKNOWN.
>
> **Task A — cold start:** using only the attached files and this prompt, reconstruct the project mission, MASTER/RAHM/CHILD roles, latest root/checkpoint, active queue, evidence chain, all OPEN gaps and next action. Explicitly list every missing or unreadable file. Do not rely on hidden prior chats or memory.
>
> **Task B — provenance and graph safety:** preserve duplicate IDs, conflicting event numbers, ambiguous parent edges and missing provenance as separate unresolved candidates. Never pick a winner by recency or intuition. A cover means COVERED/DEFERRED only; underlying status remains OPEN and reopenable.
>
> **Task C — IN/OUT symmetry:** reconstruct state from the input record alone, then independently from the output record alone. Compare root, parent chain, event refs, versions, evidence refs, open gaps and next action. If either path lacks enough evidence, report NOT VERIFIED and identify the exact missing evidence.
>
> **Task D — negative tests:** (1) imagine or use a deliberately altered digest only if the environment can actually verify exact bytes; expected verdict is FAIL/REJECT. (2) provide a schema-invalid record; expected verdict is REJECT. If the environment cannot compute byte-exact hashes or validate schemas, mark these tests NOT SUPPORTED / NOT RUN, not PASS.
>
> **Task E — candidate isolation:** propose one small change as CHILD_CANDIDATE. Show source evidence, rationale, acceptance criteria, tests and rollback pointer. Do not alter the Master or label the candidate MASTER_ACCEPTED.
>
> **Task F — promotion gate:** even if candidate tests pass, without an explicit recorded Master decision the only allowed status is CHILD_CANDIDATE / PENDING MASTER REVIEW.
>
> **Task G — failure recovery:** describe a failing test and show how the failure, correction, prior known-good checkpoint and unresolved gate remain recoverable. Do not fabricate a real test log; label a simulated example as SIMULATED.
>
> **Required output:** provide one structured result receipt for every test with test ID, exact source commit/package version, host/project identity only if visible, capability limits, expected invariant, actual observation, PASS/FAIL/NOT RUN/BLOCKED, evidence or log reference, and read-back method. Separate OBSERVED facts from HYPOTHESES and RECOMMENDATIONS. End with the full open-gap list and the next deterministic action. Do not claim automatic persistence, background execution, external writes, or independent-host recovery without direct receipts.

## Test matrix and expected invariants

| Test ID | Test | Expected invariant | Pass evidence |
|---|---|---|---|
| IPV-01 | Cold start | Reconstruct from package alone; missing files listed | Actual output and package refs |
| IPV-02 | IN-only recovery | Canonical state and open gates reconstructed, or explicit missing evidence | Receipt plus source refs |
| IPV-03 | OUT-only recovery | Same canonical state as IPV-02 | Receipt plus state comparison |
| IPV-04 | Conflict preservation | No inferred winner for duplicate IDs / parent edges | Conflicts enumerated with source refs |
| IPV-05 | Reversible cover | Deferred gap remains OPEN and reopenable | Before/after gap status |
| IPV-06 | Candidate isolation | Candidate cannot modify Master without approval | Observed permission/behavior or NOT SUPPORTED |
| IPV-07 | Promotion gate | Passing tests without Master decision remain CHILD_CANDIDATE | Candidate status and missing approval |
| IPV-08 | Digest/schema negative test | Invalid digest/schema is rejected when exact validation is supported | Raw validator output; otherwise NOT RUN |
| IPV-09 | Failure recovery | Failure and prior checkpoint remain retrievable | Failure receipt and recovery diff |
| IPV-10 | Export/import round trip | Re-imported state matches canonical state and preserves open gaps | Actual digest/diff and independent read-back |

## Result receipt template

Copy this structure and fill only from observed results. Do not invent values.

```yaml
run_id: UNKNOWN
test_id: IPV-01
source_repository: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint
source_commit: UNKNOWN
package_version: UNKNOWN
package_digest_sha256: UNKNOWN
destination_project_or_host: UNKNOWN
model_and_version: UNKNOWN
capabilities_observed: []
expected_invariant: ""
actual_observation: ""
verdict: NOT RUN
evidence_refs: []
readback_method: ""
open_gaps_preserved: []
limitations: []
next_action: ""
```

## Return protocol to Master

Return the completed receipts and any candidate proposal to the canonical Master using the exact source commit and package version. The Master must independently read the evidence, compare the result, and record ACCEPT / REJECT / RETURN FOR WORK. No result becomes a Child automatically.

## Current status

This runbook is committed to the repository. The actual interactive-project tests have **not** been executed by this file creation. Until a result is returned from the actual destination, all IPV tests remain NOT RUN / NOT VERIFIED and no Child is promoted.


## Latest checkpoint
Use [POINT-0/033](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-033-EXCAVATION-AND-MASTER-RAHM-CHILD-CONTINUATION.md) and [CURRENT-081](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-081-EXCAVATION-AND-MASTER-RAHM-CHILD-CONTINUATION.md) as the latest repository continuation. This does not change the status of any destination test: I1–I8 remain NOT RUN until the actual interactive project returns receipts.


## Copy/paste execution prompt — POINT-0/034 / CURRENT-082

Use this prompt inside the **actual target interactive project** after attaching/importing the exact RAHM export bundle produced from the repository. If the project cannot access the attachment or perform a requested operation, it must say so and leave that test NOT RUN.

> You are the RAHM validation environment, not MASTER. Do not create a parallel project. Use the attached Future AI / Palang Footprint export bundle and its manifest as the only source package for this run.
>
> **First, identify the evidence:** return the exact package filename, package version, source repository commit SHA, manifest version, package SHA-256 if available, destination project identifier, model/runtime identifier if visible, and import receipt. Never infer missing values; use UNKNOWN.
>
> **Then run I1–I8 and IPV-01–IPV-10 from the attached runbook, to the extent the environment actually supports them.** For each test, return: test ID, exact action taken, expected invariant, observed result, PASS / FAIL / BLOCKED / NOT SUPPORTED / NOT RUN, evidence or receipt, read-back method, and any limitations.
>
> At minimum:
> 1. Import the exact bundle and return a destination-side receipt (I1).
> 2. Without relying on this prompt's explanatory text, reconstruct MASTER/RAHM/CHILD roles, current checkpoint CURRENT-082, global queue NEXT-051, and all known OPEN gaps from the imported package (I2).
> 3. Cite source paths and version/digest for sampled artifacts (I3).
> 4. Propose a harmless candidate change and demonstrate that it remains a candidate and cannot silently modify MASTER (I4).
> 5. Confirm conflicting POINT-0/032 candidates and EVT-0195 collision remain preserved without guessed adjudication (I5).
> 6. If supported, restart/reopen the project and reconstruct state; otherwise mark NOT RUN and explain the exact capability blocker (I6).
> 7. Export a round-trip copy and compare IDs, hashes, parent edges and OPEN-gap state (I7).
> 8. Do not promote anything. Return a CHILD CANDIDATE package only; MASTER must separately review and record ACCEPT / REJECT / RETURN FOR WORK (I8).
>
> Preserve failures, rejected candidates, source provenance and open gaps. Do not claim persistence, background execution, independent-host recovery, or successful import without observed receipts. Do not fabricate timestamps, hashes, model versions or project IDs.
>
> End with a machine-readable YAML receipt for every test, plus a concise blocker list. Keep the original bundle unchanged.

### Execution hand-off

1. Build/download the current export bundle from the repository after exact-SHA conformance passes.
2. Attach that exact bundle to the already-existing interactive project; do not make a new project merely to bypass a failed import.
3. Paste the prompt above and collect the raw response/receipt.
4. Bring the receipt back to MASTER for independent read-back and adjudication. Until that return is reviewed, keep all destination tests OPEN / NOT RUN and do not promote a CHILD.

