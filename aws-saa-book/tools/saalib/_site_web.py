"""`web lint`, `web selftest`, `web shots` (tools/web/ARCHITECTURE.md sections 9.2, 9.3, 9.5).

Loaded by saalib/site.py; no subcommand of its own (the name starts with `_`, so saa.py skips it).
"""
from __future__ import annotations

import functools
import html
import http.server
import math
import re
import shutil
import subprocess
import threading
from pathlib import Path

from saalib import common

SHOTS = ["home", "chapter", "prose", "evidence", "glossary", "toc", "quiz-open", "quiz-stemfirst", "quiz-checked",
         "mock-run", "mock-results", "mistakes", "cards", "plan", "progress", "files", "speak-self", "speak-result",
         "ask", "search"]
SIZES = {"desktop": (1280, 900), "phone": (400, 860)}
NAMED = ("aliceblue antiquewhite aqua aquamarine azure beige bisque black blanchedalmond blue blueviolet brown burlywood "
         "cadetblue chartreuse chocolate coral cornflowerblue cornsilk crimson cyan darkblue darkcyan darkgoldenrod darkgray "
         "darkgreen darkgrey darkkhaki darkmagenta darkolivegreen darkorange darkorchid darkred darksalmon darkseagreen "
         "darkslateblue darkslategray darkslategrey darkturquoise darkviolet deeppink deepskyblue dimgray dimgrey dodgerblue "
         "firebrick floralwhite forestgreen fuchsia gainsboro ghostwhite gold goldenrod gray green greenyellow grey honeydew "
         "hotpink indianred indigo ivory khaki lavender lavenderblush lawngreen lemonchiffon lightblue lightcoral lightcyan "
         "lightgoldenrodyellow lightgray lightgreen lightgrey lightpink lightsalmon lightseagreen lightskyblue lightslategray "
         "lightslategrey lightsteelblue lightyellow lime limegreen linen magenta maroon mediumaquamarine mediumblue "
         "mediumorchid mediumpurple mediumseagreen mediumslateblue mediumspringgreen mediumturquoise mediumvioletred "
         "midnightblue mintcream mistyrose moccasin navajowhite navy oldlace olive olivedrab orange orangered orchid "
         "palegoldenrod palegreen paleturquoise palevioletred papayawhip peachpuff peru pink plum powderblue purple "
         "rebeccapurple red rosybrown royalblue saddlebrown salmon sandybrown seagreen seashell sienna silver skyblue "
         "slateblue slategray slategrey snow springgreen steelblue tan teal thistle tomato turquoise violet wheat white "
         "whitesmoke yellow yellowgreen").split()
RE_NAMED = re.compile(r"(?<![\w-])(" + "|".join(NAMED) + r")(?![\w-])", re.I)
RE_COLOR_PROP = re.compile(r"(?<![\w-])(color|background|background-color|border(?:-[a-z]+)*|outline(?:-color)?|fill|stroke|"
                           r"box-shadow|text-shadow|caret-color|accent-color|text-decoration(?:-color)?|column-rule(?:-color)?)"
                           r"\s*:\s*([^;{}]+)", re.I)
RE_HEX = re.compile(r"#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})(?![0-9A-Za-z_-])")
RE_FUNC_COLOR = re.compile(r"(?<![\w-])(?:rgba?|hsla?)\(")
RE_VH = re.compile(r"(?<![A-Za-z0-9_.-])\d*\.?\d+[dsl]?vh\b")
RE_URL = re.compile(r"https?://([A-Za-z0-9.-]+)")
ALLOWED_URL_HOSTS = {"fonts.googleapis.com", "www.w3.org"}


# ---------------------------------------------------------------- lint

def _blank(text: str, start: int, end: int) -> str:
    return text[:start] + re.sub(r"[^\n]", " ", text[start:end]) + text[end:]


def strip_css_comments(text: str) -> str:
    return re.sub(r"/\*.*?\*/", lambda m: re.sub(r"[^\n]", " ", m.group(0)), text, flags=re.S)


