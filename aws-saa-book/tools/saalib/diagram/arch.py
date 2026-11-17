"""The "arch" kind: grid layout plus orthogonal routing, iterated until the gutters fit.

build_scene(spec) returns a scene: plain geometry that svg.py draws and lint.py checks.
Other kinds return the same scene shape (see TOOLS-diagram.md, "Scene").
"""
from __future__ import annotations

import math

from . import layout_grid
from . import route
from . import style as S


def _place_group_labels(lay: dict, points: list) -> bool:
    """Align each group label left or right so that no edge runs through it.

    Returns True when at least one label still collides (the caller widens the columns)."""
    segs = [s for pts in points if pts for s in route.segments(pts)]
    unresolved = False
    for g in lay["groups"]:
        if g["label_w"] + 2 * S.GROUP_LABEL_INSET > g["w"]:
            unresolved = True
            continue
        for anchor in ("start", "end"):
            layout_grid.place_group_label(g, anchor)
            if not any(route.seg_hits_rect(s, g["label_box"], S.GROUP_LABEL_CLEAR) for s in segs):
                break
        else:
            layout_grid.place_group_label(g, "start")
            unresolved = True
    return unresolved


def _label_bias(lay: dict, routed: dict, edges: list) -> dict:
    """Port shifts that let an arrow pass beside a group label instead of through it.

    An arrow that enters or leaves a node at the top or bottom crosses the label band of the
    groups around the node. When the label (kept at the left) reaches the arrow, the arrow moves
    to the right, as far as the node side allows. Returns (node id, side) -> shift; a label that
    no such shift can clear is left to the caller (right-aligned label, then wider columns)."""
    nodes = {n["id"]: n for n in lay["nodes"]}
    bias = {}
    for g in lay["groups"]:
        if g["label_w"] + 2 * S.GROUP_LABEL_INSET > g["w"]:
            continue
        layout_grid.place_group_label(g, "start")
        box = g["label_box"]
        need = {}
        possible = True
        for i, pts in enumerate(routed["points"]):
            if not pts or not possible:
                continue
            segs = route.segments(pts)
            for k, seg in enumerate(segs):
                if not route.seg_hits_rect(seg, box, S.GROUP_LABEL_CLEAR):
                    continue
                shift = box[0] + box[2] + S.GROUP_LABEL_CLEAR + 2.5 - seg[0][0]
                sa, sb = routed["sides"][i]
                ends = []
                if not route.is_h(seg):
                    if k == 0 and sa in ("top", "bottom"):
                        ends.append((edges[i]["from"], sa))
                    if k == len(segs) - 1 and sb in ("top", "bottom"):
                        ends.append((edges[i]["to"], sb))
                if not ends:
                    possible = False
                    break
                for node_id, side in ends:
                    node = nodes[node_id]
                    offset = seg[0][0] - node["ports"][side][0]
                    if offset + shift > node["port_span"][side] + 0.01:
                        possible = False
                    need[(node_id, side)] = max(need.get((node_id, side), 0.0), shift)
        if possible:
            for key, shift in need.items():
                bias[key] = max(bias.get(key, 0.0), shift)
    return bias


def _solve(spec: dict, cell_w: float):
    """Layout and routing for one column width; the gutters grow until every track fits."""
    edges = spec.get("edges", [])
    flow = spec.get("flow", "down")
    vt, ht = {}, {}
    lay = routed = None
    for _ in range(8):
        lay = layout_grid.layout(spec, cell_w, vt, ht)
        routed = route.route(lay, edges, flow)
        grew = False
        for (axis, k), n in routed["tracks"].items():
            store = vt if axis == "V" else ht
            if n > store.get(k, 0):
                store[k] = n
                grew = True
        if not grew:
            break
    # tighten: drop gutters that an earlier pass reserved but the final routes do not use
    used_v = {k: n for (axis, k), n in routed["tracks"].items() if axis == "V"}
    used_h = {k: n for (axis, k), n in routed["tracks"].items() if axis == "H"}
    if used_v != vt or used_h != ht:
        lay2 = layout_grid.layout(spec, cell_w, used_v, used_h)
        routed2 = route.route(lay2, edges, flow)
        again_v = {k: n for (axis, k), n in routed2["tracks"].items() if axis == "V"}
        again_h = {k: n for (axis, k), n in routed2["tracks"].items() if axis == "H"}
        if again_v == used_v and again_h == used_h:
            lay, routed = lay2, routed2
    return lay, routed


def build_scene(spec: dict) -> dict:
    edges = spec.get("edges", [])
    cell_w = S.CELL_W
    while True:
        lay, routed = _solve(spec, cell_w)
        bias = _label_bias(lay, routed, edges)
        if bias:
            routed = route.route(lay, edges, spec.get("flow", "down"), bias)
        unresolved = _place_group_labels(lay, routed["points"])
        if not unresolved or cell_w >= S.CELL_W_MAX:
            break
        cell_w += S.CELL_W_STEP
    labels = route.place_labels(lay, edges, routed["points"])

    scene_edges = []
    for i, edge in enumerate(edges):
        scene_edges.append({
            "index": i, "from": edge["from"], "to": edge["to"], "step": edge.get("step"),
            "points": routed["points"][i],
            "arrow": edge.get("arrow", "end"), "emph": bool(edge.get("emph")), "dashed": bool(edge.get("dashed")),
            "label": labels[i]["label"], "badge": labels[i]["badge"], "no_room": bool(labels[i].get("no_room")),
            "sides": routed["sides"][i],
        })
    groups = sorted(lay["groups"], key=lambda g: (g["depth"], g["id"]))
    return {
        "kind": "arch", "id": spec["id"], "w": int(math.ceil(lay["w"])), "h": int(math.ceil(lay["h"])),
        "groups": groups, "nodes": lay["nodes"], "edges": scene_edges, "texts": [],
        "cell_w": cell_w, "group_labels_unresolved": unresolved,
    }
