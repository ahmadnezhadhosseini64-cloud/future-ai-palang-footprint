#!/usr/bin/env python3
"""Legacy owner-operated event transfer worker; host-originated writes to the master repo are disabled.
The master repository is owner-only WRITE. This worker must not write to it, including host-intake.
A future broker must resolve a verified Host ID server-side and use a GitHub App scoped to that host's private repository.
No token may be placed in an AI host runtime, prompt, chat, package, or host-controlled secret store.
"""
import base64,json,os,re,sqlite3,sys,urllib.error,urllib.request
DB=os.environ.get('PALANG_DB_PATH','palang-events.sqlite3')
REPO=os.environ.get('PALANG_GITHUB_REPOSITORY','ahmadnezhadhosseini64-cloud/future-ai-palang-footprint')
TOKEN=os.environ.get('GITHUB_TOKEN','')
API=os.environ.get('GITHUB_API_URL','https://api.github.com')
BRANCH='host-intake'
MASTER_REPOSITORY='ahmadnezhadhosseini64-cloud/future-ai-palang-footprint'
if os.environ.get('PALANG_GITHUB_BRANCH','host-intake') != BRANCH:
    raise SystemExit('BLOCKED: host intake worker writes only to the dedicated host-intake branch; owner-reviewed pull request required for promotion.')
def request(method,url,payload=None):
 if not TOKEN: raise RuntimeError('GITHUB_TOKEN is required; no repository write attempted')
 data=None if payload is None else json.dumps(payload,ensure_ascii=False).encode()
 req=urllib.request.Request(url,data=data,method=method,headers={'Accept':'application/vnd.github+json','Authorization':'Bearer '+TOKEN,'X-GitHub-Api-Version':'2022-11-28','User-Agent':'Palang-Host-Adapter'})
 if data is not None: req.add_header('Content-Type','application/json')
 try:
  with urllib.request.urlopen(req,timeout=20) as r: return r.status,json.loads(r.read().decode())
 except urllib.error.HTTPError as e:
  body=e.read().decode(errors='replace')
  if e.code==404: return 404,{'message':body}
  raise RuntimeError(f'GitHub API HTTP {e.code}: {body}')
def main():
 if REPO == MASTER_REPOSITORY:
  raise SystemExit('BLOCKED: owner-only master repository. Host-originated writes to master, including host-intake, are disabled. Use an owner-operated, verified broker and a per-host private repository.')
 if not TOKEN: raise SystemExit('BLOCKED: no authorized broker credential configured; do not place a GitHub token in a host runtime.')
 with sqlite3.connect(DB,timeout=10) as db:
  rows=db.execute("SELECT event_id,event_type,parent_event_id,received_utc,received_tehran,payload_json,payload_sha256 FROM events WHERE status='QUEUED' ORDER BY received_utc").fetchall()
  print(f'queued_events={len(rows)} repository={REPO} branch={BRANCH}')
  for row in rows:
   eid,etype,parent,utc,tehran,payload_text,digest=row
   safe=re.sub(r'[^A-Za-z0-9._-]','-',eid)[:120]
   path=f'docs/architecture/BEHAVIOR-TRACE/INGESTED-EVENTS/{safe}.json'
   url=f'{API}/repos/{REPO}/contents/{path}'
   record={'event_id':eid,'event_type':etype,'parent_event_id':parent,'received_utc':utc,'received_tehran':tehran,'payload_sha256':digest,'payload':json.loads(payload_text),'promotion_status':'QUARANTINED_OWNER_REVIEW_REQUIRED'}
   raw=(json.dumps(record,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
   status,existing=request('GET',url)
   if status==200:
    decoded=base64.b64decode(existing.get('content','').replace('\n',''))
    if decoded!=raw:
     print(f'CONFLICT event_id={eid} path={path}; existing content differs; not overwritten'); continue
    sha=existing.get('sha')
   else: sha=None
   body={'message':f'Ingest interaction event {safe}','content':base64.b64encode(raw).decode(),'branch':BRANCH}
   if sha: body['sha']=sha
   put_status,put=request('PUT',url,body)
   read_status,readback=request('GET',url)
   if read_status!=200:
    print(f'READBACK_FAIL event_id={eid} status={read_status}'); continue
   actual=base64.b64decode(readback.get('content','').replace('\n',''))
   if actual!=raw:
    print(f'READBACK_MISMATCH event_id={eid}'); continue
   db.execute("UPDATE events SET status='REPOSITORY_WRITTEN_AND_READBACK_VERIFIED' WHERE event_id=?",(eid,))
   db.commit()
   print(f'PASS event_id={eid} github_commit={put.get("commit",{}).get("sha","UNKNOWN")} readback=EXACT_MATCH')
if __name__=='__main__': main()
