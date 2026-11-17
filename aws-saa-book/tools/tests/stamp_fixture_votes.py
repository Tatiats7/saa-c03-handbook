#!/usr/bin/env python3
"""Write the `content` hash into the vote log of the TEST FIXTURE book (tools/tests/fixtures/book only).

    python3 aws-saa-book/tools/tests/stamp_fixture_votes.py

Run it after a change to a fixture fact or to facts.content_hash(). It never touches the real book:
real votes get their hash from `saa.py facts vote`, and a vote without the right hash does not count.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from saalib import common, facts  # noqa: E402

FIXTURE = HERE / "fixtures" / "book"

if __name__ == "__main__":
    changed = 0
    for path in sorted((FIXTURE / "data" / "facts").glob("*.jsonl")):
        canon = {row["id"]: row for row in common.read_jsonl(path)}
        log = FIXTURE / "_build" / "facts" / "votes" / path.name
        rows = common.read_jsonl(log)
        for vote in rows:
            fact = canon.get(vote.get("fact"))
            if fact is not None and vote.get("rev") == fact.get("rev"):
                want = facts.content_hash(fact)
                changed += vote.get("content") != want
                vote["content"] = want
        common.write_jsonl(log, rows)
    print(f"stamped {changed} fixture votes")
