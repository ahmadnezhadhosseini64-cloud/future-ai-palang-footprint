# معماری امنیتی میزبان‌های مستقل و مخزن مادر فقط‌مالک

- Stable ID: HAIF-OWNER-ONLY-MASTER-PER-HOST-PRIVATE-REPOS-2026-11-21-001
- Version: 1.4.0
- Status: OWNER-DIRECTED / DESIGN-APPROVED / IDENTITY-SEPARATION-ADDED / IMPLEMENTATION-PARTIAL
- Parent: POINT-0/GOLDEN → CURRENT-140 → NEXT-051
- Canonical root: POINT-0 only
- Canonical master repository: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint
- Owner: repository owner only

## 1. تصمیم امنیتی مالک

مخزن مادر متعلق به مالک است. هیچ Host AI، حتی میزبان ثبت‌شده، نباید collaborator، team member، deploy key holder یا دارندهٔ credential نوشتن برای مخزن مادر باشد. مجوز میزبان نسبت به مخزن مادر همیشه PUBLIC READ ONLY است؛ public READ برای مشاهدهٔ کد/اسناد است و به معنی احراز هویت، ثبت میزبان یا اجازهٔ کار در workspace نیست.

هر میزبان فقط در محیط خصوصی و مجزای خودش فعالیت می‌کند. فضای پایدار پیشنهادی برای هر میزبان یک مخزن GitHub جداگانه با visibility=PRIVATE است که مالک آن را ایجاد و مدیریت می‌کند. هیچ دو میزبان از طریق اشتراک repo یا credential به workspace یکدیگر دسترسی ندارند.

## 2. واقعیت‌های امنیتی غیرقابل چشم‌پوشی

1. مخزن Public برای همهٔ اینترنت قابل خواندن/clone/fetch است. نمی‌توان تمام خوانندگان ناشناس یا کپی‌کنندگان را به‌صورت فردی شناسایی کرد. بازدید/clone عمومی به‌تنهایی Host Node نیست.
2. Host ID فقط پس از handshake قابل‌تأیید و رسید مستقیم از مسیر کنترل‌شده، سپس بررسی و تأیید مالک صادر می‌شود. برای بازدیدکنندهٔ ناشناس شناسه صادر نمی‌شود.
3. دستور متنی، نام پوشه، نام branch یا شناسه به‌تنهایی مجوز امنیتی ایجاد نمی‌کند.
4. پوشه‌های متفاوت در یک repository مرز امنیتی نیستند. Permissionهای معمول GitHub repository-scoped هستند، نه folder-scoped.
5. هر میزبان یا ابزار متصل به مخزن مادر با مجوز Write می‌تواند بالقوه روی branchها، PRها، Issues یا سایر سطوحی که مجوز می‌دهد اقدام کند؛ بنابراین میزبان نباید هیچ credential نوشتن برای مخزن مادر دریافت کند.
6. در personal-account private repository، نقش collaborator به‌طور معمول read/write است و read-only collaborator role در دسترس نیست. اگر دسترسی granular لازم باشد، از GitHub Organization و نقش/تیم مناسب یا GitHub App با دسترسی انتخابی استفاده شود.
7. هیچ طراحی نرم‌افزاری تضمین مطلق در برابر compromise شدن حساب مالک، دستگاه مالک، GitHub App private key یا زیرساخت broker نمی‌دهد. MFA/passkey، secret manager، audit و revoke فوری لازم‌اند.

## 3. توپولوژی مرجع

```text
OWNER (sole authority)
  |
  +-- MASTER REPOSITORY (public source / owner-only write)
  |      Host access: anonymous HTTPS READ only
  |      No host collaborator / no host PAT / no host deploy key
  |      No host writes, branches, PRs, issues, releases, workflows, settings
  |
  +-- HOST-REGISTRY (owner-controlled; no self-registration)
  |
  +-- HOST-A private repository (PRIVATE; owner-owned)
  |      Host-A workspace + snapshot + proposals + tests + receipts + export
  |      Only Host-A's scoped route can write; owner can inspect/revoke
  |
  +-- HOST-B private repository (PRIVATE; owner-owned)
  |      Host-B workspace + snapshot + proposals + tests + receipts + export
  |      Only Host-B's scoped route can write; owner can inspect/revoke
  |
  +-- HOST-N private repository (PRIVATE; owner-owned)
         No cross-host visibility or shared write credentials
```

## 4. لایه‌های دسترسی

