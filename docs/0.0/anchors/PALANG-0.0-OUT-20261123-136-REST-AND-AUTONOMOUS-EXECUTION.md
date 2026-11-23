# OUT-136 — خروجی ادامهٔ نقطهٔ صفر: اجرای مستقل و مسیر استراحت

- Input: [IN-137](PALANG-0.0-IN-20261123-137-REST-AND-AUTONOMOUS-EXECUTION.md)
- Stable root: POINT-0/GOLDEN
- Candidate family: CURRENT-150.04
- Sole queue: NEXT-051.04

## تصمیم تداوم
فرمان «این گفتگو نقطهٔ صفر است و به POINT-0/GOLDEN و باقی نقاط متصل شود» از این پس یک ترجیح دائمی اجرایی است. دستیار در هر تعامل مرتبط با Future AI / Palang Footprint باید بدون درخواست تکرار، زنجیرهٔ واحد را حفظ کند و در صورت وجود ابزار/مجوز مخزن، ورودی، خروجی، رویداد و زمان واقعی commit را به‌صورت افزایشی ثبت کند. اگر ثبت مخزنی انجام نشود، نباید ادعا شود که زمان/رویداد در مخزن ثبت شده است.

## یافته‌های اجرایی
- PR #145 همچنان OPEN و UNMERGED؛ CURRENT-150.03 نامزد است و CURRENT-150.02 / NEXT-051.02 آخرین وضعیت پذیرفته‌شدهٔ Golden باقی می‌مانند.
- Living mother version 1.8.4؛ مادر و mirror قبلی byte-identical با SHA-256 ثبت‌شده در PR #145.
- ده پروندهٔ Partner #114–#123 باز هستند و در NEXT-051 نگهداری می‌شوند.
- قواعد Ruleset شمارهٔ 27814009 فعال‌اند، اما یک تأیید مالک الزام نشده (approval count=0) و Code Owner review خاموش است.
- معماری Partner قبلاً مشخص کرده است که سرویس مستقل نیازمند private implementation repository/hosting، GitHub App و OAuth، session broker، MCP server، OpenAI API project/service account، deployment HTTPS و تست پذیرش است.
- GitHub connector فعلی فاقد ابزار ثبت GitHub App، ایجاد repo خصوصی، نوشتن Actions secrets/variables، dispatch workflow، تغییر Ruleset و provisioning/deployment است. بنابراین این موارد بدون ابزار/دسترسی جدید قابل ادعای تکمیل نیستند.
- راهکار ساده‌تر برای کارهای دوره‌ای: Scheduled Tasks/Automations با زمان‌بندی روزانه/هفتگی؛ این قابلیت بیدارشدن در زمان مقرر است، نه تفکر پیوسته یا پردازش نامحدود در پس‌زمینه. زمان دقیق تکرارشونده تضمین نمی‌شود؛ زمان‌بندی منعطف است.
- «Dots» می‌تواند گزینهٔ عامل همیشه‌فعال باشد، اما دسترسی/واجدشرایط بودن این حساب و اتصال ابزارها باید از Help Center بررسی شود؛ در این ثبت فعال بودن آن ادعا نمی‌شود.

## وضعیت
این خروجی یک ثبت کاندید روی شاخهٔ کاری است. هیچ‌یک از گیت‌های owner-only، provisioning، deployment، independent-host recovery یا ادغام Golden با این ثبت بسته نمی‌شود.

## 10-item Partner triage and simpler implementation candidates

The ten issues are separate acceptance gates, not ten tasks that all require the owner to do everything manually.

| Issue | Work package | Current execution boundary |
|---|---|---|
| #114 | Private Partner source repository + HTTPS host | Owner must create/authorize destination; assistant can prepare source and deployment config after target exists. |
| #115 | GitHub App + OAuth | App registration and installation are owner-side; callback depends on real host URL. |
| #116 | OAuth callback/session broker | Source design and tests can be prepared; secure secret/session deployment needs host. |
| #117 | MCP tool server | Consider GitHub's maintained remote MCP server for ordinary GitHub operations; retain a thin custom broker only for owner-specific privileged actions and approval/audit policy. |
| #118 | OpenAI API project/service account | Owner must create project/service account and securely store its key; do not paste key into chat. |
| #119 | HTTPS deployment/health checks | Cloudflare Workers is a candidate managed host; deployment and account authorization remain owner-side. |
| #120 | Trusted bot PR promotion | Assistant can prepare workflow and tests; App identity/install and owner approval remain prerequisites. |
| #121 | Main approval gate/principal audit | Read-only ruleset evidence available; settings change and collaborator/App/deploy-key audit need owner administration UI/API access. |
| #122 | Private owner-only RAHM | Owner must create the private repository; assistant can prepare its schema, policies and tests. |
| #123 | RAHM→CHILD and clean-host recovery | Test harness can be prepared; actual independent host and private RAHM access are required for acceptance. |

