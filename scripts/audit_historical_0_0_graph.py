#!/usr/bin/env python3
"""Evidence-first audit of the historical 0.0 graph and related project records.

UTC timestamps in the report describe this audit execution, not original user messages.
The script never deletes or rewrites historical records. Exact-content duplicates are
reported as candidates for canonical aliasing, not automatic deletion.
"""
from pathlib import Path
from collections import defaultdict
from urllib.parse import urlparse, unquote
import hashlib, json, re, subprocess
from datetime import datetime, timezone
from graph_identifier_roles import metadata_header

ROOT = Path(".")
OUT = ROOT / "audit-output"
OUT.mkdir(exist_ok=True)
RUN_UTC = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
try:
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
except Exception:
    commit = "UNKNOWN"

# Evidence Gate outputs are retained and counted separately from architectural source nodes.
all_files = sorted(p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts and p.suffix != ".pyc" and "audit-output" not in p.parts)
evidence_files = [p for p in all_files if re.fullmatch(r"evidence-gate-.*\.txt", p.name) and p.parent.as_posix() == "evidence"]
source_files = [p for p in all_files if p not in evidence_files]
zero_paths = [p for p in all_files if "0.0" in p.as_posix()]
checkpoint_paths = [p for p in all_files if "checkpoint" in p.as_posix().lower()]
evt_files = [p for p in all_files if re.search(r"(^|/)EVT-\d+-.+", p.name)]
ref_docs = [p for p in all_files if p.as_posix().startswith("docs/reference/REFERENCE-DOCUMENTS/")]

def read_text(path):
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None

def vals(text, pattern):
    return [m.group(1).strip().strip("`' ") for m in re.finditer(pattern, text, re.I | re.M)]

def id_vals(text, pattern):
    # Keep the same conservative token normalization as build_historical_graph_manifest.py.
    excluded = {"unknown", "unverified", "none", "null", "n/a", "na", "tbd",
                "not-assigned", "not-assigned-yet", "not-applicable", "placeholder"}
    result = set()
    for value in vals(text, pattern):
        if not value.strip():
            continue
        token = value.split()[0].strip(" ' ,;:()[]{}")
        if not token or token.casefold() in excluded:
            continue
        if "$" in token or token.startswith(("{{", "<")) or "}}" in token or "%s" in token:
            continue
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:/+-]*", token):
            continue
        result.add(token)
    return sorted(result)

stable_map, prod_map, reference_id_map, content_map, evt_num_map = defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list)
records, broken_links, decode_errors = [], [], []
for p in source_files:
    raw = p.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    content_map[sha].append(p.as_posix())
    text = read_text(p)
    if text is None:
        decode_errors.append(p.as_posix())
        continue
    metadata_text, metadata_line_count = metadata_header(text)
    # Identity collision maps use only this file's own bounded metadata header.
    # Body mentions remain provenance/reference evidence and cannot create definitions.
    stable = id_vals(metadata_text, r"^\s*(?:[-*]\s*)?(?:\*\*)?(?:Stable ID(?:\s*/\s*شناسهٔ پایدار)?|Stable-ID|Canonical Stable ID|Stable Reference ID|Stable Report ID|شناسهٔ پایدار(?: این نقطه)?|شناسه پایدار(?: این نقطه)?)(?:\*\*)?\s*:\s*(?:\*\*)?`?([^`\r\n]+)")
    prod = id_vals(metadata_text, r"^\s*(?:[-*]\s*)?(?:\*\*)?(?:Production ID(?:\s*/\s*شناسهٔ تولید)?|Production-ID|Production / Registration ID|شناسهٔ تولید|شناسه تولید|شناسهٔ ثبت)(?:\*\*)?\s*:\s*(?:\*\*)?`?([^`\r\n]+)")
    reference_ids = id_vals(metadata_text, r"^\s*(?:[-*]\s*)?(?:\*\*)?Reference ID(?:\*\*)?\s*:\s*(?:\*\*)?`?([^`\r\n]+)")
    vers = vals(metadata_text, r"^\s*(?:[-*]\s*)?(?:\*\*)?Version(?:\*\*)?\s*:\s*(?:\*\*)?`?([^`\r\n]+)")
    parent = vals(metadata_text, r"^\s*(?:[-*]\s*)?(?:Parent(?: input| event| reference)?|Parent ID|Parent Stable ID)\s*:\s*`?([^`\r\n]+)")
    for x in stable: stable_map[x].append(p.as_posix())
    for x in prod: prod_map[x].append(p.as_posix())
    for x in reference_ids: reference_id_map[x].append(p.as_posix())
    evt = re.match(r"EVT-(\d+)-", p.name)
    if evt: evt_num_map[evt.group(1)].append(p.as_posix())
    links = []
    # Markdown links embedded in source-code test fixtures are examples, not repository navigation edges.
    # Audit navigation links only in documentation formats; still scan all text files for IDs and provenance.
    if p.suffix.lower() in {".md", ".markdown", ".mdx", ".rst"}:
        link_matches = re.finditer(r"!??\[[^\]]*\]\(([^)]+)\)", text)
    else:
        link_matches = ()
    for m in link_matches:
        target = m.group(1).strip().split()[0].strip("<>")
        if not target or target.startswith("#"): continue
        u = urlparse(target)
        if u.scheme or u.netloc: continue
        path_part = unquote(u.path)
        if not path_part: continue
        candidate = (p.parent / path_part).resolve()
        try: rel = candidate.relative_to(ROOT.resolve()).as_posix()
        except ValueError: continue
        links.append(target)
        if not candidate.exists():
            broken_links.append({"source":p.as_posix(),"target":target,"resolved_candidate":rel})
    records.append({
        "path":p.as_posix(),"sha256":sha,"bytes":len(raw),
        "stable_ids":stable,"production_ids":prod,"reference_ids":reference_ids,
        "versions":sorted(set(vers)),"parents":sorted(set(parent)),
        "event_number":evt.group(1) if evt else None,"local_links_checked":len(links)
    })

