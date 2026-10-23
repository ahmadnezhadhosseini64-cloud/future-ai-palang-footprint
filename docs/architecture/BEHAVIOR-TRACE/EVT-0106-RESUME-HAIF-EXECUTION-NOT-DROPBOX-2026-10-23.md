# EVT-0106 — ازسرگیری اجرای HAIF، نه Dropbox

- Stable ID: EVT-0106-RESUME-HAIF-EXECUTION-NOT-DROPBOX-2026-10-23
- Production ID: EVT-0106
- Version: 1.0.0
- Date: 2026-10-23
- Parent master: [CMIND](../../reference/REFERENCE-DOCUMENTS/CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-MASTER-REFERENCE-2026-10-22-001.md)
- Input: [IN-018](../../0.0/anchors/PALANG-0.0-IN-20261023-018-RESUME-HAIF-EXECUTION.md)
- Output: [OUT-018](../../0.0/anchors/PALANG-0.0-OUT-20261023-018-RESUME-HAIF-EXECUTION.md)
- Product master: [HAIF extractable interaction model](../مدل%20اولیه%20AI/سند%20مرجع%20مادر%20—%20الگوریتم%20استخراج%20مدل%20و%20محصول%20رایگان%20HAIF.md)
- Status: EVENT DOCUMENT CREATED; read-back pending.
- Exact event time: not independently captured; use actual repository commit time as canonical registration time after commit, not as user-message time.

## Trigger
کاربر گفت: «خوب شروع کن». لنگرهای قبلی دستور می‌دهند ادامه از مدل اولیه و prototype/haif-v0 باشد؛ Dropbox خارج از دامنهٔ جاری است.

## Observation
در مخزن، نمونهٔ HAIF v0 و دفتر جفت تعامل INT/IN/OUT از قبل وجود دارند. مستندات نمونه، ذخیره‌سازی SQLite، hash محتوا، بازخوانی پس از نوشتن و آزمون‌های idempotency، شناسهٔ متعارض، lookup معکوس و بازیابی پس از ساخت مجدد برنامه را شرح می‌دهند. CI ثبت‌شده 39824020260 در README به‌عنوان موفق معرفی شده، اما در این رویداد اجرای تازه‌ای انجام نشده است.

## Architecture lesson
- لنگر تاریخیِ یک مقصد، مجوز تغییر مسیر کار جاری نیست.
- خطای انتخاب مسیر و علت احتمالی آن باید در دفتر رفتار ثبت شوند، نه اینکه فقط در گفت‌وگو توضیح داده شوند.
- «موجود در کد»، «CI قبلی موفق»، «آزمون تازه اجرا شد» و «تأیید سرتاسری» چهار ادعای متفاوت‌اند.
- یکپارچگی فقط با شاهد مقصدی و بازخوانی تأیید می‌شود.
- ترتیب ادامه: مدل اولیه → سند مادر HAIF → بررسی importer/schema/tests → ingest و restart test → ثبت شواهد → داوری معنایی گراف.

## Action
گام بعدی، بررسی متمرکز importer و schema/test suite و اجرای آزمون واقعی در محیطی که مخزن checkout شده و سرویس محلی قابل اجرا باشد. اگر محیط موجود نباشد، آزمون اجراشده وانمود نشود و مانع به‌عنوان OPEN ثبت بماند.

## Verification ledger
- Repository write: این فایل در همین عملیات ایجاد می‌شود؛ commit SHA و زمان canonical باید از پاسخ GitHub ثبت شوند.
- Read-back: پس از نوشتن، فایل باید از شاخهٔ پیش‌فرض مجدداً خوانده شود.
- Match: شناسه‌ها، روابط IN/OUT، سند مادر، مرز دامنه و اقدام بعدی باید تطبیق داده شوند.
- Runtime test: NOT RUN in this event.
- External persistence: NOT ATTEMPTED.
