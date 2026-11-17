"""The "ladder" kind: a decision tree drawn as a ladder.

A vertical spine of questions. Each question has one answer that leaves to the right and ends on
an outcome; the other answer continues down the spine to the next question. The spine ends on the
"else" outcome. Questions are boxes; outcomes are icons or pills, so the two differ by shape.
"""
from __future__ import annotations

from . import shapes
from . import style as S
from . import textmetrics

KIND = "ladder"

MAX_RUNGS = 6
MAX_QUESTION_WORDS = 9
MAX_ANSWER_WORDS = 3

Q_W = 172             # every question box has this width
Q_LINES = 3
OUT_W = 136           # widest outcome label
BRANCH_MIN = 64       # shortest branch arrow
ROW_GAP = 42          # between two rungs: room for the spine arrow and its label


def _outcomes(spec: dict) -> list:
    return [(f"rung {i}", r["then"]) for i, r in enumerate(spec.get("rungs", []), 1)] + [("else", spec["else"])]


def lint_spec(spec: dict, icons: dict) -> list:
    issues = shapes.common_issues(spec)
    rungs = spec.get("rungs", [])
    if len(rungs) > MAX_RUNGS:
        issues.append(shapes.issue("error", "limit-rungs", f"{len(rungs)} rungs; the limit is {MAX_RUNGS}. Split the decision."))
    for i, rung in enumerate(rungs, 1):
        issues += shapes.label_issues(f"rung {i}: question", rung["q"], MAX_QUESTION_WORDS, question=True)
        for key in ("answer", "next"):
            if key in rung:
                issues += shapes.label_issues(f"rung {i}: {key!r}", rung[key], MAX_ANSWER_WORDS)
        if rung.get("answer", "Yes").strip().lower() == rung.get("next", "No").strip().lower():
            issues.append(shapes.issue("error", "answers-equal", f"rung {i}: both answers read {rung.get('answer', 'Yes')!r}"))
    for name, outcome in _outcomes(spec):
        issues += shapes.label_issues(f"{name}: outcome", outcome["label"], S.MAX_LABEL_WORDS)
        issues += shapes.icon_issues(f"{name}: outcome", outcome.get("icon"), icons)
    issues += shapes.emph_issues(sum(1 for _name, o in _outcomes(spec) if o.get("emph")))
    return issues


def _outcome_node(m: dict, ident: str, cx: float, top: float, emph) -> dict:
    if m["icon"]:
        return shapes.place(m, ident, cx, top, emph=emph)
    return shapes.place(m, ident, cx, top, emph=emph, rx=m["h"] / 2, emph_fill=True)


def build_scene(spec: dict) -> dict:
    rungs = spec["rungs"]
    questions = [shapes.measure(r["q"], Q_W, width=Q_W) for r in rungs]
    outs = [shapes.measure(r["then"]["label"], OUT_W, r["then"].get("icon")) for r in rungs]
    last = shapes.measure(spec["else"]["label"], Q_W, spec["else"].get("icon"))
    pill_w = max([m["w"] for m in outs if not m["icon"]], default=0)
    for m in outs:
        if not m["icon"]:
            m["w"] = pill_w                      # all pills share one width, so the column reads as a column
    answers = [r.get("answer", "Yes") for r in rungs]
    branch = max([BRANCH_MIN] + [textmetrics.text_width(a, S.EDGE_FS) + 26 for a in answers])

    # a highlighted icon gets a ring 6 units outside its box; keep that inside the canvas
    ring = any(o.get("emph") and o.get("icon") for _name, o in _outcomes(spec))
    margin = S.MARGIN + (6 if ring else 0)
    spine = margin + Q_W / 2
    out_w = max(m["w"] for m in outs)
    out_cx = margin + Q_W + S.PORT_GAP + branch + S.PORT_GAP + out_w / 2
    width = out_cx + out_w / 2 + margin

    nodes, edges = [], []
    y = margin
    prev = None
    for i, (rung, qm, om) in enumerate(zip(rungs, questions, outs), 1):
        up = max(qm["h"] / 2, shapes.anchor_y(om))
        cy = y + up
        q = shapes.place(qm, f"q{i}", spine, cy - qm["h"] / 2, max_lines=Q_LINES)
        out = _outcome_node(om, f"a{i}", out_cx, cy - shapes.anchor_y(om), rung["then"].get("emph"))
        nodes += [q, out]
        if prev is not None:
            a, b = prev["ports"]["bottom"], q["ports"]["top"]
            label = shapes.v_label(rungs[i - 2].get("next", "No"), spine, (a[1] + b[1]) / 2 - 3)
            edges.append(shapes.edge(len(edges), prev["id"], q["id"], [a, b], label, sides=("bottom", "top")))
        a, b = q["ports"]["right"], out["ports"]["left"]
        if om["icon"] and rung["then"].get("emph"):
            b = (out["bbox"][0] - 5, b[1])          # stop on the highlight ring, not inside it
        label = shapes.h_label(answers[i - 1], (a[0] + b[0] - S.ARROW_LEN) / 2, cy)
        edges.append(shapes.edge(len(edges), q["id"], out["id"], [a, b], label, emph=rung["then"].get("emph"),
                                 sides=("right", "left")))
        y = max(q["bbox"][1] + q["bbox"][3], out["bbox"][1] + out["bbox"][3]) + ROW_GAP
        prev = q
    end = _outcome_node(last, "else", spine, y, spec["else"].get("emph"))
    nodes.append(end)
    a, b = prev["ports"]["bottom"], end["ports"]["top"]
    label = shapes.v_label(rungs[-1].get("next", "No"), spine, (a[1] + b[1]) / 2 - 3)
    edges.append(shapes.edge(len(edges), prev["id"], "else", [a, b], label, emph=spec["else"].get("emph"),
                             sides=("bottom", "top")))
    height = end["bbox"][1] + end["bbox"][3] + margin
    return shapes.scene(KIND, spec["id"], width, height, nodes, edges)
