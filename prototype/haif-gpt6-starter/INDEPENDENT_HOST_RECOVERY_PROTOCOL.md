# Independent-host recovery proof protocol

Package version: 0.3.1
Project: Future AI / Palang Footprint
Canonical chain: POINT-0/043 (0+ marker) → POINT-0/044 (canonical 0) → IN-082 → OUT-081 → EVT-0219 → CURRENT-094 → NEXT-051

## Purpose
Prove that a genuinely separate AI host can reconstruct the project from the package without relying on this chat's hidden history. Repository presence, a CI pass, or a runtime-to-runtime test is not independent-host acceptance.

## Required procedure
1. Freeze the package: record repository commit SHA, package version, manifest bytes/SHA-256, ZIP bytes/SHA-256 and exact file inventory.
2. Verify integrity: extract into a clean directory, check the package digest and required files, reject altered/missing files.
3. Prove host independence: use a separate host/session with no prior conversation context. Record host/model/version only when visible; otherwise UNKNOWN.
4. Import: provide only the package and its included instructions. The host must identify current point, active queue, master reference, parent lineage, version inventory and every open gap without inventing missing data.
5. Reconstruct from IN and OUT separately: both paths must recover the same normalized chain, checkpoint, event IDs, package version, evidence references and open-gate statuses.
6. Negative controls: modify one byte, remove a required file, and supply invalid state. Each defect must be detected or rejected.
7. Independent read-back: export or display reconstructed state and compare it with frozen expected state. Save raw receipts and hashes.
8. Restart/persistence: close the session or restart the host and repeat recovery. If persistence is unavailable, record NOT SUPPORTED / NOT VERIFIED.

## PASS criteria
PASS requires direct evidence for package hash, complete inventory, clean host identity, independent import, IN/OUT equivalence, preserved open gaps, negative controls and read-back. Restart persistence is a separate gate.

## Status at package build
- Local starter tests: must be read from the exact CI run for this package revision.
- ZIP build and SHA-256: pending until workflow artifact and digest are inspected.
- Real independent AI-host import: NOT RUN.
- Second-host and restart persistence: NOT RUN.
- Automatic message capture and background execution: NOT PROVEN.

Never mark a host gate PASS from documentation alone.


## Existing ZIP replacement identity
The deliverable is the existing starter package continuously updated under the canonical filename `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`; do not publish a second version-named ZIP. The historic v0.3.0 digest (297b3b329143c4b99f55373db0c4bb97896b0e484253622e63eeb32a4429f164) is historical only. The updated archive must carry a fresh digest and byte count from its own build receipt.
