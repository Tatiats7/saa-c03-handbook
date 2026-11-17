"""Registrar scan for chapter 24 (read-only). Usage: python3 -I reg_scan.py OUT_FILE"""
import json, re, sys, glob, os

ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
out = open(sys.argv[1], "w")
ABS = re.compile(r"\b(only|always|never|cannot|can't|must|by default|up to|at most|not supported|maximum|minimum)\b", re.I)


def words(s):
    return len(s.split())


facts = []
for line in open(ROOT + "/data/facts/backup.jsonl"):
    line = line.strip()
    if line:
        facts.append(json.loads(line))

# other namespaces authored by chapter 24 miners
others = []
for p in glob.glob(ROOT + "/data/facts/*.jsonl"):
    if p.endswith("backup.jsonl"):
        continue
    for line in open(p):
        line = line.strip()
        if not line:
            continue
        f = json.loads(line)
        if str(f.get("author", "")).startswith("mine-24") or "24" in str(f.get("amended_by", "")):
            others.append(f)

long_disp = []
hard_false_abs = []
no_question = []
for f in facts:
    if f["status"] in ("rejected", "superseded"):
        continue
    for v in f["values"]:
        d = v["display"]
        if not re.search(r"\d", d) and words(d) > 8:
            long_disp.append((f["id"], v["key"], d))
    if not f.get("hard") and ABS.search(f["claim"]):
        hard_false_abs.append((f["id"], f["kind"], f["claim"]))
    if f.get("hard") and not f.get("question"):
        no_question.append(f["id"])

out.write("LIVE %d\n" % sum(1 for f in facts if f["status"] not in ("rejected", "superseded")))
out.write("HARD %d\n" % sum(1 for f in facts if f["status"] not in ("rejected", "superseded") and f.get("hard")))
out.write("STATUS %s\n" % json.dumps({s: sum(1 for f in facts if f["status"] == s) for s in set(f["status"] for f in facts)}))
out.write("\n== LONG NUMBER-FREE DISPLAYS (%d)\n" % len(long_disp))
for i, k, d in long_disp:
    out.write("%s %s [%d] %s\n" % (i, k, words(d), d))
out.write("\n== HARD FALSE WITH ABSOLUTE WORD (%d)\n" % len(hard_false_abs))
for i, k, c in hard_false_abs:
    out.write("%s %s | %s\n" % (i, k, c))
out.write("\n== HARD WITHOUT QUESTION %s\n" % no_question)
out.write("\n== OTHER NAMESPACES BY CHAPTER 24 MINERS (%d)\n" % len(others))
for f in others:
    out.write("%s %s home=%s status=%s hard=%s\n" % (f["id"], f["service"], f["home_chapter"], f["status"], f.get("hard")))

out.write("\n== NON-BACKUP-GUIDE SOURCES\n")
for f in facts:
    if f["status"] in ("rejected", "superseded"):
        continue
    for e in f["evidence"]:
        if "aws-backup/latest" not in e["source_id"]:
            out.write("%s | %s\n" % (f["id"], e["source_id"]))
out.write("\n== QUALIFIERS\n")
for f in facts:
    if f["status"] in ("rejected", "superseded"):
        continue
    q = f["qualifiers"]
    out.write("%s | %s | hard=%s | rel=%s | t0=%s | vol=%s | scope=%s | dm=%s | adj=%s | cond=%s\n" % (
        f["id"], f["kind"], f.get("hard"), f.get("exam_relevance"), f.get("tier0"), f.get("volatility"),
        q.get("scope"), q.get("default_or_max"), q.get("adjustable"), q.get("condition")))
out.write("\n== QUOTES\n")
for f in facts:
    if f["status"] in ("rejected", "superseded"):
        continue
    for e in f["evidence"]:
        out.write("%s | %s | %s\n" % (f["id"], e["source_id"].split("/")[-1], e["quote"][:300]))
out.close()
print("ok")
