"""Orthogonal edge routing for grid layouts.

Every edge leaves a node on one side and enters the other node on one side. Between the two it
runs straight, makes one bend through a cell centre line, or travels along the mid-line of a
gutter (a "channel"). Candidates are enumerated and scored; the cheapest one that hits no node
wins. Then the ports on each node side are spread, parallel edges in one channel get their own
tracks, and a small local search swaps port and track orders to remove crossings.

Everything here is deterministic: no randomness, stable sort keys.
"""
from __future__ import annotations

from . import style as S
from . import textmetrics

SIDES = ("top", "right", "bottom", "left")
OUT = {"top": (0, -1), "bottom": (0, 1), "left": (-1, 0), "right": (1, 0)}
HORIZ = {"left", "right"}


# ------------------------------------------------------------------ geometry helpers

def segments(points: list) -> list:
    return [(points[i], points[i + 1]) for i in range(len(points) - 1)]


def seg_len(seg) -> float:
    (x1, y1), (x2, y2) = seg
    return abs(x2 - x1) + abs(y2 - y1)


def path_len(points) -> float:
    return sum(seg_len(s) for s in segments(points))


def is_h(seg) -> bool:
    return abs(seg[0][1] - seg[1][1]) < 0.01


def seg_hits_rect(seg, rect, pad: float = 0.0) -> bool:
    """True when the axis-aligned segment enters the rectangle grown by pad."""
    (x1, y1), (x2, y2) = seg
    rx, ry, rw, rh = rect
    return (min(x1, x2) < rx + rw + pad and max(x1, x2) > rx - pad
            and min(y1, y2) < ry + rh + pad and max(y1, y2) > ry - pad)


def seg_hits_node(seg, node, pad: float = 0.0) -> bool:
    return any(seg_hits_rect(seg, r, pad) for r in node["shapes"])


def rects_overlap(a, b, pad: float = 0.0) -> bool:
    return (a[0] < b[0] + b[2] + pad and a[0] + a[2] + pad > b[0]
            and a[1] < b[1] + b[3] + pad and a[1] + a[3] + pad > b[1])


def count_crossings(p1: list, p2: list) -> int:
    total = 0
    for a in segments(p1):
        for b in segments(p2):
            if is_h(a) == is_h(b):
                continue
            h, v = (a, b) if is_h(a) else (b, a)
            hx1, hx2 = sorted((h[0][0], h[1][0]))
            vy1, vy2 = sorted((v[0][1], v[1][1]))
            if hx1 + 0.5 < v[0][0] < hx2 - 0.5 and vy1 + 0.5 < h[0][1] < vy2 - 0.5:
                total += 1
    return total


def count_overlaps(p1: list, p2: list, near: float = 4.0) -> int:
    """Parallel segments that run closer than `near` over a shared stretch."""
    total = 0
    for a in segments(p1):
        for b in segments(p2):
            if is_h(a) != is_h(b):
                continue
            if is_h(a):
                if abs(a[0][1] - b[0][1]) >= near:
                    continue
                lo = max(min(a[0][0], a[1][0]), min(b[0][0], b[1][0]))
                hi = min(max(a[0][0], a[1][0]), max(b[0][0], b[1][0]))
            else:
                if abs(a[0][0] - b[0][0]) >= near:
                    continue
                lo = max(min(a[0][1], a[1][1]), min(b[0][1], b[1][1]))
                hi = min(max(a[0][1], a[1][1]), max(b[0][1], b[1][1]))
            if hi - lo > 3:
                total += 1
    return total


