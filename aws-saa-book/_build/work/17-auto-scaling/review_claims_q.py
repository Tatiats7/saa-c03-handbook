import json, re
d = json.load(open('aws-saa-book/data/17-auto-scaling/questions.json'))
strip = lambda s: re.sub(r'\]\(\.\./facts/[^)]*#([^)]*)\)', r']{\1}', s or '')
from collections import Counter
print(Counter(q.get('status') for q in d['items']))
for q in d['items']:
    if q.get('status') == 'rejected':
        continue
    print('###', q['id'], q.get('status'), q.get('type'), q.get('qualifier'))
    print('S:', q['stem'])
    for o in q['options']:
        print(' %s%s %s' % (o['id'], '*' if o['correct'] else ' ', o['text']))
        print('    why:', strip(o.get('why')))
    for k in ('explanation', 'explain', 'teach'):
        if q.get(k):
            print(' EXPL:', strip(q[k] if isinstance(q[k], str) else json.dumps(q[k])))
