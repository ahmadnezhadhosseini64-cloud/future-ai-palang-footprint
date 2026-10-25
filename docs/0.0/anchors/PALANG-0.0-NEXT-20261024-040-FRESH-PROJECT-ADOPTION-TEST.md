# NEXT-040 — آزمون پذیرش اصول بنیادین روی پروژهٔ تازه

- Stable ID: `PALANG-NEXT-FRESH-PROJECT-ADOPTION-TEST-2026-10-24-040`
- Production ID: `G6IP-NEXT-040`
- Version: 1.0.3
- Status: OPEN / ACTIVE / LIVING / FIXTURE CREATED; STRUCTURAL CHECKS PASS; CLEAN-HOST TEST NOT RUN
- Parent checkpoint: [CURRENT-042](./PALANG-0.0-CURRENT-20261024-042-NEW-PROJECT-ARCHITECTURE-HARD-AUDIT.md)
- Audit mother: [HA-001](../../reference/REFERENCE-DOCUMENTS/NEW-PROJECT-ARCHITECTURE-HARD-AUDIT-2026-10-24-001.md)
- Governing principles: [NPFAP-20261024-001](../../reference/REFERENCE-DOCUMENTS/NEW-PROJECT-FOUNDATIONAL-ARCHITECTURE-PRINCIPLES-2026-10-24-001.md)
- Existing prototype task preserved: [NEXT-039](./PALANG-0.0-NEXT-20261024-039-BUILD-INTERACTIVE-PROTOTYPE.md)

## Objective

Run a fresh-project adoption test to determine whether the new branch actually instantiates the inherited HAIF/Palang rules rather than merely linking to them.

## Test procedure

1. Create or designate a minimal test project/folder without overwriting any historic files.
2. Confirm the minimum bundle exists: project Point 0, independent 0.0/CURRENT checkpoint, living mother, IN/OUT/event trace, stable/production IDs, version/provenance, UTC-first time ledger, evidence gate, open-gap list, next-action anchor and export/recovery instructions.
3. Confirm Child → Rahm → Master is a gated lifecycle and no unverified hypothesis is promoted.
4. Confirm the two-track behavior model: continuity/recovery/growth and drift/error/evidence control.
5. Check relative links and IDs from the new project back to governing mothers and from IN/OUT to event/current/next.
6. Read back all created files and compare the declared acceptance criteria with actual content.
7. Record PASS / FAIL / INCONCLUSIVE per criterion. Do not infer runtime automation from document presence.
8. Preserve failures and repair only the demonstrated gaps; retest only the changed criteria.

## Acceptance criteria

- All required files exist and cross-link without broken local paths.
- IDs, versions, provenance and status semantics are internally consistent.
- UTC commit time and derived Tehran equivalent are separate from unknown message time.
- Prototype/runtime, cold-start recovery and external destinations remain NOT RUN / NOT VERIFIED unless separately exercised.
- The final test record is linked from CURRENT and the living audit mother.

## Result

PARTIAL PASS — fixture JSON parsed successfully; 32 local Markdown link occurrences across the focused CURRENT-061 chain/prototype/mother/queue set resolved to 15 unique local targets with zero missing destinations. Prototype HTML static contract markers were present. These are repository-structure checks only. Browser execution and actual fresh independent-host adoption remain NOT RUN / NOT VERIFIED.


## CURRENT-061 execution receipt — fixture created
- [x] Created [fresh-project adoption fixture](../../architecture/interactive-prototype/ADOPTION-TEST-FIXTURE.json) with root/checkpoint/architecture-zero/NEXT-039/NEXT-040 lineage and explicit required contract fields.
- [x] Created a browser prototype README that separates repository fixture checks from real-host adoption.
- [ ] Current fixture JSON parse and relative-link/target checks: pending independent verification.
- [ ] Full fresh-project test result per criterion: PARTIAL / NOT YET RUN end-to-end.
- [ ] Clean independent AI-host adoption with no prior chat context: NOT RUN.
- [ ] Cold-start recovery, second-host import, persistence restart and idle/background execution: NOT RUN / NOT VERIFIED.
- Result: fixture preparation is complete; the adoption test itself remains OPEN until current-commit checks and an actual clean-host test have evidence.
