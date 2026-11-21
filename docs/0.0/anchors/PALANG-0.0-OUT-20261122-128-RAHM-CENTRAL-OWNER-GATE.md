# OUT-128 — پاسخ و تصمیم معماری رحم مرکزی مالک

- Stable ID: HAIF-OUT-128-RAHM-CENTRAL-OWNER-GATE-2026-11-22
- Parent: IN-129 → POINT-0/086
- Status: IMPLEMENTED IN REPOSITORY / OPERATIONAL SETUP PARTIAL

## تصمیم اجرایی

RAHM در کنترل‌پلین مرکزی و تحت اختیار مالک قرار می‌گیرد. به علت Public بودن مخزن مادر، payload خصوصی و خام در مخزن جداگانه PRIVATE نگهداری می‌شود؛ مخزن مادر فقط schema، policy، validator، workflow و Childهای پالایش‌شده را نگه می‌دارد.

مسیر: HOST PRIVATE WORKSPACE → OWNER-COMMANDED MONITOR/EXPORT → PRIVATE RAHM → VALIDATION/RECONCILIATION → BOT-AUTHORED PR → OWNER REVIEW/APPROVAL → CHILD → SEPARATE OWNER-APPROVED MASTER PR.

این پیاده‌سازی، workflow و validator را در مخزن ایجاد می‌کند؛ ایجاد مخزن خصوصی، ساخت/نصب GitHub App، ثبت Secrets/Variables، اتصال ChatGPT به مخزن خصوصی و فعال‌سازی Ruleset هنوز نیازمند عملیات مدیریتی واقعی و بازخوانی است.
