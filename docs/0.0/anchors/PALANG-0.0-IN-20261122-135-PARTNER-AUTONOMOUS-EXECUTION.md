# IN-135 — دستور اجرای مستقل یار پلنگ در زمان مشغلهٔ مالک

- Stable ID: HAIF-IN-135-PARTNER-AUTONOMOUS-EXECUTION-2026-11-22
- Canonical root: POINT-0
- Baseline: POINT-0/GOLDEN
- Parent resolver: CURRENT-150.01
- Sole queue: NEXT-051.01
- Owner: @ahmadnezhadhosseini64-cloud

## فرمان مالک

مالک اعلام کرد که فعلاً درگیر است و تا اطلاع بعدی نباید برای کارهای معمول یا تصمیم‌های قابل‌استنتاج از معماری متوقف شود. یار پلنگ باید تمام بررسی‌ها، اقدامات، آزمون‌ها و اصلاحات قابل‌انجام با ابزارها و مجوزهای واقعی خود را مستقل پیش ببرد؛ هر ده اقدام Partner و سایر کارهای قابل‌انجام در NEXT-051 را بررسی کند؛ و مواردی را که به ورود امن مالک، ایجاد منابع بیرونی یا قابلیت فنیِ در دسترس‌نبودن نیاز دارند، دقیق و زنده در صف نگه دارد.

## قیود الزام‌آور

1. هیچ درخواست اقدام از مالک مطرح نشود، مگر آنکه یک مانع واقعیِ غیرقابل‌عبور به ورودی یا تأیید او نیاز داشته باشد.
2. هیچ Secret، رمز، کد MFA، کلید خصوصی یا توکن در گفتگو یا مخزن عمومی درخواست یا ثبت نشود.
3. هیچ میزبان آینده‌ای حق نوشتن مستقیم یا غیرمستقیم به MASTER ندارد؛ RAHM فقط‌مالک و بیرون از workspace میزبان می‌ماند.
4. تغییرات این مرحله فقط روی شاخهٔ کاری و از مسیر PR به POINT-0/GOLDEN انجام می‌شود؛ main دست‌نخورده می‌ماند.
5. ثبت سند، ایجاد شاخه یا موفقیت CI معادل provision سرویس، امنیت زنده یا بازیابی میزبان واقعی نیست.
6. هر اقدام باید با SHA، نتیجهٔ واقعی، read-back و وضعیت OPEN/DONE/BLOCKED ثبت شود؛ زمان پیام مالک UNKNOWN می‌ماند مگر منبع معتبر مستقلی وجود داشته باشد.

## دامنهٔ اجرا

ممیزی زندهٔ مخزن، شاخه‌ها، PRها، Ruleset، فایل‌های امنیتی، workflowها، ده Issue مستقل، بستهٔ قابل‌حمل، release، آزمون‌ها و موانع ابزار؛ سپس ثبت نتیجه در همان زنجیرهٔ ثابت CURRENT-150 / NEXT-051.


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
