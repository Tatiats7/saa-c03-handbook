import json, sys, os, re, collections
BASE = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'facts')
SVCS = ['storage-gateway', 'datasync', 'snow-family', 'transfer-family']
out = sys.argv[1]
facts = []
for s in SVCS:
    seen = {}
    for line in open(os.path.join(BASE, s + '.jsonl')):
        line = line.strip()
        if not line:
            continue
        f = json.loads(line)
        seen[f['id']] = f
    for f in seen.values():
        if f.get('home_chapter') == '25':
            facts.append(f)
stat = collections.Counter(f['status'] for f in facts)
with open(out, 'w') as o:
    o.write('TOTAL %d %s\n' % (len(facts), dict(stat)))
    o.write('HARD %d\n' % sum(1 for f in facts if f['hard'] and f['status'] not in ('rejected', 'superseded')))
    o.write('BYSVC %s\n' % dict(collections.Counter(f['service'] for f in facts)))
    o.write('REL %s\n' % dict(collections.Counter(f.get('exam_relevance') for f in facts)))
    for f in sorted(facts, key=lambda x: x['id']):
        if f['status'] in ('rejected', 'superseded'):
            continue
        ev = f['evidence'][0]
        q = re.sub(r'\]\([^)]*\)', ']', ev['quote'])
        o.write('\n## %s [%s r%d %s hard=%s rel=%s vol=%s chg=%s]\n' % (f['id'], f['status'], f['rev'], f['kind'], f['hard'], f.get('exam_relevance'), f.get('volatility'), 'Y' if f.get('changed') else '-'))
        o.write('C: %s\n' % f['claim'])
        o.write('D: %s\n' % ' || '.join(v['display'] for v in f['values']))
        qq = f['qualifiers']
        o.write('Q: scope=%s; dom=%s; cond=%s\n' % (qq.get('scope'), qq.get('default_or_max'), qq.get('condition')))
        o.write('E: %s :: %s%s\n' % (ev['source_id'], q[:400], ' [+%d ev]' % (len(f['evidence']) - 1) if len(f['evidence']) > 1 else ''))
