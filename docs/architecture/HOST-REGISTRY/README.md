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
