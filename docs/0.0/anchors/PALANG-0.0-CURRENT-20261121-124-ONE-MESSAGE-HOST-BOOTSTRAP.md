# CURRENT-124 — راه‌اندازی یک‌پیامی میزبان GPT و نشانگر 0++

- Status: ACTIVE / LIVING / SOURCE UPDATE REGISTERED; PACKAGE VERIFICATION PENDING
- Previous checkpoint: CURRENT-123
- Current point: POINT-0/071 (0++ marker on canonical root point 0; not a new root)
- Input/output: IN-114 → OUT-113
- Event/time: EVT-0289 → TIME-BINDING-EVT-0289
- Living master target: v1.7.76
- Starter package target: internal 0.4.2; stable identity and canonical ZIP filename unchanged
- Sole execution queue: NEXT-051
- Repository: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint

## ثبت
پیام واحد راه‌اندازی میزبان در منبع starter اضافه شد. دستور واحد باید اتصال خواندنی به فقط مخزن رسمی، بازیابی آخرین release pointer/receipt، تطبیق سند مادر و ZIP، استخراج و اجرای تست‌ها، و ساخت workspace خصوصی runtime میزبان را orchestrate کند.

## مرز و وضعیت
- 0، 0+ و 0++ همان ریشه canonical هستند؛ 0++ فقط نشانگر برجسته‌سازی آمادگی به‌روزرسانی/تحویل است.
- 0.0 ادامه والددار همان ریشه است.
- Host workspace باید در فضای خصوصی میزبان باشد؛ پوشه در مخزن عمومی/مشترک کنترل دسترسی مستقل ایجاد نمی‌کند.
- اتصال پیش‌فرض READ-ONLY؛ هیچ credential نوشتن مستقیم به main/MASTER/release/workflow/registry مجاز نیست.
- یک پیام نمی‌تواند OAuth، connector، ابزار اجرا یا sandbox پایدار را ایجاد کند؛ نبود آن‌ها باید صریح گزارش شود.
- Host Registry تا هویت و پذیرش واقعی خالی می‌ماند.
- ثبت هر تعامل فقط با producer/adapter مجاز، durable write و read-back receipt اثبات می‌شود؛ عدم ثبت نیز به‌عنوان gap ثبت می‌شود.
- اتصال واقعی میزبان، workspace پایدار، آزمون منفی جداسازی و بازیابی clean-host هنوز NOT RUN هستند.

## لنگر زمانی
زمان canonical این checkpoint از GitHub commit metadata و فایل TIME-BINDING-EVT-0289 خوانده می‌شود؛ زمان دقیق پیام اصلی کاربر به‌صورت مستقل در دسترس نیست و UNKNOWN باقی می‌ماند.

## زنجیره
POINT-0/070 → IN-114 → OUT-113 → EVT-0289 → TIME-BINDING-EVT-0289 → CURRENT-124 → NEXT-051.
