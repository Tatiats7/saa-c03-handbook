import json, sys, glob
ids = set(sys.argv[1:])
pref = [i[:-1] for i in ids if i.endswith('*')]
for path in glob.glob('aws-saa-book/data/facts/*.jsonl'):
    for line in open(path):
        f = json.loads(line)
        fid = f['id']
        if fid in ids or any(fid.startswith(p) for p in pref):
            print('==', fid, '|', f.get('status', ''), '|', f.get('kind'))
            print('  claim:', f.get('claim'))
            q = f.get('qualifiers') or {}
            if q.get('condition') or q.get('scope'):
                print('  scope:', q.get('scope'), '| cond:', q.get('condition'))
            for e in f.get('evidence', []):
                print('  Q[%s]: %s' % (e.get('source_id'), e.get('quote')))
