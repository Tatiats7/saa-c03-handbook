import json,sys,glob
base='/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/data/facts/'
terms=[t.lower() for t in sys.argv[1:]]
n=0
for fn in ['aurora','aurora-serverless']:
    for l in open(base+fn+'.jsonl'):
        f=json.loads(l); n+=1
        txt=(f['claim']+' '+' '.join(e['quote'] for e in f['evidence'])).lower()
        if all(t in txt for t in terms) if terms else True:
            print(f['id'],'|',f['kind'],'|',f['status'],'|',f['claim'][:110])
print('total',n)
