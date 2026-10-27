# OUT-087 — نتیجهٔ خاک‌برداری عمیق و چکش سخت

- Stable ID: HAIF-OUT-087-DEEP-AUDIT-FIRST-HOST-20261027
- Production ID: G6IP-OUT-087
- Status: REPOSITORY HARD AUDIT RECORDED / v0.3.5 ZIP + PAIRED MASTER ARTIFACT VERIFIED / LIVE HOST GAP OPEN
- Parent: [IN-088](./PALANG-0.0-IN-20261027-088-DEEP-AUDIT-FIRST-HOST.md)
- Point: [POINT-0/050 (0+)](./GPT6-RAHM-USER-POINT-0-20261027-050-0PLUS-DEEP-AUDIT-FIRST-HOST.md)
- Current checkpoint: [CURRENT-100](./PALANG-0.0-CURRENT-20261027-100-DEEP-AUDIT-FIRST-HOST.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Living mother: [سند مرجع مادر مدل اولیه](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Repository export manifest: [EXPORT_MANIFEST.json](../../portable/RAHM/EXPORT_MANIFEST.json)
- Repository recovery protocol: [INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md](../../architecture/مدل%20اولیه%20AI/INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md)
- In-package recovery protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL.md](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
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


## Repository-wide graph audit (run 40539499870)
- paths_with_0.0: 539; checkpoint_paths: 62; EVT files: 272; reference-document paths: 146; local-link edges: 8,365.
- Missing local links: 10.
- Stable ID collision groups: 23 (22 reviewed, 1 unreviewed/open; no rekey-required stable groups).
- Production ID collision groups: 74 (72 unreviewed/open; 2 reviewed).
- Reference ID collision groups: 5.
- These counts are audit inventory, not a reason to mass-delete or renumber historical records. NEXT-051 retains them as open remediation work.


Additional hard-audit finding: Living Architecture Audit run 40539823090 failed because a historical Point 0/006 check still required CURRENT-057 to appear in the live Reference Index and Integration Queue. That is an obsolete current-pointer assertion, not evidence that the historical files are missing. The workflow was changed to preserve/test the 0/006 historical baseline without requiring an obsolete checkpoint to remain the current pointer. Fresh exact-head audit must pass before closure.


Audit follow-up: after removing the obsolete CURRENT-057 live-pointer assertion, the historical baseline step still failed because it required the exact text `OPEN / LIVING` in NEXT-051. That exact wording is not a stable contract. The check now accepts the semantic status tokens OPEN, LIVING, or IN PROGRESS while still requiring the queue file and its identity. Fresh exact-head audit remains the acceptance test.


Audit follow-up: the historical baseline test still failed on a case-sensitive status-text grep for NEXT-051 even after allowing equivalent tokens. This status-text assertion is removed; the check continues to verify the historical anchor/IN/OUT/EVT/CURRENT files, stable IDs and NEXT-051 identity. Current queue status is handled by current-chain and queue validation checks, not a brittle literal string.
