# POINT-0/044 — Update the existing starter ZIP in place

- Stable ID: HAIF-POINT-0-044-STARTER-ZIP-INPLACE-UPDATE-20261027
- Production ID: HAIF-P044-ZIP-UPDATE-20261027
- Date: 2026-10-27
- Type: canonical point 0
- Parent: POINT-0/043 (0+ production marker)
- Continuation: IN-082 → OUT-081 → EVT-0219 → CURRENT-094 → NEXT-051
- Goal: update the existing HAIF starter package in its established package line and preserve its canonical ZIP filename; do not fork a separate package/version ZIP identity.
- Required capability: independent-host recovery protocol and evidence-driven import, IN/OUT reconstruction, negative controls, read-back and restart gate.
- Key correction: changing repository source or EXPORT_MANIFEST alone does not update the starter ZIP. The canonical ZIP must be rebuilt from the starter source directory under the same established filename, then its exact bytes/hash and artifact must be verified.
- Status: REGISTERED IN SOURCE; ZIP replacement build and artifact receipt PENDING until the triggered workflow completes and is inspected.
- Do not claim real independent-host acceptance from a build/CI pass. Keep NEXT-051 the sole active queue; do not create NEXT-052.
