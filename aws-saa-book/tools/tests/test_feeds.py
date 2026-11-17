"""Tests for saalib/feeds.py. Offline: the transport is replaced, the corpus is a temp folder.

The samples in tests/fixtures/feeds/ are small cuts of pages captured on 2026-10-05 (VPC FAQ, EC2 FAQ,
Aurora FAQ, VPC document history, What's New API, customer-references API). Lines marked
"test text" in them are made up for the tests.
"""
import argparse
import contextlib
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from saalib import common, corpus, feeds

FIX = common.FIXTURES / "feeds"
VPC_FAQ = "https://aws.amazon.com/vpc/faqs/"
EC2_FAQ = "https://aws.amazon.com/ec2/faqs/"
AURORA_FAQ = "https://aws.amazon.com/rds/aurora/faqs/"
AURORA_ROOT = "https://docs.aws.amazon.com/rds/latest/auroraextendedcontent/"
HISTORY = "https://docs.aws.amazon.com/vpc/latest/userguide/WhatsNew.html"
HISTORY_MD = "https://docs.aws.amazon.com/vpc/latest/userguide/WhatsNew.md"
VPC_TAG = "whats-new-v2#general-products#amazon-vpc"


def fixture(name: str) -> bytes:
    return (FIX / name).read_bytes()


def html_answer(body: bytes):
    return (200, {"content-type": "text/html; charset=utf-8"}, body)


def md_answer(body: bytes):
    return (200, {"content-type": "text/markdown"}, body)


def json_answer(obj):
    return (200, {"content-type": "application/json"}, json.dumps(obj).encode())


class FakeNet:
    def __init__(self):
        self.routes = {}
        self.calls = []

    def __call__(self, url, headers, timeout):
        self.calls.append(url)
        return self.routes.get(url) or (404, {"content-type": "text/html"}, b"<html>missing</html>")

    def urls(self):
        return [u for u in self.calls if not u.endswith("/robots.txt")]


