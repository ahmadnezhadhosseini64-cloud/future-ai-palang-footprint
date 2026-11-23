# NEXT-051.04 — اجرای مستقل و بررسی ساده‌ترین مسیرهای تکمیل

- Stable queue: NEXT-051
- Revision: 051.04
- Status: ACTIVE / LIVING / GOLDEN-BRANCH-CANDIDATE
- Parent: NEXT-051.03
- Current: CURRENT-150.04
- Input: IN-137
- Output: OUT-136
- Event: EVT-0324
- Root: POINT-0/GOLDEN

## Priority 1 — exact candidate and repository integrity
1. Re-read PR #145 diff and exact-head checks; identify any stale references or regressions.
2. Keep mother 1.8.4 authoritative and preserve canonical ZIP identity.
3. Run exact-head audit/conformance after any source changes; read back every changed file.
4. Keep CURRENT-066/CURRENT-150 ambiguity open until deterministic evidence resolves it.

## Priority 2 — ten Partner dossiers (#114–#123)
- #114 private service repository + HTTPS hosting.
- #115 GitHub App registration/installation and owner OAuth.
- #116 OAuth callback, CSRF/state/PKCE, encrypted owner session/token lifecycle.
- #117 remote MCP server and least-privilege GitHub tools.
- #118 OpenAI API project, service account and secure Responses API runtime.
- #119 deployment, HTTPS endpoint, health checks and release pipeline.
- #120 owner-controlled promotion workflow and bot-authored PR route.
- #121 main approval gate and repository-principal audit.
- #122 private owner-only RAHM repository and read/export boundary.
- #123 synthetic RAHM→CHILD, clean-host recovery and isolation acceptance.

For each issue: separate source-code work the assistant can prepare from provider-side actions requiring owner sign-in, secrets, billing, app registration, or settings access. Use official docs and the least-complex managed route. Keep every issue OPEN until its own acceptance evidence exists.

## Priority 3 — owner-dependent actions and simpler routes
- Identify exact UI-only steps, prerequisites, and secure handoff instructions for private repo creation, GitHub App registration, OpenAI API project/service account, and Ruleset approval configuration.
- Do not request credentials in chat. Prefer owner-side secure UI and minimal permissions.
- Investigate whether an existing managed host or supported deployment integration can replace bespoke infrastructure, without assuming account access.

## Priority 4 — Issue #20 and #21
- #20: advance local runtime, live-capture design, and deterministic test harness; do not claim automatic ChatGPT capture or independent recovery without direct proof.
- #21: deterministic semantic census, parent-edge and identity collision triage; preserve quarantined duplicates and unresolved ambiguity.

## Priority 5 — scheduled execution
- Offer a bounded daily/weekly/monthly scheduled review when owner supplies a preferred schedule.
- A scheduled run is not continuous background reasoning. Report each run's concrete work, evidence, blockers and next steps.
- No task is scheduled until a time/frequency is provided.

## Acceptance discipline
Documented ≠ implemented; implemented ≠ deployed; deployed ≠ tested; tested ≠ merged; merged ≠ released; package conformance ≠ independent-host recovery. No MASTER write, bypass, auto-merge, or host write path.
