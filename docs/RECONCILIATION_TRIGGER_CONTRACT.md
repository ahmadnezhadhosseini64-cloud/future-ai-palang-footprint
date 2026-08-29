# Reconciliation Trigger Contract

Every registration event and every scheduled reconciliation run MUST inspect eligible pending registrations. No manual reminder is required for already-pending work.

Triggers:
- registration event
- repository capability recovery/event
- scheduled reconciliation
- explicit recovery/bootstrap

Each trigger must record its own execution evidence. Trigger existence does not prove successful reconciliation.
