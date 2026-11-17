"""Apply the registrar plan of chapter 08 (register-08) through saa.py's own CLI entry point.

Each step is exactly one `saa.py facts ...` command, run in-process with saa.main(argv) so the
tool's checks, locks and logs apply unchanged; this only saves the start-up cost of 200 processes.

Usage: python3 aws-saa-book/_build/work/08-edge-protection/reg_apply.py PLAN.json [--dry-run] [--only supersede,reject,amend,conflicts]
Writes a log next to the plan: reg-apply.log (or reg-apply-dry.log).
"""
import contextlib, copy, io, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(BOOK, 'tools'))
import saa  # noqa: E402

plan_path = sys.argv[1]
dry = '--dry-run' in sys.argv
only = None
if '--only' in sys.argv:
    only = set(sys.argv[sys.argv.index('--only') + 1].split(','))
plan = json.load(open(plan_path))
LABEL = plan['label']
log = []


def run(argv):
    buf = io.StringIO()
    code = None
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
        try:
            code = saa.main(argv)
        except SystemExit as e:
            code = e.code
    out = buf.getvalue().strip()
    log.append(f"$ saa.py {' '.join(argv)}\n  exit={code}\n  " + out.replace('\n', '\n  '))
    return code, out


def load_fact(fid):
    for fn in os.listdir(os.path.join(BOOK, 'data', 'facts')):
        if not fn.endswith('.jsonl'):
            continue
        with open(os.path.join(BOOK, 'data', 'facts', fn)) as fh:
            for line in fh:
                if line.strip():
                    f = json.loads(line)
                    if f['id'] == fid:
                        return f
    return None


def want(step):
    return only is None or step in only


if want('supersede'):
    for old, new, why in plan.get('supersede', []):
        f = load_fact(old)
        if f is None or f['status'] in ('rejected', 'superseded'):
            log.append(f"skip supersede {old}: {'missing' if f is None else f['status']}")
            continue
        argv = ['facts', 'amend', old, '--supersede', new, '--relink', '--reason', why, '--by', LABEL]
        if dry:
            argv.append('--dry-run')
        run(argv)

if want('reject'):
    for fid, why in plan.get('reject', []):
        f = load_fact(fid)
        if f is None or f['status'] in ('rejected', 'superseded'):
            log.append(f"skip reject {fid}")
            continue
        argv = ['facts', 'amend', fid, '--reject', '--reason', why, '--by', LABEL]
        if dry:
            argv.append('--dry-run')
        run(argv)

if want('amend'):
    services = ['waf', 'shield', 'firewall-manager', 'network-firewall']
    ids = []
    for s in services:
        with open(os.path.join(BOOK, 'data', 'facts', s + '.jsonl')) as fh:
            for line in fh:
                if line.strip():
                    ids.append(json.loads(line)['id'])
    hard_kinds = set(plan.get('hard_kinds', []))
    patch_dir = os.path.join(HERE, 'reg-patches')
    os.makedirs(patch_dir, exist_ok=True)
    for fid in ids:
        f = load_fact(fid)
        if f['status'] in ('rejected', 'superseded') or f.get('home_chapter') != '08':
            continue
        patch, why = {}, []
        kind = plan.get('kind', {}).get(fid, f['kind'])
        if kind != f['kind']:
            patch['kind'] = kind
            why.append(f"kind {f['kind']} -> {kind}")
        dmap = plan.get('displays', {}).get(fid)
        if dmap:
            vals = []
            for v in f['values']:
                if v['key'] in dmap:
                    nd = dmap[v['key']]
                    if nd is None:
                        continue
                    v = dict(v, display=nd)
                vals.append(v)
            for k, d in dmap.items():
                if k.startswith('+'):
                    vals.append({'key': k[1:], 'display': d})
            if vals != f['values']:
                patch['values'] = vals
                why.append('displays: number-free displays cut to verbatim quote phrases of at most 8 words (RULINGS 2026-10-11)')
        sc = plan.get('scope', {}).get(fid)
        if sc and not (f['qualifiers'].get('scope') or '').strip():
            q = copy.deepcopy(f['qualifiers'])
            q['scope'] = sc
            patch['qualifiers'] = q
            why.append('scope qualifier completed')
        if not f['hard'] and kind in hard_kinds:
            patch['hard'] = True
            why.append(f'hard set for kind {kind} (can/cannot and price claims are hard, RULINGS rule 1)')
        if not patch:
            continue
        p = os.path.join(patch_dir, fid + '.json')
        with open(p, 'w') as fh:
            json.dump(patch, fh, indent=1)
        argv = ['facts', 'amend', fid, '--file', os.path.relpath(p, os.getcwd()), '--reason', '; '.join(why), '--by', LABEL]
        if dry:
            argv.append('--dry-run')
        run(argv)

if want('conflicts') and not dry:
    for cf, why in plan.get('conflicts_both', []):
        run(['facts', 'conflicts', '--resolve', cf, '--both', '--reason', why])

out = os.path.join(HERE, 'reg-apply-dry.log' if dry else 'reg-apply.log')
with open(out, 'a') as fh:
    fh.write('\n'.join(log) + '\n')
fails = [l for l in log if '\n  exit=' in l and '\n  exit=0' not in l and '\n  exit=2' not in l]
print(f"steps={len(log)} failed={len(fails)} log={os.path.relpath(out, os.getcwd())}")
for l in fails:
    print(l.split('\n')[0][:160])
