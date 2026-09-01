# Failure Regression Record — 0.0 Time/Location

- ID: FAILURE-REGRESSION-0.0-TIME-LOCATION-2026-09-01-001
- Reference: 0.0
- Date: 2026-09-01
- Status: ACTIVE / LIVING
- Type: Failure Case / Regression Test / Architectural Finding
- Evidence Status: VERIFIED at repository write/read-back level

## Trigger
A previously identified 0.0 time/location error was repeated: the project/user reference was Iran / Gonbad-e Kavus / Asia-Tehran, but Baku / UTC+4 was incorrectly used.

## Required Interpretation
This recurrence is not treated as an isolated mistake. It is a regression failure of the control intended to prevent recurrence.

## Required Investigation
Determine where the execution chain failed: retrieval, reference selection, rule selection, priority resolution, time-source selection, verification-before-response, or response execution.

## Required Architecture Response
Convert the failure into a reusable regression test and extract all available evidence, root-cause findings, architectural gaps, and control improvements. Do not guess missing evidence.

## Regression Test
Given a stored project reference of Iran / Gonbad-e Kavus / Asia-Tehran, the 0.0 timestamp/location output MUST NOT substitute inferred device/IP location such as Baku unless the project reference is explicitly changed and verified.

## Recovery / Living Rule
This record itself is part of the project's recoverable production chain. If any subsequent finalization or registration step fails, preserve its identity and pending state in the designated Recovery/Pending layer and include it in the scope of the "زنده‌سازی" / "خاک‌برداری و زنده‌سازی" command.

## Chain
Previous → Current → Next

Previous: Existing 0.0 time/location rule and anti-recurrence controls.
Current: Repeated time/location regression detected on 2026-09-01.
Next: Root-cause analysis → control update → regression execution → evidence verification → continued chain.
