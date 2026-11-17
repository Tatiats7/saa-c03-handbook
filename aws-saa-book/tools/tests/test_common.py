import unittest

from saalib import common


class NormalizeText(unittest.TestCase):
    PAGE = """
# NAT gateway basics
<a name="nat-gateway-basics"></a>

+ A NAT gateway supports 5 Gbps of bandwidth and automatically scales up to 100 Gbps\\. If you require more bandwidth, you can split your resources into multiple subnets\\.
+ You can associate exactly one Elastic IP address with a public NAT gateway – see [Elastic IP addresses](elastic-ip-addresses.md "EIP") for details.
+ It’s a **managed** service; you can’t attach a `security group` to it.

| Quota | Default | Adjustable |
| --- | --- | --- |
| NAT gateways per Availability Zone | 5 | Yes |
"""

    def test_true_quotes_match(self):
        for quote in [
            "A NAT gateway supports 5 Gbps of bandwidth and automatically scales up to 100 Gbps.",
            "You can associate exactly one Elastic IP address with a public NAT gateway - see Elastic IP addresses for details.",
            "It's a managed service; you can't attach a security group to it.",
            "NAT gateways per Availability Zone | 5 | Yes",
        ]:
            self.assertIsNotNone(common.find_quote(quote, self.PAGE), quote)

    def test_paraphrase_must_fail(self):
        self.assertIsNone(common.find_quote("A NAT gateway supports up to 100 Gbps of bandwidth.", self.PAGE))

    def test_wrong_number_must_fail(self):
        self.assertIsNone(common.find_quote("A NAT gateway supports 5 Gbps of bandwidth and automatically scales up to 45 Gbps.", self.PAGE))

    def test_empty_quote_must_fail(self):
        self.assertIsNone(common.find_quote("   ", self.PAGE))

    def test_html_entities_and_tags(self):
        page = "<p>Amazon S3 is designed for 99.999999999% (11 9&#39;s) of durability&nbsp;of objects.</p>"
        self.assertIsNotNone(common.find_quote("designed for 99.999999999% (11 9's) of durability of objects", page))


class Registry(unittest.TestCase):
    def test_seed_loads(self):
        chapters = common.chapters()
        self.assertGreaterEqual(len(chapters), 50)
        self.assertEqual(common.chapter("iam")["id"], "03")
        self.assertTrue(str(common.chapter_dir("03")).endswith("aws-saa-book/03-iam"))


class Output(unittest.TestCase):
    def test_out_must_stay_inside_book(self):
        class Args:
            out = "/tmp/outside.txt"
            max_lines = 0
        with self.assertRaises(SystemExit) as ctx:
            common.emit("x", Args())
        self.assertEqual(ctx.exception.code, common.EXIT_POLICY)


if __name__ == "__main__":
    unittest.main()
