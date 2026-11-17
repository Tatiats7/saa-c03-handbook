# adjudicate-23: refresh demand fact lists in brief.v0.json after adjudication.
import json
P = 'aws-saa-book/_build/work/23-efs-fsx/brief.v0.json'
MAP = {
 "efs-change-access-points-1000-per-file-system-2023-01": "efs-change-access-points-10000-per-file-system-2025-02",
 "efs-change-elastic-read-throughput-60-gibps-2024-10": "efs-change-elastic-read-throughput-20-gibps-other-regions-2025-04",
 "efs-change-elastic-read-iops-90000-infrequent-2024-01": "efs-quota-elastic-iops-increase-factor",
 "efs-free-tier-5gb-12-months": "efs-faq-free-tier-5-gb-standard",
}
st = {}
for svc in ('efs', 'fsx'):
    for line in open(f'aws-saa-book/data/facts/{svc}.jsonl'):
        if line.strip():
            f = json.loads(line); st[f['id']] = (f['status'], f.get('superseded_by'))
b = json.load(open(P))
changed = 0
dead_other = []
for d in b['demand']:
    old = list(d.get('facts') or [])
    new = []
    for fid in old:
        fid2 = MAP.get(fid, fid)
        s = st.get(fid2, (None, None))
        if s[0] == 'superseded' and s[1]:
            fid2 = s[1]; s = st.get(fid2, (None, None))
        if s[0] in ('rejected', 'superseded', None):
            dead_other.append((d['id'], fid2, s[0])); continue
        if fid2 not in new:
            new.append(fid2)
    if new != old:
        d['facts'] = new; changed += 1
        d['adjudicated_by'] = 'adjudicate-23'
    if not new and d.get('status') != 'not-found':
        d['status'] = 'not-found'; changed += 1
    pend = [f for f in new if st[f][0] != 'verified']
    if pend:
        d['awaiting_revote'] = pend
    else:
        d.pop('awaiting_revote', None)
json.dump(b, open(P, 'w'), indent=1, ensure_ascii=False)
import collections
print('changed', changed, 'dead', dead_other)
print(collections.Counter(d['status'] for d in b['demand']), sum(1 for d in b['demand'] if d.get('awaiting_revote')))
