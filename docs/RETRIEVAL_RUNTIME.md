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


## Mandatory destination-first retrieval control — LAL-20261106-001

Apply this control before the ordinary LOCATE → RETRIEVE → VERIFY sequence:

1. **Resolve intent and destination.** Honor the store explicitly named by the user. Do not silently substitute Library for GitHub, or one store for another.
2. **Keep stores independent.** GitHub, ChatGPT Library, local attachments, ZIP/package artifacts and external hosts have separate inventories and evidence. A search miss in one cannot establish absence in another.
3. **Read the destination map.** Inspect the canonical README/index/recovery manifest for the selected destination before broad search.
4. **Resolve aliases.** Map a short human name to an exact path plus branch/ref/version using that destination's official map.
5. **Fetch the whole artifact.** A search result, snippet, filename or listing is not the requested document.
6. **Read back identity and content.** Check destination, exact path, branch/ref/version, blob SHA (or store-equivalent immutable identity), full content and requested key fields.
7. **Recover within the same destination after a miss.** Recheck aliases, branch, path, spelling and search terms; do not switch stores without user authorization or a clearly stated separate cross-store check.
8. **Report precise state.** Distinguish not found, inaccessible, incomplete search, retrieved, read-back verified and independent-host recovery.

### Regression acceptance matrix

| ID | Scenario | Required behavior |
|---|---|---|
| SR-01 | User explicitly says “from GitHub/repository” | Repository is searched first; Library is not substituted |
| SR-02 | Same alias could exist in multiple stores | Stores and their results remain separate |
| SR-03 | Official README/index maps a short alias | Exact canonical path/ref is selected from that map |
| SR-04 | Search returns only a snippet/listing | Do not claim full retrieval |
| SR-05 | First search misses in the named store | Retry with corrected alias/path/branch/search strategy in that same store |
| SR-06 | Full artifact is fetched | Verify path, ref/version, SHA and key content |
| SR-07 | A different store has no matching file | Do not infer absence from the requested store |
| SR-08 | Fresh independent host is used | Record its identity/context and independent read-back receipt; do not simulate independence on the original host |

Lesson: `LAL-20261106-001`. Event: `EVT-0252`. The repository CI check validates that this contract and matrix remain present. It does not, by itself, prove that every AI host follows the rule; fresh-host conformance remains a separate gate.
