"""Scene to SVG.

render_standalone(): a complete SVG file. Light palette baked in, opaque ground, icons embedded.
    Used by the Markdown preview, the PDF and Anki.
render_inline(): an <svg> fragment for the web app. Classes bound to the --dg-* tokens, no ids,
    no <style>, transparent ground, icons by <use href="#ic-NAME"> into the shell's sprite.

Arrowheads are explicit polygons (no markers), so dozens of inline diagrams cannot collide.
"""
from __future__ import annotations

import html

from . import style as S
from . import textmetrics
from .style import fmt


# ------------------------------------------------------------------ stylesheet

def _css(color) -> str:
    """color(token) -> CSS value. One template serves both outputs."""
    rules = [
        f".dg{{font-family:{textmetrics.FONT_STACK}}}",
        f".dg-ground{{fill:{color('--dg-ground')}}}",
        ".dg-g{fill:none;stroke-linejoin:round}",
    ]
    for _type, (suffix, token, width, dash, tint, _name) in S.GROUPS.items():
        rule = f".dg-g-{suffix}{{stroke:{color(token)};stroke-width:{fmt(width) if width != 1.25 else '1.25'}"
        if dash:
            rule += f";stroke-dasharray:{dash}"
        if suffix == "region":
            rule += ";stroke-linecap:round"
        if tint:
            rule += f";fill:{color(token)};fill-opacity:.07"
        rules.append(rule + "}")
    ink, edge, emph = color("--dg-ink"), color("--dg-edge"), color("--dg-emph")
    rules += [
        f".dg-gl{{font-size:{S.GROUP_FS}px;fill:{ink}}}",
        f".dg-nl{{font-size:{S.NODE_FS}px;fill:{ink};text-anchor:middle}}",
        f".dg-nb{{fill:{color('--dg-node')};stroke:{edge};stroke-width:1.25}}",
        f".dg-ne{{fill:{emph};fill-opacity:.08;stroke:{emph};stroke-width:2}}",
        f".dg-e{{fill:none;stroke:{edge};stroke-width:{S.EDGE_W};stroke-linejoin:round}}",
        f".dg-e-emph{{stroke:{emph};stroke-width:{S.EDGE_W_EMPH}}}",
        ".dg-e-dash{stroke-dasharray:5 4}",
        f".dg-ah{{fill:{edge}}}",
        f".dg-ah-emph{{fill:{emph}}}",
        f".dg-el{{font-size:{S.EDGE_FS}px;fill:{ink}}}",
        f".dg-el-emph{{fill:{emph}}}",
        f".dg-b{{fill:{edge}}}",
        f".dg-b-emph{{fill:{emph}}}",
        f".dg-bt{{font-size:{S.BADGE_FS}px;font-weight:700;fill:{color('--dg-ground')};text-anchor:middle}}",
    ]
    return "".join(rules)


def _css_kinds(color) -> str:
    """Classes that only the kinds other than arch use. Kept apart so arch files do not change."""
    ink, muted, edge, emph = color("--dg-ink"), color("--dg-muted"), color("--dg-edge"), color("--dg-emph")
    return "".join([
        f".dg-ll{{fill:none;stroke:{muted};stroke-width:1;stroke-dasharray:2 4}}",                 # lifeline, guide
        f".dg-nt{{fill:{color('--dg-node')};stroke:{muted};stroke-width:1;stroke-dasharray:3 3}}",  # note box
        f".dg-nf{{fill:none;stroke:{edge};stroke-width:1.25}}",                                    # inner border, final state
        f".dg-sp{{fill:{emph};fill-opacity:.12;stroke:{emph};stroke-width:2}}",                    # highlighted box
        f".dg-ax{{fill:none;stroke:{edge};stroke-width:{S.EDGE_W}}}",                              # axis, tick
        f".dg-ev{{fill:none;stroke:{emph};stroke-width:2}}",                                       # event line
        f".dg-mt{{font-size:{S.GROUP_FS}px;fill:{muted}}}",                                        # small muted text
        f".dg-evl{{font-size:{S.EDGE_FS}px;font-weight:700;fill:{emph}}}",                         # event label
        f".dg-ph{{font-size:{S.NODE_FS}px;font-weight:700;fill:{ink}}}",                           # panel heading
    ])


