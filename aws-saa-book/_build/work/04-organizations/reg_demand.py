"""register-04: write demand statuses and fact lists into brief.v0.json from the three miner notes.

Superseded fact ids are replaced by their successor; ids that do not exist are dropped.
Status: found (live facts, no open gap), partial (facts plus a stated gap), not-found (no fact).
Usage: python3 aws-saa-book/_build/work/04-organizations/reg_demand.py
"""
import json, os, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
W = os.path.dirname(os.path.abspath(__file__))

facts = {}
for p in glob.glob(os.path.join(ROOT, 'data', 'facts', '*.jsonl')):
    with open(p) as fh:
        for line in fh:
            if line.strip():
                f = json.loads(line)
                facts[f['id']] = f


def live_id(i):
    seen = set()
    while i in facts and facts[i]['status'] == 'superseded' and i not in seen:
        seen.add(i)
        i = facts[i].get('superseded_by') or i
    if i not in facts or facts[i]['status'] in ('rejected', 'superseded'):
        return None
    return i


miners = {}
for fn in ('mine-behavior+decisions.json', 'mine-faq.json', 'mine-numbers+changes.json'):
    d = json.load(open(os.path.join(W, fn)))
    for k, v in (d.get('demand') or {}).items():
        miners.setdefault(k, []).append((fn, v))

# registrar additions and resolutions (targeted search of 2026-10-12)
REG = {
    'd083': {'add': ['ram-share-prefix-lists-any-account', 'ram-share-ipam-pools-any-account', 'ram-share-license-configurations-any-account'],
             'status': 'found', 'note': 'register-04: shareable rows adopted from docs/ram/latest/userguide/shareable (prefix lists, IPAM pools, License Manager) next to subnets, transit gateways, Resolver rules, Aurora clusters and security groups.'},
    'd093': {'add': ['ram-faq-stop-sharing', 'ram-account-leaving-org-loses-access', 'ram-disable-trusted-access-removes-org-principals'],
             'status': 'found', 'note': 'register-04: stop sharing (FAQ), loss of access when a consumer leaves the organization (getting-started-sharing), removal of org principals when trusted access is disabled.'},
    'd124': {'add': ['ram-share-subnets-only-within-organization', 'ram-share-transit-gateway-any-account', 'ram-share-prefix-lists-any-account'],
             'status': 'found', 'note': 'register-04: the FAQ points to the shareable-resources page; its rows are in the canon (see d083).'},
    'd007': {'add': ['organizations-faq-hierarchy-five-levels-including-root-and-accounts'],
             'note': 'register-04: teach the quotas-page wording (five levels of OUs under a root); the FAQ counts the root and accounts in the five levels.'},
    'd066': {'add': ['control-tower-lz4-mandatory-not-default'],
             'note': 'register-04: mandatory controls are always applied up to landing zone 3.x; from landing zone 4.0 they are no longer applied by default. Teach both with the version.'},
    'd078': {'add': ['control-tower-lz4-mandatory-not-default']},
    'd130': {'note': 'register-04: rename date of guardrail to control is not on any saved page (miner searched doc history, terminology, change feed); teach "control (formerly guardrail)" without a date.'},
    'd036': {'note': 'register-04: SCP example library moved to GitHub (not on the allow-list); CloudTrail/Config/GuardDuty protection examples stay unfilled. Use the Control Tower mandatory log-archive and CloudTrail controls instead.'},
    'd037': {'note': 'register-04: no saved AWS page holds an SCP example that requires tags; teach the aws:PrincipalArn exemption only.'},
    'd113': {'note': 'register-04: Sixth Street snapshot is the generic listing; use Volkswagen Financial Services (d114) and Norstella (d115).'},
    'd135': {'note': 'register-04: no saved page defines multi-party approval for Organizations; leave out of the chapter (low exam relevance).'},
}

brief_path = os.path.join(W, 'brief.v0.json')
brief = json.load(open(brief_path))
counts = {}
for d in brief['demand']:
    ids, gaps, notes = [], [], []
    for fn, v in miners.get(d['id'], []):
        for i in v.get('facts') or []:
            j = live_id(i)
            if j and j not in ids:
                ids.append(j)
        st = (v.get('status') or '').lower()
        if v.get('not_found'):
            gaps.append(f"{fn.replace('.json', '')}: {v['not_found']}")
        elif st in ('partial', 'partly not found', 'not-found', 'not found'):
            gaps.append(f"{fn.replace('.json', '')}: {st}")
        if v.get('note'):
            notes.append(f"{fn.replace('.json', '')}: {v['note']}")
    r = REG.get(d['id'], {})
    for i in r.get('add', []):
        j = live_id(i)
        if j and j not in ids:
            ids.append(j)
    if r.get('status'):
        status = r['status']
        gaps = []
    elif not ids:
        status = 'not-found'
    elif gaps:
        status = 'partial'
    else:
        status = 'found'
    if r.get('note'):
        notes.append(r['note'])
    d['status'] = status
    d['facts'] = ids
    if gaps:
        d['gaps'] = gaps
    elif 'gaps' in d:
        del d['gaps']
    if notes:
        d['register_note'] = ' | '.join(notes)
    counts[status] = counts.get(status, 0) + 1
brief['registered_by'] = 'register-04'
brief['registered_at'] = '2026-10-12'
with open(brief_path, 'w') as fh:
    json.dump(brief, fh, indent=2, ensure_ascii=False)
    fh.write('\n')
print(json.dumps({'counts': counts, 'not_found': [d['id'] for d in brief['demand'] if d['status'] == 'not-found'],
                  'partial': [d['id'] for d in brief['demand'] if d['status'] == 'partial']}))
