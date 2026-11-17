"""One-time, repeatable migration of data/terms.json for contract fix 1 (see _build/reports/contract-fix.md).

Run:  python3 aws-saa-book/tools/helpers/contract_fix_terms.py [--book-dir DIR]

What it does (safe to run twice):
1. Splits `banned` into three lists, because the lint can only match literal text:
   - `banned`       literal variants, matched without regard to case (lint L901);
   - `banned_case`  variants that are wrong only in this exact capitalisation (lint L901, case-sensitive);
   - `avoid`        variants that are wrong only in a context, written as "text (context)"; reviewers check them, the lint does not.
2. Renames the term ids that differ from the GitHub anchor of their term, so that glossary anchors equal ids.
"""
import json
import re
import sys
from pathlib import Path

CASE_ONLY = re.compile(r"^(.*?) \((lowercase|capitalised)\)$")
# Single common words that are correct in other AWS terms ("hosted zone", "state machine", "a secret in Secrets Manager").
CONTEXT_WORDS = {"zone", "machine", "secret", "script", "drive"}


def anchor(term):
    return re.sub(r"[^a-z0-9 -]", "", term.lower()).replace(" ", "-")


def split(banned, old_case, old_avoid):
    literal, case, avoid = [], list(old_case), list(old_avoid)
    for entry in banned:
        m = CASE_ONLY.match(entry)
        if m:
            case.append(m.group(1))
        elif "(" in entry:
            avoid.append(entry)
        elif entry in CONTEXT_WORDS:
            avoid.append(entry + " (when it stands for this term)")
        else:
            literal.append(entry)
    return literal, case, avoid


def main(argv):
    book = Path(__file__).resolve().parents[2]
    if "--book-dir" in argv:
        book = Path(argv[argv.index("--book-dir") + 1]).resolve()
    path = book / "data" / "terms.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    renamed = []
    out = []
    for term in data["terms"]:
        literal, case, avoid = split(term["banned"], term.get("banned_case", []), term.get("avoid", []))
        new_id = anchor(term["term"])
        if new_id != term["id"]:
            renamed.append((term["id"], new_id))
        row = {}
        for key, value in term.items():
            if key in ("banned_case", "avoid"):
                continue
            row[key] = new_id if key == "id" else (literal if key == "banned" else value)
            if key == "banned":
                row["banned_case"] = case
                row["avoid"] = avoid
        out.append(row)
    ids = [t["id"] for t in out]
    if len(ids) != len(set(ids)):
        print("duplicate ids after rename; nothing written")
        return 1
    lines = ["{", ' "v": 1,', ' "note": ' + json.dumps(data["note"], ensure_ascii=False) + ",", ' "terms": [']
    lines += ["  " + json.dumps(t, ensure_ascii=False) + ("," if i < len(out) - 1 else "") for i, t in enumerate(out)]
    lines += [" ]", "}"]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"terms": len(out), "renamed": renamed,
                      "banned_case": sum(len(t["banned_case"]) for t in out), "avoid": sum(len(t["avoid"]) for t in out)}))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
