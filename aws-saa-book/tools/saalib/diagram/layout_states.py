"""The "states" kind: a lifecycle. States sit on a grid like arch nodes and are drawn as pills;
a final state has a double border. Transitions are routed and labelled by the arch router.
"""
from __future__ import annotations

from . import arch
from . import lint
from . import shapes

KIND = "states"

MAX_STATES = 8
MAX_TRANSITIONS = 12


def _as_arch(spec: dict) -> dict:
    """The same figure as an arch spec without icons and groups."""
    return {
        "id": spec["id"], "kind": "arch", "title": spec.get("title", ""), "claim": spec.get("claim", ""),
        "alt": spec.get("alt", ""), "cols": spec["cols"], "rows": spec["rows"], "flow": spec.get("flow", "down"),
        "groups": [],
        "nodes": [{"id": s["id"], "label": s["label"], "at": s["at"], "emph": bool(s.get("emph"))} for s in spec["states"]],
        "edges": [dict(t) for t in spec.get("transitions", [])],
    }


def lint_spec(spec: dict, icons: dict) -> list:
    issues = []
    states = spec.get("states", [])
    transitions = spec.get("transitions", [])
    if len(states) > MAX_STATES:
        issues.append(shapes.issue("error", "limit-states", f"{len(states)} states; the limit is {MAX_STATES}. Split the figure."))
    if len(transitions) > MAX_TRANSITIONS:
        issues.append(shapes.issue("error", "limit-transitions", f"{len(transitions)} transitions; the limit is "
                                   f"{MAX_TRANSITIONS}. Split the figure."))
    for item in lint.lint_spec(_as_arch(spec), {}):
        if item["code"] in ("limit-nodes", "limit-edges"):
            continue
        item["msg"] = item["msg"].replace("node", "state").replace("edge", "transition")
        issues.append(item)
    linked = {t[end] for t in transitions for end in ("from", "to")}
    for s in states:
        if len(states) > 1 and s["id"] not in linked:
            issues.append(shapes.issue("error", "state-unlinked", f"state {s['id']!r} has no transition"))
        if s.get("final") and any(t["from"] == s["id"] for t in transitions):
            issues.append(shapes.issue("error", "final-leaves", f"state {s['id']!r} is final but a transition leaves it"))
    return issues


def build_scene(spec: dict) -> dict:
    scene = arch.build_scene(_as_arch(spec))
    scene["kind"] = KIND
    final = {s["id"] for s in spec["states"] if s.get("final")}
    for node in scene["nodes"]:
        node["rx"] = node["bbox"][3] / 2
        node["emph_fill"] = True
        node["inner"] = node["id"] in final
    return scene
