"""Registrar register-32: writes demand statuses and fact lists into brief.v0.json.
Run: python3 -I aws-saa-book/_build/work/32-step-functions/reg_update_brief.py"""
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


maps, notes, status_in = {}, {}, {}
num = json.load(open(os.path.join(HERE, 'mine-numbers+changes.json')))
for k, d in num['demand'].items():
    maps.setdefault(k, []).extend(d['facts'])
    status_in[k] = d['status']
    for key in ('note', 'not_found'):
        if d.get(key):
            notes.setdefault(k, []).append('numbers+changes: ' + d[key])
beh = json.load(open(os.path.join(HERE, 'mine-behavior+decisions.json')))
for k, d in beh['items'].items():
    maps.setdefault(k, []).extend(d['facts'])
    status_in[k] = d['status']
    if d.get('note'):
        notes.setdefault(k, []).append('behavior+decisions: ' + d['note'])
for x in beh.get('not_found_items', []):
    k = x.split(' ')[0]
    notes.setdefault(k, []).append('behavior+decisions not found: ' + x[len(k):].strip())
faq = json.load(open(os.path.join(HERE, 'mine-faq.json')))
for k, v in faq['demand_map'].items():
    maps.setdefault(k, []).extend(v)
    status_in.setdefault(k, 'filled')
for k, v in faq.get('partial', {}).items():
    status_in[k] = 'partial'
    notes.setdefault(k, []).append('faq: ' + v)

ADD = {
    'd049': ['step-functions-executionthrottled-metric'],
    'd051': ['step-functions-task-credentials-target-role', 'step-functions-change-2022-11-cross-account-access', 'step-functions-task-token-same-account-only'],
    'd094': ['sqs-faq-mq-for-existing-apps', 'sqs-faq-sqs-sns-for-new-apps', 'sns-faq-mq-for-existing-apps-standards-based-brokers', 'sqs-vs-mq-new-apps-vs-broker-migration'],
    'd068': ['sqs-vs-mq-new-apps-vs-broker-migration', 'sqs-faq-mq-for-existing-apps', 'sns-faq-mq-for-existing-apps-standards-based-brokers'],
    'd083': ['step-functions-sdk-integrations-9000-actions', 'step-functions-sdk-integrations-almost-any-api', 'step-functions-http-task-calls-https-apis'],
    'd085': ['step-functions-map-inline-when-to-use', 'step-functions-map-distributed-mode', 'step-functions-quota-map-run-parallel-children'],
    'd091': ['step-functions-console-logging-default-by-type', 'step-functions-express-history-only-cloudwatch-logs'],
    'd101': ['mq-activemq-eos-auto-upgrade-within-45-days', 'mq-change-2024-05-version-support-calendar'],
}
STATUS = {
    'd019': 'partial', 'd032': 'partial', 'd033': 'partial', 'd049': 'partial', 'd065': 'partial', 'd068': 'partial',
    'd051': 'found', 'd094': 'found', 'd083': 'found', 'd085': 'found', 'd091': 'found', 'd101': 'found',
}
REG = {
    'd049': 'register-32: one more targeted search (ExecutionThrottled) found the quotas page sentence; adopted as step-functions-executionthrottled-metric. No saved page sentence names ExecutionsFailed with its meaning; teach only ExecutionThrottled.',
    'd051': 'register-32: one more targeted search (cross-account) found the Task state Credentials field sentence and the document history row of November 18, 2022; adopted as step-functions-task-credentials-target-role and step-functions-change-2022-11-cross-account-access. Task tokens are same-account only (step-functions-task-token-same-account-only).',
    'd065': 'register-32: searched the Amazon MQ guide (snapshots and full guide) for public accessibility and for cannot-be-changed settings: subnets, security groups, storage type and the VPC endpoint IP type are fixed after creation; no sentence says whether public accessibility can change. Do not state it.',
    'd068': 'register-32: chapter 31 facts reused for MQ versus SQS/SNS (existing applications on standard protocols versus new applications). No saved sentence says consumers stay connected to the broker; do not state it.',
    'd094': 'register-32: the Amazon MQ FAQ has no MQ-versus-SQS/SNS answer; reused the chapter 31 facts from the SQS and SNS FAQs.',
    'd019': 'register-32: searched the Step Functions guide (snapshots and full guide) for IPv6: no saved page; the dual-stack item stays a feed row only. No change fact.',
    'd083': 'register-32: the FAQ counts are not stored; the developer guide count (over two hundred services, over nine thousand API actions) is step-functions-sdk-integrations-9000-actions.',
    'd085': 'register-32: Map numbers taken from the developer guide and quotas pages (not the FAQ).',
    'd091': 'register-32: the FAQ default-logging sentence contradicts the guide; the guide fact step-functions-console-logging-default-by-type is current truth.',
    'd101': 'register-32: end-of-support behaviour is stored from the guide and release notes; FAQ default versions are stale and not stored.',
    'd032': 'register-32: unit prices are not in the saved pricing page text; teach the dimensions only.',
    'd033': 'register-32: over 50 connectors stays a feed row only; low exam weight.',
}

path = os.path.join(HERE, 'brief.v0.json')
d = json.load(open(path))
counts = {}
for item in d['demand']:
    i = item['id']
    ids, dropped = [], []
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
        elif src in ('partial', 'partly-filled', 'filled-partly'):
            st = 'partial'
        else:
            st = 'found'
    item['status'] = st
    item['facts'] = ids
    n = ([item['note']] if item.get('note') else []) + notes.get(i, []) + ([REG[i]] if i in REG else [])
    if dropped:
        n.append('register-32: dropped facts that are not live: ' + ', '.join(dropped))
    if n:
        item['note'] = ' | '.join(n)
    item['registered_by'] = 'register-32'
    counts[st] = counts.get(st, 0) + 1
json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(counts)
for item in d['demand']:
    if item['status'] != 'found':
        print(item['id'], item['status'], len(item['facts']))
other = sorted({f for item in d['demand'] for f in item['facts'] if canon[f].get('home_chapter') != '32'})
print('facts of other chapters named:', len(other))
for f in other:
    print(' ', f, canon[f]['status'], canon[f].get('home_chapter'))
named = {f for item in d['demand'] for f in item['facts']}
live32 = [f for f, x in canon.items() if x.get('home_chapter') == '32' and x['status'] not in ('rejected', 'superseded')]
print('live chapter facts not named by any demand item:', len([f for f in live32 if f not in named]))