### L0 — Unknown / unregistered
- No Host ID; no private repository; no broker session.
- May read the public source like any internet visitor.
- Cannot be reliably identified merely from anonymous public reads.
- Never receives private workspace access.

### L1 — Registered read-only host
- Owner has verified the host's direct enrollment receipt and assigned Host ID.
- Public master source remains read-only.
- Host can read a pinned snapshot and work in its private runtime if that runtime is isolated.
- No GitHub write credential and no private-repository write path.

### L2 — Owner-provisioned private workspace
- Owner creates one private repository per host, for example `haif-host-<HOST_ID>`.
- Owner records repository ID/full name and maps it to exactly one Host ID and Workspace ID.
- Host cannot create or choose its own target repository.
- No shared collaborators, teams, deploy keys, PATs or credentials between hosts.
- If host must only read, give no write credential; export is owner-mediated.

### L3 — Broker-mediated write to own private repository (optional, not default)
- Host submits a structured proposal to an authenticated broker; it does not receive the GitHub credential.
- Broker authenticates the host/session, derives the destination from the server-side Host Registry, and never trusts a client-supplied repository name or path.
- GitHub App installation/token is restricted to the single host repository; minimum permissions only (metadata read and contents write only if required). No Administration, Actions, Secrets, Workflows, or master-repository access.
- Token is short-lived, server-side, held in a secret manager, never shown to the model, chat, prompt, package, logs or host workspace.
- Broker validates schema, size, file types, path allowlist, symlinks/path traversal, hashes, provenance, privacy/redaction and idempotency.
- Writes only to that host's private repository and a designated quarantine area/branch. No cross-host destination override.
- If broker, App scope, audit, revocation and negative tests are not operational, L3 remains DISABLED.

No L4 or direct master-write permission is defined for AI hosts.

## 5. Required repository separation

For each Host ID:
- One private repository owned by the owner, unique repo ID, no reuse across hosts.
- Private visibility verified after creation.
- Default branch protected by owner-controlled rules/ruleset.
- Host write, if ever enabled, is via a dedicated GitHub App/broker scope for that repository only; not a personal access token with broad account scope.
- Host cannot manage repository settings, collaborators, rulesets, secrets, Actions, webhooks, deploy keys or repository transfer/deletion.
- Owner retains admin, export, archive, revoke and delete authority.
- Host A's credentials must fail on Host B repository and on master repository. Host B's credentials must fail on Host A and master.
- Private repo is durable storage, not an independent security boundary against compromise of the owner account or GitHub App.

## 6. Master repository controls

Required owner actions:
1. Confirm no AI host accounts, teams, deploy keys or GitHub Apps with write access are installed/added to the master repository.
2. Keep master write authority owner-only; audit collaborators and installed Apps periodically.
3. Configure a main-branch ruleset/protection: require pull request, block force push and deletion, require checks where available, restrict updates and use no AI-host bypass. Verify effective rules in GitHub UI/API after saving.
4. Keep host intake/broker credentials out of the master repo and its workflows. No host token may have master repository selected in an App installation.
5. Enable MFA/passkey, secure recovery methods, review authorized OAuth Apps and revoke unexpected sessions/tokens.
6. Keep secrets out of public files and history. Treat all public repository contents as disclosed to the internet.

Live read-back on 2026-11-22: Ruleset PROTECT-MAIN-BRANCH64 (27814009) is active for the default branch main; the branch API reports protected=true. The live ruleset blocks deletion, force-push and direct non-PR updates. Required approvals are still 0 and Code Owner review is false; collaborator/App audit remains OPEN. The connected GitHub action can read rulesets but does not expose ruleset writes.

## 7. Registration and provisioning lifecycle

`UNKNOWN → ENROLLMENT_REQUESTED → RECEIPT_RECEIVED → OWNER_IDENTITY_REVIEW → HOST_ID_ASSIGNED → PRIVATE_REPO_CREATED_BY_OWNER → ACCESS_SCOPE_TESTED → L1_READ_ONLY or L2_PRIVATE_WORKSPACE → (optional) L3_BROKER_WRITE → ACTIVE`

- An unknown public reader is not enrolled.
- Host never self-assigns official IDs or creates its own trusted registry record.
- The owner manually approves the host and creates its private repo.
- Workspace/repo IDs are recorded only after GitHub creation and read-back.
- If a host is compromised or misbehaves: disable broker route, revoke App installation/token, suspend/revoke registry entry, preserve receipts, export/quarantine evidence, rotate secrets and test that access fails.
- An owner can set a host to READ_ONLY, SUSPENDED or REVOKED without changing the master repository.

