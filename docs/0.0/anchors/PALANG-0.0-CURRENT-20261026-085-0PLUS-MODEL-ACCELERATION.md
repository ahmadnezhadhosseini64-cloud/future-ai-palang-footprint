# CURRENT-085 — 0+ Model Acceleration and Dual-Path Execution

- Stable ID: HAIF-CURRENT-085-0PLUS-MODEL-ACCELERATION-20261026
- Production ID: HAIF-C085
- Version: 1.0.2
- Status: ACTIVE / LIVING / OPEN / EXECUTION REQUIRED
- Root / 0+ marker: [POINT-0/036](./GPT6-RAHM-USER-POINT-0-20261026-036-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md)
- Chain: [IN-073](./PALANG-0.0-IN-20261026-073-0PLUS-MODEL-ACCELERATION.md) → [OUT-072](./PALANG-0.0-OUT-20261026-072-0PLUS-MODEL-ACCELERATION.md) → [EVT-0207](../../architecture/BEHAVIOR-TRACE/EVT-0207-POINT-0-036-0PLUS-MODEL-ACCELERATION-2026-10-26.md)
- Previous checkpoint: [CURRENT-084](./PALANG-0.0-CURRENT-20261026-084-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Last verified baseline
Exact-head CI receipts after 0+ registration and reversible parent-gap cover:
- Living Architecture Audit: PASS on main SHA `127cfd03095a881ae2aa9a625e0fe923644e9795`; [run 40355174264](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40355174264). Audit artifact 12665756382, SHA-256 `e866aa261fb199e3bfa7e0aaa6c4f591d5ff955aaa59a54b2de3c4b702fffafd`.
- Portable RAHM Conformance: PASS on the same SHA `127cfd03095a881ae2aa9a625e0fe923644e9795`; [run 40355174175](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40355174175). Package artifact 12666090367, artifact archive digest `sha256:f7e6ba056a1a174b995d472e621bc317b5ba5b06c3cf8ed8f238e83754939976`; package content SHA-256 `a96485ead239e3fa6150fc6e76b7382dd5b1cd54b98c2a16f6c448a42c445826`.
- Conformance scanned 50 manifest files: 50/50 exact-byte matches; 127 live-reference files checked; schema conformance and IN/OUT recovery equivalence PASS.
- Current-pointer discovery: `SCOPED_CONSISTENT`; global registries now declare CURRENT-085 while the bounded overlay remains CURRENT-066. No winner was guessed by numeric order.
- Local starter engine: 13 tests PASS. Host adapter tests: PASS.
- Graph audit on SHA `127cfd03095a881ae2aa9a625e0fe923644e9795`: 5,008 files including generated evidence; 1,332 source text files; 7,680 local-link edges; 0 missing local links; 2 unresolved parent edges; 0 ambiguous parent edges. Identity groups still open: 1 Stable-ID, 66 Production-ID, 5 Reference-ID, 3 event-number groups unreviewed; 11 exact-content duplicate groups remain classified, not auto-deleted.
- The two unresolved edges both point to the missing standalone historical parent `HAIF-CORE-MASTER-CHILD-RAHM-2026-09-15-001`. A reversible gap cover is now registered: [Recovery Bridge](../../reference/REFERENCE-DOCUMENTS/HAIF-CORE-MASTER-CHILD-RAHM-RECOVERY-BRIDGE-2026-10-26-001.md). It is not the original parent; both edges remain UNRESOLVED.
- Timestamp normalization at that SHA: 2,889 timestamp strings normalized and paired UTC/Tehran; 0 parse ambiguity; the repository-time normalization audit passed. Two legacy files still show missing/unknown exact-time labels.
- Pointer scope: SCOPED_CONSISTENT. Historical overlay CURRENT-066 and global project pointer CURRENT-073 are intentionally distinct scopes.

## Architecture invariant: MASTER → RAHM → validation → CHILD
- MASTER: immutable governing architecture, provenance, policies, schemas, stable references and accepted lessons; new versions append, not overwrite the historical source.
- RAHM: portable transfer and continuity layer. Captures IN/OUT/event anchors, hash-chained ledger, checkpoints, evidence, schema validation, package export/import and recovery. Rejects tampering, duplicate IDs, self-parenting and unsupported promotion.
- CHILD: candidate executable instance or project/model grown from a validated RAHM package. It receives the governing contract and evidence, runs bootstrap/self-tests, and remains CANDIDATE until its own host returns import, read-back, restart and round-trip receipts.
- Validation gate: only evidence-backed, reversible changes may enter the accepted state. Unresolved historical edges and collisions remain explicit gaps.

## Path A — portable executable model
1. Preserve the starter engine and its 13 passing tests.
2. Verify the exact package manifest, byte digests and read-back on the latest main SHA.
3. Prepare a single clean-host bootstrap procedure that exports the package, imports it into a new host, reads back the ledger, restarts the host and exports/imports a second round-trip.
4. Do not call external-host transfer complete until a host-generated receipt identifies the host, package digest, import result, read-back, restart and round-trip.

## Path B — historical graph remediation
1. Inspect the exact two unresolved parent edges from the current audit artifact. Select only source-proven targets; otherwise retain OPEN.
2. Adjudicate remaining identity groups in small batches using full declared identifiers, source path, content hash and provenance.
3. Keep body references distinct from metadata declarations; never merge by short event number or choose by numeric order.
4. Keep exact-content duplicates as provenance-bearing candidates until role is adjudicated.
5. Rerun audit and portable conformance on the same final SHA and read back both artifacts.

## Completion gate
No gap closes without source evidence, a corresponding correction where required, passing tests on the corrected SHA and read-back. NEXT-051 remains the sole active queue; no parallel NEXT file is created.
