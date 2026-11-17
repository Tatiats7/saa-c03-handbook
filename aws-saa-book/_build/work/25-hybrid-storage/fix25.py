import json,re,sys
for fn in sys.argv[1:]:
    d=json.load(open(fn))
    n=0
    for f in d:
        for v in f['values']:
            dp=v['display']
            num=re.search(r'(?<![A-Za-z0-9])\d[\d,.]*(?![A-Za-z])',dp)
            if not num and len(dp.split())>8:
                v['display']=' '.join(dp.split()[:8]).rstrip(',;:')
                n+=1
        if re.search(r'\b(only|always|never|cannot|must|by default|up to|at most|not supported)\b',f['claim'],re.I) and not f['hard']:
            f['hard']=True; n+=1
        if f['hard'] and not f.get('question'):
            print('NOQ',f['id'])
        if f['kind'] in('limit','quota','default') and (not f['qualifiers']['scope'] or not f['qualifiers']['default_or_max']): print('M6',f['id'])
        if len({v['display'] for v in f['values']})<len(f['values']): print('DUPDISP',f['id'])
    json.dump(d,open(fn,'w'),indent=0,ensure_ascii=False)
    print(fn,'fixed',n)