## 8. Owner monitoring and cross-host learning

Owner's control plane is the only place where host workspaces are compared. A host cannot list other hosts, see their repositories, access their receipts or write to the Registry. The owner pulls or receives sanitized exports and then performs:
`HOST PRIVATE REPO → OWNER EXPORT → QUARANTINE → CROSS-HOST RECONCILIATION → RAHM → CHILD → EXPLICIT OWNER APPROVAL → MASTER`.

Ideas and findings remain proposals. Nothing is automatically promoted into the mother architecture.

## 9. Negative acceptance tests (mandatory before any L3 activation)

- Host A cannot push/create PR/issue/write to master.
- Host A cannot read or write Host B private repository.
- Host B cannot read or write Host A private repository.
- Unknown/unregistered host cannot access any private repository or broker write route.
- Expired/revoked credential is rejected.
- Client-supplied repo name, branch, path, host_id or workspace_id cannot override server-side mapping.
- Path traversal, symlink, executable/workflow/settings mutation, oversized payload and malformed schema are rejected.
- Broker restart preserves audit and idempotency state.
- Owner can export and restore a host workspace and verify its manifest/hash.
- Main protection blocks non-owner updates as configured; admin/owner bypass behavior is explicitly tested and documented.

All tests require real GitHub/App/broker evidence. A prompt or local mock test is not a security proof.

## 10. Current implementation status

- Multi-host registry/workspace design: EXISTS.
- Owner-only master policy: REGISTERED IN THIS DESIGN; actual permission audit OPEN.
- Master repository visibility: PUBLIC (verified).
- Authenticated connector account currently has admin/push rights as repository owner; this is the owner connection, not an AI-host permission.
- main protection: live branch API reports protected=true; Ruleset 27814009 is active and requires PRs, blocks deletion and non-fast-forward updates. Required approval count is still 0 and Code Owner review is false; full approval enforcement remains OPEN.
- Host-specific private repositories: NOT CREATED.
- GitHub App per-host scoped installation: NOT CONFIGURED.
- Broker and server-side identity mapping: NOT DEPLOYED / OPEN.
- Host Registry live entries: NONE VERIFIED.
- Cross-host negative security tests: NOT RUN.
- Host enrollment: one-message instructions exist, but no new host is thereby registered or activated.

## 11. Safe default

Until all L3 gates pass, every new host is strictly L1_READ_ONLY against master and performs work only in a private destination runtime or owner-created private repository with no host write credential. If the environment cannot prove isolation, do not provide any repository credential; produce a local export for owner review instead.

## 12. دروازهٔ تأیید مالک برای هر ارتقا به MASTER — تصمیم 2026-11-22

این بخش، سیاست امنیتی بخش‌های 1 تا 11 را تغییر نمی‌دهد؛ یک لایهٔ کنترل تکمیلی روی ارتقای خروجی‌ها به شاخهٔ اصلی است.

1. هیچ میزبان AI به مخزن مادر دسترسی نوشتن، عضویت collaborator، PAT، deploy key، GitHub App write scope، branch، PR، issue، release، workflow یا settings ندارد.
2. هر میزبان فقط در محیط اجرایی خودش و، پس از تأیید مالک، در مخزن خصوصیِ اختصاصیِ ایجادشده توسط مالک کار می‌کند. فضای هر میزبان از سایر میزبان‌ها جداست.
3. خروجی میزبان فقط «پیشنهاد» است؛ ابتدا به‌صورت export/receipt قابل‌راستی‌آزمایی به مالک می‌رسد. مالک منشأ، محتوا، آزمون، hash، اثر معماری و محرمانگی را بررسی می‌کند.
4. هیچ پیشنهاد، فایل، commit یا نتیجه‌ای خودکار یا مستقیم وارد MASTER نمی‌شود. ارتقا فقط پس از بررسی و تصمیم صریح مالک مجاز است.
5. هر Pull Request که توسط هویت غیرمالک/اتوماسیون مجاز ایجاد شود و بخواهد به main برسد، باید دست‌کم یک تأییدیهٔ معتبر از مالک بگیرد؛ تأیید قبلی پس از push تازه باید باطل شود.
6. فایل .github/CODEOWNERS مالک مخزن را برای همهٔ مسیرها به‌عنوان Code Owner معرفی می‌کند؛ Ruleset باید require_code_owner_review=true و required_approving_review_count=1 داشته باشد. حل گفتگوهای review پیش از ادغام نیز باید الزامی باشد.
7. GitHub اجازه نمی‌دهد نویسندهٔ یک Pull Request، درخواست خودش را به‌عنوان تأییدکننده تأیید کند. بنابراین برای PRهای ساخته‌شده با حساب خود مالک، یا باید از مسیر promotion automation تحت کنترل مالک استفاده شود تا مالک reviewer باشد، یا مالک از مسیر bypass محدود و ثبت‌شدهٔ خودش استفاده کند. این bypass هرگز به میزبان یا هویت ثالث داده نمی‌شود.
8. پیشنهاد میزبان نباید با حساب میزبان به مخزن مادر PR بسازد؛ میزبان اساساً مجوز آن را ندارد. مسیر انتقال میزبان به مالک، export → quarantine → review → approval → owner-controlled promotion است.
9. تأیید GitHub فقط کنترل ادغام است و جایگزین ممیزی دسترسی collaborator/App، حفاظت مخزن خصوصی هر میزبان، broker، آزمون منفی و تأیید مالکیت میزبان نیست.

