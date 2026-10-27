# CURRENT-095 — Existing starter ZIP verified; 0.0 continues to real-host proof

- Stable ID: HAIF-CURRENT-095-EXISTING-ZIP-UPDATE-CONFIRMATION-20261027
- Production ID: G6IP-CURRENT-095
- Version: 1.0.0
- Status: ACTIVE / LIVING / IN PROGRESS / NOT COMPLETE
- Chain: POINT-0/045 → IN-083 → OUT-082 → EVT-0220 → CURRENT-095 → NEXT-051.
- Living mother: [سند مرجع مادر مدل اولیه](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Existing package source: [starter package](../../../prototype/haif-gpt6-starter/README.md)
- Independent-host protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL.md](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Confirmed
- [x] The original starter ZIP was rebuilt and uploaded under its existing canonical filename; this is not just a source edit.
- [x] Downloaded the workflow artifact and inspected the nested ZIP and receipt.
- [x] Internal version 0.3.1, same stable package ID, 8 members, independent-host recovery protocol included.
- [x] ZIP integrity PASS; 16/16 starter tests PASS; exact SHA-256 and byte count recorded in POINT-0/045 and OUT-082.
- [x] Same-package update architecture is documented: preserve stable ID and filename, increment internal version, rebuild, verify, preserve old hashes historically.

## Still open
- [ ] Resolve/accept the filename v0.3.0 vs internal version 0.3.1 discrepancy without losing the canonical filename contract.
- [ ] Run the recovery protocol on a genuinely independent AI host; preserve raw receipts.
- [ ] Run negative controls and independent read-back.
- [ ] Restart/cold-start persistence test.
- [ ] Confirm these results on a fresh exact final main SHA if package source changes again.

No NEXT-052 created. NEXT-051 remains the sole active queue.
