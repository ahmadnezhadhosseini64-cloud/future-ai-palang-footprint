# الگوی مخزن خصوصی میزبان HAIF

این سند قالب محتوایی برای مخزن خصوصی مستقل هر میزبان است. این فایل در مخزن مادر فقط template است؛ خود مخزن خصوصی باید توسط مالک جداگانه ساخته شود.

## نام‌گذاری
`haif-host-<HOST_ID>`

## الزامات تنظیمات
- Visibility: PRIVATE.
- Owner: حساب/سازمان تحت کنترل مالک.
- Repository ID و full_name پس از ساخت در Registry ثبت شوند.
- هیچ اشتراک‌گذاری بین میزبان‌ها.
- میزبان به‌عنوان collaborator در personal private repo اضافه نشود.
- اگر نوشتن خودکار لازم است: GitHub App فقط به همین repository نصب شود؛ حداقل مجوز لازم، ترجیحاً Metadata read و Contents write فقط برای broker. هیچ Administration/Actions/Secrets/Workflows permission.
- Branch protection/ruleset فعال و آزموده شود.
- Owner retains Admin, audit, export, archive, revoke and delete.

## ساختار پیشنهادی
```text
CHARTER.md
SNAPSHOT/                 # read-only source snapshot + exact commit
INBOX/                    # validated broker intake only
OBSERVATIONS/
PROPOSALS/
TESTS/
RECEIPTS/
DECISIONS/                # owner-authored/owner-approved
RECOVERY/
EXPORT/
MANIFEST.json
SECURITY.md
```

## مجوزها
- L1_READ_ONLY: no host write credential.
- L2_PRIVATE_WORKSPACE: workspace provisioned by owner; write disabled until broker passes security gates.
- L3_BROKER_WRITE: only via host-bound broker route and one-repository GitHub App installation. The model never receives the token.

## Required tests
- Host can access only its own private repo via approved broker route.
- Host A denied on Host B and master.
- Host B denied on Host A and master.
- Unknown host denied private repo/broker.
- Revoked/expired credential denied.
- Broker rejects arbitrary repo/path, traversal, symlink, secret and unauthorized file types.
- Owner export and restore succeeds with matching manifest/hash.
