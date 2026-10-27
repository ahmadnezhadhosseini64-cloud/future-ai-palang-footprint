# CURRENT-094 — Starter ZIP in-place update checkpoint

- Root: [POINT-0/044](./GPT6-RAHM-USER-POINT-0-20261027-044-STARTER-ZIP-INPLACE-UPDATE.md)
- Chain: POINT-0/044 → IN-082 → OUT-081 → EVT-0219 → CURRENT-094 → NEXT-051
- Existing package line: `prototype/haif-gpt6-starter/`, stable IDs preserved, source currently v0.3.1.
- Canonical archive filename to replace/refresh: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip` (legacy filename retained deliberately; not a separate version ZIP).
- Build workflow: must build this archive from the existing starter source directory and upload it with the same artifact name.
- Completed: registered point/input/output/event/checkpoint; documented distinction between source update and actual ZIP update.
- Pending: workflow execution, ZIP size/hash receipt, artifact inspection and download/read-back.
- Independent-host import, negative controls in the actual AI host, and restart persistence: NOT RUN.
- NEXT-051 remains the only active queue. No NEXT-052.
- Status: OPEN / LIVING / NOT COMPLETE.
