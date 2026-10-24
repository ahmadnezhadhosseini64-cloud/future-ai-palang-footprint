# OUT-045 — Output: Portable Rahm Continuation Contract

- Stable ID: `G6IP-RAHM-OUT-045-20261024`
- Production ID: `G6IP-OUT-045`
- Version: 1.0.0
- Status: REGISTERED / READ-BACK VERIFIED; file fetched after write and IDs/links matched.
- Input: [IN-046](./PALANG-0.0-IN-20261024-046-USER-POINT-0-PORTABLE-RAHM.md)
- User Point 0: [G6IP-RAHM-USER-POINT-0-20261024-002](./GPT6-RAHM-USER-POINT-0-20261024-002.md)
- Event: [EVT-0153](../../architecture/BEHAVIOR-TRACE/EVT-0153-USER-POINT-0-PORTABLE-RAHM-HARD-AUDIT-2026-10-24.md)

## Result
This interaction is anchored as a new Point 0 without overwriting CURRENT-052. CURRENT-053 and NEXT-047 provide an independent continuation. The existing NEXT-044 remains the first execution gate because it governs export creation and clean-context recovery.

## Required sequence
1. Verify current source files and actual branch head.
2. Execute NEXT-044: create a reproducible export and reconstruct in a clean context; retain raw evidence and failures.
3. Reconcile exact-byte SHA-256; Git blob SHA-1 is not SHA-256.
4. Run positive and negative fixtures against the interaction-pair JSON Schema.
5. Recover state independently from an IN record and from an OUT record.
6. Audit broken relative links, duplicate IDs, missing targets, conflicting status claims and package inventory drift.
7. Test clean-host transfer and, if available and authorized, a second independent host.
8. Test persistence and idle/background work only where a real authorized runtime exists.
9. Update mothers, index, queue, manifest and evidence ledger additively; fetch and compare every changed file.

## Evidence boundary
Repository source inspection is complete for CURRENT-050/051/052, NEXT-044, the RAHM package specification, living mother, index and queue. Export/recovery and second-host success are not claimed.

- Hard-audit event: [EVT-0154](../../architecture/BEHAVIOR-TRACE/EVT-0154-LIVING-ARCHITECTURE-HARD-AUDIT-RUN-2026-10-24.md)
