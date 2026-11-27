import test from "node:test";
import assert from "node:assert/strict";
import { once } from "node:events";

function decodeResponse(text, contentType) {
  if ((contentType || "").includes("application/json")) return JSON.parse(text);
  const dataLine = text.split(/\r?\n/).find((line) => line.startsWith("data:"));
  if (!dataLine) throw new Error("MCP_RESPONSE_DATA_NOT_FOUND");
  return JSON.parse(dataLine.slice(5).trim());
}

test("MCP initialize and tools/list work with a mocked verified owner identity", async (t) => {
  const previousFetch = globalThis.fetch;
  const previousPort = process.env.PORT;
  const previousOrigin = process.env.PUBLIC_ORIGIN;
  const previousProxy = process.env.TRUST_PROXY;
  process.env.PORT = "0";
  process.env.PUBLIC_ORIGIN = "http://127.0.0.1";
  process.env.TRUST_PROXY = "0";
  globalThis.fetch = async (input, init) => {
    const url = typeof input === "string" ? input : input.url;
    if (url === "https://api.github.com/user") {
      return new Response(JSON.stringify({ login: "ahmadnezhadhosseini64-cloud" }), {
        status: 200,
        headers: { "content-type": "application/json", "x-oauth-scopes": "repo" }
      });
    }
    return previousFetch(input, init);
  };

  const { httpServer } = await import("./server.mjs");
  if (!httpServer.listening) await once(httpServer, "listening");
  const port = httpServer.address().port;
  const origin = "http://127.0.0.1:" + port;
  process.env.PUBLIC_ORIGIN = origin;
  t.after(async () => {
    httpServer.closeAllConnections();
    await new Promise((resolve) => httpServer.close(resolve));
    globalThis.fetch = previousFetch;
    if (previousPort === undefined) delete process.env.PORT; else process.env.PORT = previousPort;
    if (previousOrigin === undefined) delete process.env.PUBLIC_ORIGIN; else process.env.PUBLIC_ORIGIN = previousOrigin;
    if (previousProxy === undefined) delete process.env.TRUST_PROXY; else process.env.TRUST_PROXY = previousProxy;
  });

  const initialize = await fetch(origin + "/mcp", {
    method: "POST",
    headers: { authorization: "Bearer ghp_testtoken", "content-type": "application/json", accept: "application/json, text/event-stream" },
    body: JSON.stringify({ jsonrpc: "2.0", id: 1, method: "initialize", params: { protocolVersion: "2025-11-25", capabilities: {}, clientInfo: { name: "palang-protocol-test", version: "0.1.0" } } })
  });
  assert.equal(initialize.status, 200);
  const initialized = decodeResponse(await initialize.text(), initialize.headers.get("content-type"));
  assert.equal(initialized.jsonrpc, "2.0");
  assert.ok(initialized.result && initialized.result.serverInfo);

  const tools = await fetch(origin + "/mcp", {
    method: "POST",
    headers: { authorization: "Bearer ghp_testtoken", "content-type": "application/json", accept: "application/json, text/event-stream", "mcp-protocol-version": "2025-11-25" },
    body: JSON.stringify({ jsonrpc: "2.0", id: 2, method: "tools/list", params: {} })
  });
  assert.equal(tools.status, 200);
  const listed = decodeResponse(await tools.text(), tools.headers.get("content-type"));
  const names = (listed.result?.tools || []).map((tool) => tool.name);
  assert.equal(names.length, 10);
  assert.ok(names.includes("github_whoami"));
  assert.ok(names.includes("github_create_branch"));
  assert.ok(names.includes("github_create_pull_request"));
});
