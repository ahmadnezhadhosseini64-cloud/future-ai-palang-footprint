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
