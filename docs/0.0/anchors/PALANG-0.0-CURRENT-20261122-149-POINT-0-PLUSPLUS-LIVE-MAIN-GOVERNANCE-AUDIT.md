# CURRENT-149 — POINT-0++ / live main governance audit

- Stable ID: HAIF-CURRENT-149-POINT-0-PLUSPLUS-LIVE-MAIN-GOVERNANCE-AUDIT-2026-11-22
- Status: ACTIVE / LIVING / RULESET-READBACK / APPROVAL-GATE-OPEN
- Canonical root: POINT-0
- Golden baseline: POINT-0/GOLDEN
- Parent checkpoint: CURRENT-148
- Event: EVT-0318 → TIME-BINDING-EVT-0318
- Event commit: d613c96b2560d6f0f27f625f87f4ce1a8f94f30b
- Exact event time: UTC 2026-11-22T07:17:16Z / Tehran 2026-11-22T10:47:16+03:30
- Sole active queue: NEXT-051
- Owner: @ahmadnezhadhosseini64-cloud

## 1. Canonical chain

POINT-0/GOLDEN → CURRENT-148 → EVT-0318 → TIME-BINDING-EVT-0318 → CURRENT-149 → sole NEXT-051.

All prior POINT-0, 0.0, 0+, 0++ and IN/OUT/EVT/TIME/CURRENT records remain connected under the same canonical root. No parallel root or queue.

## 2. Live Ruleset 27814009

Read-back from GitHub API:
- Name: PROTECT-MAIN-BRANCH64.
- Target: branch / default branch.
- Enforcement: ACTIVE.
- Deletion and non-fast-forward protections: enabled.
- Required approving review count: 0.
- CODEOWNERS review: false.
- Last-push approval: false.
- Required review-thread resolution: false.
- Bypass actors: empty.
- Current user bypass: never.

Result: main is protected against deletion and force-push, but the intended owner approval gate is NOT ENFORCED because required approvals are 0 and CODEOWNERS review is disabled.

## 3. Promotion workflow source

The same workflow file exists on main and Golden:
- Path: .github/workflows/golden-owner-controlled-main-snapshot-promotion.yml
- Blob SHA on both branches: c9357765c0997576eee8180181f1106377033957.
- Workflow requires explicit workflow_dispatch confirmation PROMOTE_GOLDEN_TO_MAIN.
- It requires repository variable PALANG_PROMOTION_APP_CLIENT_ID and secret PALANG_PROMOTION_APP_PRIVATE_KEY.
- It creates a narrowly scoped App token and prepares a bot-authored snapshot PR; it cannot approve, merge, auto-merge or bypass rulesets.

The workflow file exists, but App registration/installation, secret/variable configuration, dispatch, PR creation and acceptance are NOT VERIFIED / NOT RUN in this session.

## 4. Main / Golden relationship

Latest compare after CURRENT-148: DIVERGED.
- Golden ahead: 187 commits.
- Golden behind: 17 commits.
- Main base SHA: aaf96c5e195f6f4f59dea43ebd9922b5f009c9ea.
- Merge base SHA: 9ebd4bcc5cfc0168276e366c1867da8709dfb566.

No force-sync or direct human-authored shortcut. Publish only through the trusted App-authored PR path and independent owner approval.

## 5. Issue state

Issues #114–#123 remain OPEN under NEXT-051. They have been updated to CURRENT-148. No action is closed without its own acceptance evidence.

## 6. Required next actions

1. #120 — owner registers and installs the least-privilege GitHub App; configures PALANG_PROMOTION_APP_CLIENT_ID and PALANG_PROMOTION_APP_PRIVATE_KEY through secure GitHub settings; dispatches the workflow; verifies a bot-authored PR.
2. #121 — owner changes Ruleset 27814009 to require at least one approval and CODEOWNERS review; read back the exact rules; run a negative test proving an unapproved PR cannot merge.
3. #114 — owner creates the private palang-partner repository and provides its URL; no host collaborators.
4. Continue #116–#119 and #122–#123 in dependency order. Keep all external/runtime states OPEN until receipts are verified.

## 7. Security invariants

MASTER is PUBLIC READ ONLY for hosts. RAHM remains private and owner-only. No secrets in chat, public Issues, repository or logs. No host write path, bypass or auto-merge. No host becomes ACTIVE without independent acceptance.

NEXT-051 remains the sole active queue.
