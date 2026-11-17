"""Registrar register-31: builds the amend patches for chapter 31 (one JSON file per fact).
Run: python3 -I aws-saa-book/_build/work/31-messaging/reg-gen-patches.py
Checks every new number-free display against the quotes before writing."""
import json, os, re, copy

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
BASE = os.path.join(ROOT, 'data', 'facts')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reg-patches')
os.makedirs(OUT, exist_ok=True)

facts = {}
for s in ['sqs', 'sns', 'eventbridge']:
    for line in open(os.path.join(BASE, s + '.jsonl'), encoding='utf-8'):
        if line.strip():
            f = json.loads(line)
            facts[f['id']] = f

MAP = str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"', '—': '-', '–': '-'})


def norm(s):
    return re.sub(r'\s+', ' ', (s or '').translate(MAP).replace('`', '').replace('*', '')).strip().lower()


# id -> {old display: new display}  (None removes the value)
DISPLAYS = {
    'sqs-dlq-denyall-blocks-use-as-dlq': {'the queue cannot be used as a dead-letter queue': 'cannot be used as a dead-letter queue'},
    'sqs-dlq-max-receive-count-meaning': {'number of times a consumer can receive a message': 'number of times a consumer can receive'},
    'sqs-dlq-same-account-and-region': {'same AWS account and Region as the source queue': 'same AWS account and Region',
                                        'must be in the same AWS account and Region': 'must be in the same AWS account'},
    'sqs-faq-dlq-fifo-needs-fifo-standard-needs-standard': {'must use a FIFO dead letter queue with a FIFO queue': 'must use a FIFO dead letter queue',
                                                            'only a standard dead letter queue with a standard queue': 'only a standard dead letter queue'},
    'sqs-faq-dlq-redrive-velocity-selectable': {'rate at which Amazon SQS will move the messages': 'select the redrive velocity'},
    'sqs-faq-fair-queues-versus-fifo-noisy-neighbor': {'limiting the number of in-flight messages from each tenant': 'in-flight messages from each tenant'},
    'sqs-faq-sse-no-extra-sqs-charge-kms-calls-charged': {'charges for calls from Amazon SQS to AWS KMS': 'calls from Amazon SQS to AWS KMS'},
    'sqs-faq-sse-uses-kms-keys': {'decrypts messages only when they are sent to an authorized consumer': 'sent to an authorized consumer'},
    'sqs-fifo-generated-dedup-id-from-body-hash': {'generates a deduplication ID by hashing the message body': 'by hashing the message body'},
    'sqs-kms-service-senders-need-customer-managed-key': {'add permissions in the key policy for the service': 'permissions in the key policy'},
    'sqs-sse-backlogged-messages-not-encrypted': {'encrypted only if it is sent after the encryption': 'encrypted only if it is sent after'},
    'sqs-sse-encrypts-message-body': {'body of a message in an Amazon SQS queue': None},
    'sqs-temporary-queues-map-onto-one-queue': {'make fewer API calls and have a higher throughput': 'fewer API calls and have a higher throughput'},
    'sns-faq-fanout-identical-messages-to-multiple-sqs-queues': {'subscribe multiple SQS standard queues to the SNS topic': 'multiple SQS standard queues to the SNS topic'},
    'sns-faq-message-filtering-subscribers-receive-subset': {'as opposed to receiving all messages published to a topic': 'receiving all messages published to a topic'},
    'sns-faq-order-attempted-but-network-issues-can-reorder': {'attempt to deliver messages from the publisher in the order': 'attempt to deliver messages from the publisher'},
    'sns-fifo-messagegroup-scope-not-reversible': {'it cannot be reverted back to the Topic throughput': 'cannot be reverted back to the Topic throughput'},
    'sns-filter-nonmatching-message-not-sent': {"Amazon SNS doesn't send the message to that subscriber": "doesn't send the message to that subscriber"},
    'sns-filter-scope-attributes-default-or-body': {'Applies the filter policy to message attributes (default setting)': 'message attributes (default setting)'},
    'sns-pricing-attribute-filtering-free': {'payload-based message filtering is based on the total amount of outbound payload data scanned': 'total amount of outbound payload data scanned'},
    'sns-pricing-fifo-subscription-messages': {'multiplying the number of published messages and the number of subscriptions': 'multiplying the number of published messages'},
    'sns-publish-size-counts-body-and-attributes': {'combined size of the message body and message attributes': 'message body and message attributes'},
    'sns-push-mechanism-no-polling': {'removes the need to check or “poll” for updates': 'removes the need to check or “poll”'},
    'sns-retry-exhausted-discards-unless-dlq': {'unless a dead-letter queue is attached to the subscription': 'a dead-letter queue is attached to the subscription'},
    'sns-sse-backlogged-messages-not-encrypted': {'encrypted only if it is sent after the encryption': 'encrypted only if it is sent after'},
    'eventbridge-api-destination-https-endpoint-target': {'HTTPS endpoints that you can invoke as the target': 'HTTPS endpoints that you can invoke'},
    'eventbridge-aws-service-events-go-to-default-bus': {'on a durable or best-effort basis': 'AWS services send events to EventBridge'},
    'eventbridge-faq-cross-account-target-default-or-other-event-bus': {'default event bus or any other event bus in another account': 'default event bus or any other event bus'},
    'eventbridge-faq-rule-can-customize-event-before-target': {'customize an event before it is sent to the target': 'customize an event before it is sent'},
    'eventbridge-pipe-to-bus-fans-out-to-many-targets': {'a pipe with an event bus as its target': 'a pipe with an event bus'},
    'eventbridge-pricing-aws-management-events-free': {'AWS management events are ingested by the event bus for free': 'ingested by the event bus for free'},
    'eventbridge-retry-exhausted-event-dropped': {'configure a dead-letter queue (DLQ) to receive all failed events': 'configure a dead-letter queue (DLQ)'},
    'eventbridge-sqs-fair-fifo-target-needs-sqsparameters': {'specify the message group to use as the target': 'the message group to use as the target'},
    'eventbridge-cloudtrail-events-need-trail-logging': {'AWS API Call via CloudTrail': 'a request to a public AWS service API'},
}

