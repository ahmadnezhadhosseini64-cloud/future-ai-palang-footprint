# POINT-0/029 — Reversible Gap Covers and Fast Host Transfer

- Stable ID: `HAIF-USER-POINT-0-029-REVERSIBLE-GAP-COVERS-20261026`
- Production ID: `HAIF-P0-029`
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / REVERSIBLE-COVERS-APPLIED
- Project: Future AI / Palang Footprint
- Parent: POINT-0/028 + POINT-0+ (highlight overlay; neither is replaced)
- Prior checkpoint: CURRENT-076
- Active queue: NEXT-051 (existing queue only; do not create NEXT-052)
- Event: EVT-0199
- Input/output pair: IN-065 → OUT-064
- New checkpoint: CURRENT-077
- Canonical repository: `ahmadnezhadhosseini64-cloud/future-ai-palang-footprint`, branch `main`

## User intent

Create a new POINT-0 for this turn. Audit architecture gaps, apply a reversible containment/cover where doing so does not damage architecture, but keep each gap OPEN and ACTIVE. Prioritize a quick, truthful transfer to a new AI host.

## Core decision

A **cover is not closure**. A cover may make a gap safer to carry and easier to resume, but cannot turn OPEN / NOT RUN / NOT VERIFIED into CLOSED, PASS, VALIDATED, or INTEGRATED. Each cover must retain the original gap ID, evidence, owner/condition, next action, and removal/review condition. Do not delete, merge, renumber, or overwrite historic evidence.

## Reversible covers applied in architecture

1. **Clean-host transfer gap — COVERED, OPEN:** a portable boot sequence and minimum transfer checklist are specified. Actual import by an independent new host remains NOT RUN until a real host produces a receipt.
2. **Manifest/package drift — COVERED, OPEN:** the manifest is treated as a generated artifact; do not hand-invent SHA-256 or Git blob hashes. Regenerate through the repository workflow, then read back exact bytes and compare the receipt.
3. **CURRENT-065/CURRENT-066 pointer conflict — COVERED, OPEN:** preserve both branches and evidence; use the latest source-backed root only for navigation, not as an inferred winner of the historic conflict.
4. **EVT-0195 duplicate/collision — COVERED, OPEN:** preserve both same-number artifacts and EVT-0179 collision history. No speculative merge or renumbering.
5. **Repository graph identity/parent/time collisions — COVERED, OPEN:** adjudicate one finding at a time under NEXT-051; no bulk deletion or guessed parent/time.
6. **Buffer/Persistent Memory/Dropbox — COVERED, OPEN:** these are separate destinations and are not implied by repository success. Dropbox stays on its existing branch; do not divert the current transfer task into Dropbox.
7. **Runtime/automatic capture/background execution — COVERED, OPEN:** local source and CI are not proof of host-level runtime, durable memory, automatic capture, or idle execution.
8. **Visible progress — COVERED, ACTIVE:** at each durable milestone, state what was actually written/read back, what was tested, what remains open, and the exact resume point; do not imply hidden background work between turns.

## Fast transfer path

1. Use the canonical repository and export manifest as source of truth; fetch the actual current branch head first.
2. Provide the new host with the RAHM boot contract, living master, export manifest, schema, conformance tests, recovery/rollback guide, and current POINT-0/CURRENT/NEXT chain. Use the repository's actual current files, not stale links embedded in old text.
3. Ask the new host to enumerate supplied files, report its actual model/runtime/capabilities (UNKNOWN when not observable), verify manifest digests, reconstruct mission and open gates, and return a structured import receipt.
4. Verify its returned receipt against the repository. Record independent host/model/version, input package digest, import result, recovered IDs, missing files, capability limits, and a cold-start/restart result. If no real host is available, leave this gate NOT RUN.
5. After any source changes, regenerate package evidence and verify against the exact final SHA; never reuse a successful receipt from a parent commit as proof for a newer HEAD.

## Acceptance boundaries

- Repository anchor files: verify by independent read-back.
- CI: only the tests and SHA named by their run receipts may be called passed.
- Independent host import: OPEN / NOT RUN until direct evidence.
- Persistent memory after restart and idle/background execution: OPEN / NOT VERIFIED.
- Buffer, Library and Dropbox: independently unverified unless their own receipts exist.
- Architecture-wide graph: REVIEW REQUIRED until NEXT-051 findings are adjudicated.

## Resume instruction

Start from CURRENT-077, read POINT-0/029, OUT-064, EVT-0199, the living master, RAHM_BOOT, EXPORT_MANIFEST and NEXT-051. Continue the **fast clean-host transfer path** first; do not start Dropbox. Preserve all OPEN gates and add evidence incrementally.

## Time and evidence

UTC is canonical; Asia/Tehran is derived from the same instant (+03:30). For repository registration time, use the actual commit timestamp of the file's final content from Git metadata. Event/user-message time is separate contextual evidence. Do not guess missing seconds, hashes, or host receipts.
