# HAIF Universal Host Connectivity

This package provides a host-neutral acceptance-receipt contract and a dependency-free validator.

## Validate a receipt

```bash
python3 scripts/host-connectivity/validate_receipt.py path/to/receipt.json
```

Exit codes: `0` valid, `1` receipt rejected, `2` file/JSON input error.

## Run tests

```bash
python3 -m unittest discover -s scripts/host-connectivity/tests -v
```

## Security

The receipt stores only non-secret metadata. Never put OAuth tokens, PATs, passwords, cookies, OTPs, secrets or authorization headers in receipts. OAuth must be approved independently in the official UI of each destination host. A text handshake is not authentication. READ, EXECUTE, WORKSPACE and WRITE are distinct capabilities; writes are branch-only and proposed through PR.

See `docs/host-connectivity/UNIVERSAL-AI-HOST-CONNECTIVITY-CONTRACT-2026-11-21-001.md` for the governing contract.
