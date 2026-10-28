# IN-094 — User input: no version increment; update the same canonical ZIP in place

- Stable ID: HAIF-IN-094-POINT-056-INPLACE-VERSION-GOVERNANCE-20261028
- Parent: [POINT-0/056 (0+)](./GPT6-RAHM-USER-POINT-0-20261028-056-0PLUS-INPLACE-UPDATE-VERSION-GOVERNANCE.md)
- Prior highlight retained: [POINT-0/055](./GPT6-RAHM-USER-POINT-0-20261028-055-0PLUS-ARCHITECTURE-ZIP-MASTER-HARD-AUDIT.md)
- Output: [OUT-093](./PALANG-0.0-OUT-20261028-093-POINT-056-INPLACE-VERSION-GOVERNANCE.md)
- Event: [EVT-0231](../../architecture/BEHAVIOR-TRACE/EVT-0231-POINT-056-INPLACE-VERSION-GOVERNANCE-2026-10-28.md)
- Current: [CURRENT-106](./PALANG-0.0-CURRENT-20261028-106-INPLACE-VERSION-GOVERNANCE.md)
- Sole active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Living master: [سند مرجع مادر مدل اولیه هوش مصنوعی](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Independent-host proof protocol: [INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001](../../architecture/مدل%20اولیه%20AI/INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md)
- Package recovery protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL.md](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- Package manifest: [manifest.json](../../../prototype/haif-gpt6-starter/manifest.json)

## Captured requirement
The user explicitly reaffirmed: do not create a new version number; update the existing version and rebuild the same canonical ZIP. Version remains 0.3.8. Stable package ID and canonical filename must not change. Prior artifact digest is historical only.

## Required execution
1. Keep manifest version and current_internal_version at 0.3.8.
2. Keep supersedes at 0.3.7 (the previous distinct version), not 0.3.8.
3. Align package docs and tests to the current graph.
4. Trigger/inspect exact-head conformance workflow and verify downloaded ZIP bytes, digest, inventory and extracted tests.
5. Leave external host acceptance gates OPEN until direct host receipts exist.

## Registration anchor and status
- Commit UTC: 2026-10-28T04:43:22Z (`c49448bc2b57feb980ee93e082d9090c33440362`); Tehran equivalent 2026-10-28T08:13:22+03:30.
- Status: REGISTERED / READ-BACK VERIFIED. All gates not directly proven remain OPEN.
