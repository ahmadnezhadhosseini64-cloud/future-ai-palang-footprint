> **CURRENT GOVERNANCE — POINT-0/GOLDEN / CURRENT-140 / 2026-11-22**
> The canonical root remains the single existing POINT-0. This is the golden baseline of the already-built project, not a new project, root, or parallel queue. Always retrieve exact main HEAD, the current living mother, CURRENT-140, and the sole active NEXT-051 before acting. Historical points and embedded snapshots are evidence only; they never override this baseline or reopen a settled decision by themselves.
>
> **Absolute host boundary:** every host has PUBLIC READ ONLY access to the canonical master. No host, host-held credential, host App, broker, branch, PR, issue, release, workflow, setting, or indirect relay may write to or promote content into the master. Host work remains in its own isolated runtime and, if owner-provisioned, its own private repository. The owner alone exports selected material.
>
> **RAHM placement:** RAHM is a central, private, owner-only quarantine outside every host workspace. Hosts cannot access, inspect, write, administer, or promote anything from RAHM. Raw/private exports are stored only in the owner-controlled private repository future-ai-palang-rahm; the public master contains policy, schemas, validators, workflows, and sanitized Child candidates only.
>
> **Learning and promotion:** OWNER COMMAND → inspect only verified and accessible Host IDs → owner export/redaction → private RAHM quarantine → cross-host reconciliation → schema/hash/privacy/provenance/tests → trusted bot-authored PR to CHILD → owner review and approval. CHILD is not MASTER. Any later Master update requires a separate owner-directed PR and a separate owner approval.
>
> **No false activation:** no host is ACTIVE until its identity, workspace isolation, repository scope, connector permissions, and acceptance receipt are verified. No continuous monitoring is claimed unless a separate owner-controlled service is actually deployed and evidenced.

# دفتر ثبت میزبان‌ها — HAIF

- Governance checkpoint: CURRENT-140
- Architecture: POINT-0/086 (0++) and CURRENT-139
- Status: REGISTRY STRUCTURE REGISTERED / NO LIVE HOSTS VERIFIED

## Purpose
هر میزبان هوش مصنوعی که به مخزن متصل می‌شود باید پیش از ارسال داده، یک Host Node مستقل با شناسهٔ یکتا و دامنهٔ مجوز محدود داشته باشد. دفتر ثبت، هویت فنی، نسخه‌ها، سطح دسترسی، وضعیت اتصال، زمان ثبت، وضعیت لغو و ارجاع رسیدهای پذیرش را نگه می‌دارد.

## Files
- `HOST-REGISTRY.json`: وضعیت جاری میزبان‌های ثبت‌شده؛ فعلاً فهرست خالی است تا میزبان واقعی با رسید مستقیم ثبت شود.
- `HOST-REGISTRY-SCHEMA.json`: قرارداد داده و اعتبارسنجی ثبت میزبان.

## Lifecycle
Status lifecycle: PROPOSED → IDENTITY_VERIFIED → ACTIVE → SUSPENDED / REVOKED.

Permission scopes are separate: L0_OFFLINE → L1_MASTER_PUBLIC_READ_ONLY → L2_HOST_PRIVATE_WORKSPACE_ONLY → L3_OWNER_EXPORT_PROPOSAL_ONLY → L4_OWNER_BROKERED_PRIVATE_HOST_REPO. L4 can write only to that host's own PRIVATE repository through an owner-controlled broker; it never grants any master branch, RAHM, PR, workflow, settings, or bypass permission.

سطح L4 فقط برای عملیات مشخص، مدت‌دار و با تأیید صریح مالک قابل طرح است؛ دسترسی admin یا bypass برای میزبان AI مجاز نیست. هیچ سطحی مجوز نوشتن در مخزن مادر یا RAHM ایجاد نمی‌کند.

## Mandatory fields
host_id, workspace_id, host_type, model_version, adapter_version, owner_approval_ref, permission_scope, status, registered_at_utc, master_version_seen, master_commit_seen, private_repository, private_repository_visibility, master_access, master_write_access=false, rahm_access=NONE, host_direct_write_access=false, broker_write_access, connector_read_access, monitoring_mode, acceptance_receipt_ref, owner_id_issuer, host_id_issue_receipt_ref, owner_export_receipt_ref, last_export_at_utc, workspace_isolation_ref, revocation_ref. credential_reference is a secret-manager pointer only, never a token or secret.

## Status truth
این دفتر، ساختار ثبت را ایجاد می‌کند؛ وجود میزبان متصل را اثبات نمی‌کند. میزبان فقط پس از ارائه رسید خام از خود میزبان، آزمون مجوز و read-back مخزن می‌تواند REGISTERED / ACTIVE شود. در این commit هیچ میزبان خارجی به‌عنوان ACTIVE ثبت نشده است.


## POINT-0/070 — محیط‌های مستقل میزبان

- Workspace model: [HOST-WORKSPACES](../HOST-WORKSPACES/README.md)
- Workspace charter: [template](../HOST-WORKSPACES/WORKSPACE-CHARTER-TEMPLATE.md)
- Isolation and promotion protocol: [protocol](../HOST-WORKSPACES/WORKSPACE-ISOLATION-AND-PROMOTION-PROTOCOL.md)
- Host Registry همچنان تا دریافت هویت و رسید واقعی خالی می‌ماند؛ هیچ میزبان در این نقطه ACTIVE نشده است.
- پوشه‌بندی به‌تنهایی جداسازی امنیتی نیست؛ broker، allowlist مسیر، credential حداقلی و branch protection واقعی باید پیش از اتصال نوشتنی اثبات شوند.


