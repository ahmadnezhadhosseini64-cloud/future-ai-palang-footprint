> **CURRENT GOVERNANCE — POINT-0/GOLDEN / CURRENT-140 / 2026-11-22**
> The canonical root remains the single existing POINT-0. This is the golden baseline of the already-built project, not a new project, root, or parallel queue. Always retrieve exact main HEAD, the current living mother, CURRENT-140, and the sole active NEXT-051 before acting. Historical points and embedded snapshots are evidence only; they never override this baseline or reopen a settled decision by themselves.
>
> **Absolute host boundary:** every host has PUBLIC READ ONLY access to the canonical master. No host, host-held credential, host App, broker, branch, PR, issue, release, workflow, setting, or indirect relay may write to or promote content into the master. Host work remains in its own isolated runtime and, if owner-provisioned, its own private repository. The owner alone exports selected material.
>
> **RAHM placement:** RAHM is a central, private, owner-only quarantine outside every host workspace. Hosts cannot access, inspect, write, administer, or promote anything from RAHM. Raw/private exports are stored only in the owner-controlled private repository future-ai-palang-rahm; the public master contains policy, schemas, validators, workflows, and sanitized Child candidates only.
>
> **Learning and promotion:** OWNER COMMAND → inspect only verified and accessible Host IDs → owner export/redaction → private RAHM quarantine → cross-host reconciliation → schema/hash/privacy/provenance/tests → trusted bot-authored PR to CHILD → owner review and approval. CHILD is not MASTER. Any later Master update requires a separate owner-directed PR and a separate owner approval.
>
> **No false activation:** no host is ACTIVE until its identity, workspace isolation, repository scope, connector permissions, and acceptance receipt are verified. No continuous monitoring is claimed unless a separate owner-controlled service is actually deployed and evidenced.

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
`HOST → ISOLATED PRIVATE WORKSPACE → OWNER-COMMANDED EXPORT → PRIVATE OWNER-ONLY RAHM → CROSS-HOST RECONCILIATION → VALIDATION → BOT-AUTHORED CHILD PR → OWNER APPROVAL → CHILD CANDIDATE`

فقط نتیجه‌ای وارد نسخه مادر و ZIP می‌شود که:
- منشأ و hash روشن داشته باشد؛
- مستقل و قابل بازتولید باشد؛
- آزمون مثبت/منفی را بگذراند؛
- امنیت، حریم خصوصی، سازگاری و پیوندهای معماری را حفظ کند؛
- از دروازه RAHM عبور کند؛
- تأیید صریح مالک را داشته باشد.

## 7. دفتر دائمی
هر تعامل مجاز در محیط میزبان با رسید محلی و منشأ ثبت می‌شود. انتقال به RAHM فقط با فرمان و اقدام مالک، پس از redaction و receipt انجام می‌شود. هیچ میزبان، broker یا adapter حق نوشتن در RAHM یا مخزن مادر را ندارد.

## 8. گیت‌های اثبات باز
- واقعی‌سازی broker با allowlist مسیر و host identity: OPEN.
- جداسازی credential و محدودیت دسترسی واقعی: OPEN.
- branch protection/rulesets و PR-only enforcement: OPEN.
- اتصال اولین میزبان واقعی، read-back و رسید مستقیم: OPEN.
- آزمون منفی عدم امکان دسترسی میزبان A به workspace میزبان B و MASTER: OPEN.
- آزمون restart/revoke و clean-host recovery: OPEN.

این قرارداد، طراحی و مسیر اجرایی را ثبت می‌کند؛ تا زمانی که آزمون‌ها و رسیدهای عملیاتی موجود نباشند، هیچ میزبان فعال یا محیط امنیتیِ اثبات‌شده اعلام نمی‌شود.


## 9. RAHM central owner-control extension — POINT-0/086

The central RAHM environment is outside every host workspace and is controlled only by the owner. Host data is inspected and exported only by the owner on explicit command, then redacted, provenance-bound, and validated in private RAHM. No host or host-controlled intermediary can write to RAHM or the master. A trusted App may create a bot-authored PR to CHILD only after owner-controlled validation. A Child candidate is not Master. See docs/architecture/RAHM/README.md and CURRENT-139. This extension is DESIGN REGISTERED / OPERATIONAL SETUP PENDING until the private RAHM repository, promotion App, secrets, connector access and negative isolation tests are verified.
