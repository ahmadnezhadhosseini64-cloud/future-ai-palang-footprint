# EVT-0288 — ثبت معماری محیط‌های کاری مستقل میزبان‌ها

- Event ID: EVT-0288
- Point: POINT-0/070
- Input: IN-113
- Output: OUT-112
- Parent event: EVT-0287
- Parent checkpoint: CURRENT-122
- Status: REGISTERED / IMPLEMENTATION PARTIAL

## Event
قرارداد workspace مستقل، شناسه‌گذاری پایدار هر میزبان و جداسازی فعالیت میزبان‌ها از MASTER ثبت شد. ساختار شامل منشور میزبان، inbox قرنطینه، مشاهده‌ها، پیشنهادها، تست‌ها، رسیدها و تصمیم‌های مالک است. ورودی‌ها باید از broker احراز هویت‌شده و مسیر allowlisted عبور کنند.

## Integrity and governance
- No direct host write to main or MASTER.
- No cross-host workspace access.
- Host payloads remain untrusted until validation.
- Only owner-approved, RAHM-validated outcomes may update the living master and canonical ZIP.
- Git folder structure alone is not a security boundary.
- No external host is ACTIVE or provisioned by this event.

## Evidence
- docs/architecture/HOST-WORKSPACES/README.md
- docs/architecture/HOST-WORKSPACES/WORKSPACE-CHARTER-TEMPLATE.md
- docs/architecture/HOST-WORKSPACES/WORKSPACE-ISOLATION-AND-PROMOTION-PROTOCOL.md
- Mother reference append: version 1.7.75
- Multi-host architecture append: version 1.1.0
