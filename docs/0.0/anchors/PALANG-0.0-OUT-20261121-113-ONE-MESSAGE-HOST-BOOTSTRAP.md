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


## رسید خروجی و راستی‌آزمایی بسته — 2026-11-21

- پیام واحد در `prototype/haif-gpt6-starter/ONE_MESSAGE_HOST_BOOTSTRAP_FA.md` ثبت و در فهرست 18 فایل بسته canonical قرار گرفت.
- سند مادر زنده v1.7.76 در همان build checkout به ZIP کپی شد و تطبیق بایت paired-master PASS شد.
- نخستین اجرای کامل build روی source SHA `75a8f8399385b4b6fef7a4f3693da4a8c0b1fb08`: run `44871779034`, SUCCESS.
- نسخه داخلی starter: `0.4.2`; stable package ID و نام canonical ZIP بدون تغییر.
- ZIP: 236819 bytes; SHA-256 `aa989519d666d517bc01c23b75d2d773c67d2614688d454e089613cd8262e63b`.
- inventory: 18 files; CRC PASS; source-byte read-back PASS; artifact round-trip PASS; extracted tests 24/24 PASS.
- paired living master: 667106 bytes; SHA-256 `decf9700232c0a5d57249f18f0e3dbb183f1148210573bdc1d060feba1a96f72`; Git blob SHA `cd0e2e06b84eb38fcbf8af1e8c7ab332284882c8`, مطابق منبع مخزن.
- Stable release `haif-latest-verified` refreshed at `2026-11-21T05:38:14Z`; five assets published/read back as metadata. Workflow: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/44871779034
- وضعیت مستقل: target-host connection, persistent workspace, negative isolation tests و clean-host acceptance هنوز NOT RUN؛ package verification معادل host recovery نیست.
- پس از ثبت این رسید، آخرین pointer و receipt پایدار همچنان مرجع نسخه تحویل است؛ هر تغییر source بعدی باید مجدداً build و verify شود.


## شکست ثبت‌شده و اصلاح مسیر artifact — 2026-11-21

- Run `44871939090` روی source SHA `46137c4d325857556f813767e3d2b071d1ddcc12`: منبع و تست‌های استخراج‌شده 24/24 PASS و ZIP build PASS؛ اما مرحلهٔ دانلود artifact با lookup نامی `actions/download-artifact@v4` شکست خورد (`Artifact not found for name`). در نتیجه artifact round-trip و انتشار release در آن run اجرا نشدند؛ این run PACKAGE_VERIFIED نیست.
- اصلاح workflow: مرحلهٔ upload اکنون شناسهٔ واقعی artifact را از output همان step می‌گیرد و download با `artifact-ids` دقیق انجام می‌شود، نه lookup مبهم بر اساس نام.
- پس از اصلاح، فقط run جدیدی که artifact-id round-trip، digest، master byte match، CRC، inventory و تست‌ها را PASS کند می‌تواند latest release را refresh کند.


## اصلاح دوم artifact round-trip — 2026-11-21

- Run `44872027513`: package source tests 24/24 PASS، ZIP build و upload PASS و دانلود artifact با ID دقیق PASS؛ مرحلهٔ paired read-back به‌دلیل رفتار پیش‌فرض download-artifact در ایجاد زیرپوشه‌ای به نام artifact، فایل‌ها را در ریشهٔ مورد انتظار پیدا نکرد (`DOWNLOADED_ARTIFACT_MISSING_ZIP_RECEIPT_OR_MASTER`). انتشار release اجرا نشد؛ این run PACKAGE_VERIFIED نیست.
- اصلاح workflow: `merge-multiple: true` افزوده شد تا artifact واحد در مسیر مقصد ادغام و ساختار مورد انتظار verifier حفظ شود. سپس read-back سند مادر، digest، inventory، CRC و تست استخراج‌شده دوباره اجرا می‌شود.


## اصلاح زنجیرهٔ پیوندها — run 44872168517

- Run `44872168517` روی commit `f5b4b1d0729e40df8cce31b8a8230cc0d0c3349c`، بازیابی زنجیره را به‌علت نبود پیوند مستقیم OUT-113 به POINT-0/071 رد کرد. تست‌های package در آن run به‌دلیل شکست مرحلهٔ زنجیره، build نهایی را کامل نکردند.
- پیوند مستقیم OUT-113 → POINT-0/071 به نسخهٔ canonical OUT-113 افزوده می‌شود؛ سپس checker و package pipeline دوباره اجرا می‌شوند.


## اصلاح event marker — run 44872286383

- Run `44872286383` روی source commit `584a1cd3cecc660bfe5a5f7dd88a1e45bd89bde8`: زنجیرهٔ IN/OUT/CURRENT خوانده شد، اما checker رویداد را به‌دلیل نبود ارجاع صریح `POINT-0/071` در EVT-0289 رد کرد (`event_missing_marker_POINT-0/071`).
- فیلد Point صریح به هر دو mirror رویداد EVT-0289 افزوده شد؛ آزمون زنجیره باید مجدداً اجرا شود. این run نیز PACKAGE_VERIFIED نیست.


## اصلاح سوم artifact read-back — run 44872371185

- Run `44872371185`: زنجیرهٔ جاری و پیوندهای IN/OUT/EVT/TIME/CURRENT PASS؛ build و تست‌های بسته 24/24 PASS؛ upload artifact PASS. اما `actions/download-artifact@v4` با وجود ID معتبر artifact را پیدا نکرد (`None of the provided artifact IDs were found`) و round-trip/انتشار release انجام نشد. این run PACKAGE_VERIFIED نیست.
- اصلاح نهایی workflow: دریافت artifact از REST endpoint رسمی GitHub با همان artifact ID و `GITHUB_TOKEN` محدود به `actions: read` انجام می‌شود؛ سپس ZIP، receipt و سند مادر از آرشیو دانلودشده read-back و تطبیق می‌شوند. توکن فقط در محیط GitHub Actions است و وارد prompt، ZIP یا مخزن نمی‌شود.
