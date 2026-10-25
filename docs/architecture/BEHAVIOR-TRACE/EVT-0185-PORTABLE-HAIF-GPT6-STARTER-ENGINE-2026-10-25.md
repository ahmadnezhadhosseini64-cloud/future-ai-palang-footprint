# EVT-0185 — Portable HAIF GPT-6 Starter Engine

- Stable ID: HAIF-EVT-0185-PORTABLE-HAIF-GPT6-STARTER-ENGINE-20261025
- Production ID: HAIF-EVT-0185-20261025
- Version: 1.0.0
- Status: REGISTERED / LIVING / LOCAL STARTER TESTS PASS ON f482083 / EXTERNAL HOST GATES OPEN
- Root: [POINT-0/022](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261025-022-PORTABLE-STARTER-ENGINE.md)
- IN: [IN-052](../../0.0/anchors/PALANG-0.0-IN-20261025-052-PORTABLE-STARTER-ENGINE.md)
- OUT: [OUT-052](../../0.0/anchors/PALANG-0.0-OUT-20261025-052-PORTABLE-STARTER-ENGINE.md)
- Time binding: [TIME-BINDING-EVT-0185](./TIME-BINDING-EVT-0185-POINT-0-022-2026-10-25.md)\n- Current execution checkpoint: [CURRENT-069](../../0.0/anchors/PALANG-0.0-CURRENT-20261025-069-PORTABLE-STARTER-ENGINE-AND-GATE-CLOSURE.md)
- Existing queue retained: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Implementation

Added package prototype/haif-gpt6-starter/:
- engine.py — Python standard-library engine, local state, event hash chain, independent IDs, gap register, evidence-gated gap closure and Child promotion, portable bundle digest verification, atomic write.
- test_engine.py — tests for independent identifiers, event tampering, evidence-gated gap closure, promotion gating, portable round-trip and tamper detection, and file read-back.
- GPT6_HOST_INSTRUCTIONS.md — host startup/recovery rules, evidence statuses, architecture loop and honest capability boundaries.
- manifest.json and state.schema.json — machine-readable package and state contracts.
- README.md — quick start and import guidance.
- Updated .github/workflows/living-architecture-audit.yml to run these tests and validate manifest/schema.

## Purpose

Provide an actual moving engine rather than another architecture-only document. Keep it connected to Future AI / Palang Footprint and allow the package to be carried to GPT-6 as host instructions plus runtime/state files. It is a local executable reference implementation, not a native GPT plugin.

## Evidence and status

The files were committed through the repository contents API. The workflow has been wired, but its exact run and artifacts must be inspected before claiming test PASS. A workflow definition is not a test receipt.

## Open gates preserved

- CURRENT-065/CURRENT-066 canonical pointer adjudication.
- NEXT-051 historical graph triage, Issue #20, Issue #21, BOART-FOLLOWUP-01.
- Independent GPT-host import and durable host restart.
- Native host adapter, automatic capture, background execution, external repository write and cross-device persistence.
- Exact-head audit, portable bundle artifact and failure-injection coverage.


## Verified starter execution receipt

