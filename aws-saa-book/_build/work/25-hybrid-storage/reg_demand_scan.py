import json, sys, os, collections
W = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(W, '..', '..', '..')
out = sys.argv[1]
brief = json.load(open(os.path.join(W, 'brief.v0.json')))
facts = {}
for s in ['storage-gateway', 'datasync', 'snow-family', 'transfer-family']:
    for line in open(os.path.join(B, 'data', 'facts', s + '.jsonl')):
        if line.strip():
            f = json.loads(line)
            facts[f['id']] = f
# notes that mention demand ids
bynote = collections.defaultdict(list)
for f in facts.values():
    if f.get('home_chapter') != '25' or f['status'] in ('rejected', 'superseded'):
        continue
    for tok in (f.get('note') or '').replace(',', ' ').split():
        if tok.startswith('d25-'):
            bynote[tok].append(f['id'])
o = open(out, 'w')
st = collections.Counter(d.get('status') for d in brief['demand'])
o.write('keys %s\nstatus %s\n' % (list(brief.keys()), dict(st)))
for d in brief['demand']:
    fs = d.get('facts') or []
    missing = [x for x in fs if x not in facts]
    dead = [x for x in fs if x in facts and facts[x]['status'] in ('rejected', 'superseded')]
    o.write('%s [%s] bullet=%s n=%d note=%d miss=%s dead=%s | %s\n' % (d['id'], d.get('status'), d.get('bullet'), len(fs), len(bynote.get(d['id'], [])), missing, dead, d['question'][:150]))
o.write('\nfirst item: %s\n' % json.dumps(brief['demand'][0])[:800])
