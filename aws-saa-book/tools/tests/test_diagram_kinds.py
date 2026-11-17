"""Tests for the diagram kinds other than arch: sequence, ladder, states, timeline, compare, raw.

Run: python3 aws-saa-book/tools/tests/run.py diagram     (runs test_diagram.py and this file)

Nothing here touches real book data: specs are built in memory, icons are a small fake set, and
the tests that need files write them to a sandbox under _build/tmp/.
"""
import copy
import json
import shutil
import unittest
from unittest import mock

from saalib import common
from saalib.diagram import icons, layout_raw, pipeline, schema, shapes, svg
from saalib.diagram import style as S

SANDBOX = common.REAL_BOOK / "_build" / "tmp" / "test-diagram-kinds"

FAKE_BODY = '<rect width="48" height="48" fill="#8C4FFF"/>'
FAKE_ICONS = {name: {"viewBox": "0 0 48 48", "body": FAKE_BODY, "kind": "resource"}
              for name in ("user", "instance", "s3", "alb", "nlb", "db-instance")}
FAKE_ICONS["user"]["dark"] = '<rect width="48" height="48" fill="#FFFFFF"/>'

COMMON = {"title": "A test figure", "claim": "The request goes from the user to the server.",
          "alt": "A user sends a request to a server, and the server answers."}


def check(spec, base_dir=None):
    return pipeline.check_spec(spec, icons=FAKE_ICONS, base_dir=base_dir)


def codes(result, level="error"):
    return {i["code"] for i in result["issues"] if i["level"] == level}


def sequence_spec() -> dict:
    return dict(COMMON, id="t-seq", kind="sequence", size="s",
                actors=[{"id": "user", "icon": "user", "label": "User"},
                        {"id": "app", "label": "App server"},
                        {"id": "s3", "icon": "s3", "label": "Amazon S3"}],
                messages=[{"from": "user", "to": "app", "label": "Ask for file", "say": "The user asks for a file."},
                          {"from": "app", "to": "app", "label": "Sign URL", "say": "The app server signs a URL."},
                          {"from": "app", "to": "user", "label": "URL", "dashed": True, "say": "The app server returns the URL."},
                          {"from": "user", "to": "s3", "label": "GET", "emph": True, "say": "The user sends the request."}],
                asides=[{"after": 2, "over": "app", "text": "Signed locally"}])


def ladder_spec() -> dict:
    return dict(COMMON, id="t-ladder", kind="ladder", size="s",
                rungs=[{"q": "HTTP or HTTPS traffic?", "then": {"label": "Application Load Balancer", "icon": "alb", "emph": True}},
                       {"q": "TCP or UDP traffic?", "answer": "Yes", "next": "No", "then": {"label": "Network Load Balancer"}}],
                **{"else": {"label": "Read it again"}})


def states_spec() -> dict:
    return dict(COMMON, id="t-states", kind="states", size="s", cols=2, rows=2,
                states=[{"id": "pending", "label": "pending", "at": "A1"},
                        {"id": "running", "label": "running", "at": "B1", "emph": True},
                        {"id": "gone", "label": "terminated", "at": "B2", "final": True}],
                transitions=[{"from": "pending", "to": "running", "label": "ready"},
                             {"from": "running", "to": "gone", "label": "terminate"}])


def timeline_spec() -> dict:
    return dict(COMMON, id="t-timeline", kind="timeline", size="s", axis="Object age",
                ticks=[{"id": "d0", "label": "Day 0"}, {"id": "d30", "label": "Day 30"}, {"id": "d90", "label": "Day 90"}],
                lanes=[{"label": "Storage class", "spans": [{"from": "d0", "to": "d30", "label": "S3 Standard"},
                                                            {"from": "d30", "label": "S3 Glacier Deep Archive", "emph": True}]}],
                events=[{"at": "d90", "label": "Expires", "emph": True}])


