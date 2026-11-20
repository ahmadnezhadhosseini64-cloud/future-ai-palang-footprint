# IN-112 — درخواست تثبیت دائمی ورودی/خروجی میزبان‌ها

- Parent: POINT-0/069
- Status: ACTIVE / LIVING
- User intent: هر ورودی و خروجی واقعی از میزبان‌های متصل، در صورت عبور از مسیر مجاز، به‌صورت دائمی، قابل‌ردیابی، متصل به نقاط قبلی و دارای لنگر زمانی و رسید ثبت شود.
- Governance: میزبان‌ها داده و تجربه برای تکامل فراهم می‌کنند، اما مالکیت و اختیار تغییر سند مادر نزد کاربر باقی می‌ماند.
- Required architecture: per-host registry, event ledger, paired IN/OUT anchors, quarantine-first intake, provenance, UTC time binding, payload digest, privacy minimization, durable write, read-back receipt, failure-gap recording, RAHM validation, CHILD proposal and explicit owner approval.
- Existing code boundary: repository includes `scripts/host_adapter.py` and `scripts/host_adapter_github_worker.py`; CI has tested synthetic authenticated durable intake and worker-related paths. This does not prove an external AI host is live-connected or that a worker is deployed with real credentials.
- Exact user-message timestamp: UNKNOWN / UNVERIFIED.
- Next: OUT-111.