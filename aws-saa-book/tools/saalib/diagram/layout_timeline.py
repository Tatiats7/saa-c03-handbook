"""The "timeline" kind: a horizontal axis with ticks, lanes of spans above it, and events.

The axis is ordinal, not to scale: ticks follow each other in order, whatever their labels say
(Day 0, Day 30, Day 365). The distance from one tick to the next grows until every span label fits
in its bar. A span without "to" runs on past the last tick. An event is a vertical line through
all lanes at one tick.
"""
from __future__ import annotations

from . import shapes
from . import style as S
from . import textmetrics

KIND = "timeline"

MAX_TICKS = 7
MAX_LANES = 4
MAX_SPANS = 12
MAX_EVENTS = 3
MAX_TICK_WORDS = 3
MAX_EVENT_WORDS = 3

COL_MIN = 84          # smallest distance between two ticks
COL_MAX = 190         # largest; a label that still does not fit is a lint error
COL_STEP = 4
BAR_H = 40
BAR_INSET = 2         # a bar stops this far from its ticks, so neighbours do not touch
EVENT_INSET = 5       # ... and this far from a tick that carries an event line, so line and border stay apart
TAIL = 26             # the axis runs on past the last tick and ends in an arrowhead
EVENT_BAND = 20       # room for event labels above the lanes
LANE_LABEL = 17       # lane label band above its bars
LANE_GAP = 12
TICK = 5


def lint_spec(spec: dict, icons: dict) -> list:
    issues = shapes.common_issues(spec)
    ticks = spec.get("ticks", [])
    lanes = spec.get("lanes", [])
    events = spec.get("events", [])
    ids = [t["id"] for t in ticks]
    order = {ident: i for i, ident in enumerate(ids)}
    for ident in shapes.duplicates(ids):
        issues.append(shapes.issue("error", "ref-duplicate", f"tick id {ident!r} is used more than once"))
    if len(ticks) > MAX_TICKS:
        issues.append(shapes.issue("error", "limit-ticks", f"{len(ticks)} ticks; the limit is {MAX_TICKS}"))
    if len(lanes) > MAX_LANES:
        issues.append(shapes.issue("error", "limit-lanes", f"{len(lanes)} lanes; the limit is {MAX_LANES}"))
    if len(events) > MAX_EVENTS:
        issues.append(shapes.issue("error", "limit-events", f"{len(events)} events; the limit is {MAX_EVENTS}"))
    total = sum(len(lane["spans"]) for lane in lanes)
    if total > MAX_SPANS:
        issues.append(shapes.issue("error", "limit-spans", f"{total} spans; the limit is {MAX_SPANS}. Split the figure."))
    for t in ticks:
        issues += shapes.label_issues(f"tick {t['id']!r}", t["label"], MAX_TICK_WORDS)
    if spec.get("axis"):
        issues += shapes.label_issues("axis title", spec["axis"], 5)
    emph = 0
    for li, lane in enumerate(lanes, 1):
        issues += shapes.label_issues(f"lane {li}", lane["label"], 5)
        taken = []
        for si, span in enumerate(lane["spans"], 1):
            name = f"lane {li}, span {si}"
            issues += shapes.label_issues(name, span["label"], S.MAX_LABEL_WORDS)
            emph += bool(span.get("emph"))
            bad = [span[k] for k in ("from", "to") if k in span and span[k] not in order]
            for ident in bad:
                issues.append(shapes.issue("error", "ref-unknown", f"{name}: unknown tick {ident!r}"))
            if bad:
                continue
            start = order[span["from"]]
            end = order[span["to"]] if "to" in span else len(ticks)
            if end <= start:
                issues.append(shapes.issue("error", "span-order", f"{name}: \"to\" must be a later tick than \"from\""))
                continue
            if any(start < e and s < end for s, e in taken):
                issues.append(shapes.issue("error", "span-overlap", f"{name} overlaps another span of the lane"))
            taken.append((start, end))
    seen = set()
    for ei, event in enumerate(events, 1):
        issues += shapes.label_issues(f"event {ei}", event["label"], MAX_EVENT_WORDS)
        emph += bool(event.get("emph"))
        if event["at"] not in order:
            issues.append(shapes.issue("error", "ref-unknown", f"event {ei}: unknown tick {event['at']!r}"))
        elif event["at"] in seen:
            issues.append(shapes.issue("error", "event-same-tick", f"event {ei}: tick {event['at']!r} already has an event"))
        seen.add(event["at"])
    return issues + shapes.emph_issues(emph)


