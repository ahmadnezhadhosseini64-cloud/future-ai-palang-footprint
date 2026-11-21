# CURRENT-138 — دروازهٔ تأیید مالک و جداسازی میزبان‌ها

- Status: ACTIVE / LIVING / OWNER-DIRECTED / DESIGN-APPROVED / MERGED TO MAIN / READ-BACK VERIFIED
- Parent checkpoint: CURRENT-137
- Current point: POINT-0/085 (0++)
- Input/output: IN-128 → OUT-127
- Event/time: EVT-0305 → TIME-BINDING-EVT-0305
- Living master target: 1.7.92
- Sole active queue: NEXT-051
- Canonical master: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint

## Decision
Preserve the existing owner-only master and per-host isolated private workspace architecture. Add an owner-controlled promotion gate: host outputs remain proposals and cannot enter MASTER until owner export, quarantine, provenance/hash/test review and explicit approval.

## Required GitHub review policy
- One approving review for non-owner/automation-authored PRs.
- Owner is the Code Owner for all paths.
- Dismiss stale approvals on new commits and require review-thread resolution.
- No host identity or host application may receive master access or bypass.
- GitHub prevents a PR author from approving their own PR; owner-authored PRs need a narrowly scoped owner-only PR bypass or a trusted owner-controlled promotion bot.

## Live evidence
- Ruleset PROTECT-MAIN-BRANCH64 / 27814009 is active and targets main.
- Deletion, non-fast-forward and pull-request rules are active.
- Live approval count remains 0; Code Owner review remains false.
- Branch API reports protected=true.
- GitHub connector supports ruleset read but not ruleset update; manual UI configuration and exact read-back remain pending.
- CODEOWNERS and all architecture files were merged through PR #93; 12/12 changed files were read back from main and blob-SHA matched.

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