def compare_spec() -> dict:
    def panel(label, edge_label):
        return {"label": label, "cols": 2, "rows": 2,
                "nodes": [{"id": "app", "icon": "instance", "label": "App server", "at": "A1"},
                          {"id": "db", "icon": "db-instance", "label": "Primary DB", "at": "A2"},
                          {"id": "other", "icon": "db-instance", "label": "Other DB", "at": "B2", "emph": True}],
                "edges": [{"from": "app", "to": "db", "label": "writes"},
                          {"from": "db", "to": "other", "label": edge_label}]}
    return dict(COMMON, id="t-compare", kind="compare", size="m",
                panels=[panel("Multi-AZ deployment", "sync copy"), panel("Read replica", "async copy")])


RAW_OK = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100">\n'
          '  <rect class="dg-nb" x="10" y="30" width="80" height="40" rx="4"/>\n'
          '  <text class="dg-nl" x="50" y="55">Left part</text>\n'
          '  <use href="#ic-user" x="120" y="26" width="48" height="48"/>\n'
          '  <g transform="translate(0 4)"><line class="dg-ax" x1="10" y1="84" x2="190" y2="84"/></g>\n'
          '</svg>\n')


def raw_spec() -> dict:
    return dict(COMMON, id="t-raw", kind="raw", size="s")


class RawCase(unittest.TestCase):
    def setUp(self):
        shutil.rmtree(SANDBOX, ignore_errors=True)
        SANDBOX.mkdir(parents=True)

    def tearDown(self):
        shutil.rmtree(SANDBOX, ignore_errors=True)

    def raw(self, text, spec=None):
        (SANDBOX / "t-raw.svg").write_text(text, encoding="utf-8")
        return check(spec or raw_spec(), SANDBOX)


class SchemaTests(unittest.TestCase):
    def test_every_kind_has_a_branch_and_a_builder(self):
        pipeline._discover()
        kinds = schema.load_schema()["properties"]["kind"]["enum"]
        self.assertEqual(sorted(kinds), sorted(pipeline.KINDS))

    def test_valid_specs_pass(self):
        for spec in (sequence_spec(), ladder_spec(), states_spec(), timeline_spec(), compare_spec(), raw_spec()):
            self.assertEqual(schema.validate(spec), [], spec["kind"])

    def test_must_fail_fields_of_another_kind(self):
        spec = sequence_spec()
        spec["nodes"] = []                         # an arch field
        self.assertTrue(any("unknown property 'nodes'" in e for e in schema.validate(spec)))

    def test_must_fail_missing_required_parts(self):
        spec = sequence_spec()
        del spec["messages"][0]["say"]
        self.assertIn("schema", codes(check(spec)))
        spec = ladder_spec()
        del spec["else"]
        self.assertIn("schema", codes(check(spec)))
        spec = states_spec()
        del spec["transitions"][0]["label"]
        self.assertIn("schema", codes(check(spec)))
        spec = timeline_spec()
        spec["ticks"] = spec["ticks"][:1]
        self.assertIn("schema", codes(check(spec)))
        spec = raw_spec()
        spec["svg"] = "../outside.svg"             # the file must sit next to the spec
        self.assertIn("schema", codes(check(spec)))


