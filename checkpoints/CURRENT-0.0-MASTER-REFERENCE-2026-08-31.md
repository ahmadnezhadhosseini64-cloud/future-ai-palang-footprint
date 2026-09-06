# Current 0.0 Master Reference — 2026-09-06

**Project:** Future AI / Palang Footprint  
**Owner:** Ahmad Nezhadhosseini  
**Status:** ACTIVE / LIVE / RECOVERABLE / PERMANENT

## Current 0.0
`0.0-MERGED-2026-09-06-PMRH-XLR`

Current merged checkpoint:
`checkpoints/0.0/0.0-MERGED-CONTINUATION-2026-09-06.md`

This is the single current 0.0 continuation point. It merges the previously active/uncontinued 0.0 lineage with the new Persistent-Memory Recovery Hammer lineage so both remain live and recoverable.

## Merged continuation tracks
### Track A — previous unfinished 0.0
- Previous 0.0: `0.0-2026-09-03-2031-Gonbad`
- Continuation anchor: `XLR-PMA-2026-09-03-001`
- Excavation/revival: `EXC-REV-2026-09-03-001`
- Adapter: `PMA-2026-09-01-001`
- State: `ACTIVE / RECOVERABLE / CONTINUATION REQUIRED`

### Track B — new Persistent-Memory recovery
- Production: `PMRH-2026-09-06-001`
- Hammer: `Palang Persistent-Memory Recovery Hammer`
- Regression test: `PMRH-TEST-NO-MEMORY-LOSS-001`
- State: `ACTIVE / LIVING / PERMANENT / VERIFIED (Repository-side)`
- Recovery route: `NO MEMORY / NO READ-BACK → SAME ID + COMPLETE PAYLOAD → DURABLE REPOSITORY / RECOVERY PENDING → EXCAVATION → SAME ID → MEMORY WRITE → READ-BACK → VERIFY → RECONCILE → CLOSE`

## Mandatory 0.0 rule
On every `0.0`:
`RETRIEVE MASTER → RETRIEVE CURRENT MERGED CHECKPOINT → RETRIEVE APPLICABLE LATEST PROTOCOLS/CHECKPOINTS → RESOLVE RULES → VERIFY REPOSITORY STATE → CONTINUE BOTH ACTIVE TRACKS`

A 0.0 must contain: 0.0 ID, Date, Exact Local Time, IANA timezone, UTC offset, location, status, previous reference, current state, Continuation Anchors, rule-resolution status, and verification status.

## Canonical location/time hard lock
- Location: `Gonbad-e Kavus, Iran`
- IANA Timezone: `Asia/Tehran`
- UTC Offset: `+03:30`

Runtime/IP location is non-authoritative and must not replace the canonical project reference.

## Registration rule
`ثبت کن` means: resolve/apply governing rules → preserve stable Production ID/lineage → write/update canonical destination → read back → verify → reconcile applicable cross-layer state → status.

Operational cycle:
`WRITE → READ-BACK → MATCH → VERIFY → RECONCILE → STATUS`

Never regenerate a successful Production ID. Never duplicate. Never claim VERIFIED without evidence.

## Memory limitation / recovery rule
If a required Memory destination is unavailable or cannot be independently read back:
`PRODUCTION → SAME ID → COMPLETE PAYLOAD → DURABLE REPOSITORY / RECOVERY PENDING → PENDING/UNVERIFIED → EXCAVATION/REVIVAL → SAME ID → WRITE → READ-BACK → VERIFY → RECONCILE`.

The Recovery/Pending store is a live, discoverable holding state, not a graveyard. A later excavation command must recover the original record by the same ID and continue its lineage.

Repository persistence is separate from ChatGPT Provider-level Persistent Memory. Provider-level Memory must remain `NOT AVAILABLE / NOT VERIFIED` unless provider-level WRITE + independent READ-BACK evidence exists.

## Active governing controls
- `PMDRP-2026-08-31-001` — Persistent Memory Deferred Reconciliation
- `PMA-2026-09-01-001` — Persistent Memory Adapter
- `MPGG-2026-09-01-001` — Persistent Memory evidence boundary
- `GEN-EXEC-GOV-2026-09-06-001` — Generation & Execution Governance
- `PEFH-2026-09-06-001` — Palang Execution Fidelity Hammer
- `PMRH-2026-09-06-001` — Palang Persistent-Memory Recovery Hammer
- `PMRH-TEST-NO-MEMORY-LOSS-001` — Permanent recovery regression test

## Continuation rule
The older 0.0 is not considered forgotten or silently closed. Its lineage remains Track A and must be continued from `XLR-PMA-2026-09-03-001` while Track B is followed from `PMRH-2026-09-06-001`.

On return, do not reconstruct from conversational memory alone. Retrieve this master and the merged checkpoint first.

## Closure command
`STOP → RECORD → VERIFY → THEN CONTINUE / GOODBYE`

**English status:** `CURRENT 0.0 = MERGED / BOTH TRACKS ACTIVE / RECOVERABLE / RESUME FROM XLR-PMA + PMRH`

## Historical preservation
The previous full master content remains preserved in Git history. This file is the current operational master and supersedes the prior 2026-09-03 operational pointer without deleting historical evidence.
