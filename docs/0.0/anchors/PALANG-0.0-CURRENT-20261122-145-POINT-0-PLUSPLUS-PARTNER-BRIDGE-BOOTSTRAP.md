# CURRENT-145 — POINT-0++ / Independent Palang Partner bridge bootstrap

- Stable ID: HAIF-CURRENT-145-POINT-0-PLUSPLUS-PARTNER-BRIDGE-BOOTSTRAP-2026-11-22
- Display label: POINT-0++
- Status: ACTIVE / LIVING / IMPLEMENTATION-IN-PROGRESS
- Canonical root: POINT-0
- Canonical baseline: POINT-0/GOLDEN
- Parent: CURRENT-144
- Event: [EVT-0314](../../architecture/BEHAVIOR-TRACE/EVT-0314-OWNER-APPROVED-INDEPENDENT-PARTNER-API-MCP-BRIDGE-BOOTSTRAP-2026-11-22.md) → [TIME-BINDING-EVT-0314](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0314-OWNER-APPROVED-PARTNER-BRIDGE-2026-11-22.md)
- Sole active queue: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Owner: @ahmadnezhadhosseini64-cloud

## 1. Owner instruction and operating rule

The owner explicitly approved the independent OpenAI API + GitHub OAuth/MCP route and authorized the Palang Partner to complete all operations supported by the connected tools. Do not defer supported work or request repeated approval. Continue until a real platform/tool boundary, mandatory secure sign-in, or missing external credential is reached.

## 2. Architecture decision

OpenAI API and GitHub OAuth/MCP are both required components of one independent Partner service:
- OpenAI Responses API provides the model interface.
- GitHub OAuth through an owner-authorized GitHub App provides owner identity and GitHub authorization.
- The remote MCP service exposes controlled GitHub operations to the Responses API.
- A private hosting target stores the service, encrypted sessions, audit records and secrets.

This service is independent of the current ChatGPT Free mobile conversation. It does not automatically add tools to this conversation.

## 3. Verified repository-side work

- Working branch created from Golden: `partner-control-plane-bootstrap-20261122`.
- Bridge specification added: [PALANG PARTNER — INDEPENDENT OPENAI API + GITHUB OAUTH/MCP BRIDGE](../../architecture/PALANG-PARTNER-INDEPENDENT-API-MCP-BRIDGE-2026-11-22.md).
- Owner authorization event: [EVT-0314](../../architecture/BEHAVIOR-TRACE/EVT-0314-OWNER-APPROVED-INDEPENDENT-PARTNER-API-MCP-BRIDGE-BOOTSTRAP-2026-11-22.md).
- Exact event time: [TIME-BINDING-EVT-0314](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0314-OWNER-APPROVED-PARTNER-BRIDGE-2026-11-22.md).
- Architecture source commit: `cc27e678f12b53de3b8b1a4835906f426ad03c8d`.
- Event commit: `48519b4db9f9635bdaaa963c33aab4e3eca018fd`.
- PR #109 to Golden: MERGED / VERIFIED (merge commit `414a87792b701e4d97fe28bec7d93de1a0328381`).

## 4. Runtime status — do not overclaim

| Component | State |
|---|---|
| Architecture and tool/permission design | MERGED TO GOLDEN AND MAIN |
| Working branch and event evidence | CREATED |
| GitHub App registration and owner OAuth | NOT CREATED |
| OpenAI API project/key | NOT CONFIGURED |
| Private service repository | NOT CREATED |
| Hosting / HTTPS endpoint | NOT PROVISIONED |
| MCP server implementation | NOT BUILT |
| OpenAI API integration | NOT BUILT |
| Live end-to-end tests | NOT RUN |
| Host isolation runtime proof | NOT RUN |

The current connected tools do not expose GitHub App registration, repository creation, OpenAI project/key creation, hosting provisioning, or arbitrary authenticated deployment. No credentials may be pasted into chat. The assistant will continue all repository operations it can execute and will identify only the exact remaining external boundary.

## 5. Isolation invariants

- Partner authority is distinct from future host permissions.
- No future host receives Partner tokens, GitHub OAuth sessions, OpenAI API keys, or RAHM access.
- The promotion bot remains narrow; do not expand its permissions to substitute for the Partner connection.
- No secrets in source control, chat, or audit logs.
- No auto-merge; every write must be followed by read-back.
- No destructive operations or bypass tools in the MCP surface.

## 6. Continuation

CURRENT-145 extends CURRENT-144 on the existing POINT-0 root. NEXT-051 remains the sole queue. The immediate next repository action is to finish this proposal branch and open a PR to Golden. Runtime provisioning follows only through a secure owner-authorized provider flow.
