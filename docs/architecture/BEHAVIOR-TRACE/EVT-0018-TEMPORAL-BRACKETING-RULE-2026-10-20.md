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

## وضعیت ثبت و راستی‌آزمایی
- Canonical reference: section 9 contains the governing rule; section 9.1 now explicitly links EVT-0018 and recovery destinations. The latest subsection is awaiting the final fetch-and-match pass.
- Living reference: section 22 contains the temporal bracketing rule and was read back in the preceding audit.
- Behavior trace: EVT-0018 entry is present and was read back in the preceding audit.
- Central 0.0 registry: EVT-0018 entry is present and was read back in the preceding audit.
- Current 0.0 anchor: explicit EVT-0018 link was fetched and matched in the preceding audit; current anchor blob SHA observed: 75bcf926365811e26873069792be8d652cbcd2db.
- Architecture integration queue: section 22 explicitly indexes EVT-0018 and was fetched and matched in the preceding audit; blob SHA observed: e58c9422ba7711258caec35dcc111746c5dd5908.
- Exact request timestamp: UNKNOWN / UNVERIFIED. Commit timestamp is distinct and must not be substituted.
- Buffer, Persistent Memory, Library and Dropbox: NOT VERIFIED by this repository chain. Dropbox failover remains OPEN / WAITING.
- Final acceptance: fetch the latest canonical reference, this event file, living reference, behavior trace, 0.0 registry, current anchor and queue index; verify IDs, links and temporal rule. Keep any mismatch OPEN / PENDING.
