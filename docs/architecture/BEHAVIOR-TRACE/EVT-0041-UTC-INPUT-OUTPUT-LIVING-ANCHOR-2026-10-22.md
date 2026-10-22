# EVT-0041 — تثبیت قاعدهٔ UTC ورودی تا خروجی و نقطهٔ ۰.۰ تازه

- Stable ID: `PALANG-EVT-0041-UTC-INPUT-OUTPUT-LIVING-ANCHOR-2026-10-22-001`
- Production ID: `EVT41-HAIF-UILA-2026-10-22-001`
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EVOLVABLE
- Parent: EVT-0040
- Governing reference: [UTC INPUT→OUTPUT LIVING ANCHOR (UILA)](../../reference/REFERENCE-DOCUMENTS/UTC-INPUT-TO-OUTPUT-INTERACTION-ANCHOR-LIVING-GOVERNANCE-2026-10-22-001.md)
- New 0.0 anchor: [PALANG-0.0-UTC-INPUT-TO-OUTPUT-BEHAVIOR-ANCHOR-2026-10-22-001](../../0.0/anchors/PALANG-0.0-UTC-INPUT-TO-OUTPUT-BEHAVIOR-ANCHOR-2026-10-22-001.md)

## ورودی
درخواست کاربر برای پابند کردن رفتار آینده به UTC ورودی تا خروجی؛ ثبت ورودی/خروجی تعاملی، جست‌وجو و رفتار قابل مشاهده، لنگر زمانی و مستقل، نام جدید، سند مرجع کامل و نقطهٔ ۰.۰ تازه؛ همچنین درخواست ثبت نسخهٔ نهایی در Gmail.

## خروجی و تصمیم معماری
نام جدید: **UTC INPUT→OUTPUT LIVING ANCHOR (UILA)** — «لنگر زندهٔ UTC از ورودی تا خروجی».
قاعدهٔ ثبت شدنی: زمان مرجع ثبت مخزن = زمان واقعی آخرین commit بر حسب UTC؛ زمان تهران از همان لحظه مشتق می‌شود. زمان دریافت ورودی، پاسخ، اجرای ابزار، جست‌وجو، ثبت و بازخوانی از یکدیگر جدا می‌مانند. مدت تفکر داخلی به‌عنوان telemetry قابل‌مشاهده نیست و نباید ساختگی ثبت شود؛ فقط زمان‌های واقعی قابل مشاهده و تأخیر سرتاسری، در صورت وجود دو timestamp معتبر، قابل محاسبه است.

## لنگر مستقل
- Event: EVT-0041.
- Stable ID: `PALANG-EVT-0041-UTC-INPUT-OUTPUT-LIVING-ANCHOR-2026-10-22-001`.
- 0.0: `PALANG-0.0-UTC-INPUT-TO-OUTPUT-BEHAVIOR-ANCHOR-2026-10-22-001`.
- Previous anchors: PRESERVED; no replacement or closure.
- Input timestamp UTC: UNKNOWN / NOT EXPOSED by current tools.
- Output timestamp UTC: UNKNOWN / NOT EXPOSED as an independent host event.
- Internal thinking duration: NOT EXPOSED / NOT MEASURED.
- Repository canonical time: actual last-change commit UTC; Tehran equivalent computed from same instant. Initial event commit: UTC `2026-10-22T06:38:32Z`; Tehran `2026-10-22 10:08:32`.

## مقصدها
- Repository: WRITE=PASS / READ-BACK=PASS / MATCH=PASS; the event file and cross-links were fetched after commit and identifiers/status matched.
- Library: pending independent write/read-back for this new reference.
- Gmail: BLOCKED / NOT VERIFIED based on current connector evidence in EVT-0039; no message sent or retrieved in this operation.
- Buffer / Persistent Memory: NOT VERIFIED.
- Dropbox: OPEN / NOT VERIFIED.

## اقدام بعدی
1. Repository event, reference and 0.0 anchor were written and independently read back; matching IDs and links verified.
2. پیوند دادن به سند مادر، نمایهٔ ۰.۰ و صف کارها.
3. بارگذاری و بازخوانی Library در صورت امکان.
4. ادامهٔ `GMAIL-CONNECTION-AND-READBACK-01` فقط با دسترسی ایمیل مجاز؛ سپس بازیابی همان پیام و تطبیق آن.
5. این الگو برای تعامل‌های آیندهٔ پروژه اعمال و با شواهد نسخه‌بندی‌شده توسعه یابد.

اصل: `REQUESTED ≠ WRITTEN ≠ READ-BACK ≠ VERIFIED`; `OBSERVABLE LATENCY ≠ INTERNAL THINKING DURATION`.
