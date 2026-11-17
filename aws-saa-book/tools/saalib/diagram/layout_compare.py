"""The "compare" kind: two or three small arch panels side by side.

Each panel is laid out and linted as its own arch figure. The build writes one SVG per panel
(<id>.p1.svg, ...) and a combined file (<id>.svg) with the panels in a row. On the web the panels
are separate <svg> elements in a wrapper that stacks them when the screen is narrow.
"""
from __future__ import annotations

from . import arch
from . import lint
from . import shapes
from . import style as S
from . import textmetrics

KIND = "compare"

MIN_PANELS = 2
MAX_PANELS = 3
MAX_PANEL_NODES = 6
MAX_PANEL_EDGES = 7
MAX_HEAD_WORDS = 4
PANEL_GAP = 28
HEAD_H = 22           # panel heading band above each panel


def _as_arch(spec: dict, number: int, panel: dict) -> dict:
    return {
        "id": f"{spec['id']}-p{number}", "kind": "arch", "size": "s", "title": panel["label"],
        "claim": spec.get("claim", ""), "alt": spec.get("alt", ""),
        "cols": panel["cols"], "rows": panel["rows"], "flow": panel.get("flow", "down"),
        "groups": panel.get("groups", []), "nodes": panel["nodes"], "edges": panel.get("edges", []),
    }


def lint_spec(spec: dict, icons: dict) -> list:
    issues = shapes.common_issues(spec)
    panels = spec.get("panels", [])
    if not MIN_PANELS <= len(panels) <= MAX_PANELS:
        issues.append(shapes.issue("error", "limit-panels", f"{len(panels)} panels; a comparison has {MIN_PANELS} or {MAX_PANELS}"))
    emph = 0
    for number, panel in enumerate(panels, 1):
        name = f"panel {number}"
        issues += shapes.label_issues(f"{name}: heading", panel["label"], MAX_HEAD_WORDS)
        if len(panel["nodes"]) > MAX_PANEL_NODES:
            issues.append(shapes.issue("error", "limit-nodes", f"{name}: {len(panel['nodes'])} nodes; a panel holds "
                                       f"{MAX_PANEL_NODES} at most"))
        if len(panel.get("edges", [])) > MAX_PANEL_EDGES:
            issues.append(shapes.issue("error", "limit-edges", f"{name}: {len(panel['edges'])} edges; a panel holds "
                                       f"{MAX_PANEL_EDGES} at most"))
        if any("step" in e or "say" in e for e in panel.get("edges", [])):
            issues.append(shapes.issue("error", "compare-step", f"{name}: panels take edge labels, not step numbers"))
        emph += sum(1 for x in panel["nodes"] + panel.get("edges", []) if x.get("emph"))
        for item in lint.lint_spec(_as_arch(spec, number, panel), icons):
            # one Region or account box per panel is the point of many comparisons
            if item["code"] in ("claim", "emph-many", "lone-region", "lone-account"):
                continue
            issues.append(dict(item, msg=f"{name}: {item['msg']}"))
    return issues + shapes.emph_issues(emph)


def build_scene(spec: dict) -> dict:
    panels = []
    x = S.MARGIN
    for number, panel in enumerate(spec["panels"], 1):
        sub = shapes.make_room_for_rings(arch.build_scene(_as_arch(spec, number, panel)))
        head_w = textmetrics.text_width(panel["label"], S.NODE_FS, bold=True)
        panels.append({"label": panel["label"], "alt": panel.get("alt"), "scene": sub, "x": x, "y": S.MARGIN + HEAD_H,
                       "head_y": S.MARGIN + 13, "head_w": head_w, "w": max(sub["w"], head_w)})
        x += max(sub["w"], head_w) + PANEL_GAP
    width = x - PANEL_GAP + S.MARGIN
    height = S.MARGIN + HEAD_H + max(p["scene"]["h"] for p in panels) + S.MARGIN
    out = shapes.scene(KIND, spec["id"], width, height)
    out["panels"] = panels
    out["phone_w"] = max(p["scene"]["w"] for p in panels)
    return out


def lint_scene(scene: dict, spec: dict) -> tuple:
    """Each panel gets the full geometry lint; a panel must fit a phone, the row must fit its size."""
    issues = []
    stats = {"width": scene["w"], "height": scene["h"], "nodes": 0, "edges": 0, "crossings": 0, "scrolls_on_phone": False}
    for number, panel in enumerate(scene["panels"], 1):
        sub_issues, sub = lint.lint_scene(panel["scene"], "s")
        issues += [dict(i, msg=f"panel {number}: {i['msg']}") for i in sub_issues]
        if panel["head_w"] > panel["scene"]["w"]:
            issues.append(shapes.issue("error", "text-overflow", f"panel {number}: the heading {panel['label']!r} is wider "
                                       f"than the panel"))
        for key in ("nodes", "edges", "crossings"):
            stats[key] += sub[key]
        stats["scrolls_on_phone"] = stats["scrolls_on_phone"] or sub["scrolls_on_phone"]
    size = spec.get("size", "m")
    budget = S.SIZE_BUDGET.get(size, S.SIZE_BUDGET["m"])
    if scene["w"] > budget:
        issues.append(shapes.issue("warn", "size-budget", f"the row of panels is {scene['w']} wide; size {size!r} allows "
                                   f"{budget}. The panels will stack on a desktop too."))
    return issues, stats