def _simplify(points: list):
    """Drop repeated points and merge collinear runs. None when the path doubles back."""
    out = []
    for p in points:
        if out and abs(out[-1][0] - p[0]) < 0.01 and abs(out[-1][1] - p[1]) < 0.01:
            continue
        out.append(p)
    i = 1
    while i < len(out) - 1:
        a, b, c = out[i - 1], out[i], out[i + 1]
        if abs(a[0] - b[0]) < 0.01 and abs(b[0] - c[0]) < 0.01:
            if (b[1] - a[1]) * (c[1] - b[1]) < 0:
                return None
            del out[i]
        elif abs(a[1] - b[1]) < 0.01 and abs(b[1] - c[1]) < 0.01:
            if (b[0] - a[0]) * (c[0] - b[0]) < 0:
                return None
            del out[i]
        else:
            i += 1
    for a, b in segments(out):
        if abs(a[0] - b[0]) > 0.01 and abs(a[1] - b[1]) > 0.01:
            return None
    return out


def _direction(seg):
    (x1, y1), (x2, y2) = seg
    if abs(x2 - x1) > abs(y2 - y1):
        return (1 if x2 > x1 else -1, 0)
    return (0, 1 if y2 > y1 else -1)


# ------------------------------------------------------------------ trunks (edges of one step)

def share_keys(edges: list) -> list:
    """Per edge (key_a, key_b): the trunk it shares at its start and at its end, or None.

    Two or more edges of one step that leave one node (fan-out) or enter one node (fan-in), drawn
    in the same style, form a trunk: they use one port and one gutter track, so they are drawn as
    one line that splits (or joins) near the nodes, and they carry one step badge."""
    def key(edge, end):
        if edge.get("step") is None:
            return None
        return (end, edge["step"], edge["from" if end == "a" else "to"], bool(edge.get("emph")),
                bool(edge.get("dashed")), edge.get("arrow", "end"))
    count = {}
    for edge in edges:
        for end in ("a", "b"):
            k = key(edge, end)
            if k is not None:
                count[k] = count.get(k, 0) + 1
    out = []
    for edge in edges:
        ka, kb = key(edge, "a"), key(edge, "b")
        out.append((ka if count.get(ka, 0) > 1 else None, kb if count.get(kb, 0) > 1 else None))
    return out


def keys_mate(k1, k2) -> bool:
    return (k1[0] is not None and k1[0] == k2[0]) or (k1[1] is not None and k1[1] == k2[1])


def mates(e1: dict, e2: dict) -> bool:
    """True when two edges belong to one trunk (lint uses this on scene edges)."""
    keys = share_keys([e1, e2])
    return keys_mate(keys[0], keys[1])


# ------------------------------------------------------------------ candidates

def realize(cand: dict, pa, pb, vx=None, hy=None):
    """Points of a candidate for the given port positions and channel coordinates."""
    kind = cand["kind"]
    a_h = cand["sa"] in HORIZ
    if kind == "S":
        pts = [pa, (pb[0], pa[1])] if a_h else [pa, (pa[0], pb[1])]
    elif kind == "L":
        pts = [pa, (pb[0], pa[1]), pb] if a_h else [pa, (pa[0], pb[1]), pb]
    elif kind == "Z":
        pts = [pa, (vx, pa[1]), (vx, pb[1]), pb] if a_h else [pa, (pa[0], hy), (pb[0], hy), pb]
    else:  # "W": three bends through one vertical and one horizontal channel
        if a_h:
            pts = [pa, (vx, pa[1]), (vx, hy), (pb[0], hy), pb]
        else:
            pts = [pa, (pa[0], hy), (vx, hy), (vx, pb[1]), pb]
    return _simplify(pts)


def _valid(points, sa: str, sb: str) -> bool:
    if not points or len(points) < 2:
        return False
    segs = segments(points)
    if _direction(segs[0]) != OUT[sa]:
        return False
    inward = (-OUT[sb][0], -OUT[sb][1])
    if _direction(segs[-1]) != inward:
        return False
    if len(segs) == 1:
        return seg_len(segs[0]) >= S.ARROW_LEN + 8
    return seg_len(segs[0]) >= 10 and seg_len(segs[-1]) >= S.ARROW_LEN + 6