CLAIMS = {
    'sns-raw-delivery-firehose-body-only': 'With raw message delivery enabled for Firehose endpoints, the message body is delivered; message attributes are not sent.',
    'eventbridge-cloudtrail-events-need-trail-logging': 'To record events with one of the CloudTrail detail-type values, you must enable a CloudTrail trail with logging. These events represent requests to a public AWS service API.',
}

EXTRA = {
    'sqs-sse-encrypts-message-body': {'tier0': True},
    'sqs-in-flight-fifo-limit': {'change_items': ['whats-new-v2#p170969243'],
                                 'note': 'd006, d112. Raised from 20K to 120K in-flight messages for FIFO queues on 2024-11-21 (What\'s New, change item whats-new-v2#p170969243); older questions may assume 20,000. The quotas page is current truth.'},
    'sqs-faq-sse-producer-needs-generatedatakey-and-decrypt': {
        'evidence_add': {'url': 'https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-key-management.html',
                         'source_id': 'docs/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-key-management',
                         'quote': 'Therefore, the producer must have the `kms:Decrypt` and `kms:GenerateDataKey` permissions for the KMS key.'},
        'qualifiers': {'scope': 'producer of an SSE-KMS queue, per KMS key', 'default_or_max': '', 'adjustable': False,
                       'condition': 'CONFLICT kept open on purpose: the SQS documentation history row of July 24, 2024 (sqs-change-sendmessage-needs-only-generatedatakey-2024) says SendMessage no longer requires kms:Decrypt; the FAQ and the current key-management page still say a producer needs both. Granting both permissions to a producer is the design that works under either reading.'},
        'note': 'd029, d114. Registrar register-31 kept this fact and added the key-management page as a second source; the book should teach: grant a producer kms:GenerateDataKey and kms:Decrypt, and mention the 2024 history row as a Changed recently note.'},
}

LIGHT = {
    'sns-change-max-message-size-1mib-opt-in-2026': {'exam_relevance': 'reference'},
    'eventbridge-change-custom-event-bus-classic-rename-2026': {'exam_relevance': 'reference'},
    'sqs-fifo-queue-name-suffix': {'exam_relevance': 'core'},
    'sqs-fifo-partition-throughput-3000-batched-300-single': {'exam_relevance': 'core', 'tier0': True},
    'sqs-fifo-no-per-message-timers': {'exam_relevance': 'core'},
    'sqs-pricing-no-minimum-fee': {'exam_relevance': 'extended'},
}

