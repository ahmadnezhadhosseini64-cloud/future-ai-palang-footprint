# Owner-Controlled Promotion GitHub App — Setup Contract

- Stable ID: HAIF-RAHM-PROMOTION-APP-SETUP-2026-11-22-001
- Status: SPECIFIED / NOT CREATED / NOT INSTALLED
- Suggested App name: palang-owner-promotion-bot
- Owner: ahmadnezhadhosseini64-cloud

## 1. Create the App

Open https://github.com/settings/apps/new while signed in as the repository owner.

- GitHub App name: palang-owner-promotion-bot (choose an available unique name if already taken).
- Homepage URL: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint
- Webhook: inactive; no webhook URL or webhook secret is required for the current workflow.
- Do not request user-to-server permissions.
- Do not subscribe to repository events unless a later reviewed feature requires them.

## 2. Minimum repository permissions

| Permission | Access | Purpose |
|---|---|---|
| Metadata | Read (GitHub default) | Required repository metadata |
| Contents | Read and write | Checkout main, create a dedicated promotion branch, push candidate files |
| Pull requests | Read and write | Open a bot-authored PR for owner review |

All other repository permissions must remain No access, especially:
- Administration, Rules, Branch protection, Actions, Secrets, Variables, Environments, Workflows, Deployments, Issues, Releases, Webhooks and Pages.

The App is a PR publisher only. It is not an approver, merger, administrator, or bypass identity.

## 3. Install scope

Install the App on selected repositories only:
- Select only ahmadnezhadhosseini64-cloud/future-ai-palang-footprint.
- Do not install it on future-ai-palang-rahm or any host-private repository.
- Do not add the App as a bypass actor in Ruleset 27814009.
- Do not grant any AI host access to the App installation or private key.

## 4. Add repository variable and secret

In the master repository:
- Settings → Secrets and variables → Actions → Variables → New repository variable:
  - Name: PALANG_PROMOTION_APP_CLIENT_ID
  - Value: the GitHub App Client ID.
- Settings → Secrets and variables → Actions → Secrets → New repository secret:
  - Name: PALANG_PROMOTION_APP_PRIVATE_KEY
  - Value: the private key generated for this App.

The private key is a secret. Never paste it into ChatGPT, host prompts, issues, files, commits, or logs.

## 5. RAHM read-only credential

Create a fine-grained personal access token limited to the single private repository future-ai-palang-rahm:
- Repository access: Only selected repositories → future-ai-palang-rahm.
- Repository permission: Contents Read only (Metadata read is automatic).
- No write, administration, Actions, workflow, pull-request, or bypass permission.
- Add it to the master repository as Actions secret RAHM_READ_TOKEN.

This credential is separate from the Promotion App token. It can read RAHM only; it cannot write to master.

## 6. First end-to-end test

After the private RAHM repository, App, installation, variable and secrets are configured:
1. Put a synthetic, owner-redacted candidate with manifest.json, proposal.md, evidence.json and validation.json in private RAHM.
2. Run the owner-only workflow RAHM to CHILD — Owner-Controlled Promotion from main.
3. Confirm the PR author is the Promotion GitHub App bot, not the owner account.
4. Confirm the destination is only docs/architecture/CHILD-CANDIDATES/<CANDIDATE_ID>/.
5. Confirm no automatic merge occurs and no living Master document changes.
6. ChatGPT performs a technical/security review report; the owner submits the required GitHub approval.
7. Confirm the merge only admits the candidate to CHILD. Master promotion remains a separate future PR.

## 7. Ruleset order

Do not change required approvals from 0 to 1 until the bot-authored PR route has passed the synthetic end-to-end test. Then set:
- Required approving reviews = 1
- Require Code Owner review = ON
- Dismiss stale approvals on new commits = ON
- Require review-thread resolution = ON

CODEOWNERS must remain solely @ahmadnezhadhosseini64-cloud. The App must not be a bypass actor. Re-read Ruleset 27814009 after saving and confirm exact values before declaring the gate active.
