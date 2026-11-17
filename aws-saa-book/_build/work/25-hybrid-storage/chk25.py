import json,re,sys
for fn in sys.argv[1:]:
    d=json.load(open(fn))
    print(fn,len(d),'facts')
    ids=set()
    for f in d:
        if f['id'] in ids: print('DUP',f['id'])
        ids.add(f['id'])
        for v in f['values']:
            dp=v['display']
            num=re.search(r'(?<![A-Za-z0-9])\d[\d,.]*(?![A-Za-z])',dp)
            if not num and len(dp.split())>8: print('LONG',f['id'],'|',dp)
        if len(f['values'])<2 and f['kind'] in('behavior','capability'): print('ONEDISP',f['id'])
        q=f['evidence'][0]['quote']
        for v in f['values']:
            import unicodedata
            norm=lambda s: re.sub(r'\s+',' ',s).lower()
            if norm(v['display']) not in norm(q) and norm(v['display']) not in norm(f['claim']): print('NOTHELD',f['id'],'|',v['display'])
    for f in d:
        if not f['hard']:
            m=re.findall(r'\b(only|always|never|cannot|must|by default|up to|at most|not supported)\b',f['claim'],re.I)
            if m: print('HARD?',f['id'],m)
            if re.search(r'\d+\s*(GB|TB|GiB|TiB|MB|Mbps|Gbps|seconds|minutes|hours|days|months|years|%|percent)',f['claim']): print('HARD(unit)?',f['id'])
