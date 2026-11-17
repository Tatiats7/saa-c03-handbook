"""Tests for the diagram system (saalib/diagram). Run: python3 aws-saa-book/tools/tests/run.py diagram

Nothing here touches real book data: specs are built in memory, icons are a small fake set, and
the one test that writes files patches the paths to a sandbox under _build/tmp/.
"""
import copy
import json
import shutil
import unittest
from pathlib import Path
from unittest import mock

from saalib import common
from saalib.diagram import arch, icons, layout_grid, lint, pipeline, preview, route, schema, svg, textmetrics
from saalib.diagram import style as S

FIX = Path(__file__).resolve().parent / "fixtures" / "diagram"
SANDBOX = common.REAL_BOOK / "_build" / "tmp" / "test-diagram"

FAKE_BODY = '<rect width="48" height="48" fill="#8C4FFF"/>'
FAKE_ICONS = {name: {"viewBox": "0 0 48 48", "body": FAKE_BODY, "kind": "resource"}
              for name in ("users", "alb", "instance", "db-instance", "db-instance-standby", "s3", "internet")}
FAKE_ICONS["users"]["dark"] = '<rect width="48" height="48" fill="#FFFFFF"/>'


def base_spec() -> dict:
    return {
        "id": "t-basic", "kind": "arch", "size": "s",
        "title": "A test figure",
        "claim": "The request goes from the users to the server.",
        "alt": "Users send a request to a load balancer, which forwards it to a server.",
        "cols": 2, "rows": 3,
        "groups": [{"id": "vpc", "type": "vpc", "label": "VPC", "cells": "A2:B3"}],
        "nodes": [
            {"id": "users", "icon": "users", "label": "Users", "at": "A1:B1"},
            {"id": "alb", "icon": "alb", "label": "Load balancer", "at": "A2:B2"},
            {"id": "a", "icon": "instance", "label": "App server", "at": "A3"},
            {"id": "b", "icon": "instance", "label": "App server", "at": "B3"},
        ],
        "edges": [
            {"from": "users", "to": "alb", "step": 1, "label": "HTTPS", "say": "The user sends a request."},
            {"from": "alb", "to": "a", "step": 2, "say": "The load balancer forwards the request."},
            {"from": "alb", "to": "b", "step": 2},
        ],
    }


def check(spec):
    return pipeline.check_spec(spec, icons=FAKE_ICONS)


def codes(result, level="error"):
    return {i["code"] for i in result["issues"] if i["level"] == level}


class SchemaTests(unittest.TestCase):
    def test_valid_spec_passes(self):
        self.assertEqual(schema.validate(base_spec()), [])

    def test_must_fail_missing_title(self):
        spec = base_spec()
        del spec["title"]
        self.assertIn("schema", codes(check(spec)))

    def test_must_fail_unknown_property(self):
        spec = base_spec()
        spec["nodes"][0]["colour"] = "#ff0000"       # literal colours are not part of the spec
        errors = schema.validate(spec)
        self.assertTrue(any("unknown property 'colour'" in e for e in errors), errors)

    def test_must_fail_bad_cell(self):
        spec = base_spec()
        spec["nodes"][0]["at"] = "1A"
        self.assertTrue(schema.validate(spec))

    def test_must_fail_bad_group_type_and_step(self):
        spec = base_spec()
        spec["groups"][0]["type"] = "cloud"
        spec["edges"][0]["step"] = 0
        errors = schema.validate(spec)
        self.assertEqual(len(errors), 2, errors)

    def test_must_fail_unsupported_kind(self):
        spec = base_spec()
        spec["kind"] = "hologram"
        self.assertTrue(schema.validate(spec))
        spec["kind"] = "sequence"
        if "sequence" not in pipeline.KINDS:
            self.assertTrue(any("not supported yet" in e for e in schema.validate(spec)))