def inline_css() -> str:
    """Stylesheet for the web shell. Every colour is a token; nothing is literal."""
    def color(token):
        if token == "--dg-ground":
            return "var(--dg-ground,var(--surface,#fff))"
        return f"var({token})"
    extra = (".dg{display:block;width:calc(var(--dg-w)*1px);max-width:100%;"
             f"min-width:calc(var(--dg-w)*{S.MIN_SCALE}px);height:auto}}"
             ".dg-il{display:var(--dg-show-light,inline)}.dg-id{display:var(--dg-show-dark,none)}"
             # compare: panels side by side; a panel that does not fit at the minimum scale wraps
             ".dg-cmp{display:flex;flex-wrap:wrap;gap:16px 24px;align-items:flex-start}"
             f".dg-cmp-p{{flex:1 1 calc(var(--dg-w)*{S.MIN_SCALE}px);max-width:calc(var(--dg-w)*1px);min-width:0}}"
             f".dg-cmp-h{{font:700 {S.NODE_FS}px/1.3 {textmetrics.FONT_STACK};color:var(--dg-ink);margin:0 0 6px}}")
    return _css(color) + _css_kinds(color) + extra + "\n"


def standalone_css(kind: str = "arch") -> str:
    def color(token):
        return S.LIGHT[token]
    return _css(color) + ("" if kind == "arch" else _css_kinds(color))


def known_classes() -> set:
    """Every class the shared stylesheet defines (the raw kind may use these and no others)."""
    import re
    return set(re.findall(r"\.(dg(?:-[a-z0-9]+)*)", inline_css()))


# ------------------------------------------------------------------ drawing

def _esc(text: str) -> str:
    return html.escape(text, quote=True)


def _edge_path(points: list, arrow: str) -> str:
    """Path with rounded bends, shortened where an arrowhead covers the end."""
    pts = [tuple(p) for p in points]

    def pull(p, q, dist):
        dx, dy = q[0] - p[0], q[1] - p[1]
        length = abs(dx) + abs(dy)
        if length <= dist:
            return q
        return (p[0] + dx / length * dist, p[1] + dy / length * dist)

    if arrow in ("end", "both"):
        pts[-1] = pull(pts[-1], pts[-2], S.ARROW_LEN - 1.5)
    if arrow == "both":
        pts[0] = pull(pts[0], pts[1], S.ARROW_LEN - 1.5)
    out = [f"M{fmt(pts[0][0])} {fmt(pts[0][1])}"]
    for i in range(1, len(pts) - 1):
        prev, cur, nxt = pts[i - 1], pts[i], pts[i + 1]
        len_in = abs(cur[0] - prev[0]) + abs(cur[1] - prev[1])
        len_out = abs(nxt[0] - cur[0]) + abs(nxt[1] - cur[1])
        r = min(S.BEND_R, len_in / 2, len_out / 2)
        p1 = pull(cur, prev, r)
        p2 = pull(cur, nxt, r)
        out.append(f"L{fmt(p1[0])} {fmt(p1[1])}Q{fmt(cur[0])} {fmt(cur[1])} {fmt(p2[0])} {fmt(p2[1])}")
    out.append(f"L{fmt(pts[-1][0])} {fmt(pts[-1][1])}")
    return "".join(out)


