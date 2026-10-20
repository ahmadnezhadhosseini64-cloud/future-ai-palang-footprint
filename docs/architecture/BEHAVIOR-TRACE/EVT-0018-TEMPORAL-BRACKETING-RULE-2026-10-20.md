# EVT-0018 — قاعدهٔ ثبت محصور بین دو لنگر زمانی

- Event ID: EVT-0018-TEMPORAL-BRACKETING-RULE-2026-10-20
- Stable ID: TEMPORAL-BRACKETING-AND-BOUNDED-TIMESTAMP-GOVERNANCE-2026-10-20-001
- Production ID: TBBTG-HAIF-2026-10-20-001
- Version: 1.0.0
- Project: Future AI / Palang Footprint — HAIF
- Owner: احمد پلنگ / Ahmad Nezhadhosseini
- Source: درخواست کاربر در گفت‌وگوی جاری، 2026-10-20
- Exact request timestamp: UNKNOWN / UNVERIFIED؛ از زمان commit استنتاج نمی‌شود.
- Repository: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint, branch main

## درخواست
وقتی زمان دقیق رویداد در دسترس نیست، اگر ثبت زمان‌دار معتبر پیش و پس از آن وجود دارد، رویداد در فاصلهٔ میان آن دو ثبت شود تا جایگاه زمانی‌اش قابل بازیابی باشد.

## قاعده
- لنگر زمانی قبل: شناسه، زمان معتبر، منطقهٔ زمانی، منبع و شاهد.
- لنگر زمانی بعد: شناسه، زمان معتبر، منطقهٔ زمانی، منبع و شاهد.
- بازهٔ رویداد: در فاصلهٔ دو لنگر، فقط در صورتی که ترتیب با شواهد اثبات شود.
- زمان دقیق رویداد: همچنان UNKNOWN / UNVERIFIED مگر شاهد مستقل وجود داشته باشد.
- زمان میانی یا ساعت و دقیقهٔ حدسی ممنوع است.
- اگر فقط یک لنگر معتبر باشد، مرز یک‌طرفه ثبت شود؛ اگر ترتیب اثبات نشود، بازه قطعی اعلام نشود.
- زمان پیام، commit، تغییر فایل، بازخوانی و تأیید مستقل‌اند و جای یکدیگر را نمی‌گیرند.
- اگر بعداً شاهد دقیق‌تر به دست آمد، با منشأ و تاریخچه اضافه شود؛ عدم‌قطعیت قبلی بی‌ردپا پاک نشود.

## چرخه و معیار پذیرش
PRESERVE → IDENTIFY → FIND PRECEDING ANCHOR → FIND FOLLOWING ANCHOR → PROVE ORDER → REGISTER BOUNDED INTERVAL → LINK SOURCES → READ-BACK → MATCH → VERIFY.

معنی: حفظ → شناسایی → یافتن لنگر قبل → یافتن لنگر بعد → اثبات ترتیب → ثبت بازه → پیوند شواهد → بازخوانی → تطبیق → تأیید.

برای پذیرش باید شناسهٔ رویداد، دو لنگر و زمان معتبرشان، منطقهٔ زمانی، بازه، شاهد ترتیب، محدودیت دقت و پیوندهای بازیابی ثبت و بازخوانی شوند. این رویداد به‌خودی‌خود زمان دقیق پیام فعلی را ثابت نمی‌کند.

## مراجع
- [سند مرجع جامع حاکم](../../reference/REFERENCE-DOCUMENTS/PERMANENT-LIVING-EXECUTION-ANCHOR-TIMESTAMP-GOVERNANCE-2026-10-20-001.md)
- [مرجع حاکم زنده](../../reference/REFERENCE-DOCUMENTS/UNIFIED-OUTPUT-ANCHOR-REGISTRATION-LIVING-REFERENCE-2026-10-19-001.md)
- [دفتر رفتار](./INTERACTION-BEHAVIOR-TRACE-2026-10-19-001.md)
- [دفتر مرکزی ۰.۰](../../0.0/README.md)
- [لنگر جاری ۰.۰](../../../checkpoints/PALANG-0.0-CURRENT-2026-10-20-001.md)

## وضعیت ثبت و راستی‌آزمایی نهایی
- نتیجهٔ بازخوانی نهایی: هر هفت فایل زیر از شاخهٔ main بازیابی و محتوای قاعده/شناسه/پیوندها بررسی شد.
- سند مرجع جامع: `docs/reference/REFERENCE-DOCUMENTS/PERMANENT-LIVING-EXECUTION-ANCHOR-TIMESTAMP-GOVERNANCE-2026-10-20-001.md` — blob SHA: `3d20de2c378f7ef189d22b56edc8f8c2ec1ab972`; پیوند EVT-0018 در بخش 9.1 موجود است.
- مرجع زنده: `docs/reference/REFERENCE-DOCUMENTS/UNIFIED-OUTPUT-ANCHOR-REGISTRATION-LIVING-REFERENCE-2026-10-19-001.md` — blob SHA: `89013a69c265dee6da1010d02c764cbed82ce5f9`; بخش 22 موجود است.
- این رویداد: `docs/architecture/BEHAVIOR-TRACE/EVT-0018-TEMPORAL-BRACKETING-RULE-2026-10-20.md` — blob SHA این نسخه: `4d640860dd2ba944479a702ebbb4dd38dc3312f4`; شناسه‌ها، قاعده و مسیر بازیابی بازخوانی شدند.
- دفتر رفتار: `docs/architecture/BEHAVIOR-TRACE/INTERACTION-BEHAVIOR-TRACE-2026-10-19-001.md` — blob SHA: `c07951a545803285e8c64fa6d09b5a3cfe660b71`; ورودی EVT-0018 موجود است.
- دفتر 0.0: `docs/0.0/README.md` — blob SHA: `f7734352274f43d1be1952eb9eb181639f95f5c1`; ورودی EVT-0018 موجود است.
- لنگر جاری 0.0: `checkpoints/PALANG-0.0-CURRENT-2026-10-20-001.md` — blob SHA: `75bcf926365811e26873069792be8d652cbcd2db`; پیوند EVT-0018 موجود است.
- صف معماری: `docs/architecture/INTEGRATION-QUEUE/README.md` — blob SHA: `e58c9422ba7711258caec35dcc111746c5dd5908`; بخش 22 موجود است.
- زمان دقیق پیام درخواست: UNKNOWN / UNVERIFIED؛ از زمان commit استنتاج نشده است.
- وضعیت مقصدها: مخزن (Repository) — بازخوانی و تطبیق این زنجیره انجام شد؛ بافر، حافظهٔ پایدار، کتابخانه و Dropbox — مستقلاً تأیید نشده‌اند. لنگر Dropbox همچنان OPEN / WAITING است.
- نتیجه: پیوندهای مخزن برای این قاعده ثبت و تطبیق شدند. این نتیجه به معنی ذخیره یا تأیید در مقصدهای دیگر نیست.
