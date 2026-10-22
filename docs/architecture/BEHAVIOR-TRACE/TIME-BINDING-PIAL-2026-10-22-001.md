# TIME-BINDING-PIAL-2026-10-22-001 — پابند زمانی جفت تعامل

- Stable ID: PALANG-TIME-BINDING-PIAL-2026-10-22-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / EVIDENCE-BINDING
- Canonical rule: actual latest Git commit timestamp in UTC; Tehran = UTC+03:30 from the same instant.

## زمان پیام کاربر
- Interaction: INT-20261022-002
- Input ID: IN-20261022-002
- Source: conversation metadata supplied by the platform
- Observed time: 2026-10-22 14:28 (+03:30), minute precision only.
- This is not a repository commit timestamp. Exact seconds were not available and are not invented.

## زمان ثبت مخزن
زمان canonical برای EVT-0089، دو لنگر و سند مادر باید از commit metadata واقعی فایل‌ها استخراج و پس از read-back در نسخهٔ بعدی این پابند افزوده شود. اگر خود این فایل تغییر کند، زمان canonical خودش نیز به commit جدید تغییر می‌کند؛ بنابراین خودگواهی آینده ممنوع است.

## زمان خروجی
- Output ID: OUT-20261022-002
- زمان دقیق پایان پاسخ از منبع مستقل در دسترس نیست؛ زمان commit ثبت خروجی به‌عنوان زمان ثبت مخزن استفاده می‌شود، نه ادعای زمان تولید دقیق متن.

## پیوندها
- [EVT-0089](./EVT-0089-EVERY-INTERACTION-IN-OUT-TEMPORAL-ANCHOR-AND-RECOVERY-GOVERNANCE-2026-10-22.md)
- [IN anchor](../../0.0/anchors/PALANG-0.0-IN-20261022-002-EVERY-INTERACTION-ANCHOR-GOVERNANCE.md)
- [OUT anchor](../../0.0/anchors/PALANG-0.0-OUT-20261022-002-EVERY-INTERACTION-ANCHOR-GOVERNANCE.md)
- [PIAL master reference](../../reference/REFERENCE-DOCUMENTS/PER-INTERACTION-IN-OUT-TEMPORAL-ANCHOR-LIVING-MASTER-REFERENCE-2026-10-22-001.md)
- [LBAF master reference](../../reference/REFERENCE-DOCUMENTS/LIVING-BEHAVIOR-ARCHITECTURE-FORESIGHT-MASTER-REFERENCE-2026-10-22-001.md)


## مدرک بازخوانی timestampهای commit
جدول commitهای واقعی و زمان متناظر تهران در [EVT-0089-TIMESTAMP-READBACK](./EVT-0089-TIMESTAMP-READBACK-2026-10-22-001.md) ثبت شده است. زمان commit خود این پابند را از metadata commit واقعی آن بخوان؛ از self-certification استفاده نکن.
