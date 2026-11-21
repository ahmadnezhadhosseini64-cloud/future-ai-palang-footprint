# OUT-113 — قرارداد و پیام واحد راه‌اندازی میزبان GPT

- Parent: IN-114
- Status: ONE-MESSAGE BOOTSTRAP SPEC REGISTERED / PACKAGE SOURCE UPDATED
- Result: CI BUILD AND TARGET-HOST EXECUTION PENDING

خروجی ثبت‌شده:
- ایجاد `prototype/haif-gpt6-starter/ONE_MESSAGE_HOST_BOOTSTRAP_FA.md` به‌عنوان تنها پیام قابل ارسال به میزبان GPT جدید؛
- تعریف اتصال خواندنی فقط به مخزن رسمی `ahmadnezhadhosseini64-cloud/future-ai-palang-footprint`؛
- بازیابی و تطبیق HEAD، latest-verified pointer، رسید، SHA-256، سند مادر، ZIP، inventory، CRC و تست‌های استخراج‌شده؛
- تعریف workspace خصوصی runtime با CHARTER، INBOX، OBSERVATIONS، PROPOSALS، TESTS، RECEIPTS، DECISIONS و SNAPSHOT؛
- منع استفاده از پوشه داخل مخزن مشترک به‌عنوان مرز امنیتی و منع credential نوشتن مستقیم روی main/MASTER؛
- صدور Host ID/Workspace ID/Session ID فقط بر پایه اطلاعات واقعی؛
- حفظ 0 و 0+/0++ به‌عنوان یک ریشه canonical و حفظ 0.0 به‌عنوان ادامه والددار؛
- ثبت تعامل واقعی با جفت IN/OUT یا رویداد شکست و رسید read-back؛
- تصریح اینکه مجوز connector، ابزار اجرا، workspace پایدار و پذیرش میزبان باید در محیط مقصد واقعاً آزمون شوند.

گیت‌های باز: اجرای پیام در میزبان مقصد، مجوز واقعی GitHub، provisioning workspace پایدار، آزمون منفی جداسازی، receipt end-to-end و پذیرش مستقل میزبان.