def _candidates(a: dict, b: dict, lay: dict, edge: dict) -> list:
    out = []
    sides_a = [edge["fromSide"]] if edge.get("fromSide") else SIDES
    sides_b = [edge["toSide"]] if edge.get("toSide") else SIDES
    for sa in sides_a:
        for sb in sides_b:
            pa, pb = a["ports"][sa], b["ports"][sb]
            a_h, b_h = sa in HORIZ, sb in HORIZ
            combos = []
            if a_h == b_h:
                # straight, when the two ports face each other closely enough
                delta = (pa[1] - pb[1]) if a_h else (pa[0] - pb[0])
                reach = max(a["port_span"][sa], b["port_span"][sb])
                if abs(delta) <= reach and OUT[sa] == (-OUT[sb][0], -OUT[sb][1]):
                    narrow_a = a["port_span"][sa] <= b["port_span"][sb]
                    pin = (pa if narrow_a else pb)[1 if a_h else 0]
                    combos.append({"kind": "S", "pin": pin})
                for k in range(len(lay["vx"] if a_h else lay["hy"])):
                    combos.append({"kind": "Z", "k": k})
            else:
                combos.append({"kind": "L"})
                for k in range(len(lay["vx"])):
                    for m in range(len(lay["hy"])):
                        combos.append({"kind": "W", "k": k, "m": m})
            for combo in combos:
                cand = dict(combo, sa=sa, sb=sb)
                pts = nominal_points(cand, a, b, lay)
                if _valid(pts, sa, sb):
                    cand["points"] = pts
                    cand["_from"], cand["_to"] = a["id"], b["id"]
                    out.append(cand)
    return out


def _pinned(cand, pa, pb):
    if cand["kind"] != "S":
        return pa, pb
    if cand["sa"] in HORIZ:
        return (pa[0], cand["pin"]), (pb[0], cand["pin"])
    return (cand["pin"], pa[1]), (cand["pin"], pb[1])


def nominal_points(cand, a, b, lay):
    pa, pb = _pinned(cand, a["ports"][cand["sa"]], b["ports"][cand["sb"]])
    vx = lay["vx"][cand["k"]] if cand["kind"] in ("Z", "W") and (cand["sa"] in HORIZ or cand["kind"] == "W") else None
    if cand["kind"] == "Z":
        hy = lay["hy"][cand["k"]] if cand["sa"] not in HORIZ else None
    elif cand["kind"] == "W":
        hy = lay["hy"][cand["m"]]
    else:
        hy = None
    return realize(cand, pa, pb, vx, hy)


def _border_crossings(points, groups) -> int:
    total = 0
    for g in groups:
        rect = (g["x"], g["y"], g["w"], g["h"])
        for seg in segments(points):
            inside = [rect[0] < p[0] < rect[0] + rect[2] and rect[1] < p[1] < rect[1] + rect[3] for p in seg]
            if inside[0] != inside[1]:
                total += 1
            elif not inside[0] and seg_hits_rect(seg, rect):
                total += 2
    return total


