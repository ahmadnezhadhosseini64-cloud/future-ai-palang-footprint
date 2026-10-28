# CURRENT-109 — گام ۰.۰: ثبت پایدار و بازسازی بستهٔ جاری

- Stable ID: HAIF-CURRENT-109-REPOSITORY-PERSISTENCE-REPAIR-20261028
- Production ID: G6IP-CURRENT-109
- Previous checkpoint: [CURRENT-108](./PALANG-0.0-CURRENT-20261028-108-INDEPENDENT-HOST-RECOVERY.md)
- Point 0: [POINT-0/059](./GPT6-RAHM-USER-POINT-0-20261028-059-REPOSITORY-PERSISTENCE-REPAIR.md)
- Input: [IN-097](./PALANG-0.0-IN-20261028-097-POINT-059-REPOSITORY-PERSISTENCE-REPAIR.md)
- Output: [OUT-096](./PALANG-0.0-OUT-20261028-096-POINT-059-REPOSITORY-PERSISTENCE-REPAIR.md)
- Event: [EVT-0235](../../architecture/BEHAVIOR-TRACE/EVT-0235-POINT-059-REPOSITORY-PERSISTENCE-REPAIR-2026-10-28.md)
- Sole active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Status: ACTIVE / LIVING / REPOSITORY WRITE + READ-BACK VERIFIED / EXTERNAL HOST ACCEPTANCE OPEN

## Canonical chain
`POINT-0/059 → IN-097 → OUT-096 → EVT-0235 → CURRENT-109 → NEXT-051`

Preserved prior chain: `POINT-0/058 (0+) → IN-096 → OUT-095 → EVT-0233 → CURRENT-108 → NEXT-051`. EVT-0234 collision history remains preserved. Do not create NEXT-052.

## Verified findings carried forward
- The previous local hard-audit bundle is evidence-only and not release-ready as a current paired package.
- The inner package's 23/23 tests and ZIP integrity do not prove external-host acceptance.
- The bundled master reference was version 1.7.24, while the repository mother reference is version 1.7.29; rebuild both from the same source state before presenting as current.
- External host import, exact identity read-back, negative-control test, fresh-session/restart recovery, second-host recovery, persistent memory, Buffer, Dropbox, and host write-back remain OPEN / NOT VERIFIED.
- CURRENT-065/CURRENT-066 pointer/overlay lineage conflict remains OPEN; do not resolve by inference.
- NEXT-051 remains the only active queue; no NEXT-052.

## Next actions
1. Repository chain and central pointers are written and read back; the current checkpoint is repository-verified.
2. Update `docs/0.0/README.md`, `docs/REFERENCE_INDEX.md`, and the living mother reference to the verified chain and status.
3. Rebuild the canonical ZIP and `LIVING_MASTER_REFERENCE.md` from the same current main/source commit, preserve stable package identity/name/version unless a governing change requires otherwise, and independently check SHA-256 + byte count + receipt.
4. Run a real independent AI-host import with both artifacts; capture raw receipt, perform negative control and fresh-session/restart recovery.
5. Keep every gate OPEN until its own evidence is read back and matched.
