# EVT-0314 — Owner-approved independent Partner API/MCP bridge bootstrap

- Event ID: EVT-0314
- Status: ACTIVE / LIVING / IMPLEMENTATION-IN-PROGRESS
- Canonical root: POINT-0
- Baseline: POINT-0/GOLDEN
- Parent checkpoint: CURRENT-144 / POINT-0++
- Sole queue: NEXT-051
- Owner: @ahmadnezhadhosseini64-cloud

## Owner direction

The owner explicitly approved the independent OpenAI API + GitHub OAuth/MCP route and authorized the Palang Partner to carry out all supported work without repeated approval. This event records that decision and the initial repository-side implementation.

## Decision

OpenAI API and GitHub OAuth/MCP are components of one independent Partner execution service, not alternatives. The service is separate from the current ChatGPT Free mobile conversation. Future hosts remain isolated and receive no Partner credentials or RAHM access.

## Executed work

1. Created branch `partner-control-plane-bootstrap-20261122` from `governance/point-0-golden-baseline-20261122`.
2. Added `docs/architecture/PALANG-PARTNER-INDEPENDENT-API-MCP-BRIDGE-2026-11-22.md` with target topology, owner OAuth, GitHub App permission model, MCP tool inventory, approval policy, audit/read-back requirements, deployment components, acceptance sequence and current tool boundary.
3. Source commit: `cc27e678f12b53de3b8b1a4835906f426ad03c8d`.

## Current state

- Repository-side bridge architecture: MERGED to Golden through PR #109 and mirrored to main through PR #110.
- PR #109: MERGED; merge commit `414a87792b701e4d97fe28bec7d93de1a0328381`.
- GitHub App registration/OAuth client: NOT CREATED.
- OpenAI API project/key: NOT CONFIGURED.
- Private service repository/hosting: NOT PROVISIONED.
- MCP implementation/deployment/live endpoint: NOT BUILT / NOT DEPLOYED.
- Host isolation: design specified; runtime proof NOT RUN.
- PR #110 snapshot merge commit/main HEAD: `90a0282e03e1a50b270d33ed470cbd9d15d6f5b9`.
- Golden/main tree equality read-back: PASS; both tree SHA `88dcc25f6fa0c25da85f59d916218ecc4f484b9a`.

Do not describe the bridge as connected or active until OAuth, deployment, tool calls, tests and read-back are proven. Continue all supported work under NEXT-051.