def _cost(cand, edge_i, a, b, lay, chosen, flow, keys=None) -> float:
    pts = cand["points"]
    segs = segments(pts)
    cost = path_len(pts) + 34 * (len(pts) - 2)
    for n in lay["nodes"]:
        if n is a or n is b:
            continue
        if any(seg_hits_node(s, n, 5) for s in segs):
            cost += 100000
    # the path may touch its own nodes only at its two ends
    if any(seg_hits_node(s, a, 1) for s in segs[1:]):
        cost += 100000
    if any(seg_hits_node(s, b, 1) for s in segs[:-1]):
        cost += 100000
    cost += 10 * _border_crossings(pts, lay["groups"])
    for j, other in enumerate(chosen):
        if other is None or j == edge_i:
            continue
        cost += 420 * count_crossings(pts, other["points"])
        if keys and keys_mate(keys[edge_i], keys[j]):
            # one trunk: the shared stretch is wanted; leave the shared node on the same side
            ka, kb = keys[edge_i], keys[j]
            if ka[0] is not None and ka[0] == kb[0] and other["sa"] != cand["sa"]:
                cost += 60
            if ka[1] is not None and ka[1] == kb[1] and other["sb"] != cand["sb"]:
                cost += 60
            continue
        mine, theirs = pts, other["points"]
        # two edges that share a node side are separated later by port spreading
        if other.get("_to") == b["id"] and other["sb"] == cand["sb"] and len(mine) > 2 and len(theirs) > 2:
            mine, theirs = mine[:-1], theirs[:-1]
        if other.get("_from") == a["id"] and other["sa"] == cand["sa"] and len(mine) > 2 and len(theirs) > 2:
            mine, theirs = mine[1:], theirs[1:]
        cost += 160 * count_overlaps(mine, theirs)
    # the outer channels cost canvas space
    if cand["kind"] in ("Z", "W"):
        if cand["sa"] in HORIZ or cand["kind"] == "W":
            if cand["k"] in (0, lay["cols"]):
                cost += 40
        if cand["kind"] == "W" and cand["m"] in (0, lay["rows"]):
            cost += 40
        if cand["kind"] == "Z" and cand["sa"] not in HORIZ and cand["k"] in (0, lay["rows"]):
            cost += 40
    # mild preference for the reading direction
    want_in = "top" if flow == "down" else "left"
    want_out = "bottom" if flow == "down" else "right"
    if cand["sb"] != want_in:
        cost += 3
    if cand["sa"] != want_out:
        cost += 2
    return cost


# ------------------------------------------------------------------ ports and tracks

def _lead_key(points, horizontal_side: bool):
    """Where a path heads after leaving its port: used to order the ports on one side."""
    idx = 1 if horizontal_side else 0      # ports on a left/right side are spread along y
    start = points[0][idx]
    for p in points[1:]:
        if abs(p[idx] - start) > 0.5:
            return p[idx] - start
    return 0.0


def _track_gap(step_a, step_b) -> float:
    """Free stretch needed between two edges that follow each other on one gutter track.

    Edges of different steps that nearly touch on one track read as one line, so they need a
    clear gap; otherwise they get their own tracks."""
    if step_a is not None and step_b is not None and step_a != step_b:
        return S.TRACK_STEP_GAP
    return 14


