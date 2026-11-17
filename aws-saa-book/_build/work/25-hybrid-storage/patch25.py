import json,sys
fn=sys.argv[1]; m=json.loads(sys.argv[2])
d=json.load(open(fn))
for f in d:
    for v in f['values']:
        if v['display'] in m: v['display']=m[v['display']]
json.dump(d,open(fn,'w'),indent=0,ensure_ascii=False)