### Lowest-complexity candidate architecture (not yet selected as deployed)
1. Keep the current public MASTER and existing Golden governance flow unchanged.
2. Use a separate private Partner implementation repository.
3. Evaluate Cloudflare Workers as the managed HTTPS runtime: official Cloudflare docs provide a remote MCP server template, OAuth authorization components, and durable bindings such as D1/KV. This may avoid managing a conventional server/VM.
4. For ordinary GitHub operations, evaluate GitHub's official remote MCP endpoint with explicit OAuth scopes and tool allowlisting. This could eliminate much of a bespoke GitHub MCP implementation. Keep owner-only repository creation, secret writes, Ruleset changes and promotion behind a custom narrow broker or secure owner UI; do not expose broad admin tools to the model.
5. Use an OpenAI API project service account for the deployed application, with its key held only in the hosting secret manager. Do not reuse a personal ChatGPT subscription as an API credential.
6. Where supported, prefer short-lived workload identity/OIDC for deployment access rather than long-lived cloud tokens.
7. Keep per-operation owner approval, immutable audit, read-back and fail-closed behavior.

Official research:
- Cloudflare remote MCP server: https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/
- Cloudflare MCP OAuth authorization: https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/
- GitHub remote MCP and toolsets: https://docs.github.com/en/copilot/concepts/customizations/mcp
- GitHub App registration and OAuth callback: https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app
- OpenAI Responses API remote MCP: https://developers.openai.com/api/docs/guides/tools-connectors-mcp
- OpenAI service accounts and API keys: https://developers.openai.com/api/docs/guides/api-keys
- GitHub OIDC: https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-cloud-providers

These are research-backed implementation candidates, not proof that any external service has been created or connected.


## Workflow failure analysis and correction attempt

- Run 45109931516: runtime/schema/chain checks, ZIP build, source-byte read-back and 24 extracted starter tests passed. The failure occurred only at the same-run artifact download step.
- The uploaded artifact was finalized and visible through the GitHub REST artifact listing; the failure is consistent with the action immediate same-run lookup not seeing the artifact at that instant.
- A first correction passed the workflow token explicitly. This was rejected by the existing governance test `test_portable_conformance_release_write_is_owner_controlled`, which intentionally forbids passing `${{ github.token }}` to the download action because the same workflow also has release-write permission.
- The safer correction now uses the public repository exact upload output `artifact-id` and the documented unauthenticated download endpoint for public artifacts, with bounded retries and ZIP integrity checking. It does not pass the broad workflow token to the download action.
- This correction is still pending exact-head CI. Do not mark the artifact round-trip gate PASS until run 45110068180 (or a later run on the final head) completes successfully.


## Issue #21 — first full-tree inventory completed (semantic census still open)

- Exact main commit: `30d1d3b2de09078131fa3c8a0ff7c492a7ab0d7e`; tree SHA: `3beac697b90922a93d1618a869bedd4dab212f73`.
- Recursive tree returned 6,716 entries with `truncated=false`.
- Top-level: evidence 4,708; docs 1,644; checkpoints 39; prototype 34; scripts 36; architecture 45; tests 28; .github 23; provenance 25.
- Targeted path families: 644 entries across docs/0.0, behavior trace, architecture lessons, behavior observatory, behavior-hunter, haif-runtime, tests/rahm and starter prototype.
- Issue #21 was updated with this exact partial evidence and remains OPEN. This is a complete path inventory for that exact tree, not a completed semantic source/rule census; content extraction, Git history, duplicate identity adjudication and rule→component→test mapping remain open.


## Exact-head CI receipt — successful artifact round-trip correction

- Portable RAHM Conformance run `45110219381` completed SUCCESS on tested candidate SHA `cfac0057832f3116d94cddc11294427af55dd063`.
- Living Architecture Audit run `45110219361` completed SUCCESS on the same tested SHA.
- Runtime, schema fixtures, host registry, IN/OUT chain equivalence, manifest SHA inventory, RAHM archive build, starter package tests, same-identity ZIP rebuild, exact artifact-ID download, artifact receipt verification and downloaded ZIP extraction/tests all passed.
- The artifact download issue was resolved by using the exact upload `artifact-id`, GitHub REST API download with the workflow token limited to GitHub API use, bounded retries, then ZIP verification. The governance test also passed; the token was not passed as a generic `github-token` input to the download action.
- Durable release refresh was SKIPPED because this was a pull-request event. Real independent-host acceptance remains NOT RUN. Later documentation-only updates for Issue #21 have moved the branch head beyond this tested SHA; exact latest-head audit remains required before promotion.


## Issue #21 — targeted family and repeated-basename screen

From the same exact main tree: docs/0.0/anchors 579 blobs; BEHAVIOR-TRACE 558; ARCHITECTURE-LESSONS 20; BEHAVIOR-OBSERVATORY 9; behavior-hunter 13; haif-runtime 3; tests/rahm 5; portable starter prototype 23. A filename-only screen found 21 repeated-basename groups: 17 groups with different Git blob SHAs and 4 byte-identical groups. This is not an identity-collision conclusion: README.md/index.html are naturally repeated names; other pairs require source authority and semantic comparison. No files were changed/deleted by this screen. Issue #21 updated and remains OPEN.
