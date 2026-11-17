import json,re,sys
stop=set('which their there these those about would could should being under other while where after before between through using within without across into from that this with have been than then them they also more most only each such when what whose will your you are for the and not can may does doing has had its'.split())
def toks(s): return {w for w in re.findall(r'[a-z0-9]+',s.lower()) if len(w)>3 and w not in stop}
for svc in ['storage-gateway','datasync','snow-family','transfer-family']:
    for line in open('/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/data/facts/%s.jsonl'%svc):
        f=json.loads(line)
        if f.get('author')!='mine-25-behavior+decisions': continue
        if f['status'] in('rejected','superseded'): continue
        q=' '.join(e['quote']+' '+(e.get('table_header') or '') for e in f['evidence'])
        ct=toks(f['claim']); qt=toks(q)
        miss=ct-qt
        # allow plural/stem match
        miss={m for m in miss if not any(m.rstrip('s') in w or w in m for w in qt)}
        if len(ct) and len(miss)/len(ct)>0.3:
            print(round(len(miss)/len(ct),2),f['id'],sorted(miss))
