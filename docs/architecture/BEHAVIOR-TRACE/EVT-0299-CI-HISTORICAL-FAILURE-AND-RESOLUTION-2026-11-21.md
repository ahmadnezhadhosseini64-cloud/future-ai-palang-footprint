# EVT-0299 — Historical CI inconsistency preserved and resolved

- Stable ID: HAIF-EVT-0299-CI-FAILURE-RESOLUTION-2026-11-21-001
- Status: ACTIVE / LIVING / HISTORICAL-FAILURE-PRESERVED / REPAIR-COMMITTED / LATEST-CI-PENDING
- Root: POINT-0/077 (0++)
- Chain: CURRENT-132 → IN-123 → OUT-122 → EVT-0299 → TIME-BINDING-EVT-0299 → CURRENT-133 → NEXT-051
- PR: #64
- Sole queue: NEXT-051

## Event
The first portable conformance execution exposed a stale expected-chain assertion: the starter README had moved to CURRENT-132 while test_engine.py still expected CURRENT-131. The owner authorized correction and explicitly required preservation of the failed state and its history.

## Owner authorization and chain
- IN-123 records the owner's explicit approval to repair the mismatch while preserving the failed state.
- OUT-122 records the additive correction and follow-up recurrence.
- CURRENT-133 is the linked checkpoint; NEXT-051 remains the sole queue.

## Resolution
Updated the test assertion to include the CURRENT-132 continuation. The failed run remains recorded in IN-123 and its original Actions evidence; no history is erased.

## Passing evidence at exact head
9190b0a9c2dcf1db0133bd937be0bb1a81d3624c:
- 44911581459 — Portable RAHM Conformance and Digest Evidence — success.
- 44911581473 — Living Architecture Audit — success.
- 44911581532 — Universal AI Host Contract Tests — success.
- 44911581743 — Universal AI Host Connectivity Tests — success.

## Boundary
This is branch CI verification only. PR #64 remains subject to review/merge. ZIP build, exact archive hash/read-back and clean-host recovery remain separate acceptance gates.


## Follow-up recurrence retained (not overwritten)
At head c49e3db2332925b85061219505398ee86abe9441, the portable conformance and living architecture audit failed again because the same expected CURRENT-133 chain was missing from GPT6_HOST_INSTRUCTIONS.md (and the package README). Runs 44912041984 and 44912042023 preserve this second occurrence. Both package documents have now been updated to include the exact chain. New exact-head CI is pending; the earlier passing run remains historical evidence for its own SHA only.


## Third stale-copy recurrence and correction (latest source update)

- Exact head `0c36063afe9b5ec44f30da9d7031a2f000967cff` failed portable conformance run `44912318893` because `INDEPENDENT_HOST_RECOVERY_PROTOCOL.md` still advertised an older canonical chain. The package test requires the same CURRENT-133 chain in four host-facing contracts.
- The mismatch was not deleted. Run `44912318893` and its extracted-ZIP assertion remain preserved.
- Corrective source updates now add the full CURRENT-133 chain to `INDEPENDENT_HOST_RECOVERY_PROTOCOL.md`, `INTERACTION-RESPONSE-AND-ANCHOR-PROTOCOL.md`, and `HOST_GROWTH_AND_REPOSITORY_SYNC_CONTRACT.md`; GPT6_HOST_INSTRUCTIONS.md and README.md were already aligned.
- New exact-head checks are required after these three additive changes. Earlier successful runs apply only to their own source SHA.
