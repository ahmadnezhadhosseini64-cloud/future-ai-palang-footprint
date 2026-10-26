# CURRENT-085 — 0+ Model Acceleration and Dual-Path Execution

- Stable ID: HAIF-CURRENT-085-0PLUS-MODEL-ACCELERATION-20261026
- Production ID: HAIF-C085
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EXECUTION REQUIRED
- Root / 0+ marker: [POINT-0/036](./GPT6-RAHM-USER-POINT-0-20261026-036-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md)
- Chain: [IN-073](./PALANG-0.0-IN-20261026-073-0PLUS-MODEL-ACCELERATION.md) → [OUT-072](./PALANG-0.0-OUT-20261026-072-0PLUS-MODEL-ACCELERATION.md) → [EVT-0207](../../architecture/BEHAVIOR-TRACE/EVT-0207-POINT-0-036-0PLUS-MODEL-ACCELERATION-2026-10-26.md)
- Previous checkpoint: [CURRENT-084](./PALANG-0.0-CURRENT-20261026-084-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Last verified baseline
Exact-head CI on main SHA `18ccbef16e5bae6e9e31879de8cf575c1c371bec`:
- Living Architecture Audit: PASS; [run 40348805748](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40348805748).
- Portable RAHM Conformance: PASS; [run 40348805726](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40348805726).
- Audit artifact 12661318656, SHA-256 `da4e3ecd4e77f47830baec8c0ede02f9a835a2070db28f30de2069cc1431e41a`.
- Portable package SHA-256 `a2d6cd45d2cafe48bf28c2304d3d1142b5c4a516ccc63e6afabe381e50a73dbd`.
- Local starter engine: 13 tests PASS. Host adapter tests: PASS.
- Graph: 0 missing local links; 2 unresolved parent edges; 0 ambiguous parent edges. Identity groups still open: 1 Stable-ID, 66 Production-ID, 5 Reference-ID, 3 event-number groups unreviewed; 11 exact-content duplicate groups remain classified, not auto-deleted.
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
