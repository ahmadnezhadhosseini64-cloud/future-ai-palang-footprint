# EVT-0064 — پیاده‌سازی ورود و بازیابی سند با منشأ در مدل اولیه HAIF

- Event ID / شناسهٔ رویداد: EVT-0064
- Stable ID / شناسهٔ پایدار: HAIF-DOCUMENT-INGEST-RETRIEVAL-PROVENANCE-2026-10-21-001
- Production ID / شناسهٔ تولید: HDIRP-2026-10-21-001
- Version / نسخه: 1.0.0
- Project / پروژه: Future AI / Palang Footprint — HAIF
- Owner / مالک: احمد پلنگ
- Date / تاریخ: 2026-10-21
- Exact message timestamp / زمان دقیق پیام: UNKNOWN / UNVERIFIED
- Status / وضعیت: IMPLEMENTED / TESTED / REPOSITORY-ONLY
- Parent / سند مادر: [سند مرجع مادر مدل اولیهٔ هوش مصنوعی](../مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Queue / صف ادامه: [صف گام‌های بعدی و موارد باز](../مدل%20اولیه%20AI/صف%20گام‌های%20بعدی%20و%20موارد%20باز.md)

## درخواست و تصمیم

هدف ساخت مدل هوش مصنوعیِ قابل‌رشد و قابل‌استخراج برای محصول است. به‌جای افزودن معماری موازی، قابلیت بعدی در همان نمونهٔ `prototype/haif-v0` ساخته شد: ورود سند و بازیابی واژه‌محور همراه با منشأ قابل‌ردیابی.

## تغییرات واقعی

- `POST /api/v1/documents`: ثبت عنوان، مسیر منبع، نسخه، متن، منشأ، زمان و SHA-256؛ سپس بازخوانی رکورد و تطبیق hash.
- `GET /api/v1/search?q=...`: جست‌وجوی زیررشته‌ای case-insensitive و بازگرداندن شناسهٔ سند، مسیر، نسخه، منشأ، hash و روش بازیابی.
- آزمون‌ها برای نوشتن/بازخوانی، حفظ منشأ، بازیابی موفق و نتیجهٔ بدون تطبیق اضافه شدند.

## شواهد پذیرش

- [HAIF Prototype Tests run 39580170352](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39580170352): SUCCESS — 7 passed, 1 warning, 0 failed.
- [Living Architecture Audit run 39580209577](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39580209577): SUCCESS روی commit `19ae7062b3017d6eb1900112ef08a9a563745475`; 543 فایل منبع، 1,343 پیوند محلی، 0 پیوند مفقود، 0 خطای رمزگشایی؛ شمارش همسان 39 Stable ID، 50 Production ID، 7 Reference ID.

## محدودیت و گام بعد

این نسخه بازیابی واژه‌محور ساده است و ادعای جست‌وجوی معنایی/برداری ندارد. داده‌ها فقط در SQLite محلی نمونه ذخیره می‌شوند؛ هیچ مقصد بیرونی یا اتصال خودکار به گفتگوها تأیید نشده است. گام بعدی: آزمون restart و بازیابی همان سند/hash/منشأ پس از راه‌اندازی مجدد؛ سپس طراحی استخراج کنترل‌شدهٔ اسناد مخزن با حفظ منشأ و نسخه.


## Acceptance update — restart proof

- Added a restart test: create a document, close the app client, create a fresh app instance against the same SQLite file, search again, and verify document ID, SHA-256, source path, version and origin.
- [HAIF Prototype Tests run 39580527915](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39580527915): SUCCESS — **8 passed, 1 warning, 0 failed**.
- [Living Architecture Audit run 39580528257](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39580528257): SUCCESS on commit `1df9d6246ee3d830115385aa047c5475b9ce10ef`; 544 source files, 1,354 local links, 0 missing links, 0 decode errors, 39/50/7 identifier-group counts aligned.
- Restart persistence is verified only for the same local SQLite file and test environment. It does not prove external backup or deployment persistence.
