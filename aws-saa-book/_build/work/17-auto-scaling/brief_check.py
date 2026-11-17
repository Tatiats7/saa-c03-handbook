"""Check brief.json: every fact id anywhere is verified; every [display] matches a display of a fact named
in the same text; ids of sections, traps and slots resolve. Writes brief_check.out next to this file.

Run: python3 aws-saa-book/_build/work/17-auto-scaling/brief_check.py
"""
import json
import pathlib
import re
import unicodedata

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parents[2]  # aws-saa-book/
brief = json.loads((HERE / "brief.json").read_text())

facts = {}
for p in (ROOT / "data" / "facts").glob("*.jsonl"):
    for line in p.read_text().splitlines():
        if line.strip():
            row = json.loads(line)
            facts[row["id"]] = row

PREFIX = r"(?:ec2-auto-scaling|aws-auto-scaling|ec2|elb|global-infrastructure)"
ID_RE = re.compile(r"\b" + PREFIX + r"-[a-z0-9]+(?:-[a-z0-9]+)*")
BR_RE = re.compile(r"\[([^\]]+)\]")


def norm(s):
    s = unicodedata.normalize("NFKC", s).replace("’", "'").replace("`", "")
    return re.sub(r"\s+", " ", s).strip().lower()


def displays(fid):
    return [norm(v.get("display", "")) for v in facts.get(fid, {}).get("values", [])]


problems, ids_seen = [], set()


def walk(node, path):
    if isinstance(node, dict):
        for k, v in node.items():
            walk(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, f"{path}[{i}]")
    elif isinstance(node, str):
        if path.endswith((".concept", ".service")):
            return
        # trap ids, item ids and wildcard family names are not fact ids
        node = re.sub(r"[a-z0-9-]+-trap-[a-z0-9-]+", " ", node)
        node = re.sub(r"\b[a-z0-9-]+-(?:c|q|s|t)\d{2,3}\b", " ", node)
        node = re.sub(r"\b[a-z0-9-]+-\*", " ", node)
        found = [m for m in ID_RE.findall(node) if "-trap-" not in m]
        for fid in found:
            ids_seen.add(fid)
            if fid not in facts:
                problems.append(f"UNKNOWN fact {fid} at {path}")
            elif facts[fid].get("status") != "verified":
                problems.append(f"NOT VERIFIED {fid} ({facts[fid].get('status')}) at {path}")
        disp_pool = [d for fid in found for d in displays(fid)]
        for br in BR_RE.findall(node):
            b = norm(br)
            if b.endswith(".md") or b.startswith("what is a scaling plan") or not found:
                continue
            if not any(d and d in b for d in disp_pool):
                problems.append(f"DISPLAY? [{br}] at {path} (facts: {', '.join(found)})")


walk(brief, "brief")

# section ids and trap placement
sec_ids = {f"{s['file']}#{s['section']}" for s in brief["sections"]}
for t in brief["traps"]:
    if t["placed_in"] not in sec_ids:
        problems.append(f"trap {t['id']} placed_in unknown section {t['placed_in']}")
for q in brief["question_slots"]:
    if q["section"] not in sec_ids:
        problems.append(f"slot {q['id']} section unknown {q['section']}")
for c in brief["cards"]:
    if c["section"] not in sec_ids:
        problems.append(f"card {c['id']} section unknown {c['section']}")
for t in brief["tasks"] + brief["speak"]:
    if t["section"] not in sec_ids:
        problems.append(f"{t['id']} section unknown {t['section']}")

# heading word counts of How-it-works subsections (5 to 14 words)
for s in brief["sections"]:
    if s["file"] == "2-deep.md" and isinstance(s.get("plan"), dict):
        n = len(s["heading"].split())
        if not 5 <= n <= 14:
            problems.append(f"heading length {n}: {s['heading']}")
        anchor = re.sub(r"[^a-z0-9 -]", "", s["heading"].lower()).replace(" ", "-")
        if anchor != s["section"]:
            problems.append(f"section id {s['section']} != anchor {anchor}")

# exam English ids
ee = set(re.findall(r'"id": "(ee-[^"]+)"', (ROOT / "data" / "exam-english.json").read_text()))
for q in brief["question_slots"]:
    for w in q["exam_english"]:
        if w not in ee:
            problems.append(f"slot {q['id']} unknown exam English {w}")

out = [f"fact ids seen: {len(ids_seen)}", f"problems: {len(problems)}"] + problems
(HERE / "brief_check.out").write_text("\n".join(out) + "\n")
print("\n".join(out[:80]))
