# EVT-0277 — Certificate Introduction Reference Anchor

- Trace ID: `EVT-0277`
- Stable ID: `PALANG-CERTIFICATE-INTRO-REFERENCE-ANCHOR-2026-11-20`
- Project event: `CERT-EVT-20261120-002`
- Input: `CERT-IN-20261120-002`
- Output: `CERT-OUT-20261120-002`
- Child anchor: `CERT-POINT-0PLUS-20261120-002`
- Baseline ID: `CERT-INTRO-BASELINE-20261120-001`
- Parent certificate checkpoint: `CERT-POINT-0.0-20261120-002`
- Domain: Certificate project child branch; this trace does not replace global Palang root POINT-0/064, CURRENT-115 or NEXT-051.
- Status: ACTIVE / LIVING / OPEN — behavioral observation registered; promotion to HAIF-wide rule pending review.

## Observed user behavior and explicit constraint
The user designated the exact introduction-letter text in the input record as the permanent comparison baseline. The user explicitly prohibited assistant-initiated edits and reserved all change decisions to the user. Subsequent candidate texts must be compared against the exact baseline, with differences reported rather than silently normalized.

## Behavior pattern captured
1. User establishes a reference artifact and freezes it as the comparison baseline.
2. User requires persistent temporal anchoring and continuity across conversations/hosts.
3. User requires every relevant input and output to receive identifiers and be connected to the project graph.
4. Assistant must distinguish suggestions from approved changes and preserve the original baseline.
5. Repository registration, content approval, finalization and independent recovery are separate states and must not be conflated.

## Architectural learning hypothesis
This interaction is evidence for a candidate HAIF behavior: user-controlled immutable baselines with append-only version evolution and explicit approval gates. It is an observation, not yet a universal rule. Any promotion to the master architecture requires cross-case validation and an explicit governance decision.

## Trace chain
`CERT-IN-20261120-002` → `CERT-OUT-20261120-002` → `CERT-EVT-20261120-002` → `CERT-POINT-0PLUS-20261120-002` → this trace → Behavior Trace README / Reference Index → certificate living master.

## Timestamp policy
- User-message time reference: 2026-11-20T10:51+03:30; seconds unknown.
- UTC equivalent: 2026-11-20T07:21Z; seconds unknown.
- These are conversation time references, not Git timestamps.
- Git author/committer times for each artifact must be retrieved from commit metadata after the write.
