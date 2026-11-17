"""register-35: print the dump blocks of the fact ids given on the command line (read-only)."""
import sys

D = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/35-analytics/reg-dump.txt"
want = set(sys.argv[1:])
cur = None
for line in open(D):
    if line.startswith("=== "):
        cur = line[4:].split(" | ")[0].strip()
        if cur in want:
            print()
    if cur in want:
        print(line.rstrip()[:900])