SCOPE_BY_SOURCE = {
    'sns-or-sqs-or-eventbridge': {'sqs': 'Amazon SQS, in the SNS, SQS or EventBridge decision guide',
                                  'sns': 'Amazon SNS, in the SNS, SQS or EventBridge decision guide',
                                  'eventbridge': 'Amazon EventBridge, in the SNS, SQS or EventBridge decision guide'},
    'application-integration-on-aws-how-to-choose': 'application integration decision guide',
    'event-driven-architectures': 'Serverless Applications Lens, event-driven architectures',
    'welcome': 'SQS developer guide overview (SQS, SNS and Amazon MQ)',
    'rel_prevent_interaction_failure_loosely_coupled_system': 'Well-Architected reliability pillar, REL04-BP02 loosely coupled dependencies',
    'rel_mitigate_interaction_failure_throttle_requests': 'Well-Architected reliability pillar, REL05-BP02 throttle requests',
    'rel_prevent_interaction_failure_idempotent': 'Well-Architected reliability pillar, REL04-BP04 idempotent operations',
    'doc-history': 'EventBridge Scheduler and Pipes documentation history',
    'sns-sqs-as-subscriber': 'SNS topic with SQS queue subscribers',
    'faqs': {'sqs': 'Amazon SQS FAQ comparison', 'sns': 'Amazon SNS FAQ comparison', 'eventbridge': 'EventBridge FAQ comparison'},
}

problems = []
written = []


def check_display(fid, f, disp, quotes):
    if re.search(r'\d', disp):
        return
    if len(disp.split()) > 8:
        problems.append('%s: display over 8 words: %s' % (fid, disp))
    if not any(norm(disp) in q for q in quotes):
        problems.append('%s: display not in a quote: %s' % (fid, disp))


ids = set(DISPLAYS) | set(CLAIMS) | set(EXTRA) | set(LIGHT)
for fid, f in facts.items():
    if f['status'] in ('rejected', 'superseded'):
        continue
    if not f['qualifiers'].get('scope'):
        ids.add(fid)

for fid in sorted(ids):
    f = facts.get(fid)
    if f is None or f['status'] in ('rejected', 'superseded'):
        problems.append('%s: missing or not live' % fid)
        continue
    patch = {}
    quotes = [norm(e['quote']) for e in f['evidence']]
    if fid in DISPLAYS:
        vals = []
        seen = set()
        for v in f['values']:
            old = v['display']
            if old in DISPLAYS[fid]:
                new = DISPLAYS[fid][old]
                if new is None:
                    continue
                v = dict(v, display=new)
            vals.append(v)
        olds = {v['display'] for v in f['values']}
        for o in DISPLAYS[fid]:
            if o not in olds:
                problems.append('%s: old display not found: %s' % (fid, o))
        patch['values'] = vals
    if fid in CLAIMS:
        patch['claim'] = CLAIMS[fid]
    if fid in EXTRA:
        ex = copy.deepcopy(EXTRA[fid])
        if 'evidence_add' in ex:
            ev = copy.deepcopy(f['evidence'])
            ea = ex.pop('evidence_add')
            ev.append({'source_id': ea['source_id'], 'url': ea['url'], 'quote': ea['quote'], 'table_header': None})
            patch['evidence'] = ev
            quotes.append(norm(ea['quote']))
        patch.update(ex)
    if fid in LIGHT:
        patch.update(LIGHT[fid])
    if not f['qualifiers'].get('scope') and 'qualifiers' not in patch:
        src = f['evidence'][0]['source_id'].split('/')[-1]
        sc = SCOPE_BY_SOURCE.get(src)
        if isinstance(sc, dict):
            sc = sc[f['service']]
        if not sc:
            problems.append('%s: no scope rule for %s' % (fid, src))
        else:
            q = dict(f['qualifiers'])
            q['scope'] = sc
            patch['qualifiers'] = q
    for v in patch.get('values', f['values']):
        check_display(fid, f, v['display'], quotes)
    with open(os.path.join(OUT, fid + '.json'), 'w', encoding='utf-8') as o:
        json.dump(patch, o, ensure_ascii=False, indent=1)
    light = all(k in ('exam_relevance', 'tier0', 'question', 'note') for k in patch)
    written.append((fid, 'light' if light else 'rev'))

for p in problems:
    print('PROBLEM', p)
for fid, kind in written:
    print(kind, fid)
print('written', len(written))
