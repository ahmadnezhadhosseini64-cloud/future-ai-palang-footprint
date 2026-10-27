# OUT-084 — نتیجهٔ بررسی بستهٔ اولیه و نقص باقی‌مانده

- Stable ID: HAIF-OUT-084-SAME-STARTER-ZIP-CONTINUITY
- Production ID: G6IP-OUT-084
- Parent input: [IN-085](./PALANG-0.0-IN-20261027-085-SAME-STARTER-ZIP-CONTINUITY.md)
- Root: [POINT-0/047](./GPT6-RAHM-USER-POINT-0-20261027-047-SAME-STARTER-ZIP-CONTINUITY.md)
- Status: PRIOR ZIP BUILD VERIFIED / NEW VERSION RECONCILIATION OPEN

## شواهد تأییدشده
اجرای [40508128142](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40508128142) روی commit `2621508611935e243fe4085c9045193ae19bfedf` موفق بود. همان نام آرشیو اصلی دوباره ساخته شد: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`. ZIP داخلی نسخهٔ 0.3.2، اندازهٔ 19,242 بایت، SHA-256 برابر `861be3d9998e96c8588d03642f70d01a6e2060b7b5056f45ef50008fc6f61da4`، 8 فایل و 16/16 آزمون موفق داشت.

## نقص واقعی کشف‌شده
بازخوانی ZIP نشان داد `manifest.json` نسخهٔ 0.3.2 می‌گوید، اما فایل پروتکل داخل همان ZIP هنوز `Package version: 0.3.1` دارد. این ناهماهنگی باید اصلاح شود. تغییر manifest منبع به 0.3.3 به‌تنهایی ZIP را به‌روز نمی‌کند و تا ساخت مجدد، آزمون و بازخوانی ZIP جدید، نسخهٔ 0.3.3 تأییدشده نیست.

## گام الزامی
همهٔ فایل‌های نسخه/پروتکل/دستورالعمل/آزمون باید هم‌نسخه شوند؛ سپس workflow روی یک SHA دقیق اجرا، ZIP با همان نام اصلی ساخته، دانلود و از داخل artifact استخراج شود؛ هش و اندازه با receipt تطبیق و آزمون‌ها دوباره اجرا شوند. پذیرش میزبان مستقل و restart همچنان جداگانه باز است.
