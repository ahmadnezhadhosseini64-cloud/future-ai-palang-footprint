# Retrieval Runtime

**Reference ID:** RTR-2026-08-29-001  
**Project:** Future AI / Palang Footprint  
**Reference Point:** 0.0  
**Status:** ACTIVE

## Operational Contract

At every 0.0 recovery or continuation boundary, use this sequence:

**LOCATE → RETRIEVE → VERIFY → RECONCILE → REPORT → CONTINUE**

### 1. LOCATE
Use the canonical repository and `main` branch as the external retrieval source.

### 2. RETRIEVE
Retrieve the minimum recovery set:
- `README.md`
- `docs/STABLE_RETRIEVAL_CORE.md`
- `docs/REFERENCE_INDEX.md`
- `docs/EVIDENCE_GATE.md`
- `docs/CHECKPOINT.md`
- `docs/CURRENT_STATE.md` when present

### 3. VERIFY
Check that the retrieved files exist and that their statuses and evidence agree. Do not infer missing evidence.

### 4. RECONCILE
If two canonical documents disagree, do not silently overwrite either one. Record the contradiction, identify the newer verified state, and resolve it through a new commit using the current file SHA.

### 5. REPORT
Separate:
- VERIFIED facts
- HISTORICAL evidence
- UNVERIFIED claims
- WARNINGS / conflicts

### 6. CONTINUE
Only after verification and reconciliation may project execution continue.

## Evidence Gate Integration

The Evidence Gate is currently **PROVEN / ACTIVE / CLOSED / PASS**. Independent execution evidence must remain tied to an inspectable GitHub Actions run. The successful run history is evidence; this document is only the runtime procedure.

## Anti-Drift Rule

A later document must not silently downgrade or upgrade evidence status. Any status transition requires a new dated record and supporting evidence.

## Recovery Truth Boundary

Repository retrieval proves availability of the external record. It does not, by itself, prove execution. Execution claims require Evidence Gate verification.
