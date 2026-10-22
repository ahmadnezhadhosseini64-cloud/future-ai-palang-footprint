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


## پیوندهای بازیابی افزوده‌شده
- سند مرجع مادر: [ELVR](../../reference/REFERENCE-DOCUMENTS/EXECUTABLE-INTERACTION-LEDGER-VALIDATION-MASTER-REFERENCE-2026-10-22-001.md).
- لنگر مستقل ۰.۰: [PALANG-0.0-EXECUTABLE-INTERACTION-LEDGER-VALIDATION-2026-10-22-001](../../0.0/anchors/PALANG-0.0-EXECUTABLE-INTERACTION-LEDGER-VALIDATION-2026-10-22-001.md).
- Workflow: [interaction-ledger-validation.yml](../../../.github/workflows/interaction-ledger-validation.yml).
- Fixture: [interaction-pair-ledger-smoke-test.json](./fixtures/interaction-pair-ledger-smoke-test.json).
- نتیجهٔ اجرای workflow هنوز باید از GitHub Actions بازخوانی شود؛ تا آن زمان وضعیت آن NOT VERIFIED است.


## نتیجهٔ آزمون CI — شواهد واقعی
- Workflow run: [39750440075 — موفق](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39750440075).
- Commit آزموده‌شده: [aa8f7beae0c5d3b5043686fc7c1e0a2f6f5b056f](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/commit/aa8f7beae0c5d3b5043686fc7c1e0a2f6f5b056f).
- آغاز workflow: UTC 2026-10-22T08:47:52Z؛ تهران 2026-10-22T12:17:52+03:30.
- پایان/آخرین به‌روزرسانی run: UTC 2026-10-22T08:48:06Z؛ تهران 2026-10-22T12:18:06+03:30.
- نتیجهٔ jobها: schema-validation PASS؛ recover-from-input PASS؛ recover-from-output PASS.
- آزمون واقعیِ انجام‌شده: طرح‌واره و fixture ساختگی بررسی شدند؛ دو job جدا با checkout تازه توانستند از IN و OUT به یک زوج و lineage برسند.
- مرز اثبات: این موفقیت، بازیابی fixture ساختگی از checkout تازه را ثابت می‌کند؛ نه cold-start یک سرویس تولیدی، نه جمع‌آوری خودکار همهٔ مکالمات، و نه ذخیره در Gmail/Library/Buffer/Memory/Dropbox.


## Reconciliation — نتیجهٔ قبلی و وضعیت جاری
این رویداد در ابتدا نتیجهٔ CI را در وضعیت انتظار گذاشته بود، زیرا هنوز اجرا و بازخوانی نشده بود. آن وضعیت تاریخی با ثبت و بازخوانی [EVT-0087 — نتیجهٔ راستی‌آزمایی](./EVT-0087-INTERACTION-VALIDATION-RECOVERY-RESULT-2026-10-22.md) به‌روزرسانی شد. وضعیت جاری: CI موفق برای schema و fixture ساختگی؛ بازیابی IN و OUT در checkoutهای تازه موفق؛ بازیابی cold-start سرویس تولیدی و جمع‌آوری خودکار گفتگوها همچنان باز/تأییدنشده.
