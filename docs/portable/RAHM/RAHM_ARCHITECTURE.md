# RAHM_ARCHITECTURE — portable architecture contract
Version 1.0.0 | Package ID: HAIF-RAHM-PORTABLE-20261024-001

## Layers
1. MASTER: canonical rules, identities, versions, lineage, acceptance and promotion.
2. RAHM: bounded lab for observing interaction behavior, generating hypotheses and testing candidate changes.
3. EVIDENCE LEDGER: additive record of inputs, outputs, events, sources, timestamps, tests, failures and corrections.
4. HOST ADAPTER: capability declaration for memory, tools, filesystem/repository access, scheduling, background execution and export.
5. CHILD CANDIDATE: versioned package with provenance, acceptance evidence, limitations and rollback.
6. EXPORT/RECOVERY: self-contained files reconstructable without hidden history.

## Two separate persistence planes
A. Durable artifact persistence: repository/object store/filesystem readable by identifier/version.
B. Host conversational memory: host-managed memory with its own scope, retention, deletion and retrieval rules.
Neither implies the other. Repository file ≠ proof of host memory; host memory ≠ complete archive.

## Background execution is separate
Prompt response capability does not imply an always-on agent. Background execution requires an actual scheduler/agent/job runner, permissions, durable state, execution logs, failure/retry behavior and stop/revoke controls. If absent or untested, no always-on claim.

## Capability proof ladder
DECLARED → CONFIGURED → EXECUTION OBSERVED → RESTART/IDLE TEST PASSED → INDEPENDENT READ-BACK → ACCEPTED.
Persistent memory proof: write a unique marker, cross a session boundary/restart, retrieve by key, compare and retain receipts.
Idle-background proof: schedule a permitted job, leave user interaction inactive, verify timestamped execution and durable output, then independently read back.
Never skip a rung.

Failure handling: missing access, failed writes, broken links, duplicate IDs, partial imports, contradictory records and unavailable tools create explicit open gates.