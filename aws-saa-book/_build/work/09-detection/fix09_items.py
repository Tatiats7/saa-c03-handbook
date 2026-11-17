import json
base = 'aws-saa-book/data/09-detection/'
out = 'aws-saa-book/_build/work/09-detection/'

# task t02: technical-07 (verify can pass while a detector exists) and technical-10 (optional plans)
d = json.load(open(base + 'tasks.json'))
t02 = [x for x in d['items'] if x['id'] == 'detection-t02'][0]
step5 = t02['steps'][4]
assert step5['command'].startswith('aws guardduty get-detector')
step5['expect'] = ('Pairs of a feature name and a status. FLOW_LOGS, CLOUD_TRAIL and DNS_LOGS show ENABLED. '
                   'Some optional protection plans can also show ENABLED, because GuardDuty turns some of them on automatically.')
t02['verify']['expect'] = ('An empty list. Then run aws guardduty list-detectors as well: DetectorIds shows an empty list. '
                           'If it shows an ID, run the cleanup again.')
t02['still_costs'][0] = ('Nothing after the cleanup. A detector that stays on costs $0 a day during the free trial. After the trial, '
                         'it adds charges by the volume of logs and events analyzed, also for the protection plans that are on.')
if 'guardduty-first-enable-all-plans-except-runtime' not in t02['facts']:
    t02['facts'].append('guardduty-first-enable-all-plans-except-runtime')
json.dump([t02], open(out + 'fix-t02.json', 'w'), indent=1, ensure_ascii=False)

# speak s01 kp5 (reader-27 idiom) and s02 continuous recording (technical-11)
d = json.load(open(base + 'speak.json'))
s01 = [x for x in d['items'] if x['id'] == 'detection-s01'][0]
kp5 = [k for k in s01['key_points'] if k['id'] == 'kp5'][0]
kp5['point'] = 'Security Hub CSPM receives findings from GuardDuty, Inspector and Macie in one place.'
s02 = [x for x in d['items'] if x['id'] == 'detection-s02'][0]
i = s02['sixty_second'].index('Config records a configuration item each time the security group changes.')
s02['sixty_second'][i] = 'With continuous recording, Config records a configuration item each time the group changes.'
if 'config-guide-continuous-or-daily-recording' not in s02['facts']:
    s02['facts'].append('config-guide-continuous-or-daily-recording')
json.dump([s01, s02], open(out + 'fix-speak.json', 'w'), indent=1, ensure_ascii=False)

# card c007 (claims-05: the back said every rule evaluates after the change)
d = json.load(open(base + 'cards.json'))
c007 = [x for x in d['items'] if x['id'] == 'detection-c007'][0]
c007['back'] = 'No. A rule reports noncompliance but does not block the change.'
json.dump([c007], open(out + 'fix-c007.json', 'w'), indent=1, ensure_ascii=False)
print('ok')
