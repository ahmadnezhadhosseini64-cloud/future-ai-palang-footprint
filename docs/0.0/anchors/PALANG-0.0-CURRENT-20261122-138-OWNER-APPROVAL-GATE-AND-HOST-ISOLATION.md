> Historical checkpoint: superseded by CURRENT-139 / POINT-0/086 (0++). Its Ruleset and architecture receipts remain historical; consult CURRENT-139 for the latest continuation.

# CURRENT-138 — دروازهٔ تأیید مالک و جداسازی میزبان‌ها

- Status: ACTIVE / LIVING / OWNER-DIRECTED / DESIGN-APPROVED / MERGED TO MAIN / READ-BACK VERIFIED
- Parent checkpoint: CURRENT-137
- Current point: POINT-0/085 (0++)
- Input/output: IN-128 → OUT-127
- Event/time: EVT-0305 → TIME-BINDING-EVT-0305
- Living master target: 1.7.93
- Sole active queue: NEXT-051
- Canonical master: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint

## Decision
Preserve the existing owner-only master and per-host isolated private workspace architecture. Add an owner-controlled promotion gate: host outputs remain proposals and cannot enter MASTER until owner export, quarantine, provenance/hash/test review and explicit approval.

## Required GitHub review policy
- Exactly one approving review is required, and the only intended approver/Code Owner is GitHub account `@ahmadnezhadhosseini64-cloud`; `.github/CODEOWNERS` assigns all paths to this account.
- Owner is the Code Owner for all paths.
- Dismiss stale approvals on new commits and require review-thread resolution.
- No host identity or host application may receive master access or bypass.
- GitHub prevents a PR author from approving their own PR; owner-authored PRs need a narrowly scoped owner-only PR bypass or a trusted owner-controlled promotion bot.

## Live evidence
- Ruleset PROTECT-MAIN-BRANCH64 / 27814009 is active and targets main.
- Deletion, non-fast-forward and pull-request rules are active.
- Live approval count remains 0; Code Owner review remains false; stale-review dismissal and review-thread resolution remain false. The intended settings are 1 approval by `@ahmadnezhadhosseini64-cloud`, Code Owner review ON, stale-review dismissal ON and review-thread resolution ON.
- Branch API reports protected=true.
- The available GitHub connection in this workflow supports repository content/PR operations and Ruleset read-back, but does not expose a Ruleset update operation. Manual UI configuration and exact read-back remain pending.
- CODEOWNERS and architecture baseline were merged through PR #93; 12/12 changed files were read back and blob-SHA matched. PR #95 then synchronized the living master (1.7.93), NEXT-051, Reference Index and Integration Queue to CURRENT-138; all 4/4 changed files were read back from main with exact blob-SHA matches at HEAD `8a22c302dff17a3be7cb9b9a2513be011cf969a7`.

## PR #95 synchronization receipt
- PR #95: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/pull/95
- Merge commit: `8a22c302dff17a3be7cb9b9a2513be011cf969a7` (UTC `2026-11-21T23:03:07Z`).
- Exact-main read-back: 4/4 changed files blob-SHA matched.

## Open gates
- Set approval count to 1 and enable Code Owner review, stale-review dismissal and conversation resolution in GitHub UI; read back exact settings.
- Configure owner-only PR-scoped bypass or owner-controlled promotion automation for owner-authored PRs; never add hosts to bypass.
- Audit collaborator/App/deploy-key access and perform negative isolation tests.
- Provision real private host repositories and broker only when required and proven.
- No claim of SECURITY_VERIFIED or HOST_RECOVERED until direct evidence exists.
## Merge receipt
- PR #93: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/pull/93
- Merge commit: f40b9fee9368d68d8d3719fcedda4f39aa41ea9c
- Commit timestamp: 2026-11-21T22:55:11Z UTC.
- Exact-main read-back: 12/12 changed files SHA-matched.
