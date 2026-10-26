# CURRENT-077 — Reversible Gap Covers and Fast Host Transfer

- Stable ID: `HAIF-CURRENT-077-REVERSIBLE-GAP-COVERS-20261026`
- Production ID: `HAIF-C077`
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EXECUTION REQUIRED
- User root: [POINT-0/029](./GPT6-RAHM-USER-POINT-0-20261026-029-REVERSIBLE-GAP-COVERS-AND-FAST-HOST-TRANSFER.md)
- Input/output: [IN-065](./PALANG-0.0-IN-20261026-065-REVERSIBLE-GAP-COVERS-AND-FAST-HOST-TRANSFER.md) → [OUT-064](./PALANG-0.0-OUT-20261026-064-REVERSIBLE-GAP-COVERS-AND-FAST-HOST-TRANSFER.md)
- Event: [EVT-0199](../../architecture/BEHAVIOR-TRACE/EVT-0199-REVERSIBLE-GAP-COVERS-AND-FAST-HOST-TRANSFER-2026-10-26.md)
- Previous checkpoint: [CURRENT-076](./PALANG-0.0-CURRENT-20261026-076-POINT-0-PLUS-ARCHITECTURE-CLOSURE.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Portable startup: [RAHM_BOOT](../../portable/RAHM/RAHM_BOOT.md)
- Transfer checklist: [QUICK-TRANSFER-CHECKLIST](../../portable/RAHM/QUICK-TRANSFER-CHECKLIST.md)

## State

The reversible-cover policy is registered. Gaps are contained for safe transfer but remain OPEN; this checkpoint does not close them.

## Next execution order

1. Fetch this checkpoint and all referenced files from the current main HEAD; check relative links.
2. Read back the latest main head, package manifest, boot contract, living master and NEXT-051. Use actual current files rather than stale pointers copied from old artifacts.
3. Regenerate package hashes using the repository workflow; do not hand-edit generated hashes.
4. Run portable conformance and living architecture audit on the exact same final SHA. If a workflow creates a follow-up evidence commit, repeat on the new HEAD.
5. Prepare the export package from that verified SHA.
6. Import into a real clean destination AI host and capture a structured receipt; if unavailable, mark NOT RUN.
7. Reconstruct POINT-0, CURRENT, IN/OUT, EVT, NEXT and all open gaps from package contents alone; compare with repository truth.
8. Keep CURRENT-065/CURRENT-066, EVT-0195 collision, graph identity/parent/time findings, Issues #20/#21, Buffer/Persistent Memory/Library/Dropbox and runtime/background claims open until each has its own evidence.

## Non-destructive cover rule

A cover is a removable overlay. Keep source records unchanged; retain each gap's original identity and evidence. Remove the cover only after documented acceptance and independent read-back. Never use a cover to label a gap CLOSED or PASS.

## Time/evidence

Repository registration time must be read from the actual commit timestamp of this file's final content in Git metadata; UTC is canonical and Tehran is derived (+03:30). Event time is contextual. Exact-head tests and independent host import are NOT VERIFIED until direct receipts exist.