def _arrowhead(tip, prev) -> str:
    dx, dy = tip[0] - prev[0], tip[1] - prev[1]
    length = (abs(dx) + abs(dy)) or 1.0
    ux, uy = dx / length, dy / length
    bx, by = tip[0] - ux * S.ARROW_LEN, tip[1] - uy * S.ARROW_LEN
    px, py = -uy * S.ARROW_HALF, ux * S.ARROW_HALF
    return (f"{fmt(tip[0])},{fmt(tip[1])} {fmt(bx + px)},{fmt(by + py)} {fmt(bx - px)},{fmt(by - py)}")


def _decor(item: dict) -> str:
    """One plain shape of scene["decor"]: a lifeline, an axis, a tick, an arrowhead."""
    kind, cls = item["t"], item["cls"]
    if kind == "line":
        return (f'<line class="{cls}" x1="{fmt(item["x1"])}" y1="{fmt(item["y1"])}" '
                f'x2="{fmt(item["x2"])}" y2="{fmt(item["y2"])}"/>')
    if kind == "rect":
        return (f'<rect class="{cls}" x="{fmt(item["x"])}" y="{fmt(item["y"])}" width="{fmt(item["w"])}" '
                f'height="{fmt(item["h"])}" rx="{fmt(item.get("rx", 0))}"/>')
    if kind == "circle":
        return f'<circle class="{cls}" cx="{fmt(item["cx"])}" cy="{fmt(item["cy"])}" r="{fmt(item["r"])}"/>'
    if kind == "poly":
        return f'<polygon class="{cls}" points="{" ".join(f"{fmt(x)},{fmt(y)}" for x, y in item["points"])}"/>'
    raise ValueError(f"unknown decor shape {kind!r}")


def decor_box(item: dict) -> tuple:
    """Bounding rectangle of a decor shape (the lint uses it for the clip check)."""
    kind = item["t"]
    if kind == "line":
        return (min(item["x1"], item["x2"]), min(item["y1"], item["y2"]),
                abs(item["x2"] - item["x1"]), abs(item["y2"] - item["y1"]))
    if kind == "rect":
        return (item["x"], item["y"], item["w"], item["h"])
    if kind == "circle":
        return (item["cx"] - item["r"], item["cy"] - item["r"], 2 * item["r"], 2 * item["r"])
    xs = [p[0] for p in item["points"]]
    ys = [p[1] for p in item["points"]]
    return (min(xs), min(ys), max(xs) - min(xs), max(ys) - min(ys))


def _raw(node: dict, icon_markup) -> str:
    """Serialise one element of a hand-written SVG (the raw kind). <use> becomes an icon."""
    attrs = dict(node["attrs"])
    if node["tag"] == "use":
        name = (attrs.get("href") or "")[len("#ic-"):]
        return icon_markup(name, float(attrs.get("x", 0)), float(attrs.get("y", 0)), float(attrs.get("width", S.ICON)))
    head = node["tag"] + "".join(f' {k}="{_esc(v)}"' for k, v in node["attrs"])
    inner = _esc(node["text"]) + "".join(_raw(c, icon_markup) + _esc(c["tail"]) for c in node["children"])
    return f"<{head}>{inner}</{node['tag']}>" if inner else f"<{head}/>"