class LimitTests(unittest.TestCase):
    def test_base_is_clean(self):
        result = check(base_spec())
        self.assertEqual(result["issues"], [])
        self.assertEqual(result["stats"]["crossings"], 0)

    def test_must_fail_too_many_nodes(self):
        spec = base_spec()
        spec["cols"], spec["rows"] = 4, 5
        spec["groups"] = []
        spec["nodes"] = [{"id": f"n{i}", "icon": "instance", "label": "Node", "at": f"{'ABCD'[i % 4]}{i // 4 + 1}"}
                         for i in range(13)]
        spec["edges"] = []
        self.assertIn("limit-nodes", codes(check(spec)))

    def test_must_fail_unlabelled_edge(self):
        spec = base_spec()
        spec["edges"].append({"from": "a", "to": "b"})
        self.assertIn("edge-unlabelled", codes(check(spec)))

    def test_must_fail_unknown_icon_and_unknown_node(self):
        spec = base_spec()
        spec["nodes"][0]["icon"] = "no-such-icon"
        spec["edges"][0]["to"] = "ghost"
        found = codes(check(spec))
        self.assertIn("icon-unknown", found)
        self.assertIn("ref-unknown", found)

    def test_must_fail_three_azs_and_lone_region(self):
        spec = base_spec()
        spec["cols"] = 3
        spec["groups"] = [
            {"id": "r", "type": "region", "label": "Region", "cells": "A2:C3"},
            {"id": "z1", "type": "az", "label": "AZ a", "in": "r", "cells": "A3"},
            {"id": "z2", "type": "az", "label": "AZ b", "in": "r", "cells": "B3"},
            {"id": "z3", "type": "az", "label": "AZ c", "in": "r", "cells": "C3"},
        ]
        found = codes(check(spec))
        self.assertIn("limit-az", found)
        self.assertIn("lone-region", found)

    def test_must_fail_sentence_label_and_step_rules(self):
        spec = base_spec()
        spec["nodes"][1]["label"] = "This balancer spreads the load."
        spec["edges"][1]["step"] = 4
        spec["edges"][2]["step"] = 4
        found = codes(check(spec))
        self.assertIn("sentence", found)
        self.assertIn("steps-gap", found)

    def test_must_fail_step_without_say_and_two_sentence_claim(self):
        spec = base_spec()
        del spec["edges"][1]["say"]
        spec["claim"] = "First sentence. Second sentence."
        found = codes(check(spec))
        self.assertIn("step-without-say", found)
        self.assertIn("claim", found)

    def test_must_fail_groups_that_cross(self):
        spec = base_spec()
        spec["groups"].append({"id": "x", "type": "generic", "label": "Cross", "cells": "A1:A2"})
        self.assertIn("layout", codes(check(spec)))

    def test_two_headed_arrow_warns(self):
        spec = base_spec()
        spec["edges"][0]["arrow"] = "both"
        self.assertIn("two-headed", codes(check(spec), "warn"))


class GeometryTests(unittest.TestCase):
    def test_must_fail_node_overlap(self):
        spec = base_spec()
        spec["nodes"][3]["at"] = "A3"                 # two nodes in one cell
        self.assertIn("node-overlap", codes(check(spec)))

    def test_must_fail_text_overflow(self):
        spec = base_spec()
        spec["nodes"][2]["label"] = "Supercalifragilisticexpialidocious"
        self.assertIn("text-overflow", codes(check(spec)))

    def test_must_fail_three_line_label(self):
        spec = base_spec()
        spec["nodes"][2]["label"] = "Application\nserver\nfleet"
        self.assertIn("text-lines", codes(check(spec)))

    def test_must_fail_edge_through_node(self):
        scene = copy.deepcopy(check(base_spec())["scene"])
        users = next(n for n in scene["nodes"] if n["id"] == "users")
        a = next(n for n in scene["nodes"] if n["id"] == "a")
        # a hand-made edge from the users straight down to app server a passes through nothing,
        # so bend it through the load balancer icon
        alb = next(n for n in scene["nodes"] if n["id"] == "alb")
        cx = alb["icon_box"][0] + 24
        scene["edges"].append({"index": 99, "from": "users", "to": "a", "arrow": "end", "emph": False, "dashed": False,
                               "label": None, "badge": None, "no_room": False, "sides": ("bottom", "top"),
                               "points": [users["ports"]["bottom"], (cx, a["ports"]["top"][1] - 20),
                                          (a["ports"]["top"][0], a["ports"]["top"][1] - 20), a["ports"]["top"]]})
        issues, _ = lint.lint_scene(scene)
        found = {i["code"] for i in issues}
        self.assertIn("edge-through-node", found)

    def test_must_fail_label_overlap_and_detached_arrow(self):
        scene = copy.deepcopy(check(base_spec())["scene"])
        edge = scene["edges"][0]
        target = next(n for n in scene["nodes"] if n["id"] == "a")
        edge["label"]["box"] = target["label_box"]     # put the edge label on top of a node label
        edge["points"][-1] = (edge["points"][-1][0], edge["points"][-1][1] - 15)
        found = {i["code"] for i in lint.lint_scene(scene)[0]}
        self.assertIn("label-overlap", found)
        self.assertIn("edge-detached", found)

    def test_must_fail_clip_and_overlapping_edges(self):
        scene = copy.deepcopy(check(base_spec())["scene"])
        scene["w"] -= 80
        scene["edges"][2]["points"] = [tuple(p) for p in scene["edges"][1]["points"]]
        found = {i["code"] for i in lint.lint_scene(scene)[0]}
        self.assertIn("clip", found)
        self.assertIn("edge-overlap", found)

    def test_must_fail_too_many_crossings(self):
        scene = copy.deepcopy(check(base_spec())["scene"])
        w, h = scene["w"], scene["h"]
        scene["nodes"] = []
        scene["groups"] = []
        scene["edges"] = []
        blank = {"arrow": "none", "emph": False, "dashed": False, "label": None, "badge": None, "no_room": False,
                 "sides": None, "from": "x", "to": "y"}
        for i in range(2):
            scene["edges"].append(dict(blank, index=i, points=[(10, 40 + 30 * i), (w - 10, 40 + 30 * i)]))
            scene["edges"].append(dict(blank, index=2 + i, points=[(60 + 40 * i, 10), (60 + 40 * i, h - 10)]))
        issues, stats = lint.lint_scene(scene)
        self.assertEqual(stats["crossings"], 4)
        self.assertIn("limit-crossings", {i["code"] for i in issues})

    def test_arrows_end_on_node_edges_and_are_orthogonal(self):
        scene = check(base_spec())["scene"]
        for edge in scene["edges"]:
            for (x1, y1), (x2, y2) in route.segments(edge["points"]):
                self.assertTrue(abs(x1 - x2) < 0.01 or abs(y1 - y2) < 0.01)

    def test_group_border_lanes_nest(self):
        spec = base_spec()
        spec["groups"].append({"id": "sub", "type": "subnet-private", "label": "Private", "in": "vpc", "cells": "A3:B3"})
        lay = layout_grid.layout(spec)
        vpc = next(g for g in lay["groups"] if g["id"] == "vpc")
        sub = next(g for g in lay["groups"] if g["id"] == "sub")
        self.assertAlmostEqual(sub["x"] - vpc["x"], S.GROUP_STEP)
        self.assertGreaterEqual(sub["y"] - vpc["y"], S.GROUP_BAND)


