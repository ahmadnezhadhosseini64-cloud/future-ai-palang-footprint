# EVT-0292 — POINT-0++ / معماری محدود میزبان اول

- Point: [POINT-0/073](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261121-073-FIRST-HOST-RESTRICTED-EXECUTION-0PLUSPLUS.md).
- Input: [IN-116](../../0.0/anchors/PALANG-0.0-IN-20261121-116-FIRST-HOST-EXECUTION-BOUNDARY.md).
- Output: [OUT-115](../../0.0/anchors/PALANG-0.0-OUT-20261121-115-FIRST-HOST-EXECUTION-BOUNDARY.md).
- Contract: [FHRWE-2026-11-21-001](../../reference/REFERENCE-DOCUMENTS/FIRST-HOST-RESTRICTED-WORKSPACE-EXECUTION-AND-READ-ONLY-REPOSITORY-CONTRACT-2026-11-21-001.md).
- Host role: FIRST NEW HOST / FIRST_HOST / HOST-001.
- Authentication gate: OPEN / DEFERRED.
- Repository: READ-ONLY; workspace tasks: OWNER-DEFINED / ALLOWLISTED ONLY.
- Repository writeback: DENIED.
- Exact user-message timestamp: UNKNOWN / UNVERIFIED.
- Status: POLICY REGISTERED ON PROPOSAL BRANCH / NOT MERGED / TECHNICAL ENFORCEMENT NOT VERIFIED / HOST ACCEPTANCE NOT RUN.

## رویداد
مالک درخواست کرد نقطهٔ جاری ۰++ شود و معماری میزبان اول کامل گردد تا پس از دریافت سند مادر متنی، میزبان بتواند به مخزن وصل شود، نسخهٔ جاری را بخواند، workspace اختصاصی خود را در محدودهٔ تعریف‌شدهٔ مالک به‌روز کند و فقط وظایف مجاز را اجرا کند.

## مرز اختیار
میزبان مدیر مخزن نیست. دسترسی مخزن فقط‌خواندنی است؛ workspace فقط محیط واقعی و provision‌شده با allowlist مالک است. هر نوع نوشتن/حذف/commit/push/branch/PR/merge/release/settings/permission و writeback ممنوع است. میزبان نمی‌تواند دسترسی، task scope یا مقصدهای خود را گسترش دهد.

## شواهد
قرارداد و اسناد در شاخهٔ پیشنهاد ثبت شده‌اند. main merge، canonical ZIP build/receipt، sandbox/ACL واقعی و آزمون میزبان مستقل هنوز PENDING / NOT VERIFIED / NOT RUN هستند.
