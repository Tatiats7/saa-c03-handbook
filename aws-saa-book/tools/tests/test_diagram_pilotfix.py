"""Tests for the renderer defects found by the diagram pilot gate (2026-10-04).

Run: python3 aws-saa-book/tools/tests/run.py diagram_pilotfix

Specs are built in memory and the icons are a fake set; nothing here reads or writes book data.
"""
import copy
import unittest

from saalib.diagram import lint, pipeline, route, schema
from saalib.diagram import layout_timeline
from saalib.diagram import style as S

FAKE_BODY = '<rect width="48" height="48" fill="#8C4FFF"/>'
FAKE_ICONS = {name: {"viewBox": "0 0 48 48", "body": FAKE_BODY, "kind": "resource"}
              for name in ("users", "alb", "instance", "nat-gateway", "internet-gateway", "internet", "s3", "user")}


def check(spec):
    return pipeline.check_spec(spec, icons=FAKE_ICONS)


def errors(result):
    return [i for i in result["issues"] if i["level"] == "error"]


def fan_out_spec() -> dict:
    return {
        "id": "t-fan", "kind": "arch", "size": "s", "title": "A test figure",
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


def two_az_spec() -> dict:
    """Two columns with VPC, Availability Zone and subnet borders: the widest common figure."""
    groups = [{"id": "vpc", "type": "vpc", "label": "VPC", "cells": "A1:B3"}]
    nodes = [{"id": "igw", "icon": "internet-gateway", "label": "Internet gateway", "at": "A3:B3"},
             {"id": "internet", "icon": "internet", "label": "Internet", "at": "A4:B4"}]
    edges = []
    for n, col in ((1, "A"), (2, "B")):
        groups += [
            {"id": f"az{n}", "type": "az", "label": f"Availability Zone {col}", "in": "vpc", "cells": f"{col}1:{col}2"},
            {"id": f"priv{n}", "type": "subnet-private", "label": "Private subnet", "in": f"az{n}", "cells": f"{col}1"},
            {"id": f"pub{n}", "type": "subnet-public", "label": "Public subnet", "in": f"az{n}", "cells": f"{col}2"},
        ]
        nodes += [{"id": f"app{n}", "icon": "instance", "label": "EC2 instance", "at": f"{col}1"},
                  {"id": f"nat{n}", "icon": "nat-gateway", "label": "NAT gateway", "at": f"{col}2"}]
        edges += [{"from": f"app{n}", "to": f"nat{n}", "step": 1, "say": "The instance sends traffic to the NAT gateway."},
                  {"from": f"nat{n}", "to": "igw", "step": 2, "say": "The NAT gateway forwards the traffic."}]
    edges.append({"from": "igw", "to": "internet", "step": 3, "say": "The internet gateway connects to the internet."})
    return {"id": "t-two-az", "kind": "arch", "size": "s", "title": "Two Availability Zones",
            "claim": "Each instance uses the NAT gateway in its own Availability Zone.",
            "alt": "Two Availability Zones, each with an instance and a NAT gateway.",
            "cols": 2, "rows": 4, "groups": groups, "nodes": nodes, "edges": edges}


class TrunkTests(unittest.TestCase):
    """Defects 3 and 4: edges of one step that share a node are one trunk with one badge."""

    def test_fan_out_is_one_trunk_with_one_badge(self):
        result = check(fan_out_spec())
        self.assertEqual(errors(result), [])
        e1, e2 = result["scene"]["edges"][1], result["scene"]["edges"][2]
        self.assertEqual(e1["points"][0], e2["points"][0], "both edges leave the load balancer at one port")
        self.assertEqual(e1["points"][1], e2["points"][1], "and share the first stretch")
        self.assertEqual(sum(1 for e in (e1, e2) if e["badge"]), 1, "one badge for the step")

    def test_share_keys_need_same_step_and_style(self):
        edges = [{"from": "x", "to": "a", "step": 1}, {"from": "x", "to": "b", "step": 1},
                 {"from": "x", "to": "c", "step": 2}, {"from": "x", "to": "d", "step": 1, "dashed": True},
                 {"from": "x", "to": "e"}]
        keys = route.share_keys(edges)
        self.assertTrue(route.keys_mate(keys[0], keys[1]))
        for other in (2, 3, 4):
            self.assertFalse(route.keys_mate(keys[0], keys[other]))

    def test_must_fail_trunk_edges_on_top_of_each_other(self):
        scene = copy.deepcopy(check(fan_out_spec())["scene"])
        scene["edges"][2]["points"] = [tuple(p) for p in scene["edges"][1]["points"]]
        found = {i["code"] for i in lint.lint_scene(scene)[0]}
        self.assertIn("edge-overlap", found)

    def test_must_fail_other_step_on_the_trunk(self):
        scene = copy.deepcopy(check(fan_out_spec())["scene"])
        scene["edges"][2]["step"] = 3          # no longer the same step: the shared stretch is an overlap
        found = {i["code"] for i in lint.lint_scene(scene)[0]}
        self.assertIn("edge-overlap", found)

    def test_must_fail_step_without_badge(self):
        scene = copy.deepcopy(check(fan_out_spec())["scene"])
        for e in scene["edges"][1:]:
            e["badge"] = None
        found = {i["code"] for i in lint.lint_scene(scene)[0]}
        self.assertIn("step-badge-missing", found)


class TrackTests(unittest.TestCase):
    """Defect 2: edges of different steps do not follow each other closely on one gutter track."""

    def test_gap_between_steps(self):
        self.assertEqual(route._track_gap(3, 5), S.TRACK_STEP_GAP)
        self.assertGreater(S.TRACK_STEP_GAP, route._track_gap(3, 3))
        self.assertEqual(route._track_gap(None, 5), route._track_gap(3, 3))


class PhoneWidthTests(unittest.TestCase):
    """Defects 1, 6 and 7: a two-AZ figure fits a phone at scale 0.85, labels stay at the left."""

    def test_two_az_figure_reaches_phone_scale(self):
        result = check(two_az_spec())
        self.assertEqual(result["issues"], [])
        scene = result["scene"]
        self.assertEqual(scene["cell_w"], S.CELL_W, "the columns were not widened for a group label")
        self.assertGreaterEqual(S.PHONE_FIT / scene["w"], S.PHONE_SCALE)
        self.assertEqual({g["label_anchor"] for g in scene["groups"]}, {"start"})

    def test_arrow_moves_beside_the_label_but_stays_on_the_icon(self):
        scene = check(two_az_spec())["scene"]
        nodes = {n["id"]: n for n in scene["nodes"]}
        edge = scene["edges"][0]                      # app1 to nat1, enters through "Public subnet"
        x = edge["points"][-1][0]
        icon = nodes["nat1"]["icon_box"]
        self.assertGreater(x, nodes["nat1"]["cx"])
        self.assertLess(x, icon[0] + icon[2])
        label = next(g for g in scene["groups"] if g["id"] == "pub1")["label_box"]
        self.assertGreaterEqual(x, label[0] + label[2] + S.GROUP_LABEL_CLEAR)

    def test_must_fail_wider_than_the_phone_budget(self):
        scene = copy.deepcopy(check(two_az_spec())["scene"])
        scene["w"] = int(S.PHONE_FIT / S.PHONE_SCALE) + 2
        found = {i["code"] for i in lint.lint_scene(scene, "s")[0]}
        self.assertIn("size-budget", found)

    def test_must_fail_edge_through_group_label(self):
        scene = copy.deepcopy(check(two_az_spec())["scene"])
        box = next(g for g in scene["groups"] if g["id"] == "pub1")["label_box"]
        edge = scene["edges"][0]
        x = box[0] + box[2] / 2
        edge["points"] = [(x, p[1]) for p in edge["points"]]
        found = {i["code"] for i in lint.lint_scene(scene)[0]}
        self.assertIn("edge-on-label", found)


class HighlightTests(unittest.TestCase):
    """Defect 5: a highlighted icon node keeps its ring inside the canvas and clear of arrowheads."""

    def spec(self):
        spec = fan_out_spec()
        spec["nodes"][0]["emph"] = True      # first row: the old ring was cut off by the canvas
        spec["nodes"][1]["emph"] = True      # arrows end on this node
        return spec

    def test_ring_is_inside_and_arrows_stop_at_it(self):
        result = check(self.spec())
        self.assertEqual(errors(result), [])
        scene = result["scene"]
        nodes = {n["id"]: n for n in scene["nodes"]}
        for ident in ("users", "alb"):
            ring = nodes[ident]["ring"]
            self.assertGreaterEqual(ring[0], 1)
            self.assertGreaterEqual(ring[1], 1)
        tip = scene["edges"][0]["points"][-1]         # users to alb, enters at the top
        self.assertLessEqual(tip[1], nodes["alb"]["ring"][1] - S.PORT_GAP + 0.01)

    def test_must_fail_arrow_into_the_ring(self):
        scene = copy.deepcopy(check(self.spec())["scene"])
        nodes = {n["id"]: n for n in scene["nodes"]}
        icon = nodes["alb"]["icon_box"]
        pts = scene["edges"][0]["points"]
        scene["edges"][0]["points"] = pts[:-1] + [(pts[-1][0], icon[1] + icon[3] / 2)]
        found = {i["code"] for i in lint.lint_scene(scene)[0]}
        self.assertIn("edge-through-node", found)


def timeline_spec() -> dict:
    return {"id": "t-time", "kind": "timeline", "size": "s", "title": "A timeline",
            "claim": "The object moves and then expires.", "alt": "A timeline with two spans and one event.",
            "axis": "Object age",
            "ticks": [{"id": "t0", "label": "Created"}, {"id": "t1", "label": "Later"}, {"id": "t2", "label": "Last day"}],
            "lanes": [{"label": "Class", "spans": [{"from": "t0", "to": "t1", "label": "First"},
                                                    {"from": "t1", "to": "t2", "label": "Second"}]}],
            "events": [{"at": "t2", "label": "Expiration", "emph": True}]}


class TimelineTests(unittest.TestCase):
    """Defect 8: an event line does not lie on the border of a span."""

    def test_bar_stops_before_the_event_line(self):
        result = check(timeline_spec())
        self.assertEqual(errors(result), [])
        scene = result["scene"]
        event_x = scene["ticks_x"][2]
        last = scene["nodes"][1]["box"]
        self.assertGreaterEqual(event_x - (last[0] + last[2]), layout_timeline.EVENT_INSET - 0.01)
        self.assertGreater(layout_timeline.EVENT_INSET, layout_timeline.BAR_INSET + 2)
        first = scene["nodes"][0]["box"]             # a tick without an event keeps the small inset
        self.assertAlmostEqual(scene["ticks_x"][1] - (first[0] + first[2]), layout_timeline.BAR_INSET, places=2)

    def test_must_fail_event_through_lane_label(self):
        spec = timeline_spec()
        spec["lanes"][0]["label"] = "A lane label that is long"
        spec["events"].append({"at": "t1", "label": "Transition"})
        found = {i["code"] for i in check(spec)["issues"] if i["level"] == "error"}
        self.assertIn("event-on-label", found)


def sequence_spec() -> dict:
    return {"id": "t-seq", "kind": "sequence", "size": "s", "title": "A sequence",
            "claim": "The user asks and the service answers.", "alt": "A user sends a request and gets a response.",
            "actors": [{"id": "u", "icon": "user", "label": "User"}, {"id": "s", "icon": "s3", "label": "Service"}],
            "messages": [{"from": "u", "to": "s", "label": "Request", "say": "The user sends a request."},
                         {"from": "s", "to": "u", "label": "Response", "dashed": True, "say": "The service answers."}],
            "asides": [{"after": 1, "over": "s", "text": "Checks the policy", "emph": True}]}


class SequenceTests(unittest.TestCase):
    """Defect 12 and the highlighted aside."""

    def test_badge_sits_on_the_sender_lifeline(self):
        result = check(sequence_spec())
        self.assertEqual(errors(result), [])
        scene = result["scene"]
        for edge in scene["edges"]:
            start = edge["points"][0][0]
            self.assertLessEqual(abs(edge["badge"]["cx"] - start) - S.BADGE_R, 1.01)

    def test_aside_can_be_highlighted(self):
        scene = check(sequence_spec())["scene"]
        aside = next(n for n in scene["nodes"] if n["id"] == "aside1")
        self.assertTrue(aside["emph"] and aside["emph_fill"])

    def test_must_fail_aside_emph_not_boolean(self):
        spec = sequence_spec()
        spec["asides"][0]["emph"] = "yes"
        self.assertTrue(schema.validate(spec))
        self.assertIn("schema", {i["code"] for i in check(spec)["issues"]})


if __name__ == "__main__":
    unittest.main()
