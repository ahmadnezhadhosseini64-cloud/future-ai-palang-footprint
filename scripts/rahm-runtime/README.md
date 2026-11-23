# RAHM Runtime — HAIF Evidence Bridge

**Status: runnable local kernel and service; supervised deployment package is a candidate pending host installation and acceptance.**

## Core path

`HAIF export → authenticated RAHM intake → verified provenance ledger → proposal-only review`

MAIN remains owner-governed. RAHM cannot write to MAIN/MASTER. Host identifiers are operator-supplied labels, not cryptographic identity proofs.

## Five operational capabilities in this candidate

1. **Automatic start and restart:** `deploy/systemd/rahm.service` starts at boot and restarts a failed process.
2. **Recovery:** systemd restarts the service; `rahm_ops.py restore` verifies a backup manifest, SHA-256, file size and internal ledger chain before atomic restore.
3. **Backup:** `rahm-backup.timer` schedules daily verified snapshots.
4. **Health monitoring:** `rahm-healthcheck.timer` probes the service each minute; a failed probe triggers `rahm-restart.service`.
5. **Independent hosts:** `rahm_host_agent.py` verifies a HAIF export locally and pushes it over authenticated HTTPS; the RAHM ledger records the claimed host label and remains idempotent.

These files are implementation candidates. None of the systemd units is installed or running on a production host merely because it exists in Git.

## Local development

```bash
python scripts/rahm-runtime/rahm_runtime.py --ledger ./rahm-ledger.json init
python scripts/haif-runtime/haif_runtime.py --state ./haif-state.json init
python scripts/haif-runtime/haif_runtime.py --state ./haif-state.json record --input "user input" --output "assistant output"
python scripts/haif-runtime/haif_runtime.py --state ./haif-state.json export > ./haif-export.json
python scripts/rahm-runtime/rahm_runtime.py --ledger ./rahm-ledger.json ingest-haif ./haif-export.json
python scripts/rahm-runtime/rahm_runtime.py --ledger ./rahm-ledger.json verify
python -m unittest discover -s scripts/haif-runtime/tests -v
python -m unittest discover -s scripts/rahm-runtime/tests -v
```

## Backup and restore

```bash
python scripts/rahm-runtime/rahm_ops.py backup --source ./rahm-ledger.json --directory ./backups
python scripts/rahm-runtime/rahm_ops.py restore --source ./backups/rahm-ledger-TIMESTAMP.json --target ./recovered-ledger.json
python scripts/rahm-runtime/rahm_runtime.py --ledger ./recovered-ledger.json verify
```

Backups include a SHA-256/size manifest. Restore refuses a missing/mismatched manifest or invalid internal event chain. Store backup copies off-host for disaster recovery; the repository does not provision that storage.

## Independent host adapter

Set a unique random token in the sender and receiver environments; never commit it. The receiver should be exposed only through a hardened TLS reverse proxy or private network. The bundled service itself defaults to loopback HTTP.

```bash
export RAHM_API_TOKEN="use-a-random-secret-of-at-least-32-characters"
python scripts/rahm-runtime/rahm_host_agent.py --source ./haif-export.json --url https://rahm.example.net/v1/haif/ingest --host-id host-01
```

The host label is provenance metadata supplied by the sender, not proof of identity. Strong per-host identity, key rotation, mutual TLS, rate limiting and revocation remain deployment gates. The adapter does not capture ChatGPT conversations automatically; a real host integration must export HAIF state and invoke this adapter.

## systemd candidate installation (Linux)

Assumptions to adapt before use: repository installed at `/opt/future-ai-palang-footprint`; service account `rahm`; ledger at `/var/lib/rahm/rahm-ledger.json`; backup directory `/var/backups/rahm`.

1. Create a dedicated `rahm` user and directories; make the ledger and backup directories writable only by that account.
2. Initialize the ledger once, then create `/etc/rahm/rahm.env` with `RAHM_API_TOKEN=` plus a random 32+ character value; set permissions to `0600`.
3. Review and install the unit files from `deploy/systemd/` into `/etc/systemd/system/`. The backup service requires `/var/backups/rahm` to exist and be writable by `rahm`.
4. Run `systemctl daemon-reload`, enable and start `rahm.service`, `rahm-backup.timer` and `rahm-healthcheck.timer`.
5. Verify with `systemctl status`, `journalctl -u rahm.service`, the local health endpoint and a real host push. Test reboot, process kill, backup restore and clean-host recovery before calling it production-ready.

The service unit binds to loopback. Remote access requires a separately configured TLS reverse proxy and firewall; do not bind the Python service directly to a public interface.

## Security and honest operational boundary

- RAHM requires a 32+ character environment token and defaults to loopback.
- The host adapter rejects non-HTTPS remote endpoints.
- Health endpoint is intended for local monitoring; protect it at the network boundary.
- Hash chains and SHA-256 manifests detect accidental/tampered content but do not prove author identity or prevent an attacker who can rewrite both data and manifests.
- systemd unit files have not been installed, enabled, reboot-tested or monitored on an actual server.
- Daily backups are scheduled only after the timer is installed and enabled; off-host replication and restore drills remain required.
- This is not automatic ChatGPT capture, semantic AI reasoning, model training or a deployed 24/7 service.
- All RAHM outputs remain `PROPOSAL_ONLY_NO_MASTER_WRITE`.
