# CURRENT-095 — ادامهٔ 0.0 برای تکمیل پیوستهٔ بستهٔ اولیه

- Stable ID: HAIF-CURRENT-095-INITIAL-ZIP-CONTINUITY-20261027
- Production ID: G6IP-CURRENT-095
- Status: ACTIVE / LIVING / IN PROGRESS / NOT COMPLETE
- Chain: POINT-0/045 → IN-083 → OUT-082 → EVT-0220 → CURRENT-095 → NEXT-051
- Previous verified package checkpoint: [CURRENT-094](./PALANG-0.0-CURRENT-20261027-094-STARTER-ZIP-INPLACE-UPDATE.md)
- Living mother: [سند مرجع مادر مدل اولیه](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Existing starter source: [prototype/haif-gpt6-starter](../../../prototype/haif-gpt6-starter/README.md)
- Independent-host protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL.md](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- Sole active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Verified baseline
- Canonical ZIP: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`
- Internal version: 0.3.1
- Stable package ID: `HAIF-GPT6-PORTABLE-STARTER-20261025-004`
- Size: 19,042 bytes
- SHA-256: `3a17f64880519a0da714f09a1dc8065fafcd88321fa5674eb2d995dfd8f63e83`
- Workflow: [40489753805](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40489753805)
- Tests after fresh extraction: 16/16 PASS; ZIP CRC PASS; 8-file inventory PASS.

## Continuity contract
The initial ZIP is the persistent product line. Future work changes its existing source, preserves stable identity and canonical filename, rebuilds the same archive, checks exact bytes and SHA-256, runs tests, and reads back the artifact. Do not create a parallel version-named ZIP. Keep historical digests immutable.

## Remaining work
- [ ] Verify full package source and workflow always build the canonical ZIP from current source.
- [ ] Test export/import in a truly independent AI host with no inherited chat context.
- [ ] Reconstruct independently from IN and OUT and compare normalized state.
- [ ] Run altered-byte, missing-file and invalid-state negative controls.
- [ ] Capture independent read-back receipts.
- [ ] Restart/cold-start recovery and persistence acceptance.
- [ ] Keep unknown/unsupported host capabilities explicitly OPEN.

CURRENT-095 is not complete until these gates have direct evidence. NEXT-051 remains the only active queue; do not create NEXT-052.
