# OUT-085 — اصلاح گردش‌کار ZIP موجود

- Stable ID: HAIF-OUT-085-SAME-ZIP-READBACK-20261027
- Production ID: G6IP-OUT-085
- Version: 1.0.0
- Status: IMPLEMENTATION COMMITTED / CI RESULT PENDING
- Parent: [IN-086](./PALANG-0.0-IN-20261027-086-SAME-ZIP-READBACK-AND-CONTINUOUS-UPDATE.md)
- Root marker: [POINT-0/048 (0+)](./GPT6-RAHM-USER-POINT-0-20261027-048-SAME-ZIP-READBACK-AND-CONTINUOUS-UPDATE.md)
- Next checkpoint: [CURRENT-098](./PALANG-0.0-CURRENT-20261027-098-SAME-ZIP-READBACK-AND-CONTINUOUS-UPDATE.md)

## Implementation
1. Preserved stable package identity `HAIF-GPT6-PORTABLE-STARTER-20261025-004`.
2. Preserved canonical archive filename `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`.
3. Kept package internal version 0.3.3; workflow hardening does not change package source bytes or falsely claim a new product version.
4. Added clean extraction, byte-for-byte source comparison and execution of package tests from extracted ZIP.
5. The run on fix commit `08155ef02f30533558b2396848e9772621b865ba` is queued; final pass/fail, new digest and artifact read-back must be inspected before closure.

Real independent-host import, negative controls at that host, independent reconstruction from IN/OUT and restart persistence remain OPEN / NOT VERIFIED.
