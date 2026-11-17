"""Registrar view of chapter 04 facts (register-04). Read-only: prints a compact table and flags.
Adapted from the chapter 05 registrar view.

Usage: python3 aws-saa-book/_build/work/04-organizations/reg_view.py MODE [--out FILE]
MODE: table | flags | dups [thr] | ev ID ... | demand [all] | cf | ns
"""
import json, re, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from saalib import common, lint  # noqa

SERV = ['organizations', 'control-tower', 'ram']
CH = '04'
WDIR = '04-organizations'
ABS = ["only", "always", "never", "cannot", "must", "by default", "up to", "at most", "not supported"]


def load(svc):
    out = []
    p = os.path.join(ROOT, 'data', 'facts', svc + '.jsonl')
    with open(p) as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def live(f):
    return f.get('status') not in ('rejected', 'superseded')


def toks(s):
    return set(w for w in re.findall(r'[a-z]+', re.sub(r'\S*\d\S*', ' ', s.lower())) if len(w) > 2)


def has_abs(s):
    for w in ABS:
        if re.search(r'(?<![A-Za-z0-9-])' + re.escape(w) + r'(?![A-Za-z0-9-])', s, re.I):
            return w
    return None


def main():
    mode = sys.argv[1]
    outp = None
    if '--out' in sys.argv:
        outp = sys.argv[sys.argv.index('--out') + 1]
    lines = []
    facts = []
    for s in SERV:
        facts += load(s)
    L = [f for f in facts if live(f)]
    if mode == 'table':
        for f in L:
            ds = ' || '.join(v['display'] for v in f['values'])
            lines.append(f"{f['id']} | {f['kind']} | h={int(f['hard'])} | {f.get('exam_relevance')} | {f.get('volatility')} | ch={'Y' if f.get('changed') else '-'} | {f['claim']} | D: {ds} | S: {f['qualifiers'].get('scope')} | B: {','.join(f.get('bullets') or [])} | n={f.get('note')}")
    elif mode == 'flags':
        for f in L:
            qs = [common.normalize_text(e['quote']) for e in f['evidence']]
            for v in f['values']:
                d = v['display']
                if not re.search(r'\d', d):
                    n = len(d.split())
                    held_q = any(lint.holds_display(q, common.normalize_text(d)) for q in qs)
                    if n > 8 or not held_q:
                        lines.append(f"DISPLAY {f['id']} [{v['key']}] words={n} inquote={held_q}: {d}")
            a = has_abs(f['claim'])
            if a and not f['hard']:
                lines.append(f"HARD? {f['id']} abs='{a}'")
            if f['hard'] and not f.get('question'):
                lines.append(f"QUESTION {f['id']}")
            if f['kind'] in ('limit', 'quota', 'default') and not f['qualifiers'].get('default_or_max'):
                lines.append(f"QUAL {f['id']}")
            if not f['qualifiers'].get('scope'):
                lines.append(f"SCOPE {f['id']}")
            if f.get('exam_relevance') not in ('core', 'extended', 'reference'):
                lines.append(f"REL {f['id']} {f.get('exam_relevance')}")
        from collections import Counter
        lines.append('STATUS ' + str(Counter(f['status'] for f in facts)))
        lines.append('REL ' + str(Counter(f.get('exam_relevance') for f in L)))
        lines.append('KIND ' + str(Counter(f['kind'] for f in L)))
        lines.append('HARD ' + str(Counter(f['hard'] for f in L)))
    elif mode == 'dups':
        thr = float(sys.argv[2]) if len(sys.argv) > 2 and not sys.argv[2].startswith('--') else 0.5
        T = [(f, toks(f['claim'])) for f in L]
        for i in range(len(T)):
            for j in range(i + 1, len(T)):
                a, ta = T[i]; b, tb = T[j]
                if not ta or not tb:
                    continue
                jac = len(ta & tb) / len(ta | tb)
                sameq = any(e['quote'] == g['quote'] for e in a['evidence'] for g in b['evidence'])
                if jac >= thr or sameq:
                    lines.append(f"{jac:.2f} {'SAMEQ ' if sameq else ''}{a['id']} <> {b['id']}")
    elif mode == 'ev':
        want = [a for a in sys.argv[2:] if not a.startswith('--') and a != outp]
        by = {f['id']: f for f in facts}
        for w in want:
            f = by[w]
            lines.append(f"## {w} [{f['status']}] {f['author']} rel={f.get('exam_relevance')} h={f['hard']} q={f.get('question')}")
            lines.append(f"   claim: {f['claim']}")
            lines.append(f"   values: {json.dumps(f['values'])}  qual: {json.dumps(f['qualifiers'])} changed: {json.dumps(f.get('changed'))} vol: {f.get('volatility')}")
            for e in f['evidence']:
                lines.append(f"   - {e['source_id']}: {e['quote']}" + (f" [H:{e.get('heading')}]" if e.get('heading') else '') + (f" [T:{e.get('table_header')}]" if e.get('table_header') else ''))
    elif mode == 'demand':
        W = os.path.join(ROOT, '_build', 'work', WDIR)
        brief = json.load(open(os.path.join(W, 'brief.v0.json')))
        by = {f['id']: f for f in facts}
        from collections import Counter
        lines.append('BRIEF STATUS ' + str(Counter(d['status'] for d in brief['demand'])))
        for d in brief['demand']:
            ids = list(d.get('facts') or [])
            dead = [i for i in ids if i in by and by[i]['status'] in ('rejected', 'superseded')]
            livef = [i for i in ids if i in by and by[i]['status'] not in ('rejected', 'superseded')]
            other = [i for i in ids if i not in by]
            if 'all' in sys.argv or d['status'] != 'found' or dead or other or not livef:
                lines.append(f"{d['id']} [{d['status']}] {d['bullet']} live={len(livef)} dead={dead} other={other} Q: {d['question']} N: {d.get('note') or ''}")
    elif mode == 'cf':
        ids = {f['id'] for f in facts}
        with open(os.path.join(ROOT, '_build', 'facts', 'conflicts.jsonl')) as fh:
            for line in fh:
                if not line.strip():
                    continue
                r = json.loads(line)
                if any(i in ids for i in r['facts']):
                    lines.append(f"{r['id']} {r['status']} {' / '.join(r['facts'])} {r.get('reason') or ''}")
    elif mode == 'ns':
        for f in L:
            ok = f['id'].startswith(f['service'] + '-')
            if not ok or f['home_chapter'] != CH:
                lines.append(f"NSBAD {f['id']} svc={f['service']} home={f['home_chapter']}")
        d = os.path.join(ROOT, 'data', 'facts')
        for fn in sorted(os.listdir(d)):
            if not fn.endswith('.jsonl') or fn[:-6] in SERV:
                continue
            with open(os.path.join(d, fn)) as fh:
                for line in fh:
                    if not line.strip():
                        continue
                    f = json.loads(line)
                    if not live(f):
                        continue
                    c = f['claim']
                    if re.search(r'AWS Organizations|Control Tower|Resource Access Manager|AWS RAM|service control polic|\bSCPs?\b|resource control polic|\bRCPs?\b', c):
                        lines.append(f"OTHER {f['id']} ({f['home_chapter']}, {f['status']}): {c}")
    text = '\n'.join(lines) + '\n'
    if outp:
        with open(outp, 'w') as fh:
            fh.write(text)
        print(f'wrote {outp} ({len(lines)} lines)')
    else:
        print(text)


main()