class _State:
    def __init__(self, lay, edges, chosen, bias=None):
        self.lay = lay
        self.edges = edges
        self.chosen = chosen
        self.bias = bias or {}    # (node id, side) -> shift of every port on that side
        self.keys = share_keys(edges)
        self.nodes = {n["id"]: n for n in lay["nodes"]}
        self.ports = {}       # (node id, side) -> [port id, ...] in order; a trunk is one port
        self.gid = {}         # (edge index, "a"|"b") -> port id
        self.slots = {}       # (axis, k) -> {"of": {edge index: slot}, "order": [slot, ...]}
        self._init_ports()
        self._init_slots()

    def mates(self, i, j) -> bool:
        return keys_mate(self.keys[i], self.keys[j])

    def _init_ports(self):
        keyed = {}
        for i, (edge, cand) in enumerate(zip(self.edges, self.chosen)):
            pts = cand["points"]
            for end, node_id, side, path in (("a", edge["from"], cand["sa"], pts),
                                             ("b", edge["to"], cand["sb"], pts[::-1])):
                gid = self.keys[i][0 if end == "a" else 1] or ("edge", i, end)
                self.gid[(i, end)] = gid
                group = keyed.setdefault((node_id, side), {})
                group.setdefault(gid, []).append(_lead_key(path, side in HORIZ))
        for key in sorted(keyed):
            ranked = sorted((min(leads), n) for n, leads in enumerate(keyed[key].values()))
            gids = list(keyed[key])
            self.ports[key] = [gids[n] for _lead, n in ranked]

    def _init_slots(self):
        raw = {}
        for i, cand in enumerate(self.chosen):
            pts = cand["points"]
            if cand["kind"] == "Z":
                axis = "V" if cand["sa"] in HORIZ else "H"
                lo, hi = sorted((pts[0][1], pts[-1][1])) if axis == "V" else sorted((pts[0][0], pts[-1][0]))
                raw.setdefault((axis, cand["k"]), []).append((lo, hi, i))
            elif cand["kind"] == "W":
                vx, hy = self.lay["vx"][cand["k"]], self.lay["hy"][cand["m"]]
                if cand["sa"] in HORIZ:
                    raw.setdefault(("V", cand["k"]), []).append((*sorted((pts[0][1], hy)), i))
                    raw.setdefault(("H", cand["m"]), []).append((*sorted((vx, pts[-1][0])), i))
                else:
                    raw.setdefault(("H", cand["m"]), []).append((*sorted((pts[0][0], vx)), i))
                    raw.setdefault(("V", cand["k"]), []).append((*sorted((vx, pts[-1][1])), i))
        for key in sorted(raw):
            # edges of one trunk share a track: merge them into one cluster first
            clusters = []     # [lo, hi, [edge index, ...]]
            for lo, hi, i in sorted(raw[key]):
                for cluster in clusters:
                    if any(self.mates(i, j) for j in cluster[2]):
                        cluster[0], cluster[1] = min(cluster[0], lo), max(cluster[1], hi)
                        cluster[2].append(i)
                        break
                else:
                    clusters.append([lo, hi, [i]])
            ends = []         # per slot: list of (lo, hi, step)
            of = {}
            for lo, hi, members in sorted(clusters):
                step = self.edges[members[0]].get("step")
                for slot, spans in enumerate(ends):
                    if all(lo > h + _track_gap(step, st) or hi < l - _track_gap(step, st) for l, h, st in spans):
                        spans.append((lo, hi, step))
                        break
                else:
                    ends.append([(lo, hi, step)])
                    slot = len(ends) - 1
                for i in members:
                    of[i] = slot
            self.slots[key] = {"of": of, "order": list(range(len(ends)))}

    def tracks(self) -> dict:
        return {key: len(val["order"]) for key, val in self.slots.items()}

    def _port_offset(self, node_id, side, edge_i, end):
        order = self.ports[(node_id, side)]
        n = len(order)
        if n == 1:
            return 0.0
        span = self.nodes[node_id]["port_span"][side]
        step = min(S.PORT_STEP, 2 * span / (n - 1))
        return (order.index(self.gid[(edge_i, end)]) - (n - 1) / 2) * step

    def _track_offset(self, axis, k, edge_i):
        slot = self.slots[(axis, k)]
        n = len(slot["order"])
        return (slot["order"].index(slot["of"][edge_i]) - (n - 1) / 2) * S.TRACK

    def points(self, i):
        edge, cand = self.edges[i], self.chosen[i]
        a, b = self.nodes[edge["from"]], self.nodes[edge["to"]]
        sa, sb = cand["sa"], cand["sb"]
        bias_a = self.bias.get((a["id"], sa), 0.0)
        bias_b = self.bias.get((b["id"], sb), 0.0)
        off_a = self._port_offset(a["id"], sa, i, "a") + bias_a
        off_b = self._port_offset(b["id"], sb, i, "b") + bias_b
        pa, pb = a["ports"][sa], b["ports"][sb]
        if cand["kind"] == "S":
            # both ends share one coordinate: follow the busier side
            busy_b = len(self.ports[(b["id"], sb)]) > len(self.ports[(a["id"], sa)])
            off = (off_b - bias_b if busy_b else off_a - bias_a) + max(bias_a, bias_b, key=abs)
            if sa in HORIZ:
                pa, pb = (pa[0], cand["pin"] + off), (pb[0], cand["pin"] + off)
            else:
                pa, pb = (cand["pin"] + off, pa[1]), (cand["pin"] + off, pb[1])
            return realize(cand, pa, pb) or cand["points"]
        pa = (pa[0], pa[1] + off_a) if sa in HORIZ else (pa[0] + off_a, pa[1])
        pb = (pb[0], pb[1] + off_b) if sb in HORIZ else (pb[0] + off_b, pb[1])
        vx = hy = None
        if cand["kind"] == "Z":
            if sa in HORIZ:
                vx = self.lay["vx"][cand["k"]] + self._track_offset("V", cand["k"], i)
            else:
                hy = self.lay["hy"][cand["k"]] + self._track_offset("H", cand["k"], i)
        elif cand["kind"] == "W":
            vx = self.lay["vx"][cand["k"]] + self._track_offset("V", cand["k"], i)
            hy = self.lay["hy"][cand["m"]] + self._track_offset("H", cand["m"], i)
        return realize(cand, pa, pb, vx, hy) or cand["points"]

    def all_points(self):
        return [self.points(i) for i in range(len(self.edges))]

    def score(self):
        pts = self.all_points()
        hits = 0
        for i, p in enumerate(pts):
            edge = self.edges[i]
            for n in self.lay["nodes"]:
                if n["id"] in (edge["from"], edge["to"]):
                    continue
                if any(seg_hits_node(s, n, 2) for s in segments(p)):
                    hits += 1
        over = cross = 0
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                if not self.mates(i, j):
                    over += count_overlaps(pts[i], pts[j])
                cross += count_crossings(pts[i], pts[j])
        return (hits, over, cross, round(sum(path_len(p) for p in pts), 1))

    def improve(self):
        best = self.score()
        for _round in range(12):
            improved = False
            for key in sorted(self.ports):
                order = self.ports[key]
                for i in range(len(order) - 1):
                    order[i], order[i + 1] = order[i + 1], order[i]
                    trial = self.score()
                    if trial < best:
                        best, improved = trial, True
                    else:
                        order[i], order[i + 1] = order[i + 1], order[i]
            for key in sorted(self.slots):
                order = self.slots[key]["order"]
                for i in range(len(order)):
                    for j in range(i + 1, len(order)):
                        order[i], order[j] = order[j], order[i]
                        trial = self.score()
                        if trial < best:
                            best, improved = trial, True
                        else:
                            order[i], order[j] = order[j], order[i]
            if not improved:
                break
        return best


