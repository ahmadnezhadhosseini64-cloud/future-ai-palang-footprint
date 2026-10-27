# OUT-087 — نتیجهٔ خاک‌برداری عمیق و چکش سخت

- Stable ID: HAIF-OUT-087-DEEP-AUDIT-FIRST-HOST-20261027
- Production ID: G6IP-OUT-087
- Status: REPOSITORY HARD AUDIT RECORDED / v0.3.4 ARTIFACT VERIFIED / LIVE HOST GAP OPEN
- Parent: [IN-088](./PALANG-0.0-IN-20261027-088-DEEP-AUDIT-FIRST-HOST.md)
- Point: [POINT-0/050 (0+)](./GPT6-RAHM-USER-POINT-0-20261027-050-0PLUS-DEEP-AUDIT-FIRST-HOST.md)
- Current checkpoint: [CURRENT-100](./PALANG-0.0-CURRENT-20261027-100-DEEP-AUDIT-FIRST-HOST.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Living mother: [سند مرجع مادر مدل اولیه](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Recovery protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL.md](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- First-host checklist: [FIRST_HOST_GPT6_ACCEPTANCE_CHECKLIST.md](../../../prototype/haif-gpt6-starter/FIRST_HOST_GPT6_ACCEPTANCE_CHECKLIST.md)

## Verified facts
- Canonical archive filename remains `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`; stable package ID remains `HAIF-GPT6-PORTABLE-STARTER-20261025-004`.
- v0.3.4 inner ZIP: 20,075 bytes, SHA-256 `2ae583a3029d489e636439133b40e24a480754f6b569ada475694abad97c7f3b`; 17/17 tests; CRC/inventory, exact source-byte comparison and artifact round-trip PASS.
- Paired artifact includes ZIP + exact receipt + living mother; mother byte-readback PASS.
- Two-runtime CI transfer passes only for the registered test pattern, not for arbitrary hosts.

## Hard findings
- The package is portable and can be handed to a separate session as files.
- It is not yet a fully autonomous interactive GPT-6 integration. The local engine is not a native plugin; the adapter is a separately deployed service; the GitHub worker requires a separately configured secret and is not called automatically by ChatGPT.
- The conformance workflow had stale hard-coded IN-084 / OUT-083 / CURRENT-096 links despite later current anchors. This weakens the meaning of the earlier recovery-equivalence PASS. The check is being redirected to IN-088 / OUT-087 / CURRENT-100 and explicitly scoped as link/checkpoint equivalence, not host recovery.
- Full readiness is therefore NOT COMPLETE until direct host receipts prove import, independent reconstruction, negative controls, restart, and permitted write-back.

The next package source revision is v0.3.5 in the same package line, with the same canonical archive filename and stable identity. It must be rebuilt and verified by the workflow; do not claim it exists as a verified ZIP until the fresh run succeeds.
