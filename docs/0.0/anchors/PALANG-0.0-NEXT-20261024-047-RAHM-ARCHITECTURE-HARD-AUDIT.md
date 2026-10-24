# NEXT-047 — Next 0.0: Portable Rahm Architecture Hard Audit

- Stable ID: `G6IP-RAHM-NEXT-047-20261024`
- Production ID: `G6IP-NEXT-047`
- Version: 1.0.0
- Status: OPEN / IN PROGRESS; individual tests remain NOT RUN until executed.
- Parent: [CURRENT-053](./PALANG-0.0-CURRENT-20261024-053-PORTABLE-RAHM-HARD-AUDIT.md)
- User Point 0: [G6IP-RAHM-USER-POINT-0-20261024-002](./GPT6-RAHM-USER-POINT-0-20261024-002.md)
- Event: [EVT-0153](../../architecture/BEHAVIOR-TRACE/EVT-0153-USER-POINT-0-PORTABLE-RAHM-HARD-AUDIT-2026-10-24.md)
- Primary existing gate: [NEXT-044](./PALANG-0.0-NEXT-20261024-044-EXTRACTABLE-RAHM-CHILD-AND-COLD-START-TEST.md)

## Execution order
1. Do not bypass NEXT-044. Create a reproducible export artifact and reconstruct it in a clean context; retain raw inputs, outputs, errors, versions and comparisons.
2. Reconcile export manifest against exact bytes with a named SHA-256 implementation. Git blob SHA-1 is not SHA-256.
3. Run positive and negative fixtures against INTERACTION_PAIR_SCHEMA.json with a named validator; retain fixtures and exact outputs.
4. Recover canonical state independently from an IN record and separately from an OUT record, including checkpoint, mother, lineage, evidence, failures, versions, open gates and next action.
5. Audit the tree for broken relative links, duplicate Stable/Production IDs, missing targets, conflicting status claims, stale CURRENT/NEXT targets and package inventory drift. Preserve historical branches; classify duplicates instead of auto-merging.
6. Update living mother, reference index, integration queue, export manifest and evidence ledger additively; fetch and compare every changed file.
7. Test clean-host import. Test a second independent host only if available and authorized.
8. Test persistence across restart and idle/background execution only if a real authorized runtime exists. Otherwise record BLOCKED/UNSUPPORTED and prerequisites.
9. Run regression tests after material changes; do not repeat passing tests without a real change, deployment, need, regression or contradictory evidence.

## Required evidence per test
Test ID; exact input; artifact version/digest; tool and version; host/model; actual UTC timestamp and derived Tehran equivalent; raw and expected results; PASS/FAIL/UNSUPPORTED/NOT RUN; evidence path; independent read-back; defect and recovery action.

## Acceptance gates
- Repository IDs and links match after read-back.
- Export manifest and exact-byte SHA-256 match.
- Valid fixture passes and invalid fixture fails schema validation.
- IN and OUT recovery reconstruct the same canonical state and open gates.
- Clean-host import reconstructs state without hidden chat memory.
- Second-host conformance is separately evidenced, not inferred.
- Persistence/background are verified only with runtime evidence.
- Mother/index/queue agree after additive updates and read-back.


## First hard-audit evidence batch — EVT-0154
- Repository-wide Living Architecture Audit run 40112051555 completed SUCCESS on tested commit `23c8b6b8bbf2585c804f6f7233f81e7cde5d11a1`; details in [EVT-0154](../../architecture/BEHAVIOR-TRACE/EVT-0154-LIVING-ARCHITECTURE-HARD-AUDIT-RUN-2026-10-24.md).
- Structural scan reported 11 missing local links, 60 unreviewed Stable-ID collision groups, 88 Production-ID collision groups, 7 reference-ID collision groups, 36 event-number collision groups, 13 ambiguous parent edges, and one ambiguous timestamp. Treat these as OPEN review work, not a clean pass.
- Focused check of the eight new Point 0/0.0 chain and extension files found zero missing relative-link targets.
- CPREL synthetic transfer workflow passed artifact transfer and digest check, but it is not a full AI-host import/reconstruction test.
- Host adapter synthetic tests passed including restart recovery; live ChatGPT producer was NOT TESTED and repository write was NOT IMPLEMENTED by that adapter.
- Continue first with NEXT-044 export/clean-context recovery. Then triage historic missing links/ID collisions and retain every decision with source-backed evidence. The full JSON Schema fixtures, RAHM package digest, IN/OUT reconstruction and real independent AI-host import remain OPEN / NOT RUN.