- Living Architecture Audit [run 40198249728](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40198249728): SUCCESS on tested content SHA \`4dce5e5a919499a9d016b4949c3968e339e8fd7c\`.
- Starter engine test result: 6 tests passed; py_compile passed; manifest and state schema parsed as valid JSON.
- ZIP created during the workflow: \`audit-output/haif-gpt6-starter-v0.1.zip\`; ZIP SHA-256 reported by the runner: \`f3dc8dde73107d5fd2f8695435d64a86ef7697e0c21d7cf6512d5c888e9c98fc\`.
- Uploaded workflow evidence artifact: ID \`12600178291\`, name \`living-architecture-audit-40198249728\`, artifact digest \`sha256:0dade9e9a288144605e3831db049691e6fe68ce6f45d50f69a641a4e8d6cfd40\`.
- The artifact contains the audit-output folder, including the generated ZIP and digest sidecar. Use the workflow run's Artifacts section to download it.

## Separate open failure retained

Portable RAHM Conformance run [40198220828](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40198220828) failed in its exact-byte manifest inventory SHA scan. This is not a failure reported by the six new starter tests; it remains a separate repository-integrity issue to diagnose and reconcile. Do not conceal this failure or infer its root cause without examining the mismatched inventory entries.

## Acceptance boundary

The local starter package passes seven automated tests on the tested revision. This does not prove native GPT plugin installation, independent GPT-host import, automatic capture, background execution, durable host memory or external repository writes.


## Latest starter verification — run 40198462347

- Result: SUCCESS on exact tested SHA \`f482083cc2aeab82964c271c5d97ba4bb8657ce1\`.
- Seven starter tests passed, including clean-process CLI export/import and tamper rejection.
- ZIP runner digest: \`7372007564d94f02807c41291ea6e0976e8899c2d1c37306c5978b30fe1399df\`.
- Workflow evidence artifact: ID \`12600674334\`, digest \`sha256:aabb3b5bada3386804710a6566f5137fb8f435c1716bff854f6aff268ce611ef\`.
- Independent GPT host import remains NOT PROVEN.
- The portable manifest SHA inventory failure run 40198220828 was resolved by updating the stale workflow digest in EXPORT_MANIFEST.json; follow-up run 40198744680 passed.


## Follow-up integrity resolution — tested SHA 99479872

- Updated docs/portable/RAHM/EXPORT_MANIFEST.json to match the current workflow Git blob SHA and raw-byte SHA-256.
- Portable RAHM Conformance [40198744680](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40198744680): SUCCESS; portable package artifact 12600074529, digest sha256:0d7b0fa8ea010f8516b3091b5bcb623f862d5922b707842675c5240c7d767046.
- Living Architecture Audit [40198744637](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40198744637): SUCCESS; structural checks PASS, pointer checker AMBIGUOUS/BLOCKED, starter tests 7/7 PASS; artifact 12600689796.
- The stale manifest digest issue is resolved for this tested SHA. Pointer ambiguity, historic graph review and real external-host capability gates remain open.


## Latest main-content verification

- Living Architecture Audit [40199078903](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40199078903): SUCCESS on tested SHA ca3745072a35cdca8db74cd62bf8ee07b23c45b3; structural checks PASS; pointer checker AMBIGUOUS/BLOCKED; starter tests 7/7 PASS.
- Starter ZIP SHA-256: 9a594ddb424ef81ec3a1969ef64dc58f34277b94f8114510488ee2103b7a5237.
- Audit artifact ID 12601800399, digest sha256:5edfca23d4f76152bbeb1bcb51830509024270d2a0bbecd66087438fe5208207.
- Portable RAHM Conformance [40199078860](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40199078860): SUCCESS on the same tested SHA; portable package artifact 12601380486, conformance evidence 12601060622.
- The manifest SHA failure is resolved on this tested revision. Real independent GPT-host import and persistent host capabilities remain unproven.


## Latest audit and clean portable ZIP verification

- Latest Living Architecture Audit [40199267408](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40199267408): SUCCESS on tested SHA 78c05af6653dead87ffda4d1ded4db92538a782f; 7/7 starter tests PASS. Audit artifact ID 12601436214, digest sha256:d9c253a5e15a21667e30d9bef926b83da0eb927485479473d77613af8826f199.
- The workflow ZIP contained Python cache files. A clean distribution ZIP was rebuilt excluding __pycache__ and .pyc files, extracted into a fresh temporary directory, and the full seven-test suite was rerun successfully.
- Clean distribution ZIP SHA-256: d8fb3ba5be22bc1064063fed67c4c705531179f221596b56f812c07a89bd028a.
- The clean ZIP contains only manifest.json, test_engine.py, GPT6_HOST_INSTRUCTIONS.md, state.schema.json, README.md and engine.py inside prototype/haif-gpt6-starter/.
- Latest Portable RAHM Conformance remains PASS on tested SHA e0a8683ed2789dcd4804970ac4a2b5a6d1d6a72a (run 40199225642). The intervening time-binding-only update did not alter the package code or export-manifested workflow bytes.


## Latest run on the time-binding-updated content head

- Living Architecture Audit [40199460301](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40199460301): SUCCESS on tested SHA f1e7cf3299714b6cba2cc8db91c962a348b8cd42.
- Structural repository checks PASS; live pointer remains AMBIGUOUS/BLOCKED; starter tests 7/7 PASS.
- Audit artifact ID 12601211931, digest sha256:949f0333c68fc0d0d1285062cf5e352688a3610d114bcbf2dba5607871755501.
- CI-generated ZIP SHA-256: d1d986c9c0d40e8726aeca33da4906d18b9a334402640ccd8247d8b4c4af1cdb.
- Separately cleaned distribution ZIP (no Python cache files) was extracted into a fresh temporary directory and independently passed all 7 tests. SHA-256: d8fb3ba5be22bc1064063fed67c4c705531179f221596b56f812c07a89bd028a.
