"""The "raw" kind: the escape hatch. A hand-written SVG next to the spec (diagrams/src/<id>.svg).

The tool does not lay anything out. It checks that the drawing uses only the shared classes (so it
follows the themes like every other figure), carries no colours, styles, ids, scripts or rotated
parts of its own, and stays inside its viewBox and the size limits. Icons are
<use href="#ic-NAME" x y width height>; the build embeds them in the standalone file.
"""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

from . import shapes
from . import style as S
from . import svg
from . import textmetrics

KIND = "raw"
WANTS_BASE_DIR = True

MAX_W = S.SIZE_BUDGET["l"]
MAX_H = 1600
MAX_TEXT_WORDS = 6

DRAWN = {"rect", "path", "line", "circle", "ellipse", "polygon", "polyline", "text"}
ALLOWED = DRAWN | {"g", "tspan", "use"}
ATTRS = {"class", "x", "y", "x1", "y1", "x2", "y2", "cx", "cy", "r", "rx", "ry", "width", "height", "d", "points",
         "transform", "text-anchor", "dx", "dy", "href"}
_RE_TRANSLATE = re.compile(r"^\s*translate\(\s*-?[\d.]+(?:[\s,]+-?[\d.]+)?\s*\)\s*$")
_RE_VIEWBOX = re.compile(r"^\s*0[\s,]+0[\s,]+(\d+(?:\.\d+)?)[\s,]+(\d+(?:\.\d+)?)\s*$")


def source_path(spec: dict, base_dir) -> Path:
    return Path(base_dir) / spec.get("svg", f"{spec['id']}.svg")


def _local(name: str) -> str:
    return name.rsplit("}", 1)[-1]


