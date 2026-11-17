"""deep-21 helper: extract fact cards for the facts that 2-deep.md sections name in brief.json."""
import json, re, sys
base = '/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/21-s3/'
brief = json.load(open(base + 'brief.json'))
ids = []
for s in brief['sections']:
    if s['file'] == '2-deep.md':
        ids += s.get('facts', [])
        ids += re.findall(r'\((s3-[a-z0-9-]+)', json.dumps(s.get('plan', '')))
for k in ('numbers', 'decision_record', 'faq', 'realworld'):
    ids += re.findall(r'(s3-[a-z0-9-]+)', json.dumps(brief.get(k)))
for d in brief['diagrams']:
    ids += d.get('facts_for_steps', []) + d.get('facts_for_caption', [])
seen = []
for i in ids:
    if i not in seen and not i.startswith('s3-trap') and not i.startswith('s3-c0') and not i.startswith('s3-t0'):
        seen.append(i)
text = open(base + 'fact-cards.md').read()
cards = {}
cur = None
for line in text.splitlines()[1:]:
    if not line.startswith(' '):
        cur = line.strip(); cards[cur] = [line]
    elif cur:
        cards[cur].append(line)
out = []
missing = []
for i in seen:
    if i in cards:
        out.append('\n'.join(cards[i]))
    else:
        missing.append(i)
open(base + 'deep21-cards.txt', 'w').write('\n'.join(out) + '\nMISSING: ' + ' '.join(missing) + '\n')
print(len(seen), 'ids;', len(missing), 'missing:', missing)
