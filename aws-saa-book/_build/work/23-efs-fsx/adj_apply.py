# adjudicate-23 driver: builds amend patches from adj_edits.py and runs saa.py facts amend for each.
# usage: python3 adj_apply.py [--dry-run] [--only ID,ID]
import json, subprocess, sys, os
sys.path.insert(0, 'aws-saa-book/tools')
sys.path.insert(0, 'aws-saa-book/_build/work/23-efs-fsx')
from saalib import corpus
from adj_edits import EDITS, SHARED, RETIRE

DRY = '--dry-run' in sys.argv
ONLY = None
if '--only' in sys.argv:
    ONLY = set(sys.argv[sys.argv.index('--only') + 1].split(','))
WORK = 'aws-saa-book/_build/work/23-efs-fsx/adj-patches'
os.makedirs(WORK, exist_ok=True)
facts = {}
for svc in ('efs', 'fsx'):
    for line in open(f'aws-saa-book/data/facts/{svc}.jsonl'):
        if line.strip():
            f = json.loads(line); facts[f['id']] = f
disputed = json.load(open('aws-saa-book/_build/work/23-efs-fsx/finalize-1.json'))['disputed']
missing = [i for i in disputed if i not in EDITS and i not in RETIRE]
extra = [i for i in list(EDITS) + list(RETIRE) if i not in disputed]
print('missing', missing, 'extra', extra)
log = []
SAA = ['python3', 'aws-saa-book/tools/saa.py']
for fid in disputed:
    if ONLY and fid not in ONLY:
        continue
    f = facts[fid]
    if f.get('status') != 'disputed':
        print('skip', fid, f.get('status')); continue
    if fid in RETIRE:
        how, new, reason = RETIRE[fid]
        cmd = SAA + ['facts', 'amend', fid, '--reason', 'adjudicate-23: ' + reason]
        cmd += ['--reject'] if how == 'reject' else ['--supersede', new]
    else:
        e = EDITS[fid]
        if isinstance(e, str):
            e = SHARED[e]
        patch = {}
        if 'claim' in e: patch['claim'] = e['claim']
        if 'values' in e: patch['values'] = e['values']
        patch.update(e.get('extra') or {})
        if 'add' in e or 'repl' in e:
            ev = [dict(x) for x in f['evidence']]
            for idx, q in (e.get('repl') or {}).items():
                ev[idx]['quote'] = q
            for item in e.get('add', []):
                sid, q = item[0], item[1]
                meta = corpus.load_meta(sid)
                it = {'source_id': sid, 'url': meta['url'], 'quote': q, 'table_header': None}
                if len(item) > 2:
                    it['heading'] = item[2]
                ev.append(it)
            for it in ev:
                for k in ('sha256', 'match', 'title'):
                    it.pop(k, None)
            patch['evidence'] = ev
        pf = f'{WORK}/{fid}.json'
        json.dump(patch, open(pf, 'w'), indent=1, ensure_ascii=False)
        cmd = SAA + ['facts', 'amend', fid, '--file', pf, '--by', 'adjudicate-23',
                     '--reason', 'adjudicate-23: repair after entail/currency dispute (scope, condition or quote added)']
    if DRY:
        cmd.append('--dry-run')
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    log.append({'id': fid, 'rc': r.returncode, 'out': out})
    print(r.returncode, fid, '|', out.replace('\n', ' / ')[:600])
json.dump(log, open(f'{WORK}/_log{"-dry" if DRY else ""}.json', 'w'), indent=1)
