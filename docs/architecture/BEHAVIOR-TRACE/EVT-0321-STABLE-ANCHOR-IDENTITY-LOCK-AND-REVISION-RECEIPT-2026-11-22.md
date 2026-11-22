# EVT-0321 — Stable POINT-0 anchor identities and append-only revision lock

- Event ID: EVT-0321
- Input: [IN-134](../../0.0/anchors/PALANG-0.0-IN-20261122-134-STABLE-ANCHOR-IDENTITY-LOCK.md)
- Output: [OUT-133](../../0.0/anchors/PALANG-0.0-OUT-20261122-133-STABLE-ANCHOR-IDENTITY-LOCK.md)
- Canonical root: POINT-0
- Golden baseline: POINT-0/GOLDEN
- Stable current identity: CURRENT-150
- Sole stable queue: NEXT-051
- Status: CANDIDATE / LIVING / EXACT-SHA ACCEPTANCE PENDING

## Event

The owner requested fixed identities for POINT-0/GOLDEN, CURRENT-150 and NEXT-051, with ordinary changes recorded only as append-only revisions (CURRENT-150.01+, NEXT-051.01+). The assistant recommends and is implementing this scheme.

Existing CURRENT-151 is retained as an immutable transition checkpoint. Its evidence is incorporated into CURRENT-150.01, and the live resolver is moved back to the stable CURRENT-150 family without deleting, renumbering or falsifying the historical CURRENT-151 record.

The event also preserves these determinations:
- Golden living mother version is authoritative; package and tests must follow it.
- CURRENT-065/CURRENT-066 remain historical, explicitly scoped, and are not resolved by numeric comparison.
- Buffer and Dropbox remain WAITING / DEFERRED / NON-BLOCKING.
- Issues #20/#21 remain separate OPEN tracks; #20 has local runtime implementation but no automatic host capture or independent recovery, while #21 remains a partial semantic source census.
- Ten Partner dossiers #114–#123 remain OPEN under NEXT-051.
- MASTER promotion remains owner-controlled; hosts receive no direct or indirect write path.

## Event timestamp

The authoritative event registration time is the UTC committer timestamp of the Git commit that first created this file. See the paired TIME-BINDING record. No user-message timestamp is inferred.
