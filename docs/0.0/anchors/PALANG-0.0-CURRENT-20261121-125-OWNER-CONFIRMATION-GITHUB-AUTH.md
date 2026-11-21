# CURRENT-125 — Easy read-only GitHub connection for a new host

- Point: [POINT-0/072](GPT6-RAHM-USER-POINT-0-20261121-072-OWNER-CONFIRMATION-GITHUB-AUTH-0PLUS.md).
- Input: [IN-115](PALANG-0.0-IN-20261121-115-OWNER-CONFIRMATION-GITHUB-AUTH.md).
- Output: [OUT-114](PALANG-0.0-OUT-20261121-114-OWNER-CONFIRMATION-GITHUB-AUTH.md).
- Event: [EVT-0291](../../architecture/BEHAVIOR-TRACE/EVT-0291-OWNER-CONFIRMATION-GITHUB-AUTH-2026-11-21.md).
- Time binding: [TIME-BINDING-EVT-0291](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0291-OWNER-CONFIRMATION-GITHUB-AUTH-2026-11-21.md).
- Previous checkpoint: CURRENT-124.
- Sole active queue: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md).
- Status: PROPOSAL REGISTERED ON HOST-INTAKE BRANCH / NOT MERGED.
- Living master target: v1.7.79.
- Package source target: 0.4.4.
- Immediate scope: anonymous public READ-ONLY access to the canonical repository, main HEAD discovery and latest-state recovery; official connector is optional while repository remains PUBLIC.
- Main branch integration: NOT DONE.
- Canonical ZIP rebuild and exact hash/receipt: PENDING.
- Independent-host connector and read-only access test: NOT RUN.
- Owner phrase/password gate («احمد نژادحسینی») and expanded authentication design: OPEN / DEFERRED TO LATER PHASE.
- Repository writes, broker deployment, host-intake write enforcement and branch protection: OPEN / OUT OF CURRENT SCOPE.
- Preserve all prior anchors, CURRENT-065/CURRENT-066 ambiguity, open gates and NEXT-051. No NEXT-052 created.

## Preserved open gates and lineage

- CURRENT-065/CURRENT-066 pointer and overlay conflict: OPEN; no winner selected.
- Full state recovery and reconstruct independently from IN and OUT: OPEN / NOT RUN.
- Clean host import and clean interactive AI-host session: OPEN / NOT RUN.
- Second-host import and second-host acceptance: OPEN / NOT RUN.
- Restart persistence and restart/new-session recovery: OPEN / NOT RUN.
- Automatic live message capture and idle/background capture: OPEN / NOT RUN.
- Graph/identity/parent/time triage, duplicate IDs and ambiguous parents: OPEN / NOT VERIFIED.
- Issue #20 and Issue #21 remain OPEN.
- External-host GitHub connector authorization and read-only recovery: NOT RUN.
- Owner phrase/password gate («احمد نژادحسینی») remains OPEN / DEFERRED; repository writes remain out of scope for POINT-0/072.

## Historical mirror references and preservation

- Mirror event: [EVT-0241](../../architecture/BEHAVIOR-TRACE/EVT-0241-LIVE-MIRROR-SYNC-RECHECK-2026-10-31.md).
- Mirror time binding: [TIME-BINDING-EVT-0241](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0241-LIVE-MIRROR-SYNC-2026-10-31.md).
- These are preserved historical mirror records, not a replacement for EVT-0291 or its time binding.

## Cross-index registration status

The POINT-0/072 chain is linked from docs/0.0/README.md, docs/REFERENCE_INDEX.md, the behavior-trace index, the integration-queue index, the living mother and the RAHM export manifest. This remains proposal-branch registration only; no main merge, package rebuild or external-host acceptance is implied.


## CURRENT-125 clarification — FIRST_HOST / HOST-001
The first new host is a constrained execution participant, not a repository maintainer. It reads the public canonical repository and runs only owner-defined tasks inside the explicitly provisioned workspace. Repository write access is prohibited. External tools and destinations are limited to owner-approved, actually provisioned permissions. Runtime identity and technical enforcement remain unverified until an independent-host acceptance test.


