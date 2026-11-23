#!/usr/bin/env python3
"""Retired adapter: external hosts must never push directly into private RAHM."""
from __future__ import annotations

import argparse
import sys


DISABLED_CODE = 4
DISABLED_MESSAGE = (
    "DISABLED_BY_POINT_0_GOLDEN: direct host-to-RAHM ingestion is forbidden. "
    "Return an evidence export to the owner for quarantine and review."
)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Retired. Direct host-to-RAHM push is forbidden."
    )
    parser.add_argument("--source", help="Legacy argument; no file is read")
    parser.add_argument("--url", help="Legacy argument; no network request is made")
    parser.add_argument("--host-id", help="Legacy argument; no host identity is accepted")
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.parse_args(argv)
    print(DISABLED_MESSAGE, file=sys.stderr)
    return DISABLED_CODE


if __name__ == "__main__":
    raise SystemExit(main())
