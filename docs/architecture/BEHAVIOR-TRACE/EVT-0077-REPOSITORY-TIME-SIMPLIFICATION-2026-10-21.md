# EVT-0077 — ساده‌سازی قاعدهٔ زمان ثبت مخزن

- Stable ID / شناسهٔ پایدار: `EVT-0077-REPOSITORY-TIME-SIMPLIFICATION-2026-10-21`
- Production ID / شناسهٔ تولید: `EVT-RTS-2026-10-21-001`
- Version / نسخه: 1.0.0
- Project: Future AI / Palang Footprint / HAIF
- Owner: احمد پلنگ
- Parent reference: [سند مرجع ساده‌سازی زمان](../../reference/REFERENCE-DOCUMENTS/REPOSITORY-TIME-ANCHOR-SIMPLIFICATION-LIVING-REFERENCE-2026-10-21-001.md)
- Independent anchor: [لنگر ۰.۰ مستقل](../../0.0/REPOSITORY-TIME-ANCHOR-SIMPLIFICATION-0.0-2026-10-21-001.md)
- Interaction time available: `2026-10-21T17:22:00Z` UTC = `2026-10-21T20:52:00+03:30` Asia/Tehran; supplied contextual time, not commit time and not verified user-message metadata.
- Exact user-message timestamp: `UNAVAILABLE / NOT CAPTURED`.
- Status before write: DECISION CAPTURED; repository proof pending.

## Input / ورودی
کاربر خواست ثبت کامل انجام شود، لنگر زمانی و لنگر مستقل ساخته شود و قاعدهٔ زمان در عملیات ثبت اصلاح و فعال بماند. توضیح محوری: معیار اصلی فقط زمان ثبت در مخزن است؛ UTC مرجع و تهران معادل آن. زمان‌های دیگر که قبلاً در جاهای مختلف ثبت می‌شدند حذف نمی‌شوند، اما فقط برای معنای مستقل خود باقی می‌مانند و نباید چند معیار زمانی رقیب بسازند. معماری نباید بی‌دلیل پیچیده شود.

## Decision / تصمیم
1. برای هر فایل مخزن، زمان آخرین commit تغییر‌دهندهٔ همان فایل معیار ثبت است.
2. UTC نخست ثبت می‌شود؛ زمان تهران از همان instant و با `Asia/Tehran` مشتق می‌شود.
3. زمان پیام/رخداد/آزمون/عملیات اگر شاهد مستقل دارد حفظ می‌شود، اما زمان ثبت مخزن جایگزین آن نیست.
4. ثبت اجباری چند timestamp برای همهٔ مراحل هر مورد حذف می‌شود؛ فقط زمان‌های دارای معنای مستقل و موردنیاز باقی می‌مانند.
5. هیچ زمان گمشده‌ای حدس زده نمی‌شود.
6. این تصمیم به معنی اصلاح سیاست است؛ کامل‌بودن اصلاح در تمام فایل‌های تاریخی تا اجرای ممیزی و read-back جداگانه OPEN است.

## Evidence / شواهد
- Existing governing standard: `docs/architecture/GOVERNANCE/ASSISTANT-TIMESTAMP-ANCHOR-STANDARD-2026-10-21-001.md`, which already contains amendment 1.2.0 stating repository registration time is canonical.
- New standalone reference and 0.0 recovery anchor are linked above.
- Exact repository commit timestamp and read-back timestamp for this event must be obtained from actual GitHub metadata/tool results; do not substitute the contextual interaction time.
- User-message exact timestamp: UNAVAILABLE / NOT CAPTURED.

## Acceptance / معیار پذیرش
- [ ] Event file written to repository.
- [ ] Event fetched back; key ID, decision and links match.
- [ ] Independent 0.0 anchor fetched back.
- [ ] Reference index and governance standard linked/updated as needed.
- [ ] Actual commit UTC and derived Tehran recorded from repository metadata.
- [ ] Buffer and Persistent Memory status checked independently or left UNVERIFIED.

## Status / وضعیت
OPEN until repository write/read-back and commit-time evidence are verified. Buffer, Persistent Memory, Library and Dropbox remain unverified unless separate evidence is captured.
