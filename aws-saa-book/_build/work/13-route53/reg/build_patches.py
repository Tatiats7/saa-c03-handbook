"""Build one amend patch per chapter-13 fact from the registrar decisions. Read-only on the canon; writes reg/patches/*.json
and reg/plan.txt (the amend list). Patches: values (display rule), hard (can/cannot rule), exam_relevance (absorbed from
superseded duplicates), claim (manual fixes)."""
import json, re, os, sys, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from saalib import common  # noqa: E402

facts = [json.loads(l) for l in open(os.path.join(ROOT, 'data', 'facts', 'route53.jsonl')) if l.strip()]
byid = {f['id']: f for f in facts}
sup = json.load(open(os.path.join(HERE, 'supersede.json')))
ov = json.load(open(os.path.join(HERE, 'display-overrides.json')))
claims = json.load(open(os.path.join(HERE, 'claim-fixes.json')))
props = json.load(open(os.path.join(HERE, 'proposals.json')))
live = [f for f in facts if f.get('home_chapter') == '13' and f['status'] not in ('rejected', 'superseded') and f['id'] not in sup]

RANK = {'reference': 0, 'extended': 1, 'core': 2}
absorb_rel, absorb_hard = {}, set()
for old, (new, _) in sup.items():
    if new == 'REJECT' or new not in byid or old not in byid:
        continue
    o = byid[old]
    if RANK.get(o.get('exam_relevance'), 0) > RANK.get(absorb_rel.get(new, byid[new].get('exam_relevance')), 0):
        absorb_rel[new] = o['exam_relevance']
    if o.get('hard'):
        absorb_hard.add(new)

HARD = re.compile(r"\b(can|cannot|can't|does not|doesn't|don't|do not|not|no|none|every|all|any|always|never|automatically|requires?|required|must|only|default|free|charges?|charged|billed|minimum|maximum|at least|optional)\b", re.I)

pdir = os.path.join(HERE, 'patches')
if os.path.isdir(pdir):
    shutil.rmtree(pdir)
os.makedirs(pdir)
plan = []
for f in sorted(live, key=lambda x: x['id']):
    patch, why = {}, []
    # displays
    if f['id'] in ov and ov[f['id']].get('KEEP'):
        pass
    elif f['id'] in props or f['id'] in ov:
        vals = props.get(f['id'], {}).get('values') or [dict(key=v['key'], display=v['display']) for v in f['values']]
        old = {v['key']: v for v in f['values']}
        o = ov.get(f['id'], {})
        new = []
        for v in vals:
            if v['key'] in o:
                if o[v['key']] is None:
                    continue
                v = dict(v, display=o[v['key']])
            base = dict(old.get(v['key'], {}))
            base.update(key=v['key'], display=v['display'])
            new.append(base)
        if [(v['key'], v['display']) for v in new] != [(v['key'], v['display']) for v in f['values']]:
            patch['values'] = new
            why.append('displays')
    # claim
    if f['id'] in claims:
        patch['claim'] = claims[f['id']]
        why.append('claim')
    # hard
    claim = patch.get('claim', f['claim'])
    if not f['hard'] and f['kind'] != 'case-study' and (HARD.search(claim) or f['id'] in absorb_hard):
        patch['hard'] = True
        why.append('hard')
    # relevance
    if f['id'] in absorb_rel and absorb_rel[f['id']] != f.get('exam_relevance'):
        patch['exam_relevance'] = absorb_rel[f['id']]
        why.append('relevance')
    if patch:
        json.dump(patch, open(os.path.join(pdir, f['id'] + '.json'), 'w'), indent=1, ensure_ascii=False)
        plan.append('%s %s' % (f['id'], '+'.join(why)))
open(os.path.join(HERE, 'plan.txt'), 'w').write('\n'.join(plan) + '\n')
# sanity: displays held and short
bad = []
for line in plan:
    fid = line.split()[0]
    p = json.load(open(os.path.join(pdir, fid + '.json')))
    if 'values' not in p:
        continue
    f = byid[fid]
    qs = [common.normalize_text(e['quote']) for e in f['evidence']] + [common.normalize_text(e.get('table_header') or '') for e in f['evidence']]
    cl = common.normalize_text(p.get('claim', f['claim']))
    seen = set()
    for v in p['values']:
        d = common.normalize_text(v['display'])
        if d in seen:
            bad.append('%s dup %r' % (fid, v['display']))
        seen.add(d)
        if not re.search(r'\d', v['display']):
            if len(v['display'].split()) > 8:
                bad.append('%s long %r' % (fid, v['display']))
            if not any(d in q for q in qs):
                bad.append('%s notinquote %r' % (fid, v['display']))
        elif not (any(d in q for q in qs) or d in cl):
            bad.append('%s notheld %r' % (fid, v['display']))
    if not p['values']:
        bad.append('%s no values' % fid)
print(len(plan), 'patches;', sum('hard' in l for l in plan), 'hard;', sum('displays' in l for l in plan), 'displays')
print('\n'.join(bad))
