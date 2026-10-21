# EVT-0069 — افزودن ورود کنترل‌شدهٔ اسناد مخزن به HAIF v0

- **Event ID / شناسهٔ رویداد:** EVT-0069
- **Stable ID / شناسهٔ پایدار:** HAIF-CONTROLLED-REPOSITORY-DOCUMENT-INGESTION-2026-10-21-001
- **Production ID / شناسهٔ تولید:** HCRDI-2026-10-21-001
- **Version / نسخه:** 1.0.0
- **Project / پروژه:** Future AI / Palang Footprint — HAIF
- **Owner / مالک:** احمد پلنگ
- **UTC reference / زمان مرجع UTC:** 2026-10-21T13:49:10Z (زمان commit مستندشده؛ نه زمان پیام کاربر)
- **Tehran equivalent / معادل تهران:** 2026-10-21T17:19:10+03:30 (Asia/Tehran)
- **Time provenance / منشأ زمان:** مهر زمانی commit مخزن
- **Status / وضعیت:** IMPLEMENTED IN REPOSITORY; CI AND RUNTIME INGESTION PENDING
- **Parent anchor / لنگر والد:** `PALANG-0.0-RETURN-EXECUTION-MASTER-ANCHOR-2026-10-21-001`
- **Master reference / سند مادر:** [لنگر بازگشت اجرایی](../../reference/REFERENCE-DOCUMENTS/PALANG-RETURN-EXECUTION-MASTER-ANCHOR-2026-10-21-001.md)
- **Queue / صف ادامه:** [صف گام‌های بعدی و موارد باز](../مدل%20اولیه%20AI/صف%20گام‌های%20بعدی%20و%20موارد%20باز.md)

## 1. دلیل تغییر

لنگر بازگشت دستور می‌دهد اسناد واقعی مخزن به همان نمونهٔ `prototype/haif-v0` وارد شوند؛ با حفظ مسیر منبع، نسخه، منشأ و hash، و بدون ساخت معماری موازی. قابلیت قبلی API ثبت سند و بازیابی واژه‌محور را داشت، اما واردکنندهٔ کنترل‌شده برای خواندن فایل‌های واقعی checkout و ارسال آن‌ها به API وجود نداشت.

## 2. تغییر واقعی انجام‌شده

- فایل تازه: `prototype/haif-v0/ingest_repository_docs.py`.
- یک allowlist صریح از شش سند مرجع/رویداد تعیین شده است؛ کل مخزن خودکار وارد نمی‌شود.
- هر payload شامل عنوان، مسیر نسبی منبع، نسخهٔ اعلام‌شده (یا `UNDECLARED`)، متن کامل و منشأ شامل شناسهٔ commit در دسترس است.
- واردکننده نتیجهٔ API را بررسی می‌کند و فقط `WRITE_READBACK_VERIFIED` همراه با SHA-256 را موفق می‌شمارد.
- فایل مفقود، خطای HTTP، شکست درخواست یا پاسخ تأییدنشده باعث گزارش غیرموفق می‌شود.
- README نمونه و صف اقدام‌های باز به‌روزرسانی شدند.
- آزمون‌های واحد برای حفظ مسیر/نسخه/commit و شکست بسته‌محور در صورت فقدان فایل اضافه شدند.

## 3. شواهد مخزن

- Commit افزودن واردکننده: `646db3067e66e24063e83dfc4e8586eb5bece581`.
- Commit آزمون‌های واردکننده: `73059342de426c89da2c1bbe54908addd71156b0`.
- Commit مستندات و صف: `9fc54888b0b25f1075205cd49bef1c0a29e96831`.
- [فایل واردکننده](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/blob/main/prototype/haif-v0/ingest_repository_docs.py).
- [آزمون‌ها](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/blob/main/prototype/haif-v0/test_app.py).
- [README نمونه](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/blob/main/prototype/haif-v0/README.md).
- [صف گام‌ها](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/blob/main/docs/architecture/%D9%85%D8%AF%D9%84%20%D8%A7%D9%88%D9%84%DB%8C%D9%87%20AI/%D8%B5%D9%81%20%DA%AF%D8%A7%D9%85%E2%80%8C%D9%87%D8%A7%DB%8C%20%D8%A8%D8%B9%D8%AF%DB%8C%20%D9%88%20%D9%85%D9%88%D8%A7%D8%B1%D8%AF%20%D8%A8%D8%A7%D8%B2.md).

## 4. معیارهای تأیید و وضعیت فعلی

