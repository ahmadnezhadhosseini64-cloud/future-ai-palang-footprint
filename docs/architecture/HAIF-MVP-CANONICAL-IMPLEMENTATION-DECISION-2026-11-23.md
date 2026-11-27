# HAIF MVP — Canonical Implementation Decision
- Status: ACTIVE / PROPOSED FOR OWNER REVIEW
- Date: 2026-11-23
- Scope: implementation selection and recoverable archival of the secondary prototype
- Canonical active runtime: `scripts/haif-runtime/`

## Decision
Use `scripts/haif-runtime/` as the single active MVP core. It is dependency-free, uses a portable JSON state file, records IN/OUT interactions, chains events with SHA-256, supports checkpoints, verifies state, exports portable JSON, and imports into a new path.

Do not continue parallel feature development in the former `prototype/haif-v0/` implementation. That implementation is moved to `archive/implementations/haif-v0/` in this candidate branch. This is a reversible archive/quarantine, not permanent deletion.

## Why this is the MVP
- Python 3.10+ and standard library only.
- One local state file; no service, database server, or third-party dependency is needed.
- Explicit write/read validation and hash-chain verification.
- Portable export and import to a new destination.
- Lower operational burden for the first independently runnable model.

SQLite/FastAPI are not rejected as technologies. They are deferred as optional future adapters only if a demonstrated requirement needs them. They must not become a second competing core.

## Checkpoint correction
A checkpoint represents a verified prefix of the event chain, not a requirement that the chain stop growing. The runtime now validates that the checkpoint count identifies an existing prefix and that its stored head hash matches that prefix. Appending later events must not invalidate an earlier checkpoint; a later checkpoint may advance the pin.

## Recoverable archive inventory
The following files were copied into the archive before their active prototype paths were removed on this candidate branch. Each archived file was read back and its Git blob SHA matched the original source blob SHA.

| Original path | Archived path | Verified original/archive blob SHA |
|---|---|---|
| `prototype/haif-v0/README.md` | `archive/implementations/haif-v0/README.md` | `1794f7f68c0f103e94b235f0219a630d3bc90e52` |
| `prototype/haif-v0/app.py` | `archive/implementations/haif-v0/app.py` | `7f85e073c92ae22409ec75b8a225817e0da713ab` |
| `prototype/haif-v0/ingest_repository_docs.py` | `archive/implementations/haif-v0/ingest_repository_docs.py` | `e26911bce9136cf0bafaf3c5ea2152a43cce9174` |
| `prototype/haif-v0/requirements.txt` | `archive/implementations/haif-v0/requirements.txt` | `0772b6ae1423f68aedeb8607f7edaecaf6619771` |
| `prototype/haif-v0/test_app.py` | `archive/implementations/haif-v0/test_app.py` | `1ec4005e381f511c3a681be66a21eb77ff45b7d4` |

## MVP acceptance path
1. Initialize a new state file.
2. Record multiple IN/OUT pairs.
3. Create a checkpoint.
4. Append additional events without invalidating the prior checkpoint.
5. Advance the checkpoint.
6. Export the state.
7. Import into a distinct, previously nonexistent path.
8. Verify the restored chain and matching head hash.
9. Demonstrate tamper detection and refusal to overwrite an existing state/import target.

## Boundaries — not yet claimed as complete
- Automatic capture of live ChatGPT conversations.
- Background execution or scheduled wake-up of an AI host.
- Cross-device durable storage and independent-host recovery in a clean environment.
- Secure OAuth/GitHub App integration, private service, deployment, and host-specific permissions.
- Cryptographic proof of author identity or protection against an attacker rewriting the entire state and chain.

## Ownership and authority
This MVP is a local continuity tool and candidate host workspace component. It does not grant any AI host write authority over MASTER. All promotion to MASTER remains owner-controlled and separately verified.

## Review status
This decision and its implementation changes are on a candidate branch and must pass repository CI and owner review before integration into `main`. A branch commit or passing unit test is not equivalent to final architecture acceptance.
