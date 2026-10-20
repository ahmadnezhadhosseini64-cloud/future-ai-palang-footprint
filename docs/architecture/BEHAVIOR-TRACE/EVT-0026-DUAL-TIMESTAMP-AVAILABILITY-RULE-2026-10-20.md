# EVT-0026 — تصویب و اتصال قاعدهٔ زمان‌گذاری دوگانه

- Event ID / شناسه رویداد: `EVT-0026-DUAL-TIMESTAMP-AVAILABILITY-RULE-2026-10-20`
- Stable ID / شناسه پایدار قاعده: `DUAL-TIMESTAMP-AVAILABILITY-RULE-2026-10-20-001`
- Production ID / شناسه تولید: `DTAR-2026-10-20-001`
- Version / نسخه: 1.0.0
- Date / تاریخ: 2026-10-20
- Status / وضعیت: ACTIVE / LIVING / GOVERNING
- Project timezone / منطقه زمانی پروژه: Asia/Tehran (UTC+03:30)
- Exact user-message time / زمان دقیق پیام کاربر: UNKNOWN / UNVERIFIED
- Rule anchor / لنگر قاعده: `PALANG-0.0-CURRENT-2026-10-20-001`
- Governing contract / قرارداد حاکم: [MRV Architecture and Living Reference Contract](../../reference/REFERENCE-DOCUMENTS/MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001.md)
- Living automation contract / قرارداد اتوماسیون زنده: [LIARC-2026-10-20-001](../../reference/REFERENCE-DOCUMENTS/LIVING-INTERACTION-AUTOMATION-AND-RECONCILIATION-2026-10-20-001.md)
- Related interaction anchor / لنگر تعامل مرتبط: [IAAR-2026-10-20-001](../../reference/REFERENCE-DOCUMENTS/INTERACTION-ANCHOR-AND-AUDIT-REASONING-2026-10-20-001.md)

## ورودی کاربر و تبصرهٔ جدید
کاربر مقرر کرد از این پس در ثبت‌های مهم، زمان مرجع دستیار/سامانه و زمان محلی تهران همزمان ثبت شوند، اگر هر دو واقعاً در دسترس باشند. اگر زمان محلی تهران در دسترس نباشد، باید زمان دقیق مرجع دستیار ثبت شود و زمان تهران صریحاً UNKNOWN / UNAVAILABLE باشد. این قاعده نباید باعث ساختن زمان، تخمین منطقهٔ زمانی، یا جایگزینی زمان پیام کاربر با زمان ثبت/commit/workflow شود.

## قاعدهٔ اجرایی
1. `Assistant/system reference time (UTC)`: زمان دقیق از منبع ساعت واقعاً در دسترس، با نام منبع و منطقهٔ زمانی.
2. `Tehran local time (Asia/Tehran)`: زمان دقیق تهران از منبع زمانی واقعاً در دسترس.
3. اگر زمان تهران در دسترس نبود: `UNKNOWN / UNAVAILABLE`; زمان مرجع دستیار حفظ شود.
4. اگر زمان مرجع دستیار در دسترس نبود: آن نیز `UNKNOWN / UNAVAILABLE`; هیچ زمان ساختگی مجاز نیست.
5. اگر یک زمان از مهر زمانی دیگر تبدیل شده، صریحاً `converted/derived` نوشته شود و مشاهدهٔ مستقل قلمداد نشود.
6. زمان پیام کاربر، زمان ثبت سند، زمان commit، زمان read-back و زمان اجرای workflow پنج نوع شاهد جدا هستند.
7. چرخهٔ اجرا: `CAPTURE → LABEL SOURCE/TZ → RECORD BOTH OR MARK UNAVAILABLE → READ-BACK → MATCH → VERIFY`.
8. قاعده به قرارداد مادر، قرارداد تعامل زنده، لنگر IAAR، نمایهٔ مرجع و صف بازیابی پیوند می‌خورد و برای ثبت‌های بعدی به ارث می‌رسد. این قاعده زمان‌های تاریخی گمشده را به‌صورت گذشته‌نگر جعل یا تکمیل نمی‌کند.

## مهر زمانی اجرای ثبت تبصره
- Tehran local time: `2026-10-20 19:23:21 +03:30`, from the time source available in this turn.
- UTC reference: `2026-10-20 15:53:21Z`, converted/derived from the same timestamp; not an independent second clock observation.
- Exact user-message timestamp: `UNKNOWN / UNVERIFIED`.
- Repository commit timestamps created by this documentation update must be recorded separately from the implementation timestamp above.

## پیوندهای معماری و وضعیت
- Reference rule included in: [IAAR reference](../../reference/REFERENCE-DOCUMENTS/INTERACTION-ANCHOR-AND-AUDIT-REASONING-2026-10-20-001.md), [LIARC](../../reference/REFERENCE-DOCUMENTS/LIVING-INTERACTION-AUTOMATION-AND-RECONCILIATION-2026-10-20-001.md), [MRV contract](../../reference/REFERENCE-DOCUMENTS/MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001.md).
- Index: [Reference Index](../../REFERENCE_INDEX.md).
- Recovery queue: [Open Gaps and Recovery Register](../INTEGRATION-QUEUE/OPEN-GAPS-RECOVERY-REGISTER-2026-10-15-001.md).
- Verification state: implementation has been written to repository documents; read-back verification remains to be performed after this event is committed.
- Open follow-up: ensure future registration templates and automations capture both timestamp fields and explicitly mark unavailable values; do not close the audit failures tracked by issue #18.
