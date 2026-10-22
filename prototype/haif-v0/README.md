# HAIF v0 — نمونهٔ اجرایی اولیه

این پوشه، نخستین نمونهٔ اجرایی کوچک بر اساس سند مرجع مادر مدل اولیهٔ HAIF است. این نمونه فقط هستهٔ «نقطهٔ ادامه + دفتر رویداد» را پیاده می‌کند تا قراردادهای ذخیره‌سازی، بازخوانی، hash و آزمون از حالت سند به کد قابل اجرا منتقل شوند.

## قابلیت‌های پیاده‌شده

- API سلامت سرویس در مسیر /health.
- ایجاد، فهرست و بازیابی لنگرها در مسیرهای /api/v1/anchors.
- ایجاد و بازیابی رویدادها در مسیرهای /api/v1/events.
- ذخیره‌سازی محلی SQLite.
- hash محتوا با JSON canonical و SHA-256.
- بازخوانی رکورد پس از نوشتن و پاسخ WRITE_READBACK_VERIFIED فقط وقتی تطبیق hash موفق است.
- زمان ایجاد رکورد به UTC ثبت می‌شود؛ زمان پیام کاربر اختیاری است و اگر نامعلوم باشد null باقی می‌ماند.
- رویداد می‌تواند به لنگر موجود متصل شود؛ ارجاع به لنگر ناموجود با 404 رد می‌شود.

## اجرا به‌صورت محلی

از این پوشه:

1. وابستگی‌ها را نصب کن: pip install -r requirements.txt
2. سرویس را اجرا کن: uvicorn app:app --reload
3. مستندات تعاملی API در /docs در دسترس است.
4. آزمون‌ها را اجرا کن: pytest -q

پایگاه داده به‌صورت پیش‌فرض در data/haif.sqlite3 ساخته می‌شود. مسیر آن را می‌توان با متغیر محیطی HAIF_DB_PATH تغییر داد.

## مرزهای مهم

- این نمونه، برنامهٔ تولیدی نیست و هنوز احراز هویت، مجوزدهی، محدودسازی نرخ، مهاجرت پایگاه داده، پشتیبان‌گیری یا استقرار امن ندارد.
- ذخیره‌سازی فقط محلی است؛ مخزن GitHub، Buffer، حافظهٔ پایدار، Library و Dropbox به‌عنوان مقصد دادهٔ برنامه متصل نشده‌اند.
- این نمونه، همهٔ گفتگوهای ChatGPT را خودکار ضبط نمی‌کند.
- جست‌وجو در این نسخه تطبیق زیررشته‌ایِ بدون حساسیت به بزرگی/کوچکی حروف است؛ جست‌وجوی معنایی/برداری هنوز پیاده نشده است.
- این نمونه هنوز گراف معنایی کامل، صف داوری، چرخهٔ Master–Child–Rahm یا ارتقای خودکار دانش را پیاده نکرده است.
- خروجی مثبت آزمون‌ها فقط همین کد و آزمون‌ها را پوشش می‌دهد؛ به کل پروژه تعمیم داده نمی‌شود.

## پیوند معماری

مدل حاکم: [سند مرجع مادر مدل اولیهٔ هوش مصنوعی](../../docs/architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
صف بعدی: [گام‌های بعدی و موارد باز](../../docs/architecture/مدل%20اولیه%20AI/صف%20گام‌های%20بعدی%20و%20موارد%20باز.md)


## Controlled repository-document ingestion

The allowlisted importer `ingest_repository_docs.py` brings a small, explicit set of real repository references into the running local API at `POST /api/v1/documents`. It preserves the repository-relative source path, declared version (or `UNDECLARED`), source commit when available, and the API's SHA-256 write/read-back result. Missing source files and failed requests produce a non-success report; the importer does not claim external persistence.

From a checked-out repository, with the API running:

```bash
python prototype/haif-v0/ingest_repository_docs.py --base-url http://127.0.0.1:8000
```

The explicit allowlist is intentionally small and reviewable. This is a controlled ingestion mechanism, not automatic ingestion of the entire repository. Reruns may create additional document records; inspect the report before rerunning.


## Interaction-pair ledger increment — INT / IN / OUT

The prototype now exposes:
- `POST /api/v1/interactions` — validates an interaction-pair record against `docs/architecture/BEHAVIOR-TRACE/interaction-pair-ledger.schema.json`, requires matching date/sequence suffixes for `INT-...`, `IN-...`, and `OUT-...`, stores the canonical record in local SQLite, hashes it with SHA-256, and verifies it by reading it back.
- `GET /api/v1/interactions/{lookup_id}` — reverse lookup from any one of the interaction, input, or output IDs to the same paired record.
- Exact retry of the same record is idempotent; conflicting reuse of an ID returns HTTP 409; unknown IDs return HTTP 404; mismatched pair suffixes are rejected.
- The test suite covers schema validation, write/read-back, lookup by all three IDs, idempotency, conflicting reuse, ID mismatch, and recovery after constructing a fresh app instance against the same SQLite database.

Verified CI: [HAIF Prototype Tests run 39824020260](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39824020260) — SUCCESS, 16 passed, 1 warning, 0 failed.

**Scope boundary:** this is a local development prototype. It does not automatically receive every ChatGPT message, is not a production deployment, and does not establish persistence to Buffer, Library, Persistent Memory, Gmail, or Dropbox. Live producer integration, authentication/authorization, deployment hardening, and external-destination tests remain open. See [Issue #20](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/20) and [CMIND master reference](../../docs/reference/REFERENCE-DOCUMENTS/CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-MASTER-REFERENCE-2026-10-22-001.md).
