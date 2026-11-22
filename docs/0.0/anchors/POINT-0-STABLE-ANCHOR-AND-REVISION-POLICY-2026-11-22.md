# POINT-0 Stable Anchor Identity and Append-Only Revision Policy

- Policy ID: POINT-0-STABLE-ANCHOR-REVISION-POLICY-2026-11-22-001
- Version: 1.0.0
- Status: CANDIDATE — requires exact-SHA audit and Golden merge
- Canonical root: POINT-0
- Baseline identity: POINT-0/GOLDEN
- Stable current identity: CURRENT-150
- Stable queue identity: NEXT-051

## 1. Permanent identities

The project has one canonical root, one Golden baseline identity, one stable current-anchor family and one active queue:

1. `POINT-0/GOLDEN` — permanent logical identity of the canonical baseline. Each tested state is pinned by an exact Git commit SHA and tree SHA.
2. `CURRENT-150` — permanent identity of the current-anchor family.
3. `NEXT-051` — permanent identity of the only active work queue.

These names are not counters to increment during normal work. Do not create a new root, CURRENT-151, NEXT-052, or parallel queue to represent an ordinary correction or implementation step.

## 2. Append-only revision notation

Routine updates become revisions under the stable identity:

- `CURRENT-150.01`, `CURRENT-150.02`, `CURRENT-150.03`, ...
- `NEXT-051.01`, `NEXT-051.02`, `NEXT-051.03`, ...

The unsuffixed identity is a resolver to the latest **verified** revision. It must never silently point to an untested candidate. A candidate revision becomes current only after exact-SHA acceptance and Golden merge/read-back.

Revision numbers are monotonically increasing within their own stable family. They are not Git commit counts, semantic versions, or a reason to renumber historical records.

## 3. Transition treatment of existing CURRENT-151

CURRENT-151 was already created and merged into Golden before this policy was proposed. It is immutable historical evidence and MUST NOT be deleted, rewritten, or renumbered.

Its findings and execution evidence are incorporated into the first stable-family revision, CURRENT-150.01. CURRENT-151 is therefore retained as a **transition snapshot / historical alias**, not a competing live pointer. The resolver and canonical registries move to CURRENT-150.01. The original CURRENT-151 file remains available and its former live-pointer claim is understood as true for its recorded historical moment only.

This is a one-time migration caused by the owner's request to stabilize identities. No further CURRENT-number migration is allowed for ordinary work.

## 4. NEXT-051 stays the one queue

NEXT-051 remains the sole queue. Its revision history is maintained at the top of the existing queue file as NEXT-051.01, NEXT-051.02, etc. All ten Partner dossiers (#114–#123), Issue #20, Issue #21, package correction, owner-gated promotion, source census, and any accepted future work remain attached to this same queue. No new queue is created.

## 5. Required revision receipt

Each accepted revision must record:
- stable family ID and revision suffix;
- parent revision and canonical root;
- candidate commit SHA and tree SHA;
- final Golden merge commit SHA and tree SHA;
- actual Git committer UTC; Tehran equivalent derived from that same UTC instant;
- input/output/event/time-binding references when applicable;
- changed paths and reason;
- exact workflow run IDs, tested SHA/tree, test results and artifact receipts;
- remaining OPEN gates and owner actions.

A branch name is not an immutable snapshot. Never fabricate message times, and never treat an untested candidate as the latest verified revision.

## 6. Golden / MASTER boundary

POINT-0/GOLDEN is the single logical baseline identity; its branch moves as revisions are accepted. Cite exact SHAs for reproducibility. Main remains separately governed. Hosts remain read-only on MASTER and receive no direct or indirect write route. Golden-to-main promotion requires the trusted owner-controlled process and an enforced owner-approval gate. No bypass, force-sync, auto-merge or secret exposure.

## 7. Operational simplification

- Golden living mother is the source of truth. Package manifests, portable mirrors and tests synchronize to it; never downgrade the mother to satisfy stale pins.
- CURRENT-065/CURRENT-066 remain preserved historical overlay evidence. Their scopes are resolved by lineage and role, not numeric comparison.
- Buffer and Dropbox are WAITING / DEFERRED / NON-BLOCKING and are not core acceptance dependencies.
- Issue #20 and #21 remain separate: runtime/capture/recovery versus historic source/lesson census. Local code tests do not close live-host gates.
- Partner Issues #114–#123 remain independent OPEN dossiers under NEXT-051.

**Minimal rule: keep the three identities fixed; version the evidence underneath them.**