def _fits(label: str, width: float) -> bool:
    m = shapes.measure(label, width, min_w=0)
    return len(m["lines"]) <= S.NODE_MAX_LINES and m["text_w"] <= m["avail"]


def _insets(spec: dict, order: dict) -> list:
    """Per tick: how far a bar stops before it."""
    marked = {order[e["at"]] for e in spec.get("events", []) if e["at"] in order}
    return [EVENT_INSET if i in marked else BAR_INSET for i in range(len(spec["ticks"]))]


def _columns(spec: dict, order: dict) -> list:
    """Distance from each tick to the next: as small as the tick labels and the span labels allow.

    The axis is ordinal, so the distances need not be equal."""
    ticks = spec["ticks"]
    insets = _insets(spec, order)
    tick_w = [textmetrics.text_width(t["label"], S.EDGE_FS) for t in ticks]
    cols = [max(COL_MIN, (tick_w[i] + tick_w[i + 1]) / 2 + 10) for i in range(len(ticks) - 1)]
    spans = []
    for lane in spec["lanes"]:
        for span in lane["spans"]:
            a = order[span["from"]]
            b = order[span["to"]] if "to" in span else len(ticks) - 1
            spans.append((b - a, a, b, span))
    for _cells, a, b, span in sorted(spans, key=lambda s: (s[0], s[1])):
        tail = 0 if "to" in span else TAIL
        if b == a:                    # an open span that starts on the last tick has only the tail
            continue
        limit = COL_MAX * (b - a)
        inset = insets[a] + (insets[b] if "to" in span else BAR_INSET)
        while not _fits(span["label"], sum(cols[a:b]) + tail - inset) and sum(cols[a:b]) < limit:
            for i in range(a, b):
                cols[i] += COL_STEP / (b - a)
    return [float(round(c)) for c in cols]


