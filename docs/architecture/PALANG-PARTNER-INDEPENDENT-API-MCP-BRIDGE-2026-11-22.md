# PALANG PARTNER — INDEPENDENT OPENAI API + GITHUB OAUTH/MCP BRIDGE

- Stable ID: HAIF-PALANG-PARTNER-INDEPENDENT-API-MCP-BRIDGE-2026-11-22-001
- Status: IMPLEMENTATION PLAN / ACTIVE — SOURCE-OF-TRUTH UNDER POINT-0
- Canonical root: POINT-0
- Baseline: POINT-0/GOLDEN
- Checkpoint: CURRENT-144 / POINT-0++
- Sole queue: NEXT-051
- Owner: @ahmadnezhadhosseini64-cloud

## 1. Decision

The selected route is one independent Partner execution service composed of both:
- OpenAI API (Responses API) as the model/runtime interface.
- GitHub OAuth through an owner-authorized GitHub App, with a remote MCP server exposing narrowly scoped GitHub operations.

These are not competing alternatives. The OAuth client handles owner sign-in and token lifecycle; the MCP service validates the resulting authorization and executes GitHub operations; the OpenAI Responses API calls the remote MCP tools. This service is separate from the current ChatGPT Free mobile conversation. It does not automatically extend the current conversation's connected GitHub tools.

Official OpenAI reference: https://developers.openai.com/api/docs/guides/tools-connectors-mcp
Official GitHub App permissions reference: https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps

## 2. Target topology

```text
Owner (GitHub sign-in + MFA)
        |
        v
Partner Web Console / OAuth callback
        |
        | encrypted, short-lived owner GitHub user token
        v
Palang Partner MCP Service  <----> Audit / session store
        |
        | allowlisted MCP tools + per-tool approval policy
        v
OpenAI Responses API (OpenAI API key held server-side)
        |
        v
Owner-facing Partner UI / conversation
```

The MCP server must be a remotely reachable HTTPS service for the initial deployment. A private/local deployment can later use OpenAI Secure MCP Tunnel if the hosting model requires it.

## 3. Identity, access and isolation

1. GitHub sign-in is performed by the owner in a first-party browser flow; never request passwords, MFA codes, OAuth codes, private keys, PATs, or API keys in ChatGPT messages.
2. Use a GitHub App with user authorization (user-to-server token) for owner actions. An installation token alone is not a substitute for owner-account operations such as creating a repository under the owner's account.
3. Validate the authenticated GitHub identity on every session and bind it to the allowlisted owner login `ahmadnezhadhosseini64-cloud`.
4. Keep the OpenAI API key and GitHub OAuth client secret in the hosting provider's secret manager. Encrypt GitHub tokens at rest; use short lifetimes, refresh/revocation where supported, and explicit disconnect.
5. Repository access is allowlisted. Initial target: `ahmadnezhadhosseini64-cloud/future-ai-palang-footprint`; private RAHM can be added only after it exists and the owner explicitly enables it.
6. The service identity is the Palang Partner, not a future host. No token, session, endpoint, credential, or permission is exposed to a host workspace.
7. RAHM stays private and outside all host workspaces. Never include RAHM content in model context unless the owner explicitly requests a scoped retrieval.

## 4. MCP tool surface

### Read / ordinary operations
- `github_whoami`: return authenticated login and granted scopes/permissions, never token material.
- `github_get_repository`: metadata for an allowlisted repository.
- `github_list_branches`: branch names and head SHAs.
- `github_read_file`: read a path on an allowlisted repository/ref.
- `github_create_branch`: create a branch from a named ref/SHA.
- `github_write_file`: create/update a file on an explicitly selected non-protected working branch.
- `github_create_pull_request`: open a PR; no auto-merge.
- `github_get_pull_request` and `github_read_commit`: read-back and verification.
- `github_list_workflow_runs`: read workflow run metadata.

### Elevated operations — separate approval gates
- `github_create_private_repository`: only under the authenticated owner's account, private visibility forced server-side; reject public visibility.
- `github_set_actions_secret`: write-only; accept secret value from a secure UI field, encrypt for GitHub using its public key, never log or return plaintext.
- `github_set_actions_variable`: create/update a named variable on an allowlisted repository.
- `github_dispatch_workflow`: dispatch only allowlisted workflow IDs and validated inputs.
- `github_update_ruleset`: only the explicitly allowlisted repository/ruleset; read current state, apply a minimal patch, then read back.
- `github_install_or_configure_app`: not an MCP runtime tool. App registration/installation is a one-time owner-side GitHub developer-settings flow.

The MCP server must not expose generic arbitrary HTTP, arbitrary GraphQL, shell, raw token retrieval, secret reads, repository deletion, transfer, collaborator management, force-push, ruleset bypass, or automatic PR merge.

