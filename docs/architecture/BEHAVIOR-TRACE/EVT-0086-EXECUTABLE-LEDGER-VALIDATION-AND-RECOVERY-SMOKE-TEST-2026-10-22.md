# EVT-0086 — اعتبارسنجی اجرایی دفتر تعامل و آزمون بازیابی آزمایشی

- Stable ID: PALANG-EXECUTABLE-LEDGER-VALIDATION-RECOVERY-SMOKE-2026-10-22-001
- Production ID: ELVR-HAIF-2026-10-22-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / GOVERNING
- Parent: EVT-0085 — دفتر زوج‌های تعامل، JSON Schema و برنامهٔ بازیابی
- Master reference: docs/reference/REFERENCE-DOCUMENTS/EXECUTABLE-INTERACTION-LEDGER-VALIDATION-MASTER-REFERENCE-2026-10-22-001.md

## ثبت این گام
این رویداد، آزمون‌های تکرارپذیر را به مخزن اضافه می‌کند: اعتبارسنجی JSON Schema با Draft 2020-12، اعتبارسنجی یک رکورد ساختگی، و آزمون جست‌وجوی معکوس از شناسهٔ IN و OUT به یک زوج و زنجیرهٔ منشأ مشترک.

## اجزای اجرایی
- Workflow: .github/workflows/interaction-ledger-validation.yml
- Schema: docs/architecture/BEHAVIOR-TRACE/interaction-pair-ledger.schema.json
- Synthetic fixture: docs/architecture/BEHAVIOR-TRACE/fixtures/interaction-pair-ledger-smoke-test.json

## معیارهای آزمون
- بررسی معتبر بودن خود طرح‌واره.
- اعتبارسنجی fixture با Draft202012Validator و بررسی قالب تاریخ.
- اثبات اینکه IN و OUT در fixture به یک interaction_id و lineage می‌رسند.
- نگه‌داشتن زمان‌های ثبت‌نشده به‌صورت null و اعلام NOT_EXPOSED؛ زمان ساختگی ممنوع است.

## مرز اثبات
تا وقتی اجرای واقعی GitHub Actions با نتیجهٔ موفق بازخوانی نشده، وضعیت آزمون CI برابر PENDING / NOT VERIFIED است. حتی در صورت موفقیت CI، این آزمون فقط طرح‌واره و جست‌وجوی معکوسِ fixture را ثابت می‌کند؛ آزمون cold-start مستقل و جمع‌آوری خودکار همهٔ مکالمات هنوز اثبات نشده است.

## پابند زمان
زمان مرجع ثبت این رویداد باید از timestamp واقعی commit نهایی این فایل در UTC استخراج شود و معادل تهران از همان لحظه محاسبه شود. زمان پیام کاربر و زمان اجرای workflow فیلدهای جدا هستند؛ اگر ثبت نشده‌اند UNKNOWN / NOT EXPOSED می‌مانند.

## اصل معماری
معماری اولیه immutable / محفوظ است؛ این رویداد فقط قابلیت آزمون‌پذیری افزایشی اضافه می‌کند. همهٔ نتایج بعدی باید به‌صورت الحاقیه یا رویداد تازه با شواهد ثبت شوند.
