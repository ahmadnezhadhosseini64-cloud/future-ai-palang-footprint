import { createServer } from "node:http";
import { Readable } from "node:stream";
import { createMcpHandler, McpServer } from "@modelcontextprotocol/server";
import * as z from "zod/v4";
import {
  OWNER_LOGIN, ALLOWED_REPOSITORY, COPY1_BRANCH, COPY2_BRANCH,
  assertOwner, assertRepository, assertBranchReadable, assertBranchCreatable,
  assertWritableBranch, assertPullRequestTargets, assertSafePath, parseBearer,
  assertPartnerBranchComparison
} from "./policy.mjs";

const API = "https://api.github.com";
const API_VERSION = "2022-11-28";
const repoPath = (repository, suffix) => "/repos/" + repository + suffix;

async function github(token, path, options = {}) {
  const response = await fetch(API + path, {
    ...options,
    headers: {
      accept: "application/vnd.github+json",
      authorization: "Bearer " + token,
      "x-github-api-version": API_VERSION,
      ...(options.body ? { "content-type": "application/json" } : {}),
      ...options.headers
    }
  });
  const raw = await response.text();
  let data = null;
  try { data = raw ? JSON.parse(raw) : null; } catch { data = null; }
  if (!response.ok) {
    const error = new Error("GITHUB_API_" + response.status);
    error.status = response.status;
    throw error;
  }
  return { data, headers: response.headers };
}
async function authenticate(token) {
  const result = await github(token, "/user");
  assertOwner(result.data && result.data.login);
  return { login: result.data.login, scopes: result.headers.get("x-oauth-scopes") || "not-exposed-by-token-type" };
}
const resultText = (value) => ({ content: [{ type: "text", text: JSON.stringify(value) }] });
const encodedPath = (path) => path.split("/").map(encodeURIComponent).join("/");

