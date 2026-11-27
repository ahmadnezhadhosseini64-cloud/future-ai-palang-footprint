import test from "node:test";
import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import { createServer } from "node:net";
import { fileURLToPath } from "node:url";

async function freePort() {
  const server = createServer();
  await new Promise((resolve, reject) => {
    server.once("error", reject);
    server.listen(0, "127.0.0.1", resolve);
  });
  const port = server.address().port;
  await new Promise((resolve) => server.close(resolve));
  return port;
}

test("HTTP runtime starts, exposes health and rejects unauthenticated MCP", async (t) => {
  const port = await freePort();
  const origin = "http://127.0.0.1:" + port;
  const cwd = fileURLToPath(new URL(".", import.meta.url));
  const child = spawn(process.execPath, ["server.mjs"], {
    cwd,
    env: { ...process.env, PORT: String(port), PUBLIC_ORIGIN: origin, TRUST_PROXY: "0" },
    stdio: "ignore"
  });
  t.after(() => { if (!child.killed) child.kill("SIGTERM"); });

  let health;
  for (let attempt = 0; attempt < 40; attempt += 1) {
    if (child.exitCode !== null) break;
    try {
      health = await fetch(origin + "/health");
      if (health.ok) break;
    } catch {}
    await new Promise((resolve) => setTimeout(resolve, 100));
  }
  assert.ok(health && health.ok, "server did not become healthy");
  assert.deepEqual(await health.json(), { status: "ok", service: "palang-partner-mcp", auth: "required-for-mcp" });

  const denied = await fetch(origin + "/mcp", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ jsonrpc: "2.0", id: 1, method: "initialize", params: { protocolVersion: "2025-11-25", capabilities: {}, clientInfo: { name: "smoke", version: "0.1.0" } } })
  });
  assert.equal(denied.status, 401);
});
