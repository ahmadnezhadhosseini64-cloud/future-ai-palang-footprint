# CURRENT-085 — 0+ Model Acceleration and Dual-Path Execution

- Stable ID: HAIF-CURRENT-085-0PLUS-MODEL-ACCELERATION-20261026
- Production ID: HAIF-C085
- Version: 1.0.1
- Status: ACTIVE / LIVING / OPEN / EXECUTION REQUIRED
- Root / 0+ marker: [POINT-0/036](./GPT6-RAHM-USER-POINT-0-20261026-036-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md)
- Chain: [IN-073](./PALANG-0.0-IN-20261026-073-0PLUS-MODEL-ACCELERATION.md) → [OUT-072](./PALANG-0.0-OUT-20261026-072-0PLUS-MODEL-ACCELERATION.md) → [EVT-0207](../../architecture/BEHAVIOR-TRACE/EVT-0207-POINT-0-036-0PLUS-MODEL-ACCELERATION-2026-10-26.md)
- Previous checkpoint: [CURRENT-084](./PALANG-0.0-CURRENT-20261026-084-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Last verified baseline
Exact-head CI receipts after 0+ registration and reversible parent-gap cover:
- Living Architecture Audit: PASS on main SHA `159c9fc4f4e6b1699bccc5f0d351a80fb172c08b`; [run 40354029943](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40354029943). Audit artifact 12665002634, SHA-256 `22b68969bfd4ea0e934557e4a7d3d9947b86022443bb0cfe7a9e2c81c0829929`.
- Portable RAHM Conformance: PASS on SHA `c68569a35d7e89e426732131615361a93afd3e77`; [run 40353992571](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40353992571). Package artifact 12665581346, archive digest `sha256:45200f30b4bd49d796a63a91c4249aa66938f1e7057d618a0c5d439ca3e6b152`; package content SHA-256 `be493445e9fe7493c36b1cd0a2f6e4909b7f4c2157e749f7b595570f073f4a6b`.
- Local starter engine: 13 tests PASS. Host adapter tests: PASS.
- Graph audit on SHA `159c9fc4f4e6b1699bccc5f0d351a80fb172c08b`: 5,004 files including generated evidence; 1,332 source text files; 7,679 local-link edges; 0 missing local links; 2 unresolved parent edges; 0 ambiguous parent edges. Identity groups still open: 1 Stable-ID, 66 Production-ID, 5 Reference-ID, 3 event-number groups unreviewed; 11 exact-content duplicate groups remain classified, not auto-deleted.
- The two unresolved edges both point to the missing standalone historical parent `HAIF-CORE-MASTER-CHILD-RAHM-2026-09-15-001`. A reversible gap cover is now registered: [Recovery Bridge](../../reference/REFERENCE-DOCUMENTS/HAIF-CORE-MASTER-CHILD-RAHM-RECOVERY-BRIDGE-2026-10-26-001.md). It is not the original parent; both edges remain UNRESOLVED.
- Timestamp normalization at that SHA: 4,811 files; 2,880 timestamp strings normalized and paired; 0 parse/offset/UTC-label failures. Two legacy files still show missing/unknown exact-time labels.
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