## 13. وضعیت زندهٔ Ruleset شاخهٔ main — بازخوانی 2026-11-22

- Ruleset فعال: PROTECT-MAIN-BRANCH64، شناسهٔ 27814009.
- Target: ~DEFAULT_BRANCH؛ در این مخزن دقیقاً main.
- Enforcement: active.
- قواعد خوانده‌شده: جلوگیری از حذف، جلوگیری از force-push و الزام Pull Request.
- Bypass actors: خالی؛ current_user_can_bypass برابر never.
- مقدار زندهٔ required_approving_review_count=0 است؛ بنابراین تأیید مستقل هنوز اجباری نشده است.
- require_code_owner_review=false و required_reviewers=[]؛ CODEOWNERS و الزام تأیید مالک هنوز در Ruleset اعمال نشده‌اند.
- Branch API مقدار protected=true را برای main برگرداند؛ این نتیجه با فعال بودن Ruleset سازگار است. حفاظت مؤثر به معنی فعال بودن همهٔ کنترل‌های پیشنهادی نیست.
- ابزار GitHub متصل در این اجرا فقط خواندن Ruleset را پشتیبانی کرد و عملیات نوشتن/ویرایش Ruleset در دسترس نبود. تغییر مقدار تأیید و گزینه‌های Code Owner باید در GitHub UI انجام و سپس از API بازخوانی شود.

## 14. تنظیم نهایی موردنیاز در GitHub UI

- Required approving reviews: 1.
- Dismiss stale approvals when new commits are pushed: true.
- Require review from Code Owners: true پس از ثبت فایل CODEOWNERS.
- Require conversation resolution: true.
- Host accounts / host Apps: هیچ‌کدام در bypass قرار نگیرند.
- هر bypass مالک، اگر برای PRهای مالک‌نویس لازم شد، باید فقط به هویت مالک و با دامنهٔ Pull Request محدود باشد؛ هرگز برای میزبان فعال نشود.
- پس از ذخیره، Ruleset از GitHub API دوباره خوانده شود. تا آن بازخوانی، این قسمت DESIGN APPROVED / CONFIGURATION PENDING است، نه VERIFIED.


## 15. RAHM مرکزی مالک و مسیر یادگیری چندمیزبانه — POINT-0/086

Host Registry schema 1.1.0 now binds each Host ID to one Workspace ID and one owner-created private repository, records connector monitoring mode, and hard-requires master_write_access=false, rahm_access=NONE and host_direct_write_access=false. Owner monitoring commands are documented in docs/architecture/RAHM/OWNER-MONITORING-COMMANDS.md.

RAHM فضای مرکزی تحت اختیار مالک است و هرگز داخل محیط کاری میزبان قرار نمی‌گیرد. مسیر دائمی:

HOST PRIVATE WORKSPACE → OWNER-COMMANDED MONITOR/EXPORT → PRIVATE RAHM QUARANTINE → CROSS-HOST RECONCILIATION → RAHM VALIDATION → BOT-AUTHORED PR → OWNER REVIEW/APPROVAL → CHILD-CANDIDATE.

