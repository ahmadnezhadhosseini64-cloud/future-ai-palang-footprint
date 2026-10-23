# EVT-0109 — آزمون کنترل‌شدهٔ بازگشت شاخه و حفظ نسخهٔ شکست‌خورده

- Stable ID: EVT-0109-CONTROLLED-GIT-ROLLBACK-RECOVERY-TEST-2026-10-23
- Production ID: EVT-0109
- Version: 1.0.0
- Parent event: [EVT-0108](./EVT-0108-LIVING-ARCHITECTURE-EXECUTION-AND-EVIDENCE-CYCLE-2026-10-23.md)
- Governing lesson: [LAL-20261023-007](../ARCHITECTURE-LESSONS/lessons/LAL-20261023-007-ROLLBACK-AS-NEW-LINEAGE-EVENT.md)
- Governing master: [CMIND](../../reference/REFERENCE-DOCUMENTS/CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-MASTER-REFERENCE-2026-10-22-001.md)
- Verification checkpoint: [VERIFY-INT-20261023-020](./VERIFICATION-CHECKPOINT-INT-20261023-020.md)
- Status: BOUNDED REPOSITORY BRANCH ROLLBACK TEST PASS; FULL SYSTEM / HOST / EXTERNAL RECOVERY OPEN

## Test objective
Prove that an isolated Git branch can create a simulated failed successor, preserve that candidate on a separate evidence branch, and then restore the test branch reference to a named baseline without deleting the candidate evidence.

## Test setup
- Baseline commit: [beebca7](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/commit/beebca722fe52d1d628ecfad85dc480ee18a4d16), canonical UTC 2026-10-23T02:12:50Z; Tehran 2026-10-23T05:42:50+03:30.
- Test branch: test/rollback-recovery-int-20261023-020.
- Evidence branch: evidence/rollback-candidate-int-20261023-020.
- Simulated candidate file: docs/architecture/ARCHITECTURE-LESSONS/rollback-test/ROLLBACK-TEST-CANDIDATE-INT-20261023-020.md.
- Candidate commit: [fd5d193](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/commit/fd5d19385ad3220bf0e8414bed7ad162256d4e1f), created_at 2026-10-23T02:13:28Z; Tehran equivalent 2026-10-23T05:43:28+03:30.
- The test candidate was created only on the isolated test branch; it was not merged into main.

## Actual procedure and results
1. Create the test branch from the named baseline: PASS.
2. Commit a simulated failed successor on the test branch: PASS; candidate commit fd5d19385ad3220bf0e8414bed7ad162256d4e1f.
3. Create the separate evidence branch at the candidate commit: PASS.
4. Move the isolated test branch reference back to the named baseline with expected-head guard: PASS; update_ref returned success.
5. Fetch the candidate file from the restored test branch: NOT FOUND (expected); PASS.
6. Fetch the candidate file from the evidence branch: found; content contains the simulated failed successor marker; PASS.
7. Fetch the baseline time-binding file from the restored test branch: found and matches the baseline version; PASS.
8. Fetch candidate commit metadata after rollback: PASS; commit remains addressable by its SHA and on the evidence branch.

## Conclusion
The bounded Git ref rollback test passed. The prior baseline was restored on the test branch while the simulated failed successor remained retrievable on a separate evidence branch. The failed candidate was not erased and main was not reset or modified by this test operation.

## Strict scope boundary
This proves one isolated repository branch rollback path only. It does not prove rollback of the entire project, restoration of every runtime/database/external destination, cold-start recovery of the production behavior hunter, or host-wide automatic capture. Those remain OPEN / NOT PROVEN and require separate tests.

## Next action
Use this as evidence for the repository-level rollback rule, then design a separate cold-start/retrieval test for the HAIF prototype under Issue #20. Do not repeat this same branch rollback test unless the procedure changes, a regression appears, or new contradictory evidence is found.
