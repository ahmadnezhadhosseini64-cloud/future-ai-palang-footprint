# Universal AI Host Connectivity Contract

- Stable ID: UNIVERSAL-AI-HOST-CONNECTIVITY-CONTRACT-2026-11-21-001
- Status: IMPLEMENTATION CANDIDATE / ACTIVE ON FEATURE BRANCH
- Parent: POINT-0/077 (0++) / CURRENT-130
- Governing continuation: NEXT-051 only
- Canonical repository: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint

## Purpose
A durable, provider-neutral entry and recovery contract lets a zero-state AI host discover its actual capabilities, obtain owner-authorized repository access through the destination's official authorization UI, recover HAIF from canonical evidence, and continue without prior chat history.

This is a reusable capability protocol, not a promise that every host exposes GitHub OAuth, shell execution, persistent workspace, background execution, or write access. Each host declares and proves only capabilities available in its own session.

## Identity and trust boundary
- The text handshake «احمد نژادحسینی» is a human-readable session-start identifier only.
- It is not a password, authentication factor, OAuth grant, ownership proof, token, or permission.
- Owner approval to begin setup does not replace secure authorization in the destination host.
- The owner completes OAuth / connector authorization in the official UI of that destination session.
- Never request, print, commit, export, or persist passwords, PATs, OAuth access/refresh tokens, cookies, OTPs, private keys, or recovery codes.
- Persist non-secret evidence only: provider/host labels, capability states, repository identity, branch/commit identifiers, test outcomes, timestamps with source, and receipt hashes.
- READ, EXECUTE, and WRITE are separate. WRITE is branch-scoped; main changes only through an owner-reviewed Pull Request.

## Required lifecycle
1. HANDSHAKE: receive the text identifier and owner intent; do not treat either as authentication.
2. CAPABILITY_DISCOVERY: inspect actual connector, repository, execution, file, and persistence capabilities.
3. AUTHORIZATION: if GitHub is not securely connected, ask the owner to complete official OAuth/connector authorization in this destination session.
4. REPOSITORY_BINDING: verify exact repository and default branch; record observed HEAD SHA.
5. SOURCE_RECOVERY: read Reference Index, living mother reference, current 0++ anchor, sole active NEXT-051 queue, and this host contract/bootstrap.
6. WORKSPACE: create or identify a real isolated checkout only if the host exposes that capability.
7. EXECUTION: run prescribed tests only in an actual execution facility; record exact commands, exit status, tested SHA, and inspectable logs.
8. WRITE_GATE: only when permissions allow, create a dedicated feature branch. Never push directly to main.
9. READ_BACK: re-read every changed path and compare it with intended content/hash. A write response alone is not acceptance.
10. RECEIPT: produce a schema-valid, secret-free host receipt and mark each stage independently.
11. CONTINUATION: resume NEXT-051 only. Do not create NEXT-052, a parallel project, or silently resolve historical ambiguities.

## Capability model
Each capability is AVAILABLE, UNAVAILABLE, or NOT_CHECKED, with evidence:
- github_repository_read
- github_oauth_or_connector_authorization
- isolated_workspace
- command_execution
- branch_scoped_write
- pull_request_creation
- artifact_download_upload
- durable_session_or_workspace_persistence

Availability may differ by provider and session. No universal capability is assumed.

## Acceptance levels
- SOURCE-RECOVERED: canonical source documents and exact repository identity/HEAD were read.
- PACKAGE-VERIFIED: portable package integrity and prescribed package tests passed for the exact source SHA.
- WORKSPACE-RECOVERED: an actual isolated destination checkout exists and its HEAD is recorded.
- EXECUTION-VERIFIED: commands ran in that workspace and exit status/logs are inspectable.
- HOST-RECOVERED: required source/workspace/execution checks passed, a receipt was read back, and restart persistence was tested where claimed.

These levels are not interchangeable. Repository CI does not prove a real independent AI-host test.

## Connection ledger
The adjacent JSON Schema defines one host/session receipt. A receipt is evidence, not a reusable credential. Persist only non-secret receipts or references; never store OAuth secrets or imply authorization transfers to another host.

## Failure and recovery
- OAuth unavailable: stop at AUTHORIZATION=UNAVAILABLE; do not claim connected.
- Repository READ unavailable: stop before source recovery.
- EXECUTE unavailable: tests are NOT RUN, not passed.
- WRITE unavailable: report read-only recovery; branch/PR remain NOT CREATED.
- Read-back mismatch: mark RECONCILIATION_REQUIRED and do not open a PR.
- Secret-like receipt content: reject; do not commit it.
- Preserve unresolved findings and NEXT-051 scope.

## Implementation artifacts
- host-capability-receipt.schema.json
- prototype/universal-ai-host/README.md
- prototype/universal-ai-host/host_receipt.py
- prototype/universal-ai-host/tests/test_host_receipt.py

## Acceptance gate
Accept only after schema/validator tests pass, feature-branch files are re-read and match, CI is inspected on the resulting branch SHA, a PR is opened against main, and owner review/merge is completed. An actual fresh destination host must return direct evidence before HOST-RECOVERED is claimed.

This contract establishes a permanent protocol and testable local validator. It does not create an external AI session, authorize OAuth, or prove independent-host recovery.
