# POINT-0 Stable Anchor Identity and Revision Policy

- Policy ID: POINT-0-STABLE-ANCHOR-REVISION-POLICY-2026-11-22-001
- Revision: 1.0.0
- Status: CANDIDATE — activated only after Golden merge and exact-SHA audit
- Scope: the single canonical Future AI / Palang Footprint root

## 1. Three permanent identities

The project uses exactly one canonical root and one active continuation lane:

1. `POINT-0/GOLDEN` — permanent logical identity of the canonical Golden baseline.
2. `CURRENT-150` — permanent identity of the current continuation anchor.
3. `NEXT-051` — permanent identity of the sole active work queue.

These are stable names, not counters to be incremented during ordinary work. Do not create CURRENT-151, NEXT-052, another Golden root, or a parallel queue merely because work advances.

## 2. Revision notation

Ordinary changes create append-only revisions under the stable identity:

- `CURRENT-150.01`, `CURRENT-150.02`, ... are revisions of CURRENT-150.
- `NEXT-051.01`, `NEXT-051.02`, ... are revisions of NEXT-051.
- `POINT-0/GOLDEN` remains the stable logical baseline identity; each accepted Git commit SHA is an immutable snapshot of that baseline.

A revision changes content/evidence, not identity, parentage, or queue ownership. Never overwrite or erase a prior revision's evidence. The unsuffixed ID always resolves to the latest verified revision, with the exact SHA and UTC timestamp shown explicitly.

## 3. Required revision receipt

Every revision must record:
- stable anchor ID and sequential revision number;
- parent revision and canonical root;
- exact source commit SHA and tree SHA;
- repository commit UTC; Tehran equivalent derived from that same UTC instant;
- input/output/event/time-binding references when applicable;
- changed files and concise reason;
- validation commands/workflow run IDs and exact tested SHA;
- result and remaining OPEN gates.

Do not fabricate message timestamps or equate a branch name with an immutable snapshot.

## 4. When may the stable identity change?

Only a deliberate owner-approved architecture migration may retire or replace CURRENT-150 or NEXT-051. Such migration requires a written reason, preserved backward resolver, graph migration plan, independent audit and explicit owner approval. Normal implementation, bug fixes, research, or queue progress are revisions and MUST NOT increment the stable identity.

## 5. Golden and main boundary

`POINT-0/GOLDEN` is the one logical canonical baseline. Its branch is a moving pointer; therefore every claim about a tested Golden state must cite an exact commit SHA. Main remains separately governed and is never advanced by a host or by an automatic shortcut. Golden-to-main promotion remains subject to the trusted owner-controlled route and enforced approval gates.

## 6. Minimal operating rule

**Keep the three names fixed; version the evidence beneath them.** Use the same NEXT-051 for every remaining action. Keep all ten Partner issues and any accepted additional work attached to this queue. Do not introduce a new root or queue to represent an ordinary update.


## 7. Initial candidate validation evidence

- Candidate pull request: [#135](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/pull/135).
- Living Architecture Audit run 45023788443: SUCCESS on PR head `7589d984cdd5313c82b1ae11ec4583548d8c5cf1`.
- Portable RAHM Conformance run 45023788437: SUCCESS on the GitHub PR merge tree commit `47b2e9b10664e52ec9ecabb8d899352c2b9609f3` (parents include Golden base `669f46f2b7a12ab9809f36c0ddf69f3e5b50acf4` and PR head `7589d984cdd5313c82b1ae11ec4583548d8c5cf1`).
- Exact-byte manifest scan: 48/48 files matched; 246 live-reference files were observed.
- RAHM export archive: 295 files, 1,438,457 bytes, SHA-256 `51b9cb5f24d3b9509f37d1e0e5811f8aa845d1247636b258559cba3daf490e2a`.
- Canonical starter ZIP `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`: 281,837 bytes, SHA-256 `dd99a07c433602a902c079263f0effc532c3c93bac4e7613233b6c481f36b30c`; 19-file inventory, ZIP integrity, source-byte match, exact artifact-ID download, paired mother byte-match, and extracted 24/24 tests all PASS.
- This evidence predates later documentation/index updates in the same PR branch. It is not the final acceptance receipt for the latest PR head; rerun both workflows on the final exact head before merging and activating this policy.
- Independent real-host recovery and durable release publication remain separate OPEN gates.

