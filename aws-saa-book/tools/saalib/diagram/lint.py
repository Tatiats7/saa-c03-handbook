"""Diagram lint: the limits of the style guide (lint_spec) and geometry (lint_scene).

Each issue is {"level": "error" | "warn", "code": str, "msg": str}. An error blocks the build.
"""
from __future__ import annotations

import re

from . import route
from . import style as S
from . import svg


def _issue(level: str, code: str, msg: str) -> dict:
    return {"level": level, "code": code, "msg": msg}


def _words(text: str) -> int:
    return len(text.replace("\n", " ").split())


# ------------------------------------------------------------------ limits

def lint_spec(spec: dict, icons: dict) -> list:
    """Checks that need no geometry. Codes starting with "ref-" make layout impossible."""
    issues = []
    nodes = spec.get("nodes", [])
    edges = spec.get("edges", [])
    groups = spec.get("groups", [])
    node_ids = [n["id"] for n in nodes]

    for ident in sorted({i for i in node_ids if node_ids.count(i) > 1}):
        issues.append(_issue("error", "ref-duplicate", f"node id {ident!r} is used more than once"))
    if len(nodes) > S.MAX_NODES:
        issues.append(_issue("error", "limit-nodes", f"{len(nodes)} nodes; the limit is {S.MAX_NODES}. Split the figure."))
    if len(edges) > S.MAX_EDGES:
        issues.append(_issue("error", "limit-edges", f"{len(edges)} edges; the limit is {S.MAX_EDGES}. Split the figure."))
    az = sum(1 for g in groups if g["type"] == "az")
    if az > S.MAX_AZ:
        issues.append(_issue("error", "limit-az", f"{az} Availability Zones drawn; the limit is {S.MAX_AZ}"))
    for gtype, word in (("region", "Region"), ("account", "account")):
        if sum(1 for g in groups if g["type"] == gtype) == 1:
            issues.append(_issue("error", f"lone-{gtype}",
                                 f"one {word} box: draw {word} boxes only when the figure compares two or more"))

    for n in nodes:
        label = n["label"]
        if _words(label) > S.MAX_LABEL_WORDS or re.search(r"[.!?]$", label.strip()):
            issues.append(_issue("error", "sentence", f"node {n['id']!r}: label {label!r} reads as a sentence "
                                 f"(at most {S.MAX_LABEL_WORDS} words, no full stop)"))
        if n.get("icon") and n["icon"] not in icons:
            issues.append(_issue("error", "icon-unknown", f"node {n['id']!r}: no icon named {n['icon']!r} "
                                 f"(see: diagram icons --list)"))
    for g in groups:
        if _words(g["label"]) > 5 or re.search(r"[.!?]$", g["label"].strip()):
            issues.append(_issue("error", "sentence", f"group {g['id']!r}: label {g['label']!r} reads as a sentence"))

    steps = {}
    for i, e in enumerate(edges):
        name = f"edge {i + 1} ({e.get('from')} to {e.get('to')})"
        for end in ("from", "to"):
            if e[end] not in node_ids:
                issues.append(_issue("error", "ref-unknown", f"{name}: unknown node {e[end]!r}"))
        if e["from"] == e["to"]:
            issues.append(_issue("error", "ref-self", f"{name}: an edge cannot start and end on the same node"))
        if not e.get("label") and e.get("step") is None:
            issues.append(_issue("error", "edge-unlabelled", f"{name}: every arrow needs a label or a step number"))
        if e.get("label") and (_words(e["label"]) > S.MAX_EDGE_LABEL_WORDS or re.search(r"[.!?]$", e["label"].strip())):
            issues.append(_issue("error", "sentence", f"{name}: label {e['label']!r} reads as a sentence "
                                 f"(at most {S.MAX_EDGE_LABEL_WORDS} words)"))
        if e.get("say") and e.get("step") is None:
            issues.append(_issue("error", "say-without-step", f"{name}: \"say\" needs a \"step\""))
        if e.get("step") is not None:
            steps.setdefault(e["step"], []).append(e)
        if e.get("arrow") == "both":
            issues.append(_issue("warn", "two-headed", f"{name}: two-headed arrow. Use one head when it matters "
                                 f"who starts the connection."))
    if steps:
        expected = list(range(1, max(steps) + 1))
        if sorted(steps) != expected:
            issues.append(_issue("error", "steps-gap", f"step numbers {sorted(steps)} must run 1 to {max(steps)} without gaps"))
        for number in sorted(steps):
            says = [e["say"] for e in steps[number] if e.get("say")]
            if not says:
                issues.append(_issue("error", "step-without-say", f"step {number}: add \"say\" (one sentence for the list under the figure)"))
            elif len(set(says)) > 1:
                issues.append(_issue("error", "step-say-differs", f"step {number}: the edges of one step carry different \"say\" texts"))

    claim = spec.get("claim", "").strip()
    if claim and (not re.search(r"[.!?]$", claim) or re.search(r"[.!?][\"')]?\s+\S", claim)):     # gate-break 60
        issues.append(_issue("error", "claim", "the claim must be exactly one sentence ending with a full stop"))
    emph = sum(1 for e in edges if e.get("emph")) + sum(1 for n in nodes if n.get("emph"))
    if emph > S.MAX_EMPH:
        issues.append(_issue("warn", "emph-many", f"{emph} highlighted items; the highlight is for the one thing the figure is about"))
    return issues


