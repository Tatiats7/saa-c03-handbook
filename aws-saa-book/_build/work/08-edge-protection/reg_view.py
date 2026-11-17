"""Registrar view of chapter 05 facts (register-05). Read-only: prints a compact table and flags.

Usage: python3 aws-saa-book/_build/work/05-identity-federation/reg_view.py MODE [--out FILE]
MODE: table | flags | dups | ns
"""
import json, re, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from saalib import common, lint  # noqa

SERV = ['waf', 'shield', 'firewall-manager', 'network-firewall']
CH = '08'
WDIR = '08-edge-protection'
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
    if mode == 'dq':
        # number-free displays that are too long or not verbatim in a quote, with the quotes
        for f in L:
            qs = [common.normalize_text(e['quote']) for e in f['evidence']]
            bad = []
            for v in f['values']:
                d = v['display']
                if re.search(r'\d', d):
                    continue
                n = len(d.split())
                held_q = any(lint.holds_display(q, common.normalize_text(d)) for q in qs)
                if n > 8 or not held_q:
                    bad.append(f"  [{v['key']}] ({n}w,{'Q' if held_q else 'noQ'}) {d}")
            if bad:
                lines.append(f"## {f['id']}")
                lines += bad
                for i, e in enumerate(f['evidence']):
                    lines.append(f"  Q{i}: {e['quote']}" + (f" [H:{e.get('heading')}]" if e.get('heading') else ''))
    elif mode == 'hard':
        # facts with hard false: would the can/cannot rule raise them?
        rx = re.compile(r"\b(can|can't|cannot|does not|doesn't|do not|don't|not|no)\b", re.I)
        for f in L:
            if f['hard']:
                continue
            why = 'capability' if f['kind'] == 'capability' else ('word:' + rx.search(f['claim']).group(0) if rx.search(f['claim']) else '')
            lines.append(f"{'RAISE' if why else 'keep '} {f['id']} | {f['kind']} | {why} | q={'Y' if f.get('question') else '-'} | {f['claim']}")
    elif mode == 'table':
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
                if a['service'] != b['service']:
                    continue
                if not ta or not tb:
                    continue
                jac = len(ta & tb) / len(ta | tb)
                sameq = any(e['quote'] == g['quote'] for e in a['evidence'] for g in b['evidence'])
                if jac >= thr or sameq:
                    lines.append(f"{jac:.2f} {'SAMEQ ' if sameq else ''}{a['id']} <> {b['id']}\n   A: {a['claim']}\n   B: {b['claim']}")
    elif mode == 'ev':
        want = [a for a in sys.argv[2:] if not a.startswith('--') and a != outp]
        by = {f['id']: f for f in facts}
        for w in want:
            f = by[w]
            lines.append(f"## {w} [{f['status']}] {f['author']} rel={f.get('exam_relevance')} h={f['hard']} q={f.get('question')}")
            lines.append(f"   claim: {f['claim']}")
            lines.append(f"   values: {json.dumps(f['values'])}  qual: {json.dumps(f['qualifiers'])}")
            for e in f['evidence']:
                lines.append(f"   - {e['source_id']}: {e['quote']}" + (f" [H:{e.get('heading')}]" if e.get('heading') else ''))
    elif mode == 'demand':
        W = os.path.join(ROOT, '_build', 'work', WDIR)
        brief = json.load(open(os.path.join(W, 'brief.v0.json')))
        by = {f['id']: f for f in facts}
        # miner maps
        mm = {}
        for fn in sorted(os.listdir(W)):
            if fn.startswith('mine-') and fn.endswith('.json') and fn != 'mine-plan.json':
                d = json.load(open(os.path.join(W, fn)))
                for k, v in d.items():
                    if isinstance(v, dict) and k not in ('summary',):
                        for dk, dv in v.items():
                            if re.match(r'd\d{3}$', dk) and isinstance(dv, dict):
                                mm.setdefault(dk, []).append((fn, dv.get('status'), dv.get('facts', []), dv.get('note') or dv.get('not_found') or ''))
                    if re.match(r'd\d{3}$', k) and isinstance(v, dict):
                        mm.setdefault(k, []).append((fn, v.get('status'), v.get('facts', []), v.get('note') or v.get('not_found') or ''))
        # facts by note tag
        tag = {}
        for f in facts:
            for m in re.findall(r'd\d{3}', str(f.get('note') or '')):
                tag.setdefault(m, []).append(f['id'])
        from collections import Counter
        lines.append('BRIEF STATUS ' + str(Counter(d['status'] for d in brief['demand'])))
        for d in brief['demand']:
            ids = list(d.get('facts') or [])
            dead = [i for i in ids if i in by and by[i]['status'] in ('rejected', 'superseded')]
            livef = [i for i in ids if i in by and by[i]['status'] not in ('rejected', 'superseded')]
            other = [i for i in ids if i not in by]
            ms = '; '.join(f"{fn}:{st}:{len(fs)}" for fn, st, fs, _ in mm.get(d['id'], []))
            lines.append(f"{d['id']} [{d['status']}] {d['bullet']} live={len(livef)} dead={dead} other={other} tagged={len(tag.get(d['id'], []))} miners=({ms}) Q: {d['question']}")
            if 'all' in sys.argv:
                for fn, st, fs, note in mm.get(d['id'], []):
                    if note:
                        lines.append(f"     {fn}: {note}")
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
        # facts of other namespaces (iam-idc-*, etc.) that mention our services
        other = []
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
                    if re.search(r'\bWAF\b|Shield|Firewall Manager|Network Firewall', c):
                        other.append(f"{f['id']} ({f['home_chapter']}, {f['status']}): {c}")
        lines += other
        for f in L:
            ok = f['id'].startswith(f['service'] + '-')
            if not ok or f['home_chapter'] != CH:
                lines.append(f"NSBAD {f['id']} svc={f['service']} home={f['home_chapter']}")
    text = '\n'.join(lines) + '\n'
    if outp:
        with open(outp, 'w') as fh:
            fh.write(text)
        print(f'wrote {outp} ({len(lines)} lines)')
    else:
        print(text)


main()
