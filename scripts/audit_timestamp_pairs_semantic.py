#!/usr/bin/env python3
"""Semantic UTC/local pair audit; source files are never rewritten."""
from pathlib import Path
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import hashlib, json, re, subprocess
ROOT=Path('.'); OUT=ROOT/'audit-output'; OUT.mkdir(exist_ok=True)
UTC=timezone.utc; TEHRAN=ZoneInfo('Asia/Tehran')
EXT={'.md','.txt','.yml','.yaml','.json','.py','.html','.xml','.csv','.toml'}; SKIP={'.git','node_modules','.venv','venv','audit-output'}
ISO=re.compile(r'(?<![A-Za-z0-9])((?:19|20)\d{2}-\d{2}-\d{2}[T ]\d{2}:\d{2}(?::\d{2}(?:\.\d{1,6})?)?(?:Z|[+-]\d{2}:?\d{2})?)(?![A-Za-z0-9])')
UTC_LABEL=re.compile(r'\bUTC\b|\bZ\b|معادل UTC',re.I); LOCAL_LABEL=re.compile(r'Asia/Tehran|تهران|Tehran local|local time',re.I)
def parse(s):
 s=s.replace(' ','T',1)
 if s.endswith('Z'): s=s[:-1]+'+00:00'
 s=re.sub(r'([+-]\d{2})(\d{2})$',r'\1:\2',s)
 d=datetime.fromisoformat(s)
 return d if d.tzinfo else None
try: commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
except Exception: commit='UNKNOWN'
run=datetime.now(UTC).isoformat(timespec='seconds').replace('+00:00','Z'); pairs=[]; errors=[]; files=[]; total=0
for p in sorted(ROOT.rglob('*')):
 if not p.is_file() or p.suffix.lower() not in EXT or any(x in SKIP for x in p.parts): continue
 try: raw=p.read_bytes(); txt=raw.decode('utf-8')
 except (OSError,UnicodeDecodeError): continue
 rel=p.as_posix()
 if not (rel.startswith(('docs/','checkpoints/','recovery/','provenance/')) or rel.startswith('scripts/audit_timestamp')): continue
 n=0
 lines=txt.splitlines()
 # A blank line separates semantic paragraphs; never pair across a paragraph boundary.
 paragraphs=[]; current=[]
 for ln,line in enumerate(lines,1):
  if not line.strip():
   if current: paragraphs.append(current); current=[]
  else: current.append((ln,line))
 if current: paragraphs.append(current)
 paired_occurrences=set()
 for para in paragraphs:
  utc_items=[]; local_items=[]; all_items=[]
  for ln,line in para:
   for m in ISO.finditer(line):
    val=m.group(1); n+=1; total+=1
    try: dt=parse(val)
    except (ValueError,OverflowError): dt=None
    item={'path':rel,'line':ln,'value':val,'dt':dt,'line_text':line.strip()[:300]}
    all_items.append(item)
    if dt is None:
     errors.append({'path':rel,'line':ln,'value':val,'reason':'timezone offset missing or invalid'})
     continue
    has_utc=bool(UTC_LABEL.search(line)) or val.endswith('Z') or val.endswith('+00:00') or val.endswith('-00:00')
    has_local=bool(LOCAL_LABEL.search(line))
    if has_utc and has_local:
     # Resolve role from the timestamp's own offset when a line has both labels.
     if dt.utcoffset().total_seconds()==0: utc_items.append(item)
     else: local_items.append(item)
    elif has_utc: utc_items.append(item)
    elif has_local: local_items.append(item)
  # Pair one-to-one in document order only when each role has matching cardinality.
  # Unequal cardinality is retained as unpaired evidence, not guessed.
  utc_items.sort(key=lambda x:(x['line'],x['value']))
  local_items.sort(key=lambda x:(x['line'],x['value']))
  if utc_items and len(utc_items)==len(local_items):
   for u,l in zip(utc_items,local_items):
    if abs(u['line']-l['line'])>8: continue
    delta=(u['dt'].astimezone(UTC)-l['dt'].astimezone(UTC)).total_seconds()
    expected=l['dt'].astimezone(TEHRAN)
    same_instant=(delta==0)
    local_zone_match=(l['dt'].utcoffset()==expected.utcoffset() and l['dt'].replace(tzinfo=None)==expected.replace(tzinfo=None))
    status='PASS_SAME_INSTANT_AND_TEHRAN_ZONE' if same_instant and local_zone_match else ('FAIL_INSTANT_MISMATCH' if not same_instant else 'FAIL_TEHRAN_ZONE_MISMATCH')
    pairs.append({'path':rel,'utc_line':u['line'],'local_line':l['line'],'utc':u['value'],'local':l['value'],'status':status,'delta_seconds_utc_minus_local':delta,'expected_tehran':expected.isoformat(timespec='seconds')})
    paired_occurrences.add((u['line'],u['value'])); paired_occurrences.add((l['line'],l['value']))
  else:
   # Same-line explicit pairs are eligible even if the paragraph has extra timestamp fields.
   for ln,line in para:
    hits=[(m.group(1),parse(m.group(1))) for m in ISO.finditer(line)]
    if len(hits)==2 and UTC_LABEL.search(line) and LOCAL_LABEL.search(line) and all(x[1] is not None for x in hits):
     a,b=hits
     if a[1].utcoffset().total_seconds()==0: u,l=a,b
     elif b[1].utcoffset().total_seconds()==0: u,l=b,a
     else: continue
     delta=(u[1].astimezone(UTC)-l[1].astimezone(UTC)).total_seconds()
     expected=u[1].astimezone(TEHRAN)
     zone_match=l[1].utcoffset()==expected.utcoffset() and l[1].replace(tzinfo=None)==expected.replace(tzinfo=None)
     status='PASS_SAME_INSTANT_AND_TEHRAN_ZONE' if delta==0 and zone_match else ('FAIL_INSTANT_MISMATCH' if delta else 'FAIL_TEHRAN_ZONE_MISMATCH')
     pairs.append({'path':rel,'utc_line':ln,'local_line':ln,'utc':u[0],'local':l[0],'status':status,'delta_seconds_utc_minus_local':delta,'expected_tehran':expected.isoformat(timespec='seconds')})
     paired_occurrences.add((ln,u[0])); paired_occurrences.add((ln,l[0]))
 files.append({'path':rel,'sha256':hashlib.sha256(raw).hexdigest(),'timestamp_count':n,'paired_timestamp_occurrences':len(paired_occurrences),'unpaired_timestamp_occurrences':max(0,n-len(paired_occurrences))})
 files.append({'path':rel,'sha256':hashlib.sha256(raw).hexdigest(),'timestamp_count':n})
