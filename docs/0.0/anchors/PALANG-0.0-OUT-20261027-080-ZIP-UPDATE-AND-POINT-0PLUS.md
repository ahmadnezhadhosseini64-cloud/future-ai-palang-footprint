# OUT-080 — اجرای اصلاح بستهٔ موجود و نقطهٔ 0+

- Stable ID: HAIF-OUT-080-20261027-EXISTING-ZIP-UPDATE
- Production ID: G6IP-OUT-080
- Version: 1.0.0
- Status: IMPLEMENTATION COMMITTED / PACKAGE BUILD PENDING / OPEN / NOT VERIFIED
- Parent: [IN-081](./PALANG-0.0-IN-20261027-081-ZIP-UPDATE-AND-POINT-0PLUS.md)
- Root: [POINT-0/043 (0+)](./GPT6-RAHM-USER-POINT-0-20261027-043-INDEPENDENT-HOST-RECOVERY-HARD-AUDIT.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Current checkpoint: [CURRENT-093](./PALANG-0.0-CURRENT-20261027-093-EXISTING-ZIP-UPDATE.md)
- Living mother: [سند مرجع مادر مدل اولیه](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Export manifest: [EXPORT_MANIFEST.json](../../portable/RAHM/EXPORT_MANIFEST.json)
- Package protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL.md](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)

## اصلاح واقعی
- بستهٔ اولیهٔ 0.3.0 در خانوادهٔ starter حفظ شد؛ شناسهٔ پایدار عوض نشده است.
- محتوای همان خط بسته به 0.3.1 ارتقا داده شد و پروتکل بازیابی مستقل داخل آن قرار گرفت.
- آزمون‌های حضور و کامل‌بودن پروتکل به مجموعهٔ starter اضافه شدند.
- گردش‌کار ساخت اصلاح شد تا ZIP تمیز نسخهٔ جاری را بسازد، cache پایتون را حذف کند، هش دقیق تولید کند و artifact را بارگذاری کند.
- این commit به‌تنهایی ثابت نمی‌کند CI موفق شده است. نتیجهٔ ساخت ZIP و تست‌ها پس از اجرای واقعی workflow باید خوانده شود.


OPEN / NOT VERIFIED: ZIP build receipt and real independent-host acceptance have not been inferred from the source commit. The CI artifact must be fetched and checked separately.