def strip_js_comments(text: str) -> str:
    """Blank out // and /* */ comments; strings and template literals are kept. Line numbers do not change."""
    out, i, n = [], 0, len(text)
    quote = None
    while i < n:
        c = text[i]
        if quote:
            out.append(c)
            if c == "\\" and i + 1 < n:
                out.append(text[i + 1])
                i += 2
                continue
            if c == quote or (c == "\n" and quote != "`"):
                quote = None
            i += 1
            continue
        if c in "\"'`":
            quote = c
            out.append(c)
            i += 1
        elif c == "/" and i + 1 < n and text[i + 1] == "/":
            j = text.find("\n", i)
            j = n if j < 0 else j
            out.append(" " * (j - i))
            i = j
        elif c == "/" and i + 1 < n and text[i + 1] == "*":
            j = text.find("*/", i + 2)
            j = n if j < 0 else j + 2
            out.append(re.sub(r"[^\n]", " ", text[i:j]))
            i = j
        else:
            out.append(c)
            i += 1
    return "".join(out)


def _line(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def _supports_ranges(text: str) -> list:
    ranges = []
    for m in re.finditer(r"@supports\s*\(\s*height\s*:\s*1dvh\s*\)\s*\{", text):
        depth, i = 1, m.end()
        while i < len(text) and depth:
            depth += {"{": 1, "}": -1}.get(text[i], 0)
            i += 1
        ranges.append((m.start(), i))
    return ranges


def lint_text(name: str, kind: str, raw: str) -> list:
    """Findings for one source file. kind: 'html', 'css', 'js' or 'stub'; name is the display path."""
    out = []
    base = name.rsplit("/", 1)[-1]

    def add(code, pos, msg, text=None):
        out.append({"code": code, "file": name, "line": _line(text if text is not None else raw, pos), "item": None, "msg": msg})

    code_text = strip_css_comments(raw) if kind == "css" else strip_js_comments(raw) if kind in ("js", "stub") else raw
    if kind in ("css", "js", "stub"):
        for m in RE_HEX.finditer(code_text):
            add("WL01", m.start(), f"literal colour {m.group(0)}; colours live in tokens.json", code_text)
        for m in RE_FUNC_COLOR.finditer(code_text):
            add("WL01", m.start(), f"literal colour function {m.group(0)}; colours live in tokens.json", code_text)
    if kind == "css":
        for m in RE_COLOR_PROP.finditer(code_text):
            value = re.sub(r"var\(\s*--[\w-]+", " ", m.group(2))
            for word in RE_NAMED.findall(value):
                add("WL01", m.start(), f"named colour {word} as the value of {m.group(1)}", code_text)
        for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", code_text):
            selectors = [s.strip() for s in m.group(1).split(",")]
            if re.search(r"overflow-x\s*:\s*(hidden|clip)", m.group(2)) and \
                    any(re.search(r"(?:^|[\s>+~])(?:body|\.app|\.shell)$", s) for s in selectors):
                add("WL02", m.start(2), "overflow-x hidden or clip on body, .app or .shell", code_text)
    if kind in ("css", "js", "stub"):
        allowed = _supports_ranges(code_text) if kind == "css" else []
        for m in RE_VH.finditer(code_text):
            if not any(a <= m.start() < b for a, b in allowed):
                add("WL02", m.start(), f"viewport unit {m.group(0)}; size a one-screen view with height: 100%", code_text)
    if kind in ("js", "stub", "html"):
        for m in re.finditer(r"window\.print|(?:(?<![\w$.])|window\.)(?:alert|confirm|prompt)\s*\(", code_text):
            add("WL03", m.start(), f"{m.group(0).strip()} is blocked in the frame", code_text)
        for m in re.finditer(r"<a\s[^>]*\bdownload\b|\.download\s*=", code_text):
            add("WL04", m.start(), "downloads started by the page are blocked; use the downloads capability", code_text)
        if base != "search.js":
            for m in re.finditer(r"URL\.createObjectURL", code_text):
                add("WL04", m.start(), "URL.createObjectURL is allowed only in search.js", code_text)
        for m in re.finditer(r"style\.display|document\.write|(?<![\w$.])eval\s*\(", code_text):
            add("WL05", m.start(), f"{m.group(0).strip()} is not allowed", code_text)
        if base != "util.js":
            for m in re.finditer(r"\b(innerHTML|outerHTML|insertAdjacentHTML)\b", code_text):
                add("WL05", m.start(), f"{m.group(1)} outside util.js; use U.set", code_text)
        if base != "util.js" and kind != "stub":
            for m in re.finditer(r"\blocalStorage\b", code_text):
                add("WL06", m.start(), "localStorage outside util.js and the stub; use U.ls or Store", code_text)
            for m in re.finditer(r"Date\.now\s*\(|new\s+Date\s*\(\s*\)", code_text):
                add("WL10", m.start(), "the clock is read only through U.now and U.nowMs", code_text)
        for m in re.finditer(r"navigator\.serviceWorker|getUserMedia", code_text):
            add("WL06", m.start(), f"{m.group(0)} is blocked in the frame", code_text)
    for m in RE_URL.finditer(code_text):
        if m.group(1).lower() not in ALLOWED_URL_HOSTS:
            add("WL06", m.start(), f"URL to the host {m.group(1)}; only fonts.googleapis.com is allowed", code_text)
    if kind == "html":
        seen = {}
        for m in re.finditer(r'\bid="([^"]*)"', raw):
            if m.group(1) in seen:
                add("WL07", m.start(), f'id="{m.group(1)}" is used twice')
            seen[m.group(1)] = True
        for tag in re.finditer(r"<[A-Za-z][^<>]*>", raw):
            inner = re.sub(r'"[^"]*"', '""', tag.group(0))
            bad = re.search(r"\s([A-Za-z_:][-\w:.]*)\s*=\s*(?!\")", inner)
            if bad:
                add("WL07", tag.start(), f"attribute {bad.group(1)} without double quotes")
    if kind in ("css", "js"):
        pattern = re.compile(r"\b(?:65|130|720)\b[^\n]{0,24}?\b(?:question|minute|score)|\b(?:question|minute|score)\w*[^\n]{0,24}?\b(?:65|130|720)\b", re.I)
        for m in pattern.finditer(code_text):
            add("WL08", m.start(), "an exam number in source; exam numbers come from verified facts or mock.json", code_text)
    if kind == "js":
        for m in re.finditer(r"</script|<!--", raw, re.I):
            add("WL09", m.start(), f"{m.group(0)} in a script that is inlined; write it as a split string")
    return out


def source_files() -> list:
    """(display name, kind, path) of every file the lint reads."""
    web = common.WEB_SRC
    rows = []
    if (web / "shell.html").is_file():
        rows.append(("tools/web/shell.html", "html", web / "shell.html"))
    for folder, kind in (("css", "css"), ("js", "js")):
        if (web / folder).is_dir():
            for path in sorted((web / folder).glob(f"*.{folder}")):
                rows.append((f"tools/web/{folder}/{path.name}", kind, path))
    stub = web / "stubs" / "claude-stub.js"
    if stub.is_file():
        rows.append(("tools/web/stubs/claude-stub.js", "stub", stub))
    return rows


def lint_sources() -> list:
    findings = []
    for name, kind, path in source_files():
        findings += lint_text(name, kind, path.read_text(encoding="utf-8"))
    return findings


def cmd_lint(args) -> int:
    files = source_files()
    findings = lint_sources()
    result = {"ok": not findings, "files": len(files), "findings": findings}
    if args.json:
        common.emit(result, args)
    else:
        lines = [f"web lint: {'ok' if not findings else 'FAILED'}; {len(files)} files, {len(findings)} findings"]
        lines += [f"{f['file']}:{f['line']}: {f['code']} {f['msg']}" for f in findings[:40]]
        common.emit("\n".join(lines), args)
    return common.EXIT_FAIL if findings else common.EXIT_OK


# ---------------------------------------------------------------- the in-process server

class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):       # no request log on stderr
        pass