class RenderTests(unittest.TestCase):
    def test_deterministic_bytes(self):
        first = check(base_spec())
        second = check(copy.deepcopy(base_spec()))
        a = svg.render_standalone(first["scene"], first["spec"], FAKE_ICONS)
        b = svg.render_standalone(second["scene"], second["spec"], FAKE_ICONS)
        self.assertEqual(a.encode(), b.encode())
        self.assertEqual(svg.render_inline(first["scene"], first["spec"], FAKE_ICONS),
                         svg.render_inline(second["scene"], second["spec"], FAKE_ICONS))

    def test_standalone_is_self_contained(self):
        result = check(base_spec())
        text = svg.render_standalone(result["scene"], result["spec"], FAKE_ICONS)
        self.assertNotIn("var(", text)
        self.assertNotIn("<use", text)
        self.assertIn('class="dg-ground"', text)
        self.assertIn(FAKE_BODY, text)
        self.assertIn("<title>A test figure</title>", text)

    def test_inline_has_no_ids_no_literal_colours(self):
        result = check(base_spec())
        text = svg.render_inline(result["scene"], result["spec"], FAKE_ICONS)
        self.assertNotIn(" id=", text)
        self.assertNotIn("<style", text)
        self.assertNotRegex(text, r"#[0-9A-Fa-f]{6}")
        self.assertIn('href="#ic-alb"', text)
        self.assertIn('class="dg-id" href="#ic-users-dark"', text)
        css = svg.inline_css()
        self.assertIn("var(--dg-vpc)", css)
        self.assertNotRegex(css.replace("#fff", ""), r"#[0-9A-Fa-f]{6}")

    def test_group_types_have_distinct_border_styles(self):
        styles = {(width, dash, tint) for (_s, _t, width, dash, tint, _n) in S.GROUPS.values()}
        self.assertEqual(len(styles), len(S.GROUPS))

    def test_golden(self):
        spec = json.loads((FIX / "golden-three-tier.json").read_text(encoding="utf-8"))
        result = check(spec)
        self.assertEqual([i for i in result["issues"] if i["level"] == "error"], [])
        text = svg.render_standalone(result["scene"], result["spec"], FAKE_ICONS)
        golden = FIX / "golden-three-tier.svg"
        if not golden.exists():        # first run records the golden file; delete it to re-record
            golden.write_text(text, encoding="utf-8")
        self.assertEqual(text, golden.read_text(encoding="utf-8"),
                         "renderer output changed; if intended, delete the golden file and run again")


class TextMetricsTests(unittest.TestCase):
    def test_widths_are_real(self):
        self.assertAlmostEqual(textmetrics.text_width("W", 1000) / textmetrics.SAFETY, 944, delta=1)
        self.assertLess(textmetrics.text_width("iii", 13), textmetrics.text_width("WWW", 13))
        self.assertGreater(textmetrics.text_width("abc", 13, bold=True), textmetrics.text_width("abc", 13))

    def test_wrap(self):
        self.assertEqual(textmetrics.wrap("Application Load Balancer", 13, 126), ["Application Load", "Balancer"])
        self.assertEqual(textmetrics.wrap("a\nb", 13, 500), ["a", "b"])


