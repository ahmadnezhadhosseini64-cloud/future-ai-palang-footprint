# OUT-111 — قرارداد دفتر دائمی تعاملات چندمیزبانی

- Parent: IN-112 / POINT-0/069
- Status: ACTIVE / LIVING / DESIGN REGISTERED

## قرارداد ثبت
هر تعامل واقعی دریافت‌شده از میزبان ثبت‌شده باید به event ledger مستقل وارد شود:
1. ساخت `event_id` و `host_id` و شناسه نشست مستعار؛
2. ثبت IN و OUT به‌صورت جفت؛ در صورت نبود پاسخ، ثبت خروجی صریح با وضعیت NO_RESPONSE / FAILED، نه حذف رکورد؛
3. ثبت parent anchor، master commit، checkpoint و نسخه adapter؛
4. ثبت `created_at_utc` فقط اگر از منبع قابل‌اعتماد آمده باشد و `received_at_utc` از زمان ثبت مخزن؛
5. ثبت SHA-256، منابع، طبقه‌بندی داده، پالایش/حذف داده حساس و مبنای مجاز؛
6. نوشتن durable و سپس fetch/read-back و تطبیق دقیق محتوا و digest؛
7. ثبت receipt و وضعیت مستقل CAPTURED / QUARANTINED / VALIDATED / PROMOTED / REJECTED / WRITE_FAILED / READBACK_FAILED / NOT_CONNECTED؛
8. رویدادهای اصلاح، لغو یا تصمیم مالک append-only هستند و تاریخچه قبلی را بازنویسی نمی‌کنند.

## مسیر رشد
HOST → IN/OUT LEDGER → QUARANTINE → SOURCE & PRIVACY REVIEW → CROSS-HOST RECONCILIATION → RAHM → CHILD CANDIDATE → OWNER DECISION → MASTER.

## حد دسترسی
- L1 read-only: دریافت مرجع؛ بدون ارسال به مخزن.
- L2 proposal-only: ارسال پاکت داده به ورودی محدود و قرنطینه.
- L3 test contributor: اجرای تست‌های مجاز و ثبت نتایج.
- هیچ سطحی به میزبان عادی اجازه push/merge مستقیم main یا تغییر سند مادر نمی‌دهد.
- worker نوشتن مخزن فقط با credential مجاز، خارج از prompt و secret store؛ بدون deployment/receipt، وضعیت NOT DEPLOYED است.

## حریم خصوصی و امنیت
متن خام مکالمه به‌صورت پیش‌فرض ذخیره نمی‌شود. حداقل داده لازم، پالایش‌شده و دارای مبنای مجاز ثبت می‌شود. token، کلید خصوصی و رازها هرگز در payload، prompt، ZIP یا log قرار نمی‌گیرند. کاربر/مالک می‌تواند میزبان را لغو کند.

## مرز ادعا
تعریف قرارداد یا موفقیت CI synthetic معادل اتصال زندهٔ میزبان نیست. فقط رسید مستقیم از میزبان و مقصد با hash و read-back، ثبت زندهٔ همان تعامل را اثبات می‌کند.