"""Write a subset of qw1-questions.json: qw1-subset.py OUT ID [ID ...] (ids in the given order)."""
import json
import sys

src = 'aws-saa-book/_build/work/31-messaging/qw1-questions.json'
items = {q['id']: q for q in json.load(open(src))}
out, ids = sys.argv[1], sys.argv[2:]
with open(out, 'w') as f:
    json.dump([items[i] for i in ids], f, indent=1)
print(out, len(ids))