class SequenceTests(unittest.TestCase):
    def test_clean_and_numbered(self):
        result = check(sequence_spec())
        self.assertEqual(result["issues"], [])
        scene = result["scene"]
        self.assertEqual([e["badge"]["n"] for e in scene["edges"]], [1, 2, 3, 4])
        self.assertEqual([n for n, _say in pipeline.caption(sequence_spec())["steps"]], [1, 2, 3, 4])

    def test_messages_end_on_lifelines(self):
        scene = check(sequence_spec())["scene"]
        xs = scene["lifelines"]
        for edge in scene["edges"]:
            self.assertIn(edge["points"][0][0], xs)
            self.assertIn(edge["points"][-1][0], xs)
        lines = [d for d in scene["decor"] if d["cls"] == "dg-ll"]
        self.assertEqual(sorted(d["x1"] for d in lines), sorted(xs))

    def test_gap_grows_for_a_long_label(self):
        short = check(sequence_spec())["scene"]
        spec = sequence_spec()
        spec["messages"][0]["label"] = "GenerateDataKeyPair request"
        long = check(spec)
        self.assertEqual(codes(long), set())
        self.assertGreater(long["scene"]["lifelines"][1] - long["scene"]["lifelines"][0],
                           short["lifelines"][1] - short["lifelines"][0])

    def test_must_fail_six_actors(self):
        spec = sequence_spec()
        for i in range(3):
            spec["actors"].append({"id": f"x{i}", "label": "Extra"})
            spec["messages"].append({"from": "user", "to": f"x{i}", "label": "call", "say": "The user calls it."})
        self.assertIn("limit-actors", codes(check(spec)))

    def test_must_fail_too_many_messages(self):
        spec = sequence_spec()
        spec["messages"] = [dict(spec["messages"][0]) for _ in range(11)]
        self.assertIn("limit-messages", codes(check(spec)))

    def test_must_fail_unknown_actor_and_sentence_label(self):
        spec = sequence_spec()
        spec["messages"][0]["to"] = "ghost"
        spec["messages"][1]["label"] = "The server signs the URL now."
        result = check(spec)
        self.assertIn("ref-unknown", codes(result))
        self.assertIn("sentence", codes(result))
        self.assertIsNone(result["scene"])

    def test_must_fail_aside_and_say_rules(self):
        spec = sequence_spec()
        spec["asides"][0]["after"] = 9
        spec["messages"][0]["say"] = "First sentence. Second sentence."
        spec["actors"].append({"id": "idle", "label": "Idle"})
        found = codes(check(spec))
        self.assertIn("aside-after", found)
        self.assertIn("say", found)
        self.assertIn("actor-unused", found)


class LadderTests(unittest.TestCase):
    def test_clean_spine_and_branches(self):
        result = check(ladder_spec())
        self.assertEqual(result["issues"], [])
        scene = result["scene"]
        by_id = {n["id"]: n for n in scene["nodes"]}
        self.assertEqual(by_id["q1"]["cx"], by_id["q2"]["cx"])          # one spine
        self.assertEqual(by_id["q1"]["cx"], by_id["else"]["cx"])
        self.assertGreater(by_id["a1"]["bbox"][0], by_id["q1"]["bbox"][0] + by_id["q1"]["bbox"][2])   # answers go right
        self.assertEqual(sorted(e["label"]["text"] for e in scene["edges"]), ["No", "No", "Yes", "Yes"])

    def test_must_fail_seven_rungs(self):
        spec = ladder_spec()
        spec["rungs"] = [copy.deepcopy(spec["rungs"][1]) for _ in range(7)]
        self.assertIn("limit-rungs", codes(check(spec)))

    def test_must_fail_long_question_unknown_icon_equal_answers(self):
        spec = ladder_spec()
        spec["rungs"][0]["q"] = "Does the traffic that arrives at the application use HTTP or HTTPS?"
        spec["rungs"][0]["then"]["icon"] = "no-such-icon"
        spec["rungs"][1]["next"] = "yes"
        found = codes(check(spec))
        self.assertIn("sentence", found)
        self.assertIn("icon-unknown", found)
        self.assertIn("answers-equal", found)

    def test_must_fail_word_too_long_for_the_box(self):
        spec = ladder_spec()
        spec["rungs"][0]["q"] = "Supercalifragilisticexpialidocious traffic?"
        self.assertIn("text-overflow", codes(check(spec)))


