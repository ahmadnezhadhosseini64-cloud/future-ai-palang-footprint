# NEXT-048 — First Living Master Conformance and Portable Host Recovery

- Stable ID: `G6IP-RAHM-NEXT-048-20261024`
- Production ID: `G6IP-NEXT-048`
- Version: 1.0.0
- Status: OPEN / IN PROGRESS; tests remain NOT RUN until evidence exists.
- Parent: [CURRENT-054](./PALANG-0.0-CURRENT-20261024-054-FIRST-LIVING-MASTER.md)
- First living master: [FIRST-LIVING-MASTER](../../portable/RAHM/FIRST-LIVING-MASTER-PORTABLE-GPT6-HAIF.md)
- Prior hard audit: [EVT-0154](../../architecture/BEHAVIOR-TRACE/EVT-0154-LIVING-ARCHITECTURE-HARD-AUDIT-RUN-2026-10-24.md)
- First acceptance gate: [NEXT-044](./PALANG-0.0-NEXT-20261024-044-EXTRACTABLE-RAHM-CHILD-AND-COLD-START-TEST.md)

## Ordered actions
1. Run NEXT-044 first; export at a named commit and recover in a clean context.
2. Compute SHA-256 over exact exported file bytes with a named implementation; reconcile every manifest entry. Git blob SHA-1 is not SHA-256.
3. Validate INTERACTION_PAIR_SCHEMA.json with a valid and an invalid fixture using a named validator/version; retain raw outputs.
4. Recover state independently from IN-047 and OUT-046; compare mission, checkpoint, lineage, evidence, versions, failures, open gates and next action.
5. Include the first living master in the export inventory; read back both inventory and manifest.
6. Triage missing local links and identifier collisions individually; preserve history and decisions.
7. Update and independently read back the base living mother, canonical docs/REFERENCE_INDEX.md and main integration queue README. Addendum-only is not base integration.
8. Test cold import in a clean context without hidden memory. Record actual host/model/capabilities and missing files.
9. Test a second AI host only if available and authorized; synthetic CI transfer is not real AI-host import.
10. Test persistence restart and idle/background only with an authorized real runtime; otherwise keep NOT VERIFIED/BLOCKED.
11. Fetch and compare each file after every write. Never close a gate without evidence.

## Acceptance
All package digests match; valid schema passes and invalid schema fails; IN and OUT recovery are equivalent; mother/index/queue are integrated and read back; clean-host reconstruction succeeds; unsupported features are explicit. Second-host, persistence and background claims require their own receipts.

## Evidence per action
Test ID; exact input; commit/artifact version; tool/version; host/model; actual UTC and derived Tehran timestamp; raw/expected result; status; evidence path; independent read-back; defect and recovery step.

## Completed first gates (evidence-backed)
- [x] Schema conformance: run [40114363915](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40114363915) — valid fixture 0 errors; invalid fixture 4 errors and rejected.
- [x] Exact-byte SHA-256 inventory comparison: same run PASS across 24 manifest entries.
- [x] Focused relative-link audit: 10 core/chain files checked, zero missing local targets; see [EVT-0156](../../architecture/BEHAVIOR-TRACE/EVT-0156-FIRST-MASTER-HARNESS-CORRECTION-2026-10-24.md).

## Still OPEN / NOT RUN
- Independent reconstruction from IN-047 and OUT-046 and equality comparison.
- Actual cold import in an independent AI host and optional second AI host.
- Persistence after restart and idle/background execution in an authorized runtime.
- Repository-wide remediation of 11 missing links, 60 unreviewed Stable-ID collision groups, other ID collision groups, 13 ambiguous parent edges and one ambiguous timestamp.
- Recheck manifest digests after any package file changes; update and read back base mother/index/queue after any further architectural changes.

## Latest verification receipt — run 40114697473
- [x] Schema valid/invalid fixture conformance passed (0 errors / 4 rejection errors).
- [x] Exact-byte SHA-256 comparison passed for all 24 manifest entries.
- [x] Limited IN/OUT recovery equivalence passed for CURRENT/NEXT/master links and open-gate preservation. Full canonical-state/evidence reconstruction remains OPEN.
- [x] Portable archive built with 25 files; SHA-256 `109cdb9af62f9f4f270aafea96076a5e0177877eb553551ed2fa268e997478df`.
- [x] Evidence: [run 40114697473](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40114697473); [package artifact](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40114697473/artifacts/12567559136).

## Remaining open gates
Full canonical-state reconstruction from raw IN and OUT; real independent AI-host import; second-host conformance; persistent memory after restart; idle/background execution; repo-wide link/identifier collision remediation and ambiguous-parent/timestamp review. Do not mark these complete based on synthetic CI or artifact creation.
