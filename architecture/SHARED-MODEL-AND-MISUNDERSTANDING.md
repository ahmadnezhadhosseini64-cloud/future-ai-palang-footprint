# Shared Model and Misunderstanding Layer

- ID: SMML-2026-08-31-001
- Status: ACTIVE / LIVING / PERMANENT
- Reference: 0.0

## Purpose
Create an explicit bridge between what the Human said, what AI interpreted, what both currently agree is understood, and what remains uncertain.

## Model
MESSAGE → INTERPRETATION → INTENT HYPOTHESIS → CONFIRMATION / CORRECTION → SHARED UNDERSTANDING

## Misunderstanding Record
When a correction occurs, preserve:
- original interpretation
- corrected interpretation
- source of correction
- ambiguity or cause
- resolution
- whether the correction generalizes

## Shared Model State
Each important project/task state may be represented as:
- AGREED
- AI-INTERPRETED / HUMAN-UNCONFIRMED
- HUMAN-CORRECTED
- DISPUTED
- UNKNOWN

## Rule
Do not silently convert an AI interpretation into shared truth. Important assumptions must remain distinguishable from confirmed shared understanding.

## Integration
Feeds the Interaction Learning Loop, Human–AI Evolution Record, Retrieval, Provenance, Evidence, and future Transfer Tests.