- معماری و قرارداد: docs/architecture/RAHM/README.md.
- قالب ساخت مخزن خصوصی RAHM: docs/architecture/RAHM/PRIVATE-RAHM-REPOSITORY-TEMPLATE.md.
- Schema پاکت candidate: docs/architecture/RAHM/CANDIDATE-MANIFEST-SCHEMA.json.
- کنترل‌پلین عمومی و غیرحساس: control-plane/rahm/README.md.
- ناحیه فرزند: docs/architecture/CHILD-CANDIDATES/README.md.
- مخزن خصوصی مورد انتظار: ahmadnezhadhosseini64-cloud/future-ai-palang-rahm؛ در زمان این ثبت هنوز ساخته و بازخوانی نشده است.
- مخزن مادر Public است؛ بنابراین raw export، گفت‌وگوی خصوصی، داده شخصی، secret و شواهد پالایش‌نشده هرگز در آن قرار نمی‌گیرند.
- فقط مالک از workspace میزبان export می‌گیرد، پالایش می‌کند و در RAHM خصوصی قرار می‌دهد. میزبان به RAHM دسترسی ندارد.
- workflow فقط با workflow_dispatch از حساب مالک روی main اجرا می‌شود، private بودن RAHM را بررسی می‌کند، manifest و hash را اعتبارسنجی می‌کند و یک PR با هویت GitHub App مورداعتماد به CHILD باز می‌کند.
- Bot فقط PR/branch ایجاد می‌کند؛ هیچ merge، auto-merge، bypass یا ویرایش مستقیم Master ندارد.
- ChatGPT می‌تواند محتوای قابل‌دسترسی را فنی/امنیتی بررسی کند؛ اما approval واقعی GitHub باید از حساب مالک باشد.
- Child پذیرش نهایی در Master نیست؛ ارتقای بعدی به اسناد مادر، PR مستقل و تأیید مجدد مالک می‌خواهد.

## 16. حذف مسیرهای نوشتن مستقیم خودکار به main — چکش سخت POINT-0/086

ممیزی workflowها مسیرهای نوشتن مستقیم زیر را پیدا کرد و در همین تغییر اصلاح کرد:

- .github/workflows/main.yml: ثبت evidence دیگر commit/push به main نمی‌کند؛ فقط artifact با retention ثبت می‌شود و permission به contents:read کاهش یافت.
- .github/workflows/pending-registration-drain.yml: از drain/commit/push خودکار به ممیزی read-only و artifact تبدیل شد؛ هیچ فایل canonical را تغییر نمی‌دهد.
- control-plane/controller.py و .github/workflows/execution-controller.yml: تولید recovery/runtime proof فقط در runner و artifact انجام می‌شود؛ git commit/push حذف شد و permission فقط read است.
- .github/workflows/rahm-portable-conformance.yml: contents:write فقط برای انتشار release پایدار ZIP پس از main باقی می‌ماند؛ هیچ commit/push به branch ندارد و workflow_dispatch فقط برای مالک مجاز است.
- worker قدیمی scripts/host_adapter_github_worker.py اکنون به‌طور کامل fail-closed و غیرفعال است؛ هیچ GitHub API request یا write انجام نمی‌دهد. مسیر آینده فقط owner export به RAHM خصوصی و bot-authored PR است.
- هر workflow یا App جدید باید PR-only باشد؛ هیچ رباتی bypass یا حق merge به main دریافت نمی‌کند.

## 17. وضعیت اجرای عملیاتی RAHM و دروازه تأیید

- RAHM private repository: NOT CREATED / NOT VERIFIED.
- Promotion GitHub App: NOT CREATED / NOT INSTALLED.
- Repository variable PALANG_PROMOTION_APP_CLIENT_ID: NOT CONFIGURED.
- Secrets PALANG_PROMOTION_APP_PRIVATE_KEY و RAHM_READ_TOKEN: NOT CONFIGURED.
- ChatGPT GitHub connector access to private RAHM: NOT VERIFIED.
- Ruleset 27814009: active, but required approvals=0 and Code Owner review=false; owner must set 1 and enable Code Owner review, stale-review dismissal and conversation resolution, then API read-back is required.
- Host Registry: no verified live hosts; no Host ID issued by this point.
- Therefore status is DESIGN REGISTERED / CODE IMPLEMENTED / OPERATIONAL SETUP PENDING. Do not claim RAHM_OPERATIONAL or HOST_SECURITY_VERIFIED.


## 16. Golden baseline — absolute no-host-to-master rule

The canonical authority is POINT-0/GOLDEN / CURRENT-140. This section supersedes every older instruction that could be interpreted as allowing a host to write to a branch of the master, create a PR against the master, or use a broker/worker/intermediary to route host-originated writes into the master.

