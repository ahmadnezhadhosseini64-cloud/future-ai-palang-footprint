# EVT-0188 — 0+ Identity and 0.0 Lineage

- Stable ID: HAIF-EVT-0188-0PLUS-IDENTITY-AND-0-0-LINEAGE-20261025
- Production ID: HAIF-EVT-0188-20261025
- Root: [POINT-0/024](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261025-024-0PLUS-PRODUCTION-MARKER.md)
- IN/OUT: [IN-054](../../0.0/anchors/PALANG-0.0-IN-20261025-054-0PLUS-PRODUCTION-MARKER.md) / [OUT-054](../../0.0/anchors/PALANG-0.0-OUT-20261025-054-0PLUS-PRODUCTION-MARKER.md)
- Current continuation: [CURRENT-071](../../0.0/anchors/PALANG-0.0-CURRENT-20261025-071-0PLUS-ENGINE-AND-HARD-AUDIT.md)
- Status: IMPLEMENTATION COMMITTED / CORRECTED ENGINE CI PASS 12/12 / RELEASE 0.2.1 AUDIT PENDING

## Why this matters
The architecture must distinguish canonical identity from a significance marker. Treating `0+` as a second root creates duplicate anchors, split lineage and ambiguous recovery. The engine now stores labels `0` and `0+` on one canonical point and links `0.0` as a child continuation.

## Regression tests added
1. Valid root: labels `0` and `0+`, one canonical point ID, production marker true; child `0.0` references that root.
2. Invalid root: `0+` alone is rejected; a second point cannot claim the same `0+` alias.

Hard-audit evidence: run [40213050985](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40213050985) failed because `append_event` received `kind` twice when registering a point. This is a real implementation defect, not a project-architecture failure. Corrected in engine commit `ab20a52d111f58c243c0e218359ae798c1072616` by naming the point metadata field `point_kind`. The corrected exact-head run [40213205539](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40213205539) is pending. Time binding: [POINT-0/024 time binding](./TIME-BINDING-POINT-0-024-EVT-0188-2026-10-25.md).


## Additional hard-audit pass
- The verifier now reconciles every point record against the append-only `POINT_REGISTERED` event, rejects tampered point fields and requires continuation parents to precede their children (self-parenting is rejected).
- Living Architecture Audit [40213463189](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40213463189): SUCCESS on `49485c593ebd6a3d115c05ddda8e8997b3c5138e`; 12/12 starter tests passed.
- The release was then bumped to v0.2.1 (manifest and README). Exact release-head audit [40213697030](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40213697030) was still pending at the time of this entry.


## Final v0.2.1 verification
- Exact-head audit [40213760585](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40213760585) passed on `0819d97283d892411a6868c544e92752a8c35c55`; 12/12 tests passed.
- Clean distribution and CLI smoke receipt: [EVT-0189](./EVT-0189-0PLUS-CLEAN-DISTRIBUTION-SMOKE-2026-10-25.md).
- Clean ZIP SHA-256: `51a5f9a6def97a0564a8b6542bbf4a5b9ca46a81a267a4a02db7c53511e16f2d`.
- Independent GPT-6 host import remains OPEN / NOT PROVEN.
