"""Propose display fixes (number-free displays: verbatim, at most 8 words, no Markdown) for the registrar to review.
Writes proposals.json {id: {"values": [...], "notes": [...]}} and proposals.txt."""
import json, re, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from saalib import common  # noqa: E402

facts = [json.loads(l) for l in open(os.path.join(ROOT, 'data', 'facts', 'route53.jsonl')) if l.strip()]
sup = json.load(open(os.path.join(HERE, 'supersede.json')))
live = [x for x in facts if x.get('home_chapter') == '13' and x['status'] not in ('rejected', 'superseded') and x['id'] not in sup]
overrides = {}
op = os.path.join(HERE, 'display-overrides.json')
if os.path.exists(op):
    overrides = json.load(open(op))

NEG = {"can't", 'cannot', 'not', "doesn't", "don't", 'never', 'only', 'must', 'no', "isn't", "aren't", "won't", 'always', 'all', 'any', 'every', 'default', 'automatically', 'both', 'free', 'charge', 'charges', "didn't", 'without'}
STOP = {'the', 'a', 'an', 'and', 'to', 'of', 'that', 'for', 'in', 'with', 'or', 'by', 'from', 'on', 'as', 'is', 'are', 'it', 'its', 'your', 'you', 'this', 'which', 'when', 'if', 'at', 'be', 'than', 'then', 'there'}


def clean(d):
    d = d.replace('**', '').replace('`', '')
    d = re.sub(r'(?<!\w)\*(\S[^*]*?)\*(?!\w)', r'\1', d)
    d = d.replace('*', '')
    d = re.sub(r'\s+', ' ', d).strip()
    d = d.rstrip('.,;:')
    return d


def held(d, qs, claim):
    nd = common.normalize_text(d)
    return any(nd and nd in q for q in qs)


def best_window(d, keytoks):
    w = d.split()
    best = None
    for n in (8, 7, 6, 5):
        for i in range(0, len(w) - n + 1):
            win = w[i:i + n]
            lw = [re.sub(r'[^a-z\']', '', t.lower()) for t in win]
            s = 0
            s += 5 * sum(1 for t in lw if t in NEG)
            s += 2 * sum(1 for t in lw if t in keytoks)
            if lw[0] in STOP:
                s -= 3
            if lw[-1] in STOP:
                s -= 4
            if win[-1].endswith(',') or win[-1].endswith('('):
                s -= 3
            if '(' in ' '.join(win) and ')' not in ' '.join(win[win.index([t for t in win if '(' in t][0]):]):
                s -= 4
            s += n * 0.5
            if best is None or s > best[0]:
                best = (s, ' '.join(win))
    return best[1].rstrip(',;:(') if best else d


out, txt = {}, []
for x in sorted(live, key=lambda y: y['id']):
    qs = [common.normalize_text(e['quote']) for e in x['evidence']] + [common.normalize_text(e.get('table_header') or '') for e in x['evidence']]
    keytoks = set(re.findall(r'[a-z]+', x['id'].lower())) - STOP - {'route'}
    vals, notes, changed = [], [], False
    for v in x.get('values', []):
        d0 = v['display']
        d = clean(d0)
        if re.search(r'\d', d):
            if d != d0:
                changed = True
                notes.append('cleaned %r' % d0)
            vals.append({'key': v['key'], 'display': d})
            continue
        if len(d.split()) > 8:
            d = best_window(d, keytoks)
        if not held(d, qs, x['claim']):
            notes.append('NOT IN QUOTE: %r' % d)
        if d != d0:
            changed = True
            notes.append('%r -> %r' % (d0, d))
        vals.append({'key': v['key'], 'display': d})
    if x['id'] in overrides:
        vals = overrides[x['id']]
        changed = True
        notes.append('OVERRIDE')
    # dedupe
    seen, dd = set(), []
    for v in vals:
        k = common.normalize_text(v['display'])
        if k in seen:
            changed = True
            notes.append('dropped duplicate %r' % v['display'])
            continue
        seen.add(k)
        dd.append(v)
    if changed:
        out[x['id']] = {'values': dd, 'notes': notes}
        txt.append('%s\n   %s' % (x['id'], '\n   '.join(notes)))
json.dump(out, open(os.path.join(HERE, 'proposals.json'), 'w'), indent=1)
open(os.path.join(HERE, 'proposals.txt'), 'w').write('\n'.join(txt))
print(len(out))
