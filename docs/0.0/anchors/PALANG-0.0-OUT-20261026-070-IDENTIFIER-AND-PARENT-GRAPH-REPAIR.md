# OUT-070 — Assistant execution decision for evidence-governed graph repair

- Stable ID: HAIF-OUT-070-IDENTIFIER-AND-PARENT-GRAPH-REPAIR-20261026
- Production ID: OUT-070
- Version: 1.0.0
- Status: REGISTERED / ACTIVE / LIVING / VALIDATION PENDING
- Root: [POINT-0/035](./GPT6-RAHM-USER-POINT-0-20261026-035-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md)
- Input: [IN-071](./PALANG-0.0-IN-20261026-071-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md)
- Event: [EVT-0205](../../architecture/BEHAVIOR-TRACE/EVT-0205-POINT-0-035-IDENTIFIER-AND-PARENT-GRAPH-REPAIR-2026-10-26.md)
- Current checkpoint: [CURRENT-083](./PALANG-0.0-CURRENT-20261026-083-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md)

## Decision
Make the source file and its own metadata declaration the identity boundary. Body references are recorded as occurrences but are not promoted into definitions. For parent edges, apply a source-specific override only when its selected path is present among the extracted candidates; otherwise leave the edge ambiguous and emit a warning. A global preference is a fallback only when no source-specific override exists.

## Evidence boundary
The repository audit on commit 8aac51fa544d56913d01a148371c160f4a6a0714 passed as a workflow, but its output still reported missing links and open collision groups. That run predates this point's final changes and is not evidence of the final SHA. The helper tests must be wired into CI and rerun before this output is treated as validated.

## Remaining gates
- Correct the four missing local links reported by the audit.
- Add CI execution for both new helper test modules.
- Rerun audit and portable conformance on the same final main SHA.
- Keep two unresolved parent edges and all unreviewed collision groups open until their own evidence is adjudicated.
- Actual interactive RAHM host import/restart/round-trip remains NOT RUN without destination receipts.
