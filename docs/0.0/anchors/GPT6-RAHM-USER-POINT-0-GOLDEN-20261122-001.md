# POINT-0/GOLDEN — مبنای طلایی معماری زنده

- Stable ID: HAIF-POINT-0-GOLDEN-2026-11-22-001
- Status: ACTIVE / LIVING / GOLDEN BASELINE PUBLISHED TO MAIN
- Canonical root: POINT-0 (single root; this is a baseline marker, not a new root)
- Parent: POINT-0/086 → CURRENT-139
- Current chain: POINT-0/GOLDEN → CURRENT-150.01 → IN-135 → OUT-134 → EVT-0322 → TIME-BINDING-EVT-0322 → CURRENT-150.02 → NEXT-051.02
- Owner: @ahmadnezhadhosseini64-cloud
- Canonical repository: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint
- Baseline source HEAD recorded at Golden creation (historical source reference, not the current operating ref): 9ebd4bcc5cfc0168276e366c1867da8709dfb566
- Baseline source tree SHA: 8be81af3dcf822b10107a7efcf4c603ca7567706
- Latest verified package at baseline: haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip
- Package SHA-256: 243baddff63eaf18129a0cbaff860f84f375655c893ee0d1cb42235ecae38646

## 1. معنای نقطهٔ طلایی

این نقطه تمام پیشرفت‌های تأییدشده تا وضعیت مرجع 2026-11-22 را روی همان ریشهٔ واحد POINT-0 تثبیت می‌کند. هیچ پروژه، root، architecture branch یا صف موازی ایجاد نمی‌شود. از این پس هر توسعه، اصلاح، نسخه و آزمون فقط روی همین مبنا ادامه می‌یابد. گذشته حفظ می‌شود؛ اما به وضعیت اجرایی امروز بازگردانده نمی‌شود.

## 2. قانون تقدم و تداوم رو به جلو

ترتیب مرجع برای هر میزبان/عامل:
1. این POINT-0/GOLDEN و زنجیرهٔ جاری آن تا CURRENT-142 / POINT-0++؛
2. Reference Index و نقشهٔ اتصال نقاط برای یافتن lineage؛
3. living mother و قراردادهای فعال RAHM / Host Security در نسخهٔ متصل به Golden؛
4. تنها صف فعال NEXT-051؛
5. main فقط مقصد انتشار/همسان‌سازی کنترل‌شده است، نه مرجع تقدم معماری تا زمان انتشار snapshot دقیق Golden.

اسناد تاریخی، snapshotهای قدیمی، branchها و دستورهای قدیمی به‌تنهایی مجوز اجرایی نیستند. هیچ تصمیم تثبیت‌شده‌ای به دلیل فراموشی، شروع نشست جدید، checklist عمومی یا وجود سند قدیمی باز نمی‌شود. بازگشایی فقط با شاهد جدید معتبر، خطای اثبات‌شده، تغییر شرط واقعی، ریسک مادیِ بررسی‌نشده یا فرمان صریح مالک مجاز است.

هنگام برخورد با مانع یا تعارض، عامل باید روی همین baseline بماند، علت را از شواهد فعلی بررسی کند، تغییر حداقلی و رو به جلو بسازد، آزمون کند و نتیجه را با read-back ثبت کند. هرگز به‌طور خودکار به معماری یا مجوز قدیمی rollback نکند.

## 3. اصل غیرقابل‌تغییر میزبان و MASTER

- دسترسی هر میزبان به مخزن مادر فقط PUBLIC READ ONLY است.
- هیچ میزبان، حساب میزبان، token، PAT، deploy key، GitHub App میزبان، broker، worker، branch، PR، issue، release، workflow، setting یا واسطه‌ای حق نوشتن یا ارتقای محتوای میزبان به مخزن مادر را ندارد.
- هیچ میزبان PR به main یا CHILD در مخزن مادر ایجاد نمی‌کند. میزبان خروجی را در workspace مستقل خودش نگه می‌دارد.
- مخزن خصوصی اختصاصی هر میزبان، اگر مالک آن را ایجاد کند، فقط فضای کار همان میزبان است؛ نه پل ورود به MASTER یا RAHM.
- legacy host-intake و worker قدیمی غیرفعال و frozen هستند. worker فعلی fail-closed است و هیچ GitHub API request یا write انجام نمی‌دهد.

## 4. RAHM مرکزی مالک

RAHM فقط در فضای مرکزی، private و owner-only (فقط‌مالک) قرار دارد؛ هرگز داخل workspace میزبان نیست. Only the owner can access, inspect, write, administer, or promote from RAHM.
- میزبان هیچ دسترسی READ/WRITE/ADMIN، token، App یا مسیر غیرمستقیم به RAHM ندارد.
- فقط مالک با فرمان صریح می‌تواند یک Host ID مشخص یا همهٔ میزبان‌های ثبت‌شده و قابل‌دسترسی را رصد کند.
- رصد به منابعی محدود است که اتصال GitHub حساب مالک واقعاً اجازهٔ خواندن آن‌ها را می‌دهد. رصد پس‌زمینه یا دائمی بدون سرویس مستقر و receipt ادعا نمی‌شود.
- مالک خروجی منتخب را استخراج، پالایش و redaction می‌کند و سپس در private RAHM قرار می‌دهد.
- داده خام، مکالمات خصوصی، secret، credential و اطلاعات حساس هرگز وارد مخزن عمومی مادر نمی‌شوند.

