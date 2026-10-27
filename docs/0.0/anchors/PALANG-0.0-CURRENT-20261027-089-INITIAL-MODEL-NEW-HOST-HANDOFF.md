# CURRENT-089 — Initial Model New-Host Handoff

- Stable ID: HAIF-CURRENT-089-INITIAL-MODEL-NEW-HOST-HANDOFF-20261027
- Production ID: HAIF-C089-20261027
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / ACCEPTANCE REQUIRED
- Root: [POINT-0/040](./GPT6-RAHM-USER-POINT-0-20261027-040-INITIAL-MODEL-NEW-HOST-HANDOFF.md)
- Chain: [IN-077](./PALANG-0.0-IN-20261027-077-INITIAL-MODEL-NEW-HOST-HANDOFF.md) → [OUT-076](./PALANG-0.0-OUT-20261027-076-INITIAL-MODEL-NEW-HOST-HANDOFF.md) → [EVT-0213](../../architecture/BEHAVIOR-TRACE/EVT-0213-INITIAL-MODEL-NEW-HOST-HANDOFF-2026-10-27.md)
- Sole active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Host bootstrap: [NEW-HOST-BOOTSTRAP](../../architecture/مدل%20اولیه%20AI/NEW-HOST-BOOTSTRAP-2026-10-27.md)

## Execution order

1. Read the bootstrap and existing starter; do not recreate the engine.
2. Discover current main and latest exact-SHA workflow receipts.
3. Reconcile package manifest coverage and digests through the supported workflow.
4. Run Living Architecture Audit and Portable RAHM Conformance on the same exact final SHA.
5. Export and independently verify the archive, then test import in a clean separate host if authorized access exists.
6. Compare state recovered from IN and OUT; preserve all OPEN gates and failures.
7. Resolve graph findings in small batches under NEXT-051; do not guess CURRENT-065 vs CURRENT-066.
8. Update mother/index/queue only after reading their current versions; read back each changed file.

## State boundary

The existing starter is an executable prototype, not a native GPT plugin. Repository and CI evidence are not proof of actual host import, persistent memory, background execution, or external destination writes. Keep those gates open until direct evidence exists. No NEXT-052.
