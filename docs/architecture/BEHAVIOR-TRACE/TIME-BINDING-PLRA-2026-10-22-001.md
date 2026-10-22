# Time Binding — PLRA-2026-10-22-001

- Stable ID: `TIME-BINDING-PLRA-2026-10-22-001`
- Production ID: `TB-PLRA-2026-10-22-001`
- Purpose: bind repository registration timestamps to the independent anchors and living master reference.
- Canonical rule: actual GitHub repository commit time in UTC is authoritative; Asia/Tehran time is derived from the same instant (+03:30).

## Registered commits

| Item | Commit SHA | Canonical UTC | Derived Asia/Tehran |
|---|---|---|---|
| Living master reference | `f71262d861539b539e209a0e43a2bd986db8fd87` | 2026-10-22T13:37:39Z | 2026-10-22T17:07:39+03:30 |
| Independent input anchor IN-20261022-007 | `4eb874e56cedc2220c0ecc2200b4a8f1fee100b0` | 2026-10-22T13:37:44Z | 2026-10-22T17:07:44+03:30 |
| Independent output anchor OUT-20261022-007 | `8795b25a16238fb3320c97919efccb7dd669e422` | 2026-10-22T13:37:47Z | 2026-10-22T17:07:47+03:30 |

## References

- Master: `docs/reference/REFERENCE-DOCUMENTS/PALANG-LIVING-REGISTRATION-AND-ANCHORING-MASTER-REFERENCE-2026-10-22-001.md`
- Input: `docs/0.0/anchors/PALANG-0.0-IN-20261022-007-LIVING-REGISTRATION.md`
- Output: `docs/0.0/anchors/PALANG-0.0-OUT-20261022-007-LIVING-REGISTRATION.md`

## Verification status

The three files were fetched from the default branch after creation. Their expected IDs, paths, and contents were present. This binding is itself a separate registration; its own commit timestamp must be retrieved and read back after creation. This is repository evidence only and does not verify Buffer, Persistent Memory, Dropbox, or background execution.