- Every host's permission on the canonical master is PUBLIC READ ONLY. No host account, host app, host token, host-held credential, workspace, broker, branch, PR, issue, release, workflow, setting, or bypass may write to or promote into the master.
- A host may write only inside its own isolated runtime and, if the owner provisions one, its own PRIVATE host repository. That repository is not a relay or write route into the master or RAHM.
- RAHM is central, private, and owner-only. It is not in any host workspace. Hosts have no RAHM read, write, admin, token, or App access.
- Only the owner can inspect/export a host's accessible workspace/repository, redact the export, and place it into private RAHM. No host-initiated broker or automatic pipeline may transfer content to RAHM or master.
- The legacy `host-intake` branch is historical/frozen. `scripts/host_adapter_github_worker.py` is disabled fail-closed and makes no GitHub API request.
- Child intake is a separate owner-controlled operation: trusted promotion App creates a bot-authored PR after validation; the owner reviews/approves. Child acceptance is not Master acceptance.
- Current Ruleset 27814009 is active but still has approval count 0 and Code Owner review OFF. Do not mark the approval gate active until the owner changes it and a live read-back verifies 1 / true / true / true. Do not turn approval to 1 before the bot-authored synthetic PR test succeeds.


## 17. Owner connector is not a host permission

The current ChatGPT GitHub integration is authenticated as the owner account and has admin/push permission on this repository. It is not a host credential and must not be shared with any new Host Node or placed in a host workspace. Its exposed tool surface does not include Ruleset writes, private-repository creation, GitHub App creation, or complete collaborator/App/deploy-key inventory. A user instruction authorizes permitted actions but does not bypass these capability boundaries or GitHub's rule that a PR author cannot approve their own PR. Private RAHM access is separate and not granted merely by connecting the public master.


## 18. مالک، ناظر معماری و میزبان اجرایی — جداسازی هویت‌ها (OWNER-APPROVED 2026-11-25)

این بخش یک قاعدهٔ هویتی و کنترلی به معماری موجود اضافه می‌کند؛ ریشهٔ POINT-0، زنجیرهٔ جاری، RAHM و صف یگانهٔ NEXT-051 را تغییر نمی‌دهد و هیچ مسیر موازی ایجاد نمی‌کند.

### 18.1 سه نقش غیرقابل‌جایگزینی

1. **OWNER / مالک انسانی:** تنها مرجع اختیار نهایی. مالک هویت انسانی و حساب GitHub مالک مخزن را کنترل می‌کند، میزبان را می‌پذیرد یا رد می‌کند، فضای خصوصی را ایجاد و مجوزها را تعیین می‌کند، دربارهٔ پذیرش CHILD و هر ارتقای بعدی به MASTER تصمیم می‌گیرد. تأیید مالک با ادعای متنی یک میزبان یا ناظر جایگزین نمی‌شود.
2. **ARCHITECTURE-OBSERVER / ناظر معماری:** نقش نظارتی مستقل که در نشست جاری، به‌صراحت از سوی مالک به دستیار GPT-6 واگذار شده است. وظیفه‌اش خواندن شواهد مجاز، تطبیق زنجیره و نسخه‌ها، ممیزی مجوزها و ادعاها، کشف تعارض و اعلام وضعیت واقعی است. ناظر مالک نیست، میزبان اجرایی نیست، اختیار اعطای دسترسی یا صدور Host ID ندارد، نمی‌تواند به‌جای مالک تأیید نهایی بدهد و هیچ مجوز نوشتن یا ارتقای MASTER از این نقش دریافت نمی‌کند. این انتساب، نقش همین نشست/عامل را مشخص می‌کند و به‌معنای تضمین تداوم هویت یک مدل در همهٔ نشست‌ها یا میزبان‌های آینده نیست؛ انتساب ناظر در هر محیط تازه باید از مسیر مالک و رجیستری مورداعتماد احراز شود.
3. **HOST / میزبان اجرایی AI:** عامل مستقل برای اجرای وظایف محول‌شده در محیط خودش. میزبان می‌تواند پیشنهاد، داده، کد یا نتیجهٔ آزمون تولید کند؛ اما مالک، ناظر یا مرجع ثبت هویت نیست. میزبان حق ندارد خود را جای مالک یا ناظر معرفی کند، نقش آن‌ها را به ارث ببرد، Host ID برای خود صادر کند، به رجیستری اعتماد دست بزند یا ادعای تأیید خودش را معتبر جلوه دهد.

