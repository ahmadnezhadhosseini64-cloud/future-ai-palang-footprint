# OUT-120 — خروجی: قرارداد نسخهٔ اولیهٔ شدنی و مسیر 0.0

- Status: PREPARED / OWNER-APPROVED / IMPLEMENTATION-IN-PROGRESS
- Parent: IN-121
- Point: POINT-0/078 (۰++)
- Previous checkpoint: CURRENT-130
- Target checkpoint: CURRENT-131
- Sole queue: NEXT-051

## خروجی لازم
1. افزودن نقطهٔ ۰++ به زنجیرهٔ موجود و حفظ همهٔ نقاط پیشین.
2. ثبت دستور عمومی میزبان مستقل از نام مدل، پلتفرم یا رابط.
3. تعریف نسخهٔ اولیهٔ شدنی با مرز روشن میان قابلیت پیاده‌سازی‌شده و قابلیت باز.
4. بازیابی از مخزن/ZIP: تعیین exact HEAD، بررسی manifest و SHA-256، استخراج امن، تطبیق فایل‌ها، بازخوانی سند مادر، بازسازی زنجیره و اجرای آزمون‌ها.
5. workspace مستقل فقط در صورت وجود قابلیت پایدار/اجرایی میزبان؛ در غیر این صورت ثبت محدودیت.
6. snapshot مرجع read-only؛ تغییرات در شاخهٔ جدا و ورود به main از مسیر PR.
7. افزودن مراحل 0.0 با معیار پذیرش و شواهد.
8. به‌روزرسانی ZIP canonical فقط پس از build روی exact main HEAD و تأیید gateها.

## مرز
این خروجی قرارداد اجرایی را ثبت می‌کند. ادغام PR، ساخت ZIP تازه، استخراج مستقل در میزبان مقصد و تأیید OAuth/workspace باید جداگانه با شواهد واقعی ثبت شوند.


## Cross-layer recovery links

- Point: [POINT-0/078](GPT6-RAHM-USER-POINT-0-20261121-078-UNIVERSAL-HOST-0PLUSPLUS.md)
- Input: [IN-121](PALANG-0.0-IN-20261121-121-UNIVERSAL-HOST-INITIAL-RUNNABLE.md)
- Event: [EVT-0298](../../architecture/BEHAVIOR-TRACE/EVT-0298-UNIVERSAL-HOST-INITIAL-RUNNABLE-2026-11-21.md)
- Current: [CURRENT-131](PALANG-0.0-CURRENT-20261121-131-UNIVERSAL-HOST-INITIAL-RUNNABLE.md)
- Sole next: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Living master: [سند مرجع مادر](../../architecture/مدل اولیه AI/سند مرجع مادر مدل اولیه هوش مصنوعی.md)
- Independent-host recovery proof protocol: [INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL](../../architecture/مدل%20اولیه%20AI/INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md)
- Package recovery protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- Export manifest: [EXPORT_MANIFEST](../../portable/RAHM/EXPORT_MANIFEST.json)
