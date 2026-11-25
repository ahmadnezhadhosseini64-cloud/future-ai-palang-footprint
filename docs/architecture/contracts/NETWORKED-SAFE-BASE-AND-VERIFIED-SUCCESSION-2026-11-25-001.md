# Networked Safe Base and Verified Version Succession

- Stable Contract ID: HAIF-SAFE-BASE-NETWORKED-SUCCESSION-2026-11-25-001
- Parent: POINT-0/GOLDEN (existing canonical root)
- Sole continuation queue: NEXT-051 (unchanged)
- Status on this branch: PROPOSAL / VALIDATION PENDING
- Scope: repository-wide change governance, safe snapshots, PR dependency graph, and verified promotion.
- This contract creates no new POINT-0 root, CURRENT/EVT numbering family, or parallel queue.

## 1. The safe point is an immutable Git object, not a moving label

The safe base for this proposal is the exact main commit:

- Ref observed: main
- Commit SHA: 2c1f9fdc308e34b23be64153e8eec2c30f08a859
- Captured: 2026-11-25 (repository observation; no user-message time inferred)
- Retrieval branch: safety/SAFE-BASE-20261125-2c1f9fd

The commit SHA is the authoritative identity of the snapshot. A branch name is only a movable retrieval pointer and MUST NOT be treated as immutable evidence. Never force-move or rewrite the recorded safe-base commit. Before creating a new safe base, verify that the prior safe-base SHA remains retrievable and that the new candidate descends from the accepted predecessor.

A safe snapshot means recoverable source state. It does not certify that every historical pointer, document, workflow, external service, or open issue inside that snapshot is correct or complete.

## 2. Networked proposal graph

Current implementation PR: [#169](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/pull/169), stacked on parent PR #168. The parent branch head at PR creation was `badae85fc84b2eaa45a23447392fb51fd8231017`; the safe-base ancestor remains `2c1f9fdc308e34b23be64153e8eec2c30f08a859`.

Each PR is a proposal node, not a new source of truth. Every node must record:
- stable PR number and URL;
- exact base branch and base commit SHA;
- exact head branch and head commit SHA;
- parent/dependency PRs and sibling/related PRs;
- changed paths and overlap with other open proposals;
- validation run IDs and the exact SHA each run tested;
- state: PROPOSED, BLOCKED, VALIDATED, ACCEPTED, or REJECTED.

Relationships are explicit:
- DEPENDS_ON: a child proposal cannot be promoted before its parent is accepted.
- RELATED_TO: sibling work that must be reconciled but is not automatically imported.
- CONFLICTS_WITH: overlapping or semantically incompatible changes requiring a deliberate resolution.
- SUPERSEDES: only an owner-approved successor may supersede an earlier proposal.

Current observed proposal relationships:
- PR #168 is the parent proposal for the two-stage owner-selected host enrollment. This implementation branch is stacked on its branch so the shared Reference Index update is not independently overwritten.
- PR #167 is a related security-governance proposal. It remains separate and is not silently included in this branch.
- PR #145 is an older divergent proposal: compared with current main it is 341 commits ahead and 46 behind, with a merge base older than the current main. It is quarantined from automatic stacking or promotion until a complete source and semantic reconciliation is performed.
- No PR is merged, closed, rebased, or retargeted by this contract alone.

## 3. Safe succession lifecycle

`SAFE-N → CHANGE-NETWORK → INTEGRATION-GATE → SAFE-CANDIDATE-(N+1) → VERIFIED-PROMOTION → SAFE-(N+1)`

1. Preserve the last accepted safe commit.
2. Build proposals from an explicitly recorded base; declare dependencies and path overlap.
3. Validate each candidate at its exact head SHA.
4. Reject stale evidence when the PR head changes after a successful run.
5. Reconcile text, file paths, references, semantics, security boundaries, and dependency order.
6. Promote only after required checks, read-back, and owner approval are evidenced.
7. Record the new accepted commit as the next safe base; preserve the previous safe base permanently.
8. If any gate fails, leave the prior safe base untouched and mark the candidate BLOCKED or REJECTED.

## 4. Mandatory promotion gates

A candidate is eligible for promotion only when all applicable conditions are true:
- exact base SHA and exact head SHA are recorded;
- all declared parent dependencies are accepted/merged;
- all required CI checks pass on the exact current head SHA;
- changed files and cross-document links are read back;
- no unresolved text, semantic, identity, permission, or provenance conflict remains;
- the candidate preserves the single POINT-0/GOLDEN root and NEXT-051 queue;
- the owner has approved the exact candidate;
- GitHub's actual ruleset permits the operation without bypassing or weakening protection.

A passing test suite is necessary but not sufficient. A passing test on an earlier head does not validate a later head. A mergeability result is not a substitute for architecture review.

## 5. Failure and recovery

- A failed or stale candidate never replaces the safe base.
- Recovery means checking out the exact prior safe-base SHA, not guessing a branch name or reverting unrelated accepted work.
- Preserve failed workflow runs and their logs as evidence; never relabel a failure as success.
- Do not force-push, rewrite the safe-base commit, or bypass branch protection.
- If the main branch advances while a candidate is being validated, rebase/retarget only through an explicit reconciliation step and rerun all required checks on the resulting exact head.

## 6. Current baseline discrepancy — OPEN

At the captured main state, two current-pointer representations disagree:
- README.md and the published POINT-0/GOLDEN snapshot identify CURRENT-144.
- The living mother and Integration Queue identify CURRENT-145.

This discrepancy is preserved as an OPEN reconciliation item. This safe-base record does not choose a winner, fabricate a missing link, or claim that the architecture pointers are fully synchronized. The next promotion must resolve it from canonical file existence, commit ancestry, event/time-binding evidence, and exact read-back.

## 7. Acceptance tests

A stacked proposal's Git base may be the exact head of an accepted parent PR rather than the safe-base commit itself. The safe-base ancestor and each dependency must still be explicitly recorded and accepted. The accompanying unit tests validate the policy model:
- safe-base identity requires a full immutable commit SHA;
- a candidate cannot promote from a stale base;
- every required gate must pass;
- failed validation preserves the previous safe base;
- dependencies must be accepted before child promotion.

The dedicated GitHub Actions workflow runs these tests on pull requests and manual dispatch. Repository policy tests do not prove external-host recovery, credential isolation, private RAHM provisioning, or background automation.

## 8. Authority and status boundaries

The owner retains final authority. A connected assistant may prepare branches, PRs, tests, evidence, and read-backs only within actual connector permissions. It must not bypass a ruleset, impersonate an independent reviewer, or treat an owner's textual declaration as technical authentication.

This proposal remains PROPOSAL until exact-head tests, read-back, dependency reconciliation, and owner-controlled acceptance are complete. Main is unchanged by this proposal branch.
