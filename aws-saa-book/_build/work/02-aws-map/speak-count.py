import json, re, sys
items = json.load(open(sys.argv[1]))
for it in items:
    lines = it["sixty_second"]
    words = sum(len(l.split()) for l in lines)
    print(it["id"], "lines", len(lines), "words", words, "ten", len(it["ten_second"].split()))
    for l in lines:
        for s in re.split(r"(?<=[.?!:])\s+", l):
            n = len(s.split())
            if n > 16:
                print("  long sentence", n, s)
