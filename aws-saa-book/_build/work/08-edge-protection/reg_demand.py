"""register-08: update the demand statuses and fact lists in brief.v0.json from the miners' notes and the canon.

Usage: python3 aws-saa-book/_build/work/08-edge-protection/reg_demand.py [--write]
Without --write it prints the proposed table only.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.abspath(os.path.join(HERE, '..', '..', '..'))

canon = {}
for fn in os.listdir(os.path.join(BOOK, 'data', 'facts')):
    if fn.endswith('.jsonl'):
        for line in open(os.path.join(BOOK, 'data', 'facts', fn)):
            if line.strip():
                f = json.loads(line)
                canon[f['id']] = f


def live_id(i, depth=0):
    f = canon.get(i)
    if f is None:
        return None
    if f['status'] == 'superseded' and f.get('superseded_by') and depth < 5:
        return live_id(f['superseded_by'], depth + 1)
    if f['status'] in ('rejected', 'superseded'):
        return None
    return i


miner = {}  # d -> list of (status, facts, note)


def walk(node, key=None):
    if isinstance(node, dict):
        did = key if key and re.fullmatch(r'd\d{3}', key) else node.get('id') if isinstance(node.get('id'), str) and re.fullmatch(r'd\d{3}', node.get('id')) else None
        if did:
            facts = [x for x in (node.get('facts') or []) if isinstance(x, str)]
            note = node.get('note') or node.get('not_found') or node.get('reason') or ''
            miner.setdefault(did, []).append((str(node.get('status') or ''), facts, note if isinstance(note, str) else json.dumps(note)))
        for k, v in node.items():
            walk(v, k)
    elif isinstance(node, list):
        for v in node:
            walk(v)


for fn in sorted(os.listdir(HERE)):
    if fn.startswith('mine-') and fn.endswith('.json') and fn != 'mine-plan.json':
        walk(json.load(open(os.path.join(HERE, fn))))

tagged = {}
for f in canon.values():
    if f.get('home_chapter') != '08':
        continue
    for m in re.findall(r'\bd\d{3}\b', str(f.get('note') or '')):
        tagged.setdefault(m, []).append(f['id'])

# registrar decisions (register-08): items that stay partial or not-found after the extra search
OVERRIDE = {
    'd002': ('filled', 'register-08 added waf-protected-resource-types from the web-acl page sentence (the what-is list cannot be quoted line by line).'),
    'd003': ('partial', 'No saved page has a cannot-sentence for NLB, EC2, API Gateway HTTP API or Global Accelerator (searched what-is-aws-waf, how-aws-waf-works-resources, web-acl, web-acl-associating-aws-resource, WAF FAQ). Teach these as not in the supported list (waf-protected-resource-types); only ALB on Outposts has a quoted cannot.'),
    'd007': ('partial', 'Cookie forwarding for the token is grounded; how to stop clients bypassing CloudFront to reach the ALB is a CloudFront topic (custom origin header or managed prefix list): no saved WAF page; search for bypass found nothing in WAF pages. Leave to the CloudFront chapter.'),
    'd012': ('partial', 'Geo match behaviour grounded; the comparison with CloudFront geographic restrictions belongs to the CloudFront chapter.'),
    'd035': ('partial', 'Destinations grounded; no saved page states how many destinations one web ACL can have (searched logging, logging-destinations, logging-management-configure for destination per / one logging destination).'),
    'd036': ('partial', None),
    'd043': ('partial', 'waf-faq-inspects-http-and-https says AWS WAF inspects HTTP and HTTPS requests; no saved WAF page states where TLS is terminated, so do not claim it.'),
    'd057': ('partial', 'CloudFront with a custom origin is grounded (shield-protect-sites-outside-aws-via-cloudfront, shield-faq-protect-outside-lock-down-backend names CloudFront or Route 53); no Shield page names Global Accelerator for this case.'),
    'd058': ('partial', None),
    'd060': ('partial', None),
    'd081': ('not-found', 'arch-igw-ngw shows the NAT gateway pattern only as a diagram; the asymmetric-routing sentence about the NAT gateway subnet sits after a bold label and fails M4. Use network-firewall-route-igw-both-directions and network-firewall-no-asymmetric-routing.'),
    'd090': ('partial', None),
    'd112': ('not-found', 'ENGIE snapshot is the generic case-study index (redirect); no quote. d113 and d114 give the real examples.'),
}

brief_path = os.path.join(HERE, 'brief.v0.json')
brief = json.load(open(brief_path))
rows = []
from collections import Counter
cnt = Counter()
for d in brief['demand']:
    ids = []
    for st, fs, note in miner.get(d['id'], []):
        ids += fs
    ids += tagged.get(d['id'], [])
    ids += d.get('facts') or []
    out = []
    for i in ids:
        j = live_id(i)
        if j and j not in out and canon[j].get('home_chapter') == '08':
            out.append(j)
    other = [i for i in ids if live_id(i) and canon[live_id(i)].get('home_chapter') != '08']
    mst = [st for st, _, _ in miner.get(d['id'], [])]
    notes = [n for _, _, n in miner.get(d['id'], []) if n]
    if d['id'] in OVERRIDE:
        status, onote = OVERRIDE[d['id']]
        note = onote or (notes[0] if notes else '')
    elif not out and not other:
        status, note = 'not-found', (notes[0] if notes else 'no live fact')
    elif any(s == 'partial' for s in mst):
        status, note = 'partial', (notes[0] if notes else '')
    else:
        status, note = 'filled', ''
    d['status'] = status
    d['facts'] = out + [o for o in other if o not in out]
    if note:
        d['note'] = note
    elif 'note' in d:
        del d['note']
    cnt[status] += 1
    rows.append(f"{d['id']} {status} n={len(d['facts'])} {note[:100]}")

print('STATUS', dict(cnt))
print('\n'.join(r for r in rows if not r.split()[1] == 'filled'))
if '--write' in sys.argv:
    with open(brief_path, 'w') as fh:
        json.dump(brief, fh, indent=1, ensure_ascii=False)
        fh.write('\n')
    print('wrote', os.path.relpath(brief_path, os.getcwd()))
