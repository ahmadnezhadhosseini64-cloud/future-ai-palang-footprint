# EVT-0318 — درس بازیابی عمیق، جلوگیری از false-negative و حفظ مرجع

- Event ID: EVT-0318
- Status: ACTIVE / LIVING / OWNER-REVIEW-PENDING
- Canonical root: POINT-0/GOLDEN
- Parent checkpoint: CURRENT-145
- Input: IN-131
- Output: OUT-130
- Proposed checkpoint: CURRENT-146
- Sole active queue: NEXT-051

## Trigger and observed failure

در پروژهٔ فرعی گواهی سابقه کار، دور اول بازیابی فقط دو سند از چهار سند مورد انتظار را گزارش کرد. مالک یادآوری کرد که هر چهار سند در تعامل قبلی بازیابی و به‌عنوان مرجع قفل‌شده ثبت شده بودند. جست‌وجوی عمیق‌تر، فایل تجمیعی canonical و سند مادر حاکم بر پروژهٔ گواهی را پیدا کرد. بنابراین گزارش اولیه یک false-negative ناشی از بازیابی ناقص بود، نه شاهدی بر نبودن دو سند دیگر.

## Verified source evidence

- Canonical aggregate: گواهی/شروع-جدید-۳۰-آبان-۱۴۰۵/چهار-سند-یکپارچه-۳۰-آبان-۱۴۰۵.md
- Aggregate Blob SHA: b84f320a0c09e9079e1d33bab2ef5e5d51db8e94
- Governing certificate master: گواهی/شروع-جدید-۳۰-آبان-۱۴۰۵/سند-مادر-زنده-و-قرارداد-دائمی-پروژه-گواهی.md
- Master Blob SHA at read-back: 971f2250e1079362896620aa688454201df2dead
- Governing certificate point: CERT-POINT-0.0-20261120-002
- Four documents are declared fixed/LOCKED; document 5 is the only ordinarily mutable document in that certificate workflow.

## Permanent architecture lesson

Adopt OUT-130's Retrieval Ladder and proof sequence. A partial search is an intermediate state, never a final absence claim. Every retrieval report must distinguish candidates, confirmed reads, complete set coverage, and unresolved gaps. The agent must correct a false-negative when deeper search finds the source and preserve the exact source provenance.

## Scope and non-effects

- This event is an additive child continuation on the existing POINT-0/GOLDEN root.
- It does not create a parallel root or queue; NEXT-051 remains the only queue.
- It does not change any of the four locked employment-certificate documents.
- It does not claim the lesson is merged into main until owner review and merge are complete.
- The date audit found the bilingual document's displayed Gregorian range (21 November 2020–21 November 2026) consistent with the Persian range (01/09/1399–30/08/1405); no date edit was made because no mismatch was present in the fetched canonical version.

## Verification status

- Source fetch: PASS
- Blob identity read-back: PASS
- Expected aggregate count: 4/4 sections present
- Four-document lock in certificate master: PASS
- Exact text before/after comparison for a date-only edit: NOT APPLICABLE — no date correction was needed; aggregate remained unchanged.
- Main-branch registration: PENDING owner review / PR merge.
- Independent-host recovery test: NOT RUN.
