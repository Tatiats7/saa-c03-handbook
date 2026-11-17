"""Tests for saalib/corpus.py. Offline: the transport is replaced, the corpus is a temp folder."""
import argparse
import contextlib
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from saalib import common, corpus

DOCS = "https://docs.aws.amazon.com"
PAGE_HTML = DOCS + "/vpc/latest/userguide/nat-gateway-basics.html"
PAGE_MD = DOCS + "/vpc/latest/userguide/nat-gateway-basics.md"
SID = "docs/vpc/latest/userguide/nat-gateway-basics"
BODY_MARK = "ZEBRA-BODY-MARKER"

MD_BODY = f"""# NAT gateway basics
<a name="nat-gateway-basics"></a>

+ A NAT gateway supports 5 Gbps of bandwidth and automatically scales up to 100 Gbps\\. {BODY_MARK}

## Quotas
<a name="q"></a>

| Name | Default | Adjustable |
| --- | --- | --- |
| NAT gateways per Availability Zone | 5 | [Yes](https://console.aws.amazon.com/x) |
| Private IP addresses per NAT gateway | 8 | Yes |

```
# not a heading | not | a table
```
""".encode()

HTML_BODY = f"""<!DOCTYPE html><html><head><title>Amazon VPC FAQs</title>
<style>.x{{color:red}}</style><script>var hidden = "SCRIPT-TEXT";</script></head>
<body><header><a href="/">HEADER-TEXT</a></header><nav><ul><li>NAV-TEXT</li></ul></nav>
<main><h1>Amazon VPC FAQs</h1>
<h2>General</h2>
<p>Amazon VPC lets you provision a <a href="/x">logically isolated section</a> of the AWS&nbsp;Cloud. {BODY_MARK}</p>
<ul><li>First item</li><li>Second <b>item</b></li></ul>
<table><tr><th>Quota</th><th>Default</th></tr><tr><td>VPCs per Region</td><td><p>5</p></td></tr></table>
</main><footer>FOOTER-TEXT</footer><script>more()</script></body></html>""".encode()

LLMS = f"""# Amazon Virtual Private Cloud User Guide

> Summary.

- [What is Amazon VPC?]({DOCS}/vpc/latest/userguide/what-is-amazon-vpc.md)
- [Quotas]({DOCS}/vpc/latest/userguide/amazon-vpc-limits.md)
- [Document history]({DOCS}/vpc/latest/userguide/WhatsNew.md)
- [Full guide]({DOCS}/vpc/latest/userguide/full.md)

## [NAT]({DOCS}/vpc/latest/userguide/vpc-nat.md)

- [NAT gateway basics]({DOCS}/vpc/latest/userguide/nat-gateway-basics.md): Learn it.
- [Other guide]({DOCS}/AWSEC2/latest/UserGuide/concepts.md)
""".encode()


class FakeNet:
    """Stands in for corpus._transport. routes: url -> (status, headers, body) or a list of those."""

    def __init__(self, routes=None):
        self.routes = dict(routes or {})
        self.calls = []

    def __call__(self, url, headers, timeout):
        self.calls.append((url, dict(headers)))
        answer = self.routes.get(url)
        if answer is None:
            return (404, {"content-type": "text/html"}, b"<html>missing</html>")
        if isinstance(answer, list):
            answer = answer.pop(0) if len(answer) > 1 else answer[0]
        if isinstance(answer, Exception):
            raise answer
        return answer

    def urls(self, skip_robots=True):
        return [u for u, _ in self.calls if not (skip_robots and u.endswith("/robots.txt"))]


def md(body=MD_BODY, etag='"v1"'):
    return (200, {"content-type": "text/markdown", "etag": etag, "last-modified": "Mon, 01 Jun 2026 00:00:00 GMT"}, body)


