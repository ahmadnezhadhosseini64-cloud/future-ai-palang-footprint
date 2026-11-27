import test from "node:test";
import assert from "node:assert/strict";
import {
  OWNER_LOGIN, ALLOWED_REPOSITORY, COPY1_BRANCH, COPY2_BRANCH,
  assertOwner, assertRepository, assertBranchCreatable, assertWritableBranch,
  assertPullRequestTargets, assertSafePath, parseBearer, assertPartnerBranchComparison
} from "./policy.mjs";

test("accepts only the canonical owner and repository", () => {
  assert.equal(assertOwner(OWNER_LOGIN), true);
  assert.equal(assertRepository(ALLOWED_REPOSITORY), true);
  assert.throws(() => assertOwner("other-user"), /OWNER_IDENTITY_MISMATCH/);
  assert.throws(() => assertRepository("other/repo"), /REPOSITORY_NOT_ALLOWLISTED/);
});
test("new partner branches must originate from Copy 2", () => {
  assert.equal(assertBranchCreatable("palang-partner/mcp-core-001", COPY2_BRANCH), true);
  assert.throws(() => assertBranchCreatable("palang-partner/mcp-core-001", "main"), /BRANCH_BASE_MUST_BE_COPY2/);
  assert.throws(() => assertBranchCreatable("main", COPY2_BRANCH), /INVALID_PARTNER_BRANCH_NAME/);
  assert.throws(() => assertBranchCreatable("palang-partner/../main", COPY2_BRANCH), /INVALID_PARTNER_BRANCH_NAME/);
});
test("direct writes to main and both safe-copy reference branches are denied", () => {
  for (const branch of ["main", COPY1_BRANCH, COPY2_BRANCH]) {
    assert.throws(() => assertWritableBranch(branch), /DIRECT_WRITE_TO_REFERENCE_BRANCH_FORBIDDEN/);
  }
  assert.equal(assertWritableBranch("palang-partner/mcp-core-001"), true);
  assert.throws(() => assertWritableBranch("feature/other"), /WRITE_REQUIRES_PARTNER_WORKING_BRANCH/);
  assert.throws(() => assertWritableBranch("palang-partner/../main"), /WRITE_REQUIRES_PARTNER_WORKING_BRANCH/);
});
test("PRs can only propose partner branches to Copy 1, never main", () => {
  assert.equal(assertPullRequestTargets("palang-partner/mcp-core-001", COPY1_BRANCH), true);
  assert.throws(() => assertPullRequestTargets("palang-partner/mcp-core-001", "main"), /PR_BASE_MUST_BE_COPY1/);
  assert.throws(() => assertPullRequestTargets(COPY2_BRANCH, COPY1_BRANCH), /PR_HEAD_MUST_BE_PARTNER_BRANCH/);
});
test("repository paths reject traversal, secrets, keys and RAHM", () => {
  assert.equal(assertSafePath("prototype/palang-partner/server.mjs"), true);
  for (const path of ["../x", "a/../x", ".env", "config/credentials.json", "tls/server.pem", "private/RAHM/export.md", "/etc/passwd", "a\\b"]) {
    assert.throws(() => assertSafePath(path));
  }
});
test("bearer parser rejects missing and malformed authorization", () => {
  assert.equal(parseBearer("Bearer ghp_exampleToken123"), "ghp_exampleToken123");
  assert.throws(() => parseBearer(undefined), /BEARER_TOKEN_REQUIRED/);
  assert.throws(() => parseBearer("Basic abc"), /BEARER_TOKEN_REQUIRED/);
});

test("partner working branches must be current descendants of Copy 2", () => {
  assert.equal(assertPartnerBranchComparison("ahead"), true);
  assert.equal(assertPartnerBranchComparison("identical"), true);
  for (const status of ["behind", "diverged", "unknown"]) {
    assert.throws(() => assertPartnerBranchComparison(status), /PARTNER_BRANCH_NOT_DERIVED_FROM_CURRENT_COPY2/);
  }
});
