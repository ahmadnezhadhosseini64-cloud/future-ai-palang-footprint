# Integration Completion Gate — Architecture

**Architecture ID:** ARCH-ICG-2026-08-30-001
**Reference ID:** REF-ICG-2026-08-30-001
**Status:** ACTIVE / CANONICAL GATE

## Rule

Recovery is not completion. A pending production is closed only after verified reintegration into every applicable project layer and living documentation identified by the Registration Matrix.

## Required flow

`PENDING → CAPABILITY RECOVERY → ACTUAL WRITE/EXECUTION → PROJECT INTEGRATION → REFERENCE/REGISTRY → ARCHITECTURE PLACEMENT → LIVING DOCUMENTATION → EVIDENCE → VERIFICATION → CLOSE`

## Enforcement

- Re-evaluate applicable destinations after capability recovery.
- Preserve the same Production ID across all layers.
- Update project state, not only an archival/recovery file.
- Require evidence for actual writes/executions.
- Keep PENDING/INCOMPLETE if any required integration step fails.
- Do not treat a recovery file alone as integration evidence.
- Block FINAL/PROVEN until all required integration states have successful evidence.
