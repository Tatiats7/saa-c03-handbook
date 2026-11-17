"""adjudicate-34: compare finalize pending list with the cut batches (read-only)."""
import json, os, sys
ROOT = sys.argv[1]
fin = json.load(open(os.path.join(ROOT, "_build/work/34-streaming/finalize-3.json")))
pend = {p["id"]: p["missing"] for p in fin["pending"]}
inb = {}
for b in sys.argv[2:]:
    d = json.load(open(os.path.join(ROOT, "_build/facts/batches", b + ".json")))
    for f in d["facts"]:
        inb.setdefault(f, []).append(d["lens"])
print("pending", len(pend), "disputed", len(fin["disputed"]), "verified", len(fin["verified"]), "rejected", len(fin["rejected"]))
for i, m in sorted(pend.items()):
    miss = [l for l in m if l not in inb.get(i, [])]
    if miss:
        print("NOT BATCHED", i, miss)
for i in sorted(inb):
    if i not in pend:
        print("BATCHED NOT PENDING", i, inb[i])
