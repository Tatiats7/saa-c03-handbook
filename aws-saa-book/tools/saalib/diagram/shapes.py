"""Building blocks shared by the kinds other than arch (sequence, ladder, states, timeline, compare, raw).

Each kind lays out its own coordinates and returns the same scene shape as arch, so svg.py draws
it and lint.lint_scene checks it. The helpers here make scene parts with the same geometry rules
as layout_grid.py: an icon with its label under it, or a labelled box.
"""
from __future__ import annotations

import re

from . import style as S
from . import textmetrics


# ------------------------------------------------------------------ lint helpers

def issue(level: str, code: str, msg: str) -> dict:
    return {"level": level, "code": code, "msg": msg}


def words(text: str) -> int:
    return len(text.replace("\n", " ").split())


def label_issues(what: str, text: str, max_words: int, question: bool = False) -> list:
    """A label inside the drawing is a few words, never a sentence."""
    text = text.strip()
    end = r"[.!]$" if question else r"[.!?]$"
    if words(text) > max_words or re.search(end, text):
        return [issue("error", "sentence", f"{what}: {text!r} reads as a sentence "
                      f"(at most {max_words} words, no full stop)")]
    return []


def one_sentence(text: str) -> bool:
    text = text.strip()
    # gate-break 60: a second sentence can also start with a small letter, a digit or a quote
    return bool(re.search(r"[.!?]$", text)) and not re.search(r"[.!?][\"')]?\s+\S", text)


def common_issues(spec: dict) -> list:
    """Checks that every kind shares: the claim is exactly one sentence."""
    claim = spec.get("claim", "")
    if claim.strip() and not one_sentence(claim):
        return [issue("error", "claim", "the claim must be exactly one sentence ending with a full stop")]
    return []


_DEFAULT_UNITS = ("KB MB GB TB PB KiB MiB GiB TiB Kbps Mbps Gbps IOPS ms milliseconds seconds second minutes minute hours hour days "
                  "day weeks week months month years year % percent vCPU vCPUs nines").split()


def _label_number_re():
    """A number followed by a unit or a count noun of SPEC.json (lint.number_with_unit), or a currency amount."""
    units, nouns = list(_DEFAULT_UNITS), []
    try:
        from .. import common
        nwu = ((common.read_json(common.STYLE_DIR / "SPEC.json") or {}).get("lint") or {}).get("number_with_unit") or {}
        units = list(nwu.get("units") or units)
        nouns = list(nwu.get("count_nouns") or [])
    except Exception:
        pass
    unit = "|".join(re.escape(u) for u in sorted(units, key=len, reverse=True))
    noun = "|".join(r"\s+".join(re.escape(p) for p in n.split()) for n in sorted(nouns, key=len, reverse=True))
    tail = "(?:" + unit + ")" + ("|(?i:" + noun + ")" if noun else "")
    return re.compile(r"\$\d[\d,]*(?:\.\d+)?|(?<![A-Za-z0-9.\-/:$])\d[\d,]*(?:\.\d+)?[ \-]?(?:" + tail + r")(?![A-Za-z0-9])")


def _texts(node, keys: tuple, skip: tuple = ()) -> list:
    """Every string that stands under one of `keys`, anywhere in the spec."""
    out = []
    if isinstance(node, dict):
        for key, value in node.items():
            if key in skip:
                continue
            if key in keys and isinstance(value, str):
                out.append(value)
            elif key in keys and isinstance(value, list):
                out += [v for v in value if isinstance(v, str)]
            else:
                out += _texts(value, keys, skip)
    elif isinstance(node, list):
        for value in node:
            out += _texts(value, keys, skip)
    return out


def _norm(text: str) -> str:
    return " ".join(text.replace("\n", " ").lower().split())


def number_issues(spec: dict, extra_labels=()) -> list:
    """TOOLS-rules R2 (gate-break 59): a number with a unit in a label repeats a value that stands in the claim
    or in a `say` sentence. The chapter lint grounds claim and say; a label is read by no other rule."""
    told = _norm(" ".join(_texts(spec, ("claim", "say")))).replace(" ", "")
    issues = []
    labels = _texts(spec, ("label", "title", "heading", "text", "note", "labels"), skip=("claim", "say", "alt")) + list(extra_labels)
    number = _label_number_re()
    for label in labels:
        for match in number.finditer(label.replace("\n", " ")):
            value = _norm(match.group(0)).replace(" ", "")
            if value not in told:
                issues.append(issue("error", "label-number", f"label {label!r} holds {match.group(0)!r}, which stands in neither "
                                    "the claim nor a \"say\" sentence; a figure states no number of its own"))
    return issues


