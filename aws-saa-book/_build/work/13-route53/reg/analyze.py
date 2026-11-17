"""Read-only analysis of chapter 13 facts for the registrar. Writes reports next to this file."""
import json, re, sys, collections, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
facts = []
with open(os.path.join(ROOT, 'data', 'facts', 'route53.jsonl')) as f:
    for line in f:
        line = line.strip()
        if line:
            facts.append(json.loads(line))
live = [x for x in facts if x.get('home_chapter') == '13' and x['status'] not in ('rejected', 'superseded')]
byid = {x['id']: x for x in facts}


def norm(s):
    s = (s or '').lower()
    s = re.sub(r'[*_`]', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()


def toks(s):
    return set(re.findall(r'[a-z]+', re.sub(r'\S*\d\S*', ' ', (s or '').lower())))

out = []
out.append('live facts: %d' % len(live))
out.append('status: %s' % collections.Counter(x['status'] for x in facts if x.get('home_chapter') == '13'))
out.append('kinds: %s' % collections.Counter(x['kind'] for x in live))
out.append('hard: %s' % collections.Counter(x['hard'] for x in live))
out.append('exam_relevance: %s' % collections.Counter(x.get('exam_relevance') for x in live))
out.append('authors: %s' % collections.Counter(x.get('author') for x in live))
out.append('services: %s' % collections.Counter(x.get('service') for x in live))

# duplicate quotes
q2 = collections.defaultdict(list)
for x in live:
    for e in x['evidence']:
        q2[(e['source_id'], norm(e['quote']))].append(x['id'])
groups = []
seen = set()
for k, ids in q2.items():
    ids = sorted(set(ids))
    if len(ids) > 1:
        groups.append(('same-quote', k[0], k[1][:160], ids))
# containment within same source
bysrc = collections.defaultdict(list)
for x in live:
    for e in x['evidence']:
        bysrc[e['source_id']].append((x['id'], norm(e['quote'])))
for src, lst in bysrc.items():
    for i, (a, qa) in enumerate(lst):
        for b, qb in lst[i + 1:]:
            if a == b or qa == qb:
                continue
            if qa in qb or qb in qa:
                groups.append(('contained', src, (qa if len(qa) < len(qb) else qb)[:160], sorted([a, b])))
out.append('\n== duplicate quote groups: %d' % len(groups))
for g in groups:
    out.append('%s | %s | %s\n   %s' % (g[0], g[1], ' ; '.join(g[3]), g[2]))

# claim similarity
pairs = []
for i, a in enumerate(live):
    ta = toks(a['claim'])
    for b in live[i + 1:]:
        tb = toks(b['claim'])
        if not ta or not tb:
            continue
        j = len(ta & tb) / len(ta | tb)
        if j >= 0.55:
            pairs.append((round(j, 2), a['id'], b['id']))
pairs.sort(reverse=True)
out.append('\n== similar claims (jaccard>=0.55): %d' % len(pairs))
for p in pairs:
    out.append('%s %s | %s' % p)

# hard consistency
absw = ['only', 'always', 'never', 'cannot', "can't", 'must', 'by default', 'up to', 'at most', 'not supported']
need = {'limit', 'quota', 'default', 'restriction', 'price', 'sla', 'change', 'exam-policy'}
out.append('\n== hard false but has absolute word or number with unit:')
for x in live:
    if not x['hard']:
        c = ' ' + x['claim'].lower() + ' '
        hits = [w for w in absw if re.search(r'\b' + re.escape(w) + r'\b', c)]
        cc = re.sub(r'Route 53|S3|EC2|IPv4|IPv6|AAAA|us-east-1|us-west-2|ps5|PS5|EDNS0|P-256|P256|ECC_NIST_P256|\b[A-Z]+\d+\b', ' ', x['claim'])
        if re.search(r'\d', cc):
            hits.append('digit')
        if hits or x['kind'] in need:
            out.append('%s %s %s' % (x['id'], x['kind'], hits))
out.append('\n== hard true by kind/claim stats (behavior/capability hard false count): %d' % sum(1 for x in live if not x['hard']))

# displays
out.append('\n== number-free displays >8 words or not verbatim in a quote:')
for x in live:
    qs = [norm(e['quote']) for e in x['evidence']] + [norm(e.get('table_header') or '') for e in x['evidence']]
    for v in x.get('values', []):
        d = v['display']
        if re.search(r'\d', d):
            continue
        nd = norm(d)
        words = len(d.split())
        inq = any(nd in q for q in qs)
        if words > 8 or not inq:
            out.append('%s [%s] %dw inquote=%s: %s' % (x['id'], v['key'], words, inq, d))
out.append('\n== single-display facts: %d' % sum(1 for x in live if len(x.get('values', [])) < 2))
out.append('\n== qualifiers missing scope:')
for x in live:
    q = x.get('qualifiers') or {}
    if not q.get('scope'):
        out.append('%s %s' % (x['id'], x['kind']))
out.append('\n== no question on hard:')
for x in live:
    if x['hard'] and not x.get('question'):
        out.append(x['id'])

with open(os.path.join(HERE, 'analysis.txt'), 'w') as f:
    f.write('\n'.join(out))

# compact dump
with open(os.path.join(HERE, 'dump.txt'), 'w') as f:
    for x in sorted(live, key=lambda y: y['id']):
        f.write('## %s [%s h=%s %s %s] %s\n' % (x['id'], x['kind'], x['hard'], x.get('exam_relevance'), x.get('author'), x['claim']))
        f.write('   D: %s\n' % ' || '.join(v['display'] for v in x.get('values', [])))
        q = x.get('qualifiers') or {}
        f.write('   Q: %s\n' % json.dumps(q))
        for e in x['evidence']:
            f.write('   E: %s :: %s%s\n' % (e['source_id'], e['quote'][:400], ('  [H: %s]' % e['table_header'][:120]) if e.get('table_header') else ''))
        if x.get('changed'):
            f.write('   C: %s\n' % json.dumps(x['changed']))

# conflicts for route53
cf = json.load(open(os.path.join(HERE, 'conflicts.json')))
items = cf if isinstance(cf, list) else cf.get('conflicts', cf)
lines = []
for c in items:
    if c.get('status') == 'open' and any(i.startswith('route53-') for i in c['facts']):
        a, b = c['facts']
        lines.append('%s %s | %s' % (c['id'], a, b))
        for i in (a, b):
            x = byid.get(i)
            if x:
                lines.append('   %s [%s %s]: %s' % (i, x['status'], x['kind'], x['claim']))
                lines.append('      Q: %s' % x['evidence'][0]['quote'][:300])
with open(os.path.join(HERE, 'conflicts-open.txt'), 'w') as f:
    f.write('\n'.join(lines))

# candidate duplicate clusters (union-find over same-quote, contained, and jaccard>=0.6 non-quota pairs)
parent = {}
def find(a):
    parent.setdefault(a, a)
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a
def union(a, b):
    parent[find(a)] = find(b)
for g in groups:
    ids = g[3]
    for i in ids[1:]:
        union(ids[0], i)
for j, a, b in pairs:
    if j >= 0.6 and not (byid[a]['kind'] in ('quota', 'limit') and byid[b]['kind'] in ('quota', 'limit')):
        union(a, b)
clusters = collections.defaultdict(list)
for k in list(parent):
    clusters[find(k)].append(k)
def entry(x):
    s = '## %s [%s h=%s %s %s r%s] %s\n' % (x['id'], x['kind'], x['hard'], x.get('exam_relevance'), x.get('author'), x['rev'], x['claim'])
    s += '   D: %s\n' % ' || '.join('%s=%s' % (v['key'], v['display']) for v in x.get('values', []))
    for e in x['evidence']:
        s += '   E: %s :: %s%s\n' % (e['source_id'].replace('docs/Route53/latest/DeveloperGuide/', 'DG/'), e['quote'][:300], ('  [H: %s]' % e['table_header'][:100]) if e.get('table_header') else '')
    return s
with open(os.path.join(HERE, 'clusters.txt'), 'w') as f:
    n = 0
    for k, ids in sorted(clusters.items(), key=lambda kv: sorted(kv[1])[0]):
        if len(ids) < 2:
            continue
        n += 1
        f.write('=== C%03d (%d)\n' % (n, len(ids)))
        for i in sorted(ids):
            f.write(entry(byid[i]))
print('ok', len(live), len(groups), len(pairs), len(lines))