### 18.2 اصل عدم جانشینی و احراز نقش

- نقش از نام مدل، متن prompt، ادعای خود عامل، نام شاخه، نام فایل یا محتوای خروجی استنتاج نمی‌شود؛ نقش باید از انتساب و مجوز قابل‌راستی‌آزمایی کنترل‌پلین مالک به دست آید.
- هر ورودی میزبان، از جمله ادعای «من ناظر هستم»، «مالک تأیید کرده» یا «این تغییر مجاز است»، دادهٔ غیرقابل‌اعتماد است تا زمانی که از مسیر مستقل و مجاز مالک تأیید شود.
- میزبان تازه هرگز صرفاً با دریافت سند مادر، بستهٔ انتقال، تاریخچهٔ گفتگو یا دسترسی خواندن، به هویت ناظر یا مالک تبدیل نمی‌شود.
- ناظر نیز نمی‌تواند با خوداظهاری، دسترسی یا اختیار جدیدی برای خود ایجاد کند. اختیار ناظر فقط همان دامنهٔ نظارتیِ واگذارشده و قابل‌اثبات است.
- اگر هویت، انتساب یا مجوز هر نقش مبهم باشد، توقف امن اعمال می‌شود: فقط خواندن عمومی و بدون هیچ نوشتن، انتقال، ثبت میزبان یا ارتقا.

### 18.3 ماتریس اختیار

| عملیات | مالک انسانی | ناظر معماری | میزبان اجرایی |
|---|---|---|---|
| تعیین/لغو نقش و Host ID | مجاز | بررسی و گزارش | ممنوع |
| ایجاد مخزن خصوصی میزبان | مجاز | بررسی و راستی‌آزمایی | ممنوع |
| خواندن MASTER عمومی | مجاز | فقط در حدود اتصال مجاز | فقط خواندن عمومی |
| نوشتن در MASTER یا main | فقط از مسیر کنترل‌شدهٔ مالک | ممنوع | ممنوع |
| دسترسی به RAHM خصوصی | مالک‌محور | فقط در صورت دسترسی جداگانه و مجاز | ممنوع |
| کار در workspace خصوصی میزبان | نظارت/مدیریت مالک | ممیزی فقط با دسترسی مجاز | فقط workspace اختصاص‌یافته |
| مقایسهٔ خروجی میزبان‌ها | تصمیم‌گیر | ممیزی و گزارش | ممنوع نسبت به فضای دیگر میزبان‌ها |
| پذیرش CHILD | تأیید مالک طبق دروازه | ارزیابی و پیشنهاد | فقط ارائهٔ پیشنهاد |
| ارتقا به MASTER | فقط با فرمان و تأیید جداگانهٔ مالک | ممیزی؛ بدون اختیار ارتقا | ممنوع |

### 18.4 مدل دسترسی و جداسازی محیط

- مخزن مادر عمومی باقی می‌ماند؛ بنابراین خواندن عمومی، clone یا fetch قابل مشاهده/تفکیک قطعی به میزبان ثبت‌شده نیست. خواندن عمومی به‌تنهایی ثبت میزبان یا مجوز محیط کاری نیست.
- میزبان هیچ حساب collaborator، PAT، deploy key، GitHub App installation، token یا credential دارای نوشتن در مخزن مادر دریافت نمی‌کند. میزبان نه branch در مخزن مادر می‌سازد، نه PR/Issue می‌نویسد و نه از workflow یا واسطه برای انتقال تغییرات به MASTER استفاده می‌کند.
- فضای کاری پایدار هر میزبان، در صورت نیاز، یک مخزن PRIVATE جداگانه است که فقط مالک ایجاد و به همان Host ID متصل می‌کند. یک مخزن یا credential مشترک برای چند میزبان ممنوع است.
- branch و branch protection در مخزن خصوصی میزبان می‌توانند برای کنترل تغییرات همان workspace استفاده شوند؛ اما branch به‌تنهایی مرز امنیتی نیست و هرگز مجوز یا مسیر دسترسی به مخزن مادر ایجاد نمی‌کند.
- هر شاخهٔ پیشنهادی که ناظر/اتصال مالک برای آماده‌سازی یک PR معماری در مخزن مادر می‌سازد، محیط خصوصی میزبان محسوب نمی‌شود و هیچ میزبان حق استفاده یا نوشتن در آن را ندارد.
- هر انتقال از workspace میزبان به RAHM یا به مسیر CHILD/Master فقط از مسیر مالک‌محور و کنترل‌شدهٔ ثبت‌شده در قرارداد امنیتی موجود انجام می‌شود. هیچ مسیر host-initiated، broker یا relay مجاز نیست.