class IconTests(unittest.TestCase):
    def test_clean_keeps_shapes_drops_ids(self):
        raw = ('<?xml version="1.0"?><!-- c --><svg width="48px" height="48px" viewBox="0 0 48 48"><title>x</title>'
               '<defs><linearGradient id="g1"/></defs><g id="Icon"><path id="p" fill="url(#g1)" d="M0 0"/></g></svg>')
        out = icons.clean_svg(raw, "ic-test")
        self.assertEqual(out["viewBox"], "0 0 48 48")
        self.assertIn('id="ic-test-g1"', out["body"])
        self.assertIn("url(#ic-test-g1)", out["body"])
        self.assertNotIn('id="Icon"', out["body"])
        self.assertNotIn("<title>", out["body"])
        self.assertIn('d="M0 0"', out["body"])

    def test_must_fail_download_from_other_host(self):
        with self.assertRaises(PermissionError):
            icons._get("https://example.com/icons.zip", icons.DOWNLOAD_HOST, binary=True)
        with self.assertRaises(PermissionError):
            icons._get("http://d1.awsstatic.com/icons.zip", icons.DOWNLOAD_HOST, binary=True)

    def test_sandbox_book_without_icons_reads_the_real_manifest(self):
        # W0 integration: `--book-dir <fixture copy>` has no diagrams/icons.json; every icon was "unknown".
        book = SANDBOX / "no-icons-book"
        real = SANDBOX / "real-book"
        common.write_json(real / "diagrams" / "icons.json", {"meta": {}, "icons": FAKE_ICONS})
        with mock.patch.object(common, "BOOK", book), mock.patch.object(common, "REAL_BOOK", real):
            self.assertEqual(set(icons.load()), set(FAKE_ICONS))
            common.write_json(book / "diagrams" / "icons.json", {"meta": {}, "icons": {"own": FAKE_ICONS["s3"]}})
            self.assertEqual(set(icons.load()), {"own"})
        shutil.rmtree(SANDBOX, ignore_errors=True)

    def test_find_zip_url(self):
        page = '<a href="https://d1.awsstatic.com/x/Icon-package_07312026.abc.zip">get</a> https://evil.example/Icon.zip'
        url, _ = icons.find_zip_url(page)
        self.assertEqual(url, "https://d1.awsstatic.com/x/Icon-package_07312026.abc.zip")
        self.assertEqual(icons.release_from_url(url), "2026-07-31")


class BuildTests(unittest.TestCase):
    def setUp(self):
        shutil.rmtree(SANDBOX, ignore_errors=True)
        self.src = SANDBOX / "diagrams" / "src"
        self.out = SANDBOX / "diagrams" / "svg"
        self.src.mkdir(parents=True)
        self.patches = [mock.patch.object(common, "DIAGRAM_SRC", self.src),
                        mock.patch.object(common, "DIAGRAM_SVG", self.out),
                        mock.patch.object(icons, "load", lambda: FAKE_ICONS)]
        for p in self.patches:
            p.start()

    def tearDown(self):
        for p in self.patches:
            p.stop()
        shutil.rmtree(SANDBOX, ignore_errors=True)

    def test_build_writes_svg(self):
        (self.src / "t-basic.json").write_text(json.dumps(base_spec()), encoding="utf-8")
        result = pipeline.build_one("t-basic")
        self.assertEqual(result["issues"], [])
        self.assertTrue((self.out / "t-basic.svg").is_file())

    def test_must_fail_build_writes_nothing_on_error(self):
        spec = base_spec()
        spec["id"] = "t-bad"
        spec["nodes"][3]["at"] = "A3"
        (self.src / "t-bad.json").write_text(json.dumps(spec), encoding="utf-8")
        result = pipeline.build_one("t-bad")
        self.assertTrue(any(i["level"] == "error" for i in result["issues"]))
        self.assertFalse((self.out / "t-bad.svg").exists())

    def test_must_fail_id_differs_from_file_name(self):
        (self.src / "other-name.json").write_text(json.dumps(base_spec()), encoding="utf-8")
        self.assertIn("id-mismatch", codes(pipeline.build_one("other-name")))

    def test_must_fail_shot_outside_the_book(self):
        with self.assertRaises(preview.PreviewError) as ctx:
            preview.shot_file("/etc/hosts", "aws-saa-book/_build/tmp/x.png")
        self.assertEqual(ctx.exception.code, common.EXIT_POLICY)


if __name__ == "__main__":
    unittest.main()