class Base(unittest.TestCase):
    def setUp(self):
        common.ensure_dir(common.TMP)
        self.tmp = Path(tempfile.mkdtemp(prefix="test-corpus-", dir=common.TMP))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.net = FakeNet()
        self.sleeps = []
        for target, name, value in [
            (common, "CORPUS", self.tmp / "corpus"),
            (corpus, "_transport", self.net),
            (corpus, "_sleep", self.sleeps.append),
            (corpus, "MIN_INTERVAL", 0.0),
            (corpus, "_ROBOTS_MEMO", {}),
        ]:
            patcher = mock.patch.object(target, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def run_cli(self, *argv):
        parser = argparse.ArgumentParser()
        sub = parser.add_subparsers(dest="cmd")
        corpus.register(sub)
        args = parser.parse_args(list(argv))
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = args.func(args)
        return code, out.getvalue(), err.getvalue()

    def log(self):
        return common.read_jsonl(common.CORPUS / "fetch.log.jsonl")


class SourceIds(Base):
    def test_ids(self):
        cases = {
            PAGE_HTML: SID,
            PAGE_MD: SID,
            PAGE_HTML + "#anchor": SID,
            "https://aws.amazon.com/vpc/faqs/": "www/vpc/faqs",
            "https://d1.awsstatic.com/training-and-certification/docs/AWS-Guide.pdf": "static/training-and-certification/docs/AWS-Guide.pdf",
            "https://repost.aws/knowledge-center/nat-gateway": "repost/knowledge-center/nat-gateway",
            DOCS + "/vpc/latest/userguide/llms.txt": "docs/vpc/latest/userguide/llms.txt",
            DOCS + "/vpc/latest/userguide/": "docs/vpc/latest/userguide",
        }
        for url, sid in cases.items():
            self.assertEqual(corpus.source_id_for(url), sid, url)
        api = corpus.source_id_for("https://aws.amazon.com/api/dirs/items/search?item.directoryId=whats-new-v2&size=10")
        self.assertRegex(api, r"^api/whats-new-v2-[0-9a-f]{8}$")

    # Must-fail tests are named test_must_fail_<what> (TOOLS.md section 0 rule 10); `selftest` counts them.
    def test_must_fail_paths_and_traversal(self):
        paths = corpus.snapshot_paths(SID)
        self.assertEqual(paths["txt"], common.CORPUS / "snap" / (SID + ".txt"))
        self.assertEqual(set(paths), {"raw", "txt", "meta"})
        for bad in ("../x/y", "docs/../../etc", "/abs/path", "single", ""):
            with self.assertRaises(corpus.PolicyError):
                corpus.snapshot_paths(bad)
        self.assertNotIn("..", corpus.source_id_for(DOCS + "/a/%2e%2e/%2e%2e/b.html").split("/"))


class Policy(Base):
    def test_must_fail_foreign_host(self):
        for url in ("https://example.com/page.html", "https://docs.aws.amazon.com.evil.org/x.html",
                    "https://evil.org/?u=docs.aws.amazon.com", "ftp://docs.aws.amazon.com/x", "file:///etc/passwd",
                    "https://user:pw@docs.aws.amazon.com/x.html", "https://docs.aws.amazon.com:8443/x.html"):
            with self.assertRaises(corpus.PolicyError, msg=url):
                corpus.fetch(url)
        self.assertEqual(self.net.calls, [])
        code, out, err = self.run_cli("fetch", "https://example.com/page.html")
        self.assertEqual(code, common.EXIT_POLICY)
        self.assertEqual(self.net.calls, [])

    def test_must_fail_redirect_outside_allow_list(self):
        self.net.routes[PAGE_MD] = (302, {"location": "https://example.com/stolen.md"}, b"")
        with self.assertRaises(corpus.PolicyError):
            corpus.fetch(PAGE_HTML)
        self.assertNotIn("https://example.com/stolen.md", self.net.urls())
        self.assertIsNone(corpus.load_meta(SID))

    def test_redirect_inside_allow_list_records_final_url(self):
        final = DOCS + "/rds/latest/auroraextendedcontent/aurora-faq.html"
        self.net.routes["https://aws.amazon.com/rds/aurora/faqs/"] = (301, {"location": final}, b"")
        self.net.routes[final] = (200, {"content-type": "text/html"}, HTML_BODY)
        meta = corpus.fetch("https://aws.amazon.com/rds/aurora/faqs/")
        self.assertEqual(meta["final_url"], final)
        self.assertEqual(meta["url"], "https://aws.amazon.com/rds/aurora/faqs/")
        self.assertEqual(meta["source_id"], "www/rds/aurora/faqs")

    def test_must_fail_robots_disallow(self):
        self.net.routes[DOCS + "/robots.txt"] = (200, {"content-type": "text/plain"},
                                                 b"User-agent: *\nDisallow: /vpc/latest/userguide/nat\n")
        self.net.routes[PAGE_MD] = md()
        with self.assertRaises(corpus.PolicyError):
            corpus.fetch(PAGE_HTML)
        self.assertEqual(self.net.urls(), [])                      # the page was never requested
        code, out, err = self.run_cli("fetch", PAGE_HTML)
        self.assertEqual(code, common.EXIT_POLICY)
        self.assertIn("robots.txt", err + out)
        self.assertEqual(len(self.net.calls), 1)                   # robots.txt fetched once, then cached

    def test_must_fail_robots_unreachable_as_transient(self):
        self.net.routes[DOCS + "/robots.txt"] = (503, {}, b"")
        self.net.routes[PAGE_MD] = md()
        with self.assertRaises(corpus.TransientError):
            corpus.fetch(PAGE_HTML)
        self.assertEqual(self.net.urls(), [])

    def test_robots_matching_rules(self):
        rules, delay = corpus._parse_robots(
            "User-agent: other\nDisallow: /\n\nUser-agent: *\nCrawl-delay: 3\nDisallow: /about-aws/whats-new/2020/\n"
            "Disallow: /*?*tag=\nAllow: /about-aws/whats-new/2020/keep\nDisallow: /*.pdf$\n")
        self.assertEqual(delay, 3.0)
        self.assertTrue(corpus._robots_allowed(rules, "/vpc/faqs/"))
        self.assertFalse(corpus._robots_allowed(rules, "/about-aws/whats-new/2020/01/x/"))
        self.assertTrue(corpus._robots_allowed(rules, "/about-aws/whats-new/2020/keep/x"))
        self.assertFalse(corpus._robots_allowed(rules, "/blogs/?x=1&tag=y"))
        self.assertFalse(corpus._robots_allowed(rules, "/a/b.pdf"))
        self.assertTrue(corpus._robots_allowed(rules, "/a/b.pdf.html"))

    def test_must_fail_daily_cap(self):
        self.net.routes[PAGE_MD] = md()
        with mock.patch.object(corpus, "DAILY_CAP", 1):
            with self.assertRaises(corpus.CapError):
                corpus.fetch(PAGE_HTML)                              # robots.txt used the only request
            self.assertEqual(len(self.net.calls), 1)
            code, out, err = self.run_cli("fetch", PAGE_HTML)
            self.assertEqual(code, common.EXIT_POLICY)
        self.assertEqual(corpus.requests_today(), 1)

    def test_must_fail_binary_to_outside_book(self):
        code, out, err = self.run_cli("fetch", "https://d1.awsstatic.com/icons.zip", "--binary-to", "/tmp/icons.zip")
        self.assertEqual(code, common.EXIT_POLICY)
        self.assertEqual(self.net.calls, [])


class Fetch(Base):
    def test_md_twin_is_fetched_and_stored(self):
        self.net.routes[PAGE_MD] = md()
        meta = corpus.fetch(PAGE_HTML)
        self.assertEqual(self.net.urls(), [PAGE_MD])
        self.assertEqual(meta["state"], "fetched")
        self.assertEqual((meta["url"], meta["fetched_url"], meta["final_url"]), (PAGE_HTML, PAGE_MD, PAGE_MD))
        self.assertEqual(meta["title"], "NAT gateway basics")
        self.assertEqual(meta["kind"], "markdown")
        for key in ("source_id", "url", "fetched_url", "final_url", "status", "content_type", "etag", "last_modified",
                    "sha256", "text_sha256", "fetched_at", "title", "bytes"):
            self.assertIn(key, corpus.load_meta(SID), key)
        paths = corpus.snapshot_paths(SID)
        self.assertEqual(paths["raw"].read_bytes(), MD_BODY)
        self.assertEqual(corpus.load_text(SID), MD_BODY.decode())
        self.assertEqual(meta["sha256"], common.sha256_bytes(MD_BODY))
        self.assertIsNotNone(common.find_quote("automatically scales up to 100 Gbps.", corpus.load_text(SID)))
        self.assertIsNone(common.find_quote("automatically scales up to 45 Gbps.", corpus.load_text(SID)))
        sent = self.net.calls[-1][1]
        self.assertIn("Mozilla/5.0", sent["User-Agent"])

    def test_missing_twin_falls_back_to_html(self):
        self.net.routes[PAGE_HTML] = (200, {"content-type": "text/html; charset=utf-8"}, HTML_BODY)
        meta = corpus.fetch(PAGE_HTML)
        self.assertEqual(self.net.urls(), [PAGE_MD, PAGE_HTML])
        self.assertEqual((meta["kind"], meta["fetched_url"], meta["url"]), ("html", PAGE_HTML, PAGE_HTML))
        self.assertIn("logically isolated section", corpus.load_text(SID))

    def test_twin_that_is_really_html_falls_back(self):
        self.net.routes[PAGE_MD] = (200, {"content-type": "text/html"}, HTML_BODY)
        self.net.routes[PAGE_HTML] = (200, {"content-type": "text/html"}, HTML_BODY)
        self.assertEqual(corpus.fetch(PAGE_HTML)["fetched_url"], PAGE_HTML)

    def test_cache_hit_makes_no_request(self):
        self.net.routes[PAGE_MD] = md()
        corpus.fetch(PAGE_HTML)
        before = len(self.net.calls)
        again = corpus.fetch(PAGE_MD)                                # the twin URL maps to the same snapshot
        self.assertEqual(again["state"], "cached")
        self.assertEqual(len(self.net.calls), before)
        self.assertEqual(len(self.log()), before)

    def test_revalidate_304_keeps_snapshot(self):
        self.net.routes[PAGE_MD] = [md(), (304, {"etag": '"v1"'}, b"")]
        first = corpus.fetch(PAGE_HTML)
        second = corpus.fetch(PAGE_HTML, revalidate=True)
        self.assertEqual(second["state"], "not-modified")
        url, headers = self.net.calls[-1]
        self.assertEqual(url, PAGE_MD)
        self.assertEqual(headers["If-None-Match"], '"v1"')
        self.assertEqual(headers["If-Modified-Since"], "Mon, 01 Jun 2026 00:00:00 GMT")
        self.assertEqual(corpus.snapshot_paths(SID)["raw"].read_bytes(), MD_BODY)
        stored = corpus.load_meta(SID)
        self.assertEqual((stored["sha256"], stored["fetched_at"]), (first["sha256"], first["fetched_at"]))
        self.assertIn("revalidated_at", stored)

    def test_revalidate_changed_page_replaces_and_archives(self):
        new_body = MD_BODY.replace(b"100 Gbps", b"200 Gbps")
        self.net.routes[PAGE_MD] = [md(), md(new_body, '"v2"')]
        first = corpus.fetch(PAGE_HTML)
        second = corpus.fetch(PAGE_HTML, revalidate=True)
        self.assertEqual(second["state"], "changed")
        self.assertEqual(second["previous_sha256"], first["sha256"])
        self.assertIn("200 Gbps", corpus.load_text(SID))
        kept = list((common.CORPUS / "history").rglob("*.txt"))
        self.assertEqual(len(kept), 1)
        self.assertIn("100 Gbps", kept[0].read_text())

    def test_retry_then_success(self):
        self.net.routes[PAGE_MD] = [(503, {}, b""), (429, {"retry-after": "7"}, b""), md()]
        meta = corpus.fetch(PAGE_HTML)
        self.assertEqual(meta["status"], 200)
        self.assertEqual(self.net.urls(), [PAGE_MD] * 3)
        self.assertEqual(self.sleeps, [2.0, 7.0])
        self.assertEqual([r["status"] for r in self.log() if r["url"] == PAGE_MD], [503, 429, 200])

    def test_must_fail_persistent_5xx_transient(self):
        self.net.routes[PAGE_MD] = (500, {}, b"oops")
        with self.assertRaises(corpus.TransientError):
            corpus.fetch(PAGE_HTML)
        self.assertEqual(len(self.net.urls()), corpus.MAX_ATTEMPTS)
        self.assertIsNone(corpus.load_meta(SID))
        self.net.routes[PAGE_MD] = OSError("connection reset")
        code, out, err = self.run_cli("fetch", PAGE_HTML)
        self.assertEqual(code, common.EXIT_TRANSIENT)

    def test_must_fail_404_and_store_nothing(self):
        url = "https://aws.amazon.com/no-such-page/"
        with self.assertRaises(corpus.FetchError) as ctx:
            corpus.fetch(url)
        self.assertEqual(ctx.exception.status, 404)
        self.assertIsNone(corpus.load_meta("www/no-such-page"))
        self.assertIsNone(corpus.load_text("www/no-such-page"))
        code, out, err = self.run_cli("fetch", url)
        self.assertEqual(code, common.EXIT_FAIL)

    def test_rate_limit_reserves_one_slot_per_second(self):
        with mock.patch.object(corpus, "MIN_INTERVAL", 1.0):
            corpus._throttle()
            corpus._throttle()
            corpus._throttle()
        self.assertEqual(len(self.sleeps), 2)
        self.assertAlmostEqual(self.sleeps[0], 1.0, delta=0.2)
        self.assertAlmostEqual(self.sleeps[1], 2.0, delta=0.2)
        self.assertTrue((common.CORPUS / "rate.json").exists())
        self.assertTrue((common.CORPUS / "rate.json.lock").exists())
        self.assertEqual(corpus.requests_today(), 3)

    def test_json_is_stored_as_is_and_log_has_one_line_per_request(self):
        url = "https://aws.amazon.com/api/dirs/items/search?item.directoryId=whats-new-v2&size=1"
        body = b'{"items": [{"id": 1}]}'
        self.net.routes[url] = (200, {"content-type": "application/json"}, body)
        meta = corpus.fetch(url, source_id="api/whats-new-test")
        self.assertEqual((meta["kind"], meta["source_id"]), ("json", "api/whats-new-test"))
        self.assertEqual(corpus.load_text("api/whats-new-test"), body.decode())
        log = self.log()
        self.assertEqual(len(log), len(self.net.calls))
        self.assertEqual([r["url"] for r in log], ["https://aws.amazon.com/robots.txt", url])
        self.assertTrue(all("ts" in r and "status" in r for r in log))

    def test_cli_never_prints_the_page_body(self):
        self.net.routes[PAGE_MD] = md()
        self.net.routes["https://aws.amazon.com/vpc/faqs/"] = (200, {"content-type": "text/html"}, HTML_BODY)
        for extra in ([], ["--json"], ["--revalidate"], ["--revalidate", "--json"]):
            code, out, err = self.run_cli("fetch", PAGE_HTML, "https://aws.amazon.com/vpc/faqs/", *extra)
            self.assertEqual(code, common.EXIT_OK, err)
            self.assertNotIn(BODY_MARK, out + err)
            self.assertNotIn("Gbps", out + err)
            self.assertIn(SID, out)
            self.assertIn("nat-gateway-basics.txt", out)
        self.assertIn(BODY_MARK, corpus.load_text(SID))            # the body is on disk, not on the screen

    def test_batch_file_and_mixed_results(self):
        self.net.routes[PAGE_MD] = md()
        batch = self.tmp / "urls.txt"
        batch.write_text(f"# comment\n{PAGE_HTML}\n\nhttps://example.com/x\n")
        code, out, err = self.run_cli("fetch", "--batch", str(batch), "--json")
        self.assertEqual(code, common.EXIT_POLICY)
        result = json.loads(out)
        self.assertEqual([r["state"] for r in result["results"]], ["fetched", "error"])

    def test_binary_to_saves_bytes_inside_book(self):
        url = "https://d1.awsstatic.com/icons/Icon-package.zip"
        blob = b"PK\x03\x04" + bytes(range(256))
        self.net.routes[url] = (200, {"content-type": "application/zip"}, blob)
        dest = self.tmp / "icons" / "pkg.zip"
        code, out, err = self.run_cli("fetch", url, "--binary-to", str(dest))
        self.assertEqual(code, common.EXIT_OK, err)
        self.assertEqual(dest.read_bytes(), blob)
        self.assertEqual(common.read_json(Path(str(dest) + ".meta.json"))["sha256"], common.sha256_bytes(blob))


class VisibleText(Base):
    def test_extraction(self):
        text, title = corpus.html_to_text(HTML_BODY.decode())
        self.assertEqual(title, "Amazon VPC FAQs")
        lines = text.splitlines()
        for dropped in ("SCRIPT-TEXT", "HEADER-TEXT", "NAV-TEXT", "FOOTER-TEXT", "color:red", "more()"):
            self.assertNotIn(dropped, text)
        self.assertIn("# Amazon VPC FAQs", lines)
        self.assertIn("## General", lines)
        self.assertIn(f"Amazon VPC lets you provision a logically isolated section of the AWS Cloud. {BODY_MARK}", lines)
        self.assertIn("- First item", lines)
        self.assertIn("- Second item", lines)
        self.assertIn("| Quota | Default |", lines)
        self.assertIn("| VPCs per Region | 5 |", lines)
        self.assertIsNotNone(common.find_quote("provision a logically isolated section of the AWS Cloud", text))
        tables = corpus.parse_tables(text)
        self.assertEqual(tables[0]["rows"][0]["cells"], {"Quota": "VPCs per Region", "Default": "5"})

    def test_unclosed_header_does_not_swallow_the_page(self):
        page = "<html><body><header><div>" + "<p>Real content sentence.</p>" * 400 + "</body></html>"
        text, _ = corpus.html_to_text(page)
        self.assertIn("Real content sentence.", text)


class Reading(Base):
    def setUp(self):
        super().setUp()
        self.net.routes[PAGE_MD] = md()
        corpus.fetch(PAGE_HTML)

    def test_tables_with_headers_and_heading(self):
        tables = corpus.tables_for(SID)
        self.assertEqual(len(tables), 1)                            # the fenced block is not a table
        table = tables[0]
        self.assertEqual(table["heading"], "Quotas")
        self.assertEqual(table["headers"], ["Name", "Default", "Adjustable"])
        self.assertEqual(table["header_text"], "| Name | Default | Adjustable |")
        row = table["rows"][0]
        self.assertEqual(row["cells"]["Default"], "5")
        self.assertEqual(row["cells"]["Name"], "NAT gateways per Availability Zone")
        self.assertIsNotNone(common.find_quote(row["text"], corpus.load_text(SID)))
        code, out, err = self.run_cli("tables", SID, "--index", "0", "--json")
        self.assertEqual(code, common.EXIT_OK)
        self.assertEqual(json.loads(out)["tables"][0]["rows"][1]["cells"]["Default"], "8")
        code, out, err = self.run_cli("tables", SID, "--index", "5")
        self.assertEqual(code, common.EXIT_FAIL)

    def test_must_fail_tables_missing_source(self):
        code, out, err = self.run_cli("tables", "docs/not/fetched")
        self.assertEqual(code, common.EXIT_PRECONDITION)

    def test_search_bounds(self):
        big = common.CORPUS / "full" / "vpc-userguide.md"
        common.ensure_dir(big.parent)
        filler = "x" * 3000
        big.write_text("# Guide\n\n## NAT gateways\n\n" + "".join(
            f"{filler} needle number {i} {filler}\n" for i in range(50)), encoding="utf-8")
        result = corpus.search_corpus("needle number", scope="full", limit=7, per_file=0)
        self.assertEqual((result["shown"], result["total_hits"]), (7, 50))
        for hit in result["hits"]:
            self.assertLessEqual(len(hit["context"]), 210)
            self.assertIn("needle number", hit["context"])
            self.assertEqual((hit["source"], hit["heading"]), ("full:vpc-userguide", "NAT gateways"))
        self.assertEqual(result["hits"][0]["line"], 5)
        self.assertEqual(corpus.search_corpus("needle", scope="full", limit=10 ** 6, per_file=0)["limit"], corpus.SEARCH_MAX_LIMIT)
        self.assertEqual(corpus.search_corpus("needle", scope="full")["shown"], 5)     # per-file default
        snap = corpus.search_corpus("scales up to 100 gbps.", scope="snap")             # escapes and case ignored
        self.assertEqual([(h["source"], h["line"]) for h in snap["hits"]], [(SID, 4)])
        self.assertEqual(corpus.search_corpus(r"scales up to \d+ Gbps", scope="all", regex=True)["total_hits"], 1)
        self.assertEqual(corpus.search_corpus("needle number", scope="snap")["total_hits"], 0)
        code, out, err = self.run_cli("search", "needle number", "--scope", "full", "--limit", "3")
        self.assertEqual(code, common.EXIT_OK)
        self.assertEqual(len(out.splitlines()), 4)
        self.assertLess(len(out), 1500)
        code, out, err = self.run_cli("search", "no such text anywhere")
        self.assertEqual(code, common.EXIT_FAIL)
        code, out, err = self.run_cli("search", "([bad", "--regex")
        self.assertEqual(code, common.EXIT_FAIL)

    def test_show_is_bounded(self):
        long = common.CORPUS / "full" / "big.md"
        common.ensure_dir(long.parent)
        long.write_text("\n".join(f"line {i} " + "y" * 80 for i in range(1, 5001)) + "\n", encoding="utf-8")
        head = corpus.excerpt("full:big")
        self.assertLessEqual(len(head["text"]), 2000)
        self.assertEqual(head["start_line"], 1)
        huge = corpus.excerpt("full:big", chars=10 ** 9)
        self.assertLessEqual(len(huge["text"]), corpus.SHOW_MAX_CHARS)
        rng = corpus.excerpt("full:big", lines="10:12")
        self.assertEqual(rng["text"].splitlines()[0].split(" y")[0], "line 10")
        self.assertEqual((rng["start_line"], rng["end_line"]), (10, 12))
        self.assertLessEqual(corpus.excerpt("full:big", lines="1:5000")["end_line"], corpus.SHOW_MAX_LINES)
        mid = corpus.excerpt("full:big", around="line 2500 ", chars=600)
        self.assertEqual(mid["match_line"], 2500)
        self.assertLessEqual(len(mid["text"]), 600)
        self.assertLess(mid["start_line"], 2500)
        self.assertGreater(mid["end_line"], 2500)
        code, out, err = self.run_cli("show", PAGE_HTML, "--around", "scales up to 100 Gbps.")
        self.assertEqual(code, common.EXIT_OK)
        self.assertIn("match at line 4", out)
        self.assertIn(PAGE_HTML, out)
        code, out, err = self.run_cli("show", SID, "--around", "text that is not there")
        self.assertEqual(code, common.EXIT_FAIL)
        code, out, err = self.run_cli("show", "docs/not/fetched")
        self.assertEqual(code, common.EXIT_PRECONDITION)
        with self.assertRaises(corpus.PolicyError):
            corpus.resolve_source("full:../../secrets")


class Guide(Base):
    ROOT = DOCS + "/vpc/latest/userguide/"

    def test_guide_index(self):
        self.net.routes[self.ROOT + "llms.txt"] = (200, {"content-type": "text/plain"}, LLMS)
        self.net.routes[self.ROOT + "full.md"] = md(b"# Guide\n\n## NAT gateway basics\n\nscales up to 100 Gbps\n")
        code, out, err = self.run_cli("guide", self.ROOT + "llms.txt")
        self.assertEqual(code, common.EXIT_OK, err)
        self.assertEqual(self.net.urls(), [self.ROOT + "llms.txt", self.ROOT + "full.md"])
        index = corpus.load_index("vpc-userguide")
        self.assertEqual(index["title"], "Amazon Virtual Private Cloud User Guide")
        self.assertEqual(index["page_count"], 5)
        page = index["pages"][-1]
        self.assertEqual(page, {"title": "NAT gateway basics", "url": PAGE_HTML, "md_url": PAGE_MD, "source_id": SID})
        self.assertEqual(index["history"]["source_id"], "docs/vpc/latest/userguide/WhatsNew")
        self.assertEqual(index["quotas"]["source_id"], "docs/vpc/latest/userguide/amazon-vpc-limits")
        self.assertEqual(index["links_outside_guide"], 1)
        self.assertTrue((common.CORPUS / "full" / "vpc-userguide.md").exists())
        self.assertFalse((common.CORPUS / "snap" / "docs/vpc/latest/userguide/full.md.txt").exists())
        self.assertNotIn("Gbps", out)
        hits = corpus.search_corpus("100 Gbps", scope="full", guide="vpc-userguide")
        self.assertEqual(hits["hits"][0]["heading"], "NAT gateway basics")
        before = len(self.net.calls)
        self.assertEqual(self.run_cli("guide", self.ROOT)[0], common.EXIT_OK)       # second run: all cached
        self.assertEqual(len(self.net.calls), before)

    def test_history_names_differ_per_guide(self):
        for name, title in [("DocumentHistory", "Document history"), ("doc-history", "Document history for the guide"),
                            ("lambda-releases", "Lambda release notes"), ("sqs-release-notes", "Release notes"),
                            ("dochistory", "Doc history"), ("History", "Document history")]:
            pages = [{"title": "Getting started", "url": f"{DOCS}/g/x/start.html"},
                     {"title": "Viewing event history", "url": f"{DOCS}/g/x/view-history.html"},
                     {"title": title, "url": f"{DOCS}/g/x/{name}.html"}]
            best, _ = corpus._best(pages, corpus._score_history, 5)
            self.assertIsNotNone(best, name)
            self.assertTrue(best["url"].endswith(name + ".html"), name)

    def test_must_fail_guide_without_pages(self):
        self.net.routes[self.ROOT + "llms.txt"] = (200, {"content-type": "text/plain"}, b"# Empty\n")
        code, out, err = self.run_cli("guide", self.ROOT)
        self.assertEqual(code, common.EXIT_FAIL)
        self.assertIsNone(corpus.load_index("vpc-userguide"))

    def test_must_fail_guide_missing_llms(self):
        code, out, err = self.run_cli("guide", DOCS + "/cli/latest/reference/")
        self.assertEqual(code, common.EXIT_FAIL)


if __name__ == "__main__":
    unittest.main()