def _body(scene: dict, icon_markup) -> list:
    if scene.get("raw") is not None:
        return [_raw(node, icon_markup) for node in scene["raw"]]
    out = []
    for g in scene.get("groups", []):
        suffix = S.GROUPS[g["type"]][0]
        out.append(f'<rect class="dg-g dg-g-{suffix}" x="{fmt(g["x"])}" y="{fmt(g["y"])}" '
                   f'width="{fmt(g["w"])}" height="{fmt(g["h"])}" rx="2"/>')
    for item in scene.get("decor", []):
        out.append(_decor(item))
    for e in scene.get("edges", []):
        if not e.get("points"):
            continue
        cls = "dg-e" + (" dg-e-emph" if e["emph"] else "") + (" dg-e-dash" if e["dashed"] else "")
        out.append(f'<path class="{cls}" d="{_edge_path(e["points"], e["arrow"])}"/>')
        head = "dg-ah" + (" dg-ah-emph" if e["emph"] else "")
        if e["arrow"] in ("end", "both"):
            out.append(f'<polygon class="{head}" points="{_arrowhead(e["points"][-1], e["points"][-2])}"/>')
        if e["arrow"] == "both":
            out.append(f'<polygon class="{head}" points="{_arrowhead(e["points"][0], e["points"][1])}"/>')
    for n in scene.get("nodes", []):
        fill_emph = bool(n.get("emph") and n.get("emph_fill") and n.get("box"))
        if n.get("emph") and n.get("ring"):        # arch: a ring close around the icon
            x, y, w, h = n["ring"]
            out.append(f'<rect class="dg-ne" x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}" rx="8"/>')
        elif n.get("emph") and not fill_emph:
            x, y, w, h = n["bbox"]
            out.append(f'<rect class="dg-ne" x="{fmt(x - 6)}" y="{fmt(y - 6)}" width="{fmt(w + 12)}" '
                       f'height="{fmt(h + 12)}" rx="{fmt(n.get("rx", 0) + 6)}"/>')
        if n.get("icon_box"):
            x, y, w, h = n["icon_box"]
            out.append(icon_markup(n["icon"], x, y, w))
        elif n.get("box"):
            x, y, w, h = n["box"]
            geom = f'x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}" rx="{fmt(n.get("rx", 4))}"'
            if fill_emph:       # an opaque ground first, so that lines under the box do not show through
                out.append(f'<rect class="dg-ground" {geom}/>')
            out.append(f'<rect class="{"dg-sp" if fill_emph else n.get("box_cls", "dg-nb")}" {geom}/>')
            if n.get("inner"):
                out.append(f'<rect class="dg-nf" x="{fmt(x + 3.5)}" y="{fmt(y + 3.5)}" width="{fmt(w - 7)}" '
                           f'height="{fmt(h - 7)}" rx="{fmt(max(n.get("rx", 4) - 3.5, 0))}"/>')
        for line in n.get("lines", []):
            out.append(f'<text class="dg-nl" x="{fmt(line["x"])}" y="{fmt(line["y"])}">{_esc(line["text"])}</text>')
    for e in scene.get("edges", []):
        badge, label = e.get("badge"), e.get("label")
        if badge:
            cls = "dg-b" + (" dg-b-emph" if e["emph"] else "")
            out.append(f'<circle class="{cls}" cx="{fmt(badge["cx"])}" cy="{fmt(badge["cy"])}" r="{S.BADGE_R}"/>')
            out.append(f'<text class="dg-bt" x="{fmt(badge["cx"])}" y="{fmt(badge["cy"] + 4)}">{badge["n"]}</text>')
        if label:
            cls = "dg-el" + (" dg-el-emph" if e["emph"] else "")
            anchor = "" if label["anchor"] == "start" else f' text-anchor="{label["anchor"]}"'
            out.append(f'<text class="{cls}" x="{fmt(label["x"])}" y="{fmt(label["y"])}"{anchor}>{_esc(label["text"])}</text>')
    for g in scene.get("groups", []):
        x, y = g["label_pos"]
        anchor = ' text-anchor="end"' if g["label_anchor"] == "end" else ""
        out.append(f'<text class="dg-gl" x="{fmt(x)}" y="{fmt(y)}"{anchor}>{_esc(g["label"])}</text>')
    for t in scene.get("texts", []):
        anchor = f' text-anchor="{t["anchor"]}"' if t.get("anchor") and t["anchor"] != "start" else ""
        out.append(f'<text class="{t.get("cls", "dg-el")}" x="{fmt(t["x"])}" y="{fmt(t["y"])}"{anchor}>{_esc(t["text"])}</text>')
    return out


def _missing_icon(x, y, size) -> str:
    return (f'<rect class="dg-nb" x="{fmt(x)}" y="{fmt(y)}" width="{fmt(size)}" height="{fmt(size)}" rx="4"/>')


def render_standalone(scene: dict, spec: dict, icons: dict) -> str:
    """A complete SVG document: light palette, opaque ground, embedded icons."""
    def icon_markup(name, x, y, size):
        entry = icons.get(name)
        if not entry:
            return _missing_icon(x, y, size)
        return (f'<svg x="{fmt(x)}" y="{fmt(y)}" width="{fmt(size)}" height="{fmt(size)}" '
                f'viewBox="{entry["viewBox"]}">{entry["body"]}</svg>')

    w, h = scene["w"], scene["h"]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" class="dg dg-{scene["kind"]}" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img">',
        f'<title>{_esc(spec.get("title", ""))}</title>',
        f'<desc>{_esc(spec.get("alt", ""))}</desc>',
        f'<style>{standalone_css(scene["kind"])}</style>',
        f'<rect class="dg-ground" width="{w}" height="{h}"/>',
    ]
    if scene.get("panels") is not None:        # compare: the panels side by side in one file
        for panel in scene["panels"]:
            sub = panel["scene"]
            parts.append(f'<text class="dg-ph" x="{fmt(panel["x"])}" y="{fmt(panel["head_y"])}">{_esc(panel["label"])}</text>')
            parts.append(f'<svg x="{fmt(panel["x"])}" y="{fmt(panel["y"])}" width="{sub["w"]}" height="{sub["h"]}" '
                         f'viewBox="0 0 {sub["w"]} {sub["h"]}">')
            parts += _body(sub, icon_markup)
            parts.append("</svg>")
    else:
        parts += _body(scene, icon_markup)
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def render_inline(scene: dict, spec: dict, icons: dict = None) -> str:
    """An <svg> fragment for the web app: classes only, no ids, icons by <use>."""
    icons = icons or {}

    def icon_markup(name, x, y, size):
        geom = f'x="{fmt(x)}" y="{fmt(y)}" width="{fmt(size)}" height="{fmt(size)}"'
        if icons.get(name, {}).get("dark"):
            return (f'<use class="dg-il" href="#ic-{name}" {geom}/>'
                    f'<use class="dg-id" href="#ic-{name}-dark" {geom}/>')
        return f'<use href="#ic-{name}" {geom}/>'

    if scene.get("panels") is not None:
        # compare: a wrapper <div> with one <svg> per panel; the stylesheet stacks them on a phone
        parts = [f'<div class="dg-cmp" role="group" aria-label="{_esc(spec.get("alt", ""))}" '
                 f'data-dg="{_esc(scene["id"])}">']
        for panel in scene["panels"]:
            sub = panel["scene"]
            parts.append(f'<div class="dg-cmp-p" style="--dg-w:{sub["w"]}"><div class="dg-cmp-h">{_esc(panel["label"])}</div>')
            parts.append(f'<svg class="dg dg-{sub["kind"]}" width="{sub["w"]}" height="{sub["h"]}" '
                         f'viewBox="0 0 {sub["w"]} {sub["h"]}" role="img" aria-label="{_esc(panel["label"])}" '
                         f'style="--dg-w:{sub["w"]}">')
            parts += _body(sub, icon_markup)
            parts.append("</svg></div>")
        parts.append("</div>")
        return "\n".join(parts) + "\n"

    w, h = scene["w"], scene["h"]
    parts = [
        f'<svg class="dg dg-{scene["kind"]}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" '
        f'aria-label="{_esc(spec.get("alt", ""))}" data-dg="{_esc(scene["id"])}" style="--dg-w:{w}">',
    ]
    parts += _body(scene, icon_markup)
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def used_icons(scene: dict) -> list:
    names = {n["icon"] for n in scene.get("nodes", []) if n.get("icon")}
    names.update(scene.get("icons", []))
    for panel in scene.get("panels") or []:
        names.update(used_icons(panel["scene"]))
    return sorted(names)
