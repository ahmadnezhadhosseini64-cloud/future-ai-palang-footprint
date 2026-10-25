# EVT-0185 — Portable HAIF GPT-6 Starter Engine

- Stable ID: HAIF-EVT-0185-PORTABLE-HAIF-GPT6-STARTER-ENGINE-20261025
- Production ID: HAIF-EVT-0185-20261025
- Version: 1.0.0
- Status: REGISTERED / LIVING / IMPLEMENTATION RECORDED / TEST RESULT PENDING
- Root: [POINT-0/022](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261025-022-PORTABLE-STARTER-ENGINE.md)
- IN: [IN-052](../../0.0/anchors/PALANG-0.0-IN-20261025-052-PORTABLE-STARTER-ENGINE.md)
- OUT: [OUT-052](../../0.0/anchors/PALANG-0.0-OUT-20261025-052-PORTABLE-STARTER-ENGINE.md)
- Current execution checkpoint: [CURRENT-069](../../0.0/anchors/PALANG-0.0-CURRENT-20261025-069-PORTABLE-STARTER-ENGINE-AND-GATE-CLOSURE.md)
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
