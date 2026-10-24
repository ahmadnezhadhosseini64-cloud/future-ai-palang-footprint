# CURRENT-044 — پایهٔ معماری بازیابی‌پذیر و تکامل‌پذیر

- Stable ID: `PALANG-CURRENT-RECOVERY-EVOLVABLE-BASELINE-2026-10-24-044`
- Production ID: `G6IP-CURRENT-044`
- Version: 1.0.0
- Role: Independent 0.0 checkpoint and resumable recovery anchor
- Status: REGISTERED / READ-BACK VERIFIED / IDENTIFIERS MATCHED / ACTIVE / LIVING / EVOLVABLE.
- Parent: [CURRENT-043](./PALANG-0.0-CURRENT-20261024-043-FOUNDATIONAL-PRINCIPLES-COMPLETENESS.md) — preserved, not replaced.
- Input: [IN-036](./PALANG-0.0-IN-20261024-036-RECOVERY-EVOLVABLE-BASELINE.md)
- Output: [OUT-036](./PALANG-0.0-OUT-20261024-036-RECOVERY-EVOLVABLE-BASELINE.md)
- Event: [EVT-0144](../../architecture/BEHAVIOR-TRACE/EVT-0144-RECOVERY-EVOLVABLE-BASELINE-2026-10-24.md)
- Foundational mother: [NPFAP-20261024-001](../../reference/REFERENCE-DOCUMENTS/NEW-PROJECT-FOUNDATIONAL-ARCHITECTURE-PRINCIPLES-2026-10-24-001.md)
- Previous verification task: [NEXT-041](./PALANG-0.0-NEXT-20261024-041-FOUNDATIONAL-PRINCIPLES-VERIFICATION.md)
- Next action: [NEXT-042 — close gaps with evidence and test recovery](./PALANG-0.0-NEXT-20261024-042-GAP-CLOSURE-AND-RECOVERY-VALIDATION.md)

## Resumable state

The new point captures the user's requirement to establish a reliable architecture baseline, keep the mother document living, close verifiable gaps, and preserve all prior versions as linked history. This point is additive: CURRENT-043, CURRENT-042, CURRENT-041 and older anchors are not deleted or silently rewritten.

## Version lineage contract

For every successor version:
1. Preserve predecessor file/content and Stable ID.
2. Create a new version or successor record with a unique ID and explicit parent/successor links.
3. Record change rationale, source/provenance, acceptance criteria, tests, evidence, observed outcome and remaining gaps.
4. Write → fetch exact file → match identifiers and expected content → validate links and criteria → reconcile index/registry → assign status.
5. Keep rollback/recovery instructions and never label a design recoverable as recovery-tested until a cold-start test passes.
6. Advance a mutable current pointer only after the successor's repository read-back and required checks pass.
7. Keep external destinations independent; repository success is not Library/Buffer/Persistent Memory/Dropbox success.

## Gap register

- G-01: principle-by-principle audit of all 16 foundational principles — OPEN; NEXT-041.
- G-02: full transitive local-link scan for changed files / repository graph — OPEN; NEXT-042.
- G-03: fresh-project adoption test — OPEN / NOT RUN; NEXT-040.
- G-04: interactive prototype — NOT BUILT; NEXT-039.
- G-05: cold-start recovery from an exported/reloaded package — OPEN / NOT RUN; NEXT-042.
- G-06: external destination reconciliation — NOT VERIFIED; separate destination-specific evidence required.
- G-07: automatic background capture — NOT ESTABLISHED; do not imply it runs without an actual trigger and execution proof.
- G-08: latest NPFAP commit-time receipt needs reconciliation after its most recent revision — OPEN until actual commit metadata is fetched and UTC/Tehran values are corrected.

## Exit criteria

No gap closes because a document says it is closed. Each closes only with a repeatable check, observed result, evidence pointer, timestamp provenance and read-back. If a check cannot run, record BLOCKED / NOT RUN and the exact prerequisite.

## Timestamp rule

Repository registration time is the actual last-change Git commit timestamp in UTC; display Tehran as the equivalent of that same instant (+03:30). Do not substitute message time or guess missing timestamps. Record commit SHA and derive both values from the same commit metadata.

## Current verification boundary

At creation time, CURRENT-043 was previously read back and its commit timestamp verified. NPFAP v1.0.3 had 19/19 direct internal Markdown targets found. Neither fact proves this new point is read-back verified, the whole project link graph is clean, or the architecture passes adoption/recovery. Exact read-back of CURRENT-044 and the linked IN-036 / OUT-036 / EVT-0144 / NEXT-042 records succeeded; IDs and primary links matched. The detailed checks remain assigned to NEXT-042.