## تصریح مالک: نقش اولین میزبان و مرز اختیار (2026-11-21)

- این میزبان به‌عنوان FIRST_HOST / HOST-001 تعریف می‌شود؛ این شناسه نقش معماری است، نه ادعای شناسایی runtime. Host ID واقعی تا مشاهده از محیط میزبان UNKNOWN است.
- میزبان فقط به دو سطحی دسترسی دارد که مالک تعریف و در محیط مقصد واقعاً فراهم کرده است: (الف) خواندن مخزن canonical و اسناد/بسته‌های آن؛ (ب) محیط کاری محدود و مشخصی که برای همین میزبان ساخته و مجاز شده است.
- دسترسی مخزن در این فاز READ-ONLY است: مشاهده، دریافت، جست‌وجو، بازیابی، تطبیق نسخه و اجرای محتوای مجاز در workspace. هیچ حق ایجاد/ویرایش/حذف فایل در مخزن، commit، push، branch، PR، merge، release، تغییر تنظیمات یا مدیریت دسترسی ندارد.
- «اجرایی» به معنی اجرای وظایف مشخصی است که مالک در همان محیط کاری تعیین و به‌روزرسانی می‌کند؛ به معنی اختیار آزاد، دسترسی عمومی به سیستم، اختیار نوشتن در مخزن یا اختیار اجرای هر دستور دلخواه نیست.
- هر ارتباط بیرونی، ابزار، connector، حساب، API یا مقصد فقط در صورت تعریف صریح مالک و فراهم بودن مجوز محدود همان ابزار قابل استفاده است. میزبان نباید دامنه دسترسی را خودش گسترش دهد، credential بخواهد، یا از مجوز یک ابزار برای مقصد دیگری استفاده کند.
- پیش‌فرض workspace نیز کمینه‌مجوز است. اگر برای یک وظیفه نیاز به ساخت/ویرایش خروجی محلی باشد، فقط در مسیر workspace مشخص و در حد همان وظیفه؛ این اجازه به مخزن منتقل نمی‌شود. اگر قابلیت sandbox یا محدودسازی واقعی وجود ندارد، اجرا BLOCKED / NOT SUPPORTED گزارش شود.
- هیچ عملیات نوشتن یا همگام‌سازی از workspace به مخزن مجاز نیست. هر تغییر مرجع را مالک از مسیر کنترل‌شده و جداگانه انجام می‌دهد؛ میزبان سپس نسخه تازه را فقط می‌خواند.
- استقلال میزبان تضمین امنیت نیست؛ مرز واقعی باید با مجوزهای فنی read-only، محدودسازی workspace و connectorهای allowlist شده اعمال و آزمون شود. متن دستور به‌تنهایی sandbox یا ACL ایجاد نمی‌کند.
- پذیرش نهایی نیازمند آزمون واقعی است: تلاش خواندن موفق؛ تلاش نوشتن در مخزن ناموفق؛ دسترسی فقط به workspace تعریف‌شده؛ رد مقصد/ابزار خارج از allowlist؛ و ثبت رسید. تا آن زمان FIRST_HOST POLICY DESIGNED / TECHNICAL ENFORCEMENT NOT VERIFIED / HOST ACCEPTANCE NOT RUN.


## Superseded by CURRENT-126 — POINT-0++ continuation
The host-workspace execution architecture is continued at [CURRENT-126](PALANG-0.0-CURRENT-20261121-126-FIRST-HOST-RESTRICTED-EXECUTION.md) through IN-116 → OUT-115 → EVT-0292 → TIME-BINDING-EVT-0292. CURRENT-125 remains preserved as the preceding checkpoint; it is not deleted or silently rewritten. The controlling contract is [FHRWE-2026-11-21-001](../../reference/REFERENCE-DOCUMENTS/FIRST-HOST-RESTRICTED-WORKSPACE-EXECUTION-AND-READ-ONLY-REPOSITORY-CONTRACT-2026-11-21-001.md).
