# CURRENT-075 — Portable GPT-6 Execution and Recovery

- Stable ID: HAIF-CURRENT-075-PORTABLE-GPT6-EXECUTION-20261026
- Production ID: HAIF-C075-20261026
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EXECUTION REQUIRED
- Root: [POINT-0/028](./GPT6-RAHM-USER-POINT-0-20261026-028-PORTABLE-GPT6-EXECUTION-AND-RECOVERY.md)
- Input/output: [IN-064](./PALANG-0.0-IN-20261026-064-PORTABLE-GPT6-EXECUTION-AND-RECOVERY.md) / [OUT-063](./PALANG-0.0-OUT-20261026-063-PORTABLE-GPT6-EXECUTION-AND-RECOVERY.md)
- Event: [EVT-0195](../../architecture/BEHAVIOR-TRACE/EVT-0195-PORTABLE-GPT6-EXECUTION-AND-RECOVERY-2026-10-26.md)
- Previous root/checkpoint: [POINT-0/027](./GPT6-RAHM-USER-POINT-0-20261026-027-PATH-B-GAP-RECONCILIATION.md) / [CURRENT-074](./PALANG-0.0-CURRENT-20261026-074-PATH-B-GAP-RECONCILIATION.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Current state
The portable model skeleton and export manifest already exist in docs/portable/RAHM/. However, several startup pointers in RAHM_BOOT.md and FIRST-LIVING-MASTER still refer to older checkpoints, and the manifest describes historical package states. Current-main manifest correctness and exact-current-head conformance are not yet verified in this checkpoint.

## Execution checklist
- [ ] Discover the exact current main SHA and current pointers before any edits.
- [ ] Reconcile RAHM_BOOT, portable master and EXPORT_MANIFEST with POINT-0/028 and CURRENT-075; preserve historical provenance and do not fabricate hashes.
- [ ] Inspect the actual workflow definitions and trigger Portable RAHM Conformance plus Living Architecture Audit using the supported repository workflow path.
- [ ] Confirm both results tested the same exact final main SHA; if any commit advances main, rerun.
- [ ] Retrieve the artifact and independently verify file list, SHA-256 values and archive digest.
- [ ] Create operator-ready import instructions and transfer package from verified artifacts.
- [ ] Test import in a clean separate GPT-6/AI host; capture host capabilities and recovery proof.
- [ ] Continue source-backed identity/parent/time case review under NEXT-051.
- [ ] Keep CURRENT-065/CURRENT-066 OPEN until explicit evidence adjudicates it.
- [ ] Preserve Buffer/Persistent Memory NOT VERIFIED, Dropbox OPEN/NOT VERIFIED, and external host recovery NOT RUN until independent evidence exists.

## Completion boundary
This checkpoint records the intended next execution work. It is not a claim that the model has already been transferred, that the external GPT-6 host has been initialized, or that current-main conformance has passed.
