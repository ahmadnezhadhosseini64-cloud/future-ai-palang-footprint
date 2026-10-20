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

## وضعیت پس از تکمیل زنجیرهٔ ثبت
- Canonical reference, section 9: updated and read-back matched; current fetched blob SHA recorded in the execution log.
- This event file: created and read-back matched; this status section is itself being updated to reflect the completed chain.
- Living reference, section 22: updated and read-back matched.
- Behavior trace: EVT-0018 entry present and read-back matched.
- Central 0.0 registry: EVT-0018 entry present and read-back matched.
- Current 0.0 anchor: now explicitly links EVT-0018; final read-back of the updated anchor is required before calling this last link verified.
- Architecture integration queue: explicit EVT-0018 section 22 added; final read-back/match is part of the current verification pass.
- Exact request timestamp: UNKNOWN / UNVERIFIED. Commit timestamp is a distinct event and must not be substituted.
- Buffer, Persistent Memory, Library and Dropbox: NOT VERIFIED by this repository chain. Dropbox failover remains OPEN / WAITING.
