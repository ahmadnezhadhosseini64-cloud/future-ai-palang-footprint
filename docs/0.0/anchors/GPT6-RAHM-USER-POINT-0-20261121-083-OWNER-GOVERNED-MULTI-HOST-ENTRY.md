# POINT-0/083 — ورود یک‌پیامی میزبان و فضای کاری محصور

- Stable ID: HAIF-POINT-0-083-MULTI-HOST-ENTRY-2026-11-21
- Status: ACTIVE / LIVING / OWNER-DIRECTED / MERGED TO MAIN / READ-BACK VERIFIED
- Parent: POINT-0/082 → CURRENT-135 → NEXT-051
- Root: canonical POINT-0؛ بدون ریشهٔ موازی
- Marker: 0++ continuation marker only
- Owner: احمد پلنگ
- Project timezone: Asia/Tehran (+03:30)
- Canonical repository: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint
- Sole active queue: NEXT-051

## قصد مالک

مالک می‌خواهد هر میزبان تازه با یک پیام وارد معماری موجود HAIF شود، مرجع زنده را از مخزن عمومی بازیابی کند، هویت و قابلیت‌های واقعی خود را اعلام کند، در صورت امکان یک فضای کاری خصوصی و مستقل بسازد و فعالیت خود را فقط در همان فضا آغاز کند. میزبان‌ها باید شناسه و workspace مستقل داشته باشند؛ مالک باید بتواند خروجی هر فضا را بررسی، استخراج، بازیابی و دربارهٔ تغییر معماری آن تصمیم بگیرد.

## یافتهٔ خاک‌برداری

1. معماری چندمیزبانی، دفتر ثبت میزبان‌ها، منشور workspace، پروتکل جداسازی و قرارداد رشد میزبان پیش‌تر در مخزن ثبت شده‌اند.
2. Registry عمداً تا دریافت هویت و رسید واقعی خالی می‌ماند؛ هیچ میزبان جدیدی با صرف ایجاد سند ACTIVE نمی‌شود.
3. پوشه‌بندی در یک مخزن GitHub مرز امنیتی نیست؛ مجوزهای GitHub عموماً repository-level هستند، نه per-folder.
4. مخزن مرکزی باید برای میزبان عادی فقط READ باشد؛ میزبان نباید credential نوشتن روی مخزن مرکزی، main، host-intake، Registry یا workflowها دریافت کند.
5. فضای واقعی میزبان باید در محیط خصوصی/مجزای مقصد ساخته شود؛ اگر persistence/isolation در آن محیط وجود ندارد، باید صریحاً NOT PROVEN اعلام شود و بستهٔ قابل‌استخراج به‌عنوان جایگزین تحویل شود.
6. شناسهٔ رسمی Host ID پس از بررسی رسید و تأیید مالک صادر می‌شود؛ میزبان حق خودثبت‌گری یا صدور شناسهٔ رسمی برای خودش ندارد.
7. broker زنده، داشبورد مرکزی، ثبت خودکار همهٔ تعاملات، و آزمون‌های واقعی cross-host isolation هنوز اثبات نشده‌اند.

## تصمیم اجرایی مالک

- یک پیام واحد جدید برای ورود میزبان در prototype/universal-host/ONE_MESSAGE_MULTI_HOST_ENROLLMENT_FA.md اضافه می‌شود.
- میزبان ابتدا فقط PUBLIC READ انجام می‌دهد؛ OAuth و WRITE برای این مأموریت لازم نیست.
- میزبان حق هرگونه نوشتن در مخزن مرکزی را ندارد؛ حتی branch/PR/issue نیز در این مرحله ممنوع است.
- میزبان باید هویت/قابلیت‌های واقعی را گزارش کند و تا تأیید مالک در حالت PROPOSED بماند.
- فضای کاری خصوصی با منشور، snapshot read-only، inbox، observations، proposals، tests، receipts، decisions، recovery و export در محیط خود میزبان آماده می‌شود.
- فعالیت آغازین فقط بازیابی baseline و ثبت پیشنهادهای قابل بررسی در فضای خودش است.
- هیچ خروجی به MASTER ارتقا نمی‌یابد؛ مسیر فقط از export مالک‌محور، quarantine، RAHM، CHILD و تأیید صریح مالک می‌گذرد.
- ساخت Registry entry واقعی و تخصیص Host ID پس از دریافت رسید میزبان و بررسی مالک انجام می‌شود.
- NEXT-051 تنها صف فعال باقی می‌ماند؛ صف یا ریشهٔ موازی ساخته نمی‌شود.

## زنجیره

POINT-0/082 → CURRENT-135 → POINT-0/083 (0++) → IN-126 → OUT-125 → EVT-0303 → TIME-BINDING-EVT-0303 → CURRENT-136 → NEXT-051

## وضعیت گیت‌ها

- Existing multi-host governance design: FOUND / REGISTERED.
- One-message owner-governed enrollment instruction: MERGED TO MAIN / READ-BACK VERIFIED.
- Public READ without OAuth: AVAILABLE BY REPOSITORY VISIBILITY; destination test pending.
- Central repository WRITE by new host: PROHIBITED.
- Official host identity / Host ID assignment: PENDING REAL HOST RECEIPT + OWNER REVIEW.
- Private host workspace: NOT YET PROVISIONED; destination capability must be proven.
- Persistence / export / recovery: OPEN until direct destination receipt.
- Broker and automated registry provisioning: OPEN / NOT VERIFIED.
- Cross-host and MASTER negative isolation tests: OPEN / NOT RUN.
- HOST-RECOVERED: NOT CLAIMED.

## رسید ادغام و بازخوانی

- PR #85: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/pull/85
- Merge commit: d9156fc4bb28cc1587774ed2ab0758b141bddc8f
- Merge time: 2026-11-21T19:26:11Z UTC / 2026-11-21T22:56:11+03:30 Tehran.

## ثبت و تداوم

این نقطه ادامهٔ همان ریشهٔ یگانهٔ POINT-0 است. ایجاد این سند یا پیام، به‌تنهایی اتصال یا فعال‌شدن میزبان را اثبات نمی‌کند. تنها صف فعال NEXT-051 است.


## اثبات read-back نهایی

- PR #85 merged: d9156fc4bb28cc1587774ed2ab0758b141bddc8f.
- Final main HEAD inspected: a489a5cd56c226299b408ebbb4b603bb54108f77 (UTC 2026-11-21T19:27:18Z).
- All 10 changed/new files were fetched from main and their Git blob SHAs matched the merged branch 10/10.