def has_fatal(issues: list) -> bool:
    return any(i["code"].startswith("ref-") for i in issues)


# ------------------------------------------------------------------ geometry

def _dist_to_rect_edge(p, rect) -> float:
    """Distance from a point to the border of a rectangle (0 on the border)."""
    x, y = p
    rx, ry, rw, rh = rect
    dx = max(rx - x, 0, x - (rx + rw))
    dy = max(ry - y, 0, y - (ry + rh))
    if dx or dy:
        return max(dx, dy) if not (dx and dy) else (dx * dx + dy * dy) ** 0.5
    return min(x - rx, rx + rw - x, y - ry, ry + rh - y)


def _free_ends_apart(e1: dict, e2: dict) -> bool:
    """Two edges of one trunk may share a stretch, but they must part: the ends that are not on
    the shared node lie apart. Two edges on top of each other from end to end are an error."""
    def apart(p, q):
        return abs(p[0] - q[0]) + abs(p[1] - q[1]) >= 8
    a, b = e1["points"], e2["points"]
    if e1["from"] == e2["from"] and e1["to"] == e2["to"]:
        return False
    return apart(a[-1], b[-1]) if e1["from"] == e2["from"] else apart(a[0], b[0])


def lint_scene(scene: dict, size: str = "m") -> tuple:
    """Geometry checks on a finished scene. Returns (issues, stats)."""
    issues = []
    W, H = scene["w"], scene["h"]
    nodes = scene.get("nodes", [])
    groups = scene.get("groups", [])
    edges = scene.get("edges", [])
    by_id = {n["id"]: n for n in nodes}

    def outside(rect):
        return rect[0] < 0 or rect[1] < 0 or rect[0] + rect[2] > W or rect[1] + rect[3] > H

    # ---- text fits its node, node inside the canvas
    for item in scene.get("decor", []):
        if outside(svg.decor_box(item)):
            issues.append(_issue("error", "clip", f"a {item['t']} ({item['cls']}) is cut off by the canvas"))
    for n in nodes:
        max_lines = n.get("max_lines", S.NODE_MAX_LINES)
        if len(n.get("lines", [])) > max_lines:
            issues.append(_issue("error", "text-lines", f"node {n['id']!r}: label needs {len(n['lines'])} lines; "
                                 f"at most {max_lines} fit. Shorten it."))
        for line in n.get("lines", []):
            if line["w"] > n["max_text_w"] + 0.01:
                issues.append(_issue("error", "text-overflow", f"node {n['id']!r}: {line['text']!r} is {line['w']:.0f} wide; "
                                     f"{n['max_text_w']:.0f} fit. Shorten it or break it with \\n."))
        if outside(n["bbox"]):
            issues.append(_issue("error", "clip", f"node {n['id']!r} is cut off by the canvas"))
    for g in groups:
        if g["label_w"] + 2 * S.GROUP_LABEL_INSET > g["w"]:
            issues.append(_issue("error", "text-overflow", f"group {g['id']!r}: label {g['label']!r} is wider than the group"))
        if outside((g["x"], g["y"], g["w"], g["h"])):
            issues.append(_issue("error", "clip", f"group {g['id']!r} is cut off by the canvas"))

    # ---- nodes do not overlap
    for i, a in enumerate(nodes):
        for b in nodes[i + 1:]:
            if route.rects_overlap(a["bbox"], b["bbox"], 2):
                issues.append(_issue("error", "node-overlap", f"nodes {a['id']!r} and {b['id']!r} overlap"))

    # ---- labels do not overlap
    texts = []    # (owner key, description, box)
    for n in nodes:
        if n.get("label_box"):
            texts.append((("node", n["id"]), f"label of node {n['id']!r}", n["label_box"]))
    for g in groups:
        texts.append((("group", g["id"]), f"label of group {g['id']!r}", g["label_box"]))
    for e in edges:
        name = f"edge {e['index'] + 1}"
        if e.get("label"):
            texts.append((("edge", e["index"]), f"label of {name}", e["label"]["box"]))
        if e.get("badge"):
            b = e["badge"]
            texts.append((("edge", e["index"]), f"step badge of {name}",
                          (b["cx"] - S.BADGE_R, b["cy"] - S.BADGE_R, 2 * S.BADGE_R, 2 * S.BADGE_R)))
    for t in scene.get("texts", []):
        if t.get("box"):
            texts.append((("text", id(t)), f"text {t['text']!r}", t["box"]))
    for i, (owner_a, name_a, box_a) in enumerate(texts):
        if outside(box_a):
            issues.append(_issue("error", "clip", f"{name_a} is cut off by the canvas"))
        for owner_b, name_b, box_b in texts[i + 1:]:
            if owner_a != owner_b and route.rects_overlap(box_a, box_b, 1):
                issues.append(_issue("error", "label-overlap", f"{name_a} overlaps {name_b}"))
        for n in nodes:
            if owner_a == ("node", n["id"]):
                continue
            if any(route.rects_overlap(box_a, r, 1) for r in n["shapes"]):
                issues.append(_issue("error", "label-on-node", f"{name_a} overlaps node {n['id']!r}"))
        if owner_a[0] == "edge":
            for g in groups:
                rect = (g["x"], g["y"], g["w"], g["h"])
                inside = (box_a[0] > rect[0] and box_a[1] > rect[1] and box_a[0] + box_a[2] < rect[0] + rect[2]
                          and box_a[1] + box_a[3] < rect[1] + rect[3])
                if route.rects_overlap(box_a, rect) and not inside:
                    issues.append(_issue("warn", "label-on-border", f"{name_a} sits on the border of group {g['id']!r}"))

    # ---- edges
    keys = route.share_keys(edges) if all("from" in e and "to" in e for e in edges) else [(None, None)] * len(edges)
    mate_of = {e["index"]: {o["index"] for j, o in enumerate(edges) if j != i and route.keys_mate(keys[i], keys[j])}
               for i, e in enumerate(edges)}
    for e in edges:
        # a step whose edges form a trunk shows its number once; an edge with no number is an error
        if e.get("step") is not None and not e.get("badge") and e.get("points") and "from" in e:
            if not any(o.get("badge") for o in edges if o["index"] in mate_of[e["index"]]):
                issues.append(_issue("error", "step-badge-missing",
                                     f"edge {e['index'] + 1} ({e['from']} to {e['to']}): step {e['step']} has no badge"))
    crossings = 0
    for e in edges:
        name = f"edge {e['index'] + 1} ({e['from']} to {e['to']})"
        pts = e.get("points")
        if not pts:
            issues.append(_issue("error", "edge-unroutable", f"{name}: no route found. Move a node or set fromSide / toSide."))
            continue
        if e.get("no_room"):
            issues.append(_issue("error", "edge-label-no-room", f"{name}: no segment is long enough for its label or step badge"))
        segs = route.segments(pts)
        for a, b in segs:
            if abs(a[0] - b[0]) > 0.01 and abs(a[1] - b[1]) > 0.01:
                issues.append(_issue("error", "edge-diagonal", f"{name}: a segment is not horizontal or vertical"))
        if any(p[0] < 0 or p[1] < 0 or p[0] > W or p[1] > H for p in pts):
            issues.append(_issue("error", "clip", f"{name} leaves the canvas"))
        for n in nodes:
            if n["id"] in (e["from"], e["to"]):
                continue
            if any(route.seg_hits_node(s, n, 1) for s in segs):
                issues.append(_issue("error", "edge-through-node", f"{name} runs through node {n['id']!r}"))
        src, dst = by_id.get(e["from"]), by_id.get(e["to"])
        if src and any(route.seg_hits_node(s, src, -1) for s in segs):
            issues.append(_issue("error", "edge-through-node", f"{name} runs through its own start node"))
        if dst and any(route.seg_hits_node(s, dst, -1) for s in segs):
            issues.append(_issue("error", "edge-through-node", f"{name} runs through its own end node"))
        for node, point, word in ((src, pts[0], "start"), (dst, pts[-1], "end")):
            if node is None:
                continue
            if min(_dist_to_rect_edge(point, r) for r in node["shapes"] + [node["bbox"]]) > S.PORT_GAP + 2.5:
                issues.append(_issue("error", "edge-detached", f"{name}: the {word} is not on the edge of node {node['id']!r}"))
        for owner, tname, box in texts:
            if owner == ("edge", e["index"]) and "badge" in tname:
                continue
            if owner[0] == "edge" and "badge" in tname and owner[1] in mate_of[e["index"]]:
                continue      # the one badge of a trunk sits on every edge of the trunk
            if owner in (("node", e["from"]), ("node", e["to"])):
                continue
            if any(route.seg_hits_rect(s, box, 1) for s in segs):
                issues.append(_issue("error", "edge-on-label", f"{name} runs through the {tname}"))
        for other in edges:
            if other["index"] <= e["index"] or not other.get("points"):
                continue
            crossings += route.count_crossings(pts, other["points"])
            if other["index"] in mate_of[e["index"]] and _free_ends_apart(e, other):
                continue      # edges of one step that share a node are drawn as one trunk
            if route.count_overlaps(pts, other["points"], 3.5):
                issues.append(_issue("error", "edge-overlap", f"{name} runs on top of edge {other['index'] + 1}"))
    if crossings > S.MAX_CROSSINGS:
        issues.append(_issue("error", "limit-crossings", f"{crossings} edge crossings; the limit is {S.MAX_CROSSINGS}"))

    # ---- arrows per node side
    sides = {}
    for e in edges:
        if e.get("sides"):
            sides[(e["from"], e["sides"][0])] = sides.get((e["from"], e["sides"][0]), 0) + 1
            sides[(e["to"], e["sides"][1])] = sides.get((e["to"], e["sides"][1]), 0) + 1
    for (node_id, side), count in sorted(sides.items()):
        if count > S.PORT_MAX:
            issues.append(_issue("warn", "ports-crowded", f"node {node_id!r}: {count} arrows on its {side} side"))

    budget = S.SIZE_BUDGET.get(size, S.SIZE_BUDGET["m"])
    if W > budget:
        issues.append(_issue("warn", "size-budget", f"the drawing is {W} wide; size {size!r} allows {budget}. "
                             f"It will scroll on a phone beyond {int(336 / S.MIN_SCALE)}."))
    stats = {"width": W, "height": H, "nodes": len(nodes), "edges": len(edges), "crossings": crossings,
             "scrolls_on_phone": W * S.MIN_SCALE > 336}
    return issues, stats
