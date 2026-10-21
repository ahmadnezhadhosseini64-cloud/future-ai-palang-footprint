# EVT-0059 — پیاده‌سازی نمونهٔ اجرایی اولیهٔ HAIF v0

- Event ID / شناسهٔ رویداد: EVT-0059
- Stable ID / شناسهٔ پایدار: HAIF-V0-ANCHOR-EVENT-PROTOTYPE-2026-10-21-001
- Production ID / شناسهٔ تولید: HAIF-V0-AEP-2026-10-21-001
- Version / نسخه: 0.1.0
- Date / تاریخ: 2026-10-21
- Exact user-message time / زمان دقیق پیام کاربر: UNKNOWN / UNVERIFIED
- Timezone / منطقهٔ زمانی پروژه: Asia/Tehran (+03:30)
- Status / وضعیت: PROTOTYPE IMPLEMENTED; latest test rerun pending
- Canonical implementation: [HAIF v0 README](../../../prototype/haif-v0/README.md); API [app.py](../../../prototype/haif-v0/app.py); tests [test_app.py](../../../prototype/haif-v0/test_app.py).
- Parent model: [HAIF-IAM-MR](../مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)

## منشأ و تصمیم

پس از ثبت بستهٔ مدل اولیه، موجودی مخزن نشان داد که ابزارهای پشتیبان پایتون وجود دارند، اما چارچوب و وابستگی‌های یکپارچهٔ خود محصول، API اولیه و آزمون‌های پذیرش محصول در یک محل مستقل وجود نداشتند. طبق مسیر مرحله‌ای مدل، نمونهٔ کوچک و مستقل برای لنگرهای ادامه و دفتر رویداد ساخته شد.

## اقدام‌های انجام‌شده

1. ایجاد API با FastAPI برای سلامت سرویس، ایجاد/فهرست/بازیابی لنگرها و ایجاد/بازیابی رویدادها.
2. استفاده از SQLite محلی برای نمونهٔ توسعه.
3. محاسبهٔ SHA-256 روی JSON canonical و بازخوانی رکورد پس از نوشتن؛ پاسخ WRITE_READBACK_VERIFIED فقط در صورت تطبیق محتوا/hash.
4. نگهداری user_message_time به‌صورت null وقتی زمان پیام معلوم نیست؛ زمان UTC تولیدشده برای ذخیره‌سازی از زمان پیام جداست.
5. جلوگیری از پیوند رویداد به لنگر ناموجود.
6. ایجاد پنج آزمون خودکار برای نوشتن/بازخوانی لنگر، حفظ چند لنگر مستقل، اتصال رویداد، رد لنگر ناموجود و نمایش صریح مرز ذخیره‌سازی.
7. افزودن گردش‌کار GitHub Actions برای اجرای آزمون‌ها با Python 3.12.
8. پس از نخستین اجرای موفق، هشدار منسوخ‌شدن startup event در FastAPI اصلاح شد و به handler مبتنی بر lifespan تبدیل شد؛ آزمون‌های نسخهٔ اصلاح‌شده باید با اجرای تازه تأیید شوند.

## شاهد آزمون اولیه

اجرای [HAIF Prototype Tests 39536183142](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39536183142) موفق بود: 5 آزمون گذشت. همان اجرا هشدار منسوخ‌شدن startup handler را نشان داد؛ این هشدار باعث اصلاح کد و آغاز اجرای دوم شد. نتیجهٔ اجرای دوم پس از اصلاح باید در این رویداد افزوده شود.

## مرزهای صریح

- این یک نمونهٔ اجرایی توسعه است، نه برنامهٔ تولیدی یا مستقرشده.
- ذخیره‌سازی فقط SQLite محلی است؛ مقصدهای Repository، Buffer، Persistent Memory، Library و Dropbox به‌عنوان مقصد دادهٔ برنامه متصل نشده‌اند.
- ضبط خودکار تمام گفتگوهای ChatGPT، احراز هویت، مجوزدهی، محدودسازی نرخ، مهاجرت پایگاه داده، پشتیبان‌گیری و بازیابی مستقل هنوز پیاده‌سازی نشده‌اند.
- گراف معنایی، صف داوری، Master–Child–Rahm و ارتقای کنترل‌شدهٔ دانش در مراحل بعدی قرار دارند.

## گام بعدی

1. تأیید اجرای آزمون پس از اصلاح lifespan.
2. ثبت نتیجهٔ نهایی و ممیزی پیوندهای مخزن.
3. افزودن قابلیت Artifact/Evidence با منشأ و نسخه.
4. سپس ساخت صف بازبینی و گراف رابطه‌ها، بدون حذف تاریخچه یا ارتقای خودکار موارد نامطمئن.


## Addendum — post-lifespan test run
- HAIF Prototype Tests [39536269368](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39536269368) completed SUCCESS on commit 3ca9aa9dd57bad84fcc2baa8b73c09cd40d4c225.
- Result: 5 passed, 1 warning, 0 failed. The deprecation warning for FastAPI startup events was removed by switching to a lifespan handler. One upstream Starlette/TestClient warning remains because the current stack recommends httpx2; it does not fail the tests and remains a small maintenance item.
- The tests cover anchor write/read-back and retrieval, preservation of two independent anchors, event-to-anchor linkage, rejection of unknown anchors, and disclosure that persistence is local-only.
- This is evidence for the prototype's current test scope, not production readiness, security validation, deployment or external persistence.
