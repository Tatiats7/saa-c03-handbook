"""Preview pages and screenshots (headless Chrome, called with subprocess).

preview <id>   four panels: desktop width and 368 px, light and dark, drawn with render_inline()
               and the token values of the web app, plus the standalone file as an image.
shot <id>      PNG of that page.
shot --file    PNG of any .html or .svg inside the book (other agents use this).
sheet          one PNG with every built diagram.
"""
from __future__ import annotations

import html
import os
import re
import shutil
import signal
import subprocess
import time
from pathlib import Path

from .. import common
from . import icons as icons_mod
from . import pipeline
from . import style as S
from . import svg

DESKTOP_W = 720          # content width of the desktop panel
PHONE_W = 368            # full width of the phone panel
PHONE_PAD = 16

_MEASURE = ("<script>window.addEventListener('load',function(){var d=document.documentElement,b=document.body;"
            "d.setAttribute('data-saa-h',Math.ceil(Math.max(d.scrollHeight,b?b.scrollHeight:0,"
            "d.getBoundingClientRect().height)));});</script>")

# the web app's tokens that the diagram card needs, per theme
_PAGE = {
    "light": {"--ground": "#F2F4F8", "--surface": "#FFFFFF", "--ink": "#141C2B", "--muted": "#5A667A",
              "--line": "#D6DCE6", "--accent": "#2A3EB1"},
    "dark": {"--ground": "#0F131B", "--surface": "#171D28", "--ink": "#E7EBF3", "--muted": "#98A4B8",
             "--line": "#2A3342", "--accent": "#93A1FF"},
}


class PreviewError(Exception):
    def __init__(self, message: str, code: int = None):
        super().__init__(message)
        self.code = common.EXIT_FAIL if code is None else code


def out_dir() -> Path:
    return common.ensure_dir(common.TMP / "diagram-preview")


def _resolve(path_text: str) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = common.REPO / path
    path = path.resolve()
    if not common.inside_book(path):
        raise PreviewError(f"refused: {path} is outside {common.REAL_BOOK}", common.EXIT_POLICY)
    return path


# ------------------------------------------------------------------ Chrome

def _chrome(url: str, extra: list, width: int, height: int, scale: float, done, timeout: int = 60) -> str:
    """Run headless Chrome until done(stdout_text) is true, then stop it.

    Chrome's new headless mode often does not exit by itself on macOS after --screenshot or
    --dump-dom, so the tool watches for the result and ends the process group. Each call uses
    its own throwaway profile folder, so it never touches the user's Chrome."""
    if not Path(common.CHROME).exists():
        raise PreviewError(f"Chrome not found at {common.CHROME}", common.EXIT_PRECONDITION)
    profile = common.TMP / f"chrome-profile-{os.getpid()}"
    common.ensure_dir(profile)
    stdout_path = profile / "stdout.txt"
    cmd = [common.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
           "--no-default-browser-check", "--disable-extensions", "--allow-file-access-from-files",
           f"--user-data-dir={profile}", f"--window-size={int(width)},{int(height)}",
           f"--force-device-scale-factor={scale:g}", "--virtual-time-budget=5000"] + extra + [url]
    text = ""
    try:
        with open(stdout_path, "w", encoding="utf-8") as stdout:
            try:
                proc = subprocess.Popen(cmd, stdout=stdout, stderr=subprocess.DEVNULL, start_new_session=True)
            except OSError as exc:
                raise PreviewError(f"could not start Chrome: {exc}", common.EXIT_PRECONDITION)
            start = time.time()
            ok = False
            try:
                while time.time() - start < timeout:
                    time.sleep(0.15)
                    text = stdout_path.read_text(encoding="utf-8", errors="replace")
                    if done(text):
                        ok = True
                        break
                    if proc.poll() is not None:
                        text = stdout_path.read_text(encoding="utf-8", errors="replace")
                        ok = done(text)
                        break
            finally:
                if proc.poll() is None:
                    try:
                        os.killpg(proc.pid, signal.SIGTERM)
                        proc.wait(timeout=5)
                    except (OSError, subprocess.TimeoutExpired):
                        try:
                            os.killpg(proc.pid, signal.SIGKILL)
                        except OSError:
                            pass
            if not ok:
                raise PreviewError("Chrome produced no result in time", common.EXIT_TRANSIENT)
    finally:
        shutil.rmtree(profile, ignore_errors=True)
    return text