def _num(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _convert(el, in_text: bool) -> dict:
    tag = _local(el.tag)
    keep = tag in ("text", "tspan")
    children = [_convert(child, keep) for child in el]
    text = (el.text or "") if keep else ""
    if tag == "text":
        text = text.lstrip()
        if not children:
            text = text.rstrip()
    return {"tag": tag, "attrs": [(_local(k), v) for k, v in el.attrib.items()], "text": text,
            "tail": (el.tail or "") if in_text else "", "children": children}


def _load(spec: dict, base_dir):
    """Returns (nodes, (w, h), issues). nodes is None when the file cannot be used at all."""
    path = source_path(spec, base_dir)
    if not path.is_file():
        return None, None, [shapes.issue("error", "ref-missing", f"{path.name} not found next to the spec")]
    raw = path.read_text(encoding="utf-8", errors="replace")
    if re.search(r"<!(DOCTYPE|ENTITY)", raw, re.I):
        return None, None, [shapes.issue("error", "ref-xml", f"{path.name}: DOCTYPE and ENTITY declarations are not allowed")]
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as exc:
        return None, None, [shapes.issue("error", "ref-xml", f"{path.name} is not well-formed XML: {exc}")]
    match = _RE_VIEWBOX.match(root.attrib.get("viewBox", ""))
    if _local(root.tag) != "svg" or not match:
        return None, None, [shapes.issue("error", "ref-root", f"{path.name}: the root must be <svg viewBox=\"0 0 W H\">")]
    size = (float(match.group(1)), float(match.group(2)))
    return [_convert(child, False) for child in root], size, []


def _walk(nodes: list, moved: bool = False):
    for node in nodes:
        yield node, moved
        shifted = moved or any(k == "transform" for k, _v in node["attrs"])
        yield from _walk(node["children"], shifted)


def _box(node: dict):
    """Bounding box of the simple shapes; None when it cannot be told from the attributes."""
    a = dict(node["attrs"])
    tag = node["tag"]
    if tag in ("rect", "use"):
        vals = [_num(a.get(k, 0 if k in ("x", "y") else None)) for k in ("x", "y", "width", "height")]
        return None if None in vals else tuple(vals)
    if tag == "line":
        vals = [_num(a.get(k, 0)) for k in ("x1", "y1", "x2", "y2")]
        if None in vals:
            return None
        return (min(vals[0], vals[2]), min(vals[1], vals[3]), abs(vals[2] - vals[0]), abs(vals[3] - vals[1]))
    if tag == "circle":
        cx, cy, r = _num(a.get("cx", 0)), _num(a.get("cy", 0)), _num(a.get("r"))
        return None if None in (cx, cy, r) else (cx - r, cy - r, 2 * r, 2 * r)
    if tag == "text":
        x, y = _num(a.get("x", 0)), _num(a.get("y", 0))
        return None if None in (x, y) else (x, y - 11, 0, 14)
    return None


def _text_of(node: dict) -> str:
    return node["text"] + "".join(_text_of(c) + c["tail"] for c in node["children"])


TEXT_CLASSES = {"dg-gl": (S.GROUP_FS, False, "start"), "dg-nl": (S.NODE_FS, False, "middle"), "dg-el": (S.EDGE_FS, False, "start"),
                "dg-bt": (S.BADGE_FS, True, "middle"), "dg-mt": (S.GROUP_FS, False, "start"), "dg-evl": (S.EDGE_FS, True, "start"),
                "dg-ph": (S.NODE_FS, True, "start")}
_RE_SHIFT = re.compile(r"^\s*translate\(\s*(-?[\d.]+)(?:[\s,]+(-?[\d.]+))?\s*\)\s*$")


def _text_lines(nodes: list, dx: float = 0.0, dy: float = 0.0):
    """Every line of text of the drawing as (text, (x, y, width, height)) in viewBox units (gate-break 58).

    A <tspan> with x, y or dy starts a new line. The width comes from the font table of the renderer and the
    font size of the shared class, so two labels in one place and a label wider than the drawing can be seen."""
    for node in nodes:
        attrs = dict(node["attrs"])
        shift = _RE_SHIFT.match(attrs.get("transform", ""))
        ox = dx + (float(shift.group(1)) if shift else 0.0)
        oy = dy + (float(shift.group(2) or 0) if shift else 0.0)
        if node["tag"] != "text":
            yield from _text_lines(node["children"], ox, oy)
            continue
        x, y = _num(attrs.get("x", 0)), _num(attrs.get("y", 0))
        if x is None or y is None:
            continue
        size, bold, anchor = next((TEXT_CLASSES[c] for c in attrs.get("class", "").split() if c in TEXT_CLASSES),
                                  (S.NODE_FS, False, "start"))
        anchor = attrs.get("text-anchor", anchor)
        lines = [[x, y, node["text"]]]
        for child in node["children"]:
            ca = dict(child["attrs"])
            if any(k in ca for k in ("x", "y", "dy")):
                lines.append([_num(ca.get("x")) if _num(ca.get("x")) is not None else lines[-1][0],
                              _num(ca.get("y")) if _num(ca.get("y")) is not None else lines[-1][1] + (_num(ca.get("dy")) or 0), ""])
            lines[-1][2] += _text_of(child) + child["tail"]
        for lx, ly, text in lines:
            text = " ".join(text.split())
            if not text:
                continue
            width = textmetrics.text_width(text, size, bold)
            left = lx - width / 2 if anchor == "middle" else (lx - width if anchor == "end" else lx)
            yield text, (left + ox, ly - size + oy, width, size * 1.2)


def label_texts(spec: dict, base_dir) -> list:
    """The texts of the drawing, for the number rule that every kind shares."""
    nodes, _size, _problems = _load(spec, base_dir)
    return [text for text, _box in _text_lines(nodes or [])]


def _text_issues(nodes: list, w: float, h: float) -> list:
    issues = []
    lines = list(_text_lines(nodes))
    for text, (x, y, width, height) in lines:
        if x < -0.5 or x + width > w + 0.5 or y < -0.5 or y + height > h + 0.5:
            issues.append(shapes.issue("error", "text-overflow", f"<text> {text!r} is {width:.0f} wide at {x:.0f},{y:.0f}; "
                                       f"it leaves the viewBox ({w:g} x {h:g})"))
    for i, (text_a, a) in enumerate(lines):
        for text_b, b in lines[i + 1:]:
            if min(a[0] + a[2], b[0] + b[2]) - max(a[0], b[0]) > 1 and min(a[1] + a[3], b[1] + b[3]) - max(a[1], b[1]) > 1:
                issues.append(shapes.issue("error", "label-overlap", f"<text> {text_a!r} overlaps <text> {text_b!r}"))
    return issues


def lint_spec(spec: dict, icons: dict, base_dir) -> list:
    issues = shapes.common_issues(spec)
    nodes, size, problems = _load(spec, base_dir)
    issues += problems
    if nodes is None:
        return issues
    w, h = size
    issues += _text_issues(nodes, w, h)
    if w > MAX_W or h > MAX_H:
        issues.append(shapes.issue("error", "raw-size", f"the viewBox is {w:g} x {h:g}; the limit is {MAX_W} x {MAX_H}"))
    known = svg.known_classes()
    drawn = 0
    for node, moved in _walk(nodes):
        tag = node["tag"]
        attrs = dict(node["attrs"])
        if tag not in ALLOWED:
            issues.append(shapes.issue("error", "raw-element", f"<{tag}> is not allowed (allowed: {', '.join(sorted(ALLOWED))})"))
            continue
        for key, value in node["attrs"]:
            if key in ("fill", "stroke") and value.strip() == "none":
                continue
            if key in ("fill", "stroke", "style", "color", "stop-color"):
                issues.append(shapes.issue("error", "raw-colour", f"<{tag}> sets {key}=\"{value}\"; colours come from the "
                                           f"shared classes only"))
            elif key not in ATTRS or (key == "href" and tag != "use"):
                issues.append(shapes.issue("error", "raw-attr", f"<{tag}> has the attribute {key!r}, which is not allowed"))
        if "transform" in attrs and not _RE_TRANSLATE.match(attrs["transform"]):
            issues.append(shapes.issue("error", "raw-transform", f"<{tag}> transform=\"{attrs['transform']}\": only "
                                       f"translate() is allowed (no rotated or scaled parts)"))
        classes = attrs.get("class", "").split()
        for name in classes:
            if name not in known:
                issues.append(shapes.issue("error", "raw-class", f"<{tag}> uses the class {name!r}, which the shared "
                                           f"stylesheet does not define"))
        if tag in DRAWN:
            drawn += 1
            if not classes:
                issues.append(shapes.issue("error", "raw-class", f"<{tag}> has no class; every drawn element needs a "
                                           f"shared class (for example dg-e, dg-nb, dg-nl)"))
        if tag == "use":
            drawn += 1
            href = attrs.get("href", "")
            box = _box(node)
            if not href.startswith("#ic-"):
                issues.append(shapes.issue("error", "raw-use", f"<use href=\"{href}\">: only icons, href=\"#ic-NAME\""))
            else:
                issues += shapes.icon_issues("<use>", href[4:], icons)
            if box is None or box[2] != box[3] or box[2] <= 0:
                issues.append(shapes.issue("error", "raw-use", f"<use href=\"{href}\"> needs x, y and equal width and height"))
        if tag == "text" and shapes.words(_text_of(node)) > MAX_TEXT_WORDS:
            issues.append(shapes.issue("error", "sentence", f"<text> {_text_of(node)!r} has more than {MAX_TEXT_WORDS} words"))
        box = None if moved or "transform" in attrs else _box(node)
        if box and (box[0] < 0 or box[1] < 0 or box[0] + box[2] > w or box[1] + box[3] > h):
            issues.append(shapes.issue("error", "clip", f"<{tag}> at {box[0]:g},{box[1]:g} lies outside the viewBox"))
    if not drawn:
        issues.append(shapes.issue("error", "raw-empty", "the SVG draws nothing"))
    return issues


def _clean(nodes: list) -> list:
    """Drop what the lint rejects, so that a preview of a failing file cannot carry it either."""
    out = []
    for node in nodes:
        if node["tag"] not in ALLOWED or (node["tag"] == "use" and (
                _box(node) is None or not dict(node["attrs"]).get("href", "").startswith("#ic-"))):
            continue
        attrs = [(k, v) for k, v in node["attrs"]
                 if (k in ATTRS and (k != "href" or node["tag"] == "use")) or (k in ("fill", "stroke") and v.strip() == "none")]
        out.append(dict(node, attrs=attrs, children=_clean(node["children"])))
    return out


def build_scene(spec: dict, base_dir) -> dict:
    nodes, size, _problems = _load(spec, base_dir)
    if nodes is None:                         # lint_spec reports why; never reached through the pipeline
        from . import layout_grid
        raise layout_grid.LayoutError("the raw SVG cannot be read")
    nodes = _clean(nodes)
    out = shapes.scene(KIND, spec["id"], size[0], size[1])
    out["raw"] = nodes
    out["icons"] = sorted({dict(n["attrs"]).get("href", "")[4:] for n, _m in _walk(nodes) if n["tag"] == "use"})
    out["drawn"] = sum(1 for n, _m in _walk(nodes) if n["tag"] in DRAWN or n["tag"] == "use")
    return out


def lint_scene(scene: dict, spec: dict) -> tuple:
    issues = []
    size = spec.get("size", "m")
    budget = S.SIZE_BUDGET.get(size, S.SIZE_BUDGET["m"])
    if scene["w"] > budget:
        issues.append(shapes.issue("warn", "size-budget", f"the drawing is {scene['w']} wide; size {size!r} allows {budget}. "
                                   f"It will scroll on a phone beyond {int(336 / S.MIN_SCALE)}."))
    stats = {"width": scene["w"], "height": scene["h"], "nodes": scene.get("drawn", 0), "edges": 0, "crossings": 0,
             "scrolls_on_phone": scene["w"] * S.MIN_SCALE > 336}
    return issues, stats
