# RAHM Runtime — HAIF Evidence Bridge MVP

**Status: IMPLEMENTED AS A LOCAL CANDIDATE; NOT PRODUCTION OR AUTONOMOUS AI.**

RAHM is now a runnable, dependency-free evidence kernel that consumes a verified export from the canonical HAIF local continuity runtime.

## Quick start

```bash
python scripts/rahm-runtime/rahm_runtime.py --ledger ./rahm-ledger.json init
python scripts/haif-runtime/haif_runtime.py --state ./haif-state.json init
python scripts/haif-runtime/haif_runtime.py --state ./haif-state.json record --input "user input" --output "assistant output"
python scripts/haif-runtime/haif_runtime.py --state ./haif-state.json export > ./haif-export.json
python scripts/rahm-runtime/rahm_runtime.py --ledger ./rahm-ledger.json ingest-haif ./haif-export.json
python scripts/rahm-runtime/rahm_runtime.py --ledger ./rahm-ledger.json status
python scripts/rahm-runtime/rahm_runtime.py --ledger ./rahm-ledger.json verify
python -m unittest discover -s scripts/haif-runtime/tests -v
python -m unittest discover -s scripts/rahm-runtime/tests -v
```

## What RAHM does today

- Independently verifies the HAIF source event hash chain before accepting it.
- Ingests source events into its own append-only, SHA-256-linked ledger.
- Preserves source event IDs and hashes for provenance.
- Makes repeated imports idempotent (already-seen source hashes are skipped).
- Produces bounded review proposals and continuity markers.
- Explicitly marks all outputs as proposal-only; it has no MASTER write path.
- Preserves unimplemented capabilities as open gates.

## What it does not do

- It is **not an AI model** and does not reason semantically, train weights, or autonomously learn. Current assessment is deterministic routing of evidence to human review.
- It does not automatically capture ChatGPT conversations or run in the background.
- It does not connect to GitHub, cloud storage, a scheduler, or another host at runtime.
- It does not provide encryption, signatures, tamper-proof authorship, or multi-user access control.
- It does not write to MAIN, MASTER, branch protections, secrets, or production systems.
- It does not yet perform clean-host recovery or restart/cross-device acceptance.

## Architecture boundary

`MAIN (owner-governed authority) → HAIF (interaction continuity runtime) → RAHM (evidence ledger and review proposals)`

Feedback is returned as a proposal/evidence package for owner review. No reverse write path to MASTER exists. Owner approval remains a separate required gate.

## Acceptance

The tests verify HAIF source tamper rejection, RAHM ledger integrity, idempotent repeated ingestion, refusal to overwrite an existing ledger, and proposal-only authority labeling. These tests prove the coded local behavior only.

## Run the continuously listening local bridge

After initializing the ledger and exporting a HAIF state, the RAHM bridge can stay running as a local HTTP process:

```bash
python scripts/rahm-runtime/rahm_runtime.py --ledger ./rahm-ledger.json init
# Set a random secret of at least 32 characters in the environment; never commit it.
export RAHM_API_TOKEN="replace-with-a-long-random-secret-value"
python scripts/rahm-runtime/rahm_service.py --ledger ./rahm-ledger.json --host 127.0.0.1 --port 8765
```

- `GET /health` reports local process/ledger health.
- `POST /v1/haif/ingest` accepts a HAIF JSON export with `Authorization: Bearer <RAHM_API_TOKEN>`.
- Source chain is verified before append; duplicate events are skipped.
- Default bind is loopback only. Do not bind to a public interface without TLS, a hardened reverse proxy, network controls, rate limits, backup/restore and deployment review.
- The process is continuously listening only while the operator keeps it running. A production supervisor, host provisioning, monitoring, backups and restart policy are not yet deployed or proven.
