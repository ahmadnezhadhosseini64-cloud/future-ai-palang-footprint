# OUT-122 — خروجی معماری: تفکیک READ عمومی از OAuth و WRITE

- Parent point: POINT-0/080
- Status: ARCHITECTURE-DECISION-RECORDED
- Source: IN-123
- Canonical architecture: [Public repository and low-friction host access](../../architecture/مدل%20اولیه%20AI/معماری%20دسترسی%20عمومی%20مخزن%20و%20ورود%20کم‌اصطکاک%20میزبان.md)

## نتیجه
1. مخزن Public است؛ بنابراین میزبان می‌تواند بدون OAuth با HTTPS عمومی آن را بخواند و clone/fetch کند.
2. OAuth برای READ عمومی لازم نیست.
3. OAuth یا credential امن فقط برای WRITE احراز‌شده یا دسترسی به دادهٔ خصوصی لازم است.
4. EXECUTE، workspace خصوصی/پایدار و restart به امکانات واقعی محیط مقصد وابسته‌اند.
5. تأیید مالک برای آغاز مراحل مجاز معتبر است؛ اما credential و امکانات میزبان را ایجاد نمی‌کند.
6. میزبان نقش عامل اجرایی موقت دارد؛ MASTER و حاکمیت پروژه در اختیار مالک باقی می‌ماند.
7. تغییرات پیشنهادی ابتدا در workspace/branch جدا و سپس از مسیر PR و تصمیم مالک بررسی می‌شوند.

## تفکیک نتیجه‌ها
- PUBLIC_SOURCE_RECOVERED: فایل‌های عمومی و exact HEAD خوانده شده‌اند.
- LOCAL_EXECUTION_VERIFIED: آزمون‌ها در محیط واقعی اجرا شده‌اند.
- WORKSPACE_READY: جداسازی و پایداری اثبات شده‌اند.
- HOST_RECOVERED: بازیابی مستقل و restart با رسید مستقیم میزبان ثابت شده است.
این وضعیت‌ها مترادف نیستند و نباید با یکدیگر ادغام شوند.

## موارد باز
آزمون clean-host، اجرای مقصد، workspace پایدار، restart و write-back احراز‌شده همچنان OPEN / NOT RUN هستند.


## Canonical recovery link matrix — POINT-0/080

- Point: [POINT-0/080](GPT6-RAHM-USER-POINT-0-20261121-080-PUBLIC-READ-NO-OAUTH-HOST-ACCESS.md)
- Input: [IN-123](PALANG-0.0-IN-20261121-123-PUBLIC-READ-NO-OAUTH-HOST-ACCESS.md)
- Event: [EVT-0300](../../architecture/BEHAVIOR-TRACE/EVT-0300-PUBLIC-READ-NO-OAUTH-HOST-ACCESS-2026-11-21.md)
- Current: [CURRENT-133](PALANG-0.0-CURRENT-20261121-133-PUBLIC-READ-NO-OAUTH-HOST-ACCESS.md)
- Sole next: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Living master: [سند مرجع مادر](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Independent-host recovery proof protocol: [INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL](../../architecture/مدل%20اولیه%20AI/INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md)
- Package recovery protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL.md](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- Export manifest: [EXPORT_MANIFEST.json](../../portable/RAHM/EXPORT_MANIFEST.json)
- Canonical package manifest: [manifest.json](../../../prototype/haif-gpt6-starter/manifest.json)
