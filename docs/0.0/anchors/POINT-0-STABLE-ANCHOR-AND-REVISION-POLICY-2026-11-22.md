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

