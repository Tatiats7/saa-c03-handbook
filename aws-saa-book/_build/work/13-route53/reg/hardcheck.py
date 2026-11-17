import json, re, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
facts = [json.loads(l) for l in open(os.path.join(ROOT, 'data', 'facts', 'route53.jsonl')) if l.strip()]
live = [x for x in facts if x.get('home_chapter') == '13' and x['status'] not in ('rejected', 'superseded')]
pat = re.compile(r"\b(can|cannot|can't|does not|doesn't|don't|do not|not|no|every|all|any|automatically|requires?|need|needs|must|only|default|free|charge|charged|minimum|maximum|at least)\b", re.I)
out = collections.defaultdict(list)
for x in live:
    if x['hard']:
        continue
    m = pat.findall(x['claim'])
    key = 'match' if m else 'nomatch'
    out[key].append('%s [%s %s] q=%s :: %s  {%s}' % (x['id'], x['kind'], x.get('exam_relevance'), bool(x.get('question')), x['claim'], ','.join(sorted(set(w.lower() for w in m)))))
with open(os.path.join(HERE, 'hardcheck.txt'), 'w') as f:
    for k in ('match', 'nomatch'):
        f.write('== %s %d\n' % (k, len(out[k])))
        f.write('\n'.join(out[k]) + '\n')
print({k: len(v) for k, v in out.items()})
