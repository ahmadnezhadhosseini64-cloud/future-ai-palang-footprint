# EVT-0142 — چکش سخت و راستی‌آزمایی معماری پروژهٔ جدید

- Stable ID: `PALANG-EVT-NEW-PROJECT-ARCHITECTURE-HARD-AUDIT-2026-10-24-0142`
- Production ID: `G6IP-EVT-0142`
- Interaction: `INT-20261024-034`
- Input: [IN-034](../../0.0/anchors/PALANG-0.0-IN-20261024-034-HARD-AUDIT-NEW-PROJECT-ARCHITECTURE.md)
- Output: [OUT-034](../../0.0/anchors/PALANG-0.0-OUT-20261024-034-HARD-AUDIT-NEW-PROJECT-ARCHITECTURE.md)
- Audit report: [HA-001](../../reference/REFERENCE-DOCUMENTS/NEW-PROJECT-ARCHITECTURE-HARD-AUDIT-2026-10-24-001.md)
- Previous checkpoint: [CURRENT-041](../../0.0/anchors/PALANG-0.0-CURRENT-20261024-041-FOUNDATIONAL-ARCHITECTURE-MOTHER-ACTIVATION.md)
- New checkpoint: [CURRENT-042](../../0.0/anchors/PALANG-0.0-CURRENT-20261024-042-NEW-PROJECT-ARCHITECTURE-HARD-AUDIT.md)
- Status: REGISTERED / READ-BACK PENDING.

## Observed findings

1. New-project baseline contains inherited principles and gates, including evidence-first status, UTC-first timestamps, destination-specific verification, Child → Rahm → Master, error learning and no-redundant-retest.
2. Actual file headers disagree with recent claimed version updates: foundational mother header remains v1.0.0, inherited mother v1.0.4, GPT-6 living master v1.3.5. These are version/ledger drift, not assumed content loss.
3. Reference Index still describes NPFAP as exact read-back pending even though the exact file has been fetched after writes and its expected CURRENT-041/IN-033/OUT-033/EVT-0141 links are present.
4. Active masters and architecture-zero text still contain CURRENT-040 as the latest current anchor. CURRENT-041 is the newer registered node; CURRENT-042 becomes the latest audit continuation.
5. CURRENT-041 still lists registry/master linking as the next action, although those links are now present. The checkpoint needs a truthful handoff to this audit's follow-up.
6. The first interactive prototype is NOT BUILT; fresh-session/cold-start recovery is NOT RUN. These remain OPEN and must not be marked PASS based on documents.
7. Buffer, Persistent Memory, Library and Dropbox are not verified by GitHub evidence. Global always-on capture is not established.
8. The no-redundant-retest rule is binding; unrelated closed tests must not be rerun without a valid trigger.

## Corrective rule

Correct only the verifiable metadata and links; keep historical content as history where needed. A historical CURRENT-040 file may describe its own time, but the active master and index must point to the latest checkpoint. A test already closed with evidence must not be repeated absent a material change, new requirement, failure/regression, or contradictory evidence.

## Next gates

- Read back all changed files and match IDs/versions/links.
- Run fresh-project adoption test against a real minimal project.
- Build and exercise a small interactive prototype, then record evidence.
- Run cold-start recovery only after a real recoverable artifact exists.
- Keep external destinations separately NOT VERIFIED.
