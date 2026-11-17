"""Reorder options in qw1-questions.json: qw1-reorder.py QID=old,old,old,old [...]; ids are reassigned a, b, c ..."""
import json
import sys

src = 'aws-saa-book/_build/work/31-messaging/qw1-questions.json'
qs = json.load(open(src))
by = {q['id']: q for q in qs}
for arg in sys.argv[1:]:
    qid, order = arg.split('=')
    q = by[qid]
    opts = {o['id']: o for o in q['options']}
    new = []
    for n, old in enumerate(order.split(',')):
        o = dict(opts[old])
        o['id'] = 'abcdef'[n]
        new.append(o)
    assert len(new) == len(q['options'])
    q['options'] = new
    print(qid, [o['id'] for o in new if o['correct']])
with open(src, 'w') as f:
    json.dump(qs, f, indent=1, ensure_ascii=False)
