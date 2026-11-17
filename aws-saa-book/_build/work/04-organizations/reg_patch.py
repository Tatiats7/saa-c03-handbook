"""register-04: turn reg-spec.json into one full amend patch per fact under reg-patches/.

Checks each new display: at most 8 words when it has no digit, held by a quote of the fact (verbatim), unique.
Usage: python3 aws-saa-book/_build/work/04-organizations/reg_patch.py
"""
import json, os, re, sys, copy
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from saalib import common, lint  # noqa

W = os.path.dirname(os.path.abspath(__file__))
SERV = ['organizations', 'control-tower', 'ram']
facts = {}
for s in SERV:
    with open(os.path.join(ROOT, 'data', 'facts', s + '.jsonl')) as fh:
        for line in fh:
            if line.strip():
                f = json.loads(line)
                facts[f['id']] = f
spec = json.load(open(os.path.join(W, 'reg-spec.json')))
out = os.path.join(W, 'reg-patches')
os.makedirs(out, exist_ok=True)
errors, written = [], []
for fid, s in spec.items():
    if fid.startswith('_'):
        continue
    f = facts.get(fid)
    if f is None or f['status'] in ('rejected', 'superseded'):
        errors.append(f'{fid}: missing or retired')
        continue
    patch = {}
    qs = [common.normalize_text(e['quote']) for e in f['evidence']]
    if 'displays' in s or 'drop' in s:
        vals = copy.deepcopy(f['values'])
        vals = [v for v in vals if v['key'] not in s.get('drop', [])]
        for v in vals:
            if v['key'] in s.get('displays', {}):
                v['display'] = s['displays'][v['key']]
        keys = {v['key'] for v in vals}
        for k in s.get('displays', {}):
            if k not in keys:
                errors.append(f'{fid}: unknown key {k}')
        seen = set()
        for v in vals:
            d = v['display']
            if not re.search(r'\d', d):
                if len(d.split()) > 8:
                    errors.append(f'{fid}[{v["key"]}]: {len(d.split())} words')
                if not any(lint.holds_display(q, common.normalize_text(d)) for q in qs):
                    errors.append(f'{fid}[{v["key"]}]: not in a quote: {d}')
            if d in seen:
                errors.append(f'{fid}: duplicate display {d}')
            seen.add(d)
        patch['values'] = vals
    if 'scope' in s or 'condition' in s:
        q = copy.deepcopy(f['qualifiers'])
        if 'scope' in s:
            q['scope'] = s['scope']
        if 'condition' in s:
            q['condition'] = s['condition']
        patch['qualifiers'] = q
    for k in ('exam_relevance', 'note', 'hard'):
        if k in s:
            patch[k] = s[k]
    with open(os.path.join(out, fid + '.json'), 'w') as fh:
        json.dump(patch, fh, indent=1, ensure_ascii=False)
    written.append(fid)
print(json.dumps({'written': len(written), 'errors': errors}, indent=1))
with open(os.path.join(W, 'reg-patch-ids.txt'), 'w') as fh:
    fh.write('\n'.join(written) + '\n')
