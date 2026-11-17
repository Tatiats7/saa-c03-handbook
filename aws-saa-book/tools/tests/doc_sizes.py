"""Print the word counts that test_contract.py and test_contract_tools.py compare with the document budgets.

Run:  python3 aws-saa-book/tools/tests/doc_sizes.py
Read-only. Also prints the SHA-256 of the fixture fact file, which gates/99.facts-final.json must hold.
"""
import hashlib
import re
from pathlib import Path

BOOK = Path(__file__).resolve().parents[2]
STYLE = BOOK / "_build" / "style"
FIX = BOOK / "tools" / "tests" / "fixtures" / "book"


def content_count(text):
    if text.startswith("---\n"):
        text = text[text.index("\n---\n", 4) + 5:]
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"\]\([^)]*\)", "]", text)
    return sum(1 for tok in text.split() if re.search(r"[A-Za-z0-9]", tok))


def tools_count(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"\]\([^)]*\)", "]", text)
    return sum(1 for tok in text.split() if re.search(r"[A-Za-z0-9]", tok))


def main():
    for name, fn, limit in (("CONVENTIONS.md", content_count, 4900), ("STYLE.md", content_count, 3000),
                            ("TOOLS.md", tools_count, 7400), ("TOOLS-items.md", tools_count, 4800)):
        n = fn((STYLE / name).read_text(encoding="utf-8"))
        print(f"{name}: {n} of {limit}")
    for path in sorted(STYLE.glob("*.md")):
        if path.name not in ("CONVENTIONS.md", "STYLE.md", "TOOLS.md", "TOOLS-items.md"):
            print(f"{path.name}: {tools_count(path.read_text(encoding='utf-8'))} (no budget)")
    for rel in ("data/facts/widget.jsonl", "99-sample/1-fast.md", "99-sample/2-deep.md"):
        print(rel, hashlib.sha256((FIX / rel).read_bytes()).hexdigest())
    for name in ("1-fast.md", "2-deep.md"):
        print(name, "words", content_count((FIX / "99-sample" / name).read_text(encoding="utf-8")))


if __name__ == "__main__":
    main()