function buildServer(token, actor) {
  const server = new McpServer({ name: "palang-partner-mcp", version: "0.1.0" });
  server.registerTool("github_whoami", {
    description: "Return the verified owner identity and non-secret scope metadata.",
    inputSchema: z.object({})
  }, async () => resultText(actor));

  server.registerTool("github_get_repository", {
    description: "Read metadata for the single allowlisted Palang repository.",
    inputSchema: z.object({ repository: z.string().default(ALLOWED_REPOSITORY) })
  }, async ({ repository }) => {
    assertRepository(repository);
    const { data } = await github(token, repoPath(repository, ""));
    return resultText({ full_name: data.full_name, private: data.private, default_branch: data.default_branch, permissions: data.permissions || null });
  });

  server.registerTool("github_list_branches", {
    description: "List branch names and SHAs for the allowlisted repository.",
    inputSchema: z.object({ repository: z.string().default(ALLOWED_REPOSITORY) })
  }, async ({ repository }) => {
    assertRepository(repository);
    const { data } = await github(token, repoPath(repository, "/branches?per_page=100"));
    return resultText(data.map((item) => ({ name: item.name, sha: item.commit && item.commit.sha })));
  });

  server.registerTool("github_read_file", {
    description: "Read a file from an explicitly named branch or commit.",
    inputSchema: z.object({ repository: z.string().default(ALLOWED_REPOSITORY), path: z.string(), ref: z.string() })
  }, async ({ repository, path, ref }) => {
    assertRepository(repository); assertSafePath(path); assertBranchReadable(ref);
    const suffix = "/contents/" + encodedPath(path) + "?ref=" + encodeURIComponent(ref);
    const { data } = await github(token, repoPath(repository, suffix));
    if (data.type !== "file" || !data.content) throw new Error("FILE_NOT_READABLE");
    return resultText({ path, ref, sha: data.sha, content: Buffer.from(data.content, "base64").toString("utf8") });
  });

  server.registerTool("github_create_branch", {
    description: "Create a Palang Partner working branch from Copy 2 only.",
    inputSchema: z.object({ repository: z.string().default(ALLOWED_REPOSITORY), branch: z.string(), base: z.string().default(COPY2_BRANCH) })
  }, async ({ repository, branch, base }) => {
    assertRepository(repository); assertBranchCreatable(branch, base);
    const source = await github(token, repoPath(repository, "/git/ref/heads/" + base));
    const created = await github(token, repoPath(repository, "/git/refs"), {
      method: "POST", body: JSON.stringify({ ref: "refs/heads/" + branch, sha: source.data.object.sha })
    });
    return resultText({ branch, sha: created.data.object.sha, base, base_sha: source.data.object.sha });
  });

  server.registerTool("github_write_file", {
    description: "Write only to a Palang Partner branch; direct writes to MAIN, Copy 1 and Copy 2 are blocked.",
    inputSchema: z.object({ repository: z.string().default(ALLOWED_REPOSITORY), branch: z.string(), path: z.string(), content: z.string(), message: z.string().min(8).max(120) })
  }, async ({ repository, branch, path, content, message }) => {
    assertRepository(repository); assertWritableBranch(branch); assertSafePath(path);
    const ancestry = await github(token, repoPath(repository, "/compare/" + COPY2_BRANCH + "..." + encodeURIComponent(branch)));
    assertPartnerBranchComparison(ancestry.data.status);
    const target = "/contents/" + encodedPath(path);
    let sha;
    try {
      const current = await github(token, repoPath(repository, target + "?ref=" + encodeURIComponent(branch)));
      sha = current.data.sha;
    } catch (error) {
      if (error.status !== 404) throw error;
    }
    const payload = { message, content: Buffer.from(content, "utf8").toString("base64"), branch, ...(sha ? { sha } : {}) };
    const saved = await github(token, repoPath(repository, target), { method: "PUT", body: JSON.stringify(payload) });
    return resultText({ path, branch, commit_sha: saved.data.commit && saved.data.commit.sha, content_sha: saved.data.content && saved.data.content.sha });
  });

  server.registerTool("github_create_pull_request", {
    description: "Open a draft proposal PR from a Partner branch to Copy 1 only. Merge is not exposed.",
    inputSchema: z.object({ repository: z.string().default(ALLOWED_REPOSITORY), head: z.string(), base: z.string().default(COPY1_BRANCH), title: z.string().min(8).max(200), body: z.string().max(10000).optional() })
  }, async ({ repository, head, base, title, body = "" }) => {
    assertRepository(repository); assertPullRequestTargets(head, base);
    const ancestry = await github(token, repoPath(repository, "/compare/" + COPY2_BRANCH + "..." + encodeURIComponent(head)));
    assertPartnerBranchComparison(ancestry.data.status);
    const created = await github(token, repoPath(repository, "/pulls"), {
      method: "POST", body: JSON.stringify({ head, base, title, body, draft: true })
    });
    const data = created.data;
    return resultText({ number: data.number, url: data.html_url, state: data.state, merged: data.merged, base: data.base && data.base.ref, head: data.head && data.head.ref });
  });

  server.registerTool("github_get_pull_request", {
    description: "Read PR state and head SHA; this server cannot merge PRs.",
    inputSchema: z.object({ repository: z.string().default(ALLOWED_REPOSITORY), number: z.number().int().positive() })
  }, async ({ repository, number }) => {
    assertRepository(repository);
    const { data } = await github(token, repoPath(repository, "/pulls/" + number));
    return resultText({ number: data.number, state: data.state, merged: data.merged, base: data.base && data.base.ref, head: data.head && data.head.ref, head_sha: data.head && data.head.sha, merge_commit_sha: data.merge_commit_sha, url: data.html_url });
  });

  server.registerTool("github_read_commit", {
    description: "Read commit metadata for the allowlisted repository.",
    inputSchema: z.object({ repository: z.string().default(ALLOWED_REPOSITORY), sha: z.string().regex(/^[0-9a-f]{40}$/i) })
  }, async ({ repository, sha }) => {
    assertRepository(repository);
    const { data } = await github(token, repoPath(repository, "/commits/" + sha));
    return resultText({ sha: data.sha, message: data.commit && data.commit.message, author_date: data.commit && data.commit.author && data.commit.author.date, html_url: data.html_url, parents: (data.parents || []).map((parent) => parent.sha) });
  });

  server.registerTool("github_list_workflow_runs", {
    description: "Read recent workflow runs; does not dispatch workflows.",
    inputSchema: z.object({ repository: z.string().default(ALLOWED_REPOSITORY), branch: z.string().optional() })
  }, async ({ repository, branch }) => {
    assertRepository(repository);
    const query = branch ? "?branch=" + encodeURIComponent(branch) + "&per_page=30" : "?per_page=30";
    const { data } = await github(token, repoPath(repository, "/actions/runs" + query));
    return resultText((data.workflow_runs || []).map((run) => ({ id: run.id, name: run.name, head_branch: run.head_branch, head_sha: run.head_sha, status: run.status, conclusion: run.conclusion, created_at: run.created_at, html_url: run.html_url })));
  });
  return server;
}

