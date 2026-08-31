# Universal Rule Inheritance & Invocation Gate

**Project:** Future AI / Palang Footprint  
**Protocol ID:** URIG-2026-08-31-001  
**Status:** ACTIVE / LIVING / PERMANENT  
**Version:** 1.0  
**Reference Point:** 0.0  
**Owner:** Ahmad Nezhadhosseini  
**Location:** Iran, Gonbad-e Kavus

## 1. Purpose

Prevent the gap between a rule existing in the archive and that rule being executed when the relevant command, production, transition, or document is actually invoked.

## 2. Core Rule

> **A governing rule is not operationally inherited merely because it exists in documentation. Every applicable production and command must pass through rule-resolution and invocation gates before execution is treated as complete.**

## 3. Inheritance

All active canonical rules, protocols, principles, metadata requirements, provenance requirements, registration gates, verification gates, recovery rules, and command-specific requirements apply automatically to every new production to which they are applicable.

The user must not have to restate a governing rule for every new production.

The short command `ثبت کن` means: resolve and apply all applicable governing rules, then execute the traceable registration workflow.

The command `0.0` means: retrieve the canonical 0.0 reference first, create the required timestamped connection/checkpoint record, resolve applicable rules, and only then continue.

## 4. Rule Resolution Gate

Before executing a formal production or command:

1. Identify the production/command type.
2. Retrieve the applicable canonical rule set when required by the architecture.
3. Resolve inherited rules and required fields.
4. Construct the execution record with those requirements.
5. Execute.
6. Verify that the required rule-derived fields/actions actually occurred.

If an applicable rule cannot be resolved, the system must not silently omit it. The production enters `BLOCKED / RULE-RESOLUTION-REQUIRED` or another explicit unresolved state.

## 5. Invocation Verification Gate

A rule is not considered operationally validated because it was found in an archive or because a document says it is mandatory.

Operational validation requires a real invocation test in which:

**Trigger → Rule Resolution → Required Action/Field → Execution → Evidence → Read-back → Comparison → PASS/FAIL**

A failed test does not invalidate the rule; it identifies an execution gap that must be corrected and retested.

## 6. 0.0 Mandatory Timestamp Gate

Every invocation of `0.0` must produce, at minimum:

- 0.0 ID
- Date
- Exact local time
- IANA timezone name and UTC offset
- Country/city and location-status (`VERIFIED`, `ESTIMATED`, or `UNVERIFIED`)
- Previous 0.0/checkpoint/reference, when applicable
- Current state
- Continuation Anchor
- Rule-resolution status
- Verification status

A `0.0` record missing Date, Exact Local Time, or Timezone is **INCOMPLETE** and cannot be marked `VERIFIED` or `COMPLETE`.

## 7. Production/Document Inheritance Gate

For every new rule, command, principle, protocol, architecture element, document, checkpoint, test, evidence record, production, recovery record, or other formal artifact, the Universal Metadata & Provenance rule and all other applicable canonical rules must be resolved before final registration.

Required fields may be `N/A` only when genuinely inapplicable. Omission caused by failure to resolve the rule is not equivalent to `N/A`.

## 8. Evidence Boundary

The existence of this protocol proves only that the execution architecture has been specified. It does not prove that every future invocation will succeed.

Each critical command family must therefore have an actual invocation test and recoverable evidence. Repeated failures are execution defects, not reasons to silently weaken the rule.

## 9. Regression Requirement

Whenever a new architecture rule is added or an execution gate is changed, at least one representative real invocation must be run to verify that inherited requirements are still being applied.

For `0.0`, the regression test must explicitly inspect the produced record for Date + Exact Local Time + Timezone and verify those fields by read-back.

## 10. No False Completion

`RULE EXISTS` ≠ `RULE INVOKED` ≠ `RULE VERIFIED`.

Only the final state supported by execution evidence and read-back may be reported as operationally validated.

## 11. Continuation

Failures preserve the same Production/Test ID and exact continuation path. No duplicate test record is created merely because the first invocation failed.

## 12. Language

Human-facing canonical copies are presented Persian-first and English-second. Technical identifiers remain stable.