# ------------------------------------------------------------------ public API

def route(lay: dict, edges: list, flow: str = "down", bias: dict = None) -> dict:
    """Route all edges. Returns {"points": [...], "tracks": {(axis, k): n}, "sides": [...]}.

    bias: (node id, side) -> shift of the ports on that side (arch uses it to let a straight
    entry pass beside a group label)."""
    nodes = {n["id"]: n for n in lay["nodes"]}
    chosen = [None] * len(edges)
    keys = share_keys(edges)
    cands = []
    for edge in edges:
        a, b = nodes[edge["from"]], nodes[edge["to"]]
        cands.append(_candidates(a, b, lay, edge))
    for _round in range(2):
        for i, edge in enumerate(edges):
            if not cands[i]:
                continue
            a, b = nodes[edge["from"]], nodes[edge["to"]]
            scored = [(_cost(c, i, a, b, lay, chosen, flow, keys), n) for n, c in enumerate(cands[i])]
            chosen[i] = cands[i][min(scored)[1]]
    unroutable = [i for i, c in enumerate(chosen) if c is None]
    live = [i for i, c in enumerate(chosen) if c is not None]
    state = _State(lay, [edges[i] for i in live], [chosen[i] for i in live], bias)
    state.improve()
    pts = state.all_points()
    points = [None] * len(edges)
    sides = [None] * len(edges)
    for n, i in enumerate(live):
        points[i] = pts[n]
        sides[i] = (chosen[i]["sa"], chosen[i]["sb"])
    return {"points": points, "tracks": state.tracks(), "sides": sides, "unroutable": unroutable}


# ------------------------------------------------------------------ edge labels and step badges

