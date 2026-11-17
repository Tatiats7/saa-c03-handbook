"""Registrar register-31: writes demand statuses and fact lists into brief.v0.json.
Run: python3 -I aws-saa-book/_build/work/31-messaging/reg-update-brief.py"""
import json, os, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..', '..', '..')
canon = {}
for p in glob.glob(os.path.join(ROOT, 'data', 'facts', '*.jsonl')):
    for line in open(p, encoding='utf-8'):
        if line.strip():
            f = json.loads(line)
            canon[f['id']] = f


def resolve(fid):
    seen = set()
    while fid in canon and canon[fid]['status'] == 'superseded' and fid not in seen:
        seen.add(fid)
        fid = canon[fid].get('superseded_by') or fid
    f = canon.get(fid)
    if not f or f['status'] in ('rejected', 'superseded'):
        return None
    return fid


maps = {}
notes = {}
status_in = {}
beh = json.load(open(os.path.join(HERE, 'mine-behavior.json')))
for d in beh['demand']:
    maps.setdefault(d['id'], []).extend(d['facts'])
    status_in[d['id']] = d['status']
    if d.get('note'):
        notes.setdefault(d['id'], []).append('behavior: ' + d['note'])
dc = json.load(open(os.path.join(HERE, 'mine-decisions+changes.json')))
for k, d in dc['demand'].items():
    maps.setdefault(k, []).extend(x.split(' ')[0] for x in d['facts'])
    status_in[k] = d['status']
    if d.get('note'):
        notes.setdefault(k, []).append('decisions+changes: ' + d['note'])
faq = json.load(open(os.path.join(HERE, 'mine-faq.json')))
for k, v in faq['demand_map'].items():
    maps.setdefault(k, []).extend(v)
    status_in.setdefault(k, 'filled')
for k, v in faq.get('partial', {}).items():
    status_in[k] = 'partial'
    notes.setdefault(k, []).append('faq: ' + v)
num = json.load(open(os.path.join(HERE, 'mine-numbers.json')))
for k, d in num['demand'].items():
    maps.setdefault(k, []).extend(d['facts'])
    status_in[k] = d['status']
    for key in ('note', 'not_found'):
        if d.get(key):
            notes.setdefault(k, []).append('numbers: ' + d[key])

# registrar additions and decisions
ADD = {
    'd093': ['eventbridge-wa-deployed-multi-az-by-aws'],
    'd058': ['sns-change-fifo-archiving-replay-2023'],
    'd112': ['sqs-in-flight-fifo-limit'],
    'd114': ['sqs-faq-sse-producer-needs-generatedatakey-and-decrypt'],
    'd029': ['sqs-faq-sse-producer-needs-generatedatakey-and-decrypt', 'sqs-change-sendmessage-needs-only-generatedatakey-2024'],
    'd069': ['eventbridge-putevents-up-to-10-entries'],
}
STATUS = {
    'd015': 'partial', 'd049': 'partial', 'd069': 'partial', 'd143': 'partial',
    'd066': 'partial', 'd084': 'partial', 'd112': 'found',
}
REG_NOTES = {
    'd093': 'register-31: one more targeted search found the Well-Architected REL10-BP02 sentence that names EventBridge, SQS and SNS as automatically deployed to multiple Availability Zones by AWS; adopted as eventbridge-wa-deployed-multi-az-by-aws.',
    'd015': 'register-31: searched again (64 KB chunk, metering): the SQS pricing metering rows have no header row (saa.py tables finds no table), so the 64 KB rule, FIFO rates and data transfer rows cannot be quoted. Teach only the free tier and no-minimum-fee facts.',
    'd049': 'register-31: the 64 KB publish and delivery rules are quoted; per-request and per-delivery prices are script-rendered and not in the snapshot.',
    'd069': 'register-31: PutEvents TPS per Region stays unquotable (row over 80 words); entries per request is eventbridge-putevents-up-to-10-entries.',
    'd112': 'register-31: change item whats-new-v2#p170969243 (20K to 120K, 2024-11-21) attached to sqs-in-flight-fifo-limit; it needs a currency vote.',
    'd114': 'register-31: conflict kept open on purpose with both facts: sqs-faq-sse-producer-needs-generatedatakey-and-decrypt (FAQ plus the current key-management page: producer needs kms:GenerateDataKey and kms:Decrypt) and sqs-change-sendmessage-needs-only-generatedatakey-2024 (history row of July 24, 2024). Teach: grant a producer both permissions; add a Changed recently note on the 2024 row.',
    'd054': 'register-31: the FAQ fact that listed only SQS and HTTP(S) for raw delivery was rejected (the guide also lists Firehose).',
    'd043': 'register-31: the FAQ quota facts (10 million subscriptions, 100,000 topics) were rejected or superseded; the General Reference row (12,500,000 per standard topic, 100 per FIFO topic) is current.',
    'd044': 'register-31: the FAQ fact of 200 filter policies per account per Region was rejected; the guide says 200 per topic and 10,000 per account.',
    'd066': 'register-31: no saved page says that email and HTTP/S endpoints must confirm; only the 2-day token and the cross-account SQS confirmation rules are facts.',
    'd084': 'register-31: the read-only management events option is not a fact; the default-bus-only and trail-logging facts answer the main question.',
    'd143': 'register-31: no default throughput number is quotable from the FAQ; latency about half a second is the fact.',
}

d = json.load(open(os.path.join(HERE, 'brief.v0.json')))
counts = {}
for item in d['demand']:
    i = item['id']
    ids = []
    dropped = []
    for fid in maps.get(i, []) + ADD.get(i, []):
        r = resolve(fid)
        if r is None:
            dropped.append(fid)
        elif r not in ids:
            ids.append(r)
    st = STATUS.get(i)
    if not st:
        src = status_in.get(i, '')
        if not ids:
            st = 'not-found'
        elif src in ('partial', 'partly-filled'):
            st = 'partial'
        else:
            st = 'found'
    item['status'] = st
    item['facts'] = ids
    n = notes.get(i, []) + ([REG_NOTES[i]] if i in REG_NOTES else [])
    if dropped:
        n.append('register-31: dropped rejected facts ' + ', '.join(dropped))
    if n:
        item['note'] = ' | '.join(n)
    item['registered_by'] = 'register-31'
    counts[st] = counts.get(st, 0) + 1
json.dump(d, open(os.path.join(HERE, 'brief.v0.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(counts)
for item in d['demand']:
    if item['status'] != 'found':
        print(item['id'], item['status'], item['facts'][:4])
other = sorted({f for item in d['demand'] for f in item['facts'] if canon[f]['home_chapter'] != '31'})
print('facts of other chapters named:', len(other))
for f in other:
    print(' ', f, canon[f]['status'], canon[f]['home_chapter'])
