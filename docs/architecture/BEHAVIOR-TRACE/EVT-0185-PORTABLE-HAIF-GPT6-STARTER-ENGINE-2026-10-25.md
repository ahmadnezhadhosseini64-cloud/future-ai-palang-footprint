# EVT-0185 — Portable HAIF GPT-6 Starter Engine

- Stable ID: HAIF-EVT-0185-PORTABLE-HAIF-GPT6-STARTER-ENGINE-20261025
- Production ID: HAIF-EVT-0185-20261025
- Version: 1.0.0
- Status: REGISTERED / LIVING / IMPLEMENTATION RECORDED / TEST RESULT PENDING
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

The local starter package passes its six automated tests on the tested revision. This does not prove native GPT plugin installation, independent GPT-host import, automatic capture, background execution, durable host memory or external repository writes.


## Latest starter verification — run 40198462347

- Result: SUCCESS on exact tested SHA \`f482083cc2aeab82964c271c5d97ba4bb8657ce1\`.
- Seven starter tests passed, including clean-process CLI export/import and tamper rejection.
- ZIP runner digest: \`7372007564d94f02807c41291ea6e0976e8899c2d1c37306c5978b30fe1399df\`.
- Workflow evidence artifact: ID \`12600674334\`, digest \`sha256:aabb3b5bada3386804710a6566f5137fb8f435c1716bff854f6aff268ce611ef\`.
- Independent GPT host import remains NOT PROVEN.
- Separate portable manifest SHA inventory failure run 40198220828 remains OPEN.
