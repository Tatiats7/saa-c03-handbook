import json, re, glob, sys
root = 'aws-saa-book/'
b = json.load(open(root + '_build/work/24-backup/brief.json'))
txt = json.dumps([s for s in b['sections'] if s.get('file') == '2-deep.md']) + json.dumps(b['faq']) + json.dumps(b['realworld']) + json.dumps(b['diagrams']) + json.dumps(b['traps'])
ids = set(re.findall(r'\b((?:backup|well-architected|organizations|ebs|dynamodb|aurora|s3|rds)-[a-z0-9-]+)\b', txt))
facts = {}
for f in glob.glob(root + 'data/facts/*.jsonl'):
    for line in open(f):
        line = line.strip()
        if not line:
            continue
        d = json.loads(line)
        facts[d['id']] = d
out = []
for i in sorted(ids):
    d = facts.get(i)
    if not d:
        out.append('MISSING ' + i)
        continue
    out.append('== %s [%s] svc=%s changed=%s' % (i, d.get('status'), d.get('service'), json.dumps(d.get('changed'))))
    out.append('  displays: ' + ' | '.join(v['display'] for v in d.get('values', [])))
    for e in d.get('evidence', []):
        out.append('  url: ' + e['url'])
        out.append('  quote: ' + e['quote'][:700])
open(root + '_build/work/24-backup/deep24-facts.txt', 'w').write('\n'.join(out))
print(len(ids), 'ids')