def measure_height(page: Path, width: int, dark: bool = False) -> int:
    """Full height of a page in CSS pixels (the page must carry the _MEASURE script)."""
    extra = ["--dump-dom"] + (["--force-dark-mode"] if dark else [])
    pattern = re.compile(r'data-saa-h="(\d+)"')
    text = _chrome(page.as_uri(), extra, width, 800, 1, lambda out: bool(pattern.search(out)))
    return max(int(pattern.search(text).group(1)), 50)


def screenshot(page: Path, png: Path, width: int, height: int, scale: float = 2.0, dark: bool = False) -> Path:
    common.ensure_dir(png.parent)
    if png.exists():
        png.unlink()
    extra = [f"--screenshot={png}"] + (["--force-dark-mode"] if dark else [])
    seen = {"size": -1}

    def done(_out):
        if not png.exists():
            return False
        size = png.stat().st_size
        stable = size > 0 and size == seen["size"]
        seen["size"] = size
        return stable

    _chrome(page.as_uri(), extra, width, height, scale, done)
    return png


# ------------------------------------------------------------------ the four-panel page

def _vars(mapping: dict) -> str:
    return ";".join(f"{k}:{v}" for k, v in mapping.items())


def _card(spec: dict, inline_svg: str, phone: bool, scene_w: int) -> str:
    cap = pipeline.caption(spec)
    steps = "".join(f"<li>{html.escape(say)}</li>" for _n, say in cap["steps"])
    note = ""
    if phone:
        fit = PHONE_W - 2 * PHONE_PAD - 2
        need = int(scene_w * S.MIN_SCALE)
        note = (f'<p class="pv-note">scale {min(1.0, max(S.MIN_SCALE, fit / scene_w)):.2f}'
                + (f"; scrolls sideways (needs {need}, has {fit})" if need > fit else "") + "</p>")
    return (f'<figure class="pv-card"><figcaption class="pv-title"><span class="pv-fig">Figure</span> '
            f'{html.escape(cap["title"])}</figcaption>'
            f'<div class="pv-scroll">{inline_svg}</div>'
            f'<p class="pv-claim">{html.escape(cap["claim"])}</p>'
            + (f'<ol class="pv-steps">{steps}</ol>' if steps else "") + note + "</figure>")


