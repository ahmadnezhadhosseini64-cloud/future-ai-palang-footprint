# QUARANTINED_DUPLICATE_ID_NONCANONICAL — OUT-114 — خروجی معماری: ثبت نقطهٔ جاری و تحویل نسخهٔ قابل اثبات

- Point: [POINT-0/072](GPT6-RAHM-USER-POINT-0-20261121-072-SET-CURRENT-POINT-AND-LATEST-DELIVERY.md)
- Input: [IN-115](PALANG-0.0-IN-20261121-115-SET-CURRENT-POINT-AND-LATEST-DELIVERY.md)
- Event: [EVT-0291](../../architecture/BEHAVIOR-TRACE/EVT-0291-SET-CURRENT-POINT-AND-LATEST-DELIVERY-2026-11-21.md)
- Current: [CURRENT-125](PALANG-0.0-CURRENT-20261121-125-SET-CURRENT-POINT-AND-LATEST-DELIVERY.md)
- Sole queue: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Master: [سند مرجع مادر](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)

## نتیجه
این تعامل به‌عنوان POINT-0/072 روی همان ریشهٔ canonical ثبت می‌شود؛ زنجیرهٔ POINT-0/071 و CURRENT-124 حفظ می‌شود. EVT-0290 از قبل mirror-only است؛ شناسهٔ این رویداد EVT-0291 است. سند مادر به 1.7.79 ارتقا می‌یابد و CURRENT-125 آخرین checkpoint می‌شود. NEXT-051 تنها صف فعال باقی می‌ماند؛ NEXT-052 ایجاد نمی‌شود.

## آخرین بستهٔ واقعاً دارای رسید قبلی
نسخهٔ داخلی 0.4.3؛ نام ZIP canonical haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip؛ 238096 بایت؛ SHA-256 6cb016339822274586187b01e7fde74ec6623594167be2196d71c1d3959e0d38؛ 18 فایل؛ CRC PASS؛ آزمون‌های استخراج‌شده 24/24 PASS؛ source commit adde4cd8859e94a3f44083dd91f7d549ef684cc8؛ سند مادر جفت‌شده 1.7.77. این رسید تاریخی است و بستهٔ تازهٔ جفت‌شده با سند مادر جاری نیست.

## گیت‌های باز
بازسازی ZIP با سند مادر جدید، exact-head RAHM/Audit، بازیابی میزبان مستقل، اتصال مجاز GitHub در میزبان مقصد، workspace پایدار، restart persistence و ضبط خودکار تعاملات همچنان OPEN / NOT VERIFIED / NOT RUN.


## Duplicate identifier reconciliation
This later parallel file set reused POINT-0/072, IN-115, OUT-114 and CURRENT-125. It is preserved for forensic history but is not canonical. The earlier registered CURRENT-CHAT-ANCHOR path set is canonical; its event is uniquely EVT-0291 because EVT-0290 was already assigned to the mirror-only event.
