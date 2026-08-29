# Operational Rule — Checkpoint Command

ID: OP-CHECKPOINT-2026-08-29-001
Title: Checkpoint Command — Preserve and Resume Interaction State
Status: ACTIVE / OPERATIONAL RULE
Version: 1.0
Date: 2026-08-29
Owner/Author: Ahmad Nezhadhosseini
Origin: Long-term human–AI interaction
Origin Location: Gonbad-e Kavus, Iran
Reference: 0.0

## Command

When the project owner says: «Checkpoint بگیر» or «دارم میرم، Checkpoint بگیر», capture the current project and interaction state so the work can later resume from this point.

## Required Cycle

Capture current state → assign checkpoint ID → document → place in the appropriate project structure → register in Repository → retrieve from Repository → verify → report completion.

## Minimum State

Where applicable, preserve:
- current architecture baseline
- confirmed decisions
- active artifacts
- proposed/open ideas
- unresolved questions
- important successes and failures
- relevant evidence and references
- exact resume point / next step
- provenance and version metadata

## Separation

A Checkpoint is not a replacement for an Artifact and is not merely a raw chat transcript. It is a recoverable state snapshot that references independently registered artifacts.

## Resume Command

When the owner says «از آخرین Checkpoint ادامه بده», retrieve and verify the latest applicable checkpoint before continuing.

## Integrity Rule

A completed checkpoint must not be silently overwritten. A later state is represented by a new checkpoint.

## Human Approval

This operational rule was explicitly approved by the project owner through the instruction: «ثبت کن».
