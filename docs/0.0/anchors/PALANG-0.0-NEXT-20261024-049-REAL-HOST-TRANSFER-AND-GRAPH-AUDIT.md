# NEXT-049 — Real Host Transfer, Full Recovery and Graph Audit

- Stable ID: `G6IP-RAHM-NEXT-049-20261024`
- Production ID: `G6IP-NEXT-049`
- Version: 1.0.0
- Status: OPEN / LIVING / NOT COMPLETE.
- Parent: [CURRENT-055](./PALANG-0.0-CURRENT-20261024-055-FIRST-MASTER-READINESS.md)
- First living master: [FIRST-LIVING-MASTER](../../portable/RAHM/FIRST-LIVING-MASTER-PORTABLE-GPT6-HAIF.md)
- Prior test correction: [EVT-0157](../../architecture/BEHAVIOR-TRACE/EVT-0157-TEST-HARNESS-FAILURE-AS-ARCHITECTURE-LEARNING-2026-10-24.md)
- Existing package-build/schema/digest gate: [NEXT-048](./PALANG-0.0-NEXT-20261024-048-FIRST-MASTER-CONFORMANCE.md)

## Ordered actions — do not skip
1. Export the exact package from a named repository commit and preserve its package SHA-256 and artifact receipt.
2. Import the package into a genuinely clean GPT-6/AI host context with no prior chat memory; record host/model/version, available tools, storage, scheduling and limitations.
3. Ask the host to reconstruct mission, architecture rules, current checkpoint, IN/OUT lineage, evidence, failure history, open gates and next action solely from the package. Compare against expected state.
4. Test recovery independently starting from IN and OUT, including all event IDs, parent/child edges, versions, evidence receipts, failures, counterexamples and OPEN items—not only three links.
5. Run a second-host import only when a real second host is available and authorized.
6. Test persistence after runtime restart only in an authorized runtime with a durable storage adapter.
7. Test idle/background execution only where a real scheduler exists and is authorized; otherwise retain NOT VERIFIED/BLOCKED.
8. Audit repository-wide local links, stable/production/reference/event ID collisions, parent ambiguity, UTC/Tehran timestamp pairs and historical branch preservation. Adjudicate each issue with evidence; do not bulk-merge or renumber.
9. Update the canonical living mother, `docs/REFERENCE_INDEX.md`, main integration queue, portable manifest and evidence ledger; fetch/read back every write.
10. Preserve every failure and rerun receipt. Close a gate only when its acceptance criterion and raw evidence are both present.

## Acceptance criteria
- Clean host reproduces the expected architecture state from package alone.
- IN and OUT recovery produce equivalent full canonical state, with all open gates retained.
- Every package digest matches exact bytes.
- Mother, index, queue and manifest are read-back verified.
- Real host capability tests have receipts, or remain explicitly OPEN/BLOCKED.

## Non-closure rule
This NEXT stays OPEN and LIVING while any required criterion is untested or failed. Repository CI success does not imply AI-host import, persistence, background execution or complete graph integrity.
