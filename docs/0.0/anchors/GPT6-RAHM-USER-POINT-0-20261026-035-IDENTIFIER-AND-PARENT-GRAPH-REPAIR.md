# POINT-0/035 — Evidence-governed identifier and parent-graph repair

- Stable ID: HAIF-POINT-0-035-EVIDENCE-GOVERNED-GRAPH-REPAIR-20261026
- Production ID: POINT-0/035
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EXECUTION REQUIRED
- Previous root/checkpoint: [POINT-0/034](./GPT6-RAHM-USER-POINT-0-20261026-034-INTERACTIVE-RAHM-EXECUTION.md) / [CURRENT-082](./PALANG-0.0-CURRENT-20261026-082-INTERACTIVE-RAHM-EXECUTION.md)
- Chain: [IN-071](./PALANG-0.0-IN-20261026-071-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md) → [OUT-070](./PALANG-0.0-OUT-20261026-070-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md) → [EVT-0205](../../architecture/BEHAVIOR-TRACE/EVT-0205-POINT-0-035-IDENTIFIER-AND-PARENT-GRAPH-REPAIR-2026-10-26.md) → [CURRENT-083](./PALANG-0.0-CURRENT-20261026-083-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md)
- Canonical repository time binding: [TIME-BINDING-POINT-0-035](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-POINT-0-035-EVT-0205-2026-10-26.md).
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## User intent
Treat this message and its carried-forward findings as a new root point. Continue executable work on Path B while preserving Path A and the MASTER–RAHM–CHILD architecture. The user's explicit praise confirms that separating identifier declarations from references is a valuable architectural basis; it does not itself prove code correctness or close a gap.

## Confirmed findings
1. A short locator such as EVT-0091 can occur in multiple distinct historical records; identity must use the full declared identifier and path/provenance, not a number alone.
2. A body mention or index reference must not automatically be interpreted as a declaration owned by that file.
3. Parent edges may be resolved using source-specific, evidence-backed decisions before global preferences; invalid overrides must remain ambiguous, not silently fall back.
4. Repository CI proves only the tested repository SHA. It does not prove import into the actual interactive RAHM host.

## Implemented in repository
- Added scripts/graph_identifier_roles.py to bound identifier declaration extraction to a document's metadata header.
- Added scripts/parent_edge_resolution.py for source-specific parent resolution with a fail-closed response to invalid overrides.
- Added initial regression tests and source-specific role decisions; workflow coverage and exact-head verification are part of this point's open execution.
- Preserved prior history; no historical file is deleted or automatically merged.

## Dual-path invariants
- Path A: continue the existing RAHM portable package and actual-host I1–I8 import/recovery/round-trip validation. Repository package success is not host receipt.
- Path B: repair identifier extraction, parent edges, missing local links and collision groups one evidence-backed group at a time.
- MASTER is canonical; RAHM is the existing test/growth environment; CHILD remains a candidate until independent evidence and explicit MASTER acceptance.
- NEXT-051 remains the only global remediation queue. Do not create NEXT-052 or revive Dropbox.

## Acceptance gates
- Run the new helper tests in CI, not just store them.
- Re-run exact-head graph audit and portable conformance; inspect raw logs and artifacts.
- Fix missing links only where target identity is clear; preserve genuine lineage ambiguity.
- Keep all unadjudicated collision groups and external-host tests OPEN.