class StatesTests(unittest.TestCase):
    def test_clean_pills_and_final_state(self):
        result = check(states_spec())
        self.assertEqual(result["issues"], [])
        by_id = {n["id"]: n for n in result["scene"]["nodes"]}
        self.assertTrue(all(n["rx"] == n["bbox"][3] / 2 for n in by_id.values()))
        self.assertTrue(by_id["gone"]["inner"])
        text = svg.render_standalone(result["scene"], result["spec"], FAKE_ICONS)
        self.assertEqual(text.count('class="dg-nf"'), 1)
        self.assertEqual(text.count('class="dg-sp"'), 1)

    def test_must_fail_too_many_states(self):
        spec = states_spec()
        spec["cols"], spec["rows"] = 3, 3
        spec["states"] = [{"id": f"s{i}", "label": "state", "at": f"{'ABC'[i % 3]}{i // 3 + 1}"} for i in range(9)]
        spec["transitions"] = [{"from": f"s{i}", "to": f"s{i + 1}", "label": "next"} for i in range(8)]
        self.assertIn("limit-states", codes(check(spec)))

    def test_must_fail_unlinked_state_and_leaving_a_final_state(self):
        spec = states_spec()
        spec["states"].append({"id": "lost", "label": "lost", "at": "A2"})
        spec["transitions"].append({"from": "gone", "to": "pending", "label": "again"})
        found = codes(check(spec))
        self.assertIn("state-unlinked", found)
        self.assertIn("final-leaves", found)

    def test_must_fail_unknown_state_and_two_states_in_one_cell(self):
        spec = states_spec()
        spec["transitions"][0]["to"] = "ghost"
        self.assertIn("ref-unknown", codes(check(spec)))
        spec = states_spec()
        spec["states"][1]["at"] = "A1"
        self.assertIn("node-overlap", codes(check(spec)))


class TimelineTests(unittest.TestCase):
    def test_clean_and_ordered(self):
        result = check(timeline_spec())
        self.assertEqual(result["issues"], [])
        scene = result["scene"]
        xs = scene["ticks_x"]
        self.assertEqual(xs, sorted(xs))
        first, second = scene["nodes"]
        self.assertLess(first["bbox"][0] + first["bbox"][2], second["bbox"][0])
        self.assertGreater(second["bbox"][0] + second["bbox"][2], xs[-1])     # an open span runs past the last tick

    def test_column_grows_for_a_long_label(self):
        spec = timeline_spec()
        narrow = check(spec)["scene"]["ticks_x"]
        spec["lanes"][0]["spans"][0]["label"] = "S3 Glacier Instant Retrieval"
        wide = check(spec)
        self.assertEqual(codes(wide), set())
        self.assertGreater(wide["scene"]["ticks_x"][1] - wide["scene"]["ticks_x"][0], narrow[1] - narrow[0])

    def test_must_fail_overlap_order_and_unknown_tick(self):
        spec = timeline_spec()
        spec["lanes"][0]["spans"].append({"from": "d0", "to": "d90", "label": "Overlap"})
        self.assertIn("span-overlap", codes(check(spec)))
        spec = timeline_spec()
        spec["lanes"][0]["spans"][0].update({"from": "d30", "to": "d0"})
        self.assertIn("span-order", codes(check(spec)))
        spec = timeline_spec()
        spec["events"][0]["at"] = "d999"
        result = check(spec)
        self.assertIn("ref-unknown", codes(result))
        self.assertIsNone(result["scene"])

    def test_must_fail_limits(self):
        spec = timeline_spec()
        spec["ticks"] = [{"id": f"t{i}", "label": f"Day {i}"} for i in range(8)]
        spec["lanes"] = [{"label": "Lane", "spans": [{"from": "t0", "to": "t1", "label": "One"}]} for _ in range(5)]
        spec["events"] = []
        found = codes(check(spec))
        self.assertIn("limit-ticks", found)
        self.assertIn("limit-lanes", found)

    def test_must_fail_label_that_cannot_fit(self):
        spec = timeline_spec()
        spec["lanes"][0]["spans"][0]["label"] = "W" * 24
        self.assertIn("text-overflow", codes(check(spec)))

    def test_must_fail_event_line_through_a_lane_label(self):
        spec = timeline_spec()
        spec["lanes"][0]["label"] = "Storage class of the object"
        spec["events"][0]["at"] = "d30"
        self.assertIn("event-on-label", codes(check(spec)))


