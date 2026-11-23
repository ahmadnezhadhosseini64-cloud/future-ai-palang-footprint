#!/usr/bin/env python3
"""Verified backup/restore helpers for the RAHM evidence ledger."""
from __future__ import annotations
import argparse, hashlib, json, os, shutil, sys, tempfile
from datetime import datetime, timezone
from pathlib import Path
from rahm_runtime import load

def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def atomic_copy(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=target.name + ".", suffix=".tmp", dir=str(target.parent))
    os.close(fd)
    try:
        shutil.copyfile(source, temp_name)
        with open(temp_name, "rb") as stream:
            os.fsync(stream.fileno())
        os.replace(temp_name, target)
    except Exception:
        try: os.unlink(temp_name)
        except OSError: pass
        raise

def backup(source: Path, directory: Path) -> dict:
    load(source)  # Never create a backup from an invalid ledger.
    directory.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    target = directory / f"rahm-ledger-{stamp}.json"
    if target.exists():
        raise FileExistsError(f"backup already exists: {target}")
    atomic_copy(source, target)
    manifest = {"schema":"rahm-backup-manifest/1", "file":target.name,
                "sha256":digest(target), "bytes":target.stat().st_size,
                "created_at_utc":datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00","Z")}
    manifest_path = target.with_suffix(target.suffix + ".manifest.json")
    temp = manifest_path.with_suffix(manifest_path.suffix + ".tmp")
    temp.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    os.replace(temp, manifest_path)
    return {"result":"BACKUP_OK", "backup":str(target), "manifest":str(manifest_path), "sha256":manifest["sha256"]}

def restore(source: Path, target: Path) -> dict:
    manifest_path = source.with_suffix(source.suffix + ".manifest.json")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema") != "rahm-backup-manifest/1" or manifest.get("file") != source.name:
        raise ValueError("backup manifest identity/schema mismatch")
    actual = digest(source)
    if actual != manifest.get("sha256") or source.stat().st_size != manifest.get("bytes"):
        raise ValueError("backup checksum or size mismatch")
    load(source)  # Verify the internal event chain before restoring.
    atomic_copy(source, target)
    load(target)
    return {"result":"RESTORE_OK", "target":str(target), "sha256":actual}

def main(argv=None) -> int:
    parser=argparse.ArgumentParser(description="RAHM verified backup and restore")
    sub=parser.add_subparsers(dest="command", required=True)
    b=sub.add_parser("backup"); b.add_argument("--source",required=True); b.add_argument("--directory",required=True)
    r=sub.add_parser("restore"); r.add_argument("--source",required=True); r.add_argument("--target",required=True)
    args=parser.parse_args(argv)
    try:
        result = backup(Path(args.source),Path(args.directory)) if args.command=="backup" else restore(Path(args.source),Path(args.target))
        print(json.dumps(result,ensure_ascii=False)); return 0
    except (OSError,ValueError,json.JSONDecodeError) as exc:
        print(json.dumps({"result":"FAIL","error":str(exc)},ensure_ascii=False),file=sys.stderr); return 2

if __name__=="__main__":
    raise SystemExit(main())
