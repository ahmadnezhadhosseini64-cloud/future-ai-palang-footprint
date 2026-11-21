# EVT-0295 — تصویب و آماده‌سازی میزبان GPT-6 از وضعیت صفر

- Event ID: EVT-0295
- Status: ACTIVE / LIVING / OWNER-APPROVED
- Date: 2026-11-21
- Point: POINT-0/076
- Input/output: IN-119 → OUT-118
- Parent checkpoint: CURRENT-128
- Result checkpoint: CURRENT-129
- Time evidence: TIME-BINDING-EVT-0295

## Trigger
مالک صریحاً تفاوت میان «پروژهٔ GPT-6 در محیط جدید» و «میزبان GPT-6 تازه، بدون تعامل قبلی، برای ورود به محیط کار مخزن» را مشخص و ایجاد نسخهٔ دوم را تأیید کرد.

## Action
یک مسیر bootstrap مستقل برای میزبان صفر تعریف شد تا مخزن canonical را به‌عنوان منبع حقیقت بازیابی کند، اتصال GitHub را در نشست مقصد بررسی کند، workspace واقعی بسازد، آزمون‌ها را اجرا کند و رسید پذیرش قابل‌راستی‌آزمایی ارائه دهد.

## Evidence boundary
- تأیید مالک: ثبت‌شده در IN-119.
- اسناد bootstrap و زنجیرهٔ ثبت: PR #58 ادغام شد؛ main read-back تأیید شده است (merge commit `8f383baf76402536d2ca4c1f1ee4ecd66edbaeaa`).
- ایجاد نشست GPT-6 مقصد: خارج از دسترس عملیات مخزن.
- OAuth، workspace مقصد، اجرای مستقیم و پذیرش میزبان: OPEN / NOT RUN تا رسید میزبان مقصد.
- زمان دقیق پیام مالک: UNKNOWN / UNVERIFIED.