class Server:
    """Serves one folder on 127.0.0.1 at a free port, in a thread of this process."""
    def __init__(self, folder: Path):
        handler = functools.partial(_Quiet, directory=str(folder))
        self.httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
        self.port = self.httpd.server_address[1]
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)

    def __enter__(self):
        self.thread.start()
        return self

    def __exit__(self, *exc):
        self.httpd.shutdown()
        self.httpd.server_close()

    def url(self, page: str, route: str = "") -> str:
        return f"http://127.0.0.1:{self.port}/{page}" + (f"#{route}" if route else "")


# Headless Chrome does not lay a window out narrower than 500 px, so a "400 px" window showed the left
# 400 px of a 500 px layout. The frame page holds the preview in an iframe of the exact size (as the
# published page also runs inside a frame) and copies the selftest result line into its own DOM.
FRAME = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>frame</title>
<style>html,body{margin:0;padding:0;overflow:hidden;background:#fff}iframe{display:block;border:0;margin:0}</style></head>
<body><iframe id="f" title="preview"></iframe>
<script>
(function () {
  var q = new URLSearchParams(location.search), f = document.getElementById("f");
  f.style.width = (q.get("w") || "400") + "px";
  f.style.height = (q.get("h") || "860") + "px";
  function put(store, text) {
    try { var o = JSON.parse(text || "{}"); Object.keys(o).forEach(function (k) { store.setItem(k, o[k]); }); } catch (e) {}
  }
  put(localStorage, q.get("ls"));
  put(sessionStorage, q.get("ss"));
  f.src = (q.get("p") || "index.html") + location.hash;
  var steps = [];
  try { steps = JSON.parse(q.get("steps") || "[]"); } catch (e) {}
  function run(i, tries) {
    if (i >= steps.length) return;
    var s = steps[i], d = f.contentDocument, el;
    if (s[0] === "wait") { setTimeout(function () { run(i + 1, 0); }, Number(s[1]) || 100); return; }
    el = d && d.querySelector(s[1]);
    if (!el) { if (tries < 30) setTimeout(function () { run(i, tries + 1); }, 100); else run(i + 1, 0); return; }
    if (s[0] === "click") el.click();
    if (s[0] === "fill") { el.value = s[2] || ""; el.dispatchEvent(new f.contentWindow.Event("input", {bubbles: true})); }
    if (s[0] === "scroll") el.scrollIntoView({block: "start"});
    setTimeout(function () { run(i + 1, 0); }, 150);
  }
  f.addEventListener("load", function () { setTimeout(function () { run(0, 0); }, 300); });
  var timer = setInterval(function () {
    try {
      var pre = f.contentDocument && f.contentDocument.getElementById("saa-selftest");
      if (pre && /SELFTEST (PASS|FAIL)/.test(pre.textContent)) {
        var out = document.createElement("pre");
        out.id = "saa-selftest";
        out.textContent = pre.textContent;
        document.body.appendChild(out);
        clearInterval(timer);
      }
    } catch (e) {}
  }, 50);
})();
</script></body></html>
"""


def _preview(single: bool):
    from saalib import site
    out = common.TMP / "web-selftest"
    built = site.build_site(preview=True, single=single, out=out)
    if out.is_dir():
        (out / "frame.html").write_text(FRAME, encoding="utf-8")
    return built, out


def _framed(server, page: str, route: str, width: int, height: int, extra: dict = None) -> str:
    import json
    import urllib.parse
    query = {"p": page, "w": int(width), "h": int(height)}
    for key in ("ls", "ss", "steps"):
        if extra and extra.get(key):
            query[key] = json.dumps(extra[key], separators=(",", ":"))
    return f"http://127.0.0.1:{server.port}/frame.html?{urllib.parse.urlencode(query)}" + (f"#{route}" if route else "")


# ---------------------------------------------------------------- selftest

RE_RESULT = re.compile(r"SELFTEST (PASS|FAIL) (\d+)/(\d+)([^\n<]*)")


def _run_route(server, route, width, height):
    """(ok, passed, total, skipped, failure lines) of one browser route."""
    from saalib.diagram import preview
    url = _framed(server, "index.html", route, width, height) if width < 500 else server.url("index.html", route)
    text = preview._chrome(url, ["--dump-dom"], max(width, 500), height, 1,
                           lambda out: "SELFTEST PASS" in out or "SELFTEST FAIL" in out, timeout=90)
    m = RE_RESULT.search(text)
    block = re.search(r'<pre[^>]*id="saa-selftest"[^>]*>(.*?)</pre>', text, re.S)
    body = html.unescape(block.group(1)) if block else ""
    lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
    skipped = re.search(r"(\d+) skipped", body)
    failures = [ln for ln in lines[1:] if not re.match(r"^\d+ skipped", ln)] if m and m.group(1) == "FAIL" else []
    return (m.group(1) == "PASS", int(m.group(2)), int(m.group(3)), int(skipped.group(1)) if skipped else 0, failures)


def cmd_selftest(args) -> int:
    from saalib import site
    from saalib.diagram import preview
    only = args.only
    result = {"ok": True, "render": {"pass": 0, "total": 0, "skipped": 0}, "phone": {"pass": 0, "total": 0},
              "sim": {"pass": 0, "total": 0}, "hot": {"pass": 0, "total": 0}, "node": [], "failures": []}
    try:
        built, folder = _preview(args.single)
    except site.Stop as stop:
        return common.fail(str(stop), stop.code)
    result["build"] = {"ok": built["ok"], "out": built["out"], "build": built["build"], "errors": len(built["errors"]),
                       "warnings": len(built["warnings"])}
    for f in built["errors"]:
        result["failures"].append(f"build: {f['code']} {f['msg']}")
    code = common.EXIT_OK
    if only in (None, "node"):
        tests = sorted((common.WEB_SRC / "tests").glob("test_*.mjs"))
        node = shutil.which("node")
        if tests and not node:
            result["failures"].append("node is not installed; the node tests did not run")
            code = common.EXIT_PRECONDITION
        for path in tests if node else []:
            try:
                proc = subprocess.run([node, str(path), str(folder)], capture_output=True, text=True, timeout=300, cwd=str(common.REPO))
                ok = proc.returncode == 0
                tail = [ln for ln in (proc.stdout + proc.stderr).splitlines() if "FAIL" in ln or "Error" in ln][:5]
            except (OSError, subprocess.TimeoutExpired) as exc:
                ok, tail = False, [str(exc)]
            result["node"].append({"file": path.name, "ok": ok})
            if not ok:
                result["failures"] += [f"node {path.name}: {ln.strip()}" for ln in tail] or [f"node {path.name}: failed"]
    routes = [("render", "t.render-all", 1280, 900), ("phone", "t.render-all", 400, 860), ("sim", "t.exam-sim", 1280, 900),
              ("hot", "t.hot", 1280, 900)]
    routes = [r for r in routes if only in (None, r[0])]
    if routes:
        try:
            with Server(folder) as server:
                for name, route, width, height in routes:
                    try:
                        ok, passed, total, skipped, failures = _run_route(server, route, width, height)
                    except preview.PreviewError as exc:
                        if exc.code == common.EXIT_PRECONDITION:
                            result["failures"].append(f"{name}: {exc}")
                            code = common.EXIT_PRECONDITION
                            break
                        result["failures"].append(f"{name}: Chrome gave no result for #{route}")
                        code = max(code, common.EXIT_TRANSIENT) if code != common.EXIT_PRECONDITION else code
                        continue
                    result[name]["pass"], result[name]["total"] = passed, total
                    if name == "render":
                        result[name]["skipped"] = skipped
                    if not ok:
                        result["failures"] += [f"{name}: {ln}" for ln in failures] or [f"{name}: {passed}/{total}"]
        except OSError as exc:
            result["failures"].append(f"the local server could not start: {exc}")
            code = common.EXIT_TRANSIENT
    result["ok"] = not result["failures"]
    if args.json:
        common.emit(result, args)
    else:
        lines = [f"web selftest: {'ok' if result['ok'] else 'FAILED'}; render {result['render']['pass']}/{result['render']['total']} "
                 f"(skipped {result['render']['skipped']}), phone {result['phone']['pass']}/{result['phone']['total']}, "
                 f"sim {result['sim']['pass']}/{result['sim']['total']}, hot {result['hot']['pass']}/{result['hot']['total']}, "
                 f"node {sum(1 for n in result['node'] if n['ok'])}/{len(result['node'])}"]
        lines += result["failures"][:40]
        common.emit("\n".join(lines), args)
    if code in (common.EXIT_PRECONDITION, common.EXIT_TRANSIENT):
        return code
    return common.EXIT_OK if result["ok"] else common.EXIT_FAIL


# ---------------------------------------------------------------- shots

def _shot(url: str, png: Path, width: int, height: int, extra=None) -> None:
    from saalib.diagram import preview
    common.ensure_dir(png.parent)
    if png.exists():
        png.unlink()
    seen = {"size": -1}

    def done(_out):
        if not png.exists():
            return False
        size = png.stat().st_size
        stable = size > 0 and size == seen["size"]
        seen["size"] = size
        return stable

    preview._chrome(url, [f"--screenshot={png}"] + list(extra or []), width, height, 1, done, timeout=60)


def _sheet(folder: Path, names: list) -> Path:
    cells = []
    for name in names:
        phone, desk = folder / f"{name}.phone.light.png", folder / f"{name}.desktop.dark.png"
        if not phone.is_file() and not desk.is_file():
            continue
        imgs = "".join(f'<img src="{html.escape(p.name)}" alt="" style="width:{w}px">' for p, w in ((phone, 200), (desk, 640)) if p.is_file())
        cells.append(f"<figure><figcaption>{html.escape(name)}</figcaption><div>{imgs}</div></figure>")
    rows = max(1, math.ceil(len(cells) / 2))
    page = folder / "sheet.html"
    page.write_text(
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><title>Web contact sheet</title><style>"
        "html,body{margin:0;background:#F2F4F8}body{width:1800px;font:13px -apple-system,system-ui,sans-serif;color:#141C2B}"
        "main{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:12px}"
        "figure{margin:0;background:#fff;border:1px solid #D6DCE6;padding:8px;height:468px;box-sizing:border-box;overflow:hidden}"
        "figure div{display:flex;gap:8px;align-items:flex-start}img{display:block;height:auto}"
        "figcaption{font-weight:600;margin-bottom:6px}</style></head><body><main>" + "".join(cells) + "</main></body></html>\n",
        encoding="utf-8")
    png = folder / "sheet.png"
    _shot(page.as_uri(), png, 1800, rows * 480 + 24)
    return png


def cmd_shots(args) -> int:
    from saalib import site
    from saalib.diagram import preview
    folder_out = common.BUILD / "shots"
    if args.shots_dir:
        folder_out = Path(args.shots_dir)
        if not folder_out.is_absolute():
            folder_out = common.REPO / folder_out
        folder_out = folder_out.resolve()
        if not common.inside_book(folder_out):
            return common.fail(f"refused: --shots-dir must be inside {common.REAL_BOOK}", common.EXIT_POLICY)
    extras = []
    if getattr(args, "extra", None):
        extra_path = Path(args.extra) if Path(args.extra).is_absolute() else common.REPO / args.extra
        try:
            extras = common.read_json(extra_path)
        except (OSError, ValueError) as exc:
            return common.fail(f"--extra: cannot read {extra_path}: {exc}", common.EXIT_PRECONDITION)
        if not isinstance(extras, list) or any(not isinstance(e, dict) or not re.fullmatch(r"[a-z0-9-]+", str(e.get("name", "")))
                                               for e in extras):
            return common.fail("--extra: a list of objects with a name of [a-z0-9-]+ is needed", common.EXIT_PRECONDITION)
    names = [n.strip() for n in args.only.split(",") if n.strip()] if args.only else ([] if extras else list(SHOTS))
    unknown = [n for n in names if n not in SHOTS]
    if unknown:
        return common.fail(f"unknown shot names: {', '.join(unknown)}", common.EXIT_PRECONDITION)
    try:
        built, folder = _preview(args.single)
    except site.Stop as stop:
        return common.fail(str(stop), stop.code)
    written, failed = [], []
    common.ensure_dir(folder_out)
    try:
        with Server(folder) as server:
            jobs = []
            for name in names:
                for size, (width, height) in SIZES.items():
                    for theme, page in (("light", "index.html"), ("dark", "index-dark.html")):
                        jobs.append((f"{name}.{size}.{theme}.png", page, f"t.shot.{name}", width, height, None))
            if "home" in names:
                jobs.append(("home.phone.forced-light.png", "index-forced-light.html", "t.shot.home", 400, 860, ["--force-dark-mode"]))
            if "prose" in names:
                jobs.append(("prose.mid.light.png", "index.html", "t.shot.prose", 1100, 800, None))
            jobs = [job + (None,) for job in jobs]
            for e in extras:
                for size in e.get("sizes") or list(SIZES):
                    width, height = SIZES[size]
                    for theme in e.get("themes") or ["light", "dark"]:
                        page = "index-dark.html" if theme == "dark" else "index.html"
                        jobs.append((f"{e['name']}.{size}.{theme}.png", page, e.get("route", ""), width, height, None, e))
            for file, page, route, width, height, extra, frame in jobs:
                try:
                    _shot(_framed(server, page, route, width, height, frame), folder_out / file, width, height, extra)
                    written.append(file)
                except preview.PreviewError as exc:
                    if exc.code == common.EXIT_PRECONDITION:
                        return common.fail(str(exc), common.EXIT_PRECONDITION)
                    failed.append(file)
    except OSError as exc:
        return common.fail(f"the local server could not start: {exc}", common.EXIT_TRANSIENT)
    sheet = None
    try:
        sheet = _sheet(folder_out, names) if names else None
    except preview.PreviewError:
        failed.append("sheet.png")
    result = {"ok": not failed, "out": common.rel(folder_out), "build": built["build"], "shots": written, "failed": failed,
              "sheet": common.rel(sheet) if sheet else None}
    if args.json:
        common.emit(result, args)
    else:
        lines = [f"web shots: {'ok' if not failed else 'FAILED'}; {len(written)} files in {result['out']}; sheet {result['sheet']}"]
        lines += [f"failed: {f}" for f in failed[:40]]
        common.emit("\n".join(lines), args)
    return common.EXIT_OK if not failed else common.EXIT_TRANSIENT
