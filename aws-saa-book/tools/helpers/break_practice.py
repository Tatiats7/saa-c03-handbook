"""Gate breaker for the practice gates (questions, packs, adjudication, mocks, cards, speak, tasks, diagrams).

Run from the repo root:  python3 aws-saa-book/tools/helpers/break_practice.py [--only N,N] [--no-uv]

Every attempt runs in a fresh copy of the fixture book at aws-saa-book/_build/tmp/breaker-practice
(through tests/sandbox.py, so no real data is touched). The script writes
aws-saa-book/_build/reports/gate-break-practice.json and gate-break-practice.md. It fixes nothing.
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / "tests"))

import sandbox  # noqa: E402
from saalib import common, lab, qbank  # noqa: E402

NAME = "breaker-practice"
SEED = 20261004
SOURCE = "docs/fixture/widget-store/limits"
QF = ("data", "99-sample", "questions.json")
CF = ("data", "99-sample", "cards.json")
SF = ("data", "99-sample", "speak.json")
TF = ("data", "99-sample", "tasks.json")
ATTEMPTS = []


class Rec:
    def __init__(self):
        self.book = None
        self.steps = []

    def fresh(self):
        self.book = sandbox.make(NAME)
        # the fixture SPEC switches the overlap rule off (1.0); use the value of the real SPEC.json
        sandbox.edit_json(self.book / "_build" / "style" / "SPEC.json",
                          lambda s: s["questions"].update(stem_key_overlap_margin_max=0.25))
        return self.book

    def p(self, *parts):
        return self.book.joinpath(*parts)

    def write(self, name, obj):
        path = self.p("in", name)
        common.write_json(path, obj)
        return str(path)

    def run(self, *args, text=False, label=None):
        if text:
            rc, out, err = sandbox.run(self.book, *args)
            res = None
        else:
            rc, res, err = sandbox.run_json(self.book, *args)
            out = ""
        msg = summ(res, out, err)
        shown = " ".join(a if len(a) < 60 else "<" + Path(a).name + ">" for a in args)
        self.steps.append({"cmd": label or shown, "exit": rc, "msg": msg})
        return rc, (res if not text else out)

    def note(self, cmd, msg, rc="-"):
        self.steps.append({"cmd": cmd, "exit": rc, "msg": msg})


def summ(res, out, err):
    parts = []
    if isinstance(res, dict):
        for key in ("rejected", "refused"):
            for r in res.get(key) or []:
                if isinstance(r, dict):
                    for f in (r.get("errors") or [])[:3]:
                        parts.append(f"{f.get('code')} {f.get('msg')}")
        for f in (res.get("errors") or [])[:3]:
            if isinstance(f, dict):
                parts.append(f"{f.get('code')} {f.get('msg')}")
        for m in res.get("mocks") or []:
            for f in (m.get("errors") or [])[:3]:
                parts.append(f"{f.get('code')} {f.get('msg')}")
        if not parts:
            slim = {k: v for k, v in res.items() if k not in ("warnings", "counts", "commands", "chapters", "inputs")}
            parts.append(json.dumps(slim, ensure_ascii=False))
    else:
        lines = [l for l in ((out or "") + "\n" + (err or "")).splitlines() if l.strip()]
        parts = lines[:3]
    text = " | ".join(parts)
    return text if len(text) <= 300 else text[:297] + "..."


def attempt(gate, title, did, repro=None, severity="medium"):
    def deco(fn):
        ATTEMPTS.append({"gate": gate, "title": title, "did": did, "repro": repro, "severity": severity, "fn": fn})
        return fn
    return deco


# ---------------------------------------------------------------- builders

def stored(rec, parts, iid):
    return copy.deepcopy(next(i for i in common.read_json(rec.p(*parts))["items"] if i["id"] == iid))


def new_q(rec, base="sample-q004", change=None, keep_id=False):
    q = stored(rec, QF, base)
    if not keep_id:
        del q["id"]
    q["twin_of"] = None
    q.pop("worked", None)
    q["concept"] = "breaker-concept"
    if change:
        change(q)
    return q


def add_q(rec, q, *extra, name="q.json"):
    return rec.run("q", "add", "--chapter", "99", "--file", rec.write(name, q), "--by", "breaker", *extra)


def added(rc, res):
    return rc == 0 and isinstance(res, dict) and bool(res.get("added") or res.get("replaced"))


def candidates(rec):
    def change(doc):
        for q in doc["items"]:
            q["status"] = "candidate"
            q["verification"] = {"status": "candidate", "round": 0, "solvers": []}
    sandbox.edit_json(rec.p(*QF), change)


def answers(rec, lens, rnd=0, wrong=None, only=None, solver="default", tweak=None, pack=None):
    rows = []
    for q in common.read_json(rec.p(*QF))["items"]:
        if only and q["id"] not in only:
            continue
        order = qbank.permutation(SEED, q["id"], lens, rnd, [o["id"] for o in q["options"]])
        labels = {oid: qbank.LABELS[n] for n, oid in enumerate(order)}
        key = sorted(labels[o["id"]] for o in q["options"] if o["correct"])
        if q["id"] == wrong:
            key = sorted(labels[o["id"]] for o in q["options"] if not o["correct"])[:len(key)]
        row = {"id": q["id"], "answer": key, "flag": None, "stem_only": None, "citations": None, "case": None}
        if lens == "closed":
            row["stem_only"] = "my solution before the options"
        if lens == "ambiguity":
            row["case"] = {"label": "A", "text": "the strongest case for a wrong option"}
        if lens == "open":
            row["citations"] = {label: ["widget-shelf-scope"] for label in labels.values()}
        if tweak:
            tweak(lens, row, labels, q)
        rows.append(row)
    doc = {"pack": pack or f"sample-r{rnd}-{lens}", "lens": lens, "answers": rows}
    if solver == "default":
        doc["solver"] = f"solver-{lens}"
    elif solver is not None:
        doc["solver"] = solver
    return rec.write(f"answers-{lens}-r{rnd}.json", doc)


def adjudicate(rec, files):
    return rec.run("q", "adjudicate", "--chapter", "99", "--answers", *files, label="q adjudicate --chapter 99 --answers closed open ambiguity")


def q_state(rec, qid):
    q = stored(rec, QF, qid)
    return q["status"], q["verification"]["status"], q["verification"].get("round")


LEAK_OPTIONS = ["A crate that the company packs, labels and ships by air freight to the partner in ap-south-1.",
                "The existing shelf, moved.", "A second shelf.", "A higher shelf quota."]


def leak(q):
    for o, text in zip(q["options"], LEAK_OPTIONS):
        o["text"] = text


# ---------------------------------------------------------------- questions: q add, q lint, dedupe

@attempt("q add", "Control: two correct options on a single-answer question",
         "sample-q004 copy; option b also marked correct.")
def a_two_correct(rec):
    def ch(q):
        q["options"][1].update(correct=True, trap=None, misconception=None, distractor_type=None)
    rc, res = add_q(rec, new_q(rec, change=ch))
    return added(rc, res), "Q102 holds."


@attempt("q add", "Control: multiple-response question with one key",
         "sample-q003 copy (Select TWO); option b set to wrong.")
def a_multi_one_key(rec):
    def ch(q):
        q["options"][1].update(correct=False, misconception="breaker", distractor_type="different-problem")
    rc, res = add_q(rec, new_q(rec, base="sample-q003", change=ch))
    return added(rc, res), "Q102 holds."


@attempt("q add", "Two options with the same text, one marked correct and one marked wrong",
         "sample-q004 copy; option c gets the exact text of the key (option a). The question now has two correct "
         "answers in fact, and only one is keyed.",
         repro="q add a single-answer question where options[0].text == options[2].text, options[0].correct true, options[2].correct false.",
         severity="high")
def a_same_text(rec):
    def ch(q):
        q["options"][2]["text"] = q["options"][0]["text"]
    rc, res = add_q(rec, new_q(rec, change=ch))
    return added(rc, res), "No rule compares option texts; Q102 checks only that option ids are unique."


@attempt("q add", "Key leaked through option length (short options)",
         "sample-q004 copy; key has 17 words, the three wrong options 4, 3 and 4 words. Mean is 7 words, so Q104 "
         "(applies from a mean of 10 words) never runs.",
         repro="q add a difficulty-1 single question with option word counts 17 (key), 4, 3, 4.",
         severity="high")
def a_len_short(rec):
    rc, res = add_q(rec, new_q(rec, change=leak))
    return added(rc, res), "Q104 is switched off below a mean of 10 words; Q202 (key is longest) is a chapter warning and needs 10 questions."


@attempt("q add", "Key is the longest option, just inside the 30% spread",
         "sample-q004 copy; key has 15 words, every wrong option 11. Each option is within 30% of the mean (12), "
         "but the key is 36% longer than each distractor.",
         repro="q add a single question with option word counts 15 (key), 11, 11, 11.", severity="low")
def a_len_spread(rec):
    def ch(q):
        texts = ["A crate that the company fills with the 40 widgets and ships to the partner.",
                 "The existing shelf, moved from us-east-1 to ap-south-1 by the company.",
                 "A second shelf that the company creates in the us-east-1 Region.",
                 "A higher quota for the shelves of the account in us-east-1."]
        for o, t in zip(q["options"], texts):
            o["text"] = t
    rc, res = add_q(rec, new_q(rec, change=ch))
    return added(rc, res), "Q104 measures the distance to the mean, and the long key pulls the mean up. Only Q202 looks at 'key is longest', as a bank share."


@attempt("q add", "Key leaked through word overlap with the stem (long stem dilutes the Jaccard value)",
         "Key = 'A crate to send the partner the widgets next week from the shelf.' (6 of its 7 content words come "
         "from the stem); wrong options share no word with the stem. Step 1 with the short fixture stem (control), "
         "step 2 with one more story sentence of 26 words in the stem. SPEC margin set to the real value 0.25.",
         repro="q add a question whose key is built from stem words, whose distractors share none, and whose stem has about 30 content words (every real stem: the real minimum is 60 words).",
         severity="high")
def a_overlap(rec):
    def ch(q):
        texts = ["A crate to send the partner the widgets next week from the shelf.", "A forklift rental.",
                 "An extra ticket desk.", "A bigger loading dock."]
        for o, t in zip(q["options"], texts):
            o["text"] = t
    rc, res = add_q(rec, new_q(rec, change=ch), name="q-short.json")
    control_rejected = not added(rc, res)

    def ch2(q):
        ch(q)
        q["stem"] = q["stem"].replace("Which Amazon", "The finance team, the legal team and the operations group reviewed the contract, approved "
                                      "the budget, signed the paperwork and scheduled a carrier for Tuesday morning. Which Amazon")
    rc, res = add_q(rec, new_q(rec, change=ch2), name="q-long.json")
    return added(rc, res), ("The short-stem control is rejected by Q113. " if control_rejected else "Even the short-stem form passed. ") + \
        "Jaccard divides by the union, so a longer stem lowers the key overlap below the margin while the key still consists of stem words only."


@attempt("q add", "Explanation names options by position and letter without the word 'Option'",
         "Step 1 control: 'Option B' in the explanation. Step 2: 'The second option is wrong, and (C) is wrong too; B is the usual trap.'",
         repro="q add with explanation text 'The second option is wrong, and (C) is wrong too; B is the usual trap.'", severity="medium")
def a_letter(rec):
    def c1(q):
        q["explanation"] += " Option B is wrong."
    rc, res = add_q(rec, new_q(rec, change=c1), name="q-c.json")

    def c2(q):
        q["explanation"] += " The second option is wrong, and (C) is wrong too; B is the usual trap."
    rc, res = add_q(rec, new_q(rec, change=c2))
    return added(rc, res), "letter_reference_regex needs the word Option, Answer or Choice before the letter. Options print without letters and the app can shuffle them, so these references point at the wrong option."


@attempt("q add / q lint / gate questions", "Exact copy of an existing question under a new id",
         "sample-q001 copied without id, concept renamed. Then q lint 99, the questions gate, and q lint --all.",
         repro="q add a copy of a stored question without its id and with another concept; run gate 99 --gate questions.", severity="high")
def a_exact_dup(rec):
    rc, res = add_q(rec, new_q(rec, base="sample-q001"))
    ok_add = added(rc, res)
    rc2, _ = rec.run("q", "lint", "99")
    rc3, _ = rec.run("gate", "99", "--gate", "questions")
    rc4, _ = rec.run("q", "lint", "--all")
    rc5, _ = rec.run("q", "dedupe")
    through = ok_add and rc2 != 1 and rc3 != 1
    return through, f"q add and the questions gate accept the copy; only q lint --all (exit {rc4}) and q dedupe (exit {rc5}) see it, and no ledger stage runs them for a chapter."


@attempt("q dedupe / q lint --all", "Near-duplicate with reordered words",
         "sample-q001 with the clauses of every sentence reordered (same facts, same options, same key). Then q dedupe, q lint --all and the questions gate.",
         repro="q add sample-q001 (no id, other concept) with the stem 'On one shelf in the us-east-1 Region of Amazon Widget Store, a company keeps 400 widgets. Next month the company expects to add 300 more widgets. All widgets must stay in us-east-1, a compliance rule states. With the LEAST operational overhead, which solution will meet these requirements?'; run q dedupe.",
         severity="high")
def a_reorder(rec):
    def ch(q):
        q["stem"] = ("On one shelf in the us-east-1 Region of Amazon Widget Store, a company keeps 400 widgets. Next month the company "
                     "expects to add 300 more widgets. All widgets must stay in us-east-1, a compliance rule states. With the LEAST "
                     "operational overhead, which solution will meet these requirements?")
    rc, res = add_q(rec, new_q(rec, base="sample-q001", change=ch))
    ok_add = added(rc, res)
    rc2, pairs = rec.run("q", "dedupe")
    rc3, _ = rec.run("q", "lint", "--all")
    rc4, _ = rec.run("gate", "99", "--gate", "questions")
    dup = [p for p in (pairs or {}).get("pairs", []) if p["kind"] == "duplicate"]
    a = qbank._shingles(stored(rec, QF, "sample-q001")["stem"])
    items = common.read_json(rec.p(*QF))["items"]
    sim = qbank._jac(a, qbank._shingles(items[-1]["stem"])) if ok_add else None
    return ok_add and not dup and rc3 != 1, f"3-word shingle similarity of the two stems is {sim:.2f} (threshold 0.6). Options are never compared."


@attempt("q add", "Negative stem written in lowercase",
         "Last sentence changed to 'Which Amazon Widget Store resource is not a way to send the 40 widgets?'",
         repro="q add with a stem that asks 'which ... is not ...' in lowercase.", severity="low")
def a_negative(rec):
    def ch(q):
        q["stem"] = q["stem"].replace("should the company use to send the 40 widgets?", "is not a way to send the 40 widgets?")
        q["keywords"] = ["needs 40 of the widgets"]
    rc, res = add_q(rec, new_q(rec, change=ch))
    return added(rc, res), "negative_stem_regex matches only NOT and EXCEPT in capitals. The lowercase form is the harder one for this reader."


@attempt("q add", "'None of these options.' as an option",
         "Option d text set to 'None of these options.' (banned list holds 'none of the above').",
         repro="q add with an option text 'None of these options.'", severity="low")
def a_none(rec):
    def ch(q):
        q["options"][3]["text"] = "None of these options."
    rc, res = add_q(rec, new_q(rec, change=ch))
    return added(rc, res), "banned_in_options is a list of four literal phrases."


@attempt("q add", "Control: status ready and a passed verification smuggled in the input file",
         "Input item carries status ready and verification.status pass.")
def a_smuggle(rec):
    def ch(q):
        q["status"] = "ready"
        q["verification"] = {"status": "pass", "round": 0, "solvers": [], "checked": "2026-10-04"}
    rc, res = add_q(rec, new_q(rec, change=ch))
    qid = (res.get("added") or [None])[0]
    state = q_state(rec, qid) if qid else None
    rec.note("stored state", str(state))
    return bool(state and state[0] == "ready"), "q add resets status and verification."


# ---------------------------------------------------------------- packs

@attempt("q pack", "Control: a pack holds no key, why or explanation",
         "All four questions set to candidate; q pack --lens closed; searched the file for correct, why, explanation, trap, facts.")
def a_pack_keys(rec):
    candidates(rec)
    out = rec.p("pack-closed.json")
    rc, _ = rec.run("q", "pack", "--chapter", "99", "--lens", "closed", "--out", str(out), text=True, label="q pack --chapter 99 --lens closed --out pack-closed.json")
    text = out.read_text(encoding="utf-8")
    found = [w for w in ('"correct"', '"why"', '"explanation"', '"trap"', '"facts"', '"keywords"', '"concept"') if w in text]
    rec.note("search the pack", f"leaking keys found: {found}")
    return bool(found), "Pack items hold only id, type, select, stem, options (label, text)."


@attempt("q pack", "Stored option order recovered from a pack (the shuffle is reversible)",
         "A solver reads data/book.json (mock_seed), recomputes random.Random(sha256('<seed>|<id>|<lens>|<round>')) on the positions "
         "0..n-1 and maps each label back to the stored position. Then it answers 'the option stored first'.",
         repro="python: order = qbank.permutation(book['book']['mock_seed'], item['id'], pack['lens'], pack['round'], range(len(item['options']))); the label at order.index(0) is the option stored first.",
         severity="medium")
def a_pack_unshuffle(rec):
    candidates(rec)
    out = rec.p("pack-closed.json")
    rec.run("q", "pack", "--chapter", "99", "--lens", "closed", "--out", str(out), text=True, label="q pack --chapter 99 --lens closed --out pack-closed.json")
    pack = common.read_json(out)
    seed = common.read_json(rec.p("data", "book.json"))["book"]["mock_seed"]
    truth = {q["id"]: q for q in common.read_json(rec.p(*QF))["items"]}
    recovered = hits = keys = 0
    for item in pack["items"]:
        order = qbank.permutation(seed, item["id"], pack["lens"], pack["round"], list(range(len(item["options"]))))
        texts = [None] * len(order)
        for n, pos in enumerate(order):
            texts[pos] = item["options"][n]["text"]
        q = truth[item["id"]]
        recovered += texts == [o["text"] for o in q["options"]]
        guess = set(texts[:q["select"]])
        key = {o["text"] for o in q["options"] if o["correct"]}
        hits += guess == key
        keys += 1
    rec.note("unshuffle with the public seed", f"stored order recovered for {recovered} of {keys} questions; 'first stored options' equals the key in {hits} of {keys}")
    return ("partial" if recovered == keys else False), ("The seed is in data/book.json and the other inputs are in the pack, so the shuffle hides nothing from a solver that can read the book folder. "
            "It leaks the key as far as writers store the key first (fixture: 3 of 4). Q202 limits the position share only from 10 questions and only as a chapter warning.")


# ---------------------------------------------------------------- adjudication

def _adj(rec, **kw):
    candidates(rec)
    return [answers(rec, lens, **kw) for lens in qbank.LENSES]


@attempt("q adjudicate", "Control: only two answer files (one solver missing)",
         "Answer files of the closed and open lens only.")
def a_adj_two(rec):
    files = _adj(rec)
    rc, _ = rec.run("q", "adjudicate", "--chapter", "99", "--answers", files[0], files[1], text=True, label="q adjudicate --answers closed open")
    return rc == 0 and q_state(rec, "sample-q004")[1] == "pass", "Exit 3."


@attempt("q adjudicate", "Control: one lens has no answer for one question",
         "The ambiguity file leaves out sample-q004.")
def a_adj_missing_row(rec):
    candidates(rec)
    files = [answers(rec, "closed"), answers(rec, "open"), answers(rec, "ambiguity", only={"sample-q001", "sample-q002", "sample-q003"})]
    rc, res = adjudicate(rec, files)
    return "sample-q004" in (res or {}).get("pass", []), "The question goes to needs_edit ('ambiguity missing')."


@attempt("q adjudicate", "Answer files without a solver field",
         "Three answer files with no 'solver' key at all.",
         repro="q adjudicate with three answer files that have pack, lens, answers and no solver.", severity="medium")
def a_adj_nosolver(rec):
    files = _adj(rec, solver=None)
    rc, res = adjudicate(rec, files)
    solvers = [s.get("solver") for s in stored(rec, QF, "sample-q004")["verification"]["solvers"]]
    rec.note("stored solvers", str(solvers))
    return len((res or {}).get("pass", [])) == 4, "A missing solver is stored as 'unknown' and the question passes."


@attempt("q adjudicate", "One solver (the question's author) signs all three lenses",
         "Three answer files, all with solver 'breaker', the label that wrote the questions with q add --by breaker.",
         repro="q adjudicate with three answer files whose solver is the same label for all lenses.", severity="high")
def a_adj_same(rec):
    files = _adj(rec, solver="breaker")
    rc, res = adjudicate(rec, files)
    return len((res or {}).get("pass", [])) == 4, "Nothing requires three different solvers, and questions store no author, so the writer can be all three solvers (facts vote refuses the author; q adjudicate does not)."


@attempt("q adjudicate", "Closed lens without stem_only, ambiguity lens without a case",
         "stem_only null in the closed file; case null in the ambiguity file.",
         repro="q adjudicate with stem_only null and case null in every row.", severity="medium")
def a_adj_empty_lens(rec):
    def tweak(lens, row, labels, q):
        row["stem_only"] = None
        row["case"] = None
    files = _adj(rec, tweak=tweak)
    rc, res = adjudicate(rec, files)
    return len((res or {}).get("pass", [])) == 4, "The fields that make the lenses different are optional, so three identical 'pick the labels' runs count as three lenses."


@attempt("q adjudicate", "Open-book citations: one unrelated fact id, or the one-word quote 'the', for every label",
         "Step 1: every label cites the fact widget-shelf-max-widgets (unrelated to most options). Step 2: every label cites {source_id, quote: 'the'}.",
         repro="open answer file with citations {A: [{source_id: 'docs/fixture/widget-store/limits', quote: 'the'}], B: same, ...}.", severity="high")
def a_adj_cites(rec):
    def t1(lens, row, labels, q):
        if lens == "open":
            row["citations"] = {label: ["widget-shelf-max-widgets"] for label in labels.values()}
    files = _adj(rec, tweak=t1)
    rc, res = adjudicate(rec, files)
    first = len((res or {}).get("pass", [])) == 4

    def t2(lens, row, labels, q):
        if lens == "open":
            row["citations"] = {label: [{"source_id": SOURCE, "quote": "the"}] for label in labels.values()}
    files = _adj(rec, tweak=t2)
    rc, res = adjudicate(rec, files)
    second = len((res or {}).get("pass", [])) == 4
    ok = stored(rec, QF, "sample-q004")["verification"]["solvers"][1].get("citations_ok")
    rec.note("stored citations_ok", str(ok))
    return first and second, "A citation only has to exist: any verified fact, or any substring of any snapshot (no minimum length, no link to the option or to the question's facts)."


@attempt("q adjudicate", "Two rows for one question in one answer file (first agrees, second disagrees and flags)",
         "The ambiguity file holds sample-q004 twice: first the key, then a wrong answer with a flag.",
         repro="answer file with two rows of the same id; the first row is the key.", severity="low")
def a_adj_dup_rows(rec):
    candidates(rec)
    amb = answers(rec, "ambiguity")
    doc = common.read_json(Path(amb))
    row = copy.deepcopy(next(r for r in doc["answers"] if r["id"] == "sample-q004"))
    row["answer"] = ["A", "B"]
    row["flag"] = "two answers are defensible"
    doc["answers"].append(row)
    common.write_json(Path(amb), doc)
    rc, res = adjudicate(rec, [answers(rec, "closed"), answers(rec, "open"), amb])
    return "sample-q004" in (res or {}).get("pass", []), "Only the first row of an id is read; the flag in the second row is dropped silently."


@attempt("q adjudicate", "Old answer files applied to a question that was replaced after the packs went out",
         "Honest answer files built for the fixture questions. Then q add --replace swaps sample-q004 for the length-leak version "
         "(new option texts, same key id) while it is still a round-0 candidate. Then q adjudicate with the old files.",
         repro="q pack; solvers answer; q add --replace <same id, new stem or options, same key id>; q adjudicate with the old answer files.",
         severity="high")
def a_adj_stale(rec):
    files = _adj(rec)
    rc, res = add_q(rec, new_q(rec, keep_id=True, change=lambda q: (leak(q), q.update(concept="shelf-vs-crate"))), "--replace")
    rc, res = adjudicate(rec, files)
    state = q_state(rec, "sample-q004")
    rec.note("state of sample-q004", str(state))
    return "sample-q004" in (res or {}).get("pass", []), "Answer files carry no rev, keyRev or content hash, and a round-0 replace keeps rev. The stored text was never seen by a solver, yet it is 'verified, pass'."


@attempt("q add --replace", "More than one edit after a failed round",
         "Round 0 fails for sample-q004 (closed disagrees). Then q add --replace twice with different takeaways.",
         repro="after a round-0 failure run q add --replace on the same id twice.", severity="medium")
def a_two_edits(rec):
    candidates(rec)
    adjudicate(rec, [answers(rec, "closed", wrong="sample-q004"), answers(rec, "open"), answers(rec, "ambiguity")])
    r1 = add_q(rec, new_q(rec, keep_id=True, change=lambda q: q.update(concept="shelf-vs-crate", takeaway="Widgets that travel go in a crate, and widgets that stay go on a shelf.")), "--replace", name="e1.json")
    r2 = add_q(rec, new_q(rec, keep_id=True, change=lambda q: q.update(concept="shelf-vs-crate", takeaway="A crate carries widgets between Regions, and a shelf keeps widgets in place.")), "--replace", name="e2.json")
    q = stored(rec, QF, "sample-q004")
    rec.note("state of sample-q004", f"rev={q['rev']} round={q['verification']['round']} status={q['status']}")
    return added(*r1) and added(*r2), "RULINGS: 'unanimous or one edit then reject'. The tool counts no edits in round 1; rev just goes up."


@attempt("q add", "A rejected question comes back under a new id",
         "sample-q004 fails round 0 and round 1 and is rejected. The same content is then added again without an id.",
         repro="let a question be rejected in round 1; q add the same JSON without its id.", severity="high")
def a_readd_rejected(rec):
    candidates(rec)
    adjudicate(rec, [answers(rec, "closed", wrong="sample-q004"), answers(rec, "open"), answers(rec, "ambiguity")])
    only = {"sample-q004"}
    adjudicate(rec, [answers(rec, "closed", rnd=1, wrong="sample-q004", only=only), answers(rec, "open", rnd=1, only=only), answers(rec, "ambiguity", rnd=1, only=only)])
    rec.note("state of sample-q004", str(q_state(rec, "sample-q004")))
    rc, res = add_q(rec, new_q(rec))
    rc2, _ = rec.run("q", "lint", "--all")
    return added(rc, res), "q add does not look at rejected items or at _build/qbank/rejected.jsonl, and q dedupe skips rejected questions, so the copy is a fresh round-0 candidate."


@attempt("q set-status", "Mark a never-verified candidate as verified",
         "All questions candidate; q set-status --status verified sample-q004.",
         repro="q set-status --chapter 99 --status verified <candidate id>", severity="low")
def a_set_verified(rec):
    candidates(rec)
    rc, res = rec.run("q", "set-status", "--chapter", "99", "--status", "verified", "sample-q004", "--by", "breaker")
    state = q_state(rec, "sample-q004")
    rec.note("state of sample-q004", str(state))
    rc2, _ = rec.run("q", "lint", "99")
    return ("partial" if state[0] == "verified" else False), "Status 'verified' is set without any solver (only 'ready' is checked). Downstream --select, mocks and Q206 read verification.status, so the damage is a wrong count in q lint and q list."


# ---------------------------------------------------------------- mocks

SPLIT = [1, 3, 1, 1]
POOL = [("1.1", 1, "single"), ("1.1", 1, "single"), ("2.1", 2, "single"), ("2.1", 2, "multi"), ("2.2", 2, "single"),
        ("2.2", 2, "multi"), ("3.1", 3, "single"), ("3.1", 3, "single"), ("4.1", 4, "single"), ("4.1", 4, "single")]


def unique_words(n, count=18):
    letters = "bcdfghjklm"
    return " ".join("zq" + "".join(letters[int(d)] for d in f"{n * 100 + i:05d}") for i in range(count))


def mock_setup(rec, pad=18):
    base = {q["id"]: q for q in common.read_json(rec.p(*QF))["items"]}

    def spec(s):
        s["templates"]["mock"] = {"files": [], "counts": {"questions": {"shipped": 6, "core": 6, "extended": 0, "write": 10, "twin_pairs_min": 0,
                                                                          "multi": {"min": 1, "max": 2}, "worked": 0, "worked_wrong_path": 0}},
                                  "mock": {"domain_split": SPLIT, "minutes": 12, "max_questions_per_service": 10}}
        s["questions"]["no_qualifier_share_max"] = 1.0
    sandbox.edit_json(rec.p("_build", "style", "SPEC.json"), spec)

    def book(b):
        for cid, slug in (("50", "mock-exam-1"), ("51", "mock-exam-2")):
            b["chapters"].append({"id": cid, "slug": slug, "title": slug, "part": "storage", "tier": "mock", "wave": "W0", "services": [], "tasks": [], "bullets": [],
                                  "sources": {"guides": [], "pages": [], "faq": [], "history": [], "quotas": [], "pricing": [], "whatsnew_tags": [], "case_tags": []}})
    sandbox.edit_json(rec.p("data", "book.json"), book)
    for m, (cid, slug) in enumerate((("50", "mock-exam-1"), ("51", "mock-exam-2"))):
        items = []
        for n, (task, domain, typ) in enumerate(POOL, 1):
            q = copy.deepcopy(base["sample-q003" if typ == "multi" else "sample-q004"])
            q.pop("worked", None)
            q.update(id=f"{slug}-q{n:03d}", chapter=slug, pool="mock", layer="core", task=task, domain=domain, bullets=[],
                     section="99-sample/1-fast.md#choose-it-or-not", status="verified", twin_of=None, concept=f"concept-{m}-{n}",
                     stem=f"A company runs the {unique_words(m * 50 + n, pad)} program. " + q["stem"])
            items.append(q)
        common.write_json(rec.p("data", f"{cid}-{slug}", "questions.json"), {"v": 1, "chapter": slug, "items": items})


def mq(rec, cid="50"):
    return rec.p("data", f"{cid}-mock-exam-{int(cid) - 49}", "questions.json")


def mm(rec, cid="50"):
    return rec.p("data", f"{cid}-mock-exam-{int(cid) - 49}", "mock.json")


def mock_ok(res, cid="50"):
    return any(m["mock"] == cid and m["ok"] for m in (res or {}).get("mocks", []))


@attempt("mocks check", "Control: a mock question with the exact stem of a chapter question",
         "Assemble mock 50, then give one chosen single-answer question the exact stem of sample-q004.")
def a_mock_copy(rec):
    mock_setup(rec)
    rec.run("mocks", "assemble", "--mock", "50")
    by_id = {q["id"]: q for q in common.read_json(mq(rec))["items"]}
    chosen = next(i for i in common.read_json(mm(rec))["questions"] if by_id[i]["type"] == "single")
    stem = stored(rec, QF, "sample-q004")["stem"]

    def change(doc):
        next(q for q in doc["items"] if q["id"] == chosen)["stem"] = stem
    sandbox.edit_json(mq(rec), change)
    rc, res = rec.run("mocks", "check", "--mock", "50")
    return mock_ok(res), "K04 holds for a verbatim stem."


@attempt("mocks assemble / mocks check", "A mock built from chapter questions under new ids (one padding sentence in front of the stem)",
         "Every mock question is sample-q004 or sample-q003 with a new id and one extra first sentence of 18 new words; options, key, why and "
         "explanation are the chapter question's. This is also what the tool's own mock tests use as their pool. Second step: only 12 padding words.",
         repro="copy a chapter question into data/50-.../questions.json with a new id, pool mock, and one unrelated first sentence of about 12 content words; mocks assemble; mocks check.",
         severity="high")
def a_mock_padded(rec):
    mock_setup(rec)
    rc, res = rec.run("mocks", "assemble", "--mock", "50")
    rc, res = rec.run("mocks", "check", "--mock", "50")
    first = mock_ok(res)
    a = qbank._shingles(stored(rec, QF, "sample-q004")["stem"])
    b = qbank._shingles(next(q for q in common.read_json(mq(rec))["items"] if q["type"] == "single")["stem"])
    sim18 = qbank._jac(a, b)
    rec.fresh()
    mock_setup(rec, pad=12)
    rec.run("mocks", "assemble", "--mock", "50")
    rc, res = rec.run("mocks", "check", "--mock", "50", label="mocks check --mock 50 (12 padding words)")
    b = qbank._shingles(next(q for q in common.read_json(mq(rec))["items"] if q["type"] == "single")["stem"])
    sim12 = qbank._jac(a, b)
    return first and mock_ok(res), f"Stem similarity to the chapter question is {sim18:.2f} with 18 padding words and {sim12:.2f} with 12 (threshold 0.6). K04 compares stems only, never options or explanations."


@attempt("mocks check", "Two questions of one mock with the same stem",
         "After assemble, one chosen single-answer question gets the stem of another chosen single-answer question of the same mock.",
         repro="give two questions of one mock the same stem; mocks check.", severity="medium")
def a_mock_inner(rec):
    mock_setup(rec)
    rec.run("mocks", "assemble", "--mock", "50")
    by_id = {q["id"]: q for q in common.read_json(mq(rec))["items"]}
    singles = [i for i in common.read_json(mm(rec))["questions"] if by_id[i]["type"] == "single"]

    def change(doc):
        d = {q["id"]: q for q in doc["items"]}
        d[singles[1]]["stem"] = d[singles[0]]["stem"]
    sandbox.edit_json(mq(rec), change)
    rc, res = rec.run("mocks", "check", "--mock", "50")
    rc2, _ = rec.run("q", "lint", "--all")
    return mock_ok(res), f"K04 looks only at the other mock and at pool 'chapter'. q lint --all would report Q302 (exit {rc2}), but mocks check and the ledger gates do not run it."


@attempt("mocks check", "A mock question that copies a drill-pool question",
         "sample-q004 is moved to pool drill in chapter 99; one mock question gets its exact stem.",
         repro="copy the stem of a pool-drill question into a mock question; mocks check.", severity="medium")
def a_mock_drill(rec):
    mock_setup(rec)
    rec.run("mocks", "assemble", "--mock", "50")
    stem = stored(rec, QF, "sample-q004")["stem"]

    def to_drill(doc):
        next(q for q in doc["items"] if q["id"] == "sample-q004")["pool"] = "drill"
    sandbox.edit_json(rec.p(*QF), to_drill)
    by_id = {q["id"]: q for q in common.read_json(mq(rec))["items"]}
    chosen = next(i for i in common.read_json(mm(rec))["questions"] if by_id[i]["type"] == "single")

    def change(doc):
        next(q for q in doc["items"] if q["id"] == chosen)["stem"] = stem
    sandbox.edit_json(mq(rec), change)
    rc, res = rec.run("mocks", "check", "--mock", "50")
    return mock_ok(res), "K04 tests pool == 'chapter' only, so a drill question can be reused in a mock."


@attempt("mocks check", "Manifest edited by hand: minutes and counts changed",
         "After assemble, mock.json gets minutes 9999 and an invented counts object.",
         repro="edit data/50-.../mock.json: minutes 9999, counts {}; mocks check.", severity="low")
def a_mock_manifest(rec):
    mock_setup(rec)
    rec.run("mocks", "assemble", "--mock", "50")

    def change(m):
        m["minutes"] = 9999
        m["counts"] = {"domains": {"1": 99}, "tasks": {}, "multi": 0, "difficulty": {}, "services": {}}
        m["seed"] = 1
    sandbox.edit_json(mm(rec), change)
    rc, res = rec.run("mocks", "check", "--mock", "50")
    return mock_ok(res), "mocks check recomputes the split from the questions and ignores the stored minutes, seed and counts; the web app reads minutes from this file."


# ---------------------------------------------------------------- cards

def new_card(rec, base, **kw):
    c = stored(rec, CF, base)
    del c["id"]
    c.update(kw)
    return c


def add_card(rec, card):
    return rec.run("cards", "add", "--chapter", "99", "--file", rec.write("card.json", card), "--by", "breaker")


@attempt("cards add", "Control: list answer with semicolons", "Back 'A shelf; a crate; a quota.'")
def a_card_semicolon(rec):
    rc, res = add_card(rec, new_card(rec, "sample-c003", front="In Amazon Widget Store, which three resources exist?", back="A shelf; a crate; a quota."))
    return added(rc, res), "C105 holds."


@attempt("cards add", "List answer written with one comma and 'and', or with slashes",
         "Step 1: back 'A shelf, a crate and a quota.' Step 2: back 'shelf / crate / quota / Region'.",
         repro="cards add a decide card with back 'A shelf, a crate and a quota.'", severity="high")
def a_card_list(rec):
    r1 = add_card(rec, new_card(rec, "sample-c003", front="In Amazon Widget Store, which three resources exist?", back="A shelf, a crate and a quota."))
    r2 = add_card(rec, new_card(rec, "sample-c003", front="In Amazon Widget Store, name the four things an architect plans for.", back="shelf / crate / quota / Region"))
    return added(*r1) and added(*r2), "C105 looks for a line break, a semicolon or two commas. A three-item list in plain English has one comma."


@attempt("cards add", "Control: back of 14 words", "Back with 14 separate words.")
def a_card_long(rec):
    rc, res = add_card(rec, new_card(rec, "sample-c002", front="In Amazon Widget Store, how does a team get a shelf into another Region?",
                                     back="The team copies the shelf to the other Region and keeps the first shelf."))
    return added(rc, res), "C102 holds."


@attempt("cards add", "Back far over the word limit, joined with hyphens",
         "Back 'No. Copy-the-shelf-to-the-other-Region-then-check-the-copy-then-delete-the-first-shelf-and-tell-the-team.' (20 words, counted as 2).",
         repro="cards add with a back whose words are joined by hyphens (or slashes).", severity="medium")
def a_card_hyphen(rec):
    rc, res = add_card(rec, new_card(rec, "sample-c002", front="In Amazon Widget Store, how does a team get a shelf into another Region?",
                                     back="No. Copy-the-shelf-to-the-other-Region-then-check-the-copy-then-delete-the-first-shelf-and-tell-the-team."))
    return added(rc, res), "lint.word_count splits on whitespace only. The same trick works for every word limit (speak scripts, step texts, options)."


@attempt("cards add", "Wrong number written as a word",
         "Back 'A crate. It holds ninety widgets.' with facts [widget-crate-capacity] (the fact says 50 widgets).",
         repro="cards add with back 'A crate. It holds ninety widgets.'", severity="high")
def a_card_number_word(rec):
    rc, res = add_card(rec, new_card(rec, "sample-c003", front="In Amazon Widget Store, which resource carries a few widgets to a partner Region?", back="A crate. It holds ninety widgets."))
    return added(rc, res), "C109 sees digits only (lint.number_with_unit does not match number words), so a number in words needs no fact and can be wrong."


@attempt("cards add", "Card whose answer contradicts its own fact",
         "cannot card: front 'In Amazon Widget Store, is a new shelf readable by every user in the account?', back 'Yes. Every user reads it.', facts [widget-shelf-default-private].",
         repro="cards add a cannot card with a back that states the opposite of the fact in facts.", severity="high")
def a_card_false(rec):
    rc, res = add_card(rec, new_card(rec, "sample-c002", front="In Amazon Widget Store, is a new shelf readable by every user in the account?",
                                     back="Yes. Every user reads it.", extra=None, facts=["widget-shelf-default-private"], trap=None))
    return added(rc, res), "front and back are not strict text: no fact link, no absolute-word rule, and cards have no blind check. 'extra' can be null, so the card carries no grounded sentence at all."


@attempt("cards add", "Near-duplicate front with three filler words",
         "Front of sample-c002 plus ' Think first, please.'",
         repro="cards add a card whose front is an existing front plus three new words.", severity="low")
def a_card_neardup(rec):
    c = new_card(rec, "sample-c002")
    c["front"] += " Think first, please."
    rc, res = add_card(rec, c)
    return added(rc, res), "C106 needs a token Jaccard of 0.8; short fronts drop below it with two or three added words."


# ---------------------------------------------------------------- speak

def new_speak(rec, change=None):
    s = stored(rec, SF, "sample-s01")
    del s["id"]
    if change:
        change(s)
    return s


def add_speak(rec, item):
    return rec.run("speak", "add", "--chapter", "99", "--file", rec.write("speak.json", item), "--by", "breaker")


FILL = "the team keeps the widgets on the shelf and the shelf stays where the team made it"


@attempt("speak add", "Control: a 60-second answer of 300 words", "Twelve lines of 25 plain words each.")
def a_speak_300(rec):
    def ch(s):
        line = "The short answer is that " + " ".join(FILL.split()[:20]) + "."
        s["sixty_second"] = [line] * 11 + ["Do you agree?"]
    rc, res = add_speak(rec, new_speak(rec, ch))
    return added(rc, res), "P102 holds for plain words."


@attempt("speak add", "A 60-second answer of about 300 words, with words joined by hyphens",
         "The eight fixture lines, each with one more 'sentence' of 28 words joined by hyphens. The tool counts 8 more words; a speaker says 224 more.",
         repro="speak add with lines such as 'The short answer is: a shelf keeps your widgets in one Region. The-team-keeps-the-widgets-on-the-shelf-...'", severity="medium")
def a_speak_hyphen(rec):
    def ch(s):
        glue = "-".join((FILL + " " + FILL).split()[:28]).capitalize() + "."
        s["sixty_second"] = [line[:-1] + ". " + glue if not line.endswith("?") else glue + " " + line for line in s["sixty_second"]]
    item = new_speak(rec, ch)
    spoken = sum(len(line.replace("-", " ").split()) for line in item["sixty_second"])
    rec.note("words a speaker says", str(spoken))
    rc, res = add_speak(rec, item)
    return added(rc, res), "Same cause as the card attempt: word_count splits on whitespace."


@attempt("speak add", "300 words outside the script: follow-up answer and key point",
         "follow_ups[0].answer and key_points[0].point each get 300 words.",
         repro="speak add with a follow_ups[].answer of 300 words.", severity="medium")
def a_speak_followup(rec):
    def ch(s):
        long = " ".join([FILL] * 19) + "."
        s["follow_ups"][0]["answer"] = "No. " + long.capitalize()
        s["key_points"][0]["point"] = long.capitalize()
    rc, res = add_speak(rec, new_speak(rec, ch))
    return added(rc, res), "Only ten_second, sixty_second and the cues have word limits. 4-say.md prints the follow-up answers, and the app grades against key points."


@attempt("speak add", "Ungrounded absolute claims in the script",
         "Line 3 replaced by 'A shelf is always global and never private.' (contradicts widget-shelf-scope and widget-shelf-default-private).",
         repro="speak add with a sixty_second line 'A shelf is always global and never private.'", severity="high")
def a_speak_absolute(rec):
    def ch(s):
        s["sixty_second"][2] = "A shelf is always global and never private."
    rc, res = add_speak(rec, new_speak(rec, ch))
    return added(rc, res), "Scripts are checked for digits, number words with a unit, avoid words and banned words. There is no absolute-word rule and no tie between a script sentence and a fact (RULINGS hard rule 1)."


@attempt("speak add", "Spoken numbers that P109 does not see",
         "Step 1 control: 'One shelf holds up to six hundred widgets.' Step 2: 'One shelf holds up to nine hundred of your widgets.' Step 3: 'One shelf holds up to nineteen widgets.'",
         repro="speak add with the line 'One shelf holds up to nineteen widgets.' or '... nine hundred of your widgets.'", severity="high")
def a_speak_numbers(rec):
    out = []
    for text in ("One shelf holds up to six hundred widgets.", "One shelf holds up to nine hundred of your widgets.", "One shelf holds up to nineteen widgets."):
        def ch(s, text=text):
            s["sixty_second"][3] = text
            s["skeleton"][2] = "many per shelf"
        out.append(added(*add_speak(rec, new_speak(rec, ch))))
        if out[-1]:
            rec.fresh()
    return (not out[0]) and out[1] and out[2] or (out[1] or out[2]), ("number_word_regex has no one, seventeen, eighteen, nineteen, dozen, half or double; and the unit must follow the number word "
                                                                     "directly, so two words between number and noun switch P109 off.")


# ---------------------------------------------------------------- tasks

def new_task(rec, s1=None, cleanup=None, verify=None, **kw):
    """sample-t02 as sample-t03. With s1: steps = [s1, the fixture break-it step, a list step] (no create command)."""
    t = json.loads(json.dumps(stored(rec, TF, "sample-t02")).replace("sample-t02", "sample-t03"))
    for key in ("status", "rev", "label", "checked"):
        t.pop(key, None)
    if s1 is not None:
        first = {"text": "Run the command for <SG_ID>, <AMI_ID> and <INSTANCE_ID>.", "command": s1, "expect": "The command returns without an error.", "break_it": False, "predict": None}
        last = {"text": "List the shelves.", "command": "aws widget list-shelves", "expect": "A list of shelves.", "break_it": False, "predict": None}
        t["steps"] = [first, t["steps"][1], last]
        t["cleanup"] = [{"text": "List the shelves again.", "command": "aws widget list-shelves"}]
    if cleanup is not None:
        t["cleanup"] = cleanup
    if verify is not None:
        t["verify"] = verify
    t.update(kw)
    return t


def add_task(rec, task, label=None):
    return rec.run("tasks", "add", "--chapter", "99", "--file", rec.write("task.json", task), "--by", "breaker", label=label)


def batch(rec, variants):
    """One tasks add per command; returns {name: got through}."""
    out = {}
    for name, command in variants:
        rec.fresh()
        rc, res = add_task(rec, new_task(rec, s1=command), label=f"tasks add [{name}] {command[:150]}")
        out[name] = added(rc, res)
    return out


def verdict(results, controls=()):
    through = sorted(k for k, v in results.items() if v and k not in controls)
    held = sorted(k for k, v in results.items() if not v)
    return through, held


@attempt("tasks add", "Control: a Try without cleanup", "sample-t02 copy with cleanup [].")
def a_task_nocleanup(rec):
    rc, res = add_task(rec, new_task(rec, cleanup=[]))
    return added(rc, res), "T103 holds."


@attempt("tasks add", "A task that creates resources and deletes nothing (create verbs outside the list)",
         "Steps 'aws widget put-shelf --name saa-breaker-shelf' and 'aws widget import-shelf ...'; cleanup is 'aws widget list-shelves'. No tag anywhere.",
         repro="tasks add a Try whose creating steps use put-*, import-*, start-*, register-*, restore-*, request-* or 'aws s3 mb', with a cleanup list of one read-only command.",
         severity="high")
def a_task_no_delete(rec):
    t = new_task(rec, s1="aws widget put-shelf --name saa-breaker-shelf")
    t["steps"][2]["command"] = "aws widget import-shelf --name saa-breaker-copy --source s3://saa-breaker/shelf.json"
    rc, res = add_task(rec, t)
    return added(rc, res), "T103 wants a non-empty cleanup list, T106 and T107 act only on create|copy|run|allocate|launch. Any other creating verb needs no tag and no undo, and the cleanup can be a list command."


@attempt("tasks add", "Cleanup deletes a different resource, or only pretends (--dry-run)",
         "sample-t02 copy (create-shelf, copy-shelf); cleanup 'aws widget delete-shelf --name saa-some-other-shelf --dry-run' twice.",
         repro="tasks add where each create has a delete-<noun> cleanup command that names another resource or carries --dry-run.", severity="high")
def a_task_wrong_delete(rec):
    cleanup = [{"text": "Delete the copy in the other Region.", "command": "aws widget delete-shelf --name saa-some-other-shelf --dry-run"},
               {"text": "Delete the first shelf.", "command": "aws widget delete-shelf --name saa-some-other-shelf --dry-run"}]
    rc, res = add_task(rec, new_task(rec, cleanup=cleanup))
    return added(rc, res), "T107 pairs verbs and nouns only. It does not compare the resource name or id, and it does not know --dry-run or --generate-cli-skeleton."


@attempt("tasks add", "run-instances undone by stop-instances",
         "Step 'aws ec2 run-instances ... --tag-specifications ...'; cleanup 'aws ec2 stop-instances --instance-ids <INSTANCE_ID>'.",
         repro="tasks add with run-instances and a cleanup of stop-instances.", severity="medium")
def a_task_stop(rec):
    t = new_task(rec, s1="aws ec2 run-instances --image-id <AMI_ID> --instance-type t3.micro --tag-specifications ResourceType=instance,Tags=[{Key=book,Value=saa},{Key=task,Value=sample-t03}]",
                 cleanup=[{"text": "Stop the instance <INSTANCE_ID>.", "command": "aws ec2 stop-instances --instance-ids <INSTANCE_ID>"}],
                 verify={"command": "aws ec2 describe-instances --filters Name=tag:book,Values=saa", "expect": "An empty list."})
    rc, res = add_task(rec, t)
    return added(rc, res), "lab.UNDO accepts stop and delete for run, although cleanup_pairs maps run-instances to terminate-instances. A stopped instance keeps its EBS volume and its bill."


SG = "aws ec2 authorize-security-group-ingress --group-id <SG_ID> "


@attempt("tasks add (T105)", "Security group opened to the world: ::/0 written in full, prefix list, split ranges, rules in a file, other operations",
         "One tasks add per command. Controls first (must be rejected), then the variants.",
         repro="tasks add with a step 'aws ec2 modify-security-group-rules --group-id <SG_ID> --security-group-rules SecurityGroupRuleId=sgr-0123,SecurityGroupRule={IpProtocol=tcp,FromPort=22,ToPort=22,CidrIpv4=0.0.0.0/0}' (or any 'got through' line of this entry).",
         severity="high")
def a_task_sg(rec):
    controls = ("c1 port 22 ::/0", "c2 range 20-25 ::/0", "c3 all protocols ::/0", "c4 --port=22 --cidr=0.0.0.0/0")
    variants = [
        ("c1 port 22 ::/0", SG + "--ip-permissions IpProtocol=tcp,FromPort=22,ToPort=22,Ipv6Ranges=[{CidrIpv6=::/0}]"),
        ("c2 range 20-25 ::/0", SG + "--ip-permissions IpProtocol=tcp,FromPort=20,ToPort=25,Ipv6Ranges=[{CidrIpv6=::/0}]"),
        ("c3 all protocols ::/0", SG + "--ip-permissions IpProtocol=-1,Ipv6Ranges=[{CidrIpv6=::/0}]"),
        ("c4 --port=22 --cidr=0.0.0.0/0", SG + "--protocol=tcp --port=22 --cidr=0.0.0.0/0"),
        ("v1 ::/0 written in full", SG + "--ip-permissions IpProtocol=tcp,FromPort=20,ToPort=25,Ipv6Ranges=[{CidrIpv6=0:0:0:0:0:0:0:0/0}]"),
        ("v2 prefix list", SG + "--ip-permissions IpProtocol=tcp,FromPort=20,ToPort=25,PrefixListIds=[{PrefixListId=pl-0123456789abcdef0}]"),
        ("v3 two halves of the internet", SG + "--ip-permissions IpProtocol=tcp,FromPort=20,ToPort=25,IpRanges=[{CidrIp=0.0.0.0/1},{CidrIp=128.0.0.0/1}]"),
        ("v4 modify-security-group-rules", "aws ec2 modify-security-group-rules --group-id <SG_ID> --security-group-rules SecurityGroupRuleId=sgr-0123,SecurityGroupRule={IpProtocol=tcp,FromPort=22,ToPort=22,CidrIpv4=0.0.0.0/0}"),
        ("v5 rules in a file", SG + "--ip-permissions file://rules.json"),
        ("v6 --cli-input-json", SG + "--cli-input-json file://open-ssh.json"),
        ("v7 port 443 to the world with --cidr=", SG + "--protocol tcp --port 443 --cidr=0.0.0.0/0"),
        ("v8 all TCP ports, IPv4 range form", SG + "--ip-permissions IpProtocol=tcp,FromPort=0,ToPort=65535,IpRanges=[{CidrIp=0.0.0.0/0}]"),
        ("v9 network ACL entry", "aws ec2 replace-network-acl-entry --network-acl-id <SG_ID> --ingress --rule-number 100 --protocol 6 --port-range From=22,To=22 --cidr-block 0.0.0.0/0 --rule-action allow"),
    ]
    results = batch(rec, variants)
    through, held = verdict(results, controls)
    bad_controls = [c for c in controls if results.get(c)]
    note = f"Got through: {through}. Held: {held}." + (f" CONTROLS THAT PASSED: {bad_controls}." if bad_controls else "")
    note += " The world check is tied to the operation name authorize-security-group-ingress and to the literal strings 0.0.0.0/0 and ::/0."
    return bool(through or bad_controls), note


@attempt("tasks add (T105)", "Public exposure by other commands",
         "One tasks add per command.",
         repro="tasks add with a step 'aws s3api put-bucket-policy --bucket saa-b --policy <a policy with \"Principal\":\"*\">' (or any 'got through' line of this entry).",
         severity="high")
def a_task_public(rec):
    controls = ("c1 public-read ACL", "c2 BlockPublicAcls=false")
    variants = [
        ("c1 public-read ACL", "aws s3api put-bucket-acl --bucket saa-b --acl public-read"),
        ("c2 BlockPublicAcls=false", "aws s3api put-public-access-block --bucket saa-b --public-access-block-configuration BlockPublicAcls=false,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"),
        ("v1 bucket policy Principal *", "aws s3api put-bucket-policy --bucket saa-b --policy '{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":\"*\",\"Action\":\"s3:GetObject\",\"Resource\":\"arn:aws:s3:::saa-b/*\"}]}'"),
        ("v2 RDS publicly accessible", "aws rds modify-db-instance --db-instance-identifier saa-db --publicly-accessible --apply-immediately"),
        ("v3 public EBS snapshot", "aws ec2 modify-snapshot-attribute --snapshot-id snap-0123 --attribute createVolumePermission --operation-type add --group-names all"),
        ("v4 Lambda permission for everyone", "aws lambda add-permission --function-name saa-fn --statement-id open --action lambda:InvokeFunction --principal '*'"),
        ("v5 function URL without auth", "aws lambda put-function-url-config --function-name saa-fn --auth-type NONE"),
        ("v6 account-level public access block off", "aws s3control delete-public-access-block --account-id 111122223333"),
        ("v7 public AMI", "aws ec2 modify-image-attribute --image-id ami-0123 --launch-permission Add=[{Group=all}]"),
    ]
    results = batch(rec, variants)
    through, held = verdict(results, controls)
    return bool(through), f"Got through: {through}. Held: {held}. T105 is a list of literal patterns for S3 ACLs and the public access block; a bucket policy and the public switches of other services are not in it."


@attempt("tasks add (T104, T105)", "Credentials and non-read-only helper commands",
         "One tasks add per command.",
         repro="tasks add with a step 'aws configure export-credentials --format env'.", severity="high")
def a_task_creds(rec):
    controls = ("c1 create-access-key", "c2 curl -X POST")
    variants = [
        ("c1 create-access-key", "aws iam create-access-key --user-name saa-user"),
        ("c2 curl -X POST", "curl -X POST https://api.example.com/create"),
        ("v1 export-credentials", "aws configure export-credentials --format env"),
        ("v2 role credentials from instance metadata", "curl http://169.254.169.254/latest/meta-data/iam/security-credentials/saa-role"),
        ("v3 curl --json (a POST)", "curl --json '{\"k\":\"v\"}' https://api.example.com/create"),
        ("v4 get-session-token", "aws sts get-session-token --duration-seconds 129600"),
    ]
    results = batch(rec, variants)
    through, held = verdict(results, controls)
    return bool(through), f"Got through: {through}. Held: {held}. 'aws configure' is banned only for set, sso, import and the bare form; curl is checked against a list of flags, not for a GET of a public URL."


@attempt("tasks add (T104, T115)", "More than one command, redirects and uncaptured variables",
         "One tasks add per command.",
         repro="tasks add with a step command 'aws s3 ls\\naws iam list-users' (a line break inside the JSON string).", severity="high")
def a_task_shell(rec):
    controls = ("c1 pipe", "c2 uncaptured $VPC_ID")
    variants = [
        ("c1 pipe", "aws s3 ls | head"),
        ("c2 uncaptured $VPC_ID", "aws ec2 describe-vpcs --vpc-ids $VPC_ID"),
        ("v1 two commands on two lines", "aws s3 ls\naws iam list-users"),
        ("v2 process substitution", "aws s3 cp <(curl -s https://example.com/payload) s3://saa-b/payload"),
        ("v3 redirect into a file", "aws sts get-caller-identity > /home/cloudshell-user/.aws/config"),
        ("v4 uncaptured ${VPC_ID}", "aws ec2 describe-vpcs --vpc-ids ${VPC_ID}"),
        ("v5 uncaptured lowercase $vpc_id", "aws ec2 describe-vpcs --vpc-ids $vpc_id"),
        ("v6 input redirect", "aws s3api put-object --bucket saa-b --key k --body /dev/stdin < /etc/passwd"),
    ]
    results = batch(rec, variants)
    through, held = verdict(results, controls)
    return bool(through), f"Got through: {through}. Held: {held}. T104 flags a token only when it holds ; | or &; a line break, < > and <( ) pass. T115 knows $NAME in capitals only."


@attempt("tasks add (T106, T108)", "Tag text anywhere in the command instead of a tag",
         "create-shelf and copy-shelf carry --description \"book=saa task=sample-t03\" and no --tags; verify is 'aws widget list-shelves --name book=saa'.",
         repro="tasks add with 'aws widget create-shelf --name saa-x --description \"book=saa task=<id>\"' and no tag option.", severity="medium")
def a_task_tag_anywhere(rec):
    t = new_task(rec, verify={"command": "aws widget list-shelves --name book=saa", "expect": "An empty list."})
    t["steps"][0]["command"] = "aws widget create-shelf --name saa-sample-shelf --description \"book=saa task=sample-t03\""
    t["steps"][2]["command"] = "aws widget copy-shelf --name saa-sample-shelf --target-region eu-west-1 --description \"book=saa task=sample-t03\""
    rc, res = add_task(rec, t)
    return added(rc, res), "tag_patterns, tag_task_patterns and verify_tag_patterns are searched in the whole command string, not in the value of a tag option or filter."


@attempt("tasks add (T109)", "Cost hidden behind '$0'",
         "cost '$0 (the NAT gateway bills about 4.50 USD for each hour)'; cost_if_forgotten '$0, plus about 108 USD for each day'. No cost fact.",
         repro="tasks add with cost '$0 (about 4.50 USD for each hour)' and cost_facts [].", severity="high")
def a_task_cost(rec):
    rc, res = add_task(rec, new_task(rec, cost="$0 (the NAT gateway bills about 4.50 USD for each hour)", cost_if_forgotten="$0, plus about 108 USD for each day"))
    return added(rc, res), "T103 and T109 read only amounts written with a $ sign. A price as '4.50 USD', 'USD 4.50', '5 dollars' or 'a few cents' needs no fact and is not held against cost_usd_max or T119."


@attempt("tasks add (T103)", "A Look task that deletes",
         "sample-t01 copy as sample-t03; step 2 command 'aws widget delete-shelf --name saa-prod-shelf'.",
         repro="tasks add a look whose step command is a delete-*, terminate-*, put-* or modify-* operation.", severity="high")
def a_task_look(rec):
    t = stored(rec, TF, "sample-t01")
    for key in ("status", "rev", "label", "checked"):
        t.pop(key, None)
    t["id"] = "sample-t03"
    t["steps"][1]["command"] = "aws widget delete-shelf --name saa-prod-shelf"
    rc, res = add_task(rec, t)
    return added(rc, res), "A Look is 'read-only' only in the sense that its operation does not match create_command_regex."


@attempt("tasks add (T106, T116)", "Untaggable create with no tag and no saa- name",
         "Steps 'aws s3api create-bucket --bucket company-data-2026'; cleanup 'aws s3api delete-bucket --bucket company-data-2026'. No tagging step.",
         repro="tasks add with create-bucket on a name without the saa- prefix and no put-bucket-tagging step.", severity="medium")
def a_task_untaggable(rec):
    t = new_task(rec, s1="aws s3api create-bucket --bucket company-data-2026",
                 cleanup=[{"text": "Delete the bucket.", "command": "aws s3api delete-bucket --bucket company-data-2026"}])
    rc, res = add_task(rec, t)
    rc2, lint = rec.run("tasks", "lint", "99")
    warn = [w["code"] for w in (lint or {}).get("warnings", [])]
    rec.note("warnings of tasks lint 99", str(warn))
    return added(rc, res), "untaggable_rule says the next step tags the resource or the name starts with saa-. Neither is enforced: T116 is a warning, and nothing looks for the tagging step. The verify-by-tag step then finds nothing and reports a clean account."


def _cli_task(commands):
    steps = [{"text": f"Run read command {i + 1}.", "command": c, "expect": "A JSON document.", "break_it": False, "predict": None} for i, c in enumerate(commands)]
    return {"v": 1, "chapter": "sample", "items": [{
        "id": "sample-t01", "chapter": "sample", "type": "look", "title": "Read the instances", "kills": "\"A shelf is global, so every Region sees it.\"",
        "trap": "sample-trap-shelf-global", "section": "1-fast.md#look-first", "pass_route": False, "minutes": 3, "cost": "$0", "cost_if_forgotten": "$0",
        "cost_facts": [], "permissions": ["ec2:DescribeInstances"], "read_only_alternative": "This task is read-only. It needs no alternative.",
        "steps": steps, "cleanup": [], "verify": None, "still_costs": [], "label": "checked against docs, not run in a real account", "checked": "2026-10-04",
        "facts": ["widget-shelf-scope"], "sources": [], "status": "ready", "rev": 1}]}


NO_UV = "--no-uv" in sys.argv


@attempt("tasks check-cli", "Misspelled options that the CLI model does not see",
         "tasks.json replaced by one Look. Run A (control): 'aws ec2 describe-instances --instance-id i-0123456789abcdef0' (the option is --instance-ids). "
         "Run B: a single-dash option, a bare word in place of an option, misspelled shorthand keys, a misspelled --output value, an unknown --query path.",
         repro="tasks check-cli on 'aws ec2 describe-instances -filters Name=tag:book,Values=saa' or 'aws ec2 describe-instances --filters Nmae=tag:book,Vaules=saa'.",
         severity="high")
def a_cli(rec):
    if NO_UV:
        rec.note("tasks check-cli", "skipped (--no-uv)")
        return None, "Not run."
    common.write_json(rec.p(*TF), _cli_task(["aws ec2 describe-instances --instance-id i-0123456789abcdef0"]))
    rc_a, res_a = rec.run("tasks", "check-cli", "99", label="tasks check-cli 99 (run A, control)")
    if rc_a == common.EXIT_TRANSIENT or res_a is None:
        return None, "uv or the package index could not be reached; the attempt could not run."
    sneaky = ["aws ec2 describe-instances -filters Name=tag:book,Values=saa",
              "aws ec2 describe-instances filters Name=tag:book,Values=saa",
              "aws ec2 describe-instances --filters Nmae=tag:book,Vaules=saa",
              "aws ec2 describe-instances --output jsno",
              "aws ec2 describe-instances --query Resrevations[].Instnaces[].InstanceId"]
    common.write_json(rec.p(*TF), _cli_task(sneaky))
    rc_b, res_b = rec.run("tasks", "check-cli", "99", label="tasks check-cli 99 (run B, five misspelled commands)")
    rows = {r["command"]: r["ok"] for r in (res_b or {}).get("commands", [])}
    passed = [c for c in sneaky if rows.get(c)]
    rec.note("commands reported ok in run B", str(passed))
    return bool(passed), (f"Control exit {rc_a}. {len(passed)} of {len(sneaky)} misspelled commands are reported ok. cli_model.py skips every token that does not start with '--', "
                          "and it checks option names only: never shorthand keys, enum values or JMESPath.")


@attempt("tasks lint --ship (T113)", "A CLI report written by hand",
         "No check-cli run. _build/reports/cli/99.json written by hand with ok true and the SHA-256 of the fixture's invented 'aws widget' commands. Then tasks lint 99 --ship.",
         repro="write _build/reports/cli/<id>.json = {chapter, ok: true, commands_sha256: sha256 of the commands joined with newlines}; tasks lint <id> --ship.", severity="medium")
def a_cli_forged(rec):
    rc0, before = rec.run("tasks", "lint", "99", "--ship", label="tasks lint 99 --ship (before)")
    doc = common.read_json(rec.p(*TF))
    common.write_json(rec.p("_build", "reports", "cli", "99.json"), {"chapter": "99", "awscli": "1.46.1", "checked": "2026-10-04", "commands_sha256": lab.commands_sha256(doc), "ok": True, "commands": [], "warnings": []})
    rc, res = rec.run("tasks", "lint", "99", "--ship", label="tasks lint 99 --ship (after the hand-written report)")
    codes = [f["code"] for f in (res or {}).get("errors", [])]
    return "T113" not in codes, "T113 trusts any file with the right hash and ok true. The report has no list check (commands is empty here) and no trace of a tool run. The fixture's invented 'aws widget' commands then ship."


# ---------------------------------------------------------------- diagrams

ARCH = {
    "id": "breaker-arch", "kind": "arch", "size": "s", "sample": True, "title": "A three-tier web application",
    "claim": "A request passes through three tiers, and the load balancer is the only tier in a public subnet.",
    "alt": "Users send requests to a load balancer, which forwards them to an app server, which uses a database.",
    "cols": 2, "rows": 4, "flow": "down",
    "groups": [{"id": "vpc", "type": "vpc", "label": "VPC", "cells": "A2:B4"}],
    "nodes": [{"id": "users", "label": "Users", "at": "A1:B1"}, {"id": "alb", "label": "Load balancer", "at": "A2:B2"},
              {"id": "app1", "label": "App server", "at": "A3"}, {"id": "app2", "label": "App server", "at": "B3"},
              {"id": "db1", "label": "Primary DB", "at": "A4"}, {"id": "db2", "label": "Standby DB", "at": "B4"}],
    "edges": [{"from": "users", "to": "alb", "label": "HTTPS", "step": 1, "say": "A user sends an HTTPS request to the load balancer."},
              {"from": "alb", "to": "app1", "step": 2, "say": "The load balancer forwards the request to a healthy app server."},
              {"from": "alb", "to": "app2", "step": 2},
              {"from": "app1", "to": "db1", "label": "SQL", "step": 3, "say": "The app server reads and writes data on the primary DB instance."},
              {"from": "db1", "to": "db2", "step": 4, "dashed": True, "say": "The primary DB instance copies the data to the standby DB instance."}],
}


def diagram_lint(rec, spec, name=None, label=None):
    path = rec.p("diagrams", "src", (name or spec["id"]) + ".json")
    common.write_json(path, spec)
    rc, out = rec.run("diagram", "lint", "--file", str(path), text=True, label=label or f"diagram lint --file diagrams/src/{path.name}")
    return rc, out


@attempt("diagram lint", "Control: the clean arch spec, then two nodes in one cell",
         "Step 1: the base spec (must pass). Step 2: node app2 moved to cell A3, where app1 is.")
def a_dia_control(rec):
    rc0, _ = diagram_lint(rec, ARCH)
    spec = copy.deepcopy(ARCH)
    spec["nodes"][3]["at"] = "A3"
    rc, _ = diagram_lint(rec, spec)
    return rc in (0, 2), f"Base spec exit {rc0}; the overlapping nodes are rejected." if rc == 1 else f"Base spec exit {rc0}."


@attempt("diagram lint", "Raw diagram with two labels on top of each other",
         "kind raw; the SVG holds two <text class=\"dg-nl\"> elements at the same x and y, plus a third text that starts 2 units to the right.",
         repro="diagrams/src/<id>.json with kind raw and an SVG that has two <text> elements at the same position; diagram lint --file.", severity="high")
def a_dia_raw(rec):
    spec = {"id": "breaker-raw", "kind": "raw", "size": "s", "sample": True, "title": "The two parts of a CIDR block",
            "claim": "The prefix length says how many bits name the network.", "alt": "A bar of 32 bits in two parts.", "svg": "breaker-raw.svg"}
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 132">\n'
           '  <rect class="dg-nb" x="10" y="34" width="158" height="48" rx="4"/>\n'
           '  <text class="dg-nl" x="89" y="55">Network part</text>\n'
           '  <text class="dg-nl" x="89" y="55">Host part of address</text>\n'
           '  <text class="dg-nl" x="91" y="57">Subnet mask bits</text>\n'
           '</svg>\n')
    rec.p("diagrams", "src").mkdir(parents=True, exist_ok=True)
    rec.p("diagrams", "src", "breaker-raw.svg").write_text(svg, encoding="utf-8")
    rc, out = diagram_lint(rec, spec)
    return rc in (0, 2), "The raw kind has no geometry lint at all (TOOLS-diagram.md says so: 'overlap and text width are yours to check'). Three labels in one place pass with exit 0, and so would text wider than its box."


@attempt("diagram lint", "Node label that states an ungrounded limit",
         "Base arch spec; node db1 label 'Max 999 TB' (the number is in neither claim nor say).",
         repro="arch spec with a node label 'Max 999 TB' that the claim and the say lines do not hold.", severity="medium")
def a_dia_number(rec):
    spec = copy.deepcopy(ARCH)
    spec["nodes"][4]["label"] = "Max 999 TB"
    rc, _ = diagram_lint(rec, spec)
    return rc in (0, 2), "TOOLS-rules.md R2 asks the diagram module for this check ('a label with a number with a unit must repeat a value that stands in claim or say'). It is not implemented, so a hard fact can enter the book inside a figure without a fact."


@attempt("diagram lint", "Claim of two sentences with absolute words",
         "claim 'A request passes through three tiers. it always uses 9 hops and never fails.' (second sentence starts in lowercase).",
         repro="arch spec with claim 'One thing is true. another thing always holds.'", severity="low")
def a_dia_claim(rec):
    spec = copy.deepcopy(ARCH)
    spec["claim"] = "A request passes through three tiers. it always uses 9 hops and never fails."
    rc, _ = diagram_lint(rec, spec)
    return rc in (0, 2), "The one-sentence test looks for '. ' followed by a capital letter. (The chapter lint L702 and L705 check the caption again where the figure is embedded.)"


@attempt("gate diagrams", "SVG that does not belong to its spec",
         "The fixture has diagrams/svg/sample-hero.svg and no spec. A valid but different spec is written as diagrams/src/sample-hero.json; diagram build is not run. Then gate 99 --gate diagrams.",
         repro="change diagrams/src/<id>.json (or hand-edit diagrams/svg/<id>.svg) without running diagram build; gate <ch> --gate diagrams.", severity="high")
def a_dia_stale(rec):
    rc0, _ = rec.run("gate", "99", "--gate", "diagrams", label="gate 99 --gate diagrams (fixture, no spec)")
    spec = copy.deepcopy(ARCH)
    spec["id"] = "sample-hero"
    common.write_json(rec.p("diagrams", "src", "sample-hero.json"), spec)
    before = common.sha256_file(rec.p("diagrams", "svg", "sample-hero.svg"))
    rc, res = rec.run("gate", "99", "--gate", "diagrams", label="gate 99 --gate diagrams (new spec, old SVG)")
    same = before == common.sha256_file(rec.p("diagrams", "svg", "sample-hero.svg"))
    rec.note("SVG file", "unchanged old file" if same else "rewritten")
    return rc in (0, 2) and same, "The gate checks that the spec lints and that an SVG file exists. It never renders the spec and compares, so the reader can see a picture that no spec describes (stale, or drawn by hand with overlaps)."


# ---------------------------------------------------------------- runner and report

WORD = {True: "GOT THROUGH", False: "held", "partial": "PARTLY THROUGH", None: "NOT RUN"}


def _cell(text):
    return str(text).replace("|", "\\|").replace("\n", "\\n")


def markdown(results):
    holes = [r for r in results if r["through"] is True]
    partial = [r for r in results if r["through"] == "partial"]
    held = [r for r in results if r["through"] is False]
    skipped = [r for r in results if r["through"] is None]
    lines = ["# Gate break report: practice gates", "",
             "Written by `tools/helpers/break_practice.py` (gate breaker, " + common.today() + "). Nothing in the tool was changed.", "",
             "## Method", "",
             "- Every attempt runs in a fresh copy of the fixture book at `_build/tmp/breaker-practice/`, through `--book-dir`. No real data was touched.",
             "- One change to the fixture `SPEC.json` in the sandbox: `questions.stem_key_overlap_margin_max` is 0.25 (the value of the real `SPEC.json`; the fixture has 1.0, which switches Q113 off). The mock attempts add the same `mock` template and chapters 50 and 51 that `tests/test_qbank.py` uses.",
             "- 'Got through' means: the gate command ended with exit 0 (or 2, warnings only) and stored or accepted the bad input. Controls are bad inputs that the gate is known to reject; they show that the attempt reached the rule.",
             "- A step line reads: command, exit code, first findings or the JSON result (cut at 300 characters).",
             "- Run it again with `python3 aws-saa-book/tools/helpers/break_practice.py` (add `--no-uv` to skip the one attempt that needs `uv` and the package index; `--only=N,N` prints single attempts).", "",
             "## Totals", "",
             f"- Attempts: {len(results)}",
             f"- Got through: {len(holes)}",
             f"- Partly through: {len(partial)}",
             f"- Held (controls included): {len(held)}",
             f"- Not run: {len(skipped)}", "",
             "## Attempts", ""]
    for r in results:
        lines += [f"### {r['n']}. {r['title']}", "",
                  f"- Gate: `{r['gate']}`",
                  f"- Did: {r['did']}",
                  "- Gate answer:"]
        for s in r["steps"]:
            lines.append(f"  - `{_cell(s['cmd'])}` -> exit {s['exit']}: {_cell(s['msg'])}")
        lines += [f"- Result: **{WORD[r['through']]}**" + (f" (severity {r['severity']})" if r["through"] in (True, "partial") else ""),
                  f"- Note: {r['note']}", ""]
    lines += ["## HOLES (bad inputs that passed)", "",
              "Ordered by severity, then by attempt number. Each line: attempt, gate, what passed, smallest reproduction.", ""]
    order = {"high": 0, "medium": 1, "low": 2}
    for r in sorted(holes + partial, key=lambda r: (order.get(r["severity"], 3), r["n"])):
        tag = "" if r["through"] is True else " (partly)"
        lines += [f"- **H{r['n']:02d}** [{r['severity']}]{tag} `{r['gate']}`: {r['title']}.",
                  f"  - Reproduce: {r['repro'] or r['did']}"]
    lines += ["", "## Root causes (for the owner of the fix)", ""] + ROOT_CAUSES
    lines += ["", "## Limits of this report", "",
              "- The fixture service is invented, so 'bad' here means bad by the written rules (RULINGS, TOOLS, SPEC), not bad AWS facts.",
              "- Attempts 14, 56 and 61 need write or read access to files under the book folder. Every agent of the build has that access.",
              "- The fixture `SPEC.json` sets `key_position_share_max`, `key_is_longest_share_max` and `stem_key_overlap_margin_max` to 1.0, so the tool's own tests of Q113 and Q202 patch the values. Attempts here use 0.25 for Q113 and leave Q202 alone (it needs 10 questions).",
              "- Not tried: `tasks emulate`, `drills build`, `cards build`, the web app, and the chapter lint of hand-written Markdown (another breaker has that part).", ""]
    return "\n".join(lines)


ROOT_CAUSES = [
    "1. **Word counting splits on whitespace only** (`lint.word_count`). Hyphen- or slash-joined words defeat every word limit: card back, spoken scripts, step texts, options (attempts 34, 39).",
    "2. **Similarity is measured on the stem only, and as a Jaccard value.** `q dedupe` and K04 never compare options, keys or explanations; reordering clauses or adding one sentence drops the value below 0.6 (9, 27). Q113 has the same weakness: a long stem dilutes the overlap of a key that is made of stem words (6).",
    "3. **Duplicate checks are not part of any chapter gate.** `q add`, `q lint CH` and the `questions` gate do not run `q dedupe`; only `q lint --all` does (8). `mocks check` ignores duplicates inside one mock and copies of drill questions (28, 29). A rejected question can be added again (24).",
    "4. **Adjudication trusts the answer files.** No solver identity or independence (17, 18), no required lens evidence (19), no relevance or minimum length for citations (20), no schema for rows (21), and no binding of an answer to the question revision or text (22). Round 1 allows any number of edits (23).",
    "5. **Length and position leaks are checked only as bank shares.** Q104 is off below a mean of 10 words and measures against a mean that the key itself raises (4, 5); Q202 needs 10 questions and is a warning. The pack shuffle uses a public seed (14).",
    "6. **Literal lists instead of rules.** Option letters (7), negative stems (10), banned option phrases (11), list answers (32), number words (35, 42), create verbs (44), banned commands (47, 48, 49), shell operators (50), dollar amounts (52).",
    "7. **Cards and spoken scripts are not tied to their facts.** Only digits with a unit are checked; a sentence can contradict the fact it lists, or state 'always' and 'never' with no fact (36, 41). Follow-up answers and key points have no length limit (40).",
    "8. **Task cleanup is paired by verb and noun, not by resource.** Another name, `--dry-run`, or `stop` for `run` satisfy T107 (45, 46); tag patterns match anywhere in the command (51); untaggable creates need neither tag nor prefix (54); a Look can delete (53).",
    "9. **Reports and pictures are not bound to a tool run.** A hand-written CLI report satisfies T113 (56); the `diagrams` gate accepts any SVG file next to a spec that lints (61); the `raw` kind has no geometry check (58); node labels with numbers are not held against claim or say (59).",
    "10. **The CLI model checks option names that start with `--` and nothing else** (55): single-dash typos, bare words, shorthand keys, enum values and JMESPath are not checked.",
]


def main():
    only = None
    for arg in sys.argv[1:]:
        if arg.startswith("--only="):
            only = {int(x) for x in arg.split("=", 1)[1].split(",")}
    results = []
    for n, att in enumerate(ATTEMPTS, 1):
        if only and n not in only:
            continue
        rec = Rec()
        rec.fresh()
        try:
            through, note = att["fn"](rec)
        except Exception as exc:  # an attempt that crashes is reported, not hidden
            import traceback
            through, note = None, f"the attempt script failed: {exc!r} {traceback.format_exc().splitlines()[-3:]}"
        results.append({"n": n, "gate": att["gate"], "title": att["title"], "did": att["did"], "steps": rec.steps,
                        "through": through, "note": note, "repro": att["repro"], "severity": att["severity"]})
        word = {True: "THROUGH", False: "held", "partial": "PARTIAL", None: "NOT RUN"}[through]
        print(f"{n:02d} {word:8} {att['gate']}: {att['title']}")
    out = common.REAL_BOOK / "_build" / "reports"
    if not only:
        common.write_json(out / "gate-break-practice.json", results)
        (out / "gate-break-practice.md").write_text(markdown(results), encoding="utf-8")
        print("wrote", common.rel(out / "gate-break-practice.md"))
    else:
        for r in results:
            print(json.dumps(r, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
