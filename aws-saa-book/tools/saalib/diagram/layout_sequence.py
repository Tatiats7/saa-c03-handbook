"""The "sequence" kind: order in time. Actors across the top, a lifeline under each, numbered
messages from top to bottom, optional asides (note boxes) on a lifeline.

The gaps between lifelines grow until every message label fits in the gap next to its sender, so
a label never sits on another lifeline.
"""
from __future__ import annotations

from . import shapes
from . import style as S
from . import textmetrics

KIND = "sequence"

MAX_ACTORS = 5
MAX_MESSAGES = 10
MAX_ASIDES = 3
MAX_MESSAGE_WORDS = 4
MAX_ASIDE_WORDS = 6

HEAD_W = 112          # widest actor label
MIN_GAP = 96          # smallest distance between two lifelines
FIRST = 16            # actor to the first row
ROW = 44              # height of a message row; the line sits LINE_Y below the row top
LINE_Y = 30
LOOP_W = 30           # a message from an actor to itself: a loop to the right of the lifeline
LOOP_H = 28
ASIDE_W = 150
TAIL = 12             # lifeline below the last row


def lint_spec(spec: dict, icons: dict) -> list:
    issues = shapes.common_issues(spec)
    actors = spec.get("actors", [])
    messages = spec.get("messages", [])
    asides = spec.get("asides", [])
    ids = [a["id"] for a in actors]
    for ident in shapes.duplicates(ids):
        issues.append(shapes.issue("error", "ref-duplicate", f"actor id {ident!r} is used more than once"))
    if len(actors) > MAX_ACTORS:
        issues.append(shapes.issue("error", "limit-actors", f"{len(actors)} actors; the limit is {MAX_ACTORS}. Split the figure."))
    if len(messages) > MAX_MESSAGES:
        issues.append(shapes.issue("error", "limit-messages", f"{len(messages)} messages; the limit is {MAX_MESSAGES}. Split the figure."))
    if len(asides) > MAX_ASIDES:
        issues.append(shapes.issue("error", "limit-asides", f"{len(asides)} asides; the limit is {MAX_ASIDES}"))
    for a in actors:
        issues += shapes.label_issues(f"actor {a['id']!r}", a["label"], S.MAX_LABEL_WORDS)
        issues += shapes.icon_issues(f"actor {a['id']!r}", a.get("icon"), icons)
    used = set()
    for i, m in enumerate(messages, 1):
        for end in ("from", "to"):
            if m[end] not in ids:
                issues.append(shapes.issue("error", "ref-unknown", f"message {i}: unknown actor {m[end]!r}"))
            used.add(m[end])
        issues += shapes.label_issues(f"message {i}", m["label"], MAX_MESSAGE_WORDS)
        if not shapes.one_sentence(m["say"]):
            issues.append(shapes.issue("error", "say", f"message {i}: \"say\" must be exactly one sentence ending with a full stop"))
    for i, note in enumerate(asides, 1):
        if note["over"] not in ids:
            issues.append(shapes.issue("error", "ref-unknown", f"aside {i}: unknown actor {note['over']!r}"))
        if note["after"] > len(messages):
            issues.append(shapes.issue("error", "aside-after", f"aside {i}: \"after\" is {note['after']} but there are "
                                       f"{len(messages)} messages"))
        issues += shapes.label_issues(f"aside {i}", note["text"], MAX_ASIDE_WORDS)
    for ident in ids:
        if ident not in used and not any(i["code"].startswith("ref-") for i in issues):
            issues.append(shapes.issue("error", "actor-unused", f"actor {ident!r} sends and receives no message"))
    issues += shapes.emph_issues(sum(1 for x in actors + messages + asides if x.get("emph")))
    return issues


def caption(spec: dict) -> dict:
    return {"title": spec.get("title", ""), "claim": spec.get("claim", ""), "alt": spec.get("alt", ""),
            "steps": [(i, m["say"]) for i, m in enumerate(spec.get("messages", []), 1)]}


