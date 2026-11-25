# CURRENT-146 — POINT-0/GOLDEN / درس بازیابی عمیق اسناد

- Stable ID: HAIF-CURRENT-146-CERTIFICATE-RETRIEVAL-LESSON-2026-11-25
- Display label: POINT-0++
- Status: ACTIVE / LIVING / OWNER-REVIEW-PENDING
- Canonical root: POINT-0
- Canonical baseline: POINT-0/GOLDEN
- Parent: CURRENT-145
- Event: EVT-0318
- Input: IN-131
- Output: OUT-130
- Sole active queue: NEXT-051
- Owner: @ahmadnezhadhosseini64-cloud

## Decision captured

A retrieval agent must not turn an incomplete search into an absence claim. It must follow the retrieval ladder, read the canonical aggregate and governing master, search source files/history as appropriate, fetch the selected source, verify its exact ref/blob identity, compare content, count the complete expected set, and only then report FOUND / COMPLETE / NOT FOUND. If a deeper pass disproves an earlier result, explicitly correct the false-negative and record why the earlier pass was incomplete.

## Applied example — employment certificate

- Four expected documents recovered from one canonical aggregate.
- Aggregate Blob SHA: b84f320a0c09e9079e1d33bab2ef5e5d51db8e94.
- Governing master Blob SHA: 971f2250e1079362896620aa688454201df2dead.
- Documents 1–4 remain FIXED / LOCKED; only document 5 remains ordinarily mutable under its own contract.
- The Gregorian date range in the bilingual document already matched its Persian date range; no text mutation was required.

## Operational status

This checkpoint is a proposal on an owner-review branch. It is not yet the main-branch current pointer. No change is made to the sole queue NEXT-051. Main merge and independent-host adoption remain separate evidence gates.
