# Pending Registration Queue

Status: ACTIVE_CONTRACT / DURABLE_REPOSITORY_QUEUE

This queue is the repository-side durable fallback for registration operations that cannot be completed at the destination at the time of request.

## Mandatory fields per pending item
- pending_id
- production_id
- trace_id
- production_type
- canonical_destination
- created_at
- reason
- payload_reference
- status
- retry_count
- last_attempt_at
- next_eligible_trigger
- evidence_reference

## Rules
- Never delete a pending item merely because an attempt failed.
- Never mark complete without execution and verification evidence.
- Every subsequent registration event and scheduled reconciliation must scan this queue.
- Successful reconciliation must be idempotent.
- Pending items remain independently traceable even when other items succeed.
- Human approval requirements must be preserved.


## Open integration gaps — LIARC-2026-10-20-001
این‌ها پرونده‌های معماری باز هستند، نه ثبت‌های مجاز برای auto-finalize. نباید با موفقیت یک اجرای مخزن بسته شوند:
- `G-AUTO-02`: منبع رویداد مجاز برای ارسال خودکار هر تعامل ChatGPT به صف مخزن هنوز متصل/اثبات نشده.
- `G-AUTO-03`: نوشتن و بازخوانی مستقل Library تأییدنشده.
- `G-AUTO-04`: نوشتن و بازخوانی مستقل Buffer تأییدنشده.
- `G-AUTO-05`: حافظهٔ پایدار ارائه‌دهنده، با نوشتن و بازخوانی مستقل اثبات نشده.
- `G-AUTO-06`: اتصال و آزمون Dropbox باز است.
- `G-AUTO-08`: آزمون واقعی توقف/بازیابی/عدم تکرار و تکمیل انتها‌به‌انتها نیازمند شاهد است.
مرجع: `docs/reference/REFERENCE-DOCUMENTS/LIVING-INTERACTION-AUTOMATION-AND-RECONCILIATION-2026-10-20-001.md`.