def _text_box(seg, pos, text_w, has_badge: bool, side: int):
    """Box of a label next to a segment. side 0: right of / above the line, 1: left of / below."""
    (x1, y1), (x2, y2) = seg
    h = S.EDGE_LABEL_H
    if is_h(seg):
        px, y = pos, y1
        off = (S.BADGE_R + 3) if has_badge else 4
        top = y - off - h if side == 0 else y + off
        return (px - text_w / 2, top, text_w, h), "middle", px
    x, py = x1, pos
    off = (S.BADGE_R + 5) if has_badge else 6
    if side == 0:
        return (x + off, py - h / 2, text_w, h), "start", x + off
    return (x - off - text_w, py - h / 2, text_w, h), "end", x - off


def place_labels(lay: dict, edges: list, points: list) -> list:
    """Choose a position for the label and the step badge of every edge.

    Returns one dict per edge: {"label": {...} | None, "badge": {...} | None, "clash": int}.
    """
    placed = []           # boxes of labels and badges already placed
    hard = [r for n in lay["nodes"] for r in n["shapes"]]
    hard_labels = [g["label_box"] for g in lay["groups"]]
    borders = []
    for g in lay["groups"]:
        x, y, w, h = g["x"], g["y"], g["w"], g["h"]
        borders += [((x, y), (x + w, y)), ((x, y + h), (x + w, y + h)), ((x, y), (x, y + h)), ((x + w, y), (x + w, y + h))]
    all_segs = [(i, s) for i, pts in enumerate(points) if pts for s in segments(pts)]
    keys = share_keys(edges)
    trunks = {}           # trunk key -> index of the edge that carries the one badge of the trunk
    results = []
    for i, edge in enumerate(edges):
        pts = points[i]
        text = edge.get("label")
        step = edge.get("step")
        if step is not None and any(k is not None and k in trunks for k in keys[i]):
            step = None   # the trunk already carries the badge of this step
        if pts is None or (not text and step is None):
            results.append({"label": None, "badge": None, "clash": 0})
            continue
        text_w = textmetrics.text_width(text, S.EDGE_FS) if text else 0
        segs = segments(pts)
        arrow = edge.get("arrow", "end")
        spots = _label_spots(segs, arrow, step is not None)
        trunk = _trunk_spots(i, keys, points, arrow) if step is not None else None

        def search(tries):
            best = None
            for rank, seg, positions in tries:
                horizontal = is_h(seg)
                for t, pos in positions:
                    for side in ((0, 1) if text else (0,)):
                        clash = 0
                        soft = 0.0
                        boxes = []
                        badge = None
                        if step is not None:
                            cx, cy = (pos, seg[0][1]) if horizontal else (seg[0][0], pos)
                            badge = {"n": step, "cx": cx, "cy": cy}
                            bbox = (cx - S.BADGE_R, cy - S.BADGE_R, 2 * S.BADGE_R, 2 * S.BADGE_R)
                            boxes.append(bbox)
                            for j, other in all_segs:
                                if j != i and not keys_mate(keys[i], keys[j]) and seg_hits_rect(other, bbox, 2):
                                    clash += 1
                            for border in borders:
                                if seg_hits_rect(border, bbox, 1):
                                    soft += 150
                        label = None
                        if text:
                            tbox, anchor, tx = _text_box(seg, pos, text_w, step is not None, side)
                            label = {"text": text, "x": tx, "y": tbox[1] + 11, "anchor": anchor, "box": tbox, "w": text_w}
                            boxes.append(tbox)
                            for _j, other in all_segs:
                                if seg_hits_rect(other, tbox, 2):
                                    clash += 1
                            for border in borders:
                                if seg_hits_rect(border, tbox, 1):
                                    soft += 300
                        for box in boxes:
                            if box[0] < 2 or box[1] < 2 or box[0] + box[2] > lay["w"] - 2 or box[1] + box[3] > lay["h"] - 2:
                                clash += 1
                            clash += sum(1 for r in hard if rects_overlap(box, r, 3))
                            clash += sum(1 for r in hard_labels if rects_overlap(box, r, 2))
                            clash += sum(1 for r in placed if rects_overlap(box, r, 3))
                        score = (clash, soft + abs(t - 0.5) * 20 + side * 4 + rank * 6)
                        if best is None or score < best[0]:
                            best = (score, label, badge, boxes)
            return best

        best = None
        if trunk:
            best = search(trunk[1])
            if best is not None and best[0][0] == 0:
                for key in trunk[0]:
                    trunks[key] = i
            else:
                best = None       # no clean place on the trunk: every edge keeps its own badge
        if best is None:
            best = search(spots)
        if best is None:
            results.append({"label": None, "badge": None, "clash": 1, "no_room": True})
            continue
        placed += best[3]
        results.append({"label": best[1], "badge": best[2], "clash": best[0][0]})
    return results


