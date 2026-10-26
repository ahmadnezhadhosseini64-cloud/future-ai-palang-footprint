# QUICK-TRANSFER-CHECKLIST — Clean AI Host Import

- Stable ID: `HAIF-RAHM-QUICK-TRANSFER-20261026-001`
- Production ID: `HAIF-QTC-001`
- Version: 1.0.0
- Status: ACTIVE / LIVING / READY TO EXECUTE / HOST IMPORT NOT RUN
- Current anchor: [POINT-0/029](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-029-REVERSIBLE-GAP-COVERS-AND-FAST-HOST-TRANSFER.md)
- Current checkpoint: [CURRENT-077](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-077-REVERSIBLE-GAP-COVERS.md)
- Existing active queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Boot contract: [RAHM_BOOT](./RAHM_BOOT.md)
- Master: [FIRST-LIVING-MASTER](./FIRST-LIVING-MASTER-PORTABLE-GPT6-HAIF.md)
- Manifest: [EXPORT_MANIFEST](./EXPORT_MANIFEST.json)
- Schema: [INTERACTION_PAIR_SCHEMA](./INTERACTION_PAIR_SCHEMA.json)
- Conformance: [CONFORMANCE_TESTS](./CONFORMANCE_TESTS.md)
- Recovery: [RECOVERY_AND_ROLLBACK](./RECOVERY_AND_ROLLBACK.md)

## Before transfer — source side

- [ ] Fetch latest main HEAD and record full SHA.
- [ ] Read back the boot contract, living master, manifest, schema, conformance tests, recovery guide, CURRENT-077, POINT-0/029 and NEXT-051.
- [ ] Run the portable conformance workflow on the exact final SHA.
- [ ] Confirm every manifest entry's exact-byte digest and the produced package archive digest from workflow receipts.
- [ ] If Evidence Gate adds a new commit, repeat verification on the new HEAD; never reuse parent-SHA receipts.
- [ ] Export only the package corresponding to the verified final SHA.

## Import — destination host

Give the host the package and this instruction:

> You are initializing the Future AI / Palang Footprint RAHM portable architecture. Do not assume prior chat history, hidden memory, tools, internet access, persistent storage, or background execution. First enumerate every file actually received and report model/runtime identity only if observable. Validate manifest and file digests. Reconstruct project goal, architecture lifecycle, latest POINT-0/CURRENT, IN/OUT pair, EVT, NEXT-051, all unresolved gates, and the deterministic next action using only the supplied package. Preserve conflicts and all OPEN gates. Return a structured import receipt containing package ID/version, source SHA/digest, files received/missing, recovered identifiers, validation results, capability manifest, limitations, and a restart/cold-start result. Never mark a gate closed without direct evidence.

## Required destination receipt

- Destination host/model/version (or UNKNOWN).
- Import date/time in UTC; timezone conversion only from the same instant.
- Package ID/version and exact SHA-256 digest.
- File list received and missing.
- Manifest validation result and any digest mismatch.
- Recovered root, checkpoint, IN/OUT, EVT, active queue, and open-gate list.
- Whether a new-session/cold-start recovery was actually tested.
- Whether durable memory after restart was actually tested.
- Whether automatic capture and idle/background execution were actually tested.
- Errors, deviations, and rollback method.
- A copy of the receipt returned to the canonical repository for independent comparison.

## Acceptance boundary

A host's narrative that it “understands” the project is not proof. Accept only a structured receipt whose recovered IDs, open gates, and next action match the package and canonical repository. Clean-host import remains OPEN / NOT RUN until this receipt exists. A CI runner is not a separate AI host.

## Reversible covers

This checklist covers the route, not the unresolved gaps. Do not remove covers or close gates for CURRENT-065/CURRENT-066, EVT-0195, graph reconciliation, Issues #20/#21, Buffer/Library/Persistent Memory/Dropbox, or runtime/background execution without their own evidence.
