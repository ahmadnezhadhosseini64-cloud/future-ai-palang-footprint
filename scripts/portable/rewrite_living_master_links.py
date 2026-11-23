#!/usr/bin/env python3
"""Rewrite canonical living-master relative links for the portable starter mirror.

The canonical mother lives under docs/architecture/...; its relative links are
correct from that location. The portable mirror lives under prototype/... .
This tool preserves meaning by resolving each local link against the canonical
source and rewriting it relative to the mirror. Missing targets are reported
and left unchanged; no target is guessed or silently substituted.
"""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit, urlunsplit

LINK_RE = re.compile(r"(?P<prefix>\]\()(?P<target><[^>]+>|[^)\s]+)(?P<suffix>[^)]*\))")


def rewrite_links(text: str, repo_root: Path, source_rel: str, destination_rel: str):
    root = repo_root.resolve()
    source = (root / source_rel).resolve()
    destination = (root / destination_rel).resolve()
    unresolved = []
    rewritten = 0

    def replace(match):
        nonlocal rewritten
        raw = match.group("target")
        wrapped = raw.startswith("<") and raw.endswith(">")
        target = raw[1:-1] if wrapped else raw
        parts = urlsplit(target)
        if parts.scheme or parts.netloc or not parts.path or parts.path.startswith("/"):
            return match.group(0)

        decoded_path = unquote(parts.path)
        resolved = (source.parent / decoded_path).resolve()
        try:
            resolved.relative_to(root)
        except ValueError:
            unresolved.append({"target": target, "reason": "OUTSIDE_REPOSITORY"})
            return match.group(0)

        if not resolved.exists():
            unresolved.append({"target": target, "resolved": str(resolved.relative_to(root)), "reason": "TARGET_NOT_FOUND"})
            return match.group(0)

        relative = os.path.relpath(resolved, destination.parent).replace(os.sep, "/")
        encoded = quote(relative, safe="/-._~")
        new_target = urlunsplit(("", "", encoded, parts.query, parts.fragment))
        if wrapped:
            new_target = f"<{new_target}>"
        if new_target != raw:
            rewritten += 1
        return match.group("prefix") + new_target + match.group("suffix")

    output = LINK_RE.sub(replace, text)
    return output, {"rewritten_links": rewritten, "unresolved_links": unresolved, "unresolved_count": len(unresolved)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, help="Canonical source path relative to repository root")
    parser.add_argument("--destination", required=True, help="Portable mirror path relative to repository root")
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--strict", action="store_true", help="Fail if any relative target is unresolved")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    source = root / args.source
    destination = root / args.destination
    text = source.read_text(encoding="utf-8")
    rewritten, report = rewrite_links(text, root, args.source, args.destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(rewritten, encoding="utf-8")
    print(json.dumps({"source": args.source, "destination": args.destination, **report}, ensure_ascii=False, indent=2))
    if args.strict and report["unresolved_count"]:
        raise SystemExit("PORTABLE_MIRROR_HAS_UNRESOLVED_LOCAL_LINKS")


if __name__ == "__main__":
    main()
