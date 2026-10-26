#!/usr/bin/env python3
"""Normalize repository timestamps to canonical UTC and derived Asia/Tehran."""
from pathlib import Path
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import hashlib, json, re, subprocess
ROOT=Path('.'); OUT=ROOT/'audit-output'; OUT.mkdir(exist_ok=True)
UTC=timezone.utc; TEHRAN=ZoneInfo('Asia/Tehran')
EXT={'.md','.txt','.yml','.yaml','.json','.py','.html','.xml','.csv','.toml'}
SKIP={'.git','node_modules','.venv','venv','audit-output','__pycache__'}
ISO=re.compile(r'(?<![A-Za-z0-9])((?:19|20)\d{2}-\d{2}-\d{2}[T ]\d{2}:\d{2}(?::\d{2}(?:\.\d{1,9})?)?(?:\s*(?:Z|[+-]\d{2}:?\d{2}))?)(?![A-Za-z0-9])')
UTC_LABEL=re.compile(r'\bUTC\b|\bZ\b|معادل UTC|زمان مرجع',re.I)
LOCAL_LABEL=re.compile(r'Asia/Tehran|تهران|Tehran local|local time|زمان تهران|local-session time context',re.I)
def parse(s):
 s=s.replace(' ','T',1)
 if s.endswith('Z'): s=s[:-1]+'+00:00'
 s=re.sub(r'([+-]\d{2})(\d{2})$',r'\1:\2',s)
 return datetime.fromisoformat(s)
def git_file_time_map():
 # One history walk is much faster than launching git once per file.
 result={}
 try:
  log=subprocess.check_output(['git','log','--format=COMMIT:%cI','--name-only','--','docs','checkpoints','recovery','provenance','evidence','scripts'],text=True,stderr=subprocess.DEVNULL)
  stamp=None
  for line in log.splitlines():
   if line.startswith('COMMIT:'):
    try: stamp=datetime.fromisoformat(line[7:].replace('Z','+00:00')).astimezone(UTC)
    except ValueError: stamp=None
   elif line.strip() and stamp is not None and line not in result:
    result[line]=stamp
 except Exception: pass
 return result
try: commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
except Exception: commit='UNKNOWN'
TRACKED_FILES=set(subprocess.check_output(['git','ls-files'],text=True).splitlines())
FILE_TIMES=git_file_time_map()
# Resolve any remaining tracked paths without launching git once per normal file.
try:
 for rel in subprocess.check_output(['git','ls-files'],text=True).splitlines():
  if rel not in FILE_TIMES and rel.startswith(('docs/','checkpoints/','recovery/','provenance/','evidence/','scripts/')):
   try:
    v=subprocess.check_output(['git','log','-1','--format=%cI','--',rel],text=True,stderr=subprocess.DEVNULL).strip()
    if v: FILE_TIMES[rel]=datetime.fromisoformat(v.replace('Z','+00:00')).astimezone(UTC)
   except Exception: pass
except Exception: pass
run=datetime.now(UTC); run_s=run.isoformat(timespec='seconds').replace('+00:00','Z')
files=[]; stamps=[]; errors=[]; total=0
for p in sorted(ROOT.rglob('*')):
 if not p.is_file() or p.as_posix() not in TRACKED_FILES or p.suffix.lower() not in EXT or any(x in SKIP for x in p.parts): continue
 rel=p.as_posix()
 if not (rel.startswith(('docs/','checkpoints/','recovery/','provenance/','evidence/')) or rel.startswith('scripts/')): continue
 try: raw=p.read_bytes(); txt=raw.decode('utf-8')
 except (OSError,UnicodeDecodeError): continue
 file_time=FILE_TIMES.get(rel)
 file_utc=file_time.isoformat(timespec='seconds').replace('+00:00','Z') if file_time else None
 file_local=file_time.astimezone(TEHRAN).isoformat(timespec='seconds') if file_time else None
 file_record={'path':rel,'sha256':hashlib.sha256(raw).hexdigest(),'repository_registration_utc':file_utc,'repository_registration_tehran':file_local,'repository_time_source':'git last-change commit metadata' if file_time else 'UNAVAILABLE','timestamp_occurrences':0}
 content_lines=txt.splitlines()
 for ln,line in enumerate(content_lines,1):
  context=' '.join(content_lines[max(0,ln-10):min(len(content_lines),ln+10)])
  for m in ISO.finditer(line):
   val=m.group(1); total+=1; file_record['timestamp_occurrences']+=1
   has_utc_label=bool(UTC_LABEL.search(context))
   local_label=bool(LOCAL_LABEL.search(context))
   explicit_utc_suffix=val.endswith('Z') or val.endswith('+00:00') or val.endswith('-00:00')
   # A line may mention both UTC and Tehran; classify each value by its own explicit offset.
   # Numeric offsets/Z in the value itself outrank broad prose labels on the same line.
   utc_label=explicit_utc_suffix or (has_utc_label and not local_label)
   try: dt=parse(val)
   except (ValueError,OverflowError) as e:
    errors.append({'path':rel,'line':ln,'value':val,'reason':'parse_error: '+str(e)}); continue
   inferred=False; role='EXPLICIT_OFFSET'
   if dt.tzinfo is None:
    if local_label:
     dt=dt.replace(tzinfo=TEHRAN); role='INFERRED_ASIA_TEHRAN'; inferred=True
    elif utc_label:
     dt=dt.replace(tzinfo=UTC); role='INFERRED_UTC'; inferred=True
    else:
     errors.append({'path':rel,'line':ln,'value':val,'reason':'timezone missing and no reliable UTC/Tehran label; cannot infer safely'})
     stamps.append({'path':rel,'line':ln,'original':val,'role':'AMBIGUOUS','status':'REVIEW_REQUIRED','utc_equivalent':None,'tehran_equivalent':None,'inferred':False})
     continue
   instant=dt.astimezone(UTC); expected_local=instant.astimezone(TEHRAN)
   status='NORMALIZED_COUNTERPART_CREATED'
   local_claim=local_label and (dt.utcoffset().total_seconds()!=0 or dt.tzinfo is TEHRAN)
   if local_claim and dt.utcoffset()!=expected_local.utcoffset():
    status='REVIEW_TEHRAN_OFFSET_MISMATCH'
   if local_claim and dt.replace(tzinfo=None)!=expected_local.replace(tzinfo=None):
    status='FAIL_TEHRAN_LOCAL_VALUE_MISMATCH'
   item={'path':rel,'line':ln,'original':val,'role':role,'utc_equivalent':instant.isoformat(timespec='seconds').replace('+00:00','Z'),'tehran_equivalent':expected_local.isoformat(timespec='seconds'),'status':status,'inferred':inferred,'inference_basis':('project default Asia/Tehran; contextual only' if inferred and 'local-session time context' in context else ('nearby explicit timezone/UTC label' if inferred else 'explicit timestamp offset')),'source_line':line.strip()[:240]}
   stamps.append(item)
  # if a line explicitly presents both values, compare all normalized instants in that line.
 # repository time is the canonical timestamp for registering this file, independent of historical embedded times.
 files.append(file_record)
