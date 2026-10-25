# EVT-0190 — v0.3.0 One-Command 0+ Bootstrap and Clean Transfer Package

- Stable ID: HAIF-EVT-0190-0PLUS-BOOTSTRAP-CLEAN-PACKAGE-20261025
- Production ID: HAIF-EVT-0190-20261025
- Version: 1.0.0
- Status: PASS / EXACT-HEAD CI PASS / CLEAN PACKAGE FRESH-EXTRACT PASS / BOOTSTRAP AND COLD-START PASS
- Root: [POINT-0/024 (0+)](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261025-024-0PLUS-PRODUCTION-MARKER.md)
- Current continuation: [CURRENT-071](../../0.0/anchors/PALANG-0.0-CURRENT-20261025-071-0PLUS-ENGINE-AND-HARD-AUDIT.md)
- Prior distribution event: [EVT-0189](./EVT-0189-0PLUS-CLEAN-DISTRIBUTION-SMOKE-2026-10-25.md)

## Release identity
- Package version: `0.3.0`
- Stable ID: `HAIF-GPT6-PORTABLE-STARTER-20261025-004`
- Production ID: `HAIF-G6PS-20261025-004`
- Clean file: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`
- SHA-256: `297b3b329143c4b99f55373db0c4bb97896b0e484253622e63eeb32a4429f164`
- Size: 16,266 bytes.
- Contents: `engine.py`, `test_engine.py`, `bootstrap_0plus.py`, `state.schema.json`, `manifest.json`, `README.md`, `GPT6_HOST_INSTRUCTIONS.md`; no Python cache files.

## CI evidence
- Living Architecture Audit [40214177082](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40214177082): SUCCESS on exact head `0d5107fcb389d3ab79e03079d7c1d4d761f911a7`.
- Starter test suite: 13/13 PASS, including the one-command bootstrap, overwrite protection, canonical 0/0+ identity, parent-linked 0.0, duplicate IN/OUT rejection, point/event-ledger reconciliation, tamper rejection and self-parent rejection.
- JSON schema validation and package build passed.

## Fresh-extraction and runtime evidence
- Clean ZIP extracted into a new temporary directory; 13/13 tests passed again.
- `bootstrap_0plus.py --state haif-state.json` returned `BOOTSTRAPPED_AND_READBACK_VERIFIED`.
- Root created as one canonical point `HAIF-POINT-0-024` with labels [`0`, `0+`].
- Child created as `HAIF-POINT-0-0-071`, parent `HAIF-POINT-0-024`.
- Six gaps were explicitly preserved OPEN: independent GPT-6 host import, target-host Python availability, host durable memory/restart, automatic interaction capture, external GitHub write permission, and background execution.
- Bootstrap audit: PASS, 8 events, 6 open gaps, no integrity errors.
- Export/import into a second state path: `IMPORTED_AND_VERIFIED`; post-import audit PASS; state ID and head hash `df612906d02077f05137a90a37bf70ee5fd57e49395146dfb8bc0161f1ae8bb3` matched.

## Honest boundary
The package is ready to transfer and has a one-command initial bootstrap. This is verified in the current Python/container runtime and GitHub Actions. It is not proof of execution inside an independent GPT-6 host. Host-side Python availability, file access, persistent memory across sessions/devices, automatic chat capture, background execution, and host-side GitHub write permissions remain OPEN / NOT PROVEN.


## Time binding
Repository registration timestamp: [TIME-BINDING-EVT-0190](./TIME-BINDING-EVT-0190-BOOTSTRAP-PACKAGE-2026-10-25.md). UTC is canonical; Tehran time is derived from the same instant. The original user-message timestamp remains UNKNOWN / UNVERIFIED.
