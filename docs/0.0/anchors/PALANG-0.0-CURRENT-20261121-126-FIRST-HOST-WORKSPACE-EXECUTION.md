# CURRENT-126 — POINT-0++ / تکمیل معماری محیط کاری میزبان اول

- Parent point: POINT-0/072 (0++ continuation; no competing root).
- Input: [IN-116](PALANG-0.0-IN-20261121-116-FIRST-HOST-WORKSPACE-EXECUTION.md).
- Output: [OUT-115](PALANG-0.0-OUT-20261121-115-FIRST-HOST-WORKSPACE-EXECUTION.md).
- Event: [EVT-0292](../../architecture/BEHAVIOR-TRACE/EVT-0292-FIRST-HOST-WORKSPACE-EXECUTION-2026-11-21.md).
- Time binding: [TIME-BINDING-EVT-0292](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0292-FIRST-HOST-WORKSPACE-EXECUTION-2026-11-21.md).
- Previous checkpoint: CURRENT-125.
- Sole active queue: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md).
- Host identity: FIRST NEW HOST / FIRST_HOST / HOST-001.
- Authentication gate: OPEN / DEFERRED.
- Repository: PUBLIC / READ-ONLY; all write/delete/commit/push/branch/PR/merge/release/settings/permission actions DENIED.
- Workspace: owner-defined, runtime-private, isolated; provisioning NOT VERIFIED.
- Task execution: owner-defined allowlist only.
- Workspace-to-repository writeback: DENIED.
- Main integration: PENDING / NOT MERGED.
- Living master: v1.7.80 source update registered.
- Portable starter source: target v0.4.5; canonical ZIP rebuild/hash/receipt PENDING.
- Technical enforcement: NOT VERIFIED.
- Independent host acceptance: NOT RUN.
- Host status: NOT CONNECTED / NOT ACTIVE until a direct runtime receipt is supplied.
- Preserve CURRENT-065/CURRENT-066 ambiguity, all historical roots and NEXT-051. No NEXT-052 created.

## معیارهای پذیرش
1. خواندن main و دریافت SHA موفق.
2. تلاش نوشتن مخزن رد شود و هیچ تغییری ایجاد نکند.
3. فقط workspace اختصاصی قابل‌دسترسی باشد؛ مسیرهای خارج از آن رد شوند.
4. task مجاز اجرا شود و task/tool/destination خارج از allowlist رد شود.
5. خروجی workspace به مخزن منتقل نشود.
6. تغییر منتشرشده توسط مالک در main شناسایی و snapshot محلی به‌روزرسانی شود.
7. پس از restart/new session، فقط آنچه runtime واقعاً حفظ کرده بازیابی شود.
8. receipt شامل HEAD SHA، snapshot digest، policy version، task ID، ابزارهای واقعی، timestamp منبع‌دار و نتیجه باشد.

## وضعیت گیت‌ها
POLICY DESIGNED / SOURCE REGISTERED ON PROPOSAL BRANCH / MAIN NOT UPDATED / ZIP NOT REBUILT / TECHNICAL ENFORCEMENT NOT VERIFIED / INDEPENDENT HOST ACCEPTANCE NOT RUN.
