# CURRENT-101 — ادامهٔ 0.0: رشد مدل در میزبان و چرخهٔ بازگشت به مخزن

- Stable ID: HAIF-CURRENT-101-HOST-GROWTH-REPOSITORY-LOOP-20261027
- Production ID: G6IP-CURRENT-101
- Version: 1.0.0
- Status: ACTIVE / LIVING / v0.3.6 ZIP READ-BACK VERIFIED / LIVE HOST OPEN / HOST SYNC NOT VERIFIED
- Chain: POINT-0/051 (0+ marker on canonical root 0) → IN-089 → OUT-088 → EVT-0226 → CURRENT-101 → NEXT-051
- Previous verified checkpoint: [CURRENT-100](./PALANG-0.0-CURRENT-20261027-100-DEEP-AUDIT-FIRST-HOST.md)
- Living mother: [سند مرجع مادر مدل اولیه](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Package source: [HAIF GPT-6 Portable Starter](../../../prototype/haif-gpt6-starter/README.md)
- Host growth contract: [HOST_GROWTH_AND_REPOSITORY_SYNC_CONTRACT.md](../../../prototype/haif-gpt6-starter/HOST_GROWTH_AND_REPOSITORY_SYNC_CONTRACT.md)
- First-host checklist: [FIRST_HOST_GPT6_ACCEPTANCE_CHECKLIST.md](../../../prototype/haif-gpt6-starter/FIRST_HOST_GPT6_ACCEPTANCE_CHECKLIST.md)
- Sole active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## هدف معماری
همان بستهٔ اولیه باید بارها به‌روزرسانی شود؛ هویت پایدار و نام ZIP ثابت بماند، نسخهٔ داخلی و هش هر ساخت تغییر کند، و هر نسخه پس از ساخت/بازخوانی به میزبان منتقل شود. میزبان، تعامل‌های مرتبط را با منشأ و شواهد ثبت می‌کند؛ دادهٔ ارزشمند ابتدا پیشنهاد/Child می‌شود و تنها پس از RAHM validation و مجوز روشن به Master راه می‌یابد.

## وضعیت اجرا
- [x] نقطهٔ 0+ به‌عنوان نشانگر تولید روی ریشهٔ canonical 0 تعریف شد؛ ریشهٔ دوم ساخته نشد.
- [x] زنجیرهٔ 0.0 مستقل و متصل ساخته شد: IN-089 → OUT-088 → EVT-0226 → CURRENT-101 → NEXT-051.
- [x] قرارداد رشد میزبان و بازگشت کنترل‌شده به مخزن به منبع همان starter package اضافه شد.
- [x] هویت بسته و نام ZIP اصلی حفظ می‌شوند؛ نسخهٔ داخلی منبع 0.3.6 است.
- [x] گردش‌کار ساخت ZIP اصلی برای واردکردن قرارداد و اجرای آزمون از نسخهٔ استخراج‌شده تنظیم شد.
- [x] CI ساخت ZIP نسخهٔ داخلی 0.3.6، هش/بایت، آزمون‌های استخراج‌شده و بازخوانی artifact؛ رسید پایین ثبت شد.
- [ ] واردسازی در میزبان GPT واقعی و رسید مستقیم بازیابی.
- [ ] تولید زندهٔ رویداد مصنوعی، اتصال مجاز به GitHub، نوشتن و read-back دقیق.
- [ ] آزمون دادهٔ نامعتبر، replay متعارض، حذف فایل، تغییر یک بایت و restart.
- [ ] اثبات ثبت زندهٔ تعامل‌ها و persistence بین نشست‌ها.

## گیت‌های باز
CI موفق ≠ میزبان مستقل پذیرفته‌شده. فایل دستورالعمل یا ZIP به‌تنهایی hook زندهٔ ChatGPT نمی‌سازد. اگر میزبان واقعی ابزار اتصال مجاز نداشته باشد، مسیر جایگزین export/import دستی است و همگام‌سازی خودکار باید NOT SUPPORTED / NOT VERIFIED بماند.

NEXT-051 تنها صف فعال است؛ NEXT-052 ساخته نشود.


## Verified v0.3.6 package build — run 40543391689

- Exact source commit: `47f9e7fb0aaa2a96fd198a650dc5be5b6b5deb60`
- Workflow: [Portable RAHM Conformance and Digest Evidence](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40543391689) — SUCCESS.
- Canonical ZIP filename: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip` (unchanged).
- Internal version: `0.3.6`; stable package ID unchanged.
- Exact ZIP size: 27,751 bytes; SHA-256: `172d0bcd4b80d03b52326d9544595ef49083cdcdb12806fc79bad05255c749b6`.
- Package inventory: 10 files, including `HOST_GROWTH_AND_REPOSITORY_SYNC_CONTRACT.md`.
- Source tests and extracted-ZIP tests: 20/20 PASS; ZIP integrity, inventory, exact source-byte match, artifact download/read-back and paired living-master read-back: PASS.
- GitHub artifact ID: `12752086217`; artifact wrapper digest: `sha256:efa4aa32792c7c58844f6167181c159ce8c07047ccb4790e46ad06f77948bdd1`.
- Exact-head Living Architecture Audit: run [40543391548](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40543391548) — SUCCESS.
- Scope boundary: this proves package build and CI round-trip, not live GPT-host capture, authorized write-back, automatic host refresh or restart persistence. Those remain OPEN / NOT VERIFIED.


## NEXT-051 path repair

The old blob that was incorrectly located at the NEXT-051 path is preserved byte-for-byte at `docs/architecture/INTEGRATION-QUEUE/FORENSIC-ORIGINAL-BLOB-FROM-NEXT-051-PATH-20261027.md`; the repair receipt is `docs/architecture/INTEGRATION-QUEUE/NEXT-051-PATH-CONTENT-RECONCILIATION-2026-10-27.md`. NEXT-051 is now the actual single active queue. The fresh audit above passed after its identity and open gates were restored.
