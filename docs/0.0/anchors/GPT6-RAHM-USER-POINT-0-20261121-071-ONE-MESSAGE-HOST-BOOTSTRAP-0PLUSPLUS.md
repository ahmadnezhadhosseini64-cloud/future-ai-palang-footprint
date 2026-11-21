> QUARANTINED_DUPLICATE_ID_NONCANONICAL — این فایل یک ثبت موازی با شناسهٔ POINT-0/071 است و ریشه یا نقطهٔ فعال جداگانه نیست. مرجع canonical: [POINT-0/071](GPT6-RAHM-USER-POINT-0-20261121-071-SINGLE-MESSAGE-GPT6-HOST-BOOTSTRAP-0PLUS.md) و [CURRENT-124](PALANG-0.0-CURRENT-20261121-124-SINGLE-MESSAGE-GPT6-HOST-BOOTSTRAP.md).

# POINT-0/071 — نشانگر 0++ و راه‌اندازی یک‌پیامی میزبان GPT

- Status: ACTIVE / LIVING / APPEND-ONLY / CI BUILD PENDING
- Canonical root: POINT-0 (0 is the sole root identity)
- Marker semantics: 0+ and 0++ are highlights/production-readiness markers on the same root; neither is a new point/root.
- Parent checkpoint: CURRENT-123
- Parent point: POINT-0/070
- Input/output: IN-114 → OUT-113
- Event/time: EVT-0289 → TIME-BINDING-EVT-0289
- Living master target: v1.7.76
- Portable starter target: stable identity HAIF-GPT6-PORTABLE-STARTER-20261025-004; next internal version 0.4.2
- Canonical ZIP filename remains unchanged: haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip
- Sole execution queue: NEXT-051
- Owner: احمد پلنگ
- Repository: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint

## تصمیم
یک پیام واحد باید میزبان GPT جدید را برای اتصال خواندنی به مخزن رسمی، بازیابی آخرین نسخه، آزمون بسته و ساخت workspace خصوصی خودش راه‌اندازی کند. میزبان جدید یک میزبان GPT دیگر است؛ پیام معتبر معماری را منتقل می‌کند و نیاز به بازگویی تاریخچه را حذف می‌کند.

## مرز واقعی
پیام واحد مجوز OAuth، connector، filesystem، sandbox پایدار یا branch protection را ایجاد نمی‌کند. اگر هرکدام در محیط مقصد موجود نباشد، میزبان باید وضعیت واقعی را BLOCKED/NOT CONNECTED/NOT RUN اعلام کند. فقط مخزن رسمی انتخاب می‌شود؛ هیچ توکن یا secret در پیام/ZIP ذخیره نمی‌شود.

## workspace
workspace باید در فضای خصوصی و مستقل runtime میزبان باشد، نه صرفاً پوشه‌ای در مخزن مشترک. Host ID، Workspace ID و Session ID فقط پس از مشاهده واقعی هویت میزبان صادر می‌شوند. اتصال پیش‌فرض READ-ONLY است. Host Registry تا پذیرش واقعی و تصمیم مالک خالی می‌ماند.

## بسته و سند
پیام واحد در `prototype/haif-gpt6-starter/ONE_MESSAGE_HOST_BOOTSTRAP_FA.md` اضافه می‌شود. همان ZIP canonical با stable identity و filename موجود بازسازی می‌شود؛ نسخه داخلی هدف 0.4.2 است. سند مادر به 1.7.76 append-only ارتقا می‌یابد. هیچ ZIP موازی یا نام‌گذاری نسخه‌ای جدید ساخته نمی‌شود.

## ثبت ورودی/خروجی
در صورت وجود producer و مسیر مجاز، هر تعامل واقعی میزبان با IN/OUT مستقل، event، parent lineage، timestamp قابل اثبات یا UNKNOWN، digest و read-back receipt ثبت می‌شود. ثبت تعامل به‌تنهایی دانش را به MASTER ارتقا نمی‌دهد. ارتقا نیازمند QUARANTINE، RAHM، CHILD و تأیید صریح مالک است.

## وضعیت آزمون
ثبت اسناد و source changes به‌تنهایی به معنی بسته آماده نیست. بسته فقط پس از CI روی source SHA دقیق، تطبیق بایت master، ZIP CRC، inventory، digest، artifact round-trip و تست‌های استخراج‌شده PACKAGE_VERIFIED می‌شود. اتصال و بازیابی میزبان مستقل پس از دریافت receipt واقعی از میزبان مقصد جداگانه ارزیابی خواهد شد.

## زنجیره
POINT-0/070 → IN-114 → OUT-113 → EVT-0289 → TIME-BINDING-EVT-0289 → CURRENT-124 → NEXT-051.
