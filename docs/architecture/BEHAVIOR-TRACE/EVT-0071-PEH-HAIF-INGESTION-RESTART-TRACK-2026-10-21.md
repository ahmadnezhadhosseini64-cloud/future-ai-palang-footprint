# EVT-0071 — چکش شواهد و اتصال پیگیری آزمون ورود شش سند / بازیابی پس از restart

- Event ID / شناسهٔ رویداد: EVT-0071
- Stable ID / شناسهٔ پایدار: PALANG-PEH-ANCHOR-HAIF-INGESTION-RESTART-TRACK-2026-10-21-003
- Production ID / شناسهٔ تولید: PPA-HIR-2026-10-21-003
- Version / نسخه: 1.0.0
- UTC: 2026-10-21T14:05:14Z
- Tehran (+03:30): 2026-10-21T17:35:14+03:30
- Parent anchor: PALANG-RETURN-EXECUTION-MASTER-ANCHOR-2026-10-21-001
- Related anchor: PALANG-OUTPUT-ANCHOR-HAIF-INGESTION-2026-10-21-002
- Status: ACTIVE / LIVING / OPEN
- Tracking issue: [#19 — آزمون ورود شش سند واقعی و بازیابی پس از شروع مجدد](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/19)

## محرک
کاربر دستور داد وضعیت چکش شود، لنگر مستقل و زمانی ساخته شود و آزمون ورود شش سند واقعی و بازیابی پس از restart با پیگیری پایدار ادامه یابد.

## اقدام و شواهد
- بازخوانی job run 39612814614, job 119265878400.
- وضعیت job: completed / success.
- لاگ pytest: 11 passed, 1 warning, 0 failed؛ زمان ثبت در لاگ 2026-10-21T13:59:36.4006482Z.
- هشدار: Starlette TestClient با httpx در وضعیت deprecation.
- ایجاد GitHub issue #19 با معیارهای پذیرش: شش سند، provenance/hash، جست‌وجو، بازیابی پس از restart با همان SQLite، و آزمون تزریق شکست.
- زمان UTC/تهران این رویداد از زمان ایجاد issue در پاسخ GitHub گرفته شده؛ این زمان زمان پیام کاربر نیست.

## چکش
- PASS: شاهد CI برای آزمون نمونه بازخوانی شد.
- PASS: پیگیری پایدار در مخزن ایجاد شد.
- PASS: آزمون CI برای ورود اسناد واقعی، `verified_count == 6` و شش مسیر منبع یکتا را assert می‌کند.
- PARTIAL / OPEN: پس از restart فقط یک سند منتخب بازیابی و تطبیق می‌شود؛ بازیابی هر شش سند و تطبیق hash منبع‌به‌ذخیره هنوز باز است.
- OPEN: failure injection، ممیزی ساختاری پس از آخرین تغییر و داوری معنایی گراف.
- NOT VERIFIED: Buffer، Persistent Memory، Library، Dropbox و production deployment.

## شرط بسته‌شدن
این رویداد فقط با شاهد جدید به‌روزرسانی می‌شود. موفقیت CI موجود برای بستن معیارهای شش‌سندی/restart کافی فرض نمی‌شود. هر مرحله باید لاگ، commit، بازخوانی و تطبیق مستقل داشته باشد.