def icon_issues(what: str, icon, icons: dict) -> list:
    if icon and icon not in icons:
        return [issue("error", "icon-unknown", f"{what}: no icon named {icon!r} (see: diagram icons --list)")]
    return []


def duplicates(ids: list) -> list:
    return sorted({i for i in ids if ids.count(i) > 1})


def emph_issues(count: int) -> list:
    if count > S.MAX_EMPH:
        return [issue("warn", "emph-many", f"{count} highlighted items; the highlight is for the one thing the figure is about")]
    return []


# ------------------------------------------------------------------ nodes

def measure(label: str, max_w: float, icon: str = None, min_w: float = 72, min_h: float = S.BOX_H,
            width: float = None) -> dict:
    """Wrap a label and return the size of its node. max_w is the widest the node may be."""
    avail = max_w if icon else max_w - 20
    lines = textmetrics.wrap(label, S.NODE_FS, avail)
    widths = [textmetrics.text_width(line, S.NODE_FS) for line in lines]
    text_w = max(widths) if widths else 0
    if icon:
        w, h = max(S.ICON, text_w), S.ICON + S.LABEL_GAP + S.NODE_LH * len(lines) + 1
    else:
        w = width if width is not None else min(max_w, max(text_w + 24, min_w))
        h = max(min_h, S.NODE_LH * len(lines) + 16)
    return {"icon": icon, "label": label, "lines": lines, "widths": widths, "text_w": text_w,
            "avail": avail, "w": w, "h": h}


def anchor_y(m: dict) -> float:
    """Distance from the top of a measured node to the height where side arrows attach."""
    return S.ICON / 2 if m["icon"] else m["h"] / 2


def place(m: dict, ident: str, cx: float, top: float, emph: bool = False, **extra) -> dict:
    """Turn a measured node into a scene node with its top centre at (cx, top)."""
    lines = []
    text_w, h = m["text_w"], m["h"]
    node = {"id": ident, "icon": m["icon"], "label": m["label"], "emph": bool(emph), "max_text_w": m["avail"], "cx": cx}
    if m["icon"]:
        ix = cx - S.ICON / 2
        node["icon_box"] = (ix, top, S.ICON, S.ICON)
        node["box"] = None
        node["bbox"] = (cx - m["w"] / 2, top, m["w"], h)
        base = top + S.ICON + S.LABEL_GAP + 12
        for i, (text, lw) in enumerate(zip(m["lines"], m["widths"])):
            lines.append({"text": text, "x": cx, "y": base + i * S.NODE_LH, "w": lw})
        mid = top + S.ICON / 2
        node["ports"] = {"top": (cx, top - S.PORT_GAP), "bottom": (cx, top + h + S.PORT_GAP),
                         "left": (ix - S.PORT_GAP, mid), "right": (ix + S.ICON + S.PORT_GAP, mid)}
        node["label_box"] = (cx - text_w / 2, top + S.ICON + S.LABEL_GAP, text_w, S.NODE_LH * len(lines))
        node["shapes"] = [node["icon_box"], node["label_box"]]
    else:
        w = m["w"]
        bx = cx - w / 2
        node["icon_box"] = None
        node["box"] = (bx, top, w, h)
        node["bbox"] = (bx, top, w, h)
        first = top + h / 2 - S.NODE_LH * (len(m["lines"]) - 1) / 2 + 4.5
        for i, (text, lw) in enumerate(zip(m["lines"], m["widths"])):
            lines.append({"text": text, "x": cx, "y": first + i * S.NODE_LH, "w": lw})
        mid = top + h / 2
        node["ports"] = {"top": (cx, top - S.PORT_GAP), "bottom": (cx, top + h + S.PORT_GAP),
                         "left": (bx - S.PORT_GAP, mid), "right": (bx + w + S.PORT_GAP, mid)}
        node["label_box"] = (cx - text_w / 2, first - 12, text_w, S.NODE_LH * len(lines))
        node["shapes"] = [node["box"]]
    node["lines"] = lines
    node.update(extra)
    return node


# ------------------------------------------------------------------ edges and texts

