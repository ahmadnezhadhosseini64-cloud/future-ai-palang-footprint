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
بستهٔ canonical داخلی 0.4.6، 19 فایل و 24/24 آزمون استخراج‌شده PASS دارد؛ SHA-256 فایل ZIP داخلی: b9f56a360351d5ab16f07656018e576c2398a110db540138810e01358f8934fc. این receipt به source commit مشخص خود تعلق دارد و با سه commit بعدیِ مستندات/رسید فقط در صورت اثبات هم‌ارزی منبع قابل استفاده است. این نتیجه آزمون بسته است، نه پذیرش میزبان مستقل.

OAuth مقصد، workspace پایدار، clean-host recovery، restart و HOST-RECOVERED: OPEN / NOT RUN.
