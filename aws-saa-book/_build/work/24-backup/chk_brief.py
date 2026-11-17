"""Check every fact id named anywhere in brief.json: python3 chk_brief.py BRIEF
Prints ids that are missing or not verified (B04 checks only sections and traps; this checks all)."""
import json, re, sys
from pathlib import Path

root = Path(__file__).resolve().parents[3] / "data" / "facts"
status = {}
for p in root.glob("*.jsonl"):
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.strip():
            f = json.loads(line)
            status[f["id"]] = f.get("status")
brief = json.loads(Path(sys.argv[1]).read_text())
text = json.dumps(brief, ensure_ascii=False)
prefixes = ("backup-", "well-architected-", "ebs-", "rds-", "aurora-", "dynamodb-", "s3-", "efs-", "organizations-", "kms-")
ids = set(re.findall(r"\b((?:%s)[a-z0-9-]+)" % "|".join(p.rstrip("-") + "-" for p in prefixes), text))
skip_prefix = ("backup-trap-", "backup-q", "backup-c0", "backup-t0", "backup-s0", "backup-hero", "backup-before", "backup-after", "backup-lifecycle", "rds-trap-", "dynamodb-trap-", "aurora-trap-", "s3-trap-", "ebs-trap-", "kms-trap-")
bad = []
for i in sorted(ids):
    if i.startswith(skip_prefix) or i in ("backup-t01", "backup-plan"):
        continue
    st = status.get(i)
    if st != "verified":
        bad.append(f"{i}: {st}")
named = set()
for row in brief["sections"] + brief["traps"]:
    named.update(row.get("facts") or [])
print("named in sections/traps:", len(named), "not verified:", [i for i in named if status.get(i) != "verified"])
print("all ids in text not verified or unknown:")
for b in bad:
    print("  ", b)
