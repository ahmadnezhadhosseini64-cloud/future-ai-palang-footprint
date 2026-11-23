# MAIN–HAIF–RAHM Living Runtime Boundary

- Status: ACTIVE / IMPLEMENTED CANDIDATE / OWNER GOVERNANCE PRESERVED
- Date: 2026-11-23
- Stable architecture root: POINT-0/GOLDEN
- Sole continuation queue: NEXT-051
- Scope: RAHM evidence kernel, HAIF bridge, and five-part operational management candidate

## Permanent architecture

The three assets are one living system with distinct authority boundaries:

1. **MAIN** — canonical reference, governance, owner authority and controlled promotion.
2. **HAIF** — interaction continuity runtime: explicit IN/OUT capture, append-only event chain, checkpoint, export/import and verification.
3. **RAHM** — evidence intake, source provenance, deterministic triage, continuity proposals and owner-review feedback.

Canonical flow:

`HUMAN ↔ AI HOST ↔ HAIF → RAHM → VALIDATION / PROPOSAL → OWNER REVIEW → CONTROLLED MASTER PROMOTION`

No AI host or RAHM process has a direct or indirect write path to MAIN/MASTER. All RAHM outputs remain `PROPOSAL_ONLY_NO_MASTER_WRITE`.

## Implemented and verified in the owner-approved baseline

- RAHM verifies the HAIF source event hash chain before ingest.
- Source event IDs and hashes are preserved; duplicate source hashes are skipped.
- RAHM maintains a separate SHA-256-linked evidence ledger.
- Authenticated local HTTP intake is available at `POST /v1/haif/ingest`; health at `GET /health`.
- Real HAIF-to-RAHM end-to-end and authenticated HTTP tests passed.
- Baseline PR #150 merged to the canonical POINT-0/GOLDEN governance branch as commit `21ca06eee1dbc35c4dfa8663308d251de9e711bb`.

## Five-part operational management candidate (PR #151)

1. **Automatic start and process restart:** hardened Linux systemd service unit with boot enablement and restart-on-failure.
2. **Recovery:** verified restore tool checks manifest schema/name, SHA-256, byte count and internal ledger chain before atomic replacement; service restart is also managed by systemd.
3. **Backup:** daily persistent systemd timer and oneshot backup service; backup includes a separate checksum/size manifest.
4. **Health monitoring:** one-minute health probe; failed probe invokes a systemd restart unit. Graceful SIGTERM shutdown is implemented and integration-tested.
5. **Independent host bridge:** sender adapter verifies HAIF export, requires a 32+ character token, enforces HTTPS off-loopback, and posts to RAHM. RAHM records the sender-provided host label and skips duplicate events.

The exact tested commit is always the latest PR #151 head SHA paired with its GitHub Actions check runs; do not reuse a prior candidate SHA as current evidence.
- RAHM/HAIF runtime tests: SUCCESS.
- Living Architecture Audit: SUCCESS.
- Backup/restore tamper rejection, independent-host authenticated push, duplicate replay, health probe, graceful stop and ledger verification are covered by CI tests.

## Operational boundary — not yet deployed

The five mechanisms exist as code/configuration candidates in the repository. They are not yet installed, enabled or running on a real server. Therefore none of the following is claimed as complete:
- 24/7 process uptime or actual machine-reboot recovery;
- scheduled off-host backup execution or a disaster-recovery restore drill;
- real remote-host onboarding, TLS reverse-proxy provisioning, key rotation or cryptographic host identity;
- automatic capture of live ChatGPT conversations;
- independent clean-host recovery.

A passing CI run proves tested candidate behavior only. It does not prove production provisioning, uptime, off-host durability or security certification.

## Required real-host acceptance gates

1. Provision a Linux host and dedicated least-privilege `rahm` account.
2. Install units, initialize the ledger, configure a random secret outside the repository, and enable service/timers.
3. Reboot the host; kill the service process; verify automatic restart and health recovery.
4. Execute a backup, copy it off-host, restore on a clean environment, and compare ledger ID, event count and head hash.
5. Place the service behind TLS/private networking; enroll independent hosts with per-host credentials and revocation.
6. Verify no host or RAHM process can write to MAIN/MASTER.
7. Only after real uptime, recovery and security evidence may deployment status be upgraded.

## No-fake-closure

- Implemented ≠ deployed.
- A systemd unit in Git ≠ enabled at boot.
- Local backup ≠ off-host disaster recovery.
- Sender-provided host label ≠ cryptographic identity.
- Hash chain ≠ proof of author identity or protection against complete rewrite.
- Deterministic triage ≠ semantic AI reasoning or model training.
- CI PASS ≠ 24/7 operation or clean-host acceptance.

MAIN/MASTER remain unchanged. Owner authority and controlled promotion remain permanent.
