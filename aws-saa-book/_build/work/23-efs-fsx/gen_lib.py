"""Small helper to write fact JSON files for chapter 23 (work file, not part of the book)."""
import json, re, sys, os

ROOT = 'aws-saa-book/_build/corpus/snap/'
ABS = re.compile(r'\b(only|always|never|cannot|must|by default|up to|at most|not supported)\b', re.I)
HARDKINDS = {'limit', 'quota', 'default', 'restriction', 'price', 'sla', 'change', 'exam-policy'}
_cache = {}


def lines(src):
    if src not in _cache:
        _cache[src] = open(ROOT + src + '.txt', encoding='utf-8').read().split('\n')
    return _cache[src]


def meta_url(src):
    return json.load(open(ROOT + src + '.meta.json'))['url']


def strip_bullet(s):
    return re.sub(r'^\s*[+\-*]\s+', '', s).strip()


def find_line(src, sub, nth=1):
    hits = [i for i, l in enumerate(lines(src)) if sub in l]
    if len(hits) < nth:
        raise SystemExit('NOT FOUND in %s: %r' % (src, sub))
    return hits[nth - 1]


def sent(src, sub, nth=1):
    """sentence of a snapshot line that contains sub"""
    i = find_line(src, sub, nth)
    line = strip_bullet(lines(src)[i])
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"“(*\[])', line)
    for p in parts:
        if sub in p:
            return p.strip()
    raise SystemExit('sentence split failed %s %r' % (src, sub))


def full(src, sub, nth=1):
    return strip_bullet(lines(src)[find_line(src, sub, nth)])


def row(src, sub, nth=1):
    i = find_line(src, sub, nth)
    r = lines(src)[i].strip()
    j = i
    while j > 0 and lines(src)[j - 1].strip().startswith('|'):
        j -= 1
    # header is the first line of the table block unless it is a separator
    hdr = lines(src)[j].strip()
    return r, hdr


def ev(kind, src, sub, nth=1, quote=None):
    if kind == 'sent':
        q, h = sent(src, sub, nth), None
    elif kind == 'full':
        q, h = full(src, sub, nth), None
    elif kind == 'row':
        q, h = row(src, sub, nth)
    elif kind == 'raw':
        q, h = quote, None
    return {'source_id': src, 'url': meta_url(src), 'quote': q, 'table_header': h}


def F(id, svc, kind, claim, question, vals, evs, scope='', dm='', adj=False, cond='', hard=None,
      t0=False, vol='stable', rel='core', bul=(), changed=None, ci=(), note=None, tier=None):
    values = []
    for k, v in enumerate(vals):
        if isinstance(v, str):
            values.append({'key': 'v%d' % (k + 1), 'display': v})
        else:
            d = {'key': v[0], 'display': v[1]}
            if len(v) > 2 and v[2]:
                d['spoken'] = v[2]
            values.append(d)
    if hard is None:
        hard = bool(kind in HARDKINDS or ABS.search(claim) or re.search(r'\d', claim))
    if tier is None:
        s0 = evs[0]['source_id']
        tier = 4 if kind == 'case-study' else (1 if s0.startswith('docs/') or '/whats-new/' in s0 else 2)
    f = {
        'id': id, 'service': svc, 'home_chapter': '23', 'kind': kind, 'claim': claim, 'question': question,
        'values': values, 'qualifiers': {'scope': scope, 'default_or_max': dm, 'adjustable': adj, 'condition': cond},
        'evidence': evs, 'source_tier': tier, 'hard': hard, 'tier0': t0, 'volatility': vol,
        'changed': changed, 'exam_relevance': rel, 'bullets': list(bul), 'change_items': list(ci),
    }
    if note:
        f['note'] = note
    return f


def write(path, facts):
    ids = [f['id'] for f in facts]
    assert len(ids) == len(set(ids)), 'duplicate ids'
    import math
    m = math.ceil(len(facts) / 25)
    if m == 1:
        json.dump(facts, open(path, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
        print('wrote', path, len(facts))
    else:
        k = math.ceil(len(facts) / m)
        for j in range(m):
            c = facts[j * k:(j + 1) * k]
            p = path.replace('.json', '%s.json' % 'abcdefgh'[j])
            json.dump(c, open(p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
            print('wrote', p, len(c))


def hist(src, sub, nth=1):
    return '%s#%d' % (src, find_line(src, sub, nth) + 1)


def wn(svc, url_part):
    for l in open('aws-saa-book/_build/corpus/changes/%s.jsonl' % svc, encoding='utf-8'):
        d = json.loads(l)
        if d.get('id') and url_part in d['url']:
            return d['id']
    raise SystemExit('no whats-new id for %s %s' % (svc, url_part))


def CH(date, was, was_ev):
    return {'date': date, 'was': was, 'was_evidence': was_ev}


def head(src, sub):
    L = lines(src)
    i = next(k for k, l in enumerate(L) if l.startswith('#') and sub in l)
    j = next(k for k in range(i + 1, len(L)) if L[k].strip())
    return {'source_id': src, 'url': meta_url(src), 'quote': L[j].strip(), 'table_header': None,
            'heading': L[i].lstrip('#').strip()}