def collisions(mapping):
    return [{"key":k,"paths":sorted(set(v))} for k,v in sorted(mapping.items()) if len(set(v)) > 1]
duplicate_content = [{"sha256":k,"paths":sorted(v)} for k,v in sorted(content_map.items()) if len(v)>1]
stable_collisions = collisions(stable_map)
prod_collisions = collisions(prod_map)
reference_id_collisions = collisions(reference_id_map)
evt_collisions = collisions(evt_num_map)
report = {
    "schema":"palang-historical-graph-audit/v1",
    "audit_time_utc":RUN_UTC,
    "repository_commit":commit,
    "scope_note":"Repository source scan only. No external storage or ChatGPT-wide capture is tested.",
    "counts":{
        "all_files_including_evidence":len(all_files),
        "source_files_excluding_generated_evidence_gate":len(source_files),
        "paths_containing_0.0":len(zero_paths),
        "checkpoint_paths_case_insensitive":len(checkpoint_paths),
        "event_files_named_EVT":len(evt_files),
        "reference_document_paths":len(ref_docs),
        "generated_evidence_gate_files":len(evidence_files),
        "text_records_scanned":len(records),
        "decode_errors":len(decode_errors),
        "local_markdown_links_missing":len(broken_links),
        "stable_id_collision_groups":len(stable_collisions),
        "production_id_collision_groups":len(prod_collisions),
        "reference_id_collision_groups":len(reference_id_collisions),
        "event_number_collision_groups":len(evt_collisions),
        "exact_content_duplicate_groups":len(duplicate_content)
    },
    "stable_id_collisions":stable_collisions,
    "production_id_collisions":prod_collisions,
    "reference_id_collisions":reference_id_collisions,
    "event_number_collisions":evt_collisions,
    "exact_content_duplicates":duplicate_content,
    "missing_local_links":broken_links,
    "decode_errors":decode_errors,
    "records":records
}
(OUT/"historical-0.0-graph-audit.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
lines = [
"# Historical 0.0 Graph Audit",
"",
f"- Audit execution UTC: {RUN_UTC}",
f"- Repository commit: {commit}",
"- Scope: repository content scan; generated Evidence Gate outputs are counted separately from source nodes.",
"- Safety: no historic file is deleted or overwritten by this audit.",
"",
"## Counts",
]
for k,v in report["counts"].items(): lines.append(f"- {k}: {v}")
for title,key in [
    ("Stable ID collisions","stable_id_collisions"),
    ("Production ID collisions","production_id_collisions"),
    ("Reference ID collisions","reference_id_collisions"),
    ("EVT number collisions (number is not a unique key)","event_number_collisions"),
    ("Exact-content duplicate candidates (preserve files; canonicalize by alias/lineage)","exact_content_duplicates"),
    ("Missing local links","missing_local_links"),
    ("Unreadable/non-UTF8 files","decode_errors")
]:
    lines += ["",f"## {title}"]
    items=report[key]
    if not items: lines.append("- None detected.")
    else:
        for item in items:
            if "paths" in item: lines.append(f"- `{item.get('key',item.get('sha256'))}`: "+"; ".join(item["paths"]))
            elif "source" in item: lines.append(f"- `{item['source']}` → `{item['target']}`")
            else: lines.append(f"- `{item}`")
lines += ["","## Interpretation","- Duplicate content is not automatically deleted; preserve historical paths and create a canonical alias/lineage edge.","- Duplicate Stable ID / Production ID / EVT number groups require source and lineage adjudication; never infer identity from filename number alone.","- A zero missing-link count is limited to relative Markdown links detected by this scanner; it does not prove semantic correctness or external URL availability.","- This report does not prove Dropbox, Buffer, Library, Persistent Memory, or runtime-wide automatic interaction capture."]
(OUT/"historical-0.0-graph-audit.txt").write_text("\n".join(lines)+"\n",encoding="utf-8")
print("HISTORICAL_0_0_GRAPH_AUDIT")
print(f"audit_time_utc={RUN_UTC}")
print(f"repository_commit={commit}")
for k,v in report["counts"].items(): print(f"{k}={v}")
for item in broken_links:
    print(f"missing_local_link={item['source']} -> {item['target']} (resolved={item['resolved_candidate']})")
print("outputs=audit-output/historical-0.0-graph-audit.txt,audit-output/historical-0.0-graph-audit.json")
