"""Build one amend patch file per fact from spec.json (adjudicate-19). Writes only under the adjudicate folder."""
import json, os, sys

book = sys.argv[1]
here = os.path.join(book, '_build/work/19-containers/adjudicate')
spec = json.load(open(os.path.join(here, 'spec.json')))
facts = {}
fdir = os.path.join(book, 'data/facts')
for fn in sorted(os.listdir(fdir)):
    if fn.endswith('.jsonl'):
        for line in open(os.path.join(fdir, fn)):
            line = line.strip()
            if line:
                f = json.loads(line)
                facts[f['id']] = f

def item(e):
    out = {'source_id': e['source_id'], 'url': e['url'], 'quote': e['quote'], 'table_header': e.get('table_header')}
    if e.get('heading'):
        out['heading'] = e['heading']
    return out

pdir = os.path.join(here, 'patches')
os.makedirs(pdir, exist_ok=True)
amend, reject = [], []
for fid, s in spec.items():
    f = facts[fid]
    if s.get('reject'):
        reject.append(fid)
        continue
    patch = dict(s.get('set', {}))
    if any(k in s for k in ('evidence_set', 'evidence_replace', 'evidence_drop', 'evidence_add')):
        urls = {e['source_id']: e['url'] for e in f['evidence']}
        ev = [item(e) for e in f['evidence']]
        if 'evidence_set' in s:
            ev = []
            for e in s['evidence_set']:
                url = e.get('url')
                if not url or url == 'SAME':
                    url = urls[e['source_id']]
                ev.append(item(dict(e, url=url)))
        for k, q in s.get('evidence_replace', {}).items():
            ev[int(k)]['quote'] = q
        for i in sorted(s.get('evidence_drop', []), reverse=True):
            del ev[i]
        for e in s.get('evidence_add', []):
            url = e.get('url') or urls.get(e['source_id'])
            if not url:
                raise SystemExit('no url for ' + fid + ' ' + e['source_id'])
            it = item(dict(e, url=url))
            if 'pos' in e:
                ev.insert(e['pos'], it)
            else:
                ev.append(it)
        patch['evidence'] = ev
    if not patch:
        raise SystemExit('empty patch ' + fid)
    json.dump(patch, open(os.path.join(pdir, fid + '.json'), 'w'), indent=1, ensure_ascii=False)
    amend.append(fid)
json.dump({'amend': amend, 'reject': reject}, open(os.path.join(here, 'plan.json'), 'w'), indent=1)
print(len(amend), 'patches,', len(reject), 'rejects')
