# پروتکل جداسازی محیط میزبان و ارتقای گزینشی

- Stable ID: HAIF-HOST-WORKSPACE-ISOLATION-PROMOTION-2026-11-20-001
- Version: 1.0.0
- Parent: POINT-0/069 → POINT-0/070
- Status: REGISTERED / IMPLEMENTATION PARTIAL

## 1. اصل محیط مستقل
هر host_id دقیقاً یک workspace_id پایدار دارد. داده‌های نشست، پیشنهادها، تست‌ها و رسیدهای آن میزبان در مسیر اختصاصی خودش نگهداری می‌شوند. workspaceها با هم ادغام نمی‌شوند؛ تطبیق میان میزبان‌ها فقط در لایه ممیزی/RAHM و با داده‌های پالایش‌شده انجام می‌شود.

## 2. صدور شناسه
شناسه پس از احراز هویت فنی، تعیین مدل/نسخه/adapter، بررسی مجوز و تأیید مالک صادر می‌شود. شناسه نشست برای هر نشست مجزا است. تغییر مدل یا adapter یک revision جدید در منشور میزبان می‌سازد، نه یک میزبان ناشناس جدید؛ مگر آنکه مالک تصمیم دیگری بگیرد.

## 3. مجوز حداقلی
- L0_OFFLINE: بدون اتصال.
- L1_READ_ONLY: فقط خواندن snapshot پین‌شده.
- L2_PROPOSAL_ONLY: فقط ارسال پاکت پیشنهاد به broker.
- L3_TEST_CONTRIBUTOR: فقط تست‌های allowlisted و ارسال رسید.
هیچ میزبان AI دسترسی admin، نوشتن مستقیم main یا merge خودکار ندارد.

## 4. جداسازی و عدم آلودگی
- هر درخواست ورودی باید host_id معتبر، session_id معتبر و مقصد workspace منطبق داشته باشد.
- broker مسیر مقصد را از host_id احراز‌شده استخراج می‌کند؛ میزبان حق تعیین arbitrary path ندارد.
- ورودی‌های نامعتبر، path traversal، symlink، executable، workflow/config mutation، oversized payload، secret و داده شخصی غیرمجاز رد یا قرنطینه می‌شوند.
- خروجی میزبان به‌عنوان داده نامطمئن تلقی می‌شود؛ prompt injection و دستورهای درون payload اجرا نمی‌شوند.
- workspace میزبان هرگز منبع حقیقت master نیست.
- پوشه به‌تنهایی مرز امنیتی نیست؛ دسترسی repo-level باید حذف شود. اگر credential کم‌اختیار و broker امن فراهم نیست، جداسازی باید با repo/sandbox جدا انجام شود.

## 5. نظارت مالک
مالک به‌صورت مرکزی وضعیت هر workspace، نشست‌ها، آخرین دریافت، شکست‌ها، hashها، اختلاف نسخه، مصرف مجوز و تصمیم‌ها را می‌بیند. میزبان‌ها حق دسترسی به داشبورد/رسیدهای میزبان دیگر را ندارند. هر تصمیم مالک append-only و به رویداد مربوطه متصل می‌شود.

## 6. مسیر یادگیری بدون آلودگی MASTER
`HOST → PRIVATE WORKSPACE → REDACTED EVIDENCE → QUARANTINE → OWNER MONITORING → CROSS-HOST RECONCILIATION → RAHM VALIDATION → CHILD CANDIDATE → EXPLICIT OWNER ACCEPTANCE → MASTER + CANONICAL PACKAGE`

فقط نتیجه‌ای وارد نسخه مادر و ZIP می‌شود که:
- منشأ و hash روشن داشته باشد؛
- مستقل و قابل بازتولید باشد؛
- آزمون مثبت/منفی را بگذراند؛
- امنیت، حریم خصوصی، سازگاری و پیوندهای معماری را حفظ کند؛
- از دروازه RAHM عبور کند؛
- تأیید صریح مالک را داشته باشد.

## 7. دفتر دائمی
هر تعامل مجاز به IN/OUT مستقل و event ledger append-only متصل می‌شود. ثبت موفق نیازمند durable write و read-back receipt با digest برابر است. شکست یا عدم اتصال نیز با وضعیت مستقل ثبت می‌شود. هیچ تعامل خام و غیرمجاز به‌صورت خودکار در master ذخیره نمی‌شود.

## 8. گیت‌های اثبات باز
- واقعی‌سازی broker با allowlist مسیر و host identity: OPEN.
- جداسازی credential و محدودیت دسترسی واقعی: OPEN.
- branch protection/rulesets و PR-only enforcement: OPEN.
- اتصال اولین میزبان واقعی، read-back و رسید مستقیم: OPEN.
- آزمون منفی عدم امکان دسترسی میزبان A به workspace میزبان B و MASTER: OPEN.
- آزمون restart/revoke و clean-host recovery: OPEN.

این قرارداد، طراحی و مسیر اجرایی را ثبت می‌کند؛ تا زمانی که آزمون‌ها و رسیدهای عملیاتی موجود نباشند، هیچ میزبان فعال یا محیط امنیتیِ اثبات‌شده اعلام نمی‌شود.


## 9. RAHM central owner-control extension — POINT-0/086

The central RAHM environment is outside every host workspace and is controlled only by the owner. Host data is exported by the owner, redacted, provenance-bound, and validated in private RAHM. The public master receives only sanitized Child candidates through a bot-authored PR and owner review. A Child candidate is not Master. No host receives RAHM or master write access. See docs/architecture/RAHM/README.md and CURRENT-139. This extension is DESIGN REGISTERED / OPERATIONAL SETUP PENDING until the private RAHM repository, promotion App, secrets, connector access and negative isolation tests are verified.
