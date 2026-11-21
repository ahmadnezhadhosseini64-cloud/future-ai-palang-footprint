# OUT-115 — ثبت قرارداد محیط کاری محدود FIRST_HOST

- Point: POINT-0/072 (0++)
- Input: IN-116
- Contract: [FIRST-HOST-RESTRICTED-WORKSPACE-EXECUTION](../../reference/REFERENCE-DOCUMENTS/FIRST-HOST-RESTRICTED-WORKSPACE-EXECUTION-AND-READ-ONLY-REPOSITORY-CONTRACT-2026-11-21-001.md)
- Host identity: FIRST NEW HOST / FIRST_HOST / HOST-001
- Authentication gate: OPEN / DEFERRED
- Repository permission: READ-ONLY; all write/delete/branch/PR/merge/release/admin actions DENIED.
- Workspace permission: only owner-defined tasks in explicitly provisioned workspace; allowlisted tools/destinations only.
- Workspace-to-repository sync: DENIED.
- Owner message timestamp: UNKNOWN / UNVERIFIED.

## نتیجهٔ ثبت
قرارداد مستقل معماری میزبان اول ایجاد شد. چرخهٔ دریافت سند مادر، خواندن HEAD واقعی مخزن، تطبیق manifest، به‌روزرسانی workspace، اجرای task مجاز و تولید receipt محلی تعریف شده است. هر تغییر مرجع فقط توسط مالک و جدا از میزبان به مخزن وارد می‌شود.

## مرز شواهد
این OUT ثبت تغییر در شاخهٔ پیشنهاد و تعریف سیاست را اعلام می‌کند؛ به معنی ادغام main، ساخت ZIP، provisioning محیط واقعی، اجرای آزمون میزبان یا قبولی فنی نیست.
