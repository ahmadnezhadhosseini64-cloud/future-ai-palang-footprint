# OUT-127 — Owner approval gate and host isolation

- Stable ID: HAIF-OUT-127-OWNER-APPROVAL-GATE-2026-11-22
- Parent: IN-128
- Status: DESIGN APPROVED / IMPLEMENTATION PARTIAL

## Resolved interpretation
The existing POINT-0/084 owner-only master architecture remains canonical and unchanged in its isolation boundary. This continuation adds a promotion gate, not direct host access to the master.

## Required flow
HOST PRIVATE WORKSPACE → OWNER EXPORT → QUARANTINE → PROVENANCE/HASH/TEST REVIEW → EXPLICIT OWNER APPROVAL → OWNER-CONTROLLED PROMOTION → MASTER.

## GitHub enforcement design
- Require one approving review for PRs created by non-owner identities/authorized automation.
- Require Code Owner review with owner assigned in CODEOWNERS.
- Dismiss stale approvals on new commits and require review-thread resolution.
- No host account or host app may bypass.
- GitHub does not allow a PR author to approve their own PR. Owner-authored PRs need a narrowly scoped owner-only PR bypass or a trusted owner-controlled promotion bot. This is a GitHub workflow constraint, not a reason to grant hosts write access.

## Live state
Ruleset 27814009 is active for main; deletion, non-fast-forward and PR rules are active. Live approval count is 0 and Code Owner review is false. Configuration is pending manual GitHub UI change and read-back.