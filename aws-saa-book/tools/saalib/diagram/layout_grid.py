"""Grid layout for the "arch" kind.

Columns and rows of cells. Groups are rectangles of cells that nest as a tree. Every nested
border adds one lane of space to the gutter it sits in, and every group gets a label band at
its top. Between the border stacks of two neighbouring columns (or rows) lies the routing gutter;
its mid-line is the channel that edges use.

    x:  margin | [outer gutter] | borders | column 0 | borders | gutter 1 | borders | column 1 | ...
"""
from __future__ import annotations

import re

from . import style as S
from . import textmetrics

_RE_CELL = re.compile(r"^([A-L])(\d{1,2})$")


class LayoutError(ValueError):
    """The spec cannot be laid out (bad cell, group that does not nest, ...)."""


def parse_cells(text: str):
    """"B2" or "A2:D5" -> (c0, r0, c1, r1), zero-based and inclusive."""
    parts = text.split(":")
    cells = []
    for part in parts:
        match = _RE_CELL.match(part)
        if not match:
            raise LayoutError(f"bad cell {text!r}")
        cells.append((ord(match.group(1)) - 65, int(match.group(2)) - 1))
    (c0, r0), (c1, r1) = cells[0], cells[-1]
    if c1 < c0 or r1 < r0:
        raise LayoutError(f"range {text!r} must run from the top-left cell to the bottom-right cell")
    return c0, r0, c1, r1


def _contains(outer, inner) -> bool:
    return outer[0] <= inner[0] and outer[1] <= inner[1] and outer[2] >= inner[2] and outer[3] >= inner[3]


def _disjoint(a, b) -> bool:
    return a[2] < b[0] or b[2] < a[0] or a[3] < b[1] or b[3] < a[1]


def group_tree(spec: dict) -> list:
    """Validate nesting and return the groups with cells, parent, depth and border levels."""
    cols, rows = spec["cols"], spec["rows"]
    groups = []
    by_id = {}
    for raw in spec.get("groups", []):
        cells = parse_cells(raw["cells"])
        if cells[2] >= cols or cells[3] >= rows:
            raise LayoutError(f"group {raw['id']!r}: cells {raw['cells']} lie outside the {cols}x{rows} grid")
        if raw["id"] in by_id:
            raise LayoutError(f"duplicate group id {raw['id']!r}")
        group = {"id": raw["id"], "type": raw["type"], "label": raw["label"], "cells": cells,
                 "parent": raw.get("in"), "children": []}
        groups.append(group)
        by_id[group["id"]] = group
    for group in groups:
        parent = group["parent"]
        if parent is None:
            continue
        if parent not in by_id:
            raise LayoutError(f"group {group['id']!r}: \"in\" names an unknown group {parent!r}")
        if not _contains(by_id[parent]["cells"], group["cells"]):
            raise LayoutError(f"group {group['id']!r} is not inside its parent {parent!r}")
        by_id[parent]["children"].append(group)

    def ancestors(group):
        seen = []
        cur = group
        while cur["parent"] is not None:
            cur = by_id[cur["parent"]]
            if cur in seen or cur is group:
                raise LayoutError(f"group {group['id']!r}: \"in\" forms a loop")
            seen.append(cur)
        return seen

    for group in groups:
        group["depth"] = len(ancestors(group))
    for i, a in enumerate(groups):
        for b in groups[i + 1:]:
            if _disjoint(a["cells"], b["cells"]):
                continue
            if a in ancestors(b) or b in ancestors(a):
                continue
            raise LayoutError(f"groups {a['id']!r} and {b['id']!r} overlap; one must be \"in\" the other "
                              f"(groups that cross each other are not supported)")

    def level(group, side):
        idx = {"left": 0, "top": 1, "right": 2, "bottom": 3}[side]
        best = 0
        for child in group["children"]:
            if child["cells"][idx] == group["cells"][idx]:
                best = max(best, level(child, side))
        return best + 1

    for group in groups:
        group["level"] = {side: level(group, side) for side in ("left", "top", "right", "bottom")}
    return groups


def _side_off(level: int) -> float:
    return S.GROUP_IN + S.GROUP_STEP * (level - 1)


def _top_off(level: int) -> float:
    return S.GROUP_TOP_IN + S.GROUP_BAND * level


def _gap(base: float, tracks: int, outer: bool) -> float:
    if outer and tracks <= 0:
        return 0.0
    return max(base, 22 + S.TRACK * (max(tracks, 1) - 1))


