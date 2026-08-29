# No Silent Pending Loss

A pending registration is durable until verified reconciliation. It must not disappear because of retry failure, interruption, process restart, or temporary destination unavailability.

Every new registration trigger must include a pending-drain pass. Scheduled reconciliation must also include a pending-drain pass.

No user reminder is required to preserve or retry already-pending work.
