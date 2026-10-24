# CURRENT-046 — نقطهٔ ۰.۰ زنده: جایگزین قابلیت میزبان و ممیزی معماری
- Stable ID: G6IP-RAHM-CURRENT-046-20261024
- Production ID: G6IP-CURRENT-046
- Version: 1.0.1
- Status: REGISTERED / READ-BACK VERIFIED for listed repository artifacts; runtime capability validation remains OPEN.
- Parent: [CURRENT-045](./PALANG-0.0-CURRENT-20261024-045-RAHM-PORTABLE-HOST-PERSISTENCE.md)
- Input: [IN-038](./PALANG-0.0-IN-20261024-038-CAPABILITY-FALLBACK-AND-AUDIT.md)
- Output: [OUT-038](./PALANG-0.0-OUT-20261024-038-CAPABILITY-FALLBACK-AND-AUDIT.md)
- Event: [EVT-0146](../../architecture/BEHAVIOR-TRACE/EVT-0146-HOST-CAPABILITY-FALLBACK-AND-ARCHITECTURE-AUDIT-2026-10-24.md)
- Focused host capability Point 0: [G6IP-RAHM-HOST-PERSISTENCE-POINT-0-20261024-001](./GPT6-RAHM-HOST-PERSISTENCE-POINT-0-2026-10-24-001.md)
- Fallback architecture: [HOST-CAPABILITY-FALLBACK](../../architecture/HOST-CAPABILITY-FALLBACK/README.md)
- Portable package: [RAHM package](../../portable/RAHM/RAHM_BOOT.md)
- Next action: [NEXT-044](./PALANG-0.0-NEXT-20261024-044-FALLBACK-TEST-AND-INDEX-RECONCILIATION.md)

## State and open gates
- Host fallback architecture specifications: written; deployment not performed.
- Index prior fetch gap: prior 404 recovered by successful fetch; post-update read-back remains pending.
- Export SHA-256 verification: OPEN.
- Persistent host memory, idle background, clean-context and second-host tests: NOT VERIFIED / NOT RUN.
- Existing main HAIF CURRENT-052 and Rahm CURRENT-044/045 anchors remain preserved; no lineage overwrite.


## Read-back reconciliation — 2026-10-24
- Status: REGISTERED / READ-BACK VERIFIED for the new IN-038, OUT-038, EVT-0146, CURRENT-046, NEXT-044, five fallback architecture files, REFERENCE_INDEX, integration queue and three living mother documents. Exact paths were fetched after writes; key IDs and links were present.
- The previous REFERENCE_INDEX 404 gap is CLOSED for this cycle: fetch succeeded before update; the index was updated with CURRENT-046/NEXT-044 and then fetched again. Returned blob SHA: `6fc34f2d9433280b0a9c247c20533d2405f38d76`; marker/link match confirmed.
- JSON syntax checks: PASS for HOST_CAPABILITY_MANIFEST.json, INTERACTION_PAIR_SCHEMA.json and EXPORT_MANIFEST.json. This is syntax parsing only, not full JSON Schema conformance.
- Still OPEN: SHA-256 byte-level manifest verification; JSON Schema valid/invalid fixture test; host memory restart test; idle background execution test; runtime installation; clean-host and second-host tests; comprehensive link audit.
- No runtime capability is marked active merely because its architecture has been written.
