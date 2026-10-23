# EVT-0122 — Bidirectional IN/OUT Recovery Gate

- Event ID: EVT-0122
- Stable ID: PALANG-BIDIRECTIONAL-IN-OUT-RECOVERY-2026-10-23-001
- Production ID: BIOR-HAIF-2026-10-23-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / IMPLEMENTED-IN-REPOSITORY / CI-PASS / ARTIFACT-READ-BACK-VERIFIED / FRESH-SESSION-NOT-RUN
- Parent: EVT-0121
- Entry checkpoint: [NEXT-024](../../0.0/anchors/PALANG-0.0-NEXT-20261023-024-CONTINUITY-HISTORIC-AND-COLD-START.md)
- Current pair: [IN-026](../../0.0/anchors/PALANG-0.0-IN-20261023-026-REGISTER-ACTIVE-CONTINUATION.md) / [OUT-026](../../0.0/anchors/PALANG-0.0-OUT-20261023-026-REGISTER-ACTIVE-CONTINUATION.md)

## Purpose
The NEXT-024 repository cold-start regression passes, but it does not yet prove that recovery can start independently from either an input anchor or an output anchor. This is the next active gate, separate from global live capture and external persistence.

## Required behavior
1. Starting from an IN anchor, recover the paired OUT, interaction/event, canonical master, queue item, source/evidence, open gaps and next action.
2. Starting from an OUT anchor, recover the paired IN and the same continuation graph.
3. Reject missing, stale, ambiguous or mismatched pair IDs; preserve multiple 0.0 anchors without merging them.
4. Verify all required local links and identifiers against repository state, not a copied chat summary.
5. Return explicit statuses for recovered, partial, blocked and not-run; never infer host-wide capture or external destination persistence.
6. Add regression tests for both directions, missing pair, mismatched IDs, stale master/queue links and preservation of predecessor/successor checkpoints.
7. Run CI on the exact final main HEAD, inspect logs and artifact, then independently read back the final test/event/master/queue records.

## Acceptance boundaries
- The existing NEXT-024 cold-start regression is PASS for its tested commit/run only.
- IN→OUT and OUT→IN end-to-end recovery: NOT RUN.
- Fresh ChatGPT session recovery: NOT RUN.
- Live host-wide IN/OUT capture: OPEN / NOT PROVEN.
- Historic source census / Issue #21 remains OPEN.
- No automatic MASTER mutation; owner review is required for structural promotion.


## Canonical graph bindings
- Canonical master: [CCCMR](../../reference/REFERENCE-DOCUMENTS/CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md)
- Integration queue: [Architecture Integration Queue](../INTEGRATION-QUEUE/README.md)
- Evidence integrity target (not a production test PASS): [EVT-0120 resolver smoke evidence](../../../data/interaction-pairs/evidence/EVT-0120-RESOLVER-SMOKE-EVIDENCE.txt)
- Current pair identity: `INT-20261023-026` — [IN-026](../../0.0/anchors/PALANG-0.0-IN-20261023-026-REGISTER-ACTIVE-CONTINUATION.md) / [OUT-026](../../0.0/anchors/PALANG-0.0-OUT-20261023-026-REGISTER-ACTIVE-CONTINUATION.md)


## Execution evidence — bidirectional repository recovery PASS
- GitHub Actions run [40005934719](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40005934719): SUCCESS on tested HEAD `30f0eca4877039409ca3b0eda8643b6f8e0f4634`.
- Test suite: **47 tests ran; OK**. Both workflow steps `Recover interaction graph starting from IN anchor` and `Recover interaction graph starting from OUT anchor` succeeded.
- Artifact ID: `12523149825`; artifact ZIP SHA-256: `fbda979225dc567c54a8bcf984363f6a4e242fe7f602859e95033e69733201d2`.
- Artifact was downloaded and inspected. `recovery-from-IN.json`: `RECOVERED`, IN-026 → OUT-026, zero failures. `recovery-from-OUT.json`: `RECOVERED`, OUT-026 → IN-026, zero failures. Both preserve Issue #20 and Issue #21 as OPEN.
- Run `40005682381` failed before this correction because the anchor pair identity and EVT-0122's direct canonical graph bindings were missing. Those gaps were corrected; the failed run is preserved as evidence, not hidden.
- Boundary: this proves repository-state recovery on the tested SHA only. A separate fresh ChatGPT session, host-wide capture, and external persistence remain NOT RUN / NOT PROVEN.