def layout(spec: dict, cell_w: float = None, vtracks: dict = None, htracks: dict = None) -> dict:
    """Compute coordinates of columns, rows, channels, groups and nodes.

    vtracks / htracks: channel index -> number of parallel edge tracks the gutter must hold.
    Channel k lies before column (or row) k; channel 0 and channel cols (rows) are the outer ones
    and take no space unless an edge uses them.
    """
    cols, rows = spec["cols"], spec["rows"]
    cell_w = cell_w or S.CELL_W
    vtracks = vtracks or {}
    htracks = htracks or {}
    groups = group_tree(spec)

    left = [0.0] * cols
    right = [0.0] * cols
    top = [0.0] * rows
    bottom = [0.0] * rows
    for g in groups:
        c0, r0, c1, r1 = g["cells"]
        left[c0] = max(left[c0], _side_off(g["level"]["left"]))
        right[c1] = max(right[c1], _side_off(g["level"]["right"]))
        top[r0] = max(top[r0], _top_off(g["level"]["top"]))
        bottom[r1] = max(bottom[r1], _side_off(g["level"]["bottom"]))

    # ---- columns
    col_l, col_r, vx = [], [], []
    x = S.MARGIN
    for c in range(cols + 1):
        gap = _gap(S.COL_GAP, vtracks.get(c, 0), outer=c in (0, cols))
        vx.append(x + gap / 2 if gap else (x - S.MARGIN if c == 0 else x + S.MARGIN))
        x += gap
        if c == cols:
            break
        x += left[c]
        col_l.append(x)
        x += cell_w
        col_r.append(x)
        x += right[c]
    width = x + S.MARGIN

    # ---- nodes: wrap labels first, because row heights depend on the line count
    nodes = []
    seen = set()
    for raw in spec["nodes"]:
        cells = parse_cells(raw["at"])
        if cells[2] >= cols or cells[3] >= rows:
            raise LayoutError(f"node {raw['id']!r}: cell {raw['at']} lies outside the {cols}x{rows} grid")
        if raw["id"] in seen:
            raise LayoutError(f"duplicate node id {raw['id']!r}")
        seen.add(raw["id"])
        for g in groups:
            if not _disjoint(g["cells"], cells) and not _contains(g["cells"], cells):
                raise LayoutError(f"node {raw['id']!r} at {raw['at']} lies half inside group {g['id']!r}")
        span = col_r[cells[2]] - col_l[cells[0]]
        max_w = span - 6
        icon = raw.get("icon")
        avail = max_w if icon else max_w - 20
        lines = textmetrics.wrap(raw["label"], S.NODE_FS, avail)
        widths = [textmetrics.text_width(line, S.NODE_FS) for line in lines]
        if icon:
            height = S.ICON + S.LABEL_GAP + S.NODE_LH * len(lines) + 1
        else:
            height = max(S.BOX_H, S.NODE_LH * len(lines) + 16)
        nodes.append({"id": raw["id"], "icon": icon, "label": raw["label"], "cells": cells,
                      "emph": bool(raw.get("emph")), "lines_text": lines, "line_widths": widths,
                      "max_text_w": avail, "h": height})

    # ---- rows
    row_h = []
    for r in range(rows):
        heights = [n["h"] for n in nodes if n["cells"][1] == r and n["cells"][3] == r]
        row_h.append(max(heights) if heights else S.ICON + S.LABEL_GAP + S.NODE_LH + 1)
    row_t, row_b, hy = [], [], []
    y = S.MARGIN
    for r in range(rows + 1):
        gap = _gap(S.ROW_GAP, htracks.get(r, 0), outer=r in (0, rows))
        hy.append(y + gap / 2 if gap else (y - S.MARGIN if r == 0 else y + S.MARGIN))
        y += gap
        if r == rows:
            break
        y += top[r]
        row_t.append(y)
        y += row_h[r]
        row_b.append(y)
        y += bottom[r]
    height = y + S.MARGIN

    # ---- group rectangles
    for g in groups:
        c0, r0, c1, r1 = g["cells"]
        x0 = col_l[c0] - _side_off(g["level"]["left"])
        x1 = col_r[c1] + _side_off(g["level"]["right"])
        y0 = row_t[r0] - _top_off(g["level"]["top"])
        y1 = row_b[r1] + _side_off(g["level"]["bottom"])
        g.update({"x": x0, "y": y0, "w": x1 - x0, "h": y1 - y0})
        g["label_w"] = textmetrics.text_width(g["label"], S.GROUP_FS)
        place_group_label(g, "start")

    # ---- node geometry
    for n in nodes:
        c0, r0, c1, r1 = n["cells"]
        cx = (col_l[c0] + col_r[c1]) / 2
        if r0 == r1:
            ty = row_t[r0]
        else:
            ty = (row_t[r0] + row_b[r1]) / 2 - n["h"] / 2
        text_w = max(n["line_widths"]) if n["line_widths"] else 0
        lines = []
        if n["icon"]:
            ix = cx - S.ICON / 2
            n["icon_box"] = (ix, ty, S.ICON, S.ICON)
            n["box"] = None
            w = max(S.ICON, text_w)
            n["bbox"] = (cx - w / 2, ty, w, n["h"])
            base = ty + S.ICON + S.LABEL_GAP + 12
            for i, (text, lw) in enumerate(zip(n["lines_text"], n["line_widths"])):
                lines.append({"text": text, "x": cx, "y": base + i * S.NODE_LH, "w": lw})
            mid = ty + S.ICON / 2
            # a highlighted icon gets a ring close around the icon; arrows stop at the ring
            pad = S.EMPH_PAD if n["emph"] else 0
            n["ring"] = (ix - pad, ty - pad, S.ICON + 2 * pad, S.ICON + 2 * pad) if pad else None
            if pad:
                w = max(w, S.ICON + 2 * pad)
                n["bbox"] = (cx - w / 2, ty - pad, w, n["h"] + pad)
            n["ports"] = {"top": (cx, ty - pad - S.PORT_GAP), "bottom": (cx, ty + n["h"] + S.PORT_GAP),
                          "left": (ix - pad - S.PORT_GAP, mid), "right": (ix + S.ICON + pad + S.PORT_GAP, mid)}
            n["port_span"] = {"top": S.ICON / 2 - 6, "bottom": S.ICON / 2 - 6,
                              "left": S.ICON / 2 - 8, "right": S.ICON / 2 - 8}
            n["label_box"] = (cx - text_w / 2, ty + S.ICON + S.LABEL_GAP, text_w, S.NODE_LH * len(lines))
        else:
            w = min(n["max_text_w"] + 20, max(text_w + 24, 72))
            bx = cx - w / 2
            n["icon_box"] = None
            n["box"] = (bx, ty, w, n["h"])
            n["bbox"] = (bx, ty, w, n["h"])
            first = ty + n["h"] / 2 - S.NODE_LH * (len(n["lines_text"]) - 1) / 2 + 4.5
            for i, (text, lw) in enumerate(zip(n["lines_text"], n["line_widths"])):
                lines.append({"text": text, "x": cx, "y": first + i * S.NODE_LH, "w": lw})
            mid = ty + n["h"] / 2
            n["ports"] = {"top": (cx, ty - S.PORT_GAP), "bottom": (cx, ty + n["h"] + S.PORT_GAP),
                          "left": (bx - S.PORT_GAP, mid), "right": (bx + w + S.PORT_GAP, mid)}
            n["port_span"] = {"top": w / 2 - 8, "bottom": w / 2 - 8, "left": n["h"] / 2 - 8, "right": n["h"] / 2 - 8}
            n["label_box"] = (cx - text_w / 2, lines[0]["y"] - 12, text_w, S.NODE_LH * len(lines)) if lines else None
        n["cx"] = cx
        n["shapes"] = [r for r in (n["icon_box"], n["box"], n["label_box"] if n["icon"] else None, n.get("ring")) if r]
        n["lines"] = lines

    return {"w": width, "h": height, "cols": cols, "rows": rows, "cell_w": cell_w,
            "col_l": col_l, "col_r": col_r, "row_t": row_t, "row_b": row_b, "vx": vx, "hy": hy,
            "groups": groups, "nodes": nodes}


def place_group_label(group: dict, anchor: str) -> None:
    """Put the group label in its band, left ("start") or right ("end") aligned."""
    y = group["y"] + (S.GROUP_BAND - 14) / 2
    if anchor == "start":
        x = group["x"] + S.GROUP_LABEL_INSET
        text_x = x
    else:
        x = group["x"] + group["w"] - S.GROUP_LABEL_INSET - group["label_w"]
        text_x = group["x"] + group["w"] - S.GROUP_LABEL_INSET
    group["label_anchor"] = anchor
    group["label_box"] = (x, y, group["label_w"], 14)
    group["label_pos"] = (text_x, y + 11)
