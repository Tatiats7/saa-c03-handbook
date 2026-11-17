import json, sys, os, re
BASE = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'facts')
SVCS = ['storage-gateway', 'datasync', 'snow-family', 'transfer-family']
ids = sys.argv[2:]
out = sys.argv[1]
allf = {}
for s in SVCS:
    for line in open(os.path.join(BASE, s + '.jsonl')):
        line = line.strip()
        if line:
            f = json.loads(line)
            allf[f['id']] = f
o = open(out, 'w')
for i in ids:
    f = allf.get(i)
    if not f:
        o.write('MISSING %s\n' % i)
        continue
    o.write('\n## %s [%s r%d %s hard=%s rel=%s vol=%s tier0=%s author=%s]\n' % (i, f['status'], f['rev'], f['kind'], f['hard'], f.get('exam_relevance'), f.get('volatility'), f.get('tier0'), f.get('author')))
    o.write('C: %s\nQN: %s\n' % (f['claim'], f.get('question')))
    o.write('D: %s\n' % ' || '.join('%s=%s' % (v['key'], v['display']) for v in f['values']))
    o.write('Q: %s\n' % json.dumps(f['qualifiers']))
    o.write('chg: %s items=%s bullets=%s note=%s\n' % (json.dumps(f.get('changed')), f.get('change_items'), f.get('bullets'), f.get('note')))
    for e in f['evidence']:
        o.write('E: %s | hdr=%s | head=%s\n   %s\n' % (e['source_id'], e.get('table_header'), e.get('heading'), e['quote']))