class CompareTests(unittest.TestCase):
    def test_clean_panels(self):
        result = check(compare_spec())
        self.assertEqual(result["issues"], [])
        scene = result["scene"]
        self.assertEqual(len(scene["panels"]), 2)
        self.assertLess(scene["panels"][0]["x"] + scene["panels"][0]["scene"]["w"], scene["panels"][1]["x"])
        self.assertEqual(result["stats"]["nodes"], 6)
        self.assertEqual(scene["phone_w"], max(p["scene"]["w"] for p in scene["panels"]))

    def test_highlight_ring_stays_inside_each_panel(self):
        for panel in check(compare_spec())["scene"]["panels"]:
            sub = panel["scene"]
            for node in sub["nodes"]:
                if node["emph"]:
                    x, y, w, h = node["bbox"]
                    self.assertGreaterEqual(x - 7, 0)
                    self.assertLessEqual(x + w + 7, sub["w"])
                    self.assertLessEqual(y + h + 7, sub["h"])

    def test_inline_is_a_wrapper_with_one_svg_per_panel(self):
        result = check(compare_spec())
        text = svg.render_inline(result["scene"], result["spec"], FAKE_ICONS)
        self.assertTrue(text.startswith('<div class="dg-cmp"'))
        self.assertEqual(text.count("<svg "), 2)
        self.assertEqual(text.count('class="dg-cmp-h"'), 2)
        self.assertNotIn(" id=", text)
        self.assertNotRegex(text, r"#[0-9A-Fa-f]{6}")

    def test_must_fail_panel_count(self):
        spec = compare_spec()
        spec["panels"] = spec["panels"][:1]
        self.assertIn("limit-panels", codes(check(spec)))
        spec = compare_spec()
        spec["panels"] = spec["panels"] * 2
        self.assertIn("limit-panels", codes(check(spec)))

    def test_must_fail_big_panel_steps_and_bad_reference(self):
        spec = compare_spec()
        spec["panels"][0]["cols"], spec["panels"][0]["rows"] = 4, 2
        spec["panels"][0]["nodes"] = [{"id": f"n{i}", "label": "Node", "at": f"{'ABCD'[i % 4]}{i // 4 + 1}"} for i in range(7)]
        spec["panels"][0]["edges"] = [{"from": "n0", "to": "n1", "step": 1, "say": "The first node calls the second."}]
        spec["panels"][1]["edges"][0]["to"] = "ghost"
        result = check(spec)
        found = codes(result)
        self.assertIn("limit-nodes", found)
        self.assertIn("compare-step", found)
        self.assertIn("ref-unknown", found)
        self.assertTrue(any(i["msg"].startswith("panel 2: ") for i in result["issues"]))

    def test_must_fail_geometry_inside_a_panel(self):
        spec = compare_spec()
        spec["panels"][1]["nodes"][2]["at"] = "A2"
        result = check(spec)
        self.assertIn("node-overlap", codes(result))
        self.assertTrue(any(i["msg"].startswith("panel 2: ") for i in result["issues"]))