def edge(index: int, frm: str, to: str, points: list, label: dict = None, badge: dict = None,
         emph: bool = False, dashed: bool = False, arrow: str = "end", sides=None) -> dict:
    return {"index": index, "from": frm, "to": to, "points": [tuple(p) for p in points], "arrow": arrow,
            "emph": bool(emph), "dashed": bool(dashed), "label": label, "badge": badge,
            "no_room": False, "sides": sides}


def h_label(text: str, cx: float, line_y: float, badge: bool = False) -> dict:
    """Label centred above a horizontal line (same offsets as route._text_box)."""
    w = textmetrics.text_width(text, S.EDGE_FS)
    top = line_y - ((S.BADGE_R + 3) if badge else 4) - S.EDGE_LABEL_H
    return {"text": text, "x": cx, "y": top + 11, "anchor": "middle", "box": (cx - w / 2, top, w, S.EDGE_LABEL_H), "w": w}


def v_label(text: str, x: float, cy: float, off: float = 6) -> dict:
    """Label to the right of a vertical line, centred on cy."""
    w = textmetrics.text_width(text, S.EDGE_FS)
    top = cy - S.EDGE_LABEL_H / 2
    return {"text": text, "x": x + off, "y": top + 11, "anchor": "start", "box": (x + off, top, w, S.EDGE_LABEL_H), "w": w}


def text(value: str, x: float, baseline: float, anchor: str = "start", cls: str = "dg-el",
         size: float = S.EDGE_FS, bold: bool = False) -> dict:
    """A free text item for scene["texts"], with the box the lint checks."""
    w = textmetrics.text_width(value, size, bold)
    left = x if anchor == "start" else (x - w / 2 if anchor == "middle" else x - w)
    return {"text": value, "x": x, "y": baseline, "anchor": anchor, "cls": cls, "box": (left, baseline - 11, w, 14), "w": w}


def _move(rect, dx, dy):
    return None if rect is None else (rect[0] + dx, rect[1] + dy) + tuple(rect[2:])


def make_room_for_rings(sc: dict, ring: float = 7.0) -> dict:
    """Shift and grow a scene so that the highlight ring of every node lies inside the canvas.

    The ring is drawn 6 units outside the node box with a 2 unit stroke."""
    boxes = [n["bbox"] for n in sc.get("nodes", []) if n.get("emph") and not n.get("emph_fill")]
    if not boxes:
        return sc
    dx = max([0.0] + [ring - b[0] for b in boxes])
    dy = max([0.0] + [ring - b[1] for b in boxes])
    grow_x = max([0.0] + [b[0] + b[2] + ring - sc["w"] for b in boxes])
    grow_y = max([0.0] + [b[1] + b[3] + ring - sc["h"] for b in boxes])
    import math
    dx, dy = math.ceil(dx), math.ceil(dy)
    if dx or dy:
        for g in sc.get("groups", []):
            g["x"] += dx
            g["y"] += dy
            g["label_box"] = _move(g["label_box"], dx, dy)
            g["label_pos"] = _move(g["label_pos"], dx, dy)
        for n in sc.get("nodes", []):
            for key in ("bbox", "icon_box", "box", "label_box"):
                n[key] = _move(n.get(key), dx, dy)
            n["shapes"] = [_move(r, dx, dy) for r in n["shapes"]]
            n["ports"] = {k: _move(p, dx, dy) for k, p in n["ports"].items()}
            n["cx"] = n.get("cx", 0) + dx
            for line in n["lines"]:
                line["x"] += dx
                line["y"] += dy
        for e in sc.get("edges", []):
            if e.get("points"):
                e["points"] = [_move(p, dx, dy) for p in e["points"]]
            if e.get("label"):
                e["label"]["x"] += dx
                e["label"]["y"] += dy
                e["label"]["box"] = _move(e["label"]["box"], dx, dy)
            if e.get("badge"):
                e["badge"]["cx"] += dx
                e["badge"]["cy"] += dy
    sc["w"] = int(math.ceil(sc["w"] + dx + grow_x))
    sc["h"] = int(math.ceil(sc["h"] + dy + grow_y))
    return sc


def scene(kind: str, ident: str, w: float, h: float, nodes=None, edges=None, texts=None, decor=None) -> dict:
    import math
    return {"kind": kind, "id": ident, "w": int(math.ceil(w)), "h": int(math.ceil(h)), "groups": [],
            "nodes": nodes or [], "edges": edges or [], "texts": texts or [], "decor": decor or []}
