# Palang Partner MCP runtime — Copy 2 candidate

This is the source-controlled runtime prototype for the independent Palang Partner bridge. It is not yet the live service and must not be exposed publicly until the owner OAuth/session broker and hosting controls are configured.

## Runtime

- Node.js 20 or newer (container uses Node 22).
- MCP endpoint: \`/mcp\` using Streamable HTTP.
- Health endpoint: \`/health\` (no GitHub data is returned).
- Required environment: \`PUBLIC_ORIGIN=https://the-exact-public-host.example\`.
- When deployed behind a TLS-terminating reverse proxy, set \`TRUST_PROXY=1\`; the proxy must preserve the public Host header and set \`X-Forwarded-Proto: https\`.
- Optional environment: \`PORT\` (defaults to 8080).

## Local run

\`\`\`sh
npm install --ignore-scripts --no-audit --no-fund --package-lock=false
PUBLIC_ORIGIN=http://localhost:8080 npm start
\`\`\`

## Container

\`\`\`sh
docker build -t palang-partner-mcp:local .
docker run --rm -p 8080:8080 -e PUBLIC_ORIGIN=http://localhost:8080 palang-partner-mcp:local
\`\`\`

## Authentication and safety boundary

Every MCP request must carry an owner-authorized GitHub user access token in the HTTP Authorization bearer header. The server calls GitHub \`GET /user\` on every request and accepts only the owner login \`ahmadnezhadhosseini64-cloud\`. The token is held only in request memory and is never written to logs or persisted by this runtime.

**This repository does not yet implement the GitHub App OAuth callback, PKCE/state lifecycle, encrypted durable session store, refresh/revocation flow, owner sign-in UI, or OpenAI Responses API client.** A separate secure owner-side broker must obtain and supply the token; never paste a token into ChatGPT, commit it, or place it in a deployment variable.

The server exposes a single repository allowlist. It denies direct writes to MAIN, Copy 1 and Copy 2; new working branches must be created from Copy 2 and begin with \`palang-partner/\`. Proposal PRs are draft-only and target Copy 1. No merge, ruleset, secret, workflow-dispatch, delete, transfer or bypass tool is exposed. Repository paths containing credentials, keys, environment files or RAHM are rejected.

## Required before production

1. Register the owner-controlled GitHub App and implement its secure OAuth callback/session lifecycle.
2. Provision private hosting, HTTPS, secret management and durable encrypted audit/session storage.
3. Implement the owner-facing Partner UI and OpenAI Responses API client; keep the OpenAI API key server-side.
4. Run live MCP initialize/list/call tests, negative owner/repository/path tests, token expiry/revocation tests, disconnect tests, host-isolation tests and independent read-back.
5. Prove the deployed endpoint and exact image/source digest before calling the service connected.

Until these gates pass, status is **SOURCE CANDIDATE / NOT DEPLOYED / NOT CONNECTED**.
