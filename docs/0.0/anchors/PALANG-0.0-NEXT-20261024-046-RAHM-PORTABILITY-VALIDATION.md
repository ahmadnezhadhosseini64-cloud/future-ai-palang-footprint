# NEXT-046 — ۰.۰ بعدی: اعتبارسنجی رحم و انتقال به میزبان AI
- Stable ID: G6IP-RAHM-NEXT-046-20261024
- Production ID: G6IP-NEXT-046
- Version: 1.0.0
- Status: OPEN / IN PROGRESS; test results individually NOT RUN until executed
- Parent: [CURRENT-048](./PALANG-0.0-CURRENT-20261024-048-RAHM-INHERITED-ARCHITECTURE.md)
- Event: [EVT-0148](../../architecture/BEHAVIOR-TRACE/EVT-0148-RAHM-INHERITED-ARCHITECTURE-AND-EXPORTABLE-RECOVERY-2026-10-24.md)

## Execution sequence
1. Read back IN-040, OUT-040, EVT-0148, CURRENT-048 and NEXT-046; match IDs, versions, parent/next links and exact governing rule.
2. Update and read back the inherited architecture master, HAIF mother, GPT-6 interactive living master, Reference Index and integration queue.
3. Inspect the canonical RAHM export manifest and package inventory; do not create competing schemas or IDs without checking existing ones.
4. Compute SHA-256 over exact export bytes and reconcile manifest values; Git blob SHA is not SHA-256.
5. Validate INTERACTION_PAIR_SCHEMA.json with a positive fixture and a negative fixture; retain tool/version and exact results.
6. Test reconstruction from an IN record and separately from an OUT record, recovering related event, versions, evidence, failures and open gates.
7. Import the package into a clean target AI host and independently read back IDs, links, state and open gates. Repeat on a second host only if available and authorized.
8. Test persistence across restart/session boundary and idle background work only with an authorized runtime. If no runtime/permissions exist, mark BLOCKED / UNSUPPORTED and state the prerequisite.
9. Audit relative links, duplicate Stable/Production IDs and conflicting status claims; preserve failures as open issues.
10. Update all relevant mothers and queues only after each test produces evidence; fetch again and reconcile.

## Status rules
- REGISTERED: write receipt.
- READ-BACK VERIFIED: fetched content matches.
- VALIDATED: named test passed with retained evidence.
- INTEGRATED: required links/mothers/index/queue agree after read-back.
- TRANSFER-VERIFIED: clean target import and independent read-back pass.
- ACTIVE/LIVING never means unattended execution unless runtime evidence proves it.
- NOT RUN / BLOCKED / FAIL remain open until recovery is evidenced.

## Restart instruction
Continue here, not from Dropbox. The purpose is an extractable, reconstructable RAHM architecture that can be independently verified in a target host; do not claim portability before passing the transfer tests.