"""Collect demand -> facts from the miners' notes, follow supersessions, and report what is still uncovered.
Writes reg/demand-map.json; with --apply also writes the statuses into brief.v0.json (using reg/demand-status.json)."""
import json, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
W = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
facts = {}
for svc in ('route53', 'vpc'):
    for l in open(os.path.join(ROOT, 'data', 'facts', svc + '.jsonl')):
        if l.strip():
            f = json.loads(l)
            facts[f['id']] = f


def follow(i):
    seen = set()
    while i in facts and facts[i]['status'] == 'superseded' and i not in seen:
        seen.add(i)
        i = facts[i].get('superseded_by') or i
    return i

m = collections.defaultdict(list)
notes = collections.defaultdict(list)
b = json.load(open(os.path.join(W, 'mine-behavior.json')))
for k, v in b['demand_to_facts'].items():
    m[k] += v
for nf in b['not_found']:
    notes[nf['id']].append('behavior lens not found: %s (%s)' % (nf['part'], nf['result']))
f = json.load(open(os.path.join(W, 'mine-faq.json')))
for k, v in f['demand_map'].items():
    m[k] += v
for k, v in f.get('partial', {}).items():
    notes[k].append('faq lens partial: ' + v)
n = json.load(open(os.path.join(W, 'mine-numbers.json')))
for k, v in n['demand_covered'].items():
    m[k] += v
d = json.load(open(os.path.join(W, 'mine-decisions+changes.json')))
for it in d['demand']:
    m[it['id']] += it['facts']
    if it.get('note'):
        notes[it['id']].append('decisions lens: ' + it['note'])
# also: facts whose own "demand"/question field names a demand id are not recorded; search facts by bullet later
brief = json.load(open(os.path.join(W, 'brief.v0.json')))
out = {}
for it in brief['demand']:
    ids = []
    for i in m.get(it['id'], []):
        j = follow(i)
        if j in facts and facts[j]['status'] not in ('rejected', 'superseded') and j not in ids:
            ids.append(j)
    out[it['id']] = {'bullet': it['bullet'], 'lens': it.get('lens'), 'question': it['question'], 'facts': ids, 'notes': notes.get(it['id'], [])}
json.dump(out, open(os.path.join(HERE, 'demand-map.json'), 'w'), indent=1)
empty = [k for k, v in out.items() if not v['facts']]
print('demand', len(out), 'with facts', len(out) - len(empty), 'empty', len(empty))
for k in empty:
    print(k, out[k]['lens'], '|', out[k]['question'][:200])
if '--apply' in sys.argv:
    st = json.load(open(os.path.join(HERE, 'demand-status.json')))
    for it in brief['demand']:
        o = out[it['id']]
        s = st.get(it['id'], {})
        it['facts'] = s.get('facts', o['facts']) if s.get('facts') is not None else o['facts']
        it['status'] = s.get('status', 'found' if it['facts'] else 'not-found')
        if s.get('note'):
            it['note'] = s['note']
    json.dump(brief, open(os.path.join(W, 'brief.v0.json'), 'w'), indent=1, ensure_ascii=False)
    print('applied', collections.Counter(x['status'] for x in brief['demand']))
