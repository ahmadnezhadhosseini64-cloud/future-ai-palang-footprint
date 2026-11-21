# POINT-0/084 — مخزن مادر فقط‌مالک و مخزن خصوصی مستقل هر میزبان

- Stable ID: HAIF-POINT-0-084-OWNER-ONLY-MASTER-PER-HOST-PRIVATE-REPOS-2026-11-21
- Status: ACTIVE / LIVING / OWNER-DIRECTED / DESIGN-REGISTERED / IMPLEMENTATION-PARTIAL
- Parent: POINT-0/083 → CURRENT-136 → NEXT-051
- Canonical root: POINT-0 only; 0++ is a marker, not a new root
- Owner: ahmadnezhadhosseini64-cloud
- Master repository: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint
- Sole active queue: NEXT-051
- Living master target: 1.7.91

## فرمان مالک

مالک تأکید کرد مخزن مادر فقط متعلق به اوست و هیچ میزبان هوش مصنوعی نباید در آن نوشتن، تغییر، حذف، branch، PR، issue، release، workflow یا تنظیمات انجام دهد. هر میزبان باید هویت مستقل داشته و فقط در محیط خصوصی و مستقل خودش فعالیت کند. مالک باید بتواند هر فضای میزبان را مشاهده، استخراج، بازیابی، تعلیق یا لغو کند.

## تصمیم معماری

1. مخزن مادر Public می‌ماند تا میزبان دعوت‌شده بتواند با یک پیام و بدون OAuth، اسناد عمومی را بخواند؛ اما Public بودن به معنی قابل‌مشاهده بودن محتوا برای همهٔ اینترنت است.
2. هیچ میزبان AI به مخزن مادر به‌عنوان collaborator یا دارندهٔ PAT، deploy key یا GitHub App write scope اضافه نمی‌شود.
3. هر میزبان تأییدشده یک مخزن PRIVATE جداگانه می‌گیرد که فقط مالک آن را ایجاد و مدیریت می‌کند؛ هیچ میزبان حق ساخت یا انتخاب مقصد repo را ندارد.
4. هر مخزن خصوصی فقط به Host ID واحد نگاشت می‌شود؛ credential و دسترسی بین میزبان‌ها مشترک نیست.
5. سطح پیش‌فرض L1_READ_ONLY است. میزبان بدون credential نوشتن در مخزن مادر، snapshot را می‌خواند و در محیط خصوصی مقصد خودش کار می‌کند.
6. در صورت نیاز به ذخیره‌سازی Git، فقط مسیر اختیاری L3 از broker و GitHub App با دسترسی محدود به همان مخزن خصوصی مجاز است. credential در broker/secret manager باقی می‌ماند و به مدل یا چت تحویل نمی‌شود.
7. مخزن شخصی خصوصی به‌طور معمول read-only collaborator role ندارد؛ بنابراین به میزبان به‌عنوان collaborator دسترسی نمی‌دهیم. دسترسی نوشتن محدود باید با GitHub App انتخابی/ broker یا ساختار سازمانی مناسب اجرا شود.
8. ناشناس‌هایی که مخزن عمومی را می‌خوانند یا clone می‌کنند قابل شناسایی فردی و ثبت خودکار نیستند. فقط درخواست ثبت‌نام کنترل‌شده و رسید قابل‌تأیید می‌تواند وارد چرخهٔ Host Registry شود.
9. هیچ پیشنهاد یا داده‌ای از workspace میزبان خودکار وارد MASTER نمی‌شود؛ مالک و RAHM کنترل مسیر ارتقا را حفظ می‌کنند.

## یافتهٔ امنیتی مخزن در زمان این ثبت

- GitHub metadata: repository visibility = PUBLIC.
- مخزن در حساب شخصی مالک قرار دارد.
- اتصال GitHub مورد استفاده برای این عملیات، دسترسی admin/push مالک را گزارش می‌کند؛ این مجوز مالک است، نه میزبان.
- قرارداد موجود مخزن پیش‌تر `main.protected=false` را ثبت کرده بود. ابزار متصل در این نشست امکان خواندن/تنظیم branch protection/rulesets یا فهرست کامل collaborator/App access را ندارد؛ وضعیت فعلی این تنظیمات باید در GitHub UI بررسی شود.
- بنابراین این نقطه، سیاست و طراحی را ثبت می‌کند اما نمی‌گوید حفاظت شاخه، broker، App scope یا مخزن خصوصی میزبان‌ها همین حالا فعال شده‌اند.

## زنجیره

POINT-0/083 → CURRENT-136 → POINT-0/084 (0++) → IN-127 → OUT-126 → EVT-0304 → TIME-BINDING-EVT-0304 → CURRENT-137 → NEXT-051

## گیت‌های اجرا

- Owner-only master policy: DESIGN REGISTERED.
- Master Public READ: VERIFIED by repository metadata.
- No host write credential to master: POLICY; live collaborator/App audit OPEN.
- Main branch protection/ruleset: OPEN / NOT VERIFIED.
- Host-specific private repository template: DESIGN REGISTERED.
- Any actual private host repo: NONE CREATED / NONE VERIFIED in this step.
- GitHub App scoped installation: NOT CONFIGURED.
- Broker and server-side host-to-repo mapping: NOT DEPLOYED.
- Host Registry live records: NONE VERIFIED.
- Anonymous public readers identification: NOT POSSIBLE from ordinary public read/clone; no auto-registration.
- Cross-host negative tests and revoke/recovery tests: NOT RUN.
- First destination host acceptance: OPEN / NOT RUN.

## ثبت و تداوم

این نقطه ادامهٔ همان ریشهٔ canonical POINT-0 است؛ صف موازی ایجاد نمی‌کند. NEXT-051 تنها صف فعال می‌ماند. میزبان تازه تا رسید مستقیم و تأیید مالک، PROPOSED است. هیچ قابلیت امنیتی که در GitHub و محیط واقعی اعمال و آزموده نشده، VERIFIED اعلام نمی‌شود.