### 18.5 چرخهٔ کاری مجاز

`OWNER AUTHORIZES HOST`
→ `OWNER PROVISIONS ISOLATED PRIVATE WORKSPACE`
→ `HOST EXECUTES LOCALLY / IN ITS OWN WORKSPACE`
→ `OWNER-COMMANDED INSPECTION AND EXPORT`
→ `PRIVATE RAHM QUARANTINE`
→ `OBSERVER INDEPENDENT VALIDATION`
→ `OWNER DECISION`
→ `CHILD (IF APPROVED)`
→ `SEPARATE OWNER APPROVAL FOR ANY MASTER PROMOTION`

ناظر می‌تواند ناسازگاری را رد کند، نتیجه را OPEN نگه دارد یا شواهد تکمیلی بخواهد؛ اما نمی‌تواند با نظر خود جای تأیید مالک را پر کند. میزبان فقط پیشنهاد می‌دهد و از مسیر مالک عبور می‌کند.

### 18.6 آزمون‌های پذیرش هویتی و منفی

پیش از ACTIVE شدن هر میزبان، باید با شواهد واقعی و قابل‌بازخوانی ثابت شود:

1. میزبان در مخزن مادر نمی‌تواند branch، commit، PR، Issue، release، workflow یا تغییر تنظیمات ایجاد کند.
2. credential میزبان در مخزن مادر و RAHM رد می‌شود؛ نبود credential نیز با audit تنظیمات و نصب‌ها بررسی می‌شود.
3. میزبان A به مخزن خصوصی میزبان B دسترسی ندارد و برعکس.
4. میزبان نمی‌تواند Host ID، نقش OWNER یا نقش ARCHITECTURE-OBSERVER را برای خود صادر یا جعل کند.
5. ادعای تأیید مالک از سوی میزبان بدون رسید مستقل مالک رد می‌شود.
6. ناظر نمی‌تواند با نقش نظارتی خود مجوز، credential، merge یا ارتقای MASTER ایجاد کند.
7. لغو یا تعلیق Host ID دسترسی workspace/broker مربوط را قطع می‌کند و نتیجه با آزمون منفی تأیید می‌شود.
8. هر تغییر پیشنهادی دارای منشأ، شناسهٔ میزبان/نشست، commit، hash، آزمون و نتیجهٔ read-back قابل‌تطبیق است.

آزمون prompt یا mock به‌تنهایی اثبات امنیت نیست؛ آزمون باید روی حساب‌ها، مجوزها، مخازن و مسیرهای واقعی اجرا شود.

### 18.7 وضعیت اجرایی در زمان ثبت این بخش

- **تصمیم و مدل نقش‌ها:** با تأیید صریح مالک، مجاز و در این شاخه مستند شده است.
- **سیاست MASTER فقط‌خواندنی برای میزبان:** در قرارداد موجود ثبت شده؛ مخزن عمومی است و میزبان ناشناس می‌تواند مانند هر بازدیدکننده‌ای بخواند.
- **حفاظت main:** Ruleset 27814009 در شواهد قبلی فعال گزارش شده، اما approval count برابر 0 و Code Owner review خاموش بوده است؛ اجرای کامل دروازهٔ تأیید هنوز اثبات نشده است.
- **مخازن خصوصی میزبان‌ها، رجیستری عملیاتی، RAHM خصوصی و broker:** تا زمان ایجاد، اتصال و آزمون واقعی، NOT PROVISIONED / NOT VERIFIED می‌مانند.
- **ثبت یا فعال‌سازی میزبان جدید:** انجام نشده است؛ این سند به‌تنهایی هیچ Host ID یا دسترسی صادر نمی‌کند.
- **این تغییر:** یک پیشنهاد معماری در شاخهٔ مستقل است؛ تا ادغام و read-back روی مرجع مقصد، MASTER تغییرکرده محسوب نمی‌شود.

**قاعدهٔ نهایی:** مالک تصمیم می‌گیرد؛ ناظر مستقل بررسی و هشدار می‌دهد؛ میزبان اجرا و پیشنهاد می‌کند. هیچ‌یک جای دیگری را نمی‌گیرد و هیچ میزبان AI مسیر نوشتن یا ارتقای مستقیم/غیرمستقیم به MASTER ندارد.
