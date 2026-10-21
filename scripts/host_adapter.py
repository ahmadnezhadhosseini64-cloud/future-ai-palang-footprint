#!/usr/bin/env python3
"""Authenticated durable receiver for interaction events; not a ChatGPT host hook."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from urllib.parse import urlparse
import hashlib, hmac, json, os, sqlite3, uuid
HOST=os.environ.get('PALANG_ADAPTER_HOST','127.0.0.1'); PORT=int(os.environ.get('PALANG_ADAPTER_PORT','8765'))
SECRET=os.environ.get('PALANG_ADAPTER_SECRET',''); DB=os.environ.get('PALANG_DB_PATH','palang-events.sqlite3')
def times():
 d=datetime.now(timezone.utc); return d.isoformat(timespec='seconds').replace('+00:00','Z'),d.astimezone(ZoneInfo('Asia/Tehran')).isoformat(timespec='seconds')
def canon(x): return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
def open_db():
 d=sqlite3.connect(DB,timeout=10); d.execute('PRAGMA journal_mode=WAL')
 d.execute('CREATE TABLE IF NOT EXISTS events(event_id TEXT PRIMARY KEY,idempotency_key TEXT UNIQUE NOT NULL,event_type TEXT NOT NULL,parent_event_id TEXT,received_utc TEXT NOT NULL,received_tehran TEXT NOT NULL,payload_json TEXT NOT NULL,payload_sha256 TEXT NOT NULL,status TEXT NOT NULL)'); return d
class Handler(BaseHTTPRequestHandler):
 def reply(self,code,obj):
  b=canon(obj); self.send_response(code); self.send_header('Content-Type','application/json; charset=utf-8'); self.send_header('Content-Length',str(len(b))); self.end_headers(); self.wfile.write(b)
 def auth(self,body):
  if not SECRET: self.reply(503,{'error':'PALANG_ADAPTER_SECRET_not_configured'}); return False
  expected='sha256='+hmac.new(SECRET.encode(),body,hashlib.sha256).hexdigest()
  if not hmac.compare_digest(self.headers.get('X-Palang-Signature',''),expected): self.reply(401,{'error':'unauthorized'}); return False
  return True
 def do_GET(self):
  path=urlparse(self.path).path
  if path=='/health':
   u,t=times(); self.reply(200,{'status':'ok','utc':u,'tehran':t,'durable_store':'sqlite','live_producer_connected':False})
  elif path=='/v1/events':
   if not self.auth(b''): return
   with open_db() as d: rows=d.execute('SELECT event_id,event_type,parent_event_id,received_utc,received_tehran,payload_sha256,status FROM events ORDER BY received_utc').fetchall()
   keys=['event_id','event_type','parent_event_id','received_utc','received_tehran','payload_sha256','status']; self.reply(200,{'count':len(rows),'events':[dict(zip(keys,r)) for r in rows]})
  else: self.reply(404,{'error':'not_found'})
 def do_POST(self):
  if urlparse(self.path).path!='/v1/events': self.reply(404,{'error':'not_found'}); return
  try: n=int(self.headers.get('Content-Length','0'))
  except ValueError: n=0
  if n<1: self.reply(411,{'error':'content_length_required'}); return
  if n>1000000: self.reply(413,{'error':'body_size_out_of_range'}); return
  body=self.rfile.read(n)
  if not self.auth(body): return
  try: p=json.loads(body.decode('utf-8'))
  except Exception: self.reply(400,{'error':'invalid_json'}); return
  if not isinstance(p,dict) or p.get('event_type') not in ('USER_INPUT','ASSISTANT_OUTPUT'): self.reply(400,{'error':'invalid_event_type'}); return
  eid=p.get('event_id') or str(uuid.uuid4()); key=p.get('idempotency_key') or eid
  if not isinstance(eid,str) or not isinstance(key,str) or len(eid)>200 or len(key)>200: self.reply(400,{'error':'invalid_event_or_key'}); return
  u,t=times(); digest=hashlib.sha256(canon(p)).hexdigest()
  try:
   with open_db() as d:
    old=d.execute('SELECT event_id,payload_sha256 FROM events WHERE idempotency_key=?',(key,)).fetchone()
    if old:
     if old[1]!=digest: self.reply(409,{'error':'idempotency_conflict','existing_event_id':old[0]}); return
     self.reply(200,{'status':'duplicate_replay_same_payload','event_id':old[0],'sha256':old[1]}); return
    d.execute('INSERT INTO events VALUES(?,?,?,?,?,?,?,?,?)',(eid,key,p['event_type'],p.get('parent_event_id'),u,t,json.dumps(p,ensure_ascii=False,sort_keys=True),digest,'QUEUED'))
  except sqlite3.IntegrityError: self.reply(409,{'error':'event_id_or_key_conflict'}); return
  with open_db() as d: row=d.execute('SELECT event_id,payload_sha256,status FROM events WHERE event_id=?',(eid,)).fetchone()
  if not row or row[1]!=digest: self.reply(500,{'error':'readback_mismatch'}); return
  self.reply(201,{'status':'QUEUED_AND_READBACK_VERIFIED','event_id':eid,'received_utc':u,'received_tehran':t,'sha256':digest,'destination':'durable SQLite queue','repository_write':'NOT_IMPLEMENTED'})
 def log_message(self,*args): return
if __name__=='__main__':
 if not SECRET: raise SystemExit('Set PALANG_ADAPTER_SECRET; refusing unauthenticated start.')
 open_db().close(); print(json.dumps({'adapter':'PalangHostAdapter/1.0','host':HOST,'port':PORT,'producer_connected':False})); ThreadingHTTPServer((HOST,PORT),Handler).serve_forever()