counts={'audit_execution_utc':run,'repository_commit':commit,'files_scanned':len(files),'timestamp_strings_found':total,'explicit_same_line_utc_local_pairs':len(pairs),'pairs_pass_same_instant_and_zone':sum(x['status']=='PASS_SAME_INSTANT_AND_TEHRAN_ZONE' for x in pairs),'pairs_fail_instant_mismatch':sum(x['status']=='FAIL_INSTANT_MISMATCH' for x in pairs),'pairs_fail_tehran_zone_mismatch':sum(x['status']=='FAIL_TEHRAN_ZONE_MISMATCH' for x in pairs),'pairs_unverifiable_parse':sum(x['status']=='UNVERIFIABLE_PARSE' for x in pairs),'parse_errors_or_timezone_missing':len(errors),'unpaired_timestamp_occurrences':sum(x['unpaired_timestamp_occurrences'] for x in files)}
report={'schema':'palang-semantic-timestamp-pair-audit/v1','counts':counts,'pairs':pairs,'parse_errors':errors,'files':files,'scope_limit':'Only explicitly labelled UTC/local values on the same line are paired; unpaired timestamps are not guessed.'}
(OUT/'timestamp-pairs-semantic-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lines=['# Semantic UTC / Tehran Timestamp Pair Audit','',f'- Audit execution UTC: {run}',f'- Repository commit: {commit}','','## Counts']+[f'- {k}: {v}' for k,v in counts.items()]+['','## Pairs']
lines += [f"- {x['status']} | {x['path']}:{x['line']} | {x['utc']} <> {x['local']} | delta={x['delta_seconds_utc_minus_local']} seconds | expected Tehran={x['expected_tehran']}" for x in pairs] or ['- No confidently labelled same-line pairs detected; this is not proof none exist.']
lines += ['','## Parse issues']+[f"- {x['path']}:{x['line']} {x['value']} — {x['reason']}" for x in errors]+['','## Limits','- Explicit UTC/local labels are paired within a paragraph only when role counts agree; same-line pairs are a fallback. Ambiguous or unpaired timestamps remain flagged.','- Message time is never inferred from commit time.','- UTC is canonical; Tehran conversion uses IANA Asia/Tehran rules.']
(OUT/'timestamp-pairs-semantic-audit.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('SEMANTIC_TIMESTAMP_PAIR_AUDIT')
for k,v in counts.items(): print(f'{k}={v}')
for x in pairs: print(f"{x['status']} {x['path']}:{x['line']} {x['a']} <> {x['b']} delta_seconds={x['delta_seconds_a_minus_b']}")
print('result=REVIEW_REQUIRED' if counts['pairs_fail_instant_mismatch'] or counts['pairs_fail_tehran_zone_mismatch'] or counts['pairs_unverifiable_parse'] or errors else 'result=PAIR_ARITHMETIC_PASS_WITH_SCOPE_LIMITS')
