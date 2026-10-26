# POINT-0/023 — Excavation Findings and Dual-Path Continuation

- Stable ID: HAIF-POINT-0-023-EXCAVATION-DUAL-PATH-20261026
- Production ID: HAIF-P023-20261026
- Version: 1.0.0
- Status: REGISTERED / ACTIVE / LIVING / OPEN
- Project: Future AI / Palang Footprint
- Owner: Ahmad Nezhadhosseini / احمد پلنگ
- Canonical time rule: repository registration time is the actual commit timestamp in UTC; derive Asia/Tehran from that same instant after commit metadata is read back. This document's event/message time is contextual, not a substitute.
- Prior model checkpoint: [CURRENT-069](./PALANG-0.0-CURRENT-20261025-069-PORTABLE-STARTER-ENGINE-AND-GATE-CLOSURE.md)
- IN: [IN-053](./PALANG-0.0-IN-20261026-053-EXCAVATION-FINDINGS-AND-DUAL-PATH-CONTINUATION.md)
- OUT: [OUT-053](./PALANG-0.0-OUT-20261026-053-EXCAVATION-FINDINGS-AND-DUAL-PATH-CONTINUATION.md)
- Event: [EVT-0186](../../architecture/BEHAVIOR-TRACE/EVT-0186-EXCAVATION-FINDINGS-AND-DUAL-PATH-CONTINUATION-2026-10-26.md)
- Next execution checkpoint: [CURRENT-070](./PALANG-0.0-CURRENT-20261026-070-DUAL-PATH-EXCAVATION-EXECUTION.md)
- Existing remediation queue retained: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Why this point exists
The preceding excavation produced useful, actionable findings but was delivered as a report rather than executed as the next project step. The user accepted the findings and explicitly required the next work to advance the repository, preserve the findings as a new 0 point, and create the next 0.0 execution point.

## Durable architectural decision: two paths, one project
- Path A — Initial model construction: advance the local executable HAIF engine, portable bundle, recovery and eventual independent-host acceptance.
- Path B — Existing architecture remediation: continue the existing NEXT-051 graph triage, ambiguous CURRENT-065/CURRENT-066 pointer adjudication, ID-collision review, parent/time ambiguity review and repository integrity checks.
- A and B are coordinated but not collapsed into one path. Neither path may be abandoned, silently superseded, or treated as complete because the other advances.
- Do not create NEXT-052 merely to renumber unfinished work. NEXT-051 remains the historical remediation queue until its acceptance criteria are satisfied or explicitly reconciled with evidence.

## Excavation findings preserved
1. A local portable starter exists and has recorded local test evidence; this is not proof of deployment as a native GPT plugin.
2. Clean-process export/import and local integrity controls have evidence in prior repository receipts; current exact-head CI and artifact checks must be read from the actual tested revision before extending claims.
3. Real independent AI-host import, second-host transfer, host-native persistence after restart, automatic message capture and idle/background execution remain OPEN / NOT VERIFIED unless new direct evidence closes each gate.
4. Prior graph audit recorded unresolved stable-ID, production-ID, reference-ID, event-number, parent-edge and timestamp findings. Counts are historical receipts, not a claim of current counts; rerun the audit and adjudicate findings individually.
5. The CURRENT-065/CURRENT-066 pointer conflict must remain AMBIGUOUS/BLOCKED until provenance and consumers are reconciled. Do not select a winner by guess.
6. Dropbox remains OPEN / WAITING and is not the current work target unless the user explicitly reopens it.
7. A previous response incorrectly chose a report-shaped output instead of carrying out the next executable repository actions. Record this as a behavior/process failure: output usefulness does not equal project execution. Corrective rule: after a user accepts findings and directs execution, create the anchored event/point and proceed with the first safe, evidence-backed unchecked action in both paths.

## Acceptance boundary
This point is REGISTERED by the repository write. It is not READ-BACK VERIFIED until fetched independently and compared. It is not INTEGRATED until the IN/OUT/event/current checkpoint, index and queue are updated and read-back matched. It is not VALIDATED until applicable checks pass on the exact revision. External-host capabilities remain unproven until tested in an authorized real host.

## Immediate next actions
See CURRENT-070. Work on the first executable unchecked item in Path A and Path B in a balanced sequence; preserve failures, corrections, evidence references and every still-open gate.