#!/usr/bin/env python3
"""Synthetic adapter tests: auth, durable readback, retry and restart."""
import hashlib,hmac,json,tempfile,threading,urllib.request,urllib.error,importlib.util
from pathlib import Path
from http.server import ThreadingHTTPServer
s=importlib.util.spec_from_file_location('adapter',Path(__file__).with_name('host_adapter.py')); a=importlib.util.module_from_spec(s); s.loader.exec_module(a)
def main():
 with tempfile.TemporaryDirectory() as td:
  a.DB=str(Path(td)/'events.sqlite3'); a.SECRET='test-secret-only'
  def start():
   srv=ThreadingHTTPServer(('127.0.0.1',0),a.Handler); threading.Thread(target=srv.serve_forever,daemon=True).start(); return srv
  def req(url,p):
   b=json.dumps(p,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode(); sig='sha256='+hmac.new(a.SECRET.encode(),b,hashlib.sha256).hexdigest()
   return urllib.request.Request(url,data=b,headers={'Content-Type':'application/json','X-Palang-Signature':sig},method='POST')
  srv=start(); url=f'http://127.0.0.1:{srv.server_address[1]}/v1/events'
  p={'event_id':'synthetic-001','idempotency_key':'synthetic-001','event_type':'USER_INPUT','content':'synthetic-only','parent_event_id':None}
  with urllib.request.urlopen(req(url,p)) as r: first=json.loads(r.read()); assert r.status==201 and first['status']=='QUEUED_AND_READBACK_VERIFIED'
  with urllib.request.urlopen(req(url,p)) as r: second=json.loads(r.read()); assert r.status==200 and second['status']=='duplicate_replay_same_payload'
  try: urllib.request.urlopen(req(url,dict(p,content='different'))); raise AssertionError('expected conflict')
  except urllib.error.HTTPError as e: assert e.code==409
  srv.shutdown(); srv.server_close(); srv=start()
  listing=urllib.request.Request(f'http://127.0.0.1:{srv.server_address[1]}/v1/events',headers={'X-Palang-Signature':'sha256='+hmac.new(a.SECRET.encode(),b'',hashlib.sha256).hexdigest()})
  with urllib.request.urlopen(listing) as r: data=json.loads(r.read()); assert data['count']==1 and data['events'][0]['event_id']=='synthetic-001'
  srv.shutdown(); srv.server_close()
  print('HOST_ADAPTER_TESTS=PASS'); print('synthetic_ingest=PASS'); print('authentication=PASS'); print('durable_readback=PASS'); print('idempotent_retry=PASS'); print('conflicting_retry_rejected=PASS'); print('restart_recovery=PASS'); print('live_chatgpt_producer=NOT_TESTED'); print('repository_write=NOT_IMPLEMENTED')
if __name__=='__main__': main()