def build_scene(spec: dict) -> dict:
    actors = spec["actors"]
    messages = spec["messages"]
    asides = spec.get("asides", [])
    index = {a["id"]: i for i, a in enumerate(actors)}
    n = len(actors)
    heads = [shapes.measure(a["label"], HEAD_W, a.get("icon")) for a in actors]
    half = [m["w"] / 2 for m in heads]
    notes = [shapes.measure(note["text"], ASIDE_W, min_w=60, min_h=32) for note in asides]

    # ---- distances between lifelines
    gaps = [max(MIN_GAP, half[i] + half[i + 1] + 14) for i in range(n - 1)]
    left_extra = right_extra = 0.0

    def need_right(i, amount):
        nonlocal right_extra
        if i < n - 1:
            gaps[i] = max(gaps[i], amount + 8)
        else:
            right_extra = max(right_extra, amount)

    def need_left(i, amount):
        nonlocal left_extra
        if i > 0:
            gaps[i - 1] = max(gaps[i - 1], amount + 8)
        else:
            left_extra = max(left_extra, amount)

    for m in messages:
        a, b = index[m["from"]], index[m["to"]]
        label_w = textmetrics.text_width(m["label"], S.EDGE_FS)
        if a == b:
            need_right(a, LOOP_W + S.BADGE_R + 5 + label_w + 2)
        elif b > a:
            gaps[a] = max(gaps[a], label_w + 20)
        else:
            gaps[a - 1] = max(gaps[a - 1], label_w + 20)
    for note, m in zip(asides, notes):
        i = index[note["over"]]
        need_right(i, m["w"] / 2 + 4)
        need_left(i, m["w"] / 2 + 4)

    xs = [S.MARGIN + max(half[0], left_extra)]
    for gap in gaps:
        xs.append(xs[-1] + gap)
    width = xs[-1] + max(half[-1], right_extra) + S.MARGIN

    # ---- actors
    nodes, edges, decor = [], [], []
    head_h = max(m["h"] for m in heads)
    for a, m, x in zip(actors, heads, xs):
        nodes.append(shapes.place(m, a["id"], x, S.MARGIN, emph=a.get("emph")))

    # ---- rows: asides and messages in order
    y = S.MARGIN + head_h + FIRST

    def add_asides(after):
        nonlocal y
        for k, (note, m) in enumerate(zip(asides, notes)):
            if note["after"] != after:
                continue
            nodes.append(shapes.place(m, f"aside{k + 1}", xs[index[note["over"]]], y + 8, box_cls="dg-nt",
                                      emph=note.get("emph"), emph_fill=True))
            y += 8 + m["h"] + 4

    add_asides(0)
    for k, m in enumerate(messages):
        a, b = index[m["from"]], index[m["to"]]
        number = k + 1
        if a == b:
            x, top = xs[a], y + 16
            points = [(x, top), (x + LOOP_W, top), (x + LOOP_W, top + LOOP_H), (x, top + LOOP_H)]
            badge = {"n": number, "cx": x + LOOP_W, "cy": top + LOOP_H / 2}
            label = shapes.v_label(m["label"], x + LOOP_W, top + LOOP_H / 2, S.BADGE_R + 5)
            y += 16 + LOOP_H + 12
        else:
            line = y + LINE_Y
            direction = 1 if b > a else -1
            points = [(xs[a], line), (xs[b], line)]
            # the badge starts on the sender's lifeline, so no stub of the line shows before it
            badge = {"n": number, "cx": xs[a] + direction * (S.BADGE_R + 1), "cy": line}
            label = shapes.h_label(m["label"], (xs[a] + xs[a + direction]) / 2, line, badge=True)
            y += ROW
        # the ends are on lifelines, not on nodes, so the ids are not node ids
        edges.append(shapes.edge(k, m["from"] + ".life", m["to"] + ".life", points, label, badge,
                                 emph=m.get("emph"), dashed=m.get("dashed")))
        add_asides(number)
    bottom = y + TAIL
    for node, x in zip(nodes[:n], xs):
        decor.append({"t": "line", "cls": "dg-ll", "x1": x, "y1": node["bbox"][1] + node["bbox"][3] + S.PORT_GAP,
                      "x2": x, "y2": bottom})
    out = shapes.scene(KIND, spec["id"], width, bottom + S.MARGIN, nodes, edges, decor=decor)
    out["lifelines"] = xs
    return out
