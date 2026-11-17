"""Collect the source_ids saved by plan-25 from fetch-*.txt. Usage: python3 -I srcs.py OUT"""
import pathlib, re, sys, json
here = pathlib.Path(__file__).resolve().parent
rows, seen = [], set()
for f in sorted(here.glob("fetch-*.txt")):
    for line in f.read_text().splitlines():
        m = re.match(r"^(fetched|cached|unchanged|not-modified|changed) (\S+) status=(\d+) kind=(\S+) bytes=(\d+) title='(.*)'$", line)
        if m and m.group(2) not in seen:
            seen.add(m.group(2))
            rows.append({"source_id": m.group(2), "kind": m.group(4), "bytes": int(m.group(5)), "title": m.group(6), "batch": f.name})
pathlib.Path(sys.argv[1]).write_text(json.dumps(rows, indent=1))
print(len(rows))
