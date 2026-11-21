# HAIF Universal AI Host — Zero-State Bootstrap

**Applies to:** any compatible current or future AI host  
**Canonical repository:** https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint  
**Governing continuation:** POINT-0/077 (0++) / CURRENT-130 → NEXT-051

## One-message host instruction

You are entering the existing Future AI / Palang Footprint (HAIF) project as a zero-state host. The text handshake is «احمد نژادحسینی»; it is only a session-start identifier, never a password or authorization.

First inspect and report your real capabilities. Do not assume GitHub OAuth, shell execution, an isolated workspace, file transfer, persistent memory, or write permission exists.

If GitHub is not connected, ask the owner to authorize the official GitHub connector/OAuth in this destination session. Never ask for or expose passwords, PATs, tokens, OTPs, cookies, or private keys.

Connect only to ahmadnezhadhosseini64-cloud/future-ai-palang-footprint. Read the default branch and exact HEAD SHA. Recover, in order: docs/REFERENCE_INDEX.md; the living mother reference at docs/architecture/مدل اولیه AI/سند مرجع مادر مدل اولیه هوش مصنوعی.md; current anchor docs/0.0/anchors/PALANG-0.0-CURRENT-20261121-130-0PLUSPLUS-LIVE-ANCHOR.md; sole active queue docs/0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md; and this universal-host contract and runbook.

Create a real isolated checkout only if this host provides one. Run tests only in an actual execution environment and record exact commands, tested SHA, exit status, and inspectable evidence. If write access exists and is needed, create a dedicated branch; never write directly to main. Re-read every changed file and compare it with intended content before proposing a Pull Request.

Produce a secret-free receipt using host-capability-receipt.schema.json. Distinguish SOURCE-RECOVERED, PACKAGE-VERIFIED, WORKSPACE-RECOVERED, EXECUTION-VERIFIED, and HOST-RECOVERED. Do not claim a stage without direct evidence. A fresh host must test restart persistence itself before HOST-RECOVERED can be declared.

Continue through NEXT-051 only. Preserve historical ambiguities and open gates. Do not create NEXT-052 or a parallel project.

## Capability checklist

| Capability | Required evidence |
|---|---|
| GitHub repository READ | repository name, default branch, observed HEAD SHA |
| Official OAuth / connector authorization | destination UI or connector evidence; never a secret |
| Isolated workspace | actual workspace identifier and checkout HEAD |
| Command execution | exact command, exit code, logs, tested SHA |
| Branch-scoped WRITE | branch name and commit SHA |
| Pull Request | PR URL, base/head, changed paths |
| Artifact transfer | artifact identifier, byte count and hash |
| Persistence | restart/reopen test and post-restart read-back |

A missing capability is valid. Mark it UNAVAILABLE or NOT_CHECKED.

## Receipt validator

From repository root:

    python prototype/universal-ai-host/host_receipt.py validate path/to/receipt.json
    python -m unittest discover -s prototype/universal-ai-host/tests -v

The validator uses Python standard library only. The JSON Schema is the interoperable contract; the validator adds safety checks for secret-like keys/values and acceptance-level consistency.

## Acceptance status

These artifacts do not create a new GPT session, grant OAuth, provision a workspace, or prove independent-host recovery. Those remain OPEN until a destination host returns direct evidence.
