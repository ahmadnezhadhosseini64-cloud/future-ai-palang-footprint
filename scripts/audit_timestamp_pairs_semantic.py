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
 for ln,line in enumerate(txt.splitlines(),1):
  parsed=[]
  for m in ISO.finditer(line):
   val=m.group(1); n+=1; total+=1
   try: d=parse(val)
   except (ValueError,OverflowError): d=None
   if d is None: errors.append({'path':rel,'line':ln,'value':val,'reason':'timezone offset missing or invalid'})
   parsed.append((val,d))
  if len(parsed)>=2 and UTC_LABEL.search(line) and LOCAL_LABEL.search(line):
   for i in range(len(parsed)):
    for j in range(i+1,len(parsed)):
     a,b=parsed[i],parsed[j]
     if a[1] is None or b[1] is None: status='UNVERIFIABLE_PARSE'; delta=None
     else:
      delta=(a[1].astimezone(UTC)-b[1].astimezone(UTC)).total_seconds(); status='PASS_SAME_INSTANT' if delta==0 else 'FAIL_INSTANT_MISMATCH'
     pairs.append({'path':rel,'line':ln,'a':a[0],'b':b[0],'status':status,'delta_seconds_a_minus_b':delta})
 files.append({'path':rel,'sha256':hashlib.sha256(raw).hexdigest(),'timestamp_count':n})
counts={'audit_execution_utc':run,'repository_commit':commit,'files_scanned':len(files),'timestamp_strings_found':total,'explicit_same_line_utc_local_pairs':len(pairs),'pairs_pass_same_instant':sum(x['status']=='PASS_SAME_INSTANT' for x in pairs),'pairs_fail_instant_mismatch':sum(x['status']=='FAIL_INSTANT_MISMATCH' for x in pairs),'pairs_unverifiable_parse':sum(x['status']=='UNVERIFIABLE_PARSE' for x in pairs),'parse_errors_or_timezone_missing':len(errors)}
report={'schema':'palang-semantic-timestamp-pair-audit/v1','counts':counts,'pairs':pairs,'parse_errors':errors,'files':files,'scope_limit':'Only explicitly labelled UTC/local values on the same line are paired; unpaired timestamps are not guessed.'}
(OUT/'timestamp-pairs-semantic-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lines=['# Semantic UTC / Tehran Timestamp Pair Audit','',f'- Audit execution UTC: {run}',f'- Repository commit: {commit}','','## Counts']+[f'- {k}: {v}' for k,v in counts.items()]+['','## Pairs']
lines += [f"- {x['status']} | {x['path']}:{x['line']} | {x['a']} <> {x['b']} | delta={x['delta_seconds_a_minus_b']} seconds" for x in pairs] or ['- No confidently labelled same-line pairs detected; this is not proof none exist.']
lines += ['','## Parse issues']+[f"- {x['path']}:{x['line']} {x['value']} — {x['reason']}" for x in errors]+['','## Limits','- Only explicitly labelled same-line UTC/Tehran pairs are validated.','- Message time is never inferred from commit time.','- UTC is canonical; Tehran conversion uses IANA Asia/Tehran rules.']
(OUT/'timestamp-pairs-semantic-audit.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('SEMANTIC_TIMESTAMP_PAIR_AUDIT')
for k,v in counts.items(): print(f'{k}={v}')
for x in pairs: print(f"{x['status']} {x['path']}:{x['line']} {x['a']} <> {x['b']} delta_seconds={x['delta_seconds_a_minus_b']}")
print('result=REVIEW_REQUIRED' if counts['pairs_fail_instant_mismatch'] or counts['pairs_unverifiable_parse'] or errors else 'result=PAIR_ARITHMETIC_PASS_WITH_SCOPE_LIMITS')
