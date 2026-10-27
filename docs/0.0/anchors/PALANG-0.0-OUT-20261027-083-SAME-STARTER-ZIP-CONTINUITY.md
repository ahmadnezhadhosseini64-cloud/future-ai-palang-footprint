# OUT-083 — Continuous same-package update contract

- Stable ID: HAIF-OUT-083-SAME-STARTER-ZIP-CONTINUITY-20261027
- Production ID: G6IP-OUT-083
- Version: 1.0.0
- Status: IMPLEMENTATION COMMITTED / EXACT-HEAD BUILD PENDING
- Parent: [IN-084](./PALANG-0.0-IN-20261027-084-SAME-STARTER-ZIP-CONTINUITY.md)
- Root: [POINT-0/046](./GPT6-RAHM-USER-POINT-0-20261027-046-SAME-STARTER-ZIP-CONTINUITY.md)
- Living mother: [سند مرجع مادر مدل اولیه](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Package source: [prototype/haif-gpt6-starter](../../../prototype/haif-gpt6-starter/README.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Continuous update contract
1. Preserve Stable ID `HAIF-GPT6-PORTABLE-STARTER-20261025-004`.
2. Preserve canonical archive name `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip` for compatibility; internal manifest version states the actual package version.
3. Make every functional change in the existing `prototype/haif-gpt6-starter/` source tree.
4. Rebuild the same named archive through the existing CI workflow; never treat a source edit as a ZIP update.
5. Verify exact artifact SHA-256, byte count, inventory, ZIP CRC, extracted tests and receipt.
6. Preserve old digests as historical; never reuse an old digest for new bytes.
7. Treat actual independent-host import, IN/OUT reconstruction, negative controls, read-back and restart persistence as separate gates.

The prior ZIP is confirmed updated. This continuation adds current lineage references and ensures the conformance workflow checks the current IN/OUT pair. Fresh CI evidence for this new exact main SHA remains pending.

- Current checkpoint: [CURRENT-096](./PALANG-0.0-CURRENT-20261027-096-SAME-STARTER-ZIP-CONTINUITY.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Living mother: [سند مرجع مادر مدل اولیه](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Recovery protocol: [INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL](../../architecture/مدل%20اولیه%20AI/INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md)
- Package recovery protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL.md](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- Export manifest: [EXPORT_MANIFEST.json](../../portable/RAHM/EXPORT_MANIFEST.json)

Open gates: real independent AI-host import, independent reconstruction from IN and OUT, negative controls, independent read-back, and restart/persistence are OPEN / NOT VERIFIED. CI link-equivalence and ZIP build do not close these gates.


## Exact verified v0.3.2 archive receipt — run 40507481687
- Tested source SHA: `c6af49386493f5c542336d54511f66085c1b7906`; paired Living Architecture Audit and Portable RAHM Conformance both PASS on that same SHA.
- Workflow: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40507481687
- Artifact ID: `12735876293`; outer artifact wrapper 19,842 bytes, SHA-256 `39e11184ca4c3cb4a3255c8a2678af7b9d8057afe447b08d6dcd7a7d36df7722`.
- Downloaded and inspected nested canonical ZIP: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`, 19,242 bytes, SHA-256 `861be3d9998e96c8588d03642f70d01a6e2060b7b5056f45ef50008fc6f61da4`; ZIP CRC PASS; 8-file inventory; internal version 0.3.2; stable package ID unchanged.
- Starter tests succeeded in CI (16 tests); real independent-host acceptance remains NOT RUN.
- The tested SHA is the source revision for this receipt; later evidence-ledger commits do not alter the ZIP bytes. Do not claim the external host gate passed.