def build_scene(spec: dict) -> dict:
    ticks = spec["ticks"]
    lanes = spec["lanes"]
    events = spec.get("events", [])
    order = {t["id"]: i for i, t in enumerate(ticks)}
    cols = _columns(spec, order)

    def half(text, bold=False):
        return textmetrics.text_width(text, S.EDGE_FS, bold) / 2

    # ---- x: labels centred on a tick must stay inside the canvas
    over_left = max([half(ticks[0]["label"])] + [half(e["label"], True) for e in events if order[e["at"]] == 0])
    xs = [S.MARGIN + max(over_left, 2)]
    for col in cols:
        xs.append(xs[-1] + col)
    over_right = max([half(ticks[-1]["label"]), TAIL]
                     + [half(e["label"], True) for e in events if order[e["at"]] == len(ticks) - 1])
    end_x = xs[-1] + TAIL
    width = xs[-1] + over_right + S.MARGIN

    nodes, texts, decor = [], [], []
    y = S.MARGIN
    lanes_top = y + (EVENT_BAND if events else 0)
    y = lanes_top
    measured = []
    insets = _insets(spec, order)
    for lane in lanes:
        row = []
        for span in lane["spans"]:
            a = xs[order[span["from"]]] + insets[order[span["from"]]]
            b = (xs[order[span["to"]]] - insets[order[span["to"]]]) if "to" in span else end_x - BAR_INSET
            row.append((span, a, b, shapes.measure(span["label"], b - a, min_w=0, min_h=BAR_H, width=b - a)))
        measured.append(row)
    lane_boxes = []
    for li, (lane, row) in enumerate(zip(lanes, measured), 1):
        texts.append(shapes.text(lane["label"], xs[0] + 4, y + 11, cls="dg-mt", size=S.GROUP_FS))
        lane_boxes.append((li, texts[-1]["box"]))
        bar_h = max(m["h"] for _s, _a, _b, m in row)
        for si, (span, a, b, m) in enumerate(row, 1):
            m["h"] = bar_h
            nodes.append(shapes.place(m, f"l{li}s{si}", (a + b) / 2, y + LANE_LABEL, emph=span.get("emph"), emph_fill=True))
        y += LANE_LABEL + bar_h + LANE_GAP
    axis_y = y + 2

    # ---- guides, axis, ticks, events (drawn under the bars)
    for x in xs:
        if not any(box[0] - 3 < x < box[0] + box[2] + 3 for _li, box in lane_boxes):
            decor.append({"t": "line", "cls": "dg-ll", "x1": x, "y1": lanes_top, "x2": x, "y2": axis_y})
            continue
        top = lanes_top                          # a guide skips the lane labels it would run through
        for _li, box in lane_boxes:
            if box[0] - 3 < x < box[0] + box[2] + 3:
                if box[1] - 2 > top:
                    decor.append({"t": "line", "cls": "dg-ll", "x1": x, "y1": top, "x2": x, "y2": box[1] - 2})
                top = box[1] + box[3] + 1
        decor.append({"t": "line", "cls": "dg-ll", "x1": x, "y1": top, "x2": x, "y2": axis_y})
    decor.append({"t": "line", "cls": "dg-ax", "x1": xs[0], "y1": axis_y, "x2": end_x - S.ARROW_LEN + 1.5, "y2": axis_y})
    decor.append({"t": "poly", "cls": "dg-ah", "points": [(end_x, axis_y), (end_x - S.ARROW_LEN, axis_y - S.ARROW_HALF),
                                                          (end_x - S.ARROW_LEN, axis_y + S.ARROW_HALF)]})
    for tick, x in zip(ticks, xs):
        decor.append({"t": "line", "cls": "dg-ax", "x1": x, "y1": axis_y - TICK, "x2": x, "y2": axis_y + TICK})
        texts.append(shapes.text(tick["label"], x, axis_y + TICK + 15, anchor="middle"))
    bottom = axis_y + TICK + 19
    if spec.get("axis"):
        texts.append(shapes.text(spec["axis"], (xs[0] + end_x) / 2, bottom + 14, anchor="middle", cls="dg-mt", size=S.GROUP_FS))
        bottom += 18
    for event in events:
        x = xs[order[event["at"]]]
        strong = bool(event.get("emph"))
        decor.append({"t": "line", "cls": "dg-ev" if strong else "dg-ax", "x1": x, "y1": lanes_top - 3, "x2": x, "y2": axis_y})
        texts.append(shapes.text(event["label"], x, S.MARGIN + 11, anchor="middle",
                                 cls="dg-evl" if strong else "dg-el", bold=strong))
    out = shapes.scene(KIND, spec["id"], width, bottom + S.MARGIN, nodes, texts=texts, decor=decor)
    out["ticks_x"] = xs
    out["event_hits"] = [(event["label"], li) for event in events for li, box in lane_boxes
                         if box[0] - 3 < xs[order[event["at"]]] < box[0] + box[2] + 3]
    return out


def lint_scene(scene: dict, spec: dict) -> tuple:
    from . import lint
    issues, stats = lint.lint_scene(scene, spec.get("size", "m"))
    for label, lane in scene.get("event_hits", []):
        issues.append(shapes.issue("error", "event-on-label", f"the line of event {label!r} runs through the label of "
                                   f"lane {lane}. Shorten the lane label or move the event."))
    return issues, stats
