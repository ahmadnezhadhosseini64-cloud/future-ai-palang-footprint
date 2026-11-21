# OUT-121 — خروجی: قاعدهٔ انتشار شدنی و توسعهٔ باز

- Status: PREPARED / OWNER-APPROVED / IMPLEMENTATION-IN-PROGRESS
- Parent: IN-122
- Point: POINT-0/079 (۰++)
- Previous checkpoint: CURRENT-131
- Target checkpoint: CURRENT-132
- Sole queue: NEXT-051

## قرارداد خروجی
1. آخرین نسخهٔ شدنی از آخرین منبع اثبات‌شده استخراج شود؛ نه از یک گزارش یا نسخهٔ قدیمی‌تر.
2. قابلیت‌ها با دامنهٔ دقیق شواهد فهرست شوند؛ PASS یک محیط به معنی PASS همهٔ میزبان‌ها نیست.
3. موارد ناقص/نشدنی در Development / OPEN / BLOCKED با علت، وابستگی و معیار ارتقا ثبت شوند.
4. وابستگی قدیمی به‌صورت محدود و مستند مدیریت شود؛ نه حذف خاموش و نه توقف کلی بی‌دلیل.
5. ZIP canonical با همان stable ID و filename حفظ شود؛ فقط پس از تغییر محتوا و گذر از exact-source build/test/digest/read-back نسخهٔ داخلی افزایش یابد.
6. تاریخچه و رسیدهای قدیمی append-only باقی بمانند.
7. گام‌های 0.0 تنها صف اجرایی NEXT-051 را تکمیل کنند؛ صف موازی ساخته نشود.

## گام‌های 0.0 و معیار پذیرش
- 0.0.1 — Source of truth: دریافت main HEAD، تعیین commit دقیق و مقایسهٔ source؛ PASS با SHA مشخص.
- 0.0.2 — Runnable inventory: استخراج قابلیت‌های واقعاً پیاده‌سازی‌شده از manifest، کد و تست؛ PASS با inventory و نتیجهٔ تست.
- 0.0.3 — Dependency triage: ثبت وابستگی قدیمی، مصرف‌کنندگان و دامنهٔ اثر؛ PASS با تصمیم محدودسازی/جایگزینی و آزمون رگرسیون.
- 0.0.4 — Package: build همان ZIP canonical؛ PASS با filename/stable ID ثابت، version، bytes، SHA-256، CRC، inventory و receipt.
- 0.0.5 — Extraction/recovery: استخراج در محیط پاک و بازسازی از ZIP؛ PASS با source-byte match و round-trip.
- 0.0.6 — Open development: ثبت قابلیت‌های میزبان‌وابسته/ناقص با معیار ارتقا؛ هیچ موردی بدون شاهد بسته نشود.
- 0.0.7 — Clean-host acceptance: ورود در نشست AI مستقل، OAuth رسمی، workspace و restart؛ OPEN تا رسید مستقیم.
- 0.0.8 — Promotion: انتقال فقط قابلیت‌های PASS شده به Latest Runnable و حفظ تاریخچه.
- 0.0.9 — Reconcile: بازخوانی سند مادر، Reference Index، 0.0 index، Behavior Trace و NEXT-051؛ PASS با تطبیق پیوندها.

## وضعیت بسته در زمان ثبت

در ادامه، بستهٔ 0.4.7 روی main با workflow 44920781712 تأیید شد: 19 فایل، 256684 بایت، 24/24 آزمون، CRC و source-byte match و artifact round-trip موفق؛ SHA-256 برابر a8a34580722573aaef247acbf9d7edf1d97a80025c49d510f07a1479da4f0a05. جفت‌سازی با سند مادر 1.7.86 بایت‌به‌بایت PASS شد. وابستگی قدیمی مرحلهٔ دانلود artifact با PR #73 و action رسمی download-artifact اصلاح شد؛ شکست قبلی حفظ شده است. بستهٔ بعدی 0.4.8 با سند مادر 1.7.87 هدف‌گذاری شده است.

## وضعیت بسته در زمان ثبت
بستهٔ canonical داخلی 0.4.6، 19 فایل و 24/24 آزمون استخراج‌شده PASS دارد؛ SHA-256 فایل ZIP داخلی: b9f56a360351d5ab16f07656018e576c2398a110db540138810e01358f8934fc. این receipt به source commit مشخص خود تعلق دارد و با سه commit بعدیِ مستندات/رسید فقط در صورت اثبات هم‌ارزی منبع قابل استفاده است. این نتیجه آزمون بسته است، نه پذیرش میزبان مستقل.

OAuth مقصد، workspace پایدار، clean-host recovery، restart و HOST-RECOVERED: OPEN / NOT RUN.


## Input and state links
- [POINT-0/079](GPT6-RAHM-USER-POINT-0-20261121-079-LATEST-RUNNABLE-OPEN-DEVELOPMENT.md) → [IN-122](PALANG-0.0-IN-20261121-122-LATEST-RUNNABLE-OPEN-DEVELOPMENT.md) → [EVT-0299](../../architecture/BEHAVIOR-TRACE/EVT-0299-LATEST-RUNNABLE-OPEN-DEVELOPMENT-2026-11-21.md) → [TIME-BINDING-EVT-0299](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0299-LATEST-RUNNABLE-OPEN-DEVELOPMENT-2026-11-21.md) → [CURRENT-132](PALANG-0.0-CURRENT-20261121-132-LATEST-RUNNABLE-OPEN-DEVELOPMENT.md) → [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md).


## Shared recovery targets (must match IN-122)
- Living master: [سند مرجع مادر](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Independent-host recovery proof protocol: [INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL](../../architecture/مدل%20اولیه%20AI/INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md)
- Package recovery protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL.md](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- Export manifest: [EXPORT_MANIFEST.json](../../portable/RAHM/EXPORT_MANIFEST.json)


## Subsequent package verification — 0.4.8

Package 0.4.8 verified by workflow 44921364797 on main SHA 680a1f788a50e38da4b71768f8291dde0eeeaa31; paired master 1.7.87; 19 files; 257102 bytes; 24/24 tests PASS; CRC, exact artifact-ID download, source-byte read-back and artifact round-trip PASS. SHA-256 1e1bbab0c7acb0975b77176abc5c38f7e7097cfe8cf67b17153ffe1db4da65a6. Package 0.4.7 remains historical. The next current chain is POINT-0/080 → CURRENT-133 and package target 0.4.9.