1. **CI / آزمون خودکار:** در زمان ثبت این رویداد، گردش‌کارهای مربوط به commitهای تازه در حال اجرا/صف بودند؛ نتیجهٔ موفق هنوز ادعا نمی‌شود.
2. **Runtime ingestion / ورود واقعی به نمونهٔ در حال اجرا:** هنوز اجرا نشده است. وجود اسکریپت و آزمون واحد، ورود واقعی شش سند به SQLite را اثبات نمی‌کند.
3. **Read-back / بازخوانی:** برای هر رکورد، API باید `WRITE_READBACK_VERIFIED` برگرداند؛ سپس باید با جست‌وجو مسیر، نسخه، منشأ و hash رکوردهای واردشده تطبیق داده شوند.
4. **Restart / شروع مجدد:** آزمون قبلی restart برای سند آزمایشی عمومی وجود دارد؛ پس از ورود واقعی باید بازیابی یکی از اسناد واردشده بعد از ساخت نمونهٔ تازه با همان پایگاه داده نیز اثبات شود.
5. **Semantic graph / گراف معنایی:** داوری موردبه‌مورد شناسه‌ها، EVTها و روابط همچنان باز است و با این تغییر بسته نشده است.

## 5. مرز ادعا

این تغییر در مخزن GitHub ثبت شده است. هنوز ادعا نمی‌شود که اسناد واقعاً به نمونهٔ در حال اجرا وارد شده‌اند، دادهٔ برنامه به Dropbox یا هر مقصد خارجی منتقل شده، یا Buffer / Persistent Memory / Library به‌روزرسانی شده‌اند. هر مقصد وضعیت مستقل دارد.

## 6. اقدام بعدی دقیق

1. نتیجهٔ CI برای commit نهایی را بخوان و در صورت شکست، خطا را اصلاح کن.
2. واردکننده را علیه نمونهٔ محلی در حال اجرا با شش سند allowlist اجرا کن.
3. گزارش را نگه دار؛ تعداد موفق‌ها باید دقیقاً ۶ از ۶ باشد.
4. با `/api/v1/search` برای سندهای واردشده جست‌وجو کن و مسیر، نسخه، منشأ و hash را تطبیق بده.
5. با یک نمونهٔ تازه و همان SQLite، بازیابی پس از restart را برای سند واردشده اثبات کن.
6. شواهد واقعی، commit و زمان‌های UTC/تهران را ثبت و همین رویداد/صف را به‌روزرسانی کن.
7. پس از آن به داوری معنایی موردبه‌مورد گروه‌های شناسه و EVT برگرد؛ موارد باز را حذف یا بی‌دلیل بسته اعلام نکن.

**قاعدهٔ اثبات:** طراحی‌شدن ≠ اجراشدن؛ commit ≠ آزمون موفق؛ نوشتن ≠ بازخوانی؛ بازخوانی ≠ تطبیق؛ مخزن ≠ مقصدهای مستقل.


## 7. CI/read-back update — verified repository evidence

- **HAIF Prototype Tests:** [run 39611314780](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39611314780) — SUCCESS, **10 passed, 1 warning, 0 failed**. This run includes the importer and its two new unit tests, at commit `6725809b556d6e4f25585290773c4cfd45dacbf5`.
- **Living Architecture Audit:** [run 39611383556](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39611383556) — SUCCESS on commit `6b0128608e6bf7978e40499c822fe1f462eea41e`.
- **Cross-Layer Integrity Gate:** [run 39611383383](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39611383383) — SUCCESS on commit `6b0128608e6bf7978e40499c822fe1f462eea41e`.
- Files `ingest_repository_docs.py`, `test_app.py`, this event record, and the open-gap queue were read back from the repository; file hashes/SHAs were returned by GitHub. The architecture and cross-layer workflow conclusions apply only to their checked commits.
- CI success confirms the code/test suite and the configured audit gates, not that the importer has been run against a live API or that six documents were stored in SQLite.

**Updated state:** implementation and automated tests are repository-verified; real runtime ingestion, provenance search, and post-ingestion restart proof remain OPEN.


## پیوند به لنگر مستقل خروجی — EVT-0070

- [لنگر مستقل خروجی جاری](../../0.0/PALANG-OUTPUT-ANCHOR-HAIF-INGESTION-2026-10-21-002.md)
- [رویداد مستقل ثبت خروجی](./EVT-0070-PALANG-OUTPUT-ANCHOR-HAIF-INGESTION-2026-10-21.md)
- نتیجهٔ CI ثبت‌شده برای آزمون واحد: 10 passed, 1 warning, 0 failed.
- آزمون یکپارچهٔ تازه در run 39611543861 در آخرین بررسی هنوز نتیجهٔ نهایی نداشت؛ پس از اجرای آن باید نتیجهٔ واقعی به این رویداد و صف منعکس شود.


## Integration acceptance result — linked to EVT-0070
- The integration test was corrected and the test job passed in [HAIF Prototype Tests #39612814614](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39612814614), commit `c972e637dff093f6569d43f7e957f267cdac6484`: `11 passed, 1 warning, 0 failed`.
- The test covers six allowlisted repository documents, API write/read-back hash, provenance search, and retrieval after app restart using the same temporary SQLite database.
- See [EVT-0070](./EVT-0070-PALANG-OUTPUT-ANCHOR-HAIF-INGESTION-2026-10-21.md) and [independent output anchor](../../0.0/PALANG-OUTPUT-ANCHOR-HAIF-INGESTION-2026-10-21-002.md).
- This does not prove live-host ingestion or external persistence. Buffer, Persistent Memory, Library and Dropbox remain independently unverified.
