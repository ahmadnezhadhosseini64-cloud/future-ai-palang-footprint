export const OWNER_LOGIN = "ahmadnezhadhosseini64-cloud";
export const ALLOWED_REPOSITORY = "ahmadnezhadhosseini64-cloud/future-ai-palang-footprint";
export const COPY1_BRANCH = "palang-safe-copy-1-baseline-20261126";
export const COPY2_BRANCH = "palang-safe-copy-2-test-20261126";

export function assertOwner(login) {
  if (login !== OWNER_LOGIN) throw new Error("OWNER_IDENTITY_MISMATCH");
  return true;
}
export function assertRepository(repository) {
  if (repository !== ALLOWED_REPOSITORY) throw new Error("REPOSITORY_NOT_ALLOWLISTED");
  return true;
}
export function assertBranchReadable(branch) {
  if (typeof branch !== "string" || !branch.trim()) throw new Error("INVALID_BRANCH");
  return true;
}
function isValidPartnerBranch(name) {
  return typeof name === "string"
    && /^palang-partner\/[a-z0-9][a-z0-9._/-]{2,70}$/.test(name)
    && !name.includes("..") && !name.endsWith("/") && !name.includes("//");
}
export function assertBranchCreatable(name, base) {
  if (base !== COPY2_BRANCH) throw new Error("BRANCH_BASE_MUST_BE_COPY2");
  if (!isValidPartnerBranch(name)) throw new Error("INVALID_PARTNER_BRANCH_NAME");
  return true;
}
export function assertWritableBranch(branch) {
  if (branch === "main" || branch === COPY1_BRANCH || branch === COPY2_BRANCH) throw new Error("DIRECT_WRITE_TO_REFERENCE_BRANCH_FORBIDDEN");
  if (!isValidPartnerBranch(branch)) throw new Error("WRITE_REQUIRES_PARTNER_WORKING_BRANCH");
  return true;
}
export function assertPullRequestTargets(head, base) {
  if (!isValidPartnerBranch(head)) throw new Error("PR_HEAD_MUST_BE_PARTNER_BRANCH");
  if (base !== COPY1_BRANCH) throw new Error("PR_BASE_MUST_BE_COPY1");
  return true;
}
export function assertSafePath(path) {
  if (typeof path !== "string" || !path.trim() || path.startsWith("/") || path.includes("\\")) throw new Error("INVALID_REPOSITORY_PATH");
  const parts = path.split("/");
  if (parts.some((part) => !part || part === "." || part === "..")) throw new Error("INVALID_REPOSITORY_PATH");
  const lower = path.toLowerCase();
  if (/(^|\/)(\.env($|\.)|secrets?($|\.)|credentials?($|\.)|.*\.(pem|key|p12|pfx))/.test(lower)) throw new Error("SENSITIVE_PATH_FORBIDDEN");
  if (lower.includes("rahm")) throw new Error("PRIVATE_RAHM_PATH_FORBIDDEN");
  return true;
}
export function parseBearer(header) {
  if (typeof header !== "string") throw new Error("BEARER_TOKEN_REQUIRED");
  const match = /^Bearer\s+([A-Za-z0-9_\-\.]+)$/i.exec(header.trim());
  if (!match) throw new Error("BEARER_TOKEN_REQUIRED");
  return match[1];
}

export function assertPartnerBranchComparison(status) {
  if (status !== "ahead" && status !== "identical") throw new Error("PARTNER_BRANCH_NOT_DERIVED_FROM_CURRENT_COPY2");
  return true;
}
