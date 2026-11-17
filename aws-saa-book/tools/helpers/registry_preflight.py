"""Check `registry set` patch files against the corpus before they are applied.

Read-only on the book. Standard library only. It makes no network request.

    python3 aws-saa-book/tools/helpers/registry_preflight.py DIR --write-batch FILE
    python3 aws-saa-book/tools/helpers/registry_preflight.py DIR --check [--json]

DIR holds one patch per chapter, named `patch-<NN>.json` (the patch format of `saa.py registry set CH --file`).

`--write-batch FILE` writes every URL of the lists pages, faq, history, quotas and pricing, once, to FILE, for
`saa.py fetch --batch FILE`.

`--check` reports, per patch (code, then what it means):

  P01  the file is not a JSON object, or has a key that `registry set` does not take
  P02  a URL host is outside common.ALLOWED_HOSTS, or a guide root does not end with "/"
  P03  a URL is not in the corpus (fetch it first)
  P04  a URL was redirected: the path of final_url differs from the path of url (record the final URL instead)
  P05  the snapshot has no usable text (binary, or fewer than 200 characters)
  P06  a guide root has no index or no full.md (run `saa.py guide ROOT`), or the guide is a stub (fewer than 3 pages)
  P07  a faq URL has no parsed question in the faq index (run `saa.py faq URL`)
  P08  a bullet or task id is not in exam-guide.json
  P09  a cards key is not a service of the chapter, or a mapped key is a service of no chapter
  P10  `notes` is longer than the registry limit, or does not say that it is third-party research
  P11  a What's New tag or a case-study tag is not in the saved tag lists
  W12  (warning) more bullets than written questions of the chapter template: each bullet needs a question slot
  W13  (warning) a chapter with services has no guide

Exit 0 when there is no error, 1 with errors, 3 when DIR has no patch.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from saalib import common  # noqa: E402

URL_LISTS = ("pages", "faq", "history", "quotas", "pricing")
PATCH_KEYS = ("sources", "tasks", "bullets", "service_map", "cards", "notes")
SOURCE_LISTS = ("guides",) + URL_LISTS + ("whatsnew_tags", "case_tags")
NOTES_MAX_CHARS = 2000
NOTE_MARK = "third-party research"
MIN_TEXT_CHARS = 200
_RE_PATCH = re.compile(r"^patch-(\d{2})\.json$")


def _page_path(url: str) -> str:
    """The URL path without the page extension (the comparison rule of registry R16)."""
    path = urllib.parse.urlsplit(url or "").path
    for ext in (".html", ".htm", ".md"):
        if path.endswith(ext):
            return path[:-len(ext)]
    return path.rstrip("/")


def _host_ok(url: str) -> bool:
    try:
        parts = urllib.parse.urlsplit(url)
    except ValueError:
        return False
    return parts.scheme == "https" and (parts.hostname or "").lower() in common.ALLOWED_HOSTS


def load_patches(folder: Path) -> list:
    """[(chapter id, path, object or None)] for every patch-<NN>.json of the folder, by chapter id."""
    out = []
    for path in sorted(Path(folder).glob("patch-*.json")):
        match = _RE_PATCH.match(path.name)
        if not match:
            continue
        try:
            obj = json.loads(path.read_text(encoding="utf-8"))
        except ValueError:
            obj = None
        out.append((match.group(1), path, obj))
    return out


def urls_of(patches) -> list:
    """Every URL of the URL lists, once, in first-seen order."""
    seen, out = set(), []
    for _, _, obj in patches:
        sources = (obj or {}).get("sources") or {} if isinstance(obj, dict) else {}
        for name in URL_LISTS:
            for url in sources.get(name) or []:
                if isinstance(url, str) and url not in seen:
                    seen.add(url)
                    out.append(url)
    return out


def _template_write(ch: dict, spec: dict):
    """Number of questions the chapter template writes, or None when it has no questions."""
    override = (spec.get("chapter_overrides") or {}).get(ch["id"]) or {}
    key = override.get("template") or ch.get("kind") or ch.get("tier")
    counts = dict(((spec.get("templates") or {}).get(key) or {}).get("counts") or {})
    counts.update(override.get("counts") or {})
    questions = counts.get("questions") or {}
    return questions.get("write") if questions.get("shipped") else None


def _whatsnew_tags() -> set:
    store = common.read_json(common.CORPUS / "changes" / "_tags.json", {}) or {}
    return {record.get("tag") or tag_id.rsplit("#", 1)[-1]
            for tag_id, record in (store.get("tags") or {}).items()
            if record.get("namespace") == "whats-new-v2#general-products"}


def _case_tags() -> set:
    tags = set()
    for row in common.read_jsonl(common.CORPUS / "cases" / "index.jsonl"):
        tags.update(row.get("tags") or [])
    return tags


class _Corpus:
    """Snapshot lookup by URL: by source id first, then by the `url` of any saved meta (TOOLS.md section 0, rule 11)."""

    def __init__(self, corpus):
        self.corpus = corpus
        self._by_url = None

    def meta(self, url: str):
        meta = self.corpus.load_meta(self.corpus.source_id_for(url))
        if meta is not None:
            return meta
        if self._by_url is None:
            self._by_url = {}
            base = common.CORPUS / "snap"
            for path in sorted(base.rglob("*.meta.json")) if base.is_dir() else []:
                try:
                    row = common.read_json(path) or {}
                except ValueError:
                    continue
                if row.get("url"):
                    self._by_url.setdefault(row["url"], row)
        return self._by_url.get(url)

    def text(self, url: str, meta: dict) -> str:
        return self.corpus.load_text(meta.get("source_id") or self.corpus.source_id_for(url)) or ""


def check(folder: Path) -> dict:
    """Run every check. Returns {"ok", "patches", "errors", "warnings", "chapters"}."""
    from saalib import corpus, feeds

    patches = load_patches(folder)
    book = common.load_book()
    chapters = {ch["id"]: ch for ch in book["chapters"]}
    all_keys = {key for ch in book["chapters"] for key in ch.get("services", [])}
    guide = common.read_json(common.REGISTRY / "exam-guide.json", {}) or {}
    bullet_ids = {b["id"] for b in guide.get("bullets", [])}
    task_ids = {t["id"] for t in guide.get("tasks", [])}
    spec = common.read_json(common.STYLE_DIR / "SPEC.json", {}) or {}
    whatsnew, cases = _whatsnew_tags(), _case_tags()
    snapshots = _Corpus(corpus)
    errors, warnings, rows = [], [], []

    def add(bucket, code, chapter, msg):
        bucket.append({"code": code, "chapter": chapter, "msg": msg})

    for cid, path, obj in patches:
        ch = chapters.get(cid)
        if not isinstance(obj, dict) or ch is None:
            add(errors, "P01", cid, f"{path.name} is not a JSON object for a known chapter")
            continue
        for key in obj:
            if key not in PATCH_KEYS:
                add(errors, "P01", cid, f"key `{key}` is not a patch key of registry set")
        sources = obj.get("sources") or {}
        for name in sources:
            if name not in SOURCE_LISTS:
                add(errors, "P01", cid, f"sources.{name} is not a source list")
        for root in sources.get("guides") or []:
            if not _host_ok(root) or not root.endswith("/"):
                add(errors, "P02", cid, f"sources.guides: {root} is not an allowed guide root")
                continue
            index = corpus.load_index(corpus.guide_id_for(root))
            if not index:
                add(errors, "P06", cid, f"sources.guides: no index for {root}")
            elif not index.get("full_md") or (index.get("page_count") or 0) < 3:
                add(errors, "P06", cid, f"sources.guides: {root} is a stub or has no full.md "
                                        f"({index.get('page_count')} pages)")
        for name in URL_LISTS:
            for url in sources.get(name) or []:
                if not _host_ok(url):
                    add(errors, "P02", cid, f"sources.{name}: host of {url} is not allowed")
                    continue
                meta = snapshots.meta(url)
                if meta is None:
                    add(errors, "P03", cid, f"sources.{name}: {url} is not in the corpus")
                    continue
                if meta.get("final_url") and _page_path(meta["final_url"]) != _page_path(meta.get("url") or url):
                    add(errors, "P04", cid, f"sources.{name}: {url} was redirected to {meta['final_url']}")
                text = snapshots.text(url, meta)
                if meta.get("kind") == "binary" or len(text.strip()) < MIN_TEXT_CHARS:
                    add(errors, "P05", cid, f"sources.{name}: {url} has no usable text "
                                            f"(kind {meta.get('kind')}, {len(text.strip())} characters)")
                if name == "faq":
                    faq_rows = common.read_jsonl(common.CORPUS / "faq" / f"{feeds.faq_name_for(url)}.jsonl")
                    if not any(row.get("url") == url or row.get("final_url") == url for row in faq_rows):
                        add(errors, "P07", cid, f"sources.faq: no parsed question for {url}")
        for bullet in obj.get("bullets") or []:
            if bullet not in bullet_ids:
                add(errors, "P08", cid, f"bullet {bullet} is not in exam-guide.json")
        for task in obj.get("tasks") or []:
            if task not in task_ids:
                add(errors, "P08", cid, f"task {task} is not in exam-guide.json")
        for key in obj.get("cards") or []:
            if key not in ch.get("services", []):
                add(errors, "P09", cid, f"cards key {key} is not a service of the chapter")
        for official, keys in (obj.get("service_map") or {}).items():
            for key in keys:
                if key not in all_keys:
                    add(errors, "P09", cid, f"mapped key {key} ({official}) is a service of no chapter")
        note = obj.get("notes")
        if note is not None:
            if not isinstance(note, str) or len(note) > NOTES_MAX_CHARS:
                size = len(note) if isinstance(note, str) else "not a string"
                add(errors, "P10", cid, f"notes has {size} characters; the limit is {NOTES_MAX_CHARS}")
            elif NOTE_MARK not in note:
                add(errors, "P10", cid, f"notes does not say `{NOTE_MARK}`")
        for tag in sources.get("whatsnew_tags") or []:
            if tag not in whatsnew:
                add(errors, "P11", cid, f"What's New tag {tag} is not in changes/_tags.json")
        for tag in sources.get("case_tags") or []:
            if tag not in cases:
                add(errors, "P11", cid, f"case-study tag {tag} is not in cases/index.jsonl")
        write = _template_write(ch, spec)
        bullets = obj.get("bullets") or []
        if write is not None and len(bullets) > write:
            add(warnings, "W12", cid, f"{len(bullets)} bullets but the template writes {write} questions")
        if ch.get("services") and not sources.get("guides"):
            add(warnings, "W13", cid, "the chapter has services but the patch has no guide")
        rows.append({"chapter": cid, "guides": len(sources.get("guides") or []),
                     "urls": sum(len(sources.get(name) or []) for name in URL_LISTS),
                     "bullets": len(bullets), "questions_written": write, "cards": len(obj.get("cards") or []),
                     "notes_chars": len(note) if isinstance(note, str) else 0})
    return {"ok": not errors, "patches": len(patches), "errors": errors, "warnings": warnings, "chapters": rows}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("folder", help="folder with patch-<NN>.json files, inside aws-saa-book/")
    parser.add_argument("--write-batch", metavar="FILE", help="write the URLs of all patches to FILE")
    parser.add_argument("--check", action="store_true", help="check the patches against the corpus and the registry")
    parser.add_argument("--json", action="store_true", help="print the check result as JSON")
    args = parser.parse_args(argv)
    folder = Path(args.folder)
    if not folder.is_absolute():
        folder = common.REPO / folder
    if not common.inside_book(folder):
        return common.fail(f"the folder must be inside {common.REAL_BOOK}", common.EXIT_POLICY)
    patches = load_patches(folder)
    if not patches:
        return common.fail(f"no patch-<NN>.json in {common.rel(folder)}", common.EXIT_PRECONDITION)
    if args.write_batch:
        out = Path(args.write_batch)
        if not out.is_absolute():
            out = common.REPO / out
        if not common.inside_book(out):
            return common.fail(f"--write-batch must be inside {common.REAL_BOOK}", common.EXIT_POLICY)
        urls = urls_of(patches)
        common.ensure_dir(out.parent)
        out.write_text("\n".join(urls) + "\n", encoding="utf-8")
        print(f"wrote {common.rel(out)}: {len(urls)} URLs from {len(patches)} patches")
    if not args.check:
        return common.EXIT_OK
    result = check(folder)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=1))
    else:
        print(f"preflight: {'ok' if result['ok'] else 'FAIL'} patches={result['patches']} "
              f"errors={len(result['errors'])} warnings={len(result['warnings'])}")
        for kind in ("errors", "warnings"):
            for finding in result[kind]:
                print(f"  {finding['chapter']}: {finding['code']} {finding['msg']}")
        for row in result["chapters"]:
            print(f"  ch {row['chapter']}: guides={row['guides']} urls={row['urls']} bullets={row['bullets']}"
                  f"/{row['questions_written']} cards={row['cards']} notes={row['notes_chars']} chars")
    return common.EXIT_OK if result["ok"] else common.EXIT_FAIL


if __name__ == "__main__":
    raise SystemExit(main())