## POINT-0/070 — محیط‌های مستقل میزبان

- Workspace model: [HOST-WORKSPACES](../HOST-WORKSPACES/README.md)
- Workspace charter: [template](../HOST-WORKSPACES/WORKSPACE-CHARTER-TEMPLATE.md)
- Isolation and promotion protocol: [protocol](../HOST-WORKSPACES/WORKSPACE-ISOLATION-AND-PROMOTION-PROTOCOL.md)
- Host Registry همچنان تا دریافت هویت و رسید واقعی خالی می‌ماند؛ هیچ میزبان در این نقطه ACTIVE نشده است.
- پوشه‌بندی به‌تنهایی جداسازی امنیتی نیست؛ broker، allowlist مسیر، credential حداقلی و branch protection واقعی باید پیش از اتصال نوشتنی اثبات شوند.


## POINT-0/084 — ثبت میزبان با مخزن خصوصی مستقل و کنترل مالک

- Security policy: [OWNER-ONLY-MASTER-PER-HOST-PRIVATE-REPOSITORIES.md](../HOST-SECURITY/OWNER-ONLY-MASTER-PER-HOST-PRIVATE-REPOSITORIES.md).
- Private repository template: [PRIVATE-HOST-REPOSITORY-TEMPLATE.md](../HOST-SECURITY/PRIVATE-HOST-REPOSITORY-TEMPLATE.md).
- مخزن مادر Public فقط برای READ است؛ هیچ میزبان AI مجوز نوشتن یا credential برای آن دریافت نمی‌کند.
- پس از رسید واقعی و تأیید مالک، برای هر Host ID یک مخزن PRIVATE جداگانه توسط مالک ایجاد می‌شود. میزبان حق ساخت repo، انتخاب مقصد یا ثبت خودش را ندارد.
- مخزن شخصی private به collaborator نقش read-only نمی‌دهد؛ میزبان به‌عنوان collaborator اضافه نمی‌شود.
- مسیر نوشتن اختیاری فقط از broker و GitHub App محدود به یک مخزن میزبان می‌گذرد؛ token در secret manager باقی می‌ماند.
- L1_READ_ONLY پیش‌فرض است؛ broker/App و private host repos هنوز عملیاتی/اثبات‌شده نیستند.
- بازدیدکننده ناشناس مخزن عمومی قابل شناسایی فردی یا ثبت خودکار نیست.
- هیچ Host ID یا workspace واقعی در این نقطه فعال نشده است؛ Registry تا رسید واقعی خالی می‌ماند.


## POINT-0/086 — RAHM مرکزی و رصد میزبان‌ها

- Current checkpoint: CURRENT-139; sole active queue NEXT-051.
- RAHM is outside all host workspaces and controlled only by the owner.
- Raw/private host exports are stored only in the owner-created private repository future-ai-palang-rahm; the public master holds only schemas, policy, workflow code and sanitized Child candidates.
- Owner-issued Host IDs follow HAIF-HOST-YYYYMMDD-NNN. No host is registered until a real enrollment receipt is reviewed.
- Owner commands can select one Host ID or all verified/accessible hosts. Anonymous public readers are not discoverable or enrollable.
- No host can access RAHM, another host workspace, or write to MASTER.


## Host ID issuance — POINT-0/086

مالک فرمان ورود را می‌دهد؛ دستیار/کنترل‌پلین پس از بررسی رسید مستقیم، دسترسی واقعی و نبود شناسهٔ تکراری، Host ID بعدی را از الگوی HAIF-HOST-YYYYMMDD-NNN صادر و در Registry ثبت می‌کند. هیچ میزبان حق انتخاب یا جعل Host ID ندارد. صدور شناسه به‌تنهایی به معنی فعال‌شدن میزبان نیست.


## Monitoring and repository binding — POINT-0/086

Each verified Host ID maps to at most one owner-created PRIVATE repository and one independent Workspace ID. The ChatGPT GitHub connection must have read access to that exact host repository for LIVE_READ_VERIFIED status. If the connector can read only RAHM owner exports, monitoring_mode is OWNER_EXPORT_SNAPSHOT; it must never be described as live workspace monitoring.

The registry explicitly records that master_access is PUBLIC_READ_ONLY, master_write_access is false, rahm_access is NONE, and host_direct_write_access is false for every host. Any broker, if later deployed, is owner-controlled and can write only to the one private repository mapped to that Host ID. It has no master or RAHM route.

Host ID issuance: the owner commands ChatGPT/the HAIF control plane; the assistant checks the current registry, validates the direct enrollment receipt, and issues the next unique HAIF-HOST-YYYYMMDD-NNN ID. A host never chooses or self-assigns its ID. Issuance alone does not activate a host.


## Golden baseline status

The live registry file is intentionally empty (`hosts: []`) at the current golden baseline. This means no real host is registered or ACTIVE. Registration is owner-commanded only and requires a direct receipt and identity review. Every future record must preserve `master_access=PUBLIC_READ_ONLY`, `master_write_access=false`, `rahm_access=NONE`, and `host_direct_write_access=false`. A private host repository, if created, is isolated to that host and is not a route to RAHM or MASTER.
