# EVT-0318 — live main protection and promotion-workflow audit

- Stable ID: HAIF-EVT-0318-LIVE-MAIN-RULESET-AND-PROMOTION-WORKFLOW-AUDIT-2026-11-22
- Event class: GOVERNANCE READ-BACK / SECURITY CONTROL AUDIT
- Canonical root: POINT-0
- Baseline: POINT-0/GOLDEN
- Parent checkpoint: CURRENT-148
- Owner: @ahmadnezhadhosseini64-cloud

## Live read-back performed

- Read the owner-controlled Golden-to-main snapshot promotion workflow from both Golden and main.
- Both branches returned the same workflow blob SHA: c9357765c0997576eee8180181f1106377033957.
- Read active repository Ruleset 27814009, PROTECT-MAIN-BRANCH64.
- Ruleset enforcement is active; default branch protected against deletion and non-fast-forward.
- Pull request rule currently has required_approving_review_count = 0, require_code_owner_review = false, require_last_push_approval = false, required_review_thread_resolution = false.
- Ruleset bypass_actors is empty and current_user_can_bypass is never.
- The promotion workflow requires repository variable PALANG_PROMOTION_APP_CLIENT_ID and secret PALANG_PROMOTION_APP_PRIVATE_KEY, checks that both are present, and then mints a GitHub App token with scoped contents/pull_requests/workflows permissions.
- This session cannot read or write Actions secret/variable values and did not dispatch the workflow. App registration/installation and secret configuration are therefore NOT VERIFIED.

## Governance result

- The main approval gate is NOT ENFORCED to the intended standard while required approvals remain 0 and CODEOWNERS review is false.
- The bot-authored promotion workflow source exists on both branches but is NOT OPERATIONAL / NOT RUN until the App and its repository credentials are provisioned and the workflow is safely tested.
- No PR to main was created and main was not modified.
- Main/Golden compare after CURRENT-148 publication: DIVERGED, Golden ahead 187 / behind 17; main base SHA aaf96c5e195f6f4f59dea43ebd9922b5f009c9ea.

## Required actions

1. #120: register/install the owner-controlled promotion GitHub App, configure the exact repository variable and secret through GitHub's secure settings UI, then run a controlled workflow dispatch and verify a bot-authored PR. Never paste the private key into chat or public repository.
2. #121: set required approvals to at least 1 and enable CODEOWNERS review in the live main Ruleset, then read back the Ruleset and run a negative test proving an unapproved PR cannot merge.
3. Only after #120 and #121 acceptance, publish the exact Golden snapshot to main through the App-authored PR and owner approval path.

## Non-negotiable boundaries

MASTER remains PUBLIC READ ONLY for hosts. No host write or bypass. RAHM remains private and owner-only. No auto-merge. No secrets in chat, public repository, Issues or logs. No host activation without independent acceptance.

## Continuity

POINT-0/GOLDEN → CURRENT-148 → EVT-0318 → TIME-BINDING-EVT-0318 → CURRENT-149 → sole NEXT-051.
