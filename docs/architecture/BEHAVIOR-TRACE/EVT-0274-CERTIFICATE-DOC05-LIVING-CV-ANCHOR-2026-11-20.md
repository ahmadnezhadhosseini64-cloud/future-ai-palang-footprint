# EVT-0274 — Certificate Project: Version 5 Living CV and Point 0.0 Anchor

- Trace ID: `EVT-0274`
- Project event: `CERT-EVT-20261120-001`
- User input: `CERT-IN-20261120-001`
- Assistant output: `CERT-OUT-20261120-001`
- Recovery anchor: `CERT-POINT-0.0-20261120-002`
- Domain: Certificate project child branch; this record does not replace the Palang root architecture.

## Observed user rule
The user explicitly set the current rewritten fifth document as the latest Version 5. Documents 1–4 must remain fixed and unchanged. Document 5 alone remains mutable, registered as the latest version but still open for future updates. The user also requires automatic repository registration, temporal anchoring, and a restart point so work resumes without repeating instructions.

## Resulting state
- Documents 1–4: LOCKED / FIXED.
- Document 5: ACTIVE / LIVING, Version 5 latest, editable only through explicit approval workflow; not final.
- Latest fifth-document blob: `9c2adef6cb3b532a5b7b625cff4028b8686da49f`.
- Four-document aggregate blob: `b84f320a0c09e9079e1d33bab2ef5e5d51db8e94`.
- Point 0.0 anchor: `CERT-POINT-0.0-20261120-002`.

## Required continuation behavior
Read the living master and the latest 0.0 anchor from the repository, read the four locked documents and the latest fifth document, and continue from the exact open state. Never treat registration as final approval. Never modify documents 1–4 without explicit user authorization.

## Trace chain
`CERT-IN-20261120-001` → `CERT-OUT-20261120-001` → `CERT-EVT-20261120-001` → `CERT-POINT-0.0-20261120-002` → certificate living master.

Timestamp policy: use actual Git commit metadata for repository timestamps; do not invent message-receipt times.
