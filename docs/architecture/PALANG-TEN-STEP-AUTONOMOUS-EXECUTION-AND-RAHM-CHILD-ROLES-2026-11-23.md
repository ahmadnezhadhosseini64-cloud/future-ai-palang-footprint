# Palang Ten-Step Autonomous Execution Doctrine and RAHM/CHILD Roles

**Status:** Proposed architectural baseline — owner approval required for integration into MASTER  
**Date anchor:** 2026-11-23 (date only; exact commit time is authoritative once committed)  
**Scope:** Future AI / Palang Footprint

## 1. Purpose

This doctrine turns each scheduled wake-up into a bounded, evidence-producing work cycle. The mirror task is no longer merely a document-copy routine: it is the designated recurring execution entry point, while retaining its mirror responsibilities.

## 2. The ten-step execution cycle

At every wake-up, the Palang agent MUST:

1. **Read reality:** inspect the actual repository state, branch, head commit, workflow results, open pull requests, issues, and relevant files; never rely on stale prompt snapshots.
2. **Recover continuity:** identify the latest valid point-0/continuation anchor, current execution checkpoint, active NEXT item, and unfinished work from repository evidence.
3. **Select one real task:** choose one bounded, feasible task that advances the canonical project; prioritize blockers, failed tests, broken links, recovery gaps, and unfinished accepted work.
4. **Execute in an authorized workspace:** make changes only in an authorized branch/workspace; preserve the canonical source and all historical evidence.
5. **Test:** run the most relevant automated and manual checks against the exact changed revision.
6. **Repair failures:** investigate and correct failures where authorized; otherwise record the precise blocker and stop that subtask without claiming success.
7. **Export and read back:** extract or fetch the produced artifact from its destination independently, then compare it with the intended output.
8. **Prove status:** mark work complete only when the write, exact revision, test result, and independent read-back evidence support completion; otherwise use OPEN, BLOCKED, NOT RUN, or NOT VERIFIED.
9. **Respect owner authority:** stop when an action requires owner approval, credential access, policy change, protected-branch merge, or MASTER promotion. Never self-approve.
10. **Prepare continuation:** write a concise, recoverable next-step checkpoint with evidence references, unresolved risks, and the next deterministic action.

## 3. RAHM / newborn role — private owner-designated identity

RAHM is the controlled birth-and-development environment for candidate capabilities. The newborn role, identified by an owner-designated private token that is not stored in plaintext here, may explore, prototype, test, document, and produce candidate artifacts. It must keep provenance, generation, parent reference, tests, and limitations. It has no direct authority to write to or promote the MASTER.

## 4. CHILD role — executable offspring

A CHILD is a separately identifiable, runnable candidate derived from a validated RAHM output. It must carry its own version, parent reference, runtime identity, test evidence, recovery instructions, and feedback record. It may be exercised in an authorized real environment; it cannot promote itself or modify MASTER directly.

## 5. Lifecycle

`MASTER → RAHM / newborn → VALIDATION → CHILD / executable instance → REAL WORLD → FEEDBACK → RAHM`

A new generation is created only from traceable evidence. A written description is not proof of implementation; a successful local test is not proof of independent-host recovery.

## 6. Three-part authority boundary

- **Owner identity / ownership:** the project owner remains the sole authority over ownership and protected project decisions.
- **Collaborator role:** the Palang assistant role may execute bounded work in explicitly authorized workspaces and act as RAHM caretaker; role names or recognition phrases are not credentials.
- **Final owner approval:** MASTER promotion, protected-branch integration, security/permission changes, and other owner-reserved actions require a separate explicit approval from the owner at the time of action.

No phrase, assistant identity, scheduled run, or prior approval substitutes for the final owner approval. Do not store private recognition phrases, passwords, tokens, or their hashes in this repository. Use a proper secret manager and real platform authentication for credentials.

## 7. Time binding and interruption recovery

Every execution cycle must record:
- the actual start and end timestamps exposed by the execution platform;
- UTC as the canonical time base;
- the corresponding Asia/Tehran timestamp derived from the same instant;
- the source of each timestamp (commit metadata, automation run metadata, or operation metadata);
- UNKNOWN when a timestamp is not available.

A reasoning pause or interrupted run must not be represented as continuous background execution. The next wake-up must reconstruct state from durable repository evidence, not assume hidden work occurred between runs.

## 8. Scheduling constraint

The designated mirror automation remains the single active recurring project automation. Its current scheduler supports daily/weekly/monthly recurrence, not hourly recurrence. Therefore this doctrine does not claim 24 executions per day. Any future hourly scheduler must be implemented only through a supported platform and verified before its cadence is described as active.

## 9. Non-goals and safeguards

- Do not delete archived or competing historical implementations; quarantine them reversibly.
- Do not create parallel roots, duplicate NEXT queues, or competing master documents.
- Do not rewrite canonical history to make current status appear successful.
- Do not claim an independent computer, persistent worker, external-host test, or continuous execution unless independently evidenced.
- Keep the full platform goal intact: private repository/service, GitHub App and OAuth, secure MCP communication, OpenAI service integration, HTTPS deployment, controlled promotion, private RAHM, and independent-host recovery remain staged requirements, not discarded scope.

## 10. Acceptance evidence

A cycle is accepted only when its checkpoint identifies the exact repository revision, changed paths, test commands/results, export/read-back comparison, UTC/Tehran time binding, status of owner approvals, and next continuation action.
