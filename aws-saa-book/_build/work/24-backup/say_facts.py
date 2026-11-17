import json, sys, glob
ids = set(sys.argv[1:])
for f in glob.glob('aws-saa-book/data/facts/*.jsonl'):
    for line in open(f):
        line = line.strip()
        if not line:
            continue
        d = json.loads(line)
        if d.get('id') in ids:
            print('==', d['id'], d.get('status'), 'svc=' + str(d.get('service')))
            print('  claim:', d.get('claim'))
            print('  values:', json.dumps(d.get('values'), ensure_ascii=False))
            for e in d.get('evidence') or []:
                print('  quote:', e.get('quote'))
            ids.discard(d['id'])
print('MISSING', sorted(ids))
