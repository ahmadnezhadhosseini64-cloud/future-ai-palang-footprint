# EVT-0287 — تثبیت دفتر دائمی ورودی/خروجی میزبان‌ها

- Event ID: EVT-0287
- Status: ACTIVE / LIVING / REPOSITORY-REGISTERED
- Parent: POINT-0/069
- Input/output: IN-112 → OUT-111
- Governing architecture: [Multi-host permanent interaction ledger](../مدل%20اولیه%20AI/معماری%20اتصال%20چندمیزبانی%20و%20دفتر%20دائمی%20تعاملات.md)
- Master: living master version 1.7.74 (append-only)
- Current checkpoint: CURRENT-122
- Sole queue: NEXT-051

## Purpose
تبدیل خواستهٔ مالک به قرارداد اجرایی: هر تعامل واقعی از میزبان‌های مجاز باید با شناسه مستقل IN/OUT، منشأ، والد، زمان قابل اثبات، digest، طبقه‌بندی حریم خصوصی و رسید بازخوانی به‌صورت append-only ثبت شود. ورودی میزبان هرگز مستقیم وارد MASTER نمی‌شود.

## Changes
- تعریف Host Registry و شناسه میزبان/نشست؛
- تعریف event ledger و جفت مستقل IN/OUT؛
- ثبت وضعیت صریح برای نبود پاسخ، عدم اتصال، شکست نوشتن و شکست read-back؛
- تعریف durable write + read-back + receipt؛
- تعریف quarantine، تطبیق میان میزبان‌ها، RAHM، CHILD و تأیید مالک؛
- حفظ حداقل‌سازی داده و منع ثبت secret؛
- حفظ یک ریشه و صف یگانه.

## Verification boundary
این رویداد ثبت معماری و قرارداد را اثبات می‌کند. آزمون CI synthetic adapter به‌عنوان شاهد کد مسیر adapter شناخته می‌شود، اما اتصال واقعی میزبان‌ها، worker مستقر و credential زنده را ثابت نمی‌کند. وضعیت‌های مذکور OPEN تا رسید end-to-end واقعی باقی می‌مانند.

## Time
زمان پیام کاربر UNKNOWN / UNVERIFIED. زمان دقیق این رویداد از commit واقعی همین فایل در TIME-BINDING-EVT-0287 ثبت می‌شود.