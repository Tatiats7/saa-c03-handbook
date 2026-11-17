"""Test helper: copy the fixture book into a sandbox and run the tool against it.

    import sandbox                                  # tests/ is on sys.path under run.py

    class MyTest(unittest.TestCase):
        def setUp(self):
            self.book = sandbox.make("facts-" + self.id().split(".")[-1])
        def tearDown(self):
            sandbox.remove(self.book)

        def test_cli(self):
            code, out, err = sandbox.run(self.book, "facts", "verify", "--service", "widget", "--json")
            self.assertEqual(code, 0, err)

        def test_in_process(self):
            with sandbox.paths(self.book):          # common.BOOK, common.DATA, ... point at the sandbox
                from saalib import facts
                ...

A sandbox is always aws-saa-book/_build/tmp/<name>. Nothing here touches real data.
See tools/tests/fixtures/README.md.
"""
from __future__ import annotations

import contextlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
sys.path.insert(0, str(TOOLS))

from saalib import common  # noqa: E402

FIXTURE = HERE / "fixtures" / "book"
SAA = TOOLS / "saa.py"

# Every path attribute of common that is derived from common.BOOK, as (name, parts under BOOK).
_PATHS = [
    ("BUILD", ("_build",)), ("DATA", ("data",)), ("CORPUS", ("_build", "corpus")), ("SPEC_DIR", ("_build", "spec")),
    ("STYLE_DIR", ("_build", "style")), ("SCHEMA_DIR", ("_build", "schemas")), ("REGISTRY", ("_build", "registry")),
    ("LEDGER", ("_build", "ledger")), ("REPORTS", ("_build", "reports")), ("TMP", ("_build", "tmp")),
    ("SITE", ("_build", "site")), ("FACTS_DIR", ("data", "facts")), ("FACTSHEETS", ("facts",)),
    ("DIAGRAM_SRC", ("diagrams", "src")), ("DIAGRAM_SVG", ("diagrams", "svg")), ("EXPORTS", ("exports",)),
]


def make(name: str) -> Path:
    """Fresh copy of the fixture book at aws-saa-book/_build/tmp/<name>. Returns the sandbox path."""
    if not name or "/" in name or name.startswith("."):
        raise ValueError("sandbox name must be a plain folder name")
    dest = common.REAL_BOOK / "_build" / "tmp" / name
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(FIXTURE, dest)
    return dest


def remove(book: Path) -> None:
    book = Path(book).resolve()
    tmp = (common.REAL_BOOK / "_build" / "tmp").resolve()
    if tmp in book.parents and book.exists():
        shutil.rmtree(book)


def run(book: Path, *args: str, stdin: str | None = None):
    """Run `saa.py --book-dir <book> <args...>` in a new process. Returns (exit code, stdout, stderr)."""
    env = dict(os.environ)
    env.pop("SAA_BOOK_DIR", None)
    proc = subprocess.run([sys.executable, str(SAA), "--book-dir", str(book), *args],
                          capture_output=True, text=True, input=stdin, env=env, cwd=str(common.REPO))
    return proc.returncode, proc.stdout, proc.stderr


def run_json(book: Path, *args: str):
    """Like run(), with --json added; returns (exit code, parsed stdout or None, stderr)."""
    code, out, err = run(book, *args, "--json")
    try:
        return code, json.loads(out), err
    except ValueError:
        return code, None, err


@contextlib.contextmanager
def paths(book: Path):
    """Point every common.<PATH> at the sandbox for in-process tests, then restore."""
    book = Path(book).resolve()
    saved = {"BOOK": common.BOOK, **{name: getattr(common, name) for name, _ in _PATHS}}
    common.BOOK = book
    for name, parts in _PATHS:
        setattr(common, name, book.joinpath(*parts))
    try:
        yield book
    finally:
        for name, value in saved.items():
            setattr(common, name, value)


def edit_json(path: Path, change) -> None:
    """Load a JSON file, apply change(obj) (mutate in place or return a new object), write it back."""
    obj = common.read_json(path)
    result = change(obj)
    common.write_json(path, obj if result is None else result)


def edit_jsonl(path: Path, change) -> None:
    """Same for a JSONL file: change(rows) mutates the list or returns a new one."""
    rows = common.read_jsonl(path)
    result = change(rows)
    common.write_jsonl(path, rows if result is None else result)


def replace_text(path: Path, old: str, new: str, count: int = 1) -> None:
    text = Path(path).read_text(encoding="utf-8")
    if old not in text:
        raise AssertionError(f"{path}: text to replace not found: {old!r}")
    Path(path).write_text(text.replace(old, new, count), encoding="utf-8")
