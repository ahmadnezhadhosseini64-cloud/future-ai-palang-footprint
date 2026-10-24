# RECOVERY_AND_ROLLBACK — HAIF Rahm
Version 1.0.0
1. Start with EXPORT_MANIFEST; list present and missing files.
2. Verify package ID/version/dependencies/digests. Missing digests mean integrity INCOMPLETE.
3. Load boot, architecture, host capabilities, schema, ledger and tests. Do not rely on hidden chat memory.
4. Reconstruct checkpoint, lineage, next action, open failures and proof boundaries.
5. Record recovery as a new event/checkpoint; never overwrite the source checkpoint.
6. For partial import, continue only with verified files and preserve gaps.
7. On conflict, preserve both records, mark CONFLICTING and route to Master review.
8. Rollback selects a prior version by explicit ID/commit; never delete newer versions or failure evidence.
9. Independently reopen files and compare with manifest; import without read-back is not verified recovery.
10. If host cannot persist state, return updated package to the human for explicit export; do not imply it will exist in a later session.
11. If host cannot run idle jobs, declare background automation UNSUPPORTED and use a manually triggered checkpoint workflow.