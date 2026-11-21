# OUT-126 — خروجی: معماری مخزن مادر فقط‌مالک و workspaceهای خصوصی مستقل

- Parent: POINT-0/084
- Source: IN-127
- Status: DESIGN REGISTERED ON PROPOSAL BRANCH / IMPLEMENTATION PARTIAL

## نتیجهٔ طراحی

1. مخزن مادر فقط مرجع عمومی READ است؛ میزبان AI هیچ credential نوشتن برای آن دریافت نمی‌کند.
2. هر میزبان تأییدشده یک private repository مستقل می‌گیرد که مالک ایجاد می‌کند و Host ID/Workspace ID را به آن نگاشت می‌کند.
3. مخزن خصوصی حساب شخصی به collaborator نقش read-only نمی‌دهد؛ میزبان به‌عنوان collaborator اضافه نمی‌شود.
4. مسیر نوشتن احتمالی فقط از broker احراز هویت‌شده با GitHub App محدود به یک private repo و کمترین مجوز ممکن می‌گذرد؛ token در secret manager می‌ماند و به مدل نمی‌رسد.
5. تا زمان استقرار broker و آزمون‌های منفی، همهٔ میزبان‌ها L1_READ_ONLY هستند و خروجی را به‌صورت export برای مالک تحویل می‌دهند.
6. خوانندهٔ ناشناس مخزن عمومی قابل شناسایی فردی و ثبت خودکار نیست؛ فقط enrollment کنترل‌شده و رسید واقعی پذیرفته می‌شود.
7. حفاظت واقعی main، audit collaborator/App، ساخت private repos، broker، App scope و cross-host isolation هنوز OPEN / NOT VERIFIED هستند.

## گیت‌های باز

- اعمال/تأیید قواعد main در GitHub.
- بررسی collaborator، deploy key و GitHub App access در مخزن مادر.
- ایجاد الگوی private repo برای هر Host ID.
- استقرار GitHub App و broker با نگاشت server-side.
- آزمون رد دسترسی Host A به Host B و MASTER.
- آزمون revoke، export، restore و audit.