_SPOT_T = (0.5, 0.35, 0.65, 0.25, 0.75, 0.12, 0.88, 0.0, 1.0)


def _label_spots(segs: list, arrow: str, has_badge: bool, only: int = None, part=None) -> list:
    """Candidate places along an edge: [(rank, segment, [(t, position), ...]), ...].

    only / part: look at one segment index only, and at a part of that segment (a trunk)."""
    ranked = sorted(range(len(segs)), key=lambda k: (-seg_len(segs[k]), k))
    out = []
    for rank, k in enumerate(ranked):
        if only is not None and k != only:
            continue
        seg = part if only is not None and part is not None else segs[k]
        horizontal = is_h(seg)
        lo, hi = sorted((seg[0][0], seg[1][0])) if horizontal else sorted((seg[0][1], seg[1][1]))
        start_first = (seg[0][0] if horizontal else seg[0][1]) == lo
        m_first = 3 + (S.ARROW_LEN if k == 0 and arrow == "both" else 0)
        m_last = 3 + (S.ARROW_LEN if k == len(segs) - 1 and arrow != "none" else 0)
        m_lo, m_hi = (m_first, m_last) if start_first else (m_last, m_first)
        need = (S.BADGE_R if has_badge else (S.EDGE_LABEL_H / 2 if not horizontal else 4))
        lo2, hi2 = lo + m_lo + need, hi - m_hi - need
        if hi2 < lo2:
            continue
        out.append((0 if only is not None else rank, seg, [(t, lo2 + (hi2 - lo2) * t) for t in _SPOT_T]))
    return out


def _trunk_spots(i: int, keys: list, points: list, arrow: str):
    """Places for the one badge of a trunk: (trunk keys, spots) or None.

    The badge sits on the stretch that every edge of the trunk shares. When that stretch is too
    short for a badge, the badge sits on the point where the trunk splits (or joins)."""
    for end, key in (("a", keys[i][0]), ("b", keys[i][1])):
        if key is None:
            continue
        members = [j for j in range(len(points)) if points[j] and keys[j][0 if end == "a" else 1] == key]
        if len(members) < 2 or members[0] != i:
            continue
        paths = [points[j] if end == "a" else points[j][::-1] for j in members]
        origin = paths[0][0]
        heading = _direction((paths[0][0], paths[0][1]))
        if any(abs(p[0][0] - origin[0]) > 0.5 or abs(p[0][1] - origin[1]) > 0.5
               or _direction((p[0], p[1])) != heading for p in paths):
            continue
        shared = min(seg_len((p[0], p[1])) for p in paths)
        if all(len(p) == 2 for p in paths):
            continue          # the edges lie on top of each other from end to end: no trunk to mark
        cut = (origin[0] + heading[0] * shared, origin[1] + heading[1] * shared)
        mine = points[i]
        segs = segments(mine)
        part = (origin, cut) if end == "a" else (cut, origin)
        k = 0 if end == "a" else len(segs) - 1
        spots = _label_spots(segs, arrow, True, only=k, part=part)
        if not spots and shared >= 6:
            horizontal = is_h(part)
            spots = [(0, part, [(0.5, cut[0] if horizontal else cut[1])])]
        if spots:
            return (key,), spots
    return None
