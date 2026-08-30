# Primary Path Lock & Branch Containment Protocol

- ID: PPLBC-2026-08-30-001
- Status: ACTIVE / LIVE / PERMANENT OPERATIONAL RULE
- Project: Future AI / Palang Footprint

## Purpose
Prevent a blocker, defect, access failure, or newly discovered gap from silently replacing the primary objective during a long-running task.

## Mandatory State Model
PRIMARY GOAL → CURRENT STEP → BLOCKER → SUB-ISSUE → RETURN POINT → FINAL GATE

## Rules
1. The Primary Goal is locked for the duration of the task unless an explicit goal-change event is recorded.
2. A newly discovered issue is classified as BLOCKER or SUB-ISSUE; it does not become the Primary Goal automatically.
3. Before pursuing a branch, record which exact primary step it blocks or supports and its mandatory Return Point.
4. Every branch must retain a Parent ID linking it to the Primary Task.
5. After branch resolution, the workflow must return to the recorded Primary Current Step/Return Point.
6. No Goal Replacement: no branch may replace the Primary Goal without explicit recorded authorization and state transition.
7. Every assistant action/report must be attributable to one state: ADVANCE, BLOCKER, SUB-ISSUE, RECOVERY, RETURN, or FINALIZATION.
8. A solved blocker is not completion of the Primary Goal.
9. Checkpoint 0.0 must preserve Primary Goal, Exact Current Step, unresolved blockers, branch states, and Return Path.
10. On recovery, retrieve the Primary Task State first, then branch states; never let a branch become the recovery starting point unless explicitly recorded.
11. Final Closure applies to the Primary Goal and its Final Gate, not merely to an auxiliary branch.
12. If a capability/access limitation prevents progress, record it as a blocker inside the same task and preserve the continuation path; do not create an unrelated project unless explicitly authorized.

## Operational Gate
Before following any new branch, answer internally:
- What is the Primary Goal?
- Which exact step is blocked?
- Is this a blocker or a sub-issue?
- What is the Return Point?
- What evidence will prove return to the primary path?

If these cannot be identified, do not branch; preserve state and return to the primary task.

## Integration
This protocol integrates with Continuation Path Preservation, Checkpoint 0.0, Pending/Recovery, Final Registration Closure Gate, and Evidence/Verification rules.

## Core Principle
A branch may grow, but it may never silently consume the trunk.