## 5. Permission model

Use a GitHub App with the minimum permission set for the Partner's separately approved responsibilities. Expected repository permissions include:
- Metadata: read.
- Contents: read/write.
- Pull requests: read/write.
- Actions: write only if workflow dispatch is enabled.
- Secrets: write only if setting Actions secrets is enabled.
- Variables: write only if setting Actions variables is enabled.
- Administration: write only if repository creation/ruleset mutation is enabled and GitHub's current permission matrix requires it.
- Workflows: write only if workflow-file changes are enabled.

Do not add broad permissions to the separate `palang-owner-promotion-bot`. That bot remains narrow and cannot inherit Partner authority. Confirm the current GitHub permission matrix during App registration; do not assume every permission is available to installation tokens.

## 6. Approval policy

- Read-only calls: may run without a confirmation after owner login is verified.
- Branch/file/PR writes: allowed only on explicitly named working branches; PR creation is allowed, merging is not automatic.
- Private repository creation: require a specific tool-call approval immediately before execution, even when the owner has authorized the overall project.
- Secrets/variables: require per-operation confirmation and secure input UI; secret values are write-only and excluded from audit payloads.
- Workflow dispatch: require confirmation for production workflows; permit unattended dispatch only for explicitly allowlisted harmless test workflows.
- Ruleset changes, permission changes, installation changes and any operation affecting host isolation: require explicit per-operation confirmation and mandatory read-back.
- Destructive operations (delete/transfer/force-push/bypass) are not exposed by the service.

## 7. Audit and read-back

Every mutation records: request ID, authenticated actor, repository, operation name, target ref/path/ID, timestamp, approval event, GitHub response ID/SHA, outcome, and read-back result. Never record authorization headers, token values, secret plaintext, private keys, or OAuth codes.

A write is not complete until a separate read-back verifies the resulting state. Failed or incomplete read-back is recorded as OPEN / UNVERIFIED, never PASS.

## 8. Deployment components

The independent service requires:
1. A private source repository or a private deployment workspace for the MCP service (do not place credentials or private RAHM data in the public master).
2. A hosting target with HTTPS, environment secrets, durable encrypted session storage, logs, and a deploy pipeline.
3. An OpenAI API project and API key, stored only in the hosting secret manager.
4. A GitHub App registration with user authorization enabled, callback URL, minimum permissions, and owner installation/consent.
5. OAuth callback/session implementation with CSRF state, PKCE where supported, strict redirect URI allowlist, token encryption, revocation/disconnect, and owner-login verification.
6. Remote MCP transport compatible with the OpenAI Responses API; only approved tool names are exposed.
7. Automated unit/integration tests, including negative tests for non-owner login, non-allowlisted repositories, public RAHM creation, host token inheritance, secret logging, and protected-branch writes.

## 9. Build and acceptance sequence

- B0 — Architecture and permissions: this specification; DONE as a repository proposal once merged into Golden.
- B1 — Create a private implementation repository and hosting target.
- B2 — Register GitHub App and configure OAuth callback/permissions.
- B3 — Implement OAuth session broker and encrypted token store.
- B4 — Implement MCP server with the allowlisted tool surface.
- B5 — Implement OpenAI Responses API client; API key remains server-side; pass OAuth access token to the MCP tool configuration as documented by OpenAI.
- B6 — Deploy HTTPS endpoint and connect it to the owner-facing client.
- B7 — Run read-only identity/repository tests, then controlled branch/PR tests.
- B8 — Run separately approved private-repository, Actions, workflow and Ruleset tests as their permissions become available.
- B9 — Prove host isolation and complete read-back/audit review.

Do not mark the Partner connection ACTIVE / COMPLETE until the live endpoint, OAuth identity, tool inventory, tests, and read-back evidence exist.

## 10. Current hard boundary and immediate next step

The current ChatGPT GitHub connector can write repository content, create branches and PRs, merge PRs, and read back results. It does not expose GitHub App registration, repository creation, Actions secret/variable writes, workflow dispatch, Ruleset mutation, hosting provisioning, OpenAI API key creation, or deployment. This session also has no general-purpose authenticated browser, hosting account connector, or arbitrary HTTP POST capability.

Therefore this assistant can prepare and commit the source-controlled implementation contract and all repository-side work. It cannot truthfully register the GitHub App, create a hosting account/service, create an OpenAI API key, or deploy the endpoint from the current tool surface. Those actions require the owner to complete secure sign-in/secret entry in the relevant provider interface or to connect a deployment/API tool that exposes them. No credential should be pasted into chat.

The next operational milestone is B1: provision a private service repository and hosting target, then proceed through B2–B6. Keep all work under the sole queue NEXT-051; do not create a parallel queue.
