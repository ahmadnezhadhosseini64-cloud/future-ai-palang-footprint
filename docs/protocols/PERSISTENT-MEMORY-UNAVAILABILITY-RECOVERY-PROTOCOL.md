# Persistent Memory Unavailability & Recovery Protocol

- ID: PMURP-2026-08-31-001
- Status: ACTIVE / LIVE / PERMANENT OPERATIONAL RULE
- Project: Future AI / Palang Footprint
- Reference Point: 0.0

## Purpose

Prevent loss or false claims when the assistant's persistent-memory layer is unavailable, fails, or cannot confirm a write.

## Core Rule

Persistent Memory is one persistence layer, not the sole continuity mechanism.

A production that is approved for durable registration must never be treated as safely stored merely because the assistant attempted to save it to persistent memory.

## Mandatory Fallback

When Persistent Memory is unavailable, write access is unavailable, or post-write confirmation cannot be obtained:

`Detect → Human Approval → Create/retain unique Production ID → Persist to available durable project repository / Recovery Buffer → Retrieve → Verify → mark MEMORY=UNVERIFIED`

The repository-side record is the durable continuity record for the failed memory layer. It must preserve the same identity, provenance, status, and continuation path; it must not create a second identity merely because the memory layer failed.

## Truth Boundary

- Memory write attempted ≠ Memory persisted.
- Memory unavailable ≠ Project data lost, if a verified durable repository/recovery record exists.
- Repository registration ≠ Persistent Memory registration.
- Persistent Memory = UNVERIFIED must remain explicit until an actual memory read-back confirms persistence.
- No component may claim `MEMORY=VERIFIED` without retrievable evidence from the memory layer itself.

## Recovery

On the next valid opportunity:

1. Retrieve the repository/recovery record by its unique ID.
2. Reconcile against any available Persistent Memory record.
3. If Memory is absent or unverified, do not duplicate the production.
4. Attempt the missing memory persistence using the existing identity.
5. Retrieve/read-back the memory layer.
6. Update the cross-layer status only from evidence.

## 0.0 Integration

At `0.0`, the continuity check must include the Persistent Memory status. If Memory is unavailable, recovery continues from the verified repository/recovery record and explicitly carries `MEMORY=UNVERIFIED`.

If both Persistent Memory and the durable repository/recovery layer are unavailable, the system must stop the durable-registration claim and report `UNVERIFIED`; it must not fabricate persistence evidence.

## Scope

This protocol closes the operational gap between the existing Recovery Architecture and the actual capability boundary of Persistent Memory. It does not redefine Persistent Memory and does not promote repository storage to Memory storage.

## Evidence Requirement

A successful repository commit proves repository persistence only. A successful memory write can be claimed only after memory-layer retrieval/read-back evidence exists.

## Integration

This protocol integrates with Recovery & Resilient Memory Architecture, Continuation Path Preservation, Dual Durable Registration, Permanent Registration Not Trace, Evidence Gate, Execution Claim Integrity, and Checkpoint 0.0.
