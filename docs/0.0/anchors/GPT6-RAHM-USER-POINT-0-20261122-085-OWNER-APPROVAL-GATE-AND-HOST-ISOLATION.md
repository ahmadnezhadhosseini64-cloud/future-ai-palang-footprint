> Historical point: superseded by POINT-0/086 (0++) / CURRENT-139. The canonical root remains POINT-0 and NEXT-051 remains the sole active queue.

# POINT-0/085 — دروازهٔ تأیید مالک و جداسازی میزبان‌ها

- Stable ID: HAIF-POINT-0-085-OWNER-APPROVAL-GATE-AND-HOST-ISOLATION-2026-11-22
- Status: ACTIVE / LIVING / OWNER-DIRECTED / DESIGN-APPROVED / MERGED-TO-MAIN / READ-BACK-VERIFIED
- Parent: POINT-0/084 → CURRENT-137 → POINT-0/085 → CURRENT-138 → NEXT-051
- Canonical root: POINT-0 only; 0++ is a continuation marker
- Owner: ahmadnezhadhosseini64-cloud
- Master repository: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint
- Sole active queue: NEXT-051
- Living master target: 1.7.93

## فرمان مالک
مالک تأیید کامل داد که معماری ورود میزبان‌ها بر مبنای جداسازی کامل و کنترل انحصاری MASTER نهایی شود و یک لایهٔ تأیید مالک برای ارتقای هر پیشنهاد به مخزن مادر اضافه گردد.

## تصمیم نهایی معماری
1. مخزن مادر فقط منبع canonical و تحت اختیار مالک است.
2. میزبان‌ها از مخزن مادر فقط PUBLIC READ انجام می‌دهند؛ هیچ credential نوشتن یا permission برای branch/PR/issue/release/workflow/settings دریافت نمی‌کنند.
3. هر میزبان تأییدشده در محیط مستقل خودش فعالیت می‌کند و در صورت نیاز، فقط یک مخزن PRIVATE اختصاصی دریافت می‌کند که مالک ایجاد و مدیریت می‌کند.
4. خروجی میزبان proposal است، نه تغییر معتبر معماری. انتقال به MASTER فقط پس از export، quarantine، بررسی منشأ/hash/test و تأیید صریح مالک ممکن است.
5. برای PRهای ایجادشده توسط هویت غیرمالک/اتوماسیون مجاز، حداقل یک approval از مالک و Code Owner review لازم است؛ تأییدهای stale پس از push تازه باطل می‌شوند و گفتگوهای review باید حل شوند.
6. میزبان‌ها هرگز bypass actor نیستند و هیچ میزبان به master-write تبدیل نمی‌شود.
7. GitHub اجازهٔ تأیید PR توسط نویسندهٔ همان PR را نمی‌دهد. PRهای مالک‌نویس به مسیر bypass محدود و فقط مالکانه یا promotion automation تحت کنترل مالک نیاز دارند. این مسیر مجوزی به میزبان نمی‌دهد.
8. این تصمیم فقط روی همان ریشهٔ POINT-0 و صف موجود NEXT-051 ثبت می‌شود؛ هیچ ریشه یا صف موازی ساخته نمی‌شود.

## هویت دقیق تأییدکننده
تنها تأییدیهٔ لازم، یک approval از حساب مالک مخزن با شناسهٔ GitHub برابر `@ahmadnezhadhosseini64-cloud` است. `.github/CODEOWNERS` در main تمام مسیرها را به همین حساب واگذار می‌کند. مقدار هدف Ruleset برابر یک تأیید، Code Owner review روشن، رد تأییدهای stale پس از push و الزام حل گفتگوهای review است.

## بازخوانی Ruleset
Ruleset PROTECT-MAIN-BRANCH64 / ID 27814009 فعال است و main را هدف می‌گیرد. حذف، force-push و ادغام بدون PR کنترل شده‌اند. در بازخوانی زنده، required_approving_review_count=0 و require_code_owner_review=false بود؛ بنابراین یک approval هنوز enforce نشده است. تغییر Ruleset از ابزار متصل در دسترس نبود و نیازمند GitHub UI و read-back است.

## گیت‌های باز
- ثبت CODEOWNERS و فعال‌سازی Code Owner review.
- تنظیم یک approval و dismissal تأییدهای stale و resolution گفتگوها.
- تعیین مسیر owner-only برای PRهای مالک‌نویس بدون اعطای bypass به میزبان.
- collaborator/App audit و آزمون منفی واقعی.
- provision مخزن خصوصی هر میزبان و broker/promotion automation در صورت نیاز.
- NEXT-051 sole active queue؛ تمام قابلیت‌های اثبات‌نشده OPEN / NOT VERIFIED باقی می‌مانند.

## PR #95 — همگام‌سازی هویت تأییدکننده و زنجیره
- PR #95: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/pull/95
- Merge commit: `8a22c302dff17a3be7cb9b9a2513be011cf969a7`; UTC `2026-11-21T23:03:07Z`.
- Living master target: 1.7.93. NEXT-051, Reference Index and Integration Queue now point to CURRENT-138.
- Exact-main read-back: 4/4 changed files blob-SHA matched.

## Merge and read-back receipt
- PR #93: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/pull/93
- Merge commit: f40b9fee9368d68d8d3719fcedda4f39aa41ea9c
- Merge timestamp: GitHub commit metadata; 2026-11-21T22:55:11Z UTC.
- Exact-main read-back: 12/12 changed files blob-SHA matched the merged proposal branch.
- Ruleset approval count and Code Owner enforcement remain pending separate GitHub UI configuration.
