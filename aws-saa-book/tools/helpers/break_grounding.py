"""Gate breaker for the grounding gates (facts add/verify/vote/finalize/amend, lint fact links, sync --check).

Run from the repo root:   python3 aws-saa-book/tools/helpers/break_grounding.py
Works only in the sandbox aws-saa-book/_build/tmp/breaker-grounding (a copy of the test fixture book).
Writes aws-saa-book/_build/reports/gate-break-grounding.json (raw results of every attempt).
Standard library only. It never fixes anything; it only records what the gates answer.
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tests"))
import sandbox  # noqa: E402
from saalib import common  # noqa: E402

SB = common.REAL_BOOK / "_build" / "tmp" / "breaker-grounding"
OUT = common.REAL_BOOK / "_build" / "reports" / "gate-break-grounding.json"
URL = "https://docs.aws.amazon.com/widget-store/latest/userguide/limits.html"
SID = "docs/fixture/widget-store/limits"
DEEP = "99-sample/2-deep.md"
ANCHOR = "This default protects the widgets of a new project from a mistake. The owner decides later who else reads the shelf."
RESULTS = []


def reset():
    if SB.exists():
        shutil.rmtree(SB)
    shutil.copytree(sandbox.FIXTURE, SB)


def saa(*args):
    code, out, err = sandbox.run(SB, *args, "--json")
    try:
        obj = json.loads(out)
    except ValueError:
        obj = None
    return code, obj, (out.strip() + " " + err.strip()).strip()


def short(code, obj, raw, limit=420):
    if isinstance(obj, dict):
        msgs = []
        for key in ("rejected", "failed", "refused"):
            for row in obj.get(key) or []:
                for f in row.get("errors", []):
                    msgs.append(f"{f.get('code')} {f.get('msg')}")
        if not msgs and obj.get("errors"):
            msgs = [f"{f.get('code')} {f.get('msg')}" if isinstance(f, dict) else str(f) for f in obj["errors"]]
        if msgs:
            text = "; ".join(msgs)
        else:
            text = json.dumps({k: v for k, v in obj.items() if k not in ("dependents", "inputs", "counts")}, ensure_ascii=False)
    else:
        text = raw
    text = " ".join(text.split())
    return f"exit {code}: " + (text[:limit] + ("..." if len(text) > limit else ""))


def put(name, obj):
    path = SB / "_in" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")
    return str(path)


def fact(fid, claim, display, quote, kind="behavior", hard=True, **kw):
    f = {"id": fid, "service": "widget", "home_chapter": "99", "kind": kind, "claim": claim,
         "question": "What does the page say about this?",
         "values": [{"key": "v", "display": display}],
         "qualifiers": {"scope": "per shelf", "default_or_max": "max" if kind in ("limit", "quota") else "", "adjustable": False, "condition": ""},
         "evidence": [{"source_id": SID, "url": URL, "quote": quote}],
         "source_tier": 1, "hard": hard, "tier0": False, "volatility": "stable", "changed": None, "exam_relevance": "core"}
    f.update(kw)
    return f


def status(fid):
    for row in common.read_jsonl(SB / "data" / "facts" / "widget.jsonl"):
        if row["id"] == fid:
            return row.get("status")
    return "not-stored"


def record(aid, gate, did, answers, through, note="", repro=""):
    RESULTS.append({"id": aid, "gate": gate, "did": did, "answers": answers, "through": through, "note": note, "repro": repro})
    print(f"{aid} [{gate}] through={through}")
    for a in answers:
        print("    " + a[:300])


def add_and_finalize(f, votes=None, voter="verifier-b"):
    """facts add --by miner-a, optional votes, facts finalize. Returns (answers, final status)."""
    answers = []
    r = saa("facts", "add", "--file", put("fact.json", f), "--by", "miner-a")
    answers.append("facts add -> " + short(*r))
    if status(f["id"]) == "not-stored":
        return answers, "not-stored"
    if votes:
        r = saa("facts", "vote", "--file", put("votes.json", votes), "--by", voter)
        answers.append(f"facts vote --by {voter} -> " + short(*r))
    r = saa("facts", "finalize", f["id"])
    answers.append("facts finalize -> " + short(*r))
    return answers, status(f["id"])


# ------------------------------------------------------------------ facts: add / verify

def facts_attacks():
    reset()
    f = fact("widget-x-fab", "A shelf holds up to 900 widgets.", "900 widgets", "Each shelf can hold up to 900 widgets.", kind="limit")
    a, st = add_and_finalize(f)
    record("F01", "facts add (M3)", "Fabricated quote: the real sentence with 500 changed to 900.", a, st == "verified",
           "control: must be rejected")

    reset()
    f = fact("widget-x-stitch", "A shelf is a Regional resource that holds up to 500 widgets.", "500 widgets",
             "A shelf is a Regional resource. Each shelf can hold up to 500 widgets.", kind="limit")
    a, st = add_and_finalize(f)
    record("F02", "facts add (M3)", "Quote stitched from two real sentences that are not adjacent on the page (line 7 first half + line 8).", a, st != "not-stored")

    reset()
    f = fact("widget-x-move", "You can move a shelf to another Region.", "move a shelf to another Region",
             "move a shelf to another Region. To use another Region, copy the shelf.", hard=False)
    a, st = add_and_finalize(f)
    record("F03", "facts add (M4) + finalize", "Real quote cut so that the first two words `You cannot` are dropped; claim says the opposite "
           "(`You can move a shelf`); kind behavior, hard false, no votes.", a, st == "verified",
           "A quote of 8 or more words may start in the middle of a sentence. `can` is no absolute word, so M11 accepts hard=false, and a "
           "fact that is not hard is verified without any vote.",
           "facts add a fact with claim `You can move a shelf to another Region.`, display `move a shelf to another Region`, quote "
           "`move a shelf to another Region. To use another Region, copy the shelf.`, kind behavior, hard false; then facts finalize ID -> verified")

    reset()
    f = fact("widget-x-num", "A crate holds up to 500 widgets.", "500 widgets", "A crate can hold up to 50 widgets.", kind="limit")
    a, st = add_and_finalize(f)
    record("F04", "facts add (M5)", "Real quote (50 widgets), claim and display carry another number (500 widgets).", a, st != "not-stored", "control")

    reset()
    f = fact("widget-x-unit", "Widget Store deletes an empty crate after 7 hours.", "7 hours",
             "Widget Store deletes an empty crate after 7 days.")
    a, st = add_and_finalize(f)
    record("F05", "facts add (M5)", "Real quote (7 days), claim and display carry another unit (7 hours).", a, st != "not-stored", "control")

    reset()
    f = fact("widget-x-unit2", "Widget Store deletes an empty crate after 7 full hours.", "7 full hours",
             "Widget Store deletes an empty crate after 7 days.", hard=False)
    a, st = add_and_finalize(f)
    record("F06", "facts add (M5, M11) + finalize", "Same unit swap, with one adjective between number and unit (`7 full hours`), hard false, no votes.",
           a, st == "verified",
           "M5 and M11 see a unit only directly after the number (one optional space or hyphen). `7 full hours` is a bare 7, which the quote has.",
           "claim `Widget Store deletes an empty crate after 7 full hours.`, display `7 full hours`, quote `Widget Store deletes an empty crate "
           "after 7 days.`, kind behavior, hard false; facts add, facts finalize -> verified with no vote")

    reset()
    f = fact("widget-x-unit3", "Widget Store deletes an empty crate after 7  hours.", "7  hours",
             "Widget Store deletes an empty crate after 7 days.", hard=False)
    a, st = add_and_finalize(f)
    record("F07", "facts add (M5, M11) + finalize", "Unit swap with two spaces between number and unit (`7  hours`), hard false, no votes.", a, st == "verified",
           "The unit regex allows one space; a second space hides the unit.",
           "as F06 with claim and display `7  hours` (two spaces)")

    reset()
    f = fact("widget-x-mag", "A crate holds 50 thousand widgets.", "50 thousand widgets", "A crate can hold up to 50 widgets.", hard=False)
    a, st = add_and_finalize(f)
    record("F08", "facts add (M5, M11) + finalize", "Magnitude word after the real number (`50 thousand widgets` against a quote with 50), hard false, no votes.",
           a, st == "verified", "The digit string 50 is in the quote; `thousand` is neither unit nor count noun.",
           "claim `A crate holds 50 thousand widgets.`, display `50 thousand widgets`, quote `A crate can hold up to 50 widgets.`, hard false; add, finalize -> verified")

    reset()
    f = fact("widget-x-k", "A crate holds 50K widgets.", "50K widgets", "A crate can hold up to 50 widgets.", hard=False)
    a, st = add_and_finalize(f)
    record("F09", "facts add (M5, M11) + finalize", "Suffix on the number (`50K widgets` against a quote with 50), hard false, no votes.", a, st == "verified",
           "The number regex has no check of the character after the digits.", "as F08 with `50K widgets`")

    reset()
    f = fact("widget-x-word", "A shelf holds nine hundred widgets.", "nine hundred widgets", "Each shelf can hold up to 500 widgets.", hard=False)
    a, st = add_and_finalize(f)
    record("F10", "facts add (M5, M11) + finalize", "Number written in words (`nine hundred widgets`) against a quote with 500, hard false, no votes.",
           a, st == "verified", "On the claim side a number word counts only directly before a unit or count noun, and only zero to twelve.",
           "claim `A shelf holds nine hundred widgets.`, display `nine hundred widgets`, quote `Each shelf can hold up to 500 widgets.`, hard false; add, finalize -> verified")

    reset()
    f = fact("widget-x-false", "A shelf copies its widgets to every other Region automatically, and every user of the account reads it.",
             "copies its widgets to every other Region", "A crate is a container for widgets that you ship between Regions.", hard=False)
    a, st = add_and_finalize(f)
    record("F11", "facts add (M7, M11) + finalize", "False claim without a number or a listed absolute word, with an unrelated real quote; display taken from the claim; "
           "hard false, no votes.", a, st == "verified",
           "M7 accepts a display that stands only in the claim. Nothing mechanical ties the claim to the quote, and a non-hard fact needs no vote.",
           "claim `A shelf copies its widgets to every other Region automatically, and every user of the account reads it.`, display "
           "`copies its widgets to every other Region`, quote `A crate is a container for widgets that you ship between Regions.`, kind behavior, "
           "hard false; facts add, facts finalize -> verified")

    reset()
    f = fact("widget-x-defmax", "By default, a shelf holds 500 widgets, and you can raise this default.", "500 widgets",
             "Each shelf can hold up to 500 widgets.", kind="default",
             qualifiers={"scope": "per shelf", "default_or_max": "default", "adjustable": True, "condition": ""})
    a, st = add_and_finalize(f)
    record("F12", "facts add + finalize", "Default against maximum: the quote states a maximum, the fact says default and adjustable (the quota table says No).",
           a, st == "verified", "The mechanical checks pass (status mech-pass); the fact stays pending for an entail vote. Stopped only by the voter." if st == "mech-pass" else "")

    # same fact, then the miner votes under another label
    r = saa("facts", "vote", "--file", put("votes.json", [{"fact": "widget-x-defmax", "rev": 1, "lens": "entail", "verdict": "support", "reason": "The quote states the claim."}]), "--by", "miner-b")
    a2 = ["facts vote --by miner-b (same agent, other label) -> " + short(*r)]
    r = saa("facts", "finalize", "widget-x-defmax")
    a2.append("facts finalize -> " + short(*r))
    record("F13", "facts vote + finalize", "The author of F12 (label miner-a) votes `support` on the own fact under a second label (miner-b).", a2,
           status("widget-x-defmax") == "verified", "A label is free text. One agent with two labels is author and verifier.",
           "facts add --by miner-a; facts vote --by miner-b with verdict support; facts finalize -> verified")

    reset()
    saa("facts", "add", "--file", put("fact.json", f), "--by", "miner-a")
    r = saa("facts", "vote", "--file", put("votes.json", [{"fact": "widget-x-defmax", "rev": 1, "lens": "entail", "verdict": "support", "reason": "The quote states the claim."}]), "--by", "Miner-A")
    a = ["facts vote --by Miner-A -> " + short(*r)]
    r = saa("facts", "finalize", "widget-x-defmax")
    a.append("facts finalize -> " + short(*r))
    record("F14", "facts vote", "Author label `miner-a`, vote under `Miner-A` (case changed).", a, status("widget-x-defmax") == "verified",
           "The author test is an exact string comparison.", "facts add --by miner-a; facts vote --by Miner-A; facts finalize -> verified")

    reset()
    saa("facts", "add", "--file", put("fact.json", f), "--by", "miner-a")
    a = []
    r = saa("facts", "vote", "--file", put("votes.json", [{"fact": "widget-x-defmax", "rev": 1, "lens": "entail", "verdict": "not-supported", "reason": "the quote states a maximum"}]), "--by", "verifier-b")
    a.append("honest vote not-supported --by verifier-b -> " + short(*r))
    r = saa("facts", "finalize", "widget-x-defmax")
    a.append("facts finalize -> " + short(*r) + f" [status {status('widget-x-defmax')}]")
    r = saa("facts", "vote", "--file", put("votes.json", [{"fact": "widget-x-defmax", "rev": 1, "lens": "entail", "verdict": "support", "reason": "The quote states the claim."}]), "--by", "verifier-b")
    a.append("second vote support, label verifier-b reused by the attacker -> " + short(*r))
    r = saa("facts", "finalize", "widget-x-defmax")
    a.append("facts finalize -> " + short(*r))
    record("F15", "facts vote + finalize", "A verifier disputes the fact; the attacker reuses the verifier's label for a later `support` vote on the same rev.",
           a, status("widget-x-defmax") == "verified",
           "The last vote of a voter and lens counts, so a disputed fact becomes verified without an amend and without a new rev.",
           "vote not-supported --by verifier-b; finalize (disputed); vote support --by verifier-b; finalize -> verified")

    reset()
    f = fact("widget-x-table", "An account starts with 500 shelves in each Region.", "500 shelves",
             "Resource Default Adjustable Shelves per Region 20 Yes Widgets per shelf 500 No", kind="quota",
             qualifiers={"scope": "per Region", "default_or_max": "default", "adjustable": True, "condition": ""})
    a, st = add_and_finalize(f)
    record("F16", "facts add (M4, M8)", "Quote made of the table header and two table rows written without pipes (so no `table_header` is asked for); "
           "the claim pairs the 500 of one row with the name of another row.", a, st in ("mech-pass", "verified"),
           "normalize_text removes pipes and rule lines, so flattened table text is `verbatim`. The M4 table rules apply only when the quote "
           "starts with `|`. The fact is mech-pass and waits for an entail vote.",
           "quote `Resource Default Adjustable Shelves per Region 20 Yes Widgets per shelf 500 No`, claim `An account starts with 500 shelves in each Region.`, display `500 shelves`, kind quota -> mech-pass")

    reset()
    f = fact("widget-x-head", "Shelves and crates are the two resources of the service.", "Shelves",
             "copy the shelf. Crates A crate is a container for widgets", hard=False)
    a, st = add_and_finalize(f)
    record("F17", "facts add (M3, M8)", "Quote that runs across a section heading (`## Crates`) and starts and ends in the middle of sentences.", a, st == "verified",
           "Heading text is joined to the body text by the normaliser; only a quote that is exactly one heading line is page furniture.",
           "quote `copy the shelf. Crates A crate is a container for widgets` -> accepted")

    reset()
    f = fact("widget-x-tag", "You can now move a shelf to another Region.", "can now move a shelf",
             "You <can now move a shelf, where before you> cannot move a shelf to another Region. To use another Region, copy the shelf.", hard=False)
    a, st = add_and_finalize(f)
    record("F18", "facts add (M3, M7) + finalize", "Words smuggled into a real quote inside angle brackets. The stored `verbatim` quote reads "
           "`You <can now move a shelf, where before you> cannot move ...`; the display `can now move a shelf` is found in that quote.", a, st == "verified",
           "normalize_text drops anything of the form <...> (up to 400 characters) on both sides, so M3 matches (the display is accepted because it stands in the claim). The stored quote, which the fact sheet prints and the verifier packet shows, is not the page text.",
           "quote `You <can now move a shelf, where before you> cannot move a shelf to another Region. To use another Region, copy the shelf.` -> M3 passes")

    # fabricated snapshot
    reset()
    snap = SB / "_build" / "corpus" / "snap" / "docs" / "fixture" / "widget-store"
    text = ("# Amazon Widget Store pricing\n\nAWS Documentation Amazon Widget Store User Guide Feedback Preferences Contact Us English Create an AWS Account\n\n"
            "Each shelf can hold up to 9000 widgets in bulk mode.\n")
    (snap / "pricing.txt").write_text(text, encoding="utf-8")
    purl = "https://docs.aws.amazon.com/widget-store/latest/userguide/pricing.html"
    (snap / "pricing.meta.json").write_text(json.dumps({"source_id": "docs/fixture/widget-store/pricing", "url": purl, "title": "Amazon Widget Store pricing"}), encoding="utf-8")
    f = fact("widget-x-fake", "A shelf holds up to 9000 widgets in bulk mode.", "9000 widgets", "Each shelf can hold up to 9000 widgets in bulk mode.", kind="limit",
             evidence=[{"source_id": "docs/fixture/widget-store/pricing", "url": purl, "quote": "Each shelf can hold up to 9000 widgets in bulk mode."}])
    a, st = add_and_finalize(f, votes=[{"fact": "widget-x-fake", "rev": 1, "lens": "entail", "verdict": "support", "reason": "the quote states it"}])
    record("F19", "facts add (M2)", "Snapshot written by hand into the corpus folder (a .txt and a three-key .meta.json with an allowed URL, never fetched), "
           "then a fact that quotes it and an honest entail vote.", a, st == "verified",
           "M2 asks only that the .txt exists and that the meta `url` equals the evidence URL. There is no check that the fetch tool made the snapshot "
           "(no fetch log entry, no raw file, no `sha256` in the meta). An honest verifier sees a matching quote and supports.",
           "write _build/corpus/snap/<any/id>.txt and .meta.json {source_id, url on an allowed host}; facts add a fact that quotes it -> mech-pass")

    f = fact("widget-x-nav", "The user guide has a feedback link and a link to create an AWS account.", "Create an AWS Account",
             "AWS Documentation Amazon Widget Store User Guide Feedback Preferences Contact Us English Create an AWS Account", hard=False,
             evidence=[{"source_id": "docs/fixture/widget-store/pricing", "url": purl,
                        "quote": "AWS Documentation Amazon Widget Store User Guide Feedback Preferences Contact Us English Create an AWS Account"}])
    a, st = add_and_finalize(f)
    record("F20", "facts add (M8)", "Quote taken from a navigation line of the page (breadcrumb and footer words), none of them in the BOILERPLATE list.", a, st == "verified",
           "M8 knows ten fixed phrases. Navigation text without one of them is an accepted quote.",
           "quote `AWS Documentation Amazon Widget Store User Guide Feedback Preferences Contact Us English Create an AWS Account` -> accepted")

    # tampered snapshot
    reset()
    path = SB / "_build" / "corpus" / "snap" / "docs" / "fixture" / "widget-store" / "limits.txt"
    sandbox.replace_text(path, "Each shelf can hold up to 500 widgets.", "Each shelf can hold up to 500 widgets.\nIn bulk mode, each shelf can hold up to 9000 widgets.")
    r = saa("facts", "verify", "--service", "widget")
    record("F21", "facts verify (M2)", "One sentence added by hand to the snapshot .txt that the seven verified fixture facts cite; meta untouched.",
           ["facts verify --service widget -> " + short(*r)], r[0] == 0, "control: the stored evidence hash no longer matches")

    reset()
    sandbox.replace_text(path, "Each shelf can hold up to 500 widgets.", "Each shelf can hold up to 500 widgets.\nIn bulk mode, each shelf can hold up to 9000 widgets.")
    f = fact("widget-x-tamper", "In bulk mode, a shelf holds up to 9000 widgets.", "9000 widgets", "In bulk mode, each shelf can hold up to 9000 widgets.", kind="limit")
    a, st = add_and_finalize(f, votes=[{"fact": "widget-x-tamper", "rev": 1, "lens": "entail", "verdict": "support", "reason": "the quote states it"}])
    r = saa("facts", "verify", "widget-x-tamper")
    a.append("facts verify widget-x-tamper -> " + short(*r))
    record("F22", "facts add (M2)", "Same hand edit of the snapshot .txt, then a NEW fact that quotes the added sentence (the meta still holds the old sha256).",
           a, st == "verified",
           "`facts add` fills evidence.sha256 from the current .txt and never compares the .txt with the `sha256` of its own meta file. "
           "Only facts stored before the edit notice it (F21).",
           "append a sentence to a snapshot .txt; facts add a fact that quotes it -> mech-pass; one support vote -> verified")

    # hand-edited status
    reset()
    f = fact("widget-x-hand", "By default, a shelf holds 500 widgets, and you can raise this default.", "500 widgets",
             "Each shelf can hold up to 500 widgets.", kind="default",
             qualifiers={"scope": "per shelf", "default_or_max": "default", "adjustable": True, "condition": ""})
    saa("facts", "add", "--file", put("fact.json", f), "--by", "miner-a")

    def set_verified(rows):
        for row in rows:
            if row["id"] == "widget-x-hand":
                row["status"] = "verified"
                row["votes"] = [{"lens": "entail", "verdict": "support", "voter": "fixture-verifier-a", "rev": 1}]
    sandbox.edit_jsonl(SB / "data" / "facts" / "widget.jsonl", set_verified)
    r1 = saa("gate", "99", "--gate", "facts-final")
    hit1 = "widget-x-hand" in r1[2]
    r2 = saa("facts", "verify", "widget-x-hand")
    record("F23", "facts-final gate (F04), facts verify", "Facts file edited by hand: status set to verified and a `votes` summary written into the fact; the vote log untouched.",
           ["gate 99 --gate facts-final -> " + short(*r1), "facts verify widget-x-hand -> " + short(*r2) + f" [status now {status('widget-x-hand')}]"],
           not hit1 and r2[0] == 0, "control: F04 compares with the vote log")

    reset()
    saa("facts", "add", "--file", put("fact.json", f), "--by", "miner-a")
    sandbox.edit_jsonl(SB / "data" / "facts" / "widget.jsonl", set_verified)
    with open(SB / "_build" / "facts" / "votes" / "widget.jsonl", "a", encoding="utf-8") as h:
        h.write(json.dumps({"fact": "widget-x-hand", "rev": 1, "lens": "entail", "verdict": "support", "voter": "fixture-verifier-a",
                            "ts": "2026-10-04T00:10:00Z", "batch": "99-entail-001", "reason": "The quote states it.", "source_id": None,
                            "quote": None, "answer": None}) + "\n")
    r1 = saa("gate", "99", "--gate", "facts-final")
    hit1 = "widget-x-hand" in r1[2]
    r2 = saa("facts", "verify", "widget-x-hand")
    record("F24", "facts-final gate (F04), facts verify", "As F23, plus one forged line appended by hand to the vote log `_build/facts/votes/widget.jsonl`.",
           ["gate 99 --gate facts-final -> " + short(*r1) + (" [names widget-x-hand]" if hit1 else " [does not name widget-x-hand]"),
            "facts verify widget-x-hand -> " + short(*r2) + f" [status {status('widget-x-hand')}]"],
           not hit1 and r2[0] == 0 and status("widget-x-hand") == "verified",
           "The vote log is a plain file with no signature or chain; F04 trusts it.",
           "set status verified in data/facts/<s>.jsonl and append one vote line to _build/facts/votes/<s>.jsonl")

    reset()

    def flip_claim(rows):
        for row in rows:
            if row["id"] == "widget-shelf-move":
                row["claim"] = "You can move a shelf to another Region at any time, so there is no need to copy the shelf."
    sandbox.edit_jsonl(SB / "data" / "facts" / "widget.jsonl", flip_claim)
    r1 = saa("facts", "verify", "widget-shelf-move")
    r2 = saa("gate", "99", "--gate", "facts-final")
    hit = "widget-shelf-move" in r2[2]
    r3 = saa("facts", "render", "--service", "widget")
    sheet = (SB / "facts" / "widget.md").read_text(encoding="utf-8") if (SB / "facts" / "widget.md").exists() else ""
    record("F25", "facts verify, facts-final gate", "Claim of a verified fact rewritten by hand to the opposite; rev, status, displays and votes untouched.",
           ["facts verify widget-shelf-move -> " + short(*r1), "gate 99 --gate facts-final -> " + short(*r2) + (" [names the fact]" if hit else " [does not name the fact]"),
            "facts render -> sheet holds the false claim: " + str("You can move a shelf to another Region at any time" in sheet)],
           r1[0] == 0 and not hit and status("widget-shelf-move") == "verified",
           "A vote is bound to (fact id, rev) only, not to a hash of claim, values and evidence. A hand edit that keeps `rev` keeps the votes.",
           "edit `claim` of a verified fact in data/facts/<s>.jsonl without touching `rev`; facts verify -> ok; the fact sheet prints the new claim")


# ------------------------------------------------------------------ facts: amend

def amend_attacks():
    reset()
    patch = put("patch.json", {"claim": "A shelf is a Regional resource that copies its widgets to each other AWS Region.", "hard": False})
    r1 = saa("facts", "amend", "widget-shelf-scope", "--file", patch, "--reason", "wording")
    r2 = saa("facts", "finalize", "widget-shelf-scope")
    r3 = saa("lint", "99", "--draft")
    hit = "widget-shelf-scope" in r3[2]
    record("A01", "facts amend + finalize", "Amend of a verified hard fact: new false claim plus `hard: false` (the displays stay, so no dependent is reset).",
           ["facts amend -> " + short(*r1), "facts finalize -> " + short(*r2) + f" [status {status('widget-shelf-scope')}]",
            "lint 99 --draft names the fact: " + str(hit)],
           status("widget-shelf-scope") == "verified",
           "The amend empties the votes, but `hard: false` removes the need for any vote, so finalize verifies the new claim at once. "
           "`facts amend` has no --by, so the change is not attributed.",
           "patch {\"claim\": \"A shelf is a Regional resource that copies its widgets to each other AWS Region.\", \"hard\": false}; "
           "facts amend widget-shelf-scope --file PATCH --reason wording; facts finalize widget-shelf-scope -> verified")

    reset()
    r1 = saa("facts", "amend", "widget-shelf-scope", "--file", put("patch.json", {"status": "verified", "votes": [], "rev": 1}), "--reason", "x")
    record("A02", "facts amend", "Patch that tries to set `status`, `votes` and `rev` directly.", ["facts amend -> " + short(*r1)], r1[0] == 0, "control")

    reset()
    r1 = saa("facts", "amend", "widget-crate-capacity", "--file", put("patch.json", {"claim": "A crate holds up to 500 widgets.",
             "values": [{"key": "max", "display": "500 widgets"}]}), "--reason", "x")
    record("A03", "facts amend (M5)", "Amend that changes the number of a verified fact (50 to 500) without new evidence.", ["facts amend -> " + short(*r1)],
           r1[0] == 0, "control")

    reset()
    r1 = saa("facts", "amend", "widget-crate-capacity", "--file", put("patch.json", {
        "claim": "A crate holds 50 thousand widgets.", "kind": "behavior", "hard": False,
        "values": [{"key": "max", "display": "50 thousand widgets", "spoken": "fifty thousand widgets"}]}), "--reason", "unit")
    r2 = saa("facts", "finalize", "widget-crate-capacity")
    deep = (SB / DEEP).read_text(encoding="utf-8")
    r3 = saa("sync", "99")
    r4 = saa("facts", "render", "--service", "widget")
    r5 = saa("lint", "99", "--draft")
    crate = [f for f in ((r5[1] or {}).get("errors") or []) if "widget-crate-capacity" in json.dumps(f) or "50 thousand" in json.dumps(f)]
    record("A04", "facts amend + finalize + lint", "Amend of the verified limit `50 widgets`: kind behavior, hard false, claim and display `50 thousand widgets`. "
           "The tool then rewrites the link text in the chapter by itself.",
           ["facts amend -> " + short(*r1), "facts finalize -> " + short(*r2) + f" [status {status('widget-crate-capacity')}]",
            "2-deep.md now holds `[50 thousand widgets](../facts/widget.md#widget-crate-capacity)`: " + str("[50 thousand widgets](" in deep),
            f"lint 99 --draft -> exit {r5[0]}, errors that name the fact or the new value: {len(crate)}"],
           status("widget-crate-capacity") == "verified" and "[50 thousand widgets](" in deep and not crate,
           "Combines F08 with A01. One command changes the canon and the prose; the chapter is marked stale and the items are reset, "
           "but every gate passes again when the stages rerun, with no vote on the new value.",
           "patch {claim: `A crate holds 50 thousand widgets.`, kind: behavior, hard: false, values: [{key: max, display: `50 thousand widgets`}]}; "
           "facts amend widget-crate-capacity --file PATCH --reason unit; facts finalize widget-crate-capacity")


# ------------------------------------------------------------------ lint

def lint_state():
    saa("sync", "99")
    saa("facts", "render", "--all")
    code, obj, raw = saa("lint", "99")
    obj = obj or {}
    key = lambda f: (f.get("code"), f.get("file"), f.get("msg"))
    return code, {key(f) for f in obj.get("errors", [])}, {key(f) for f in obj.get("warnings", [])}, raw


def lint_attack(aid, did, edit, note="", repro="", expect_block=False, file=DEEP):
    reset()
    _c, base_e, base_w, _raw = lint_state()
    reset()
    edit()
    code, errs, warns, raw = lint_state()
    new_e = sorted(errs - base_e)
    new_w = sorted(warns - base_w)
    answers = [f"lint 99 -> exit {code}; new errors against the unchanged fixture: {len(new_e)}; new warnings: {len(new_w)}"]
    answers += [f"new error {c} {f}: {m}" for c, f, m in new_e[:4]]
    answers += [f"new warning {c} {f}: {m}" for c, f, m in new_w[:3]]
    if not errs and not base_e and not raw.startswith("{"):
        answers.append("raw: " + raw[:200])
    record(aid, "lint (L303/L304/L306)", did, answers, not new_e, note if not new_e else ("control" if expect_block else ""), repro if not new_e else "")


def para(text):
    return lambda: sandbox.replace_text(SB / DEEP, ANCHOR, ANCHOR + "\n\n" + text)


LINK = "../facts/widget.md#widget-shelf-max-widgets"


def lint_attacks():
    where = "added as a new paragraph in `2-deep.md`, section How it works (role how, strict)"
    lint_attack("L01", f"Control: `Each crate always holds 50 widgets.` {where}.", para("Each crate always holds 50 widgets."), expect_block=True)
    lint_attack("L02", "Bare number with a non-breaking space: `A crate holds 9000\\u00a0widgets.`", para("A crate holds 9000 widgets."),
                "The number regex allows a plain space or a hyphen only; the text unit is not normalised before matching.",
                "`A crate holds 9000<NBSP>widgets.` in a strict section -> no L304")
    lint_attack("L03", "Bare number written as a word: `A crate holds nine thousand widgets.`", para("A crate holds nine thousand widgets."),
                "Stated in TOOLS-rules R2 (number words are not matched). The reader still gets an ungrounded hard number.",
                "`A crate holds nine thousand widgets.` -> no L304")
    lint_attack("L04", "One adjective between number and count noun: `A crate holds 9000 small widgets.`", para("A crate holds 9000 small widgets."),
                "Real cases of the same shape: `5 read replicas`, `1,000 concurrent executions`, `200 route tables`, `5 Elastic IP addresses`.",
                "`A crate holds 9000 small widgets.` -> no L304")
    lint_attack("L05", "Bold around the number or the noun: `A crate holds 9000 **widgets**.`", para("A crate holds 9000 **widgets**."), "",
                "`A crate holds 9000 **widgets**.`")
    lint_attack("L06", "HTML entity for the space: `A crate holds 9000&nbsp;widgets.`", para("A crate holds 9000&nbsp;widgets."),
                "Entities are not decoded before the number and absolute-word rules.", "`A crate holds 9000&nbsp;widgets.` -> no L304")
    lint_attack("L07", "HTML entity inside an absolute word: `A shelf is alw&#97;ys private.` (renders as `always`)", para("A shelf is alw&#97;ys private."),
                "", "`A shelf is alw&#97;ys private.` -> no L304")
    lint_attack("L08", "Zero-width space inside an absolute word: `A crate is on\\u200bly for shipping, and it is ne\\u200bver private.`",
                para("A crate is on​ly for shipping, and it is ne​ver private."), "", "`on<ZWSP>ly`, `ne<ZWSP>ver` -> no L304")
    lint_attack("L09", "Absolute claims with words outside the list: `A crate is invariably public. No one except the owner is able to delete it, and "
                "nobody is able to move it.`", para("A crate is invariably public. No one except the owner is able to delete it, and nobody is able to move it."),
                "The list has nine entries. `no`, `not`, `all`, `every`, `any`, `none`, `maximum`, `minimum`, `at least`, `no more than`, `limited to`, "
                "`unlimited`, `required`, `does not support`, `is not possible`, `automatically`, `exclusively` are free.",
                "`A crate is invariably public. No one except the owner is able to delete it.` -> no L304")
    lint_attack("L10", "`can not` written as two words: `You can not copy a crate.`", para("You can not copy a crate."), "", "`You can not copy a crate.` -> no L304")
    lint_attack("L11", "Unit outside the list: `A crate weighs 9000 kg and takes 9000 TPS.`", para("A crate weighs 9000 kg and takes 9000 TPS."),
                "The real SPEC list has no `bytes`, `TPS`, `RCU`, `WCU`, `AZs`, `Tbps`, `EB`, `volumes`, `snapshots`, `nodes`, `records`, `times`, `x`.",
                "`A crate takes 9000 TPS.` -> no L304")
    lint_attack("L12", "Plus sign after the number: `A crate holds 9000+ widgets.`", para("A crate holds 9000+ widgets."), "", "`9000+ widgets` -> no L304")
    lint_attack("L13", "The claim in inline code: ``A crate holds `up to 9000 widgets`.``", para("A crate holds `up to 9000 widgets`."),
                "Inline code is removed before the rules run (it is meant for commands), but it renders as readable text.",
                "``A crate holds `up to 9000 widgets`.`` -> no L304")
    lint_attack("L14", "The claim as a question: `Did you know that a crate always holds up to 9000 widgets?`",
                para("Did you know that a crate always holds up to 9000 widgets?"),
                "Sentences that end with `?` are never read by L304 (R2).", "`Did you know that a crate always holds up to 9000 widgets?` -> no L304")
    lint_attack("L15", "A `no-fact` marker on a factual sentence: `A crate must hold at most 9000 widgets. <!-- no-fact: requirement -->`",
                para("A crate must hold at most 9000 widgets. <!-- no-fact: requirement -->"),
                "Passes with warning W308 by design; the gate result is exit 2 (pass). Only the claims reviewer can stop it.",
                "any hard sentence + `<!-- no-fact: requirement -->` -> W308 only")
    lint_attack("L16", "Absolute claim split over two sentences: `A crate stays public. Always.`", para("A crate stays public. Always."), expect_block=True)
    lint_attack("L17", "Number and unit split over two sentences: `The limit of a crate is 9000. The unit is widgets.`",
                para("The limit of a crate is 9000. The unit is widgets."), "A bare number without a unit is never a finding.",
                "`The limit of a crate is 9000. The unit is widgets.` -> no L304")
    lint_attack("L18", "Link text that hides the number in words: `A shelf holds [five hundred widgets](...#widget-shelf-max-widgets).`",
                para(f"A shelf holds [five hundred widgets]({LINK})."), expect_block=True)
    lint_attack("L19", "Link text with the display inside a larger number written with a space: `[up to 2 500 widgets](...)`",
                para(f"A shelf holds [up to 2 500 widgets]({LINK})."),
                "holds_display guards digits, commas and periods before the display, not a space-separated thousands group.",
                "`[up to 2 500 widgets](../facts/widget.md#widget-shelf-max-widgets)` -> no L303")
    lint_attack("L20", "Link text that holds the display and contradicts it: `[not 500 widgets but 9000 widgets](...)`",
                para(f"A shelf holds [not 500 widgets but 9000 widgets]({LINK})."),
                "L303 is a substring test, and the link then satisfies L304 for the whole sentence.",
                "`A shelf holds [not 500 widgets but 9000 widgets](../facts/widget.md#widget-shelf-max-widgets).` -> clean")
    lint_attack("L21", "Negated display: `A new shelf is [not private](...#widget-shelf-default-private) and can be read by all users.`",
                para("A new shelf is [not private](../facts/widget.md#widget-shelf-default-private) and can be read by all users."),
                "", "`[not private](../facts/widget.md#widget-shelf-default-private)` -> clean")
    lint_attack("L22", "Piggyback: an ungrounded hard claim in a sentence that has a fact link to another fact: `A crate always holds 9000 widgets, more than the "
                "[500 widgets](...) of a shelf.`", para(f"A crate always holds 9000 widgets, more than the [500 widgets]({LINK}) of a shelf."),
                "One fact link satisfies L304 for its sentence (R2). Left to the claims reviewer by design.",
                "`A crate always holds 9000 widgets, more than the [500 widgets](LINK) of a shelf.` -> clean")
    lint_attack("L23", "A real fact link on the wrong subject: `A crate holds [up to 500 widgets](...#widget-shelf-max-widgets).` (the fact is about shelves)",
                para(f"A crate holds [up to 500 widgets]({LINK})."), "No mechanical check of the subject; left to the claims reviewer.",
                "`A crate holds [up to 500 widgets](../facts/widget.md#widget-shelf-max-widgets).` -> clean")
    lint_attack("L24", "Exempt role: the flag of How it works changed from role=how to role=example, plus the control sentence.",
                lambda: (sandbox.replace_text(SB / DEEP, "<!-- section: role=how; route=full; minutes=6 -->", "<!-- section: role=example; route=full; minutes=6 -->"),
                         para("Each crate always holds 9000 widgets.")()), expect_block=True)
    lint_attack("L25", "Hard claim placed in the section whose role is example (Decision record): `**Decision.** ... A crate always holds up to 9000 widgets, "
                "and a shelf can never be private.`",
                lambda: sandbox.replace_text(SB / DEEP, "**Decision.** Create a second shelf in Frankfurt.",
                                             "**Decision.** Create a second shelf in Frankfurt. A crate always holds up to 9000 widgets, and a shelf can never be private."),
                "Sections with grounding `example` are not checked at all. W903 (story numbers) did not fire either: the fixture has no data/startup.json entry.",
                "add `A crate always holds up to 9000 widgets.` to a bold field of the Decision record -> clean")
    lint_attack("L26", "Hard claim in a `Startup example` callout inside the strict section: `> **Startup example:** Callvale learned that a crate always holds "
                "up to 9000 widgets.`", para("> **Startup example:** Callvale learned that a crate always holds up to 9000 widgets."),
                "Callouts with grounding `example` are exempt (R2 exemption 3).",
                "`> **Startup example:** Callvale learned that a crate always holds up to 9000 widgets.` -> no L304")
    lint_attack("L27", "Hard claim in an HTML comment: `<!-- A crate always holds 9000 widgets. -->`", para("<!-- A crate always holds 9000 widgets. -->"),
                "Passes, and is harmless for a Markdown reader (a comment is not rendered). Not counted as a hole.")
    lint_attack("L28", "Hard claim inside the collapsed Go deeper block (details).",
                lambda: sandbox.replace_text(SB / DEEP, "You can ask AWS to raise this quota.", "You can ask AWS to raise this quota. A crate always holds 9000 widgets."),
                expect_block=True)
    lint_attack("L29", "Hard claim in the summary line of a details block: `<summary>Go deeper: a crate always holds 9000 widgets</summary>`",
                lambda: sandbox.replace_text(SB / DEEP, "<summary>Go deeper: the shelf quota</summary>", "<summary>Go deeper: a crate always holds 9000 widgets</summary>"),
                "The summary line is visible text, even when the block is closed.", "`<summary>Go deeper: a crate always holds 9000 widgets</summary>` -> clean")
    lint_attack("L30", "AWS quote block cut so that the negation is gone: `> \"move a shelf to another Region.\"` under the real attribution line.",
                lambda: sandbox.replace_text(SB / DEEP, '> "You cannot move a shelf to another Region."', '> "move a shelf to another Region."'),
                "L306 accepts any substring of an evidence quote, also one that starts in the middle of a sentence.",
                "replace the FAQ quote by `> \"move a shelf to another Region.\"` -> no L306")
    lint_attack("L31", "Full-width digits: `A crate holds ９０００ widgets.`", para("A crate holds ９０００ widgets."),
                "", "`A crate holds <full-width 9000> widgets.` -> no L304")

    def extra():
        (SB / "99-sample" / "6-extra.md").write_text("# Extra notes\n\nA crate always holds up to 9000 widgets. A shelf is never private.\n", encoding="utf-8")
    lint_attack("L32", "A hand-written file that the template does not list: `99-sample/6-extra.md` with two false hard claims.", extra,
                "lint reads only the files of the resolved template. An extra .md in a chapter folder is reader-facing and unchecked.",
                "create 99-sample/6-extra.md with any text -> lint 99 unchanged")


# ------------------------------------------------------------------ sync

def sync_attacks():
    def fresh():
        reset()
        saa("sync", "99")
        saa("sync", "--all")

    fresh()
    base = saa("sync", "99", "--check")
    quiz = SB / "99-sample" / "5-quiz.md"
    text = quiz.read_text(encoding="utf-8")
    quiz.write_text(text.replace("500 widgets", "900 widgets", 1), encoding="utf-8")
    r = saa("sync", "99", "--check")
    record("S01", "sync --check", "Generated `5-quiz.md` edited by hand (first `500 widgets` changed to `900 widgets`).",
           ["baseline sync 99 --check -> " + short(*base), "after the edit -> " + short(*r)], r[0] == 0 and "500 widgets" in text, "control")

    fresh()
    sheet = SB / "facts" / "widget.md"
    exists = sheet.exists()
    text = sheet.read_text(encoding="utf-8") if exists else ""
    sheet.write_text(text.replace("Each shelf can hold up to 500 widgets.", "Each shelf can hold up to 900 widgets.").replace("`500 widgets`", "`900 widgets`"), encoding="utf-8")
    r1 = saa("sync", "99", "--check")
    r2 = saa("gate", "99", "--gate", "sync")
    r3 = saa("sync", "--all", "--check")
    r4 = saa("sync", "99", "--only", "facts", "--check")
    record("S02", "sync --check, sync gate", "Generated fact sheet `facts/widget.md` edited by hand: the AWS quote and the value changed from 500 to 900.",
           [f"sheet existed after sync --all: {exists}", "sync 99 --check -> " + short(*r1), "gate 99 --gate sync -> " + short(*r2),
            "sync --all --check -> " + short(*r3), "sync 99 --only facts --check -> " + short(*r4)],
           r1[0] == 0 and r2[0] in (0, 2),
           "The chapter form of `sync --check`, which is what the `sync` gate of `edit`, `fix` and `finalize` runs, does not build the fact sheets. "
           "Only `sync --all --check` or `--only facts` compares them.",
           "sync --all; edit facts/widget.md by hand; sync 99 --check -> ok; gate 99 --gate sync -> ok")

    fresh()
    sheet.unlink()
    r1 = saa("sync", "99", "--check")
    r2 = saa("lint", "99")
    l601 = [f for f in ((r2[1] or {}).get("errors") or []) if f.get("code") == "L601" and "facts/" in f.get("msg", "")]
    record("S03", "sync --check, lint", "Generated fact sheet `facts/widget.md` deleted (every fact link of the chapter points at it).",
           ["sync 99 --check -> " + short(*r1), f"lint 99 -> exit {r2[0]}, L601 findings that name facts/: {len(l601)}"], r1[0] == 0 and not l601,
           "Neither the sync gate nor the lint notices that the target of every fact link is missing.",
           "delete facts/widget.md; sync 99 --check -> ok; lint 99 has no finding for the fact links")

    fresh()
    (SB / "facts" / "ghost.md").write_text("<!-- generated by saa.py; do not edit -->\n# Ghost: facts\n\n### ghost-limit\n\n**Claim.** A ghost holds up to 9000 widgets.\n\n"
                                           "> \"Each ghost can hold up to 9000 widgets.\"\n> — [Ghost limits](https://docs.aws.amazon.com/ghost/limits.html)\n", encoding="utf-8")
    r1 = saa("sync", "--all", "--check")
    record("S04", "sync --all --check", "An orphan `facts/ghost.md` written by hand in the form of a generated fact sheet, for a service with no fact.",
           ["sync --all --check -> " + short(*r1)], r1[0] == 0,
           "sync compares only the files it would write; a file it would not write is never reported.",
           "write facts/ghost.md by hand; sync --all --check -> ok")

    fresh()
    quiz.write_text(quiz.read_text(encoding="utf-8") + "\nA crate always holds up to 9000 widgets.\n", encoding="utf-8")
    r = saa("sync", "99", "--check")
    record("S05", "sync --check", "One false sentence appended after the last line of generated `5-quiz.md`.", ["sync 99 --check -> " + short(*r)], r[0] == 0, "control")


HARMLESS = {"L27"}
HOLES = [
    ("H1", "critical", "A fact that is not `hard` is verified with zero votes, and M11 decides `hard` with nine words and a number-with-unit test",
     ["F03", "F11", "F17", "F20"],
     "Any false claim that avoids the nine absolute words and a number directly followed by a unit can be stored with `hard: false` and any real "
     "quote of 8 words. `facts finalize` verifies it at once. Smallest reproduction: F11."),
    ("H2", "critical", "M5 and M11 lose the unit or the size of a number", ["F06", "F07", "F08", "F09", "F10"],
     "An adjective or a second space between number and unit, a magnitude word (`50 thousand`), a suffix (`50K`), or a number in words. "
     "The claim then carries another value than the quote and still needs no vote. Smallest reproduction: F08."),
    ("H3", "high", "A quote may start and end in the middle of a sentence", ["F03", "F17", "L30"],
     "Cutting `You cannot` off the front of a real sentence gives a `verbatim` quote with the opposite meaning, for M3/M4 and for the L306 quote block. "
     "Smallest reproduction: L30 (one line of Markdown) or F03."),
    ("H4", "high", "Text inside `<...>` is invisible to the quote match", ["F18"],
     "Up to 400 characters can be added to a stored quote. The fact sheet and the verifier packet then show words that AWS never wrote. Reproduction: F18."),
    ("H5", "critical", "Nothing proves that a snapshot came from the fetch tool", ["F19", "F22"],
     "A .txt written or edited by hand under `_build/corpus/snap/` is accepted as evidence by `facts add`; an honest verifier then sees a matching quote. "
     "Smallest reproduction: F22."),
    ("H6", "medium", "Page furniture and flattened table text pass M8 and M4", ["F16", "F20"],
     "Navigation words outside the ten BOILERPLATE phrases are a valid quote (F20). Table text written without pipes needs no `table_header` and can pair "
     "a number with the wrong row (F16; this one still waits for an entail vote)."),
    ("H7", "critical", "A voter is a free-text label", ["F13", "F14", "F15"],
     "The author votes on the own fact under a second label, or under the same label in another case. A later `support` under a disputing verifier's label "
     "turns a disputed fact into a verified one. Smallest reproduction: F14."),
    ("H8", "high", "Votes are bound to the rev number, not to the content; the vote log is a plain file", ["F24", "F25"],
     "A hand edit of `claim` that keeps `rev` keeps all votes (F25). A hand edit of the status plus one appended vote line passes F04 (F24). Smallest reproduction: F25."),
    ("H9", "critical", "`facts amend` can remove the need for votes, and then rewrites the prose itself", ["A01", "A04"],
     "A patch with `hard: false` (and a kind that M11 does not force) empties the votes and makes them unnecessary in one step. With a changed display the tool "
     "replaces the link texts in the chapter. `facts amend` takes no `--by`. Smallest reproduction: A01."),
    ("H10", "high", "L304 misses a number with a unit", ["L02", "L03", "L04", "L06", "L11", "L12", "L17", "L31"],
     "Non-breaking space, `&nbsp;`, full-width digits, a number word, an adjective between number and noun, a unit outside the list, `9000+`, or number and unit "
     "in two sentences. Smallest reproduction: L04 (`A crate holds 9000 small widgets.`)."),
    ("H11", "high", "L304 misses an absolute claim", ["L07", "L08", "L09", "L10"],
     "Words outside the nine-word list (`no one`, `nobody`, `invariably`, `every`, `all`), `can not` in two words, an entity or a zero-width space inside the word. "
     "Smallest reproduction: L10 (`You can not copy a crate.`)."),
    ("H12", "high", "Places that L304 does not read but the reader does", ["L13", "L14", "L15", "L25", "L26", "L29", "L32"],
     "Inline code, a sentence that ends with `?`, a `<summary>` line, any section or callout with grounding `example`, a sentence with a `no-fact` marker "
     "(warning W308 only), and a Markdown file that the template does not list. Smallest reproduction: L14."),
    ("H13", "high", "A fact link proves only that the display string is somewhere in the link text", ["L19", "L20", "L21", "L22", "L23"],
     "`[not 500 widgets but 9000 widgets](...)`, `[not private](...)`, `[up to 2 500 widgets](...)`, a link on the wrong subject, and any other hard claim "
     "in a sentence that has one link. Smallest reproduction: L21."),
    ("H14", "medium", "The chapter form of `sync --check` (the `sync` gate) does not look at the fact sheets", ["S02", "S03", "S04"],
     "`facts/<service>.md` can be edited or deleted, and a hand-made sheet for a service without facts can be added. Smallest reproduction: S02."),
]


def render():
    data = common.read_json(OUT, {}) or {}
    rows = data.get("attempts", [])
    by = {r["id"]: r for r in rows}
    through = [r for r in rows if r["through"]]
    bad = [r for r in through if r["id"] not in HARMLESS]
    n = lambda prefix: sum(1 for r in rows if r["id"].startswith(prefix))
    out = ["# Gate break report: grounding gates", "",
           "Date: 2026-10-04. Tool contract: `TOOLS.md` version 0.9. The tool was not changed.", "",
           "All attempts ran in the sandbox `aws-saa-book/_build/tmp/breaker-grounding/` (a fresh copy of `tools/tests/fixtures/book/` before each attempt), "
           "with `--book-dir`. No real data was touched. Driver: `python3 aws-saa-book/tools/helpers/break_grounding.py` "
           "(raw results: `_build/reports/gate-break-grounding.json`).", "",
           "## Summary", "",
           f"- Attempts: {len(rows)} (facts add, verify, vote, finalize: {n('F')}; amend: {n('A')}; lint: {n('L')}; sync: {n('S')}).",
           f"- Stopped by a gate: {len(rows) - len(through)}.",
           f"- Passed: {len(through)}; {len(bad)} of them are bad inputs (one, L27, is harmless).",
           f"- The {len(bad)} passing inputs come from {len(HOLES)} root holes, listed at the end.",
           "- What held: a changed or invented quote (M3), a quote stitched from sentences that are not adjacent (M3), another number (M5), another unit "
           "directly after the number (M5), a stored fact after its snapshot changed (M2), a status set by hand without a vote line (F04), a patch that names "
           "`status`, `votes` or `rev`, an amend to a number that no quote has, a link text with the number in words (L303), a changed section role (L105), "
           "a hard claim in a reveal block, an absolute word alone in its sentence, a hand edit of a generated chapter file (`sync --check`).",
           "- The default-against-maximum fact (F12) passes every mechanical check and is stopped only by the entail voter. With H7 the author is that voter.",
           "", "## Attempts", "",
           "`Passed: yes` means the bad input got through the gate named in the entry.", ""]
    for r in rows:
        out.append(f"### {r['id']}: {r['gate']}")
        out.append("")
        out.append(f"- Did: {r['did']}")
        for a in r["answers"]:
            out.append(f"- Answer: {a}")
        out.append(f"- Passed: {'YES' if r['through'] else 'no'}" + (" (harmless)" if r["id"] in HARMLESS else ""))
        if r.get("note"):
            out.append(f"- Note: {r['note']}")
        out.append("")
    out += ["## HOLES", "", "Each hole lists the attempts that show it. The reproduction of an attempt is one or two plain commands in a sandbox.", ""]
    for hid, sev, title, ids, text in HOLES:
        out.append(f"### {hid} ({sev}): {title}")
        out.append("")
        out.append(f"Attempts: {', '.join(ids)}. {text}")
        out.append("")
        for i in ids:
            if by.get(i, {}).get("repro"):
                out.append(f"- {i}: {by[i]['repro']}")
        out.append("")
    out += ["## Notes for the owners", "",
            "- `common.normalize_text` is the source of H4 (it drops `<...>`) and of the flattened table text in H6. A change there is a change in `common.py`.",
            "- H1, H2 and H9 share one cause: the tool lets the author decide `hard`, and checks that choice with the same narrow matcher that H10 and H11 defeat.",
            "- H7 and H8 cannot be closed by the tool alone while every agent can write every file. They can be narrowed: compare labels case-insensitively, "
            "refuse a second vote of a voter on the same rev and lens, store a content hash (claim, values, evidence) in each vote and compare it in `_decide`.",
            "- The fixture facts have no `author` field, so the author test never applies to them.",
            "- During setup I changed two strings of my own driver script with a `python3 -c` one-liner instead of the Edit tool. Nothing else was edited that way."]
    path = common.REAL_BOOK / "_build" / "reports" / "gate-break-grounding.md"
    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    listed = {i for h in HOLES for i in h[3]}
    print(f"wrote {common.rel(path)}: attempts={len(rows)} passed={len(through)} bad={len(bad)} holes={len(HOLES)} "
          f"unlisted={sorted(r['id'] for r in bad if r['id'] not in listed)} listed_not_passed={sorted(i for i in listed if not by.get(i, {}).get('through'))}")


def main():
    if sys.argv[1:] == ["report"]:
        render()
        return
    only = sys.argv[1:] or ["facts", "amend", "lint", "sync"]
    if "facts" in only:
        facts_attacks()
    if "amend" in only:
        amend_attacks()
    if "lint" in only:
        lint_attacks()
    if "sync" in only:
        sync_attacks()
    old = {r["id"]: r for r in (common.read_json(OUT, {}) or {}).get("attempts", [])} if len(only) < 4 else {}
    for r in RESULTS:
        old[r["id"]] = r
    rows = sorted(old.values(), key=lambda r: r["id"])
    common.write_json(OUT, {"attempts": rows, "through": [r["id"] for r in rows if r["through"]]})
    print(f"attempts={len(rows)} through={sum(1 for r in rows if r['through'])} -> {common.rel(OUT)}")


if __name__ == "__main__":
    main()
