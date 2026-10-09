#!/usr/bin/env python3
"""Retrieve fixed C3 partitions only, no annotation/functional selection."""
import json,os,datetime
from fetch_sources import download,sha256_file,ROOT
p=ROOT+'/data/sources/c3_counts.json'
s=json.load(open(p))
done={r['alias'] for r in s['records'] if r.get('complete')}
for x in json.load(open(ROOT+'/data/sources/c3_selection.json'))['records']:
    if x['alias'] in done:continue
    d=ROOT+'/data/sources/fasta/'+x['alias']
    print('C3 downloading',x['alias'],flush=True)
    n=download(x['url'],d)
    x.update(protein_records=n,bytes=os.path.getsize(d),sha256=sha256_file(d),retrieved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),complete=True)
    s['records'].append(x)
    json.dump(s,open(p,'w'),indent=1)
    print('C3 complete',x['alias'],n,flush=True)
