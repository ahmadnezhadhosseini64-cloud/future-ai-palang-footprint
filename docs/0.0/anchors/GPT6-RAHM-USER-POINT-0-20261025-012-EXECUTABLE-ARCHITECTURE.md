# User Point 0/012 — Executable architecture over documentation

- Stable ID: G6IP-USER-POINT-0-012-20261025
- Production ID: G6IP-POINT-0-012
- Version: 1.0.0
- Parent checkpoint: [CURRENT-062](./PALANG-0.0-CURRENT-20261025-062-OPEN-GAPS-AND-CONTINUITY.md)
- User intent: Treat this message as a new Point 0, connect it to the existing architecture, register all remaining defects and next executable steps as 0.0, update the living mother, and continue implementation. The user explicitly rejects report-writing as a substitute for a practical, buildable new-project architecture.
- Previous chain: [POINT-0/011](./GPT6-RAHM-USER-POINT-0-20261025-011-OPEN-GAPS-AND-CONTINUITY.md) → [CURRENT-062](./PALANG-0.0-CURRENT-20261025-062-OPEN-GAPS-AND-CONTINUITY.md).
- New interaction chain: [IN-056](./PALANG-0.0-IN-20261025-056-EXECUTABLE-ARCHITECTURE.md) → [OUT-055](./PALANG-0.0-OUT-20261025-055-EXECUTABLE-ARCHITECTURE.md) → [EVT-0165](../../architecture/BEHAVIOR-TRACE/EVT-0165-EXECUTABLE-ARCHITECTURE-2026-10-25.md) → [CURRENT-063](./PALANG-0.0-CURRENT-20261025-063-EXECUTABLE-ARCHITECTURE.md).
- Active implementation: [HAIF local runtime](../../../../scripts/haif-runtime/haif_runtime.py), [tests](../../../../scripts/haif-runtime/tests/test_runtime.py), [runbook](../../../../scripts/haif-runtime/README.md).
- Living mother: [HAIF initial-model master](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md).
- Governing rule: executable behavior > architecture prose; register → implement → read back → test → repair → verify → reconcile → status.
- Time rule: canonical repository registration time comes from the actual last-change Git commit in UTC; Tehran equivalent must be derived from that same instant. Message time and test time remain distinct.
- Scope: continue the HAIF architecture and local runtime; do not divert to Dropbox unless explicitly reopened.
- Status: REGISTERED IN REPOSITORY; runtime source exists; CI and clean-environment acceptance remain evidence-gated.
