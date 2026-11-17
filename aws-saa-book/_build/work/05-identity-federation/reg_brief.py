"""register-05: update demand statuses and fact ids in brief.v0.json from the miner notes and the canon."""
import json, os, re, sys
from collections import Counter
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
W = os.path.dirname(os.path.abspath(__file__))
facts = {}
for fn in os.listdir(os.path.join(ROOT, 'data', 'facts')):
    if fn.endswith('.jsonl'):
        for line in open(os.path.join(ROOT, 'data', 'facts', fn)):
            if line.strip():
                f = json.loads(line)
                facts[f['id']] = f


def live(i):
    seen = 0
    while i in facts and facts[i]['status'] == 'superseded' and seen < 5:
        i = facts[i].get('superseded_by'); seen += 1
    if i not in facts or facts[i]['status'] == 'rejected':
        return None
    return i


mm = {}
for fn in ('mine-numbers+changes.json', 'mine-behavior+decisions.json'):
    d = json.load(open(os.path.join(W, fn)))
    for k, v in d.items():
        if isinstance(v, dict):
            for dk, dv in v.items():
                if re.match(r'd\d{3}$', dk) and isinstance(dv, dict):
                    mm[dk] = dv
faq = json.load(open(os.path.join(W, 'mine-faq.json')))
for dv in faq['demand']:
    mm[dv['id']] = dv

EXTRA = {
    'd006': (['iam-identity-center-permission-set-session-duration'], 'found',
             'The FAQ sentence (CLI credentials valid for 60 minutes) was rejected as outdated (register-05, as register-03 did for iam-idc-faq-cli-credentials-60-minutes); the guide answer is the permission set session duration, default 1 hour, up to 12 hours. Chapter 03 fact iam-idc-cli-and-console-use-permission-set-duration states that the CLI uses it.'),
    'd063': ([], None, 'iam-identity-center-faq-apps-saml-only rejected (outdated FAQ); use iam-identity-center-saml-and-oauth-customer-apps.'),
    'd094': (['cognito-saml-idp-initiated-app-client-saml-only', 'cognito-saml-sign-requests-encrypt-responses', 'cognito-change-saml-signing-idp-initiated-2024-02'], 'found',
             'register-05 fetched cognito-user-pools-saml-idp-things-to-know and added the IdP-initiated restriction, signing and encryption, and the 2024-02-01 history row.'),
    'd099': (['cognito-change-identity-pool-trust-policy-aud-2025-08'], 'found', 'register-05 added the 2025-08-01 history row as a change fact.'),
    'd100': (['cognito-change-inbound-federation-trigger-2026-01'], 'found', 'register-05 added the 2026-01-28 inbound federation trigger history row.'),
    'd060': (['iam-identity-center-change-multi-region-2026-02'], 'found', 'The multi-Region GA date is iam-identity-center-change-multi-region-2026-02 (2026-02-02, examinable).'),
    'd104': (['cognito-resource-server-custom-scopes', 'cognito-m2m-app-client-needs-client-secret'], 'found',
             'register-05 fetched cognito-user-pools-define-resource-servers and added resource servers, custom scopes and the client secret rule.'),
    'd160': (['cognito-change-sync-closed-to-new-customers-2026-07', 'cognito-change-sync-closure-announced-2026-06'], 'found',
             'Current status of Cognito Sync is in the history rows (no longer open to new customers since 2026-07-31; existing customers continue).'),
}
GAP = {
    'd010': 'Old value (7 days) and date (2023-09-12) only in a What\'s New post refused by robots.txt; IdC document history has no row. Current maximum 90 days is a fact. Re-checked by register-05: no history row; no other saved page states the old value.',
    'd012': 'Launch date (What\'s New 2023-11-17) refused by robots.txt; only the 2023-11-15 boundary is quotable.',
    'd017': 'Current default (MFA on) is a fact; the date of the change (What\'s New 2023-11-16) is refused by robots.txt.',
    'd055': 'The identity source list is bold link lines that M4 cannot quote; covered by the one-source, default-source, Simple AD and AD facts.',
    'd060': None,
    'd075': 'AD Connector and schema extensions: no saved page states it (register-05 searched the Directory Service guide for schema extensions; hits are Managed AD and Simple AD only).',
    'd081': 'Service-to-directory lists are one-word list lines (M4); FSx and RDS rules are quoted; Amazon Quick mapping not quoted.',
    'd083': 'No saved page states when to choose self-managed AD on EC2 over AWS Managed Microsoft AD.',
    'd100': 'Trigger list is a table of link lines; the trigger facts plus the 2026-01-28 history row cover it.',
    'd131': 'Behavox and Sophos case pages redirect to the generic customer stories page. An IAM Identity Center case exists in chapter 03: iam-case-navan-identity-center-provisioning-minutes (verified).',
    'd132': 'Banco Davivienda case page redirects to the generic customer stories page; no newer Directory Service case in the cases index.',
}
STATUS = {'filled': 'found', 'found': 'found', 'covered-earlier': 'found', 'replaced': 'found',
          'partial': 'partial', 'found-partly': 'partial', 'contradicted-or-not-found': 'partial', 'not-found': 'not-found'}

path = os.path.join(W, 'brief.v0.json')
brief = json.load(open(path))
for d in brief['demand']:
    src = mm.get(d['id'], {})
    ids = list(d.get('facts') or []) + list(src.get('facts') or [])
    st = STATUS.get(src.get('status'), None)
    ex = EXTRA.get(d['id'])
    if ex:
        ids += ex[0]
        if ex[1]:
            st = ex[1]
    out = []
    for i in ids:
        j = live(i)
        if j and j not in out:
            out.append(j)
    if st is None:
        st = 'found' if out else 'not-found'
    if not out and st != 'not-found':
        st = 'not-found'
    if d['id'] in GAP and GAP[d['id']] and st == 'found' and d['id'] not in ('d100',):
        pass
    d['facts'] = out
    d['status'] = st
    gap = GAP.get(d['id']) or src.get('not_found')
    if st != 'found' and gap:
        d['gap'] = gap
    elif d['id'] == 'd100' and gap:
        d['gap'] = gap
    if ex and ex[2]:
        d['registrar_note'] = ex[2]
    other = [i for i in out if facts[i]['home_chapter'] != '05']
    if other:
        d['facts_other_chapters'] = other

cnt = Counter(d['status'] for d in brief['demand'])
brief['registrar'] = {
    'by': 'register-05', 'date': '2026-10-12',
    'demand_statuses': dict(cnt),
    'note': "status: 'found' = the named live facts answer the demand question (mech-pass, verification pending); 'partial' = a gap remains (see 'gap'); 'not-found' = nothing quotable (see 'gap'). Superseded ids were replaced by the kept fact; rejected ids were dropped. Details: reg-notes.json."
}
json.dump(brief, open(path, 'w'), indent=1, ensure_ascii=False)
print(json.dumps(dict(cnt)))
for d in brief['demand']:
    if d['status'] != 'found':
        print(d['id'], d['status'], len(d['facts']), (d.get('gap') or '')[:90])
