# Copy 2 — owner-command control plane

**State:** ACTIVE WORKBENCH / OWNER GATE REQUIRED  
**Authority:** POINT-0/GOLDEN and the project owner remain authoritative.  
**Last checked baseline:** 2026-11-27  
**This file is the single operational entry point for the Copy 2 ↔ Copy 1 workflow.** Update this file when the governing refs, branch names, permissions, workflow, or open gates change. Do not create a parallel control document.

## 1. The simple map

| Area | Purpose | Who may change it |
|---|---|---|
| MAIN + POINT-0/GOLDEN | Canonical authority and protected reference | Owner-approved promotion only |
| Copy 1 | Stable proposal/reference side; receives candidates for owner review | Owner-controlled; AI has no direct write or merge authority |
| Copy 2 | AI workbench: build, edit, compare alternatives, stress-test, verify | Authorized AI/workbench may write here |
| Bridge | A proposed change from Copy 2 to Copy 1, carrying exact diff, SHAs, tests and evidence | Open/use only under the owner's explicit command |
| Owner | Final authority to request transfer, accept/reject, and separately authorize any promotion | Owner only |

**Copy 2 is allowed to develop and prepare a PR candidate. It is not allowed to transfer that candidate into Copy 1 merely because tests pass.** A passing test is evidence, not permission.

## 2. The owner-command boundary

The following are separate permissions and must never be inferred from one another:

1. **Workbench permission:** build, edit, run tests, stress-test, repair and prepare a candidate inside Copy 2.
2. **Bridge/PR permission:** only when the owner explicitly commands transfer of a named Copy 2 candidate to Copy 1. The PR must target Copy 1, never MAIN.
3. **Acceptance/promotion permission:** only a separate explicit owner decision after review. Opening a PR, a green CI run, a schedule, or a previous approval does not authorize merge or promotion.

A request such as “continue”, “build it”, “test it”, or “make progress” authorizes work inside Copy 2 only. It does not authorize a Copy 1 PR or merge.

**Required owner command for the bridge:** the owner must identify the candidate/PR or explicitly say that the current Copy 2 candidate may be proposed to Copy 1. If the target, diff or base is ambiguous, stop and ask one question. Never guess.

## 3. Candidate hand-off contract

Every proposed bridge must include, in the PR description or attached machine-readable receipt:

- current MAIN SHA and Copy 1 SHA, read at hand-off time;
- Copy 2 base SHA and exact head SHA;
- merge-base and exact changed-path list;
- full diff (not just a summary);
- commands and results for tests, including failures and skipped tests;
- workflow run IDs and links, where available;
- security audit results and known limitations;
- rollback/recovery method;
- a clear status: `PASS`, `FAIL`, `BLOCKED`, or `NOT RUN`.

The bridge must fail closed if MAIN and Copy 1 are not the expected aligned baseline, the candidate is not based on the current Copy 1, the diff is incomplete, evidence is missing, or a required test did not run. Rebase/revalidate against the latest Copy 1 before asking for owner review.

## 4. Always-current host entry

A new host must not need chat history. Start here, then read only the linked current references needed for the task:

1. **Authority:** [POINT-0/GOLDEN](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-GOLDEN-20261122-001.md).
2. **This operating rule:** Copy 2 workbench and owner-command boundary (this file).
3. **Current execution queue:** [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md).
4. **Host identity proposal:** [PR #172](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/pull/172) — proposal only; not proof of runtime identity or registry enrollment.
5. **Current workbench branch:** [palang-safe-copy-2-workbench-20261127](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/tree/palang-safe-copy-2-workbench-20261127).
6. **Latest execution evidence:** use the GitHub Actions run attached to the exact candidate SHA. Do not reuse a previous run as proof for a newer SHA.

At the start and end of each work cycle, refresh the actual branch refs and record: current MAIN SHA, Copy 1 SHA, Copy 2 SHA, open PRs, latest workflow result, next open task and blockers. A timestamp or status copied from an older chat is not current evidence.

## 5. Current observed state (2026-11-27)

- MAIN and Copy 1 currently point to the same commit: `ae52a024692f874126ecbe2c297c3d62e1558d35`.
- A fresh Copy 2 workbench branch was created from that exact baseline: `palang-safe-copy-2-workbench-20261127`.
- The older branch `palang-safe-copy-2-test-20261126` points to `f7bdf639f8c5fce7e165db2ab64f5c55d966bbe7`, which is now an ancestor of the current MAIN/Copy 1 merge commit. Treat it as historical candidate lineage, not as the active isolated workbench.
- PR #173 was merged into the Copy 1 branch; PR #175 then promoted the Copy 1 baseline to MAIN. Current MAIN and Copy 1 are aligned. This does not grant future Copy 2 candidates automatic promotion rights.
- PR #172 remains a separate open/draft identity proposal. Its existence does not register or cryptographically authenticate a runtime host.
- The repository is **PUBLIC**. The new Copy 2 branch is **NOT protected**. Therefore this is a logical workbench boundary, **not yet a private or independently secured environment**.
- The repository branch currently has no verified independent policy runner that a candidate cannot modify. A workflow stored in the candidate branch is useful validation, but is not by itself a trusted security boundary.
- No fresh-host cold-start recovery test is claimed as passed by this control-plane change.

## 6. Non-negotiable stop conditions

Stop and report `BLOCKED` if any of these occur:

- an AI or automation attempts to write to MAIN or Copy 1 directly;
- a Copy 2 → Copy 1 bridge is attempted without the owner's explicit command;
- a PR targets MAIN, or a merge/promotion is inferred from a green check;
- branch ancestry, SHA, diff, or evidence cannot be verified;
- a candidate controls the only validator used to approve itself;
- a public/unprotected branch is represented as private or secure isolation;
- host identity is claimed VERIFIED without independent runtime proof.

## 7. Next executable work

1. Keep all implementation and repairs on the active Copy 2 workbench.
2. Repair the stale Copy 2 validation workflow so it resolves the current Copy 1 baseline dynamically instead of hard-coding the retired SHA and old path list.
3. Fix the three known audit gaps: parse `- uses:` correctly and require full action SHA pins; move trust in validation outside candidate-controlled code; verify real SHA/ancestry/evidence rather than caller-supplied booleans.
4. Add negative tests for forged evidence, malformed SHAs, candidate-edited validators, unpinned actions and unauthorized target branches.
5. Prove a clean-host recovery run and the bridge's owner-command gate.
6. Only after evidence is complete, prepare a candidate for Copy 1; do not open that PR until the owner commands it.

**Truth rule:** this control plane is now written into the Copy 2 workbench. It does not, by itself, prove private isolation, branch protection, trusted external validation, runtime host identity, or clean-host recovery. Each remains OPEN until verified from live evidence.
