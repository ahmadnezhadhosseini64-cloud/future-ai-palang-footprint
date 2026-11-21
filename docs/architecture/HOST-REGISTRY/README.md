# دفتر ثبت میزبان‌ها — HAIF

- Governance checkpoint: CURRENT-122
- Architecture: POINT-0/068 and POINT-0/069
- Status: REGISTRY STRUCTURE REGISTERED / NO LIVE HOSTS VERIFIED

## Purpose
هر میزبان هوش مصنوعی که به مخزن متصل می‌شود باید پیش از ارسال داده، یک Host Node مستقل با شناسهٔ یکتا و دامنهٔ مجوز محدود داشته باشد. دفتر ثبت، هویت فنی، نسخه‌ها، سطح دسترسی، وضعیت اتصال، زمان ثبت، وضعیت لغو و ارجاع رسیدهای پذیرش را نگه می‌دارد.

## Files
- `HOST-REGISTRY.json`: وضعیت جاری میزبان‌های ثبت‌شده؛ فعلاً فهرست خالی است تا میزبان واقعی با رسید مستقیم ثبت شود.
- `HOST-REGISTRY-SCHEMA.json`: قرارداد داده و اعتبارسنجی ثبت میزبان.

## Lifecycle
PROPOSED → IDENTITY_VERIFIED → L1_READ_ONLY → L2_PROPOSAL_ONLY → L3_TEST_CONTRIBUTOR → SUSPENDED / REVOKED.

سطح L4 فقط برای عملیات مشخص، مدت‌دار و با تأیید صریح مالک قابل طرح است؛ دسترسی admin یا bypass برای میزبان AI مجاز نیست.

## Mandatory fields
host_id, host_type, model_version, adapter_version, owner_approval_ref, permission_scope, credential_reference (secret-manager pointer only; never secret), registered_at_utc, status, last_seen_at_utc, master_version_seen, master_commit_seen, acceptance_receipt_ref, revocation_ref.

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