async function handle(request) {
  const url = new URL(request.url);
  if (url.pathname === "/health" && request.method === "GET") return Response.json({ status: "ok", service: "palang-partner-mcp", auth: "required-for-mcp" });
  if (url.pathname !== "/mcp") return new Response("Not Found", { status: 404 });
  if (!["POST", "GET", "DELETE"].includes(request.method)) return new Response("Method Not Allowed", { status: 405 });

  const publicOrigin = process.env.PUBLIC_ORIGIN;
  if (!publicOrigin) return new Response("Service not configured", { status: 503 });
  if (url.host !== new URL(publicOrigin).host) return new Response("Invalid host", { status: 400 });
  const origin = request.headers.get("origin");
  if (origin && origin !== publicOrigin) return new Response("Origin not allowed", { status: 403 });

  let token;
  let actor;
  try {
    token = parseBearer(request.headers.get("authorization"));
    actor = await authenticate(token);
  } catch (error) {
    const status = error.message === "OWNER_IDENTITY_MISMATCH" ? 403 : ((error.status === 401 || error.message === "BEARER_TOKEN_REQUIRED") ? 401 : 403);
    return new Response("Unauthorized", { status, headers: { "www-authenticate": 'Bearer realm="Palang Partner MCP"' } });
  }
  try {
    return await createMcpHandler(() => buildServer(token, actor))(request);
  } catch {
    return new Response("MCP request failed", { status: 500 });
  }
}

const httpServer = createServer(async (incoming, outgoing) => {
  try {
    const host = incoming.headers.host || "";
    const scheme = process.env.TRUST_PROXY === "1" ? (incoming.headers["x-forwarded-proto"] || "https") : "http";
    const url = scheme + "://" + host + (incoming.url || "/");
    const hasBody = !["GET", "HEAD"].includes(incoming.method || "GET");
    const headers = new Headers();
    for (const [name, value] of Object.entries(incoming.headers)) {
      if (!value || ["connection", "transfer-encoding", "keep-alive", "upgrade", "host"].includes(name)) continue;
      headers.set(name, Array.isArray(value) ? value.join(", ") : value);
    }
    const request = new Request(url, { method: incoming.method, headers, ...(hasBody ? { body: Readable.toWeb(incoming), duplex: "half" } : {}) });
    const response = await handle(request);
    outgoing.writeHead(response.status, Object.fromEntries(response.headers.entries()));
    if (response.body) Readable.fromWeb(response.body).pipe(outgoing);
    else outgoing.end();
  } catch {
    if (!outgoing.headersSent) outgoing.writeHead(500, { "content-type": "text/plain; charset=utf-8" });
    outgoing.end("Internal Server Error");
  }
});
const port = Number(process.env.PORT || 8080);
httpServer.listen(port, "0.0.0.0", () => process.stdout.write("Palang Partner MCP listening on " + port + "\n"));

export { httpServer };