class RawTests(RawCase):
    def test_clean(self):
        result = self.raw(RAW_OK)
        self.assertEqual(result["issues"], [])
        self.assertEqual((result["scene"]["w"], result["scene"]["h"]), (200, 100))
        alone = svg.render_standalone(result["scene"], result["spec"], FAKE_ICONS)
        self.assertIn(FAKE_BODY, alone)                 # the icon is embedded
        self.assertNotIn("<use", alone)
        self.assertIn(">Left part</text>", alone)
        inline = svg.render_inline(result["scene"], result["spec"], FAKE_ICONS)
        self.assertIn('href="#ic-user-dark"', inline)   # both icon variants, switched by the theme
        self.assertNotIn(" id=", inline)

    def test_must_fail_literal_colour_and_style(self):
        result = self.raw(RAW_OK.replace('class="dg-nb"', 'class="dg-nb" fill="#ff0000" style="opacity:.5"'))
        self.assertIn("raw-colour", codes(result))
        self.assertNotIn("#ff0000", svg.render_inline(result["scene"], result["spec"], FAKE_ICONS))

    def test_must_fail_unknown_class_and_missing_class(self):
        self.assertIn("raw-class", codes(self.raw(RAW_OK.replace("dg-nb", "my-box"))))
        self.assertIn("raw-class", codes(self.raw(RAW_OK.replace(' class="dg-nl"', ""))))

    def test_must_fail_script_style_and_id(self):
        result = self.raw(RAW_OK.replace("</svg>", "<script>alert(1)</script><style>.x{}</style></svg>"))
        self.assertIn("raw-element", codes(result))
        self.assertNotIn("alert", svg.render_inline(result["scene"], result["spec"], FAKE_ICONS))
        self.assertIn("raw-attr", codes(self.raw(RAW_OK.replace("<rect ", '<rect id="a" onclick="x()" '))))

    def test_must_fail_rotation_and_foreign_use(self):
        self.assertIn("raw-transform", codes(self.raw(RAW_OK.replace("translate(0 4)", "rotate(90)"))))
        self.assertIn("raw-use", codes(self.raw(RAW_OK.replace("#ic-user", "https://example.com/x.svg#a"))))
        self.assertIn("icon-unknown", codes(self.raw(RAW_OK.replace("#ic-user", "#ic-ghost"))))

    def test_must_fail_size_and_clip(self):
        self.assertIn("raw-size", codes(self.raw(RAW_OK.replace("0 0 200 100", "0 0 1200 100"))))
        self.assertIn("clip", codes(self.raw(RAW_OK.replace('x="10" y="30"', 'x="150" y="30"'))))
        self.assertIn("size-budget", codes(self.raw(RAW_OK.replace("0 0 200 100", "0 0 600 100")), "warn"))

    def test_must_fail_unusable_file(self):
        result = check(raw_spec(), SANDBOX)             # no file
        self.assertIn("ref-missing", codes(result))
        self.assertIsNone(result["scene"])
        self.assertIn("ref-xml", codes(self.raw("<svg><rect></svg>")))
        self.assertIn("ref-xml", codes(self.raw('<!DOCTYPE svg [<!ENTITY a "b">]>' + RAW_OK)))
        self.assertIn("ref-root", codes(self.raw(RAW_OK.replace(' viewBox="0 0 200 100"', ""))))

    def test_must_fail_sentence_in_text(self):
        result = self.raw(RAW_OK.replace("Left part", "This is the left part of the whole block"))
        self.assertIn("sentence", codes(result))

    def test_known_classes_come_from_the_stylesheet(self):
        known = svg.known_classes()
        for name in ("dg-e", "dg-nb", "dg-nl", "dg-ll", "dg-sp", "dg-ax", "dg-mt", "dg-g-vpc"):
            self.assertIn(name, known)
        self.assertNotIn("my-box", known)


