"""Print fact cards of chapter 31 by id (exact) or by substring search (-s word)."""
import re
import sys

t = open('aws-saa-book/_build/work/31-messaging/fact-cards.md').read()
blocks = re.split(r'\n(?=\S)', t)
args = sys.argv[1:]
if args and args[0] == '-s':
    words = [w.lower() for w in args[1:]]
    for b in blocks:
        if all(w in b.lower() for w in words):
            print(b)
else:
    want = set(args)
    found = set()
    for b in blocks:
        fid = b.split('\n')[0].strip()
        if fid in want:
            print(b)
            found.add(fid)
    for m in sorted(want - found):
        print('MISSING', m)
