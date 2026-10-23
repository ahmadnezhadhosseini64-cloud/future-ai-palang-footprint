# Controlled rollback test candidate — INT-20261023-020

- Test ID: ROLLBACK-TEST-INT-20261023-020
- Type: ISOLATED GIT REF ROLLBACK / NON-PRODUCTION BRANCH
- Baseline commit: beebca722fe52d1d628ecfad85dc480ee18a4d16
- Purpose: create a clearly marked test-only successor on an isolated branch, preserve that candidate on an evidence branch, then restore the test branch ref to the named baseline and verify both the restored state and preserved candidate.
- This file is intentionally a simulated failed successor; it is not a production architecture rule and must not be merged into main.
- Expected rollback result: test branch points to baseline and this file is absent there; evidence branch retains this file and the candidate commit remains retrievable.