class RenderTests(unittest.TestCase):
    SPECS = (sequence_spec, ladder_spec, states_spec, timeline_spec, compare_spec)

    def test_deterministic_and_theme_safe(self):
        for make in self.SPECS:
            first, second = check(make()), check(copy.deepcopy(make()))
            a = svg.render_standalone(first["scene"], first["spec"], FAKE_ICONS)
            self.assertEqual(a, svg.render_standalone(second["scene"], second["spec"], FAKE_ICONS), make.__name__)
            self.assertNotIn("var(", a)
            self.assertNotIn("<use", a)
            inline = svg.render_inline(first["scene"], first["spec"], FAKE_ICONS)
            self.assertNotIn(" id=", inline)
            self.assertNotIn("<style", inline)
            self.assertNotRegex(inline, r"#[0-9A-Fa-f]{6}")

    def test_every_class_in_the_output_is_defined(self):
        import re
        known = svg.known_classes() | {"dg-cmp", "dg-cmp-p", "dg-cmp-h"}
        for make in self.SPECS:
            result = check(make())
            text = svg.render_inline(result["scene"], result["spec"], FAKE_ICONS)
            for value in re.findall(r'class="([^"]+)"', text):
                for name in value.split():
                    self.assertTrue(name in known or name == f"dg-{result['spec']['kind']}" or name == "dg-arch",
                                    f"{make.__name__}: class {name!r} is not in the stylesheet")

    def test_arch_files_do_not_carry_the_extra_classes(self):
        self.assertNotIn(".dg-ll", svg.standalone_css())
        self.assertIn(".dg-ll", svg.standalone_css("sequence"))
        self.assertIn(".dg-cmp", svg.inline_css())

    def test_make_room_for_rings_moves_everything_together(self):
        scene = check(compare_spec())["scene"]["panels"][0]["scene"]
        node = next(n for n in scene["nodes"] if n["emph"])
        self.assertEqual(node["icon_box"][0] + S.ICON / 2, node["lines"][0]["x"])
        before = (scene["w"], scene["h"])
        shapes.make_room_for_rings(scene)                  # a second call changes nothing
        self.assertEqual(before, (scene["w"], scene["h"]))


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

    def write(self, spec):
        (self.src / f"{spec['id']}.json").write_text(json.dumps(spec), encoding="utf-8")

    def test_compare_writes_the_row_and_one_file_per_panel(self):
        self.write(compare_spec())
        result = pipeline.build_one("t-compare")
        self.assertEqual(result["issues"], [])
        self.assertEqual(sorted(p.name for p in self.out.iterdir()),
                         ["t-compare.p1.svg", "t-compare.p2.svg", "t-compare.svg"])
        panel = (self.out / "t-compare.p2.svg").read_text(encoding="utf-8")
        self.assertIn("<title>A test figure: Read replica</title>", panel)
        self.assertEqual((self.out / "t-compare.svg").read_text(encoding="utf-8").count('class="dg-ph"'), 2)

    def test_raw_is_read_next_to_the_spec(self):
        self.write(raw_spec())
        (self.src / "t-raw.svg").write_text(RAW_OK, encoding="utf-8")
        result = pipeline.build_one("t-raw")
        self.assertEqual(result["issues"], [])
        self.assertTrue((self.out / "t-raw.svg").is_file())
        self.assertEqual(pipeline.all_ids(), ["t-raw"])    # the .svg source is not a diagram id

    def test_must_fail_build_writes_nothing_on_error(self):
        spec = sequence_spec()
        spec["messages"][0]["to"] = "ghost"
        self.write(spec)
        self.write(raw_spec())
        (self.src / "t-raw.svg").write_text(RAW_OK.replace("dg-nb", "my-box"), encoding="utf-8")
        for ident in ("t-seq", "t-raw"):
            result = pipeline.build_one(ident)
            self.assertTrue(any(i["level"] == "error" for i in result["issues"]))
        self.assertFalse(self.out.exists() and any(self.out.iterdir()))

    def test_samples_in_the_book_are_clean(self):
        for p in self.patches:                             # this one test reads the real specs (read only)
            p.stop()
        try:
            real = icons.load()
            for path in sorted(common.DIAGRAM_SRC.glob("sample-*.json")):
                result = pipeline.check_spec(common.read_json(path), path.stem, real, path.parent)
                self.assertEqual([i for i in result["issues"] if i["level"] == "error"], [], path.name)
        finally:
            for p in self.patches:
                p.start()


if __name__ == "__main__":
    unittest.main()
