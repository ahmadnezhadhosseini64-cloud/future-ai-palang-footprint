# Persistent Memory Adapter Specification

**Production ID:** PMA-2026-09-01-001  
**Status:** FINAL / ACTIVE / LIVING  
**Reference:** 0.0  
**Date:** 2026-09-01  
**Project:** Future AI / Palang Footprint

## Purpose

Provide a stronger, portable memory layer for project records without pretending that ChatGPT Persistent Memory has been independently written and read back when the required direct tool is unavailable.

## Canonical Principle

The Canonical Repository is the authoritative external memory layer. ChatGPT Persistent Memory is an auxiliary memory layer. A record is not promoted from PENDING to Persistent-Memory-VERIFIED without an independent write/read-back proof.

## Required Record Lifecycle

`IDENTIFY → CLASSIFY → VALIDATE → DEDUPLICATE → WRITE → READ-BACK → MATCH → VERIFY → CLOSE`

If WRITE or READ-BACK cannot be independently verified:

`PRESERVE SAME PRODUCTION ID → PENDING / RECOVERY`

No duplicate record is created.

## Memory Layers

1. **Canonical Repository** — authoritative, versioned, externally inspectable.
2. **Pending / Recovery Store** — preserves incomplete or unverified writes and their provenance.
3. **ChatGPT Persistent Memory** — auxiliary conversational memory; status must remain UNVERIFIED unless an independent read-back is available.
4. **Portable Adapter** — interface layer that can later connect the project record to a database, object store, Git-backed store, or another memory provider.

## Adapter Contract

A future implementation must expose these logical operations:

- `write(record_id, payload, provenance)`
- `read(record_id)`
- `verify(record_id, expected_hash_or_payload)`
- `reconcile(record_id)`
- `status(record_id)`

Each successful write must return a provider receipt or equivalent immutable identifier. Verification must read the record independently rather than trusting the write response alone.

## Required Evidence

For every verified memory write, preserve:

- Production ID
- Provider / storage target
- Write receipt or commit identifier
- Read-back result
- Integrity comparison (hash or exact canonical payload match)
- Timestamp + timezone
- Provenance
- Final state

## Current Gap

`ChatGPT Persistent Memory Direct Write + Independent Read-back = UNVERIFIED / PENDING`

This is intentional. The gap is not silently closed by treating conversation context, model memory, or repository storage as proof of a Persistent Memory write.

## Current Anchor

`MPGG-2026-09-01-001` remains the existing architectural correction record and must be reused for reconciliation where applicable. The adapter specification itself uses `PMA-2026-09-01-001` so the architecture and the original production record are not duplicated.

## Security / Integrity Rule

No provider credential, secret, API key, or private token is stored in the repository. Provider configuration must be supplied through secure runtime secrets when an implementation is deployed.

## Acceptance Test

The adapter is considered operational only after an independent test demonstrates:

1. A known record is written.
2. The provider returns a durable receipt.
3. The same record is fetched through an independent read operation.
4. The fetched payload matches the expected record.
5. A deliberately altered expected value fails verification.
6. A simulated unavailable provider preserves the same record in PENDING / RECOVERY.

Until all six conditions are demonstrated, the adapter remains `SPECIFICATION / NOT PROVEN IN EXECUTION`.
