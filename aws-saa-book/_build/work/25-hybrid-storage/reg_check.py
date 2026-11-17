import json, sys, os, re, collections, itertools
BASE = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'facts')
SVCS = ['storage-gateway', 'datasync', 'snow-family', 'transfer-family']
out = sys.argv[1]
facts = []
for s in SVCS:
    seen = {}
    for line in open(os.path.join(BASE, s + '.jsonl')):
        line = line.strip()
        if line:
            f = json.loads(line)
            seen[f['id']] = f
    for f in seen.values():
        if f.get('home_chapter') == '25' and f['status'] not in ('rejected', 'superseded'):
            facts.append(f)
ABS = r'\b(only|always|never|cannot|can\'t|must|by default|up to|at most|not supported|no longer)\b'
UNIT = r'\d[\d,.]*\s*(GB|TB|GiB|TiB|PB|PiB|MB|MiB|Mbps|Gbps|MB/s|seconds?|minutes?|hours?|days?|weeks?|months?|years?|%|percent)\b'
def norm(s):
    s = re.sub(r'\]\([^)]*\)', ']', s)
    return re.sub(r'\s+', ' ', s.replace('[', '').replace(']', '')).strip().lower()
o = open(out, 'w')
# displays
for f in facts:
    for v in f['values']:
        d = v['display']
        if not re.search(r'\d', d) and len(d.split()) > 8:
            o.write('LONGDISP %s | %s\n' % (f['id'], d))
    if not f['hard']:
        if re.search(ABS, f['claim'], re.I) or re.search(UNIT, f['claim']):
            o.write('NOTHARD %s | %s\n' % (f['id'], f['claim'][:160]))
    if f['hard'] and not f.get('question'):
        o.write('NOQUESTION %s\n' % f['id'])
    if f['kind'] in ('limit', 'quota', 'default') and not (f['qualifiers'].get('scope') and f['qualifiers'].get('default_or_max')):
        o.write('M6 %s\n' % f['id'])
    if not f['qualifiers'].get('scope'):
        o.write('NOSCOPE %s\n' % f['id'])
    if f['service'] not in f['id']:
        o.write('NS %s\n' % f['id'])
# same quote
byq = collections.defaultdict(list)
for f in facts:
    for e in f['evidence']:
        byq[(e['source_id'], norm(e['quote']))].append(f['id'])
for k, ids in byq.items():
    if len(set(ids)) > 1:
        o.write('SAMEQUOTE %s :: %s\n' % (' , '.join(sorted(set(ids))), k[1][:150]))
# overlapping quotes (one contains the other) within same source
items = [(f['id'], e['source_id'], norm(e['quote'])) for f in facts for e in f['evidence']]
bysrc = collections.defaultdict(list)
for i in items:
    bysrc[i[1]].append(i)
for src, lst in bysrc.items():
    for a, b in itertools.combinations(lst, 2):
        if a[0] == b[0] or a[2] == b[2]:
            continue
        if a[2] in b[2] or b[2] in a[2]:
            o.write('CONTAINS %s <> %s :: %s\n' % (a[0], b[0], (a[2] if len(a[2]) < len(b[2]) else b[2])[:150]))
# claim similarity across sources
def toks(s):
    return set(w for w in re.findall(r'[a-z]+', s.lower()) if len(w) > 2)
bys = collections.defaultdict(list)
for f in facts:
    bys[f['service']].append(f)
for s, lst in bys.items():
    for a, b in itertools.combinations(lst, 2):
        ta, tb = toks(a['claim']), toks(b['claim'])
        if not ta or not tb:
            continue
        j = len(ta & tb) / len(ta | tb)
        if j >= 0.5:
            o.write('SIM %.2f %s <> %s\n' % (j, a['id'], b['id']))
o.close()