class Base(unittest.TestCase):
    def setUp(self):
        common.ensure_dir(common.TMP)
        self.tmp = Path(tempfile.mkdtemp(prefix="test-feeds-", dir=common.TMP))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.net = FakeNet()
        for target, name, value in [
            (common, "CORPUS", self.tmp / "corpus"),
            (corpus, "_transport", self.net),
            (corpus, "_sleep", lambda seconds: None),
            (corpus, "MIN_INTERVAL", 0.0),
            (corpus, "_ROBOTS_MEMO", {}),
        ]:
            patcher = mock.patch.object(target, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def run_cli(self, *argv):
        parser = argparse.ArgumentParser()
        feeds.register(parser.add_subparsers(dest="cmd"))
        args = parser.parse_args(list(argv))
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = args.func(args)
        return code, out.getvalue(), err.getvalue()

    def whatsnew_pages(self, size, tag="amazon-vpc", total=None):
        items = json.loads(fixture("whatsnew.json"))["items"]
        for page in range(0, (len(items) + size - 1) // size):
            url = feeds._api_url(feeds.WHATSNEW_DIR, feeds.WHATSNEW_SORT, size, page, f"{feeds.WHATSNEW_PRODUCT_NS}#{tag}")
            self.net.routes[url] = json_answer({"items": items[page * size:(page + 1) * size],
                                                "metadata": {"count": size, "totalHits": total or len(items)}})
        return items


class FaqTests(Base):
    def test_json_markup(self):
        self.net.routes[VPC_FAQ] = html_answer(fixture("faq_json.html"))
        code, out, _ = self.run_cli("faq", VPC_FAQ, "--json")
        self.assertEqual(code, common.EXIT_OK)
        summary = json.loads(out)
        self.assertEqual(summary["name"], "vpc")
        self.assertEqual(summary["questions"], 3)
        self.assertEqual(summary["by_parser"], {"json": 3})
        self.assertEqual(summary["final_url"], VPC_FAQ)
        self.assertFalse(summary["redirected"])
        rows = common.read_jsonl(common.CORPUS / "faq" / "vpc.jsonl")
        self.assertEqual([r["position"] for r in rows], [1, 2, 3])
        self.assertEqual(rows[0]["question"], "What is Amazon Virtual Private Cloud?")
        self.assertEqual(rows[0]["section"], "General Questions")
        self.assertEqual(rows[2]["section"], "Connectivity")
        self.assertIn("stateful gateway", rows[2]["answer"])
        self.assertTrue(all(r["line"] for r in rows))
        self.assertLess(rows[0]["line"], rows[1]["line"])
        # The parsed answer is a convenience copy; the snapshot text is the evidence and contains it.
        text = corpus.load_text("www/vpc/faqs")
        for row in rows:
            self.assertTrue(row["question_in_text"] and row["answer_in_text"])
            self.assertIsNotNone(common.find_quote(row["answer"], text))
        self.assertEqual(rows[0]["source_id"], "www/vpc/faqs")

    def test_footer_and_json_ld_are_not_questions(self):
        self.net.routes[VPC_FAQ] = html_answer(fixture("faq_json.html"))
        self.run_cli("faq", VPC_FAQ)
        questions = [r["question"] for r in common.read_jsonl(common.CORPUS / "faq" / "vpc.jsonl")]
        self.assertNotIn("is this a question?", questions)
        self.assertEqual(len(questions), len(set(questions)))

    def test_legacy_markup(self):
        self.net.routes[EC2_FAQ] = html_answer(fixture("faq_legacy.html"))
        code, out, _ = self.run_cli("faq", EC2_FAQ, "--list")
        self.assertEqual(code, common.EXIT_OK)
        rows = common.read_jsonl(common.CORPUS / "faq" / "ec2.jsonl")
        self.assertEqual([r["question"] for r in rows], [
            "What is Amazon Elastic Compute Cloud (Amazon EC2)?",
            "How quickly will systems be running?",
            "What does your Amazon EC2 Service Level Agreement guarantee?"])
        self.assertTrue(all(r["parser"] == "legacy" for r in rows))
        self.assertEqual(rows[0]["section"], "General / Overview")
        self.assertEqual(rows[2]["section"], "General / Service level agreement (SLA)")
        self.assertIn("less than 10 minutes", rows[1]["answer"])
        self.assertIn("This time depends on a number of factors", rows[1]["answer"])   # second paragraph kept
        self.assertNotIn("Q:", rows[1]["answer"])
        self.assertIn("at least 99.99%", rows[2]["answer"])
        self.assertTrue(all(r["answer_in_text"] for r in rows))
        self.assertIn("3 questions (legacy 3)", out)
        self.assertIn("How quickly will systems be running?", out)

    def test_find_is_bounded_and_fails_without_match(self):
        self.net.routes[EC2_FAQ] = html_answer(fixture("faq_legacy.html"))
        code, out, _ = self.run_cli("faq", EC2_FAQ, "--find", "runinstances", "--chars", "120")
        self.assertEqual(code, common.EXIT_OK)
        self.assertIn("Q: How quickly will systems be running?", out)
        self.assertIn("1 of 1 matches shown", out)
        self.assertNotIn("how recently you have launched", out)      # cut by --chars
        code, _, _ = self.run_cli("faq", EC2_FAQ, "--find", "zebra-not-there")
        self.assertEqual(code, common.EXIT_FAIL)
        self.assertEqual(self.net.urls().count(EC2_FAQ), 1)          # the second run used the cache

    def test_aurora_redirect_to_docs_guide(self):
        landing = AURORA_ROOT + "aurora-faq.html"
        self.net.routes[AURORA_FAQ] = (301, {"location": landing}, b"")
        self.net.routes[landing] = md_answer(fixture("aurora_faq.md"))
        code, out, _ = self.run_cli("faq", AURORA_FAQ, "--json")
        self.assertEqual(code, common.EXIT_OK)
        summary = json.loads(out)
        self.assertEqual(summary["name"], "rds-aurora")
        self.assertTrue(summary["redirected"])
        self.assertEqual(summary["final_url"], landing)
        self.assertEqual(summary["by_parser"], {"markdown": 2})
        self.assertTrue(any("--follow" in w for w in summary["warnings"]))
        rows = common.read_jsonl(common.CORPUS / "faq" / "rds-aurora.jsonl")
        self.assertEqual(rows[0]["question"], "Is Amazon Aurora MySQL compatible?")
        self.assertEqual(rows[0]["final_url"], landing)
        self.assertEqual(rows[0]["source_id"], "www/rds/aurora/faqs")
        self.assertNotIn("<a name", rows[0]["answer"])
        self.assertIsNotNone(common.find_quote(rows[0]["answer"], corpus.load_text("www/rds/aurora/faqs")))

    def test_aurora_follow_reads_the_faq_pages_of_the_guide(self):
        landing = AURORA_ROOT + "aurora-faq.html"
        self.net.routes[AURORA_FAQ] = (301, {"location": landing}, b"")
        self.net.routes[landing] = md_answer(fixture("aurora_faq.md"))
        self.net.routes[AURORA_ROOT + "llms.txt"] = (200, {"content-type": "text/plain"}, (
            f"# Aurora Extended Content\n\n## [Features]({AURORA_ROOT}aurora-features.md)\n\n"
            f"## [Amazon Aurora FAQ]({AURORA_ROOT}aurora-faq.md)\n\n- [Security]({AURORA_ROOT}aurora-faq-security.md)\n").encode())
        self.net.routes[AURORA_ROOT + "aurora-faq-security.md"] = md_answer(fixture("aurora_faq_security.md"))
        code, out, _ = self.run_cli("faq", AURORA_FAQ, "--follow", "--json")
        self.assertEqual(code, common.EXIT_OK)
        self.assertEqual(json.loads(out)["questions"], 3)
        rows = common.read_jsonl(common.CORPUS / "faq" / "rds-aurora.jsonl")
        self.assertEqual(rows[2]["question"], "Can I encrypt my Aurora database?")
        self.assertEqual(rows[2]["section"], "Encryption")
        self.assertEqual(rows[2]["source_id"], "docs/rds/latest/auroraextendedcontent/aurora-faq-security")
        self.assertEqual(rows[2]["url"], AURORA_ROOT + "aurora-faq-security.html")
        self.assertNotIn(AURORA_ROOT + "aurora-features.md", self.net.urls())       # not a FAQ page

    def test_must_fail_page_without_questions_is_not_reported_as_parsed(self):
        url = "https://aws.amazon.com/vpc/features/"
        self.net.routes[url] = html_answer(b"<html><head><title>Features</title></head><body><main><h1>Features</h1>"
                                           b"<p>No question here.</p></main></body></html>")
        code, out, _ = self.run_cli("faq", url, "--name", "nothing")
        self.assertEqual(code, common.EXIT_WARN)
        self.assertIn("0 questions", out)
        self.assertEqual(common.read_jsonl(common.CORPUS / "faq" / "nothing.jsonl"), [])

    def test_must_fail_foreign_host(self):
        code, _, err = self.run_cli("faq", "https://example.com/vpc/faqs/")
        self.assertEqual(code, common.EXIT_POLICY)
        self.assertIn("allow-list", err)
        self.assertEqual(self.net.calls, [])

    def test_must_fail_missing_page(self):
        code, _, _ = self.run_cli("faq", "https://aws.amazon.com/nope/faqs/")
        self.assertEqual(code, common.EXIT_FAIL)
        self.assertFalse((common.CORPUS / "faq" / "nope.jsonl").exists())

    def test_names(self):
        self.assertEqual(feeds.faq_name_for("https://aws.amazon.com/efs/faq/"), "efs")
        self.assertEqual(feeds.faq_name_for("https://aws.amazon.com/rds/aurora/faqs/"), "rds-aurora")
        self.assertEqual(feeds.faq_name_for(AURORA_ROOT + "aurora-faq.html"), "aurora-faq")

    def test_legacy_parser_details(self):
        rows = feeds.parse_legacy("### Billing\nQ: Is it free? No, you pay for what you use each month.\n"
                                  "Q. What is a subnet?\nA range of IP addresses.\n### Other\nnot an answer\n")
        self.assertEqual([(r["question"], r["answer"], r["section"]) for r in rows], [
            ("Is it free?", "No, you pay for what you use each month.", "Billing"),
            ("What is a subnet?", "A range of IP addresses.", "Billing")])


class ChangesTests(Base):
    def test_harvest_filters_by_date_and_never_crawls_post_pages(self):
        self.whatsnew_pages(size=1000)
        code, out, _ = self.run_cli("changes", "harvest", "--tag", "amazon-vpc", "--service", "VPC", "--json")
        self.assertEqual(code, common.EXIT_OK)
        result = json.loads(out)
        self.assertEqual((result["read"], result["kept"], result["total"]), (3, 2, 2))
        self.assertEqual(result["since"], "2022-07-01")
        rows = common.read_jsonl(common.CORPUS / "changes" / "vpc.jsonl")
        self.assertEqual([r["date"] for r in rows], ["2026-09-29", "2026-08-07"])
        first = rows[0]
        self.assertEqual(first["title"], "AWS DataSync now supports shared VPCs")
        self.assertEqual(first["url"], "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-datasync-shared-vpcs/")
        self.assertEqual(first["source"], "whatsnew")
        self.assertTrue(first["summary"].startswith("AWS DataSync now supports shared Virtual Private Clouds"))
        self.assertNotIn("<p>", first["text"])
        self.assertEqual(first["product_tags"], ["amazon-vpc", "aws-datasync"])
        # Only the directory API was called: no What's New post page (robots.txt disallows the old ones).
        self.assertTrue(self.net.urls())
        self.assertTrue(all(u.startswith(feeds.API_BASE + "?") for u in self.net.urls()))
        self.assertIn("tags.id=whats-new-v2%23general-products%23amazon-vpc", self.net.urls()[0])
        self.assertIn("size=1000", self.net.urls()[0])

    def test_since_option_and_idempotent_merge(self):
        self.whatsnew_pages(size=1000)
        self.run_cli("changes", "harvest", "--tag", "amazon-vpc", "--service", "vpc", "--since", "2021-01-01")
        code, out, _ = self.run_cli("changes", "harvest", "--tag", "amazon-vpc", "--service", "vpc", "--since", "2021-01-01", "--json")
        result = json.loads(out)
        self.assertEqual((result["kept"], result["added"], result["total"]), (3, 0, 3))
        self.assertEqual(len(self.net.urls()), 1)                       # the API answer was cached

    def test_paging_stops_at_since(self):
        self.whatsnew_pages(size=2, total=3)
        code, out, _ = self.run_cli("changes", "harvest", "--tag", "amazon-vpc", "--service", "vpc", "--page-size", "2", "--json")
        result = json.loads(out)
        self.assertEqual(code, common.EXIT_OK)
        self.assertEqual((result["pages"], result["read"], result["kept"], result["stopped"]), (2, 3, 2, "end"))
        self.assertIn("page=1", self.net.urls()[1])

    def test_paging_limit_is_respected_and_reported(self):
        items = json.loads(fixture("whatsnew.json"))["items"][:2]
        tag_id = f"{feeds.WHATSNEW_PRODUCT_NS}#amazon-vpc"
        for page in range(5):
            self.net.routes[feeds._api_url(feeds.WHATSNEW_DIR, feeds.WHATSNEW_SORT, 2, page, tag_id)] = \
                json_answer({"items": items, "metadata": {"count": 2, "totalHits": 100}})
        with mock.patch.object(feeds, "API_OFFSET_LIMIT", 4):
            code, out, _ = self.run_cli("changes", "harvest", "--tag", "amazon-vpc", "--service", "vpc",
                                        "--page-size", "2", "--json")
        result = json.loads(out)
        self.assertEqual(code, common.EXIT_WARN)
        self.assertEqual(result["stopped"], "paging-limit")
        self.assertEqual(len(self.net.urls()), 2)                       # offsets 0 and 2 only
        self.assertTrue(any("not covered" in w for w in result["warnings"]))

    def test_page_size_is_capped(self):
        self.assertIn("size=1000", feeds._api_url("d", "s", 1000, 0))
        self.whatsnew_pages(size=1000)
        code, _, _ = self.run_cli("changes", "harvest", "--tag", "amazon-vpc", "--service", "vpc", "--page-size", "5000")
        self.assertEqual(code, common.EXIT_OK)
        self.assertIn("size=1000", self.net.urls()[0])

    def test_must_fail_unknown_tag(self):
        url = feeds._api_url(feeds.WHATSNEW_DIR, feeds.WHATSNEW_SORT, 1000, 0, f"{feeds.WHATSNEW_PRODUCT_NS}#amazon-nope")
        self.net.routes[url] = json_answer({"items": [], "metadata": {"count": 0, "totalHits": 0}})
        code, _, err = self.run_cli("changes", "harvest", "--tag", "amazon-nope", "--service", "nope")
        self.assertEqual(code, common.EXIT_FAIL)
        self.assertIn("changes tags", err)
        self.assertFalse((common.CORPUS / "changes" / "nope.jsonl").exists())

    def test_must_fail_bad_inputs(self):
        code, _, _ = self.run_cli("changes", "harvest", "--tag", "amazon-vpc", "--service", "vpc", "--since", "last year")
        self.assertEqual(code, common.EXIT_PRECONDITION)
        code, _, _ = self.run_cli("changes", "harvest", "--tag", "x#y&size=9", "--service", "vpc")
        self.assertEqual(code, common.EXIT_PRECONDITION)
        self.assertEqual(self.net.calls, [])

    def test_must_fail_api_answer_that_is_not_json(self):
        url = feeds._api_url(feeds.WHATSNEW_DIR, feeds.WHATSNEW_SORT, 1000, 0, VPC_TAG)
        self.net.routes[url] = html_answer(b"<html><body>Service unavailable page</body></html>")
        code, _, err = self.run_cli("changes", "harvest", "--tag", "amazon-vpc", "--service", "vpc")
        self.assertEqual(code, common.EXIT_FAIL)
        self.assertIn("not the expected JSON", err)

    def test_history_table(self):
        self.net.routes[HISTORY_MD] = md_answer(fixture("history.md"))
        code, out, _ = self.run_cli("changes", "history", HISTORY, "--service", "vpc", "--json")
        self.assertEqual(code, common.EXIT_WARN)                         # one row without a date was skipped
        result = json.loads(out)
        self.assertEqual((result["read"], result["kept"]), (5, 4))
        self.assertEqual((result["newest"], result["oldest"]), ("2025-11-21", "2011-03-27"))
        rows = common.read_jsonl(common.CORPUS / "changes" / "vpc.jsonl")
        self.assertEqual([r["date"] for r in rows], ["2025-11-21", "2025-11-19", "2024-12-09", "2023-03-01"])
        nat = rows[1]
        self.assertEqual(nat["title"], "Regional NAT gateways for automatic multi-AZ expansion")
        self.assertTrue(nat["summary"].startswith("You can now use regional NAT gateways"))
        self.assertEqual(nat["url"], HISTORY)
        self.assertEqual(nat["link"], "https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html")
        self.assertEqual(nat["source"], "history")
        self.assertEqual(rows[3]["date_precision"], "month")
        # The stored row text is verbatim, so it can be checked against the snapshot.
        self.assertIsNotNone(common.find_quote(nat["quote"], corpus.load_text("docs/vpc/latest/userguide/WhatsNew")))

    def test_must_fail_history_page_without_dated_table(self):
        url = "https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html"
        self.net.routes[url[:-5] + ".md"] = md_answer(b"# What is Amazon VPC?\n\n| Name | Default |\n| --- | --- |\n| VPCs per Region | 5 |\n")
        code, _, err = self.run_cli("changes", "history", url, "--service", "vpc")
        self.assertEqual(code, common.EXIT_FAIL)
        self.assertIn("no table with dated rows", err)
        self.assertFalse((common.CORPUS / "changes" / "vpc.jsonl").exists())

    def test_for_merges_both_sources_and_is_bounded(self):
        self.whatsnew_pages(size=1000)
        self.net.routes[HISTORY_MD] = md_answer(fixture("history.md"))
        self.run_cli("changes", "harvest", "--tag", "amazon-vpc", "--service", "vpc")
        self.run_cli("changes", "history", HISTORY, "--service", "vpc")
        code, out, _ = self.run_cli("changes", "for", "vpc", "--json")
        result = json.loads(out)
        self.assertEqual(code, common.EXIT_OK)
        self.assertEqual(result["matches"], 6)
        self.assertEqual([r["source"] for r in result["rows"][:3]], ["whatsnew", "whatsnew", "history"])
        code, out, _ = self.run_cli("changes", "for", "vpc", "--since", "2025-01-01", "--limit", "2")
        self.assertIn("2 of 4 change items shown", out)
        self.assertEqual(out.count("https://"), 2)
        code, out, _ = self.run_cli("changes", "for", "vpc", "--source", "history", "--find", "regional nat")
        self.assertIn("1 of 1 change items shown", out)
        code, _, _ = self.run_cli("changes", "for", "vpc", "--find", "zebra-not-there")
        self.assertEqual(code, common.EXIT_FAIL)

    def test_must_fail_for_unknown_service(self):
        code, _, err = self.run_cli("changes", "for", "nothing-here")
        self.assertEqual(code, common.EXIT_PRECONDITION)
        self.assertIn("changes harvest", err)

    def test_tags(self):
        code, _, _ = self.run_cli("changes", "tags")
        self.assertEqual(code, common.EXIT_PRECONDITION)                 # nothing collected yet
        items = json.loads(fixture("whatsnew.json"))["items"]
        self.net.routes[feeds._api_url(feeds.WHATSNEW_DIR, feeds.WHATSNEW_SORT, 1000, 0)] = \
            json_answer({"items": items, "metadata": {"count": 3, "totalHits": 3}})
        code, out, _ = self.run_cli("changes", "tags", "--refresh", "--json")
        self.assertEqual(code, common.EXIT_OK)
        result = json.loads(out)
        self.assertEqual([(t["tag"], t["sample_count"]) for t in result["tags"]], [("amazon-vpc", 3), ("aws-datasync", 1)])
        self.assertNotIn("tags.id", self.net.urls()[0])
        code, out, _ = self.run_cli("changes", "tags", "--find", "datasync")
        self.assertIn("aws-datasync", out)
        self.assertNotIn("amazon-vpc ", out)
        code, out, _ = self.run_cli("changes", "tags", "--all-namespaces", "--find", "2026")
        self.assertIn("whats-new-v2#year", out)
        code, _, _ = self.run_cli("changes", "tags", "--find", "zebra-not-there")
        self.assertEqual(code, common.EXIT_FAIL)

    def test_dates(self):
        self.assertEqual(feeds.parse_date("November 21, 2025"), ("2025-11-21", "day"))
        self.assertEqual(feeds.parse_date("Sept 5 2023"), ("2023-09-05", "day"))
        self.assertEqual(feeds.parse_date("21 Nov 2025"), ("2025-11-21", "day"))
        self.assertEqual(feeds.parse_date("2024-02-29"), ("2024-02-29", "day"))
        self.assertEqual(feeds.parse_date("March 2023"), ("2023-03-01", "month"))
        self.assertIsNone(feeds.parse_date("February 30, 2025"))
        self.assertIsNone(feeds.parse_date("soon"))
        self.assertIsNone(feeds.parse_date("Version 2025"))


class CasesTests(Base):
    def cases_route(self, tag="dynamodb"):
        url = feeds._api_url(feeds.CASES_DIR, feeds.CASES_SORT, 1000, 0, f"{feeds.CASES_PRODUCT_NS}#{tag}" if tag else "")
        self.net.routes[url] = (200, {"content-type": "application/json"}, fixture("cases.json"))

    def test_harvest_and_for(self):
        self.cases_route()
        code, out, _ = self.run_cli("cases", "harvest", "--tag", "dynamodb", "--json")
        self.assertEqual(code, common.EXIT_OK)
        self.assertEqual(json.loads(out)["total"], 2)
        self.assertIn("tags.id=GLOBAL%23product%23dynamodb", self.net.urls()[0])
        rows = {r["customer"]: r for r in common.read_jsonl(common.CORPUS / "cases" / "index.jsonl")}
        genesys = rows["Genesys"]
        self.assertEqual(genesys["title"], "Achieving 99.999% Availability Using Amazon DynamoDB at Genesys")
        self.assertEqual(genesys["url"], "https://aws.amazon.com/solutions/case-studies/genesys-dynamodb-case-study/")
        self.assertEqual(genesys["date"], "2025-02-27")
        self.assertEqual(genesys["tags"], ["dynamodb", "ec2"])
        self.assertEqual(genesys["segments"], ["enterprise"])
        self.assertTrue(genesys["summary"].startswith("Genesys built Genesys Cloud using AWS"))
        self.assertTrue(genesys["english"] and genesys["fetchable"])
        self.assertFalse(rows["Greenn"]["english"])
        self.assertNotIn("<p>", rows["Greenn"]["summary"])

        code, out, _ = self.run_cli("cases", "for", "dynamodb")
        self.assertEqual(code, common.EXIT_OK)
        self.assertIn("Genesys", out)
        self.assertNotIn("Greenn", out)                                   # English only by default
        self.assertIn("1 of 1 case studies shown", out)
        self.assertIn("quote from its snapshot", out)
        code, out, _ = self.run_cli("cases", "for", "dynamodb", "--all-languages", "--json")
        self.assertEqual(json.loads(out)["matches"], 2)
        code, out, _ = self.run_cli("cases", "for", "ec2", "--segment", "enterprise", "--since", "2025-01-01")
        self.assertIn("Genesys", out)
        self.assertEqual(len(self.net.urls()), 1)                         # `for` makes no request

    def test_harvest_twice_does_not_duplicate(self):
        self.cases_route()
        self.run_cli("cases", "harvest", "--tag", "dynamodb")
        code, out, _ = self.run_cli("cases", "harvest", "--tag", "dynamodb", "--refresh", "--json")
        result = json.loads(out)
        self.assertEqual((result["added"], result["total"]), (0, 2))
        self.assertEqual(len(self.net.urls()), 2)                         # --refresh asked the API again

    def test_harvest_whole_directory_and_tags(self):
        self.cases_route(tag="")
        code, _, _ = self.run_cli("cases", "harvest")
        self.assertEqual(code, common.EXIT_OK)
        self.assertNotIn("tags.id", self.net.urls()[0])
        code, out, _ = self.run_cli("cases", "tags", "--json")
        tags = {t["tag"]: t for t in json.loads(out)["tags"]}
        self.assertEqual(tags["dynamodb"]["count"], 2)
        self.assertEqual(tags["ec2"]["name"], "Amazon EC2")
        code, out, _ = self.run_cli("cases", "tags", "--find", "lambda")
        self.assertIn("AWS Lambda", out)
        self.assertNotIn("Amazon EC2", out)

    def test_must_fail_for_without_match_or_index(self):
        code, _, err = self.run_cli("cases", "for", "dynamodb")
        self.assertEqual(code, common.EXIT_PRECONDITION)
        self.assertIn("cases harvest", err)
        self.cases_route()
        self.run_cli("cases", "harvest", "--tag", "dynamodb")
        code, out, _ = self.run_cli("cases", "for", "redshift")
        self.assertEqual(code, common.EXIT_FAIL)
        self.assertIn("0 of 0", out)
        code, _, _ = self.run_cli("cases", "for", "GLOBAL#product#dynamodb")
        self.assertEqual(code, common.EXIT_PRECONDITION)

    def test_must_fail_unknown_tag(self):
        url = feeds._api_url(feeds.CASES_DIR, feeds.CASES_SORT, 1000, 0, f"{feeds.CASES_PRODUCT_NS}#nope")
        self.net.routes[url] = json_answer({"items": [], "metadata": {"count": 0, "totalHits": 0}})
        code, _, err = self.run_cli("cases", "harvest", "--tag", "nope")
        self.assertEqual(code, common.EXIT_FAIL)
        self.assertIn("cases tags", err)
        self.assertFalse((common.CORPUS / "cases" / "index.jsonl").exists())

    def test_must_fail_robots_refusal_stops_the_harvest(self):
        self.net.routes["https://aws.amazon.com/robots.txt"] = (200, {"content-type": "text/plain"},
                                                                 b"User-agent: *\nDisallow: /api/\n")
        self.cases_route()
        code, _, err = self.run_cli("cases", "harvest", "--tag", "dynamodb")
        self.assertEqual(code, common.EXIT_POLICY)
        self.assertIn("robots.txt", err)
        self.assertEqual(self.net.urls(), [])


if __name__ == "__main__":
    unittest.main()
