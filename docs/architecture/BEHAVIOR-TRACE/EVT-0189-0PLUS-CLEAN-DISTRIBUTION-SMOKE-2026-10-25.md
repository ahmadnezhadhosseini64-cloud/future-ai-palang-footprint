# EVT-0189 — v0.2.1 Clean Distribution, Point-Lineage and Cold-Start Smoke Test

- Stable ID: HAIF-EVT-0189-0PLUS-CLEAN-DISTRIBUTION-SMOKE-20261025
- Production ID: HAIF-EVT-0189-20261025
- Version: 1.0.0
- Status: PASS / CLEAN ZIP FRESH-EXTRACT TESTED / CLI EXPORT-IMPORT RECOVERY VERIFIED / INDEPENDENT GPT HOST OPEN
- Root: [POINT-0/024](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261025-024-0PLUS-PRODUCTION-MARKER.md)
- Current checkpoint: [CURRENT-071](../../0.0/anchors/PALANG-0.0-CURRENT-20261025-071-0PLUS-ENGINE-AND-HARD-AUDIT.md)
- Parent hard-audit event: [EVT-0188](./EVT-0188-POINT-0PLUS-IDENTITY-AND-0-0-LINEAGE-2026-10-25.md)

## Source and CI evidence
- Exact-head Living Architecture Audit: [run 40213760585](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40213760585), SUCCESS on `0819d97283d892411a6868c544e92752a8c35c55`.
- Engine/test code commit: `49485c593ebd6a3d115c05ddda8e8997b3c5138e`.
- Package manifest version: `0.2.1`; Stable ID `HAIF-GPT6-PORTABLE-STARTER-20261025-003`; Production ID `HAIF-G6PS-20261025-003`.
- CI starter tests: 12/12 PASS. JSON schema validation and package build passed.

## Clean distribution artifact
- File: `haif-gpt6-starter-v0.2.1-0plus-clean.zip` (generated in the current conversation).
- SHA-256: `51a5f9a6def97a0564a8b6542bbf4a5b9ca46a81a267a4a02db7c53511e16f2d`.
- ZIP size: 14,077 bytes.
- Contents: `engine.py`, `test_engine.py`, `state.schema.json`, `manifest.json`, `README.md`, `GPT6_HOST_INSTRUCTIONS.md`; no `__pycache__` or `.pyc` files.
- The ZIP was extracted into a new temporary directory and all 12 tests passed there.

## Direct CLI smoke test
Executed against the extracted package:
1. Initialize a new state — PASS.
2. Register canonical root with labels `0` and `0+` and production marker — PASS / read-back verified.
3. Register child continuation `0.0` with parent ID of the canonical root — PASS / read-back verified.
4. Record an interaction pair — PASS / independent Anchor, IN, OUT and Event IDs returned.
5. Audit the state — PASS; 3 events, zero integrity errors.
6. Export a portable JSON bundle — PASS.
7. Import into a second state path — PASS / `IMPORTED_AND_VERIFIED`.
8. Audit imported state — PASS; same state ID and head hash `10c0f3193cabee8b0bc17c9273a362ce2768321f3ef0f7307c1aa470eb87afd4`.

## Scope boundary
This proves the package executes in the current Python/container runtime and that the local CLI supports point registration, interaction logging, integrity audit, and export/import recovery. It does not prove the intended independent GPT-6 host has Python, can access files, retains state across sessions/devices, or can write to GitHub. Automatic chat capture, native GPT plugin behavior, background execution, durable host memory, external writes, and cross-device persistence remain OPEN / NOT PROVEN.
