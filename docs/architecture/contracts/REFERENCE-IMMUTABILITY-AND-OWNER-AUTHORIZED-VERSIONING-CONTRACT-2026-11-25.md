# REFERENCE IMMUTABILITY & OWNER-AUTHORIZED VERSIONING CONTRACT

- Contract ID: HAIF-REFERENCE-IMMUTABILITY-CONTRACT-2026-11-25-001
- Status: PROPOSED / OWNER-REVIEW BRANCH
- Applies: all reference texts, documents, letters, records, templates, and artifacts explicitly designated by their owner as canonical, fixed, locked, or reference.
- Trigger lesson: repeated unauthorized broad rewrites after owner-requested narrow edits.

## 1. Absolute preservation rule

When an owner marks content as a reference, the assistant must preserve the reference text exactly. This includes wording, order, paragraph boundaries, punctuation, numbers, dates, whitespace/formatting when practically represented, headings, lists, and every section.

The assistant must not silently or proactively rewrite, polish, normalize, harmonize, summarize, translate, restructure, correct, improve, or alter any part of the reference. No change is allowed merely because it appears beneficial, inconsistent, outdated, awkward, repetitive, or stylistically weaker.

## 2. Permission boundary

A change is permitted only when the owner gives a clear instruction to change the reference, or explicitly asks for a proposed change and subsequently approves that exact proposal.

Approval is scoped to the specified item(s) and change(s). Approval of one edit is not permission to change adjacent wording, paragraphs, formatting, or other content. Silence, general praise, or approval of a document as a whole does not authorize unrelated edits.

## 3. Reference versus derived revision

The canonical reference remains immutable. Any requested change produces a separate derived version. It does not overwrite, replace, or retroactively alter the reference.

Version convention:
- Document 1 reference: 1.00; first authorized derivative: 1.01; next authorized derivative: 1.02, etc.
- Document 2 reference: 2.00; first authorized derivative: 2.01; next authorized derivative: 2.02, etc.
- Document 3 reference: 3.00; first authorized derivative: 3.01; etc.
- Document 4 reference: 4.00; first authorized derivative: 4.01; etc.

The decimal part increments for each distinct owner-authorized revision of that document. A request to create a new letter from the reference is a new derived artifact, not a revision of the reference, unless the owner expressly directs it to be a revision.

## 4. Narrow-edit protocol

For every requested reference edit:
1. Identify the exact reference and its version / source hash.
2. Restate or mark the exact requested change(s) only.
3. Apply only those authorized changes in a separate derivative.
4. Compare the derivative against the reference.
5. Produce a change report listing every difference.
6. Verify that every difference is authorized and that no other content changed.
7. If any unintended difference is detected, reject the derivative and rebuild; do not deliver it as compliant.
8. Preserve the source reference unchanged.

For a request such as “change only the Gregorian date,” only the date field(s) explicitly identified may differ. No related date, duration, prose, translation, layout, or other field may be changed unless separately authorized.

## 5. Suggestions

If the assistant notices a potential improvement or inconsistency, it may mention it separately only when relevant and must not implement it. The suggestion is not an edit. Implementation requires the owner's explicit approval of the exact proposed change.

## 6. Output behavior

When the owner requests a letter based on one or more references, deliver the requested letter/artifact first. Do not replace it with an architecture report. Any architecture lesson is recorded separately and reported succinctly when relevant.

## 7. Lock status and unlocking

A locked reference stays locked indefinitely until the owner explicitly unlocks or authorizes a change to that exact reference. The owner can authorize an isolated derivative while keeping the reference locked; this is the default and safest path.

## 8. Proof / audit fields

For each derivative, record: source document ID/version, source blob hash or exact reference, derivative version, owner instruction, authorized change scope, diff result, verification result, and status. No claim of exact preservation is made without a comparison.

## 9. Application to the four employment-certificate documents

Four references remain individually locked:
- Document 1 — Persian Employment Certificate: reference 1.00; derivatives 1.01, 1.02…
- Document 2 — Bilingual Employment Certificate: reference 2.00; derivatives 2.01, 2.02…
- Document 3 — Service History & Duties Summary v03: reference 3.00; derivatives 3.01, 3.02…
- Document 4 — Employment Certificate Request Letter v02: reference 4.00; derivatives 4.01, 4.02…

No document is altered by registering this contract. The reference aggregate and four texts remain unchanged.

## 10. Chain and integration

This is an additive architecture proposal under the existing POINT-0/GOLDEN root and existing sole queue NEXT-051. It must not create a parallel root or queue. Main-branch status remains unchanged until owner review and merge.
