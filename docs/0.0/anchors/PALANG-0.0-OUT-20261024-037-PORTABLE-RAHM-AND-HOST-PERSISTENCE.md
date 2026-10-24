# OUT-037 — خروجی ثبت معماری بستهٔ انتقال و اثبات میزبان
- Stable ID: G6IP-RAHM-OUT-20261024-037
- Version: 1.0.0
- Input: IN-037
- Parent: CURRENT-044
- Created portable package artifacts under `docs/portable/RAHM/`: boot contract, architecture contract, host capability manifest, interaction-pair JSON Schema, evidence ledger, conformance tests, export manifest, recovery/rollback contract.
- Key architectural addition: persistent memory and durable artifact storage are independent; background execution is a separate capability requiring scheduler/job runner, permission, durable state, logs, stop/revoke control, idle-run evidence and independent read-back.
- Proof boundary: manifest digest fields are initially null; export integrity is not yet validated. Tests are specified but not run. Host persistent memory and idle background execution remain NOT VERIFIED. No runtime was installed by these repository writes.
- Next: compute exact file digests, update manifest, fetch every package file after writes, validate JSON/Schema, register event/current/next and update living mothers/index/queue.


## Read-back reconciliation addendum
- The eight package files were fetched again after creation; file-level Git blob identifiers were obtained.
- EXPORT_MANIFEST v1.0.1 now records those Git blob IDs and explicitly labels SHA-256 byte-level verification as pending. Git blob SHA-1 is not represented as SHA-256.
- Point 0 for the focused host-persistence branch exists; CURRENT-045 and NEXT-043 exist and were fetched after write.
- Integration queue update was fetched after write and its commit metadata confirms the new Point 0 and NEXT-043 links.
- A read-back fetch of `docs/REFERENCE_INDEX.md` returned 404 despite a successful update response. Treat index read-back as FAILED/OPEN; do not claim index reconciliation complete until recovered and fetched again.
- JSON/schema parsing and test execution have not been run. Persistent memory, idle background execution, fresh-context recovery, and second-host compatibility remain NOT VERIFIED / NOT RUN.
