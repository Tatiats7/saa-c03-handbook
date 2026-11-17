"""Print the history and quota pointers of saved guide indexes, for the registry mapping step.

Read-only. Standard library only. It makes no network request.

    python3 aws-saa-book/tools/helpers/registry_pointers.py GUIDE_ID [GUIDE_ID ...]
    python3 aws-saa-book/tools/helpers/registry_pointers.py --find "quota|limit" GUIDE_ID
    python3 aws-saa-book/tools/helpers/registry_pointers.py --all

For each guide index (`_build/corpus/index/<guide-id>.json`, made by `saa.py guide ROOT`) it prints the chosen
history and quotas pages and the other candidates with their scores. `--find REGEX` lists every page of the guide
whose title or URL matches (case is ignored), so that a pointer the scorer missed can be found by hand.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from saalib import common  # noqa: E402


def _line(kind: str, item, chosen: bool) -> str:
    mark = "*" if chosen else " "
    return f"  {mark} {kind:7} {item.get('score', '-')!s:>3}  {item.get('title', '')!r}  {item.get('url', '')}"


def show(guide_id: str, find: str | None, limit: int) -> int:
    path = common.CORPUS / "index" / f"{guide_id}.json"
    index = common.read_json(path)
    if not index:
        print(f"{guide_id}: no index at {common.rel(path)}")
        return 1
    print(f"{guide_id}: {index.get('title')!r}, {index.get('page_count')} pages, root {index.get('root')}")
    if find:
        pattern = re.compile(find, re.IGNORECASE)
        shown = 0
        for page in index.get("pages", []):
            if pattern.search(page.get("title", "")) or pattern.search(page.get("url", "")):
                print(f"    {page.get('title', '')!r}  {page.get('url', '')}")
                shown += 1
                if shown >= limit:
                    print(f"    ... (limit {limit})")
                    break
        if not shown:
            print("    no page matches")
        return 0
    for kind in ("history", "quotas"):
        chosen = index.get(kind) or {}
        if chosen:
            print(_line(kind, chosen, True))
        else:
            print(f"    {kind:7} not found")
        for item in index.get(f"{kind}_candidates", []):
            if item.get("url") != chosen.get("url"):
                print(_line(kind, item, False))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("guides", nargs="*", help="guide ids, for example sns-dg")
    parser.add_argument("--all", action="store_true", help="every saved guide index")
    parser.add_argument("--find", help="list the pages whose title or URL matches this regular expression")
    parser.add_argument("--limit", type=int, default=40, help="most pages printed per guide with --find")
    args = parser.parse_args()
    guides = list(args.guides)
    if args.all:
        guides = sorted(p.stem for p in (common.CORPUS / "index").glob("*.json"))
    if not guides:
        parser.print_help()
        return common.EXIT_PRECONDITION
    code = 0
    for guide_id in guides:
        code = max(code, show(guide_id, args.find, args.limit))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