def preview_html(result: dict, icons: dict, standalone_name: str = None) -> str:
    spec, scene = result["spec"], result["scene"]
    inline_svg = svg.render_inline(scene, spec, icons)
    sprite = icons_mod.sprite(icons, svg.used_icons(scene))
    issues = "".join(f'<li class="pv-{i["level"]}">{html.escape(i["level"])} {html.escape(i["code"])}: '
                     f'{html.escape(i["msg"])}</li>' for i in result["issues"])
    rows = []
    phone_w = scene.get("phone_w", scene["w"])      # compare: the widest panel, because panels stack
    for theme, palette in (("light", S.LIGHT), ("dark", S.DARK)):
        style = _vars({**_PAGE[theme], **palette, "--dg-ground": _PAGE[theme]["--surface"]})
        rows.append(
            f'<section class="pv-row" style="{style}">'
            f'<div class="pv-panel pv-desktop"><div class="pv-tag">desktop, {theme}</div>{_card(spec, inline_svg, False, phone_w)}</div>'
            f'<div class="pv-panel pv-phone"><div class="pv-tag">phone {PHONE_W} px, {theme}</div>{_card(spec, inline_svg, True, phone_w)}</div>'
            f'</section>')
    standalone = ""
    if standalone_name:
        standalone = (f'<section class="pv-row pv-file"><div class="pv-panel"><div class="pv-tag">standalone file '
                      f'(Markdown preview, PDF, Anki)</div><img src="{html.escape(standalone_name)}" alt=""></div></section>')
    page_w = DESKTOP_W + 2 * 24 + PHONE_W + 3 * 20
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{html.escape(spec["id"])} preview</title>
<style>
html,body{{margin:0;background:#888}}
body{{width:{page_w}px;font-family:-apple-system,"Segoe UI",system-ui,sans-serif;font-size:15px}}
.pv-head{{background:#fff;color:#141C2B;padding:10px 20px;font-size:13px}}
.pv-head ul{{margin:4px 0 0;padding-left:18px}} .pv-error{{color:#B3261E}} .pv-warn{{color:#8F5800}}
.pv-row{{display:flex;gap:20px;padding:20px;background:var(--ground);color:var(--ink);align-items:flex-start}}
.pv-file{{background:#fff}}
.pv-panel{{box-sizing:border-box}}
.pv-desktop{{width:{DESKTOP_W + 2 * 24}px}}
.pv-phone{{width:{PHONE_W}px}}
.pv-tag{{font:11px ui-monospace,Menlo,monospace;text-transform:uppercase;letter-spacing:.06em;color:var(--muted,#5A667A);margin-bottom:6px}}
.pv-card{{margin:0;background:var(--surface);border:1px solid var(--line);border-radius:4px;padding:24px;box-sizing:border-box}}
.pv-phone .pv-card{{padding:{PHONE_PAD}px}}
.pv-title{{font-weight:600;margin-bottom:12px}}
.pv-fig{{font:12px ui-monospace,Menlo,monospace;color:var(--muted);margin-right:6px}}
.pv-scroll{{overflow-x:auto}}
.pv-claim{{margin:12px 0 0;line-height:1.45}}
.pv-steps{{margin:8px 0 0;padding-left:22px;line-height:1.45;font-size:14px}}
.pv-note{{margin:8px 0 0;font:11px ui-monospace,Menlo,monospace;color:var(--muted)}}
.pv-file img{{display:block;border:1px solid #D6DCE6}}
{svg.inline_css()}</style></head>
<body>
{sprite}
<div class="pv-head"><b>{html.escape(spec["id"])}</b> &middot; {scene["w"]} x {scene["h"]} units &middot; kind {html.escape(spec["kind"])}
{f'<ul>{issues}</ul>' if issues else ' &middot; lint clean'}</div>
{''.join(rows)}
{standalone}
{_MEASURE}
</body></html>
"""


def write_preview(diagram_id: str):
    """Write TMP/diagram-preview/<id>.html. Works with lint errors too, so the author can look."""
    result = pipeline.check_id(diagram_id)
    if result["scene"] is None:
        first = result["issues"][0]["msg"] if result["issues"] else "no scene"
        raise PreviewError(f"{diagram_id}: cannot draw: {first}", common.EXIT_FAIL)
    icons = icons_mod.load()
    folder = out_dir()
    standalone = folder / f"{diagram_id}.standalone.svg"
    standalone.write_text(svg.render_standalone(result["scene"], result["spec"], icons), encoding="utf-8")
    page = folder / f"{diagram_id}.html"
    page.write_text(preview_html(result, icons, standalone.name), encoding="utf-8")
    width = DESKTOP_W + 2 * 24 + PHONE_W + 3 * 20
    return page, width


def shot_diagram(diagram_id: str, out: str = None, scale: float = 2.0) -> Path:
    page, width = write_preview(diagram_id)
    png = _resolve(out) if out else out_dir() / f"{diagram_id}.png"
    height = measure_height(page, width)
    return screenshot(page, png, width, height, scale)


# ------------------------------------------------------------------ any file

def _wrap(source: Path, dark: bool) -> Path:
    """A copy of the page under TMP with a <base> to the original folder and the measuring script."""
    folder = out_dir()
    wrapped = folder / f"shot-{common.sha256_bytes(str(source).encode())[:12]}.html"
    base = f'<base href="{html.escape(source.parent.as_uri())}/">'
    if source.suffix.lower() == ".svg":
        ground = "#0F131B" if dark else "#FFFFFF"
        text = (f'<!doctype html><html{" data-theme=\"dark\"" if dark else ""}><head><meta charset="utf-8">{base}'
                f'<style>html,body{{margin:0;background:{ground}}}img{{display:block;max-width:100%}}</style></head>'
                f'<body><img src="{html.escape(source.name)}" alt="">{_MEASURE}</body></html>')
    else:
        text = source.read_text(encoding="utf-8", errors="replace")
        if dark:
            if re.search(r"<html\b", text, re.I):
                text = re.sub(r"<html\b", '<html data-theme="dark"', text, count=1, flags=re.I)
            else:
                text = '<html data-theme="dark">' + text
        if re.search(r"<head\b[^>]*>", text, re.I):
            text = re.sub(r"(<head\b[^>]*>)", lambda m: m.group(1) + base, text, count=1, flags=re.I)
        else:
            text = base + text
        if re.search(r"</body>", text, re.I):
            idx = [m.start() for m in re.finditer(r"</body>", text, re.I)][-1]
            text = text[:idx] + _MEASURE + text[idx:]
        else:
            text += _MEASURE
    wrapped.write_text(text, encoding="utf-8")
    return wrapped


def shot_file(file: str, out: str, width: int = 1280, height: int = 900, dark: bool = False,
              full: bool = False, scale: float = 2.0) -> Path:
    source = _resolve(file)
    if not source.is_file():
        raise PreviewError(f"{source} does not exist", common.EXIT_PRECONDITION)
    if source.suffix.lower() not in (".html", ".htm", ".svg"):
        raise PreviewError("--file must be an .html or .svg file", common.EXIT_PRECONDITION)
    png = _resolve(out)
    wrapped = _wrap(source, dark)
    if full or source.suffix.lower() == ".svg":
        height = min(measure_height(wrapped, width, dark), 16000)
    return screenshot(wrapped, png, width, height, scale, dark)


# ------------------------------------------------------------------ contact sheet

def sheet(out: str = None, scale: float = 1.0):
    # <id>.p1.svg and so on are the panels of a compare diagram; the sheet shows the combined file
    files = sorted(p for p in common.DIAGRAM_SVG.glob("*.svg") if "." not in p.stem) if common.DIAGRAM_SVG.is_dir() else []
    if not files:
        raise PreviewError("no built diagrams in diagrams/svg; run: diagram build --all", common.EXIT_PRECONDITION)
    cards = []
    for path in files:
        spec = common.read_json(pipeline.spec_path(path.stem), {}) or {}
        cards.append(f'<figure><img src="{html.escape(path.as_uri())}" alt=""><figcaption><code>{html.escape(path.stem)}</code> '
                     f'{html.escape(spec.get("kind", ""))} &middot; {html.escape(spec.get("title", ""))}</figcaption></figure>')
    width = 1500
    page = out_dir() / "sheet.html"
    page.write_text(f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Diagram contact sheet</title>
<style>
html,body{{margin:0;background:#F2F4F8}}
body{{width:{width}px;font-family:-apple-system,"Segoe UI",system-ui,sans-serif;font-size:13px;color:#141C2B}}
h1{{font-size:16px;margin:0;padding:16px 20px 0}}
main{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;padding:16px 20px 20px;align-items:start}}
figure{{margin:0;background:#fff;border:1px solid #D6DCE6;border-radius:4px;padding:12px}}
img{{display:block;max-width:100%;height:auto;margin:0 auto}}
figcaption{{margin-top:8px;color:#5A667A}} code{{color:#141C2B}}
</style></head><body><h1>Diagram contact sheet: {len(files)} diagrams</h1><main>{''.join(cards)}</main>{_MEASURE}</body></html>
""", encoding="utf-8")
    png = _resolve(out) if out else out_dir() / "sheet.png"
    height = min(measure_height(page, width), 16000)
    return screenshot(page, png, width, height, scale), len(files)
