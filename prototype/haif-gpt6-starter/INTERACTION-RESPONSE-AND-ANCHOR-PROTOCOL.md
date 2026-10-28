# Interaction response and anchor protocol

Package family: HAIF GPT-6 Portable Starter
Stable package ID: HAIF-GPT6-PORTABLE-STARTER-20261025-004
Canonical ZIP filename: haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip
Internal version: 0.3.8
Current chain: POINT-0/056 (0+ marker on canonical root 0) → IN-094 → OUT-093 → EVT-0231 → CURRENT-106 → NEXT-051

## 1. Visible response is mandatory
When an input is received, the host must produce one of:
- ACKNOWLEDGED — accepted and being processed, with a durable interaction ID if available;
- COMPLETED — a user-visible result exists and its completion evidence is identified;
- BLOCKED — a named dependency, permission or missing input prevents completion;
- FAILED — the operation failed, with the actual error or concise safe reason;
- PARTIAL — completed substeps and remaining open gates are separated.

A spinner or internal processing state is not a user-facing result. If work continues beyond the current response, provide a concise status and the next concrete action. Never claim success before the tool/host confirms it. If an action cannot be performed in the current environment, say so.

## 2. Anchor each interaction
Where the host has authorized durable storage, pair each actual user input with the actual assistant output:
- independent point/anchor, IN, OUT and EVT identifiers;
- parent point/checkpoint and package version;
- exact payload or content-addressed evidence reference;
- source host/session and actual observed/received timestamps, UTC first with Tehran equivalent derived from the same instant where applicable;
- payload SHA-256, result status, evidence references and open gaps.

Do not invent message timestamps, missing outputs, tool results or success states. If a reply is absent, register RESPONSE_MISSING / OPEN only when the host can observe that absence. If storage is unavailable, return a manual export and mark persistent registration NOT VERIFIED.

## 3. Failure and recovery
On a tool failure, timeout or rejected write:
1. show FAILED/BLOCKED/PARTIAL to the user;
2. preserve the failure and retry/correction as observable evidence;
3. do not duplicate IDs or silently overwrite the original event;
4. retry idempotently when safe;
5. read back the destination and compare exact bytes before claiming VERIFIED;
6. link the correction to the original event and current checkpoint.

## 4. Growth into Future AI / Palang Footprint
- Record observable behavior, task context, tool/action summaries, outcomes, explicit feedback, failures and corrections.
- Separate OBSERVATION, INFERENCE, HYPOTHESIS, UNKNOWN and DECISION.
- Minimize private/unrelated/sensitive content; never put credentials or tokens in events.
- RAHM checks schema, provenance, integrity, privacy, conflicts and reproducibility.
- New knowledge remains a Child candidate until evidence passes and explicit human approval allows promotion to the living Master.
- Rebuild the same canonical ZIP from the package source, increment internal version, preserve stable ID and canonical filename, test extracted bytes, hash exact archive bytes and record a fresh receipt.

## 5. What this protocol does not grant
This document does not itself create a native GPT plugin, automatic message hook, background worker, repository token or persistent memory. Each requires an actual host integration and direct acceptance receipt. Until then, live capture, write-back and restart persistence are OPEN / NOT VERIFIED.