counts={'audit_execution_utc':run_s,'repository_commit':commit,'files_scanned':len(files),'timestamp_strings_found':total,'timestamps_normalized':sum(bool(x.get('utc_equivalent')) for x in stamps),'timestamps_with_utc_and_tehran_pair':sum(bool(x.get('utc_equivalent') and x.get('tehran_equivalent')) for x in stamps),'ambiguous_or_parse_errors':len(errors),'tehran_offset_or_value_failures':sum(x['status'] in ('REVIEW_TEHRAN_OFFSET_MISMATCH','FAIL_TEHRAN_LOCAL_VALUE_MISMATCH') for x in stamps),'utc_label_failures':sum(x['status']=='FAIL_UTC_LABEL_OFFSET_MISMATCH' for x in stamps),'files_with_repository_commit_time':sum(bool(x['repository_registration_utc']) for x in files),'files_without_repository_commit_time':sum(not x['repository_registration_utc'] for x in files)}
report={'schema':'palang-repository-time-normalization-audit/v2','counts':counts,'timestamp_records':stamps,'parse_or_ambiguity_issues':errors,'files':files,'rule':'Repository last-change commit timestamp is the registration anchor for each file; UTC is canonical and Asia/Tehran is derived from that UTC instant. Embedded message/event timestamps are historical evidence and do not replace repository registration time.'}
(OUT/'timestamp-pairs-semantic-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lines=['# Repository Registration Timestamp Normalization Audit','',f'- Audit execution UTC: {run_s}',f'- Repository HEAD: {commit}','','## Counts']+[f'- {k}: {v}' for k,v in counts.items()]+['','## Per-file repository registration anchors']
lines += [f"- {x['path']} | UTC={x['repository_registration_utc'] or 'UNKNOWN'} | Tehran={x['repository_registration_tehran'] or 'UNKNOWN'} | source={x['repository_time_source']}" for x in files]
lines += ['','## Embedded timestamp normalization']
lines += [f"- {x['status']} | {x['path']}:{x['line']} | original={x['original']} | role={x['role']} | UTC={x['utc_equivalent'] or 'UNKNOWN'} | Tehran={x['tehran_equivalent'] or 'UNKNOWN'} | inferred={x['inferred']}" for x in stamps]
lines += ['','## Issues']+[f"- {x['path']}:{x['line']} {x['value']} — {x['reason']}" for x in errors]+['','## Rule','- The repository registration anchor is the last-change commit timestamp for each file.','- UTC is canonical; Asia/Tehran is calculated from that UTC instant using IANA timezone rules.','- A timestamp without an offset is inferred only when the same line reliably labels it UTC or Tehran. Otherwise it remains unknown.','- Repository registration time is not represented as original message creation time.']
(OUT/'timestamp-pairs-semantic-audit.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('REPOSITORY_TIME_NORMALIZATION_AUDIT')
for k,v in counts.items(): print(f'{k}={v}')
for x in errors[:25]: print(f"ISSUE {x['path']}:{x['line']} {x['value']} — {x['reason']}")
for x in stamps:
 if x['status'] in ('REVIEW_TEHRAN_OFFSET_MISMATCH','FAIL_TEHRAN_LOCAL_VALUE_MISMATCH'): print(f"MISMATCH {x['status']} {x['path']}:{x['line']} original={x['original']} UTC={x['utc_equivalent']} Tehran={x['tehran_equivalent']} role={x['role']}")
print('result=REVIEW_REQUIRED' if errors or counts['tehran_offset_or_value_failures'] or counts['utc_label_failures'] or counts['files_without_repository_commit_time'] else 'result=REPOSITORY_TIME_NORMALIZATION_PASS')
