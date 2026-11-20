# EVT-0286 — ثبت معماری اتصال چندمیزبانی و تکامل تحت حاکمیت مالک

- Event ID: EVT-0286
- Status: ACTIVE / LIVING / REPOSITORY-REGISTERED
- Parent: POINT-0/068
- Input: IN-111
- Output: OUT-110
- Governing architecture: [Multi-host governed evolution architecture](../مدل%20اولیه%20AI/معماری%20اتصال%20چندمیزبانی%20و%20تکامل%20تحت%20حاکمیت%20مالک.md)
- Master reference: سند مرجع مادر مدل اولیه هوش مصنوعی
- Next checkpoint: CURRENT-121
- Sole queue: NEXT-051

## User intent
میزبان‌های متعدد به مخزن شخصی متصل شوند تا تجربه، بازخورد، خطا و پیشنهادهایشان در تکامل HAIF سهم داشته باشد؛ اما هیچ میزبان مستقلاً معماری را تغییر ندهد و همه‌چیز تحت اختیار و نظارت مالک باقی بماند.

## Actions
1. معماری چندمیزبانی و مسیر یک‌طرفهٔ پیشنهاد به پذیرش تعریف شد.
2. Host Registry، سطوح دسترسی، Evidence Envelope، قرنطینه، تطبیق میان میزبان‌ها، اعتبارسنجی RAHM، نامزد CHILD و دروازهٔ تأیید مالک تعریف شد.
3. کنترل حریم خصوصی، امنیت credential، حفاظت main، ممیزی و لغو اتصال ثبت شد.
4. نقطه، ورودی/خروجی و پیوند به سند مادر ثبت شدند.
5. وضعیت پیاده‌سازی از وضعیت طراحی جدا نگه داشته شد.

## Verification boundary
ثبت سند و معماری قابل بازخوانی است. اتصال واقعی میزبان، API ورودی، branch protection و clean-host recovery با این رویداد اثبات نمی‌شوند و OPEN / NOT RUN باقی می‌مانند.

## Time
زمان دقیق پیام کاربر UNKNOWN / UNVERIFIED. زمان رویداد باید فقط از commit واقعی Git این فایل استخراج و در TIME-BINDING-EVT-0286 ثبت شود.