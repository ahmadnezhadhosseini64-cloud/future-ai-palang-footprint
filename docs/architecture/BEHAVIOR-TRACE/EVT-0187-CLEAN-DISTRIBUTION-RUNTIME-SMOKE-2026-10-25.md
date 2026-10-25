# EVT-0187 — Clean Distribution Runtime Smoke Test

- Stable ID: HAIF-EVT-0187-CLEAN-DISTRIBUTION-RUNTIME-SMOKE-20261025
- Production ID: HAIF-EVT-0187-20261025
- Version: 1.0.0
- Status: PASS / LOCAL CLEAN-PACKAGE EXECUTION VERIFIED / INDEPENDENT GPT HOST OPEN
- Root: [POINT-0/023](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261025-023-HARD-AUDIT-AND-ENGINE-HARDENING.md)
- Current checkpoint: [CURRENT-070](../../0.0/anchors/PALANG-0.0-CURRENT-20261025-070-HARD-AUDIT-AND-HOST-EXECUTION.md)
- Parent engine audit: [EVT-0186](./EVT-0186-HAIF-ENGINE-HARD-AUDIT-AND-ID-UNIQUENESS-2026-10-25.md)

## Executed workflow
The cleaned distribution ZIP was extracted to a fresh temporary directory. Using the extracted `engine.py`, the following actual CLI operations were executed in sequence:

1. `init` — PASS; created state file.
2. `record` — PASS; returned `RECORDED_AND_READBACK_VERIFIED` and independent Anchor/IN/OUT/Event IDs.
3. `audit` — PASS; one interaction, no integrity errors.
4. `export` — PASS; produced a portable JSON bundle.
5. `import` into a second, clean state path — PASS; returned `IMPORTED_AND_VERIFIED`.
6. `audit` on imported state — PASS; same state identity, same event count, same head hash.

## Evidence
- Clean ZIP SHA-256: `d68e03b42e26b88385d1155c02d09b213a53366e27e99518c7c049f6ec6563be`.
- Synthetic smoke-test state ID: `HAIF-STATE-3809bda4d6504d6ba2236e4b32d71d5c`.
- Anchor ID: `HAIF-ANCHOR-5dcdf46d65dc4613b59df16125c9fb1b`.
- IN ID: `HAIF-IN-e3bd764a45e7418b94725c8683861987`.
- OUT ID: `HAIF-OUT-38b2ead8c79e488ca45f9d13c16dea9c`.
- Event ID: `EVT-008e5cbf63ca494786e465a333bc178d`.
- Imported state head hash: `d294c64ecd4c870c03c6512a6ac5aa5b9a2b099343c15c1aebef063bf439d2f5`.
- Exported smoke bundle SHA-256: `6f1824f1186d9fe2bb5bb88cdaff6aaa8dd66ab1eb0b8b3f9464ba3aa09bac01`.

## Honest boundary
This is direct execution of the Python engine in the current tool's container runtime and proves the local CLI lifecycle on the cleaned package. The sample is synthetic. It does not prove that the target GPT-6 host exposes Python, can import files, retains state across sessions, or can write to GitHub. Those host-specific checks remain OPEN / NOT PROVEN.
