# OUT-133 — Stable anchor identity design and execution decision

- Stable ID: OUT-133
- Input: IN-134
- Root: POINT-0 / POINT-0/GOLDEN
- Stable current identity: CURRENT-150
- Sole stable queue identity: NEXT-051
- Status: REGISTERED / LIVING / CANDIDATE

## Decision

Adopt fixed identities with append-only revisions:
- POINT-0/GOLDEN is the permanent logical baseline identity; every claim about a tested baseline still names an exact commit SHA.
- CURRENT-150 is the permanent current-anchor family; revisions are CURRENT-150.01, CURRENT-150.02, etc.
- NEXT-051 is the permanent sole queue; revisions are NEXT-051.01, NEXT-051.02, etc.

No ordinary change may create CURRENT-151, NEXT-052, another root or a parallel queue. Existing CURRENT-151 is not deleted or renumbered: it is preserved as a transition snapshot whose findings and evidence are incorporated into CURRENT-150.01. Its old "current" claim is historical as of the transition; the new resolver and global registries point to CURRENT-150.01.

## Technical determinations

1. Never downgrade the Golden living mother to satisfy a stale package pin. The mother is authoritative; package manifest, portable mirror and tests must synchronize to it.
2. CURRENT-065 and CURRENT-066 remain preserved. The overlay manifest's legacy filename and its internal CURRENT-066 identity are scoped as historical overlay evidence; global project continuation is a separate scope. Do not choose by numeric order.
3. Buffer and Dropbox are WAITING / DEFERRED / NON-BLOCKING. Do not build or provision them unless a concrete continuity requirement demonstrates a need that the canonical repository and owner-controlled export cannot meet more simply.
4. Issue #20 remains OPEN / PARTIALLY IMPLEMENTED: stable INT/IN/OUT IDs, schema validation, reverse lookup and local runtime tests exist, but automatic host capture and independent clean-host recovery are not proven.
5. Issue #21 remains OPEN / PARTIAL CENSUS: the repository tree and initial source families are mapped, but full semantic source census, all collision/parent-edge adjudication and exact final-head closure remain outstanding.
6. Partner Issues #114–#123 remain ten independent OPEN execution dossiers under NEXT-051.
7. MASTER stays read-only for hosts; no direct/indirect host write, bypass, auto-merge or secret exposure. Owner approval remains required for promotion.

## Acceptance boundary

This decision becomes ACTIVE only after the candidate policy, CURRENT-150.01, NEXT-051.01, living mother, portable reference and canonical indexes are merged to POINT-0/GOLDEN and read back; exact-SHA audit and portable conformance must pass. External-host and service gates remain separate and OPEN.
