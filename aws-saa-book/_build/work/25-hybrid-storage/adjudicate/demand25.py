"""adjudicate-25: update demand statuses in brief.v0.json after adjudication."""
import json

BOOK = '/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/'
BRIEF = BOOK + '_build/work/25-hybrid-storage/brief.v0.json'
REPL = {
    'datasync-faq-agent-types-follow-task-mode': ['datasync-agent-two-types-basic-and-enhanced', 'datasync-change-enhanced-mode-hdfs-azure-object-hyper-v-2026-07'],
    'datasync-faq-enhanced-mode-locations-as-of-faq': ['datasync-faq-vs-guide-enhanced-mode-locations-in-guide'],
    'datasync-faq-nfs-smb-access-needs-agent': ['datasync-agent-needed-when-storage-managed-by-you-or-other-cloud'],
    'snow-family-no-snow-device-for-new-customers-existing-unaffected': ['snow-family-change-closed-to-new-customers-2025-11', 'snow-family-change-end-of-support-2026-12-31'],
    'storage-gateway-faq-fips-endpoints-gateway-types': ['storage-gateway-change-fips-privatelink-s3-file-2026-09', 'storage-gateway-change-fips-privatelink-tape-volume-2026-08'],
    'storage-gateway-faq-s3-file-max-file-size-5-tb': ['storage-gateway-s3-file-quota-max-file-size'],
    'transfer-family-faq-sftp-ssh-keys-per-user-10': ['transfer-family-quota-ssh-keys-per-service-managed-user', 'transfer-family-ssh-key-types-rsa-ecdsa-ed25519'],
}

status = {}
for svc in ['datasync', 'snow-family', 'storage-gateway', 'transfer-family', 's3', 'efs', 'fsx', 'backup', 'direct-connect', 'well-architected']:
    try:
        for line in open(BOOK + 'data/facts/%s.jsonl' % svc):
            if line.strip():
                f = json.loads(line)
                status[f['id']] = f['status']
    except FileNotFoundError:
        pass

b = json.load(open(BRIEF))
changed = 0
counts = {}
for d in b['demand']:
    facts = list(d.get('facts') or [])
    new = []
    swapped = []
    for fid in facts:
        if fid in REPL:
            swapped.append(fid)
            for r in REPL[fid]:
                if r not in new and r not in facts:
                    new.append(r)
        elif fid not in new:
            new.append(fid)
    live = [f for f in new if status.get(f) not in ('rejected', 'superseded', None) or f not in status]
    live = [f for f in live if status.get(f) != 'rejected']
    pend = [f for f in live if status.get(f) in ('mech-pass', 'candidate', 'disputed')]
    old = d.get('status')
    if not live:
        st = 'not-found'
    else:
        st = old if old in ('found', 'partial') else 'found'
    if swapped or st != old or live != facts:
        d['facts'] = live
        d['status'] = st
        note = 'adjudicate-25 (2026-10-14):'
        if swapped:
            note += ' rejected %s, pointed to verified replacements.' % ', '.join(swapped)
        d['adjudicated'] = note
        changed += 1
    if pend:
        d['pending_revote'] = pend
    elif 'pending_revote' in d:
        del d['pending_revote']
    counts[d['status']] = counts.get(d['status'], 0) + 1
json.dump(b, open(BRIEF, 'w'), indent=1, ensure_ascii=False)
open(BRIEF, 'a').write('\n')
print('changed', changed, counts, 'with pending', sum(1 for d in b['demand'] if d.get('pending_revote')))
