#!/usr/bin/env python3
"""Deprecated legacy GitHub intake worker.

Fail-closed by design. Hosts must never hold GitHub write credentials or write to
the canonical master repository. The old host-intake branch is frozen. The only
supported future path is owner export into private RAHM and a bot-authored PR.
No GitHub API request or write is attempted by this legacy worker.
"""


def main() -> int:
    print("BLOCKED: LEGACY_DIRECT_GITHUB_WORKER_DISABLED")
    print("NO_GITHUB_WRITE_ATTEMPTED")
    print("USE_OWNER_EXPORT_TO_PRIVATE_RAHM")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
