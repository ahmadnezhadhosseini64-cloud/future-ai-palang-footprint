# IN-123 — تأیید مالک برای رفع ناسازگاری CI با حفظ سابقه

- Stable ID: HAIF-IN-123-CI-MISMATCH-PRESERVATION-2026-11-21-001
- Status: ACTIVE / LIVING / OWNER-AUTHORIZED
- Parent: CURRENT-132
- Root: POINT-0/077 (0++)
- Sole queue: NEXT-051
- Related event: EVT-0299
- PR: #64

## User instruction

«ناسازگاری در نخستین اجرای رو تایید منو داری حلش کن مشکلی نداره اما قبلی رو هم نگهدار پاک نشه ناسازگاری هم و زنجیره بده بهش»

## Authorized scope

The owner explicitly authorizes fixing the CI inconsistency. The failed run, original assertion, logs and historical state must remain preserved as immutable evidence. Do not rewrite the failed run as a success or delete the prior checkpoint. Link the failure, diagnosis, correction and subsequent verification in one continuous chain.

## Known failure

The starter package's test expected an older CURRENT checkpoint while the starter README/instructions had advanced. GitHub Actions captured the original failure; the exact failed run IDs and assertion are referenced in EVT-0299 and retained in Actions history.

## Constraint

The approval covers repairing the test/package lineage and documenting it on the existing feature branch/PR. It does not authorize merging PR #64 or changing main.
