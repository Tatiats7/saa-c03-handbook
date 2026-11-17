"""W0 integration smoke test: the whole tool chain, end to end, in a sandbox, with real AWS pages.

    python3 aws-saa-book/tools/helpers/smoke.py setup      # fresh sandbox (keeps an existing corpus), patches, fetch
    python3 aws-saa-book/tools/helpers/smoke.py run        # setup + every step; writes _build/reports/w0-smoke.log

The sandbox is aws-saa-book/_build/tmp/smoke: a copy of the test fixture book (tools/tests/fixtures/book)
with one more service key, `vpc`, on its chapter 99. Nothing here touches real book data. The only network
access is `saa.py fetch` (two pages, cached after the first run). The inputs are in tools/helpers/smoke/.
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / "tests"))

import sandbox  # noqa: E402
from saalib import common  # noqa: E402

NAME = "smoke"
BOOK = common.REAL_BOOK / "_build" / "tmp" / NAME
INPUTS = HERE / "smoke"
LOG = common.REAL_BOOK / "_build" / "reports" / "w0-smoke.log"
NAT_URL = "https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-basics.html"
QUOTA_URL = "https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html"
NAT_SID = "docs/vpc/latest/userguide/nat-gateway-basics"
QUOTA_SID = "docs/vpc/latest/userguide/amazon-vpc-limits"

_log: list[str] = []
_failed: list[str] = []


def say(text: str) -> None:
    print(text)
    _log.append(text)


def step(title: str, *args: str, expect=(0,), keep: int = 14):
    """Run one saa.py command in the sandbox; check the exit code; log a bounded part of the output."""
    code, out, err = sandbox.run(BOOK, *args)
    ok = code in expect
    say(f"\n## {title}\n$ saa.py --book-dir _build/tmp/{NAME} {' '.join(args)}\nexit={code} expected={list(expect)} {'OK' if ok else 'UNEXPECTED'}")
    lines = (out.strip().splitlines() + [f"stderr: {x}" for x in err.strip().splitlines()])
    for line in lines[:keep]:
        say("  " + line[:300])
    if len(lines) > keep:
        say(f"  ... ({len(lines) - keep} more lines)")
    if not ok:
        _failed.append(title)
    return code, out, err


def check(title: str, ok: bool) -> None:
    say(f"  check: {title}: {'OK' if ok else 'FAILED'}")
    if not ok:
        _failed.append("check: " + title)


def step_json(title: str, *args: str, expect=(0,), keep: int = 14):
    code, out, err = step(title, *args, "--json", expect=expect, keep=keep)
    try:
        return code, json.loads(out)
    except ValueError:
        return code, None


def setup() -> None:
    corpus = BOOK / "_build" / "corpus"
    saved = common.REAL_BOOK / "_build" / "tmp" / (NAME + "-corpus-keep")
    if saved.exists():
        shutil.rmtree(saved)
    have_vpc = (corpus / "snap" / "docs" / "vpc").exists()
    if have_vpc:                      # keep the fetched pages, so a second run makes no request
        shutil.copytree(corpus, saved)
    sandbox.make(NAME)
    if have_vpc:
        shutil.rmtree(corpus)
        shutil.move(str(saved), str(corpus))

    def book(obj):
        ch = obj["chapters"][0]
        ch["services"] = ["widget", "vpc"]
        ch["sources"]["pages"] += [NAT_URL]
        ch["sources"]["quotas"] += [QUOTA_URL]
        obj["service_map"]["Amazon VPC"] = ["vpc"]
    sandbox.edit_json(BOOK / "data" / "book.json", book)

    def services(obj):
        obj["in_scope"].append({
            "id": "amazon-vpc", "official_name": "Amazon VPC", "short_name": None,
            "categories": ["Networking and Content Delivery"], "keys": ["vpc"], "home_chapter": "99",
            "level": "deep", "source_id": "docs/fixture/exam-guide/in-scope", "line": 15})
    sandbox.edit_json(BOOK / "_build" / "registry" / "services.json", services)
    sandbox.replace_text(BOOK / "99-sample" / "1-fast.md", "services: [widget]", "services: [widget, vpc]")
    say(f"sandbox {common.rel(BOOK)} ready (fixture book + service key vpc on chapter 99)")
    step("fetch the NAT gateway page and the VPC quotas page (real AWS pages)", "fetch", NAT_URL, QUOTA_URL)


def main(argv) -> int:
    mode = argv[1] if len(argv) > 1 else "run"
    setup()
    if mode == "run":
        import smoke_steps
        smoke_steps.run(sys.modules[__name__])
    common.ensure_dir(LOG.parent)
    LOG.write_text("\n".join(_log) + "\n", encoding="utf-8")
    say(f"\nlog: {common.rel(LOG)}")
    if _failed:
        print("SMOKE FAILED: " + "; ".join(_failed))
        return 1
    print("SMOKE OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
