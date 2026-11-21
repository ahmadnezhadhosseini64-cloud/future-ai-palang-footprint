# EVT-0304 — معماری مخزن مادر فقط‌مالک و مخزن خصوصی مستقل هر میزبان

- Event ID: EVT-0304
- Parent: POINT-0/084 → IN-127 → OUT-126
- Status: DESIGN REGISTERED / MERGED TO MAIN / IMPLEMENTATION PARTIAL
- UTC event time: 2026-11-21T19:55:28Z (Git commit metadata for event artifact).

## Event

مالک خواست مخزن مادر فقط در اختیار خودش باشد و هر میزبان پس از ثبت و تأیید، فضای خصوصی مستقل و قابل‌بازیابی داشته باشد. دسترسی نوشتن میزبان به مخزن مادر ممنوع است. این تصمیم به طراحی معماری امنیتی و اصلاح پیام یک‌پیامی ورود میزبان منجر شد.

## Controls

- Master repository: PUBLIC READ ONLY for hosts; no host write credential.
- Per-host workspace: one owner-created PRIVATE repository per verified Host ID.
- Optional host write: broker-mediated, GitHub App scoped to that single private repo; never expose token to model.
- Default state: L1_READ_ONLY.
- Unknown public reader: not identifiable as a named host; no automatic Host ID.
- No cross-host repository/credential sharing.
- Owner retains registry, provisioning, export, revoke and promotion authority.

## Evidence and open gates

- Repository metadata confirms the master is public and the connected GitHub identity has owner/admin rights.
- Existing contract records main protection as false; current live branch rules and collaborator/App list are not readable through the available connector.
- Security architecture and revised one-message entry were merged through PR #88; 16/16 changed files were read back from main and SHA-matched.
- Actual GitHub protection, private repo provisioning, App/broker deployment, host acceptance and negative isolation tests remain OPEN. PR #88 merge commit: 446b3c7fe7bef616826ee609f5dc58cc23a1bd00 (2026-11-21T19:57:32Z).
