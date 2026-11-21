# معماری امنیتی میزبان‌های مستقل و مخزن مادر فقط‌مالک

- Stable ID: HAIF-OWNER-ONLY-MASTER-PER-HOST-PRIVATE-REPOS-2026-11-21-001
- Version: 1.0.0
- Status: OWNER-DIRECTED / DESIGN REGISTERED ON PROPOSAL BRANCH / IMPLEMENTATION PARTIAL
- Parent: POINT-0/083 → CURRENT-136 → NEXT-051
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

The latest repository contract recorded `main.protected=false`; the current GitHub connector has no action for reading/writing branch protection/rulesets or collaborator lists. Therefore actual protection and the current collaborator/App audit remain NOT VERIFIED until checked in GitHub Settings.

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
- main protection: latest recorded state `protected=false`; current live status not re-readable through available connector; NOT VERIFIED.
- Host-specific private repositories: NOT CREATED.
- GitHub App per-host scoped installation: NOT CONFIGURED.
- Broker and server-side identity mapping: NOT DEPLOYED / OPEN.
- Host Registry live entries: NONE VERIFIED.
- Cross-host negative security tests: NOT RUN.
- Host enrollment: one-message instructions exist, but no new host is thereby registered or activated.

## 11. Safe default

Until all L3 gates pass, every new host is strictly L1_READ_ONLY against master and performs work only in a private destination runtime or owner-created private repository with no host write credential. If the environment cannot prove isolation, do not provide any repository credential; produce a local export for owner review instead.
