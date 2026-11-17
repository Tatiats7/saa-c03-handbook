"""register-05: build amend patches from reg-spec.json into reg-patches/ and check displays. Prints one line per patch."""
import json, os, re, sys, copy
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from saalib import common, lint  # noqa

W = os.path.dirname(os.path.abspath(__file__))
spec = json.load(open(os.path.join(W, 'reg-spec.json')))
facts = {}
for s in ('iam-identity-center', 'directory-service', 'cognito'):
    for line in open(os.path.join(ROOT, 'data', 'facts', s + '.jsonl')):
        if line.strip():
            f = json.loads(line)
            facts[f['id']] = f
out = os.path.join(W, 'reg-patches')
os.makedirs(out, exist_ok=True)
ids = sorted(set(spec['scope']) | set(spec['display']) | set(spec['extra']))
for fid in ids:
    f = facts[fid]
    if f['status'] in ('rejected', 'superseded'):
        print('SKIP dead', fid)
        continue
    p = {}
    ex = spec['extra'].get(fid, {})
    if fid in spec['scope'] or 'qualifiers' in ex:
        q = copy.deepcopy(ex.get('qualifiers') or f['qualifiers'])
        if fid in spec['scope']:
            q['scope'] = spec['scope'][fid]
        if q != f['qualifiers']:
            p['qualifiers'] = q
    vals = copy.deepcopy(ex.get('values') or f['values'])
    for k, d in spec['display'].get(fid, {}).items():
        for v in vals:
            if v['key'] == k:
                v['display'] = d
    vals += ex.get('values_add', [])
    if vals != f['values']:
        p['values'] = vals
    for k in ('claim', 'exam_relevance', 'note', 'hard'):
        if k in ex:
            p[k] = ex[k]
    ev = f['evidence']
    if 'evidence_keep' in ex:
        ev = [f['evidence'][i] for i in ex['evidence_keep']]
        p['evidence'] = ev
    qs = [common.normalize_text(e['quote']) for e in ev]
    probs = []
    for v in (p.get('values') or f['values']):
        d = v['display']
        if not re.search(r'\d', d):
            if len(d.split()) > 8:
                probs.append(f'long:{d}')
            if not any(lint.holds_display(q, common.normalize_text(d)) for q in qs):
                probs.append(f'notinquote:{d}')
    if p.get('hard') and not f.get('question'):
        probs.append('no-question')
    json.dump(p, open(os.path.join(out, fid + '.json'), 'w'), indent=1, ensure_ascii=False)
    light = all(k in ('exam_relevance', 'tier0', 'question', 'note') for k in p)
    print(f"{'LIGHT' if light else 'REV'} {fid} keys={','.join(sorted(p))} {' '.join(probs)}")
