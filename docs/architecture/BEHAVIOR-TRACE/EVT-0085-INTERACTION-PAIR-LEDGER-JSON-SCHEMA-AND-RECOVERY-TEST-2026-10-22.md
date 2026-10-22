# EVT-0085 — دفتر زوج‌های تعامل، طرح‌وارهٔ JSON و آزمون بازیابی

- Stable ID: PALANG-INTERACTION-PAIR-LEDGER-AND-RECOVERY-TEST-2026-10-22-001
- Production ID: IPLR-HAIF-2026-10-22-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / GOVERNING
- Parent: EVT-0084 — Append-only architecture growth
- Master reference: docs/reference/REFERENCE-DOCUMENTS/INTERACTION-PAIR-LEDGER-AND-RECOVERY-MASTER-REFERENCE-2026-10-22-001.md
- Ledger specification: docs/architecture/BEHAVIOR-TRACE/interaction-pair-ledger.schema.json

## Purpose
Add a traceable interaction ledger and machine-readable validation contract without rewriting the initial architecture. Each observed user input and assistant output is represented as a linked pair; interpretation is stored separately from raw evidence. Distinguish observed evidence, inference, and unverified hypothesis.

## Time binding
The canonical repository-registration instant is the actual timestamp of the final commit that changes this event, recorded in UTC; Asia/Tehran time is calculated from that same instant. Message time, event time, operation time, and test time remain separate evidence fields. Never manufacture a missing timestamp.

## Interaction extraction contract
1. Preserve source text and provenance where permitted and available.
2. Assign INT-YYYYMMDD-NNN, IN-YYYYMMDD-NNN, and OUT-YYYYMMDD-NNN; pair suffix NNN must match.
3. Numbering is a contract, not a claim that a live runtime counter exists.
4. Record behavior candidates with evidence spans and confidence; never label a hypothesis as observed fact.
5. Link each pair to event IDs, architecture versions, gaps, tests, and recovery pointers.
6. Append new records; corrections are versioned amendments, not silent overwrites.
7. Validate each record against the JSON Schema before accepting it into the ledger.

## Acceptance / audit
- [x] Ledger fields and pair identity defined.
- [x] JSON Schema created as a separate file.
- [x] Recovery test plan and expected outcomes defined.
- [x] UTC canonical time + derived Tehran time policy included.
- [x] Runtime auto-capture is explicitly marked NOT IMPLEMENTED / NOT VERIFIED.
- [ ] Run automated schema validation in a real runtime.
- [ ] Execute cold-start/restart recovery test and record test evidence.
- [ ] Demonstrate reverse lookup from one input/output ID to all linked events, architecture versions, evidence, and gaps.

## Current truthful status
This event does not assert that future conversations are automatically captured. Gmail, Library, Buffer, Persistent Memory, and Dropbox remain separate destinations and are NOT VERIFIED unless independently tested. A documented test plan is not a passed test.

## Recovery path
Open the master reference, validate a ledger record against the schema, then follow its related event IDs, architecture references, evidence references, gap IDs, and recovery pointer. Record actual results in a new append-only test event.