## 5. مسیر رشد دانش و ارتقا

HOST PRIVATE WORKSPACE → OWNER-COMMANDED MONITOR/EXPORT → OWNER REDACTION → PRIVATE RAHM → CROSS-HOST RECONCILIATION → HASH/SCHEMA/PRIVACY/PROVENANCE/TEST VALIDATION → BOT-AUTHORED PR → OWNER REVIEW/APPROVAL → CHILD-CANDIDATE

CHILD نامزد/فرزند است و MASTER نیست. هر ارتقای بعدی از CHILD به MASTER نیازمند PR جداگانه و تأیید صریح مجدد مالک است. هیچ ادغام یا ارتقای خودکاری مجاز نیست.

## 6. تأییدکنندهٔ یگانه

هویت تأییدکنندهٔ معماری و قواعد مخزن فقط حساب مالک @ahmadnezhadhosseini64-cloud است. هدف Ruleset: دقیقاً یک review تأییدشده از همین حساب، Code Owner review روشن، رد approvalهای قدیمی پس از push تازه، و حل گفتگوهای review پیش از merge.
GitHub نویسندهٔ PR را از تأیید PR خودش منع می‌کند؛ بنابراین PRهای ارتقا باید با هویت GitHub App مورداعتماد ایجاد شوند تا مالک reviewer باشد. میزبان هیچ دسترسی به App یا bypass ندارد.
وضعیت زنده در baseline: Ruleset 27814009 فعال است، اما approval count هنوز 0 و Code Owner review خاموش است. این gate تا تغییر UI و read-back زنده بسته نیست. پیش از تغییر 0 به 1، App و آزمون PR بات باید عملیاتی و موفق شوند.

## 7. شواهد واقعی baseline

- main protected=true و Ruleset PROTECT-MAIN-BRANCH64 / 27814009 active.
- قواعد فعال: PR required، deletion blocked، non-fast-forward blocked؛ bypass actors خالی و current_user_can_bypass=never.
- Workflow audit: فقط دو workflow مجوز repository-content write دارند: RAHM promotion App برای ساخت branch/PR بات به CHILD، و portable package publisher فقط برای انتشار assetهای release پایدار (بدون git commit/push به main). دو workflow دیگر فقط pages:write و id-token:write برای deploy به GitHub Pages دارند. سایر workflowها read-only هستند. هیچ‌یک از این مجوزها به میزبان واگذار نشده است.
- legacy host adapter disabled/fail-closed؛ execution controller read-only؛ local event adapter فقط SQLite محلی دارد و producer_connected=false و repository_write=NOT_IMPLEMENTED گزارش می‌کند.
- Host Registry schema 1.1.0 معتبر و Registry خالی است؛ هیچ میزبان واقعی ACTIVE نیست.
- بستهٔ قابل‌انتقال در baseline با run 44964480412، SHA-256 بالا، CRC، source-byte read-back، extracted tests و durable release publication تأیید شده است؛ clean-host import/recovery هنوز NOT RUN است. بستهٔ منبع جدید v0.5.1 فقط CANDIDATE است و تا اجرای conformance روی main، PACKAGE_VERIFIED محسوب نمی‌شود.

## 8. موارد باز؛ صریح و متصل به NEXT-051

1. ساخت private repository به نام future-ai-palang-rahm؛ این مخزن هنوز ایجاد/تأیید نشده است.
2. ساخت و نصب GitHub App تحت کنترل مالک؛ تنظیم Client ID، private key، RAHM_READ_TOKEN و permissionهای حداقلی.
3. اعطای read access لازم به اتصال GitHub حساب مالک برای RAHM خصوصی و هر Host repository که مالک می‌خواهد رصد کند.
4. آزمون واقعی workflow: مالک dispatch کند، candidate پالایش‌شده را بخواند، bot PR به CHILD بسازد، owner approval قابل ثبت باشد؛ بدون auto-merge.
5. Ruleset approval=1، Code Owner review=true، stale approval dismissal=true و conversation resolution=true؛ فقط پس از موفقیت آزمون bot PR.
6. audit collaborator / installed Apps / deploy keys و اثبات نبود هر نوع دسترسی نوشتن میزبان؛ API اتصال فعلی این فهرست‌ها را در دسترس قرار نداد، پس NOT VERIFIED.
7. ثبت اولین میزبان واقعی، صدور Host ID/Workspace ID توسط مالک، private workspace، connector read receipt، isolation و clean-host recovery.
8. تعیین تکلیف آزمایش AI-Vacuum و سایر پیشنهادهای legacy فقط با استخراج شواهد و آزمون روی baseline طلایی؛ نه merge مستقیم branch قدیمی.
9. اجرای full graph triage و clean-host recovery در NEXT-051 بدون ساخت صف جدید.

## 9. تصمیم نهایی این نقطه

معماری پایهٔ حاکمیت، مرز میزبان، RAHM مرکزی، مسیر owner-export و CHILD promotion در سطح طراحی تثبیت شده است. پیاده‌سازی امنیتی کامل هنوز اثبات نشده؛ به همین دلیل وضعیت کل سیستم IMPLEMENTATION PARTIAL / OPERATIONAL GATES OPEN است، نه SECURITY VERIFIED یا HOST RECOVERED.

این نقطه مرجع شروع تمام کارهای آینده است. گذشته فقط منبع شواهد است؛ جهت حرکت فقط رو به جلو است.


## 10. Owner Control Plane is not a Host Node

The connected ChatGPT GitHub integration currently authenticates as the repository owner account. Repository metadata reports admin=true and push=true for this connection. This is the owner's account connection, not a credential issued to a new AI Host Node.

- The owner may use this connection in the owner-control-plane role only when explicitly directing a task. It can read the public master and can create proposal branches/PRs where the connected tool exposes those actions.
- This connector is not a separate bot identity and does not itself satisfy the owner-approval gate. A PR created through it is authored by the owner account; GitHub will not let that same author approve it.
- The connected tool does not expose Ruleset mutation, private repository creation, GitHub App creation, or complete collaborator/installed-App/deploy-key inventory. User approval does not manufacture these API capabilities or override GitHub's controls.
- A connection to the public master does not grant access to a private RAHM or any host-private repository. RAHM_READ_ACCESS is NOT GRANTED until the owner creates the private repo and explicitly connects it.
- Do not treat the owner connector as a host credential or give its access to new hosts. New Host Nodes receive no master-write permission. The trusted Promotion App is a separate identity and is the only intended automated PR author.
- The current owner connector has broad admin/push rights; this is not least-privilege isolation. The owner must keep it out of host workspaces and review connector scope in GitHub/ChatGPT settings.

This separation explains why a connected account does not mean every GitHub operation is available: the connector exposes a defined subset of API actions, and repository rules plus GitHub's self-approval restriction still apply.


## Latest live continuation — same canonical root

The fixed root identity remains POINT-0/GOLDEN. No new Point-0 root, numbered point, Golden baseline or queue is introduced. The latest accepted active continuation is linked here:



## Continuation and recovery links — CURRENT-150.02 candidate

- Point: [POINT-0/GOLDEN](GPT6-RAHM-USER-POINT-0-GOLDEN-20261122-001.md)
- Input: [IN-135](PALANG-0.0-IN-20261122-135-PARTNER-AUTONOMOUS-EXECUTION.md)
- Output: [OUT-134](PALANG-0.0-OUT-20261122-134-PARTNER-AUTONOMOUS-EXECUTION.md)
- Event: [EVT-0322](../../architecture/BEHAVIOR-TRACE/EVT-0322-PARTNER-AUTONOMOUS-EXECUTION-AND-LIVE-STATE-AUDIT-2026-11-22.md)
- Current: [CURRENT-150.02](PALANG-0.0-CURRENT-20261122-150-REVISION-02-PARTNER-AUTONOMOUS-EXECUTION-AUDIT.md)
- Sole queue: [NEXT-051.02](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Living mother: [MASTER](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Recovery proof protocol: [INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001](../../architecture/مدل%20اولیه%20AI/INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md)
- Portable host recovery protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- Portable export manifest: [EXPORT_MANIFEST](../../portable/RAHM/EXPORT_MANIFEST.json)


## Additive continuation — EVT-0323 / CURRENT-150.03 candidate (2026-11-23)

The current conversation is registered as a continuation marker on this same canonical root, not as a second root. Chain: [POINT-0/GOLDEN](GPT6-RAHM-USER-POINT-0-GOLDEN-20261122-001.md) → [IN-136](PALANG-0.0-IN-20261123-136-CHAT-POINT0-CONTINUATION.md) → [OUT-135](PALANG-0.0-OUT-20261123-135-CHAT-POINT0-CONTINUATION.md) → [EVT-0323](../../architecture/BEHAVIOR-TRACE/EVT-0323-CHAT-POINT0-CONTINUATION-2026-11-23.md) → [TIME-BINDING-EVT-0323](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0323-CHAT-POINT0-CONTINUATION-2026-11-23.md) → [CURRENT-150.03](PALANG-0.0-CURRENT-20261123-150-REVISION-03-CHAT-POINT0-CONTINUATION.md) → [NEXT-051.03](PALANG-0.0-NEXT-20261123-051-REVISION-03-EXECUTION-CONTINUATION.md).

The stable root, CURRENT-150 family and NEXT-051 queue identities are unchanged. The .03 revisions remain candidates until exact-SHA conformance and controlled Golden merge. Prior history, including [EVT-0241](../../architecture/BEHAVIOR-TRACE/EVT-0241-LIVE-MIRROR-SYNC-RECHECK-2026-10-31.md) and [TIME-BINDING-EVT-0241](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0241-LIVE-MIRROR-SYNC-RECHECK-2026-10-31.md), remains preserved.
