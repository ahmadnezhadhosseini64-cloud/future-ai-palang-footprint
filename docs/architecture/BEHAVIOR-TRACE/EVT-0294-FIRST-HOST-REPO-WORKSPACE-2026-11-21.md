# EVT-0294 — ثبت نقطهٔ میزبان اول و محیط اجرای مخزن

- Event ID: EVT-0294
- Parent chain: POINT-0/075 → IN-118 → OUT-117
- Event type: OWNER_DIRECTIVE / ARCHITECTURE_DECISION / HOST_HANDOFF
- Canonical repository: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint
- Observed main base SHA: e267c3f6f9254ef06cef38d2a5b8209a0756e5cd
- Proposal branch: haif/point-0-075-first-host-repo-workspace
- Decision: first host must receive authenticated READ access and a real isolated EXECUTE workspace; branch-scoped WRITE is permitted only when explicitly granted by the connected GitHub app; changes reach main through PR review.
- Security: no credentials in chat; no assumed OAuth; no direct privileged writes to main; no claiming remote host launch.
- Acceptance: source read-back, exact HEAD, working-tree identity, actual test output, diff, branch/PR reference, and host receipt.
- Event commit time is recorded separately in TIME-BINDING-EVT-0294. Exact user-message time remains UNKNOWN / UNVERIFIED.
