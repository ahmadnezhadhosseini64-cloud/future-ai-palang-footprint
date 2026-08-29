# Execution Claim Integrity

No operation may be reported as executed, registered, synchronized, tested, or verified without retrievable evidence for that exact operation.

Access is not execution. Intent is not execution. A workflow definition is not execution. A created file is not proof that a workflow ran. A successful write is not proof of read-back verification.

Required sequence:

TRACE -> EXECUTE -> EVIDENCE -> VERIFY -> CLAIM

If evidence is absent, the state must remain UNVERIFIED, PENDING, BLOCKED, FAILED, or NOT_PROVEN as applicable.
