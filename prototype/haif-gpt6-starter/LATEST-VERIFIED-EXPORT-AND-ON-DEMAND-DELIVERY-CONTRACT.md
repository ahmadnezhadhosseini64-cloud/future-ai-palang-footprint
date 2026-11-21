# Latest Verified Export and On-Demand Delivery — Portable Host Contract

- Stable ID: HAIF-LATEST-VERIFIED-EXPORT-DELIVERY-CONTRACT-2026-11-20-001
- Package stable ID: HAIF-GPT6-PORTABLE-STARTER-20261025-004
- Canonical ZIP filename: haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip
- Current project checkpoint at source registration: CURRENT-125 (POINT-0/072 under canonical root 0)
- Sole active queue: NEXT-051

## Required behavior

When the user asks for the latest complete version, resolve the current canonical repository main SHA, latest living mother reference, latest successful package build and its exact tested SHA. Deliver only the canonical ZIP whose receipt matches current main, together with the byte-matched living mother and machine-readable receipt/checksum.

A newer main commit invalidates the exact-current-head label until a new build succeeds. Never silently substitute an older archive.

## Package acceptance

Require stable package identity, canonical filename, valid inventory, ZIP CRC, exact source-to-extracted byte match, tests executed from the extracted ZIP, actual byte count and SHA-256, and downloaded-artifact round-trip verification. Keep the build receipt external to the ZIP to avoid a self-referential digest.

## Status vocabulary

- SOURCE_CURRENT: current sources identified; no archive proof.
- PACKAGE_BUILT: archive exists; verification may be incomplete.
- PACKAGE_VERIFIED: all package-level checks pass on exact current main SHA.
- HOST_RECOVERED: a genuinely independent clean AI host imported and reconstructed the state with direct evidence.

PACKAGE_VERIFIED is not HOST_RECOVERED.

## Honest capability boundaries

A verified archive does not prove clean-host import, restart persistence, persistent memory, automatic live message capture, background execution, live ChatGPT producer, repository write-back from a host, or external storage persistence. Keep those gates OPEN / NOT RUN / NOT VERIFIED until direct evidence exists.


## Living interactive evolution — package v0.4.1

The canonical starter is continuously evolvable through validated human–AI interaction. Preserve stable package ID, production ID, ZIP filename and release locator. Advance the internal version and paired living mother as accepted changes are incorporated. Each material advance follows capture → IN/OUT → EVT/time → CURRENT → validation → master/package reconciliation → tests → same-identity rebuild → fresh receipt/SHA → read-back. Do not silently replace historical receipts or deliver stale bytes as current.

This contract does not assert automatic capture of all conversations, background execution, foundation-model weight retraining, persistent memory or independent-host recovery. Those require separate implementation and direct evidence.


## Current paired master and event-ledger handoff
Current master version 1.7.74 and current checkpoint CURRENT-122 / POINT-0/069. The package carries the permanent interaction ledger contract and host registry schema/template. Live host connection, worker deployment and clean-host recovery remain separate gates.


## Current paired release — POINT-0/072

- Living master: 1.7.79
- Current chain: POINT-0/072 → IN-115 → OUT-114 → EVT-0290 → TIME-BINDING-EVT-0290 → CURRENT-125 → NEXT-051
- Package source target: 0.4.4 under the unchanged stable package ID and canonical ZIP filename.
- NEXT-051 remains the sole active queue.
- Release is current only when its exact source SHA, receipt and archive checks match the repository revision used for the build. Host recovery remains distinct.
