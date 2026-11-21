
## زنجیره و پیوندهای مستقیم

- [IN-129](PALANG-0.0-IN-20261122-129-RAHM-CENTRAL-OWNER-GATE.md) → [OUT-128](PALANG-0.0-OUT-20261122-128-RAHM-CENTRAL-OWNER-GATE.md)
- [EVT-0306](../../architecture/BEHAVIOR-TRACE/EVT-0306-RAHM-CENTRAL-OWNER-GATE-AND-CHILD-PROMOTION-2026-11-22.md) → [TIME-BINDING-EVT-0306](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0306-RAHM-CENTRAL-OWNER-GATE-2026-11-22.md)
- [CURRENT-139](PALANG-0.0-CURRENT-20261122-139-RAHM-CENTRAL-OWNER-GATE.md) → sole active [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- [RAHM policy](../../architecture/RAHM/README.md) · [Owner monitoring commands](../../architecture/RAHM/OWNER-MONITORING-COMMANDS.md) · [Private RAHM setup](../../architecture/RAHM/PRIVATE-RAHM-REPOSITORY-TEMPLATE.md) · [Promotion App setup](../../architecture/RAHM/PROMOTION-APP-SETUP.md) · [CHILD](../../architecture/CHILD-CANDIDATES/README.md)
- [Host security contract](../../architecture/HOST-SECURITY/OWNER-ONLY-MASTER-PER-HOST-PRIVATE-REPOSITORIES.md) · [Living mother](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
# POINT-0/086 (0++) — رحم مرکزی مالک و مسیر ارتقای میزبان‌ها

- Stable ID: HAIF-POINT-0-086-RAHM-CENTRAL-OWNER-GATE-2026-11-22
- Status: ACTIVE / LIVING / OWNER-DIRECTED / IMPLEMENTATION PARTIAL
- Parent: POINT-0/085 → CURRENT-138
- Canonical root: POINT-0 only; 0++ is a continuation marker, not a new root.
- Owner: ahmadnezhadhosseini64-cloud
- Master: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint
- Current master target: 1.7.94
- Sole active queue: NEXT-051

## فرمان و تأیید مالک

مالک تأیید کرد مسیر دائمی ورود میزبان‌های جدید، جداسازی محیط کاری هر میزبان، رصد و استخراج انتخابی با فرمان مالک، انتقال کنترل‌شده به RAHM، آزمون و تطبیق، و سپس ورود فقط با تأیید مالک به CHILD ساخته شود. هیچ میزبان حق نوشتن یا ارتقای مستقیم به مخزن مادر ندارد.

## تصمیم معماری

1. هر میزبان در محیط خصوصی مستقل خودش کار می‌کند. پس از فرمان مالک و بررسی رسید واقعی و Registry، دستیار/کنترل‌پلین Host ID یکتای بعدی را صادر می‌کند و Workspace ID جداگانه به آن متصل می‌شود؛ میزبان حق خودشناسه‌گذاری ندارد.
2. مخزن مادر برای میزبان‌ها PUBLIC READ ONLY است؛ هیچ میزبان collaborator، PAT، deploy key، App token، branch/PR/issue/workflow/settings permission یا bypass دریافت نمی‌کند.
3. RAHM فضای مرکزی تحت کنترل مالک است، نه بخشی از محیط میزبان. میزبان‌ها به RAHM دسترسی ندارند.
4. چون مخزن مادر Public است، RAHM واقعی برای داده‌های خام/خصوصی در مخزن جداگانه PRIVATE به نام future-ai-palang-rahm قرار می‌گیرد. در مخزن مادر فقط سیاست، schema، workflow و محتوای پالایش‌شده و قابل انتشار نگهداری می‌شود.
5. ChatGPT فقط با فرمان مالک و فقط برای Host IDهای ثبت‌شده و منابعی که اتصال مجاز واقعاً به آن‌ها دسترسی دارد رصد می‌کند. رصد خودکار/همیشگی بدون سرویس و رسید واقعی ادعا نمی‌شود.
6. خروجی میزبان داده نامطمئن است. منشأ، Host ID، Workspace ID، Session ID، commit مرجع، زمان، hash، حریم خصوصی، اختلاف‌ها و نتیجه آزمون باید حفظ شوند.
7. فقط خروجی پالایش‌شده و دارای تأییدیه مالک برای بررسی CHILD، با workflow و GitHub App مورداعتماد، در شاخه اختصاصی قرار می‌گیرد و PR را هویت Bot ایجاد می‌کند.
8. PR به CHILD خودکار ادغام نمی‌شود. مالک با حساب @ahmadnezhadhosseini64-cloud بررسی و تأیید می‌کند. ادغام در CHILD به معنی پذیرش در Master نیست.
9. ChatGPT می‌تواند بررسی فنی، امنیتی، منشأ و آزمون را انجام دهد و گزارش review بدهد؛ اما رأی نهایی GitHub باید از حساب مالک باشد. هیچ هویت AI یا Bot به‌جای مالک تأیید نهایی نمی‌دهد.
10. ارتقای CHILD به اسناد مادر، مرحله‌ای جداگانه با PR مستقل، آزمون، و تأیید صریح مجدد مالک است.

## شواهد پیاده‌سازی این نقطه

- RAHM architecture, private-repository template, candidate manifest schema, public control-plane index and CHILD landing area created.
- Candidate validator and unit tests added; it rejects invalid IDs, unredacted data, missing owner authorization, path traversal, symlinks, unsupported/unmanifested files, oversized payloads, SHA-256 mismatch and common secret patterns.
- Owner-only workflow added: workflow_dispatch by the owner on main; it reads a private RAHM repo, checks privacy, validates the candidate, and creates a bot-authored PR into CHILD. It does not auto-merge or modify the living Master.
- Direct-to-main automation paths found in the hard audit were changed to artifact-only/read-only behavior: Evidence Gate, execution controller, pending-registration drain, and portable conformance permissions. The legacy host adapter is fully disabled and fail-closed; it makes no GitHub API request or write.
- The current Ruleset remains approval count 0 and Code Owner review OFF. This is not claimed as active enforcement.

## Open operational gates

- Create and verify the private repository future-ai-palang-rahm.
- Create and install the owner-controlled promotion GitHub App on the master repository only; give it Contents write and Pull requests write, with no bypass, Administration, Actions, Secrets or Workflows permissions.
- Add repository variable PALANG_PROMOTION_APP_CLIENT_ID and secret PALANG_PROMOTION_APP_PRIVATE_KEY.
- Create a fine-grained read-only RAHM token for the private RAHM repository and add it as secret RAHM_READ_TOKEN.
- Grant the ChatGPT GitHub connection read access to the private RAHM repository for on-demand monitoring.
- Configure Ruleset 27814009 to one required approval, Code Owner review, stale-review dismissal and conversation resolution; re-read the live API.
- Audit collaborators, teams, installed Apps and deploy keys; run negative isolation tests.
- Enroll and verify the first real host; registry remains empty until a real receipt exists.
- Run the new RAHM validator tests and first bot-authored PR end-to-end.

No host is ACTIVE, no RAHM private repository is provisioned, no promotion App is installed, and no independent-host recovery is claimed in this point.
