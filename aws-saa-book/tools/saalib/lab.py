"""Hands-on tasks (Look, Try, Lab): `saa.py tasks add|lint|set-status|check-cli|emulate`.

Contract: _build/style/TOOLS-items.md section 8 and TOOLS-rules.md R5, R6. Limits come from
SPEC.json `tasks.*` at call time. Standard library only; the two helpers under tools/helpers/
(cli_model.py, emulate.py) carry their own inline dependencies and run through `uv run --script`.

Other modules (lint, facts, ledger, corpus) are imported inside functions and guarded: when one
is missing, a small local fallback of the same documented behaviour is used.
"""
from __future__ import annotations

import copy
import hashlib
import json
import os
import re
import shlex
import subprocess

from saalib import common

TASKS_FILE = "tasks.json"
DEAD = ("rejected", "retired")
UNDO = {"create": ["delete"], "copy": ["delete"], "run": ["terminate", "stop", "delete"],
        "allocate": ["release"], "launch": ["terminate", "delete"],
        # gate-break 44: more verbs that make a resource
        "import": ["delete"], "register": ["deregister", "delete"], "restore": ["delete"], "request": ["delete", "cancel"],
        "provision": ["deprovision", "delete", "terminate"], "purchase": ["delete", "cancel"], "put": ["delete", "remove"],
        "mb": ["rb", "delete"]}
CREATE_EXTRA = ("import", "register", "restore", "request", "provision", "purchase")
# An AWS CLI operation that starts with one of these words changes nothing (gate-break 53). Everything else changes
# something: a Look holds none of those, and a Try or a Lab that holds one has a cleanup command that deletes.
READ_VERBS = frozenset("describe list get head lookup search scan query select batch-get view show check simulate estimate "
                       "preview validate wait filter tail ls help decode detect test verify presign".split())
DELETE_VERBS = frozenset("delete terminate remove deregister release rb rm cancel schedule deprovision purge".split())
SHELL_OPERATORS = (";", "&&", "||", "|")
WORLD = ("0.0.0.0/0", "::/0")
ADMIN_PORTS = (22, 3389)
# gate-break 47: every command that writes a firewall rule, and every way to write `the whole internet`
RULE_OPERATIONS = ("authorize-security-group-ingress", "modify-security-group-rules", "create-network-acl-entry",
                   "replace-network-acl-entry", "authorize-db-security-group-ingress", "authorize-cache-security-group-ingress",
                   "authorize-cluster-security-group-ingress")
CIDR4 = re.compile(r"(?<![\d.])(\d{1,3}(?:\.\d{1,3}){3})/(\d{1,2})(?!\d)")
CIDR6 = re.compile(r"(?<![0-9A-Fa-f:.])((?:[0-9A-Fa-f]{0,4}:){2,7}[0-9A-Fa-f]{0,4})/(\d{1,3})(?!\d)")
CURL_OPTIONS = frozenset("-s -S -L -I -i -f -v -sS -sL -sI -sf -fsS -fsSL --silent --show-error --location --head --include --fail "
                         "--verbose --max-time --connect-timeout -m --compressed --http1.1 --http2 --tlsv1.2 --tlsv1.3".split())
CURL_VALUE_OPTIONS = frozenset(("--max-time", "--connect-timeout", "-m"))
HIDDEN_INPUT_OPTIONS = ("--ip-permissions", "--security-group-rules", "--policy", "--policy-document", "--launch-permission",
                        "--public-access-block-configuration", "--access-control-policy", "--attributes", "--assume-role-policy-document",
                        "--create-volume-permission", "--resource-policy")
MONEY = re.compile(r"(?:\$|USD\s?|US\$\s?)\s?(\d[\d,]*(?:\.\d+)?)(?:\s?USD)?|(\d[\d,]*(?:\.\d+)?)\s?(USD|dollars?|cents?|ct)(?![A-Za-z])", re.I)
MONEY_WORD = re.compile(r"(?<![A-Za-z])(?:USD|dollars?|cents?|bucks?)(?![A-Za-z])", re.I)
# Secure-by-default patterns that hold whatever SPEC.json lists (RULINGS hard rule 9). They only add to
# tasks.banned_command_patterns; they never replace it.
EXTRA_BANNED = [
    (r"(?i)(BlockPublicAcls|IgnorePublicAcls|BlockPublicPolicy|RestrictPublicBuckets)\"?\s*[=:]\s*false", "turns a public access block setting off"),
    (r"delete-public-access-block", "removes the public access block"),
    (r"--acl\s+(public-read|public-read-write|authenticated-read)\b", "sets a public ACL"),
    (r"(?i)acs\.amazonaws\.com/groups/global/(AllUsers|AuthenticatedUsers)", "grants access to everyone"),
    (r"(?i)aws_secret_access_key|\bAKIA[0-9A-Z]{16}\b", "holds an access key"),
    (r"create-service-specific-credential", "creates a long-term credential"),
]
FACT_LINK = re.compile(r"\[([^\]]+)\]\((?:\.\./)*facts/([a-z0-9-]+)\.md#([a-z0-9-]+)\)")
DOLLAR = re.compile(r"\$\s?(\d[\d,]*(?:\.\d+)?)")
NAME_OPTION = re.compile(r"^--(?:[a-z0-9-]+-)?name$|^--bucket$")


class HelperError(Exception):
    """uv, the package index or a helper script could not run (transient, exit 5)."""


# ---------------------------------------------------------------- small helpers

def _finding(code, item, msg, file=None, line=None) -> dict:
    return {"code": code, "file": file, "line": line, "item": item, "msg": msg}


def _spec() -> dict:
    spec = common.read_json(common.STYLE_DIR / "SPEC.json")
    if spec is None:
        raise SystemExit(common.fail("no SPEC.json in " + common.rel(common.STYLE_DIR), common.EXIT_PRECONDITION))
    return spec


def _rel(path) -> str:
    try:
        return str(path.resolve().relative_to(common.BOOK.resolve()))
    except ValueError:
        return str(path)


def _tasks_path(ch: dict):
    return common.chapter_data_dir(ch["id"]) / TASKS_FILE


def _load_doc(ch: dict):
    return common.read_json(_tasks_path(ch))


def _live(doc) -> list:
    return [t for t in (doc or {}).get("items", []) if isinstance(t, dict) and t.get("status") not in DEAD]


def _lint_mod():
    try:
        from saalib import lint
        return lint
    except Exception:
        return None


def _words(command: str) -> list:
    try:
        return shlex.split(command)
    except ValueError:
        return command.split()


def _operation(command: str):
    """The operation of an `aws <service> <operation>` command: its third word. None for curl and dig."""
    words = _words(command or "")
    if len(words) >= 3 and words[0] == "aws":
        return words[2]
    return None


def commands_of(task: dict) -> list:
    """Every command of a task as (where, command, text): steps, cleanup, verify."""
    out = []
    for i, step in enumerate(task.get("steps") or []):
        if isinstance(step, dict) and step.get("command"):
            out.append((f"steps[{i}]", step["command"], step.get("text") or ""))
    for i, step in enumerate(task.get("cleanup") or []):
        if isinstance(step, dict) and step.get("command"):
            out.append((f"cleanup[{i}]", step["command"], step.get("text") or ""))
    verify = task.get("verify")
    if isinstance(verify, dict) and verify.get("command"):
        out.append(("verify", verify["command"], verify.get("expect") or ""))
    return out


def chapter_commands(doc) -> list:
    return [cmd for task in _live(doc) for _, cmd, _ in commands_of(task)]


def commands_sha256(doc) -> str:
    return hashlib.sha256("\n".join(chapter_commands(doc)).encode("utf-8")).hexdigest()


def _range_ok(value, rng) -> bool:
    if rng is None or rng == {}:
        return True
    if isinstance(rng, dict):
        return rng.get("min", 0) <= value <= rng.get("max", 10 ** 9)
    return value == rng


def _range_text(rng) -> str:
    return f"{rng.get('min', 0)} to {rng.get('max', 'any')}" if isinstance(rng, dict) else str(rng)


def _word_count(text: str) -> int:
    lint = _lint_mod()
    if lint is not None and hasattr(lint, "word_count"):
        try:
            return int(lint.word_count(text))
        except Exception:
            pass
    plain = re.sub(r"\]\([^)]*\)", "]", text or "")
    return len([t for t in plain.split() if re.search(r"[A-Za-z0-9]", t)])


def _merge(base, over):
    if isinstance(base, dict) and isinstance(over, dict):
        out = dict(base)
        for key, value in over.items():
            out[key] = _merge(base[key], value) if key in base else copy.deepcopy(value)
        return out
    return copy.deepcopy(over)


def _template(ch: dict, spec: dict) -> dict:
    lint = _lint_mod()
    if lint is not None and hasattr(lint, "template"):
        try:
            return lint.template(ch["id"])
        except Exception:
            pass
    templates = spec.get("templates", {})
    key = ch.get("kind") if ch.get("kind") in templates else ch.get("tier")
    override = (spec.get("chapter_overrides") or {}).get(ch["id"]) or {}
    if isinstance(override, dict) and override.get("template"):
        key = override["template"]
    merged = _merge(templates.get(key, {}), {k: v for k, v in override.items() if k != "template"}
                    if isinstance(override, dict) else {})
    merged["key"] = key
    return merged


def _heading_id(heading: str) -> str:
    text = re.sub(r"\s*\(\d+\s*min\)\s*$", "", heading.strip())
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"\s", "-", text.strip())


# ---------------------------------------------------------------- context of one lint run

class _Ctx:
    """Everything a rule needs, loaded once per run. `inputs` collects the book files that were read."""

    def __init__(self, ch: dict, quick: bool = False):
        self.ch = ch
        self.quick = quick
        self.spec = _spec()
        self.t = self.spec.get("tasks", {})
        self.inputs = set()
        self.inputs.add(common.STYLE_DIR / "SPEC.json")
        self._facts = None
        self._traps = None
        self._sections = {}
        self._corpus_urls = None
        self.file = _rel(_tasks_path(ch))

    # facts
    def facts(self) -> dict:
        if self._facts is None:
            try:
                from saalib import facts as facts_mod
                self._facts = dict(facts_mod.load())
            except Exception:
                self._facts = {}
                if common.FACTS_DIR.is_dir():
                    for path in sorted(common.FACTS_DIR.glob("*.jsonl")):
                        for row in common.read_jsonl(path):
                            self._facts[row.get("id")] = row
        return self._facts

    def fact(self, fact_id):
        fact = self.facts().get(fact_id)
        if fact is not None and fact.get("service"):
            self.inputs.add(common.FACTS_DIR / f"{fact['service']}.jsonl")
        return fact

    # traps
    def traps(self) -> dict:
        if self._traps is None:
            lint = _lint_mod()
            found = None
            if lint is not None and hasattr(lint, "traps"):
                try:
                    found = dict(lint.traps())
                except Exception:
                    found = None
            if found is None:
                found = {}
                for entry in common.chapters():
                    folder = common.BOOK / f"{entry['id']}-{entry['slug']}"
                    if folder.is_dir():
                        for path in sorted(folder.glob("*.md")):
                            for trap in re.findall(r"<!--\s*trap:\s*([a-z0-9-]+)\s*-->", path.read_text(encoding="utf-8")):
                                found.setdefault(trap, entry["id"])
                    brief = common.read_json(common.BUILD / "work" / f"{entry['id']}-{entry['slug']}" / "brief.json") or {}
                    for trap in brief.get("traps", []) if isinstance(brief, dict) else []:
                        if isinstance(trap, dict) and trap.get("id"):
                            found.setdefault(trap["id"], entry["id"])
            self._traps = found
        return self._traps

    # sections
    def sections(self, entry: dict) -> dict:
        key = entry["id"]
        if key not in self._sections:
            folder = common.BOOK / f"{entry['id']}-{entry['slug']}"
            brief_path = common.BUILD / "work" / f"{entry['id']}-{entry['slug']}" / "brief.json"
            if folder.is_dir():
                self.inputs.update(p for p in folder.glob("*.md"))
            if brief_path.exists():
                self.inputs.add(brief_path)
            lint = _lint_mod()
            found = None
            if lint is not None and hasattr(lint, "sections"):
                try:
                    found = {f: set(s) for f, s in lint.sections(entry["id"]).items()}
                except Exception:
                    found = None
            if found is None:
                found = {}
                if folder.is_dir():
                    for path in sorted(folder.glob("*.md")):
                        ids, fenced = set(), False
                        for line in path.read_text(encoding="utf-8").splitlines():
                            if line.startswith("```"):
                                fenced = not fenced
                            elif not fenced and re.match(r"#{2,3} ", line):
                                ids.add(_heading_id(line.lstrip("#")))
                        found[path.name] = ids
                brief = common.read_json(brief_path) or {}
                for sec in brief.get("sections", []) if isinstance(brief, dict) else []:
                    if isinstance(sec, dict) and sec.get("file") and sec.get("section"):
                        found.setdefault(sec["file"], set()).add(sec["section"])
            self._sections[key] = found
        return self._sections[key]

    def section_ok(self, ref) -> bool:
        match = re.match(r"^(?:(\d{2}-[a-z0-9-]+)/)?([a-z0-9-]+\.md)#([a-z0-9-]+)$", ref or "")
        if not match:
            return False
        entry = self.ch
        if match.group(1):
            entry = next((c for c in common.chapters() if f"{c['id']}-{c['slug']}" == match.group(1)), None)
            if entry is None:
                return False
        return match.group(3) in self.sections(entry).get(match.group(2), set())

    # corpus
    def url_known(self, url: str) -> bool:
        if any(ev.get("url") == url for fact in self.facts().values() if fact.get("status") == "verified"
               for ev in fact.get("evidence", [])):
            return True
        if self.quick:
            return True
        try:
            from saalib import corpus
            if corpus.load_meta(corpus.source_id_for(url)) is not None:
                return True
        except Exception:
            pass
        if self._corpus_urls is None:
            self._corpus_urls = set()
            snap = common.CORPUS / "snap"
            if snap.is_dir():
                for meta_path in snap.rglob("*.meta.json"):
                    try:
                        self._corpus_urls.add((common.read_json(meta_path) or {}).get("url"))
                    except ValueError:
                        continue
        return url in self._corpus_urls


# ---------------------------------------------------------------- text rules

def _banned_words(ctx: _Ctx, text: str) -> list:
    lint_spec = ctx.spec.get("lint", {})
    banned = lint_spec.get("banned_words") or {}
    plain = re.sub(r"\]\([^)]*\)", "]", text or "")
    for exception in lint_spec.get("banned_word_exceptions") or []:
        plain = re.sub(re.escape(exception), " ", plain, flags=re.I)
    hits = []
    for phrase in banned:
        flags = 0 if phrase == "may" else re.I
        if re.search(r"(?<![A-Za-z0-9-])" + re.escape(phrase) + r"(?![A-Za-z0-9-])", plain, flags):
            hits.append(phrase)
    return hits


def _strict_text(ctx: _Ctx, text: str, where: str) -> list:
    """Messages for a strict text field. Uses lint.check_strict_text when the lint module is there."""
    lint = _lint_mod()
    if lint is not None and hasattr(lint, "check_strict_text"):
        try:
            return [f"{f.get('code', 'L304')} {f.get('msg', '')}".strip() for f in lint.check_strict_text(text, where)]
        except Exception:
            pass
    messages = []
    for label, service, fact_id in FACT_LINK.findall(text):
        fact = ctx.fact(fact_id)
        if fact is None or fact.get("service") != service:
            messages.append(f"L301 the link to {fact_id} does not resolve")
        elif fact.get("status") != "verified":
            messages.append(f"L302 the linked fact {fact_id} is not verified")
        else:
            shown = common.normalize_text(label)
            displays = [common.normalize_text(v.get("display", "")) for v in fact.get("values", [])]
            holds = getattr(lint, "holds_display", None) or (lambda text, d: bool(d) and d in text)
            if not any(holds(shown, d) for d in displays):
                messages.append(f"L303 the link text holds no value of {fact_id}")
    absolute = ctx.spec.get("lint", {}).get("absolute_words")
    if isinstance(absolute, list):
        for sentence in re.split(r"(?<=[.!?])\s+", text):
            if sentence.rstrip().endswith("?") or FACT_LINK.search(sentence):
                continue
            for word in absolute:
                if isinstance(word, str) and re.search(r"(?<![A-Za-z0-9-])" + re.escape(word) + r"(?![A-Za-z0-9-])", sentence, re.I):
                    messages.append(f"L304 '{word}' in a sentence without a fact link")
                    break
    return messages


# ---------------------------------------------------------------- command rules

def _form_errors(ctx: _Ctx, command: str, text_pool: str) -> list:
    """T104: one plain CloudShell command."""
    t = ctx.t
    errors = []
    prefixes = t.get("allowed_command_prefixes") or ["aws "]
    if not any(command.startswith(p) for p in prefixes):
        errors.append("does not start with one of " + ", ".join(p.strip() for p in prefixes))
    if "\n" in command or "\r" in command:      # gate-break 50: a line break starts a second command
        return errors + ["more than one line; a step holds one command"]
    placeholder_rx = t.get("placeholder_regex", r"<[A-Z][A-Z0-9_]*>")
    try:
        # a placeholder such as <SG_ID> is a word, not a redirect
        lexer = shlex.shlex(re.sub(placeholder_rx, "PLACEHOLDER", command), posix=True, punctuation_chars=True)
        lexer.whitespace_split = True
        tokens = list(lexer)
    except ValueError as exc:
        return errors + [f"cannot be split ({exc})"]
    for token in tokens:
        if token and all(c in "();<>|&" for c in token):
            if any(c in ";|&" for c in token):
                errors.append(f"more than one command (shell operator {token})")
            else:           # gate-break 50: > file, < file, <( command )
                errors.append(f"a redirect or a subshell ({token}); a step holds one plain command")
            break
    unquoted = re.sub(r"'[^']*'", "''", command)
    if "`" in unquoted:
        errors.append("a backtick outside single quotes")
    if "$(" in unquoted:
        errors.append("a command substitution $(")
    odd = re.search(r"\$\{[^}]*\}?|\$[a-z_][A-Za-z0-9_]*", unquoted)
    if odd:                 # gate-break 50: ${VPC_ID} and $vpc_id are variables that no capture rule sees
        errors.append(f"the variable {odd.group(0)} is not written as $NAME in capitals (a captured value)")
    words = _words(command)
    if any(w == "--profile" or w.startswith("--profile=") for w in words):
        errors.append("--profile is not allowed (AWS CloudShell has the credentials)")
    for word in words:      # gate-break 47: input that the lint cannot read
        if re.match(r"--cli-input-(json|yaml)\b", word):
            errors.append(f"{word.split('=')[0]} is not allowed: the lint cannot read the input; write the options in the command")
    for j, word in enumerate(words):
        name, _, inline = word.partition("=")
        value = inline or (words[j + 1] if j + 1 < len(words) else "")
        if name in HIDDEN_INPUT_OPTIONS and re.match(r"fileb?://", value):
            errors.append(f"{name} reads a file ({value}): the lint cannot read the rules; write them in the command")
    if "sudo" in words:
        errors.append("sudo is not allowed")
    if words and words[0] == "curl":
        skip = False
        for word in words[1:]:
            if skip or "://" in word:
                skip = False
                continue
            short = re.fullmatch(r"-[A-Za-z]+", word)
            if (short and set(word[1:]) & set("XdTFoO")) or re.match(r"--(data|request|upload-file|output|remote-name|form)\b", word):
                errors.append(f"curl is read-only here: {word} is not allowed")
            elif word.split("=")[0] not in CURL_OPTIONS:    # gate-break 49: an allow-list, not a list of bad flags (--json)
                errors.append(f"curl is read-only here: {word} is not one of the allowed options")
            skip = word in CURL_VALUE_OPTIONS
        urls = [w for w in words[1:] if "://" in w]
        if not urls or any(not (u.startswith("https://") or u.startswith("http://169.254.169.254")) for u in urls):
            errors.append("curl needs an https:// URL (or the instance metadata address)")
    for placeholder in sorted(set(re.findall(t.get("placeholder_regex", r"<[A-Z][A-Z0-9_]*>"), command))):
        name = placeholder.strip("<>")
        if placeholder not in text_pool and not re.search(r"\b" + re.escape(name) + r"\b", text_pool):
            errors.append(f"the placeholder {placeholder} is not named in the step text")
    return errors


def _ports(command: str) -> list:
    """Port ranges named by an ingress command as (low, high); [] when none is named."""
    ranges = []
    for a, b in re.findall(r"--port[= ]+(\d+)(?:-(\d+))?", command):
        ranges.append((int(a), int(b or a)))
    lows = [int(x) for x in re.findall(r"FromPort\"?\s*[=:]\s*(-?\d+)", command)]
    highs = [int(x) for x in re.findall(r"ToPort\"?\s*[=:]\s*(-?\d+)", command)]
    for i, low in enumerate(lows):
        ranges.append((low, highs[i] if i < len(highs) else low))
    for a, b in re.findall(r"From=(\d+),\s*To=(\d+)", command):       # --port-range of a network ACL entry
        ranges.append((int(a), int(b)))
    return ranges


def _wide_ranges(command: str) -> list:
    """The address ranges of a command that are the whole internet or a large part of it (gate-break 47):
    an IPv4 range with a prefix shorter than /8, an IPv6 range with a prefix shorter than /16, in any spelling."""
    wide = [f"{a}/{n}" for a, n in CIDR4.findall(command) if int(n) < 8]
    wide += [f"{a}/{n}" for a, n in CIDR6.findall(command) if int(n) < 16]
    return wide


def _exposure(command: str) -> list:
    """T105: ways to open a resource to everyone that are not an S3 ACL (gate-break 48, 49)."""
    hits = []
    plain = command.replace("\\", "")
    op = _operation(command) or ""
    if re.search(r"\"Principal\"\s*:\s*(?:\{\s*\"(?:AWS|Service|Federated)\"\s*:\s*)?\[?\s*\"\*\"", plain) \
            and re.search(r"\"Effect\"\s*:\s*\"Allow\"", plain) and '"Condition"' not in plain:
        hits.append("a policy allows the principal * (everyone) without a condition")
    if re.search(r"(^|\s)--publicly-accessible\b", command):
        hits.append("makes a database publicly accessible")
    if re.search(r"modify-(db-)?(cluster-)?(snapshot|image)-attribute", op) and \
            re.search(r"(?i)(--group-names|--values-to-add|--user-groups)[= ]+\"?'?all\b|Group\"?\s*[=:]\s*\"?all\b", command):
        hits.append("shares a snapshot or an image with all AWS accounts")
    if op == "add-permission" and re.search(r"--principal[= ]+['\"]?\*", command):
        hits.append("gives everyone the permission (--principal *)")
    if re.search(r"(?i)--auth-type[= ]+['\"]?NONE\b", command):
        hits.append("creates a function URL without authentication (--auth-type NONE)")
    if re.search(r"aws\s+configure\s+(export-credentials|get\s+aws_(secret|session)|list-profiles)", command) \
            or re.search(r"\bsts\s+(get-session-token|get-federation-token)\b", command) \
            or re.search(r"(?i)169\.254\.169\.254\S*/(security-credentials|identity-credentials)|/latest/api/token", command):
        hits.append("prints credentials")
    return hits


def _banned(ctx: _Ctx, command: str) -> list:
    """T105: secure by default."""
    hits = []
    for pattern in ctx.t.get("banned_command_patterns") or []:
        try:
            if re.search(pattern, command):
                hits.append(f"matches the banned pattern {pattern}")
        except re.error:
            hits.append(f"SPEC.json holds an invalid banned pattern {pattern}")
    for pattern, why in EXTRA_BANNED:
        if re.search(pattern, command):
            hits.append(why)
    op = _operation(command) or ""
    if op in RULE_OPERATIONS and not re.search(r"(^|\s)--egress\b", command):
        wide = _wide_ranges(command)
        prefix_list = re.search(r"(?i)PrefixListId|--(source-)?prefix-list", command)
        if wide or prefix_list:
            ranges = _ports(command)
            all_ports = (not ranges or any(low < 0 for low, _ in ranges)
                         or re.search(r"(--protocol[= ]+|IpProtocol\"?\s*[=:]\s*\"?)(-1|all)\b", command))
            if all_ports or any(low <= p <= high for low, high in ranges for p in ADMIN_PORTS):
                if wide:
                    hits.append("opens SSH or RDP (port 22 or 3389) to the world (0.0.0.0/0 or ::/0)"
                                + ("" if any(w in WORLD for w in wide) else f": {', '.join(wide)} is the world or a large part of it"))
                else:
                    hits.append("opens SSH or RDP (port 22 or 3389) to a prefix list; the lint cannot see its ranges")
    hits += _exposure(command)
    return hits


def _option_values(command: str, *parts: str) -> str:
    """The values of every option whose name holds one of `parts` (`--tags`, `--tag-specifications`, `--filters`),
    joined by spaces. A tag pattern is searched here, not in the whole command."""
    words, out, take = _words(command or ""), [], False
    for word in words:
        if word.startswith("--"):
            name, _, inline = word.partition("=")
            take = any(part in name for part in parts)
            if take and inline:
                out.append(inline)
        elif take:
            out.append(word)
    return " ".join(out)


def _verb(command: str):
    """The verb of an aws command: the first word of its operation (`create` of create-bucket; `mb` of `aws s3 mb`)."""
    op = _operation(command or "")
    return op.split("-")[0] if op else None


def _read_only(command: str) -> bool:
    """True for curl, dig and an aws operation that changes nothing (READ_VERBS)."""
    op = _operation(command or "")
    if op is None:
        return True
    return op.split("-")[0] in READ_VERBS or any(op.startswith(v + "-") for v in READ_VERBS if "-" in v)


def _create_verb(ctx, command: str):
    """The creating verb of a command, or None: create_command_regex of SPEC.json, plus import, register, restore,
    request, provision, purchase, put and `aws s3 mb` (gate-break 44)."""
    op = _operation(command or "")
    if not op:
        return None
    words = _words(command)
    if words[1:3] == ["s3", "mb"]:
        return "mb"
    match = re.search(ctx.t.get("create_command_regex", r"^(create|copy|run|allocate|launch)-"), op)
    if match:
        return match.group(1) if match.groups() else op.split("-")[0]
    verb = op.split("-")[0]
    return verb if "-" in op and (verb in CREATE_EXTRA or verb == "put") else None


def _resource_names(step: dict) -> set:
    """What identifies the resource that a creating step makes: `$NAME` of its capture and the literal values of its
    name options (--name, --bucket, --*-name, --*-identifier). Empty when the step names nothing."""
    names = set()
    capture = step.get("capture") if isinstance(step.get("capture"), dict) else None
    if capture and capture.get("name"):
        names.add("$" + str(capture["name"]))
    words = _words(step.get("command") or "")
    for j, word in enumerate(words[:-1]):
        option, _, inline = word.partition("=")
        value = inline or words[j + 1]
        if (NAME_OPTION.match(option) or re.fullmatch(r"--[a-z0-9-]*-identifier", option)) and value and not value.startswith("-"):
            names.add(value)
    if words[1:3] == ["s3", "mb"] and len(words) > 3:
        names.add(words[3].replace("s3://", "").strip("/"))
    return names


def _has_prefix(name: str, prefix: str) -> bool:
    """The name rule of T106 for an untaggable create: the name starts with name_prefix (`saa-`), or the path `/saa/`."""
    return name.lstrip("/").startswith(prefix) or name.startswith("/saa/")


def _verify_by_name(ctx, task: dict, verify: dict) -> bool:
    """T108 exception (2026-10-12): some resources no tag filter finds (the Resource Groups Tagging API does not list
    IAM roles; many describe calls take no tag filter). A verify passes without a tag filter when it is a read-only aws
    command (READ_VERBS: get-, describe-, list-, ...), names by its prefixed name a resource that a create step of the
    task makes (the T106 name rule; `put-*` and capture variables do not count), and states the expected result."""
    command = verify.get("command") or ""
    if _operation(command) is None or not _read_only(command):
        return False
    if not (isinstance(verify.get("expect"), str) and verify["expect"].strip()):
        return False
    prefix = ctx.t.get("name_prefix", "saa-")
    created = set()
    for step in task.get("steps") or []:
        if isinstance(step, dict) and _create_verb(ctx, step.get("command") or "") not in (None, "put"):
            created |= {n for n in _resource_names(dict(step, capture=None)) if _has_prefix(n, prefix)}
    named = {n for n in _resource_names({"command": command}) if not n.startswith(("$", "<"))}
    return bool(named & created)


def _pairing(ctx: _Ctx, task: dict) -> list:
    """T107: every create has its own cleanup command, in reverse order of creation."""
    regex = ctx.t.get("create_command_regex", r"^(create|copy|run|allocate|launch)-")
    pairs_spec = ctx.t.get("cleanup_pairs") or {}
    creates, puts = [], []
    for step in task.get("steps") or []:
        command = (step or {}).get("command") or ""
        op = _operation(command)
        verb = _create_verb(ctx, command)
        if verb and verb != "put":
            noun = "bucket" if verb == "mb" else op[len(verb) + 1:]
            creates.append((op, verb, noun, _resource_names(step)))
        elif verb == "put":
            puts.append((op, op[4:]))

    def key(noun):
        return noun[:-1] if noun.endswith("s") else noun

    def undoes(cleanup_op, create):
        op, verb, noun = create[:3]
        if pairs_spec.get(op) == cleanup_op:
            return True
        undo, _, rest = cleanup_op.partition("-")
        if verb == "run" and undo == "stop" and key(noun) == "instance":
            return False        # gate-break 46: a stopped instance keeps its volumes and its bill
        if verb == "mb":
            return cleanup_op == "rb" or cleanup_op == "delete-bucket"
        return undo in UNDO.get(verb, []) and key(rest) == key(noun)

    unpaired = list(range(len(creates)))
    paired, messages, cleanup_ops = [], [], []
    for n, step in enumerate(task.get("cleanup") or []):
        command = (step or {}).get("command") or ""
        op = _operation(command)
        if not op:
            continue
        cleanup_ops.append(op)
        if re.search(r"(^|\s)--(dry-run|generate-cli-skeleton)\b", command):     # gate-break 45
            messages.append(f"cleanup[{n}] only pretends (--dry-run or --generate-cli-skeleton); it deletes nothing")
            continue
        for index in reversed(unpaired):
            if undoes(op, creates[index]):
                names = creates[index][3]
                if names and not any(name in command for name in names):     # gate-break 45
                    messages.append(f"cleanup[{n}] `{op}` does not name the resource of `{creates[index][0]}` "
                                    f"({' or '.join(sorted(names))})")
                    break
                paired.append(index)
                unpaired.remove(index)
                break
    messages += [f"no cleanup command undoes `{creates[i][0]}` (create command {i + 1} of {len(creates)})" for i in unpaired]
    # gate-break 44: a put-<noun> is undone by delete-<noun>, or by the delete of the resource that holds it
    # (put-bucket-policy by delete-bucket-policy or delete-bucket)
    for op, noun in puts:
        ok = pairs_spec.get(op) in cleanup_ops
        for cleanup_op in cleanup_ops:
            undo, _, rest = cleanup_op.partition("-")
            if undo in DELETE_VERBS and rest and (key(rest) == key(noun) or noun.startswith(key(rest) + "-") or noun.startswith(rest + "-")):
                ok = True
        if not ok and not re.search(r"tag|public-access-block|encryption|versioning|lifecycle|logging|retention", noun):
            messages.append(f"no cleanup command undoes `{op}`")
    got = [key(creates[i][2]) for i in paired]
    want = [key(creates[i][2]) for i in sorted(paired, reverse=True)]
    if got != want:
        messages.append("the cleanup is not in reverse order of creation: " + ", ".join(got) + " (expected " + ", ".join(want) + ")")
    return messages


# ---------------------------------------------------------------- item rules

def item_findings(ctx: _Ctx, task: dict):
    """(errors, warnings) of one task: T101 to T112, T114 to T117, T120."""
    from saalib import schemas
    errors, warnings = [], []
    t = ctx.t
    tid = task.get("id") if isinstance(task.get("id"), str) else None
    slug = ctx.ch["slug"]

    def err(code, msg):
        errors.append(_finding(code, tid, msg, ctx.file))

    def warn(code, msg):
        warnings.append(_finding(code, tid, msg, ctx.file))

    # T101
    for message in schemas.validate(task, "task", "task"):
        err("T101", "schema: " + message)
    if tid is None or not tid.startswith(slug + "-t"):
        err("T101", f"the id does not start with {slug}-t")
    if task.get("chapter") != slug:
        err("T101", f"chapter is not {slug}")
    if task.get("label") != t.get("label"):
        err("T101", "the label is not the fixed label of SPEC.json tasks.label")

    kind = task.get("type") if task.get("type") in ("look", "try", "lab") else None
    steps = [s for s in (task.get("steps") or []) if isinstance(s, dict)]
    cleanup = [s for s in (task.get("cleanup") or []) if isinstance(s, dict)]
    verify = task.get("verify") if isinstance(task.get("verify"), dict) else None
    create_regex = t.get("create_command_regex", r"^(create|copy|run|allocate|launch)-")
    all_text = " ".join(str(s.get("text") or "") for s in steps + cleanup)

    # T102
    if kind:
        minutes = (t.get("types", {}).get(kind) or {}).get("minutes")
        if isinstance(task.get("minutes"), int) and not _range_ok(task["minutes"], minutes):
            err("T102", f"{task['minutes']} minutes; a {kind} takes {_range_text(minutes)}")
        count = (t.get("steps") or {}).get(kind)
        if not _range_ok(len(steps), count):
            err("T102", f"{len(steps)} steps; a {kind} has {_range_text(count)}")
    limit = t.get("step_words_max", 40)
    for where, group in (("steps", steps), ("cleanup", cleanup)):
        for i, step in enumerate(group):
            words = _word_count(str(step.get("text") or ""))
            if words > limit:
                err("T102", f"{where}[{i}].text has {words} words (maximum {limit})")

    # T103
    if kind in ("try", "lab"):
        for field in ("cost", "cost_if_forgotten"):
            value = task.get(field)
            if not isinstance(value, str) or not value.strip():
                err("T103", f"a {kind} needs a cost line: `{field}` is missing")
            elif not DOLLAR.search(value):
                err("T103", f"`{field}` names no dollar amount")
        if not cleanup:
            err("T103", f"a {kind} needs cleanup steps")
        elif any(s.get("command") and not _read_only(s["command"]) and _verb(s["command"]) not in DELETE_VERBS for s in steps) \
                and not any(_verb(s.get("command") or "") in DELETE_VERBS for s in cleanup):
            # gate-break 44: `list-shelves` as the only cleanup of a task that changes the account
            err("T103", f"the steps change the account, and no cleanup command deletes anything")
        if verify is None or not verify.get("command"):
            err("T103", f"a {kind} needs a verify step")
        if not task.get("permissions"):
            err("T103", f"a {kind} needs `permissions`")
        if not (isinstance(task.get("read_only_alternative"), str) and task["read_only_alternative"].strip()):
            err("T103", f"a {kind} needs `read_only_alternative`")
    elif kind == "look":
        if cleanup:
            err("T103", "a look has no cleanup")
        if task.get("verify") is not None:
            err("T103", "a look has verify null")
        if task.get("cost") != "$0":
            err("T103", "the cost of a look is $0")
        for i, step in enumerate(steps):
            op = _operation(step.get("command") or "")
            if op and re.search(create_regex, op):
                err("T103", f"steps[{i}]: a look creates nothing (`{op}`)")
            elif op and not _read_only(step["command"]):     # gate-break 53: delete-*, put-*, modify-* in a Look
                err("T103", f"steps[{i}]: a look is read-only; `{op}` changes the account")

    # T104, T105, T115
    variable = re.compile(t.get("variable_regex", r"\$[A-Z][A-Z0-9_]*"))
    captured = []
    for i, step in enumerate(steps):
        command = step.get("command")
        capture = step.get("capture") if isinstance(step.get("capture"), dict) else None
        if command:
            for message in _form_errors(ctx, command, all_text):
                err("T104", f"steps[{i}]: {message}")
            for message in _banned(ctx, command):
                err("T105", f"steps[{i}]: {message}")
            for name in sorted(set(variable.findall(command))):
                if name[1:] not in captured:
                    err("T115", f"steps[{i}]: {name} is used, but no earlier step captures it")
        if capture:
            if not command:
                err("T104", f"steps[{i}]: a capture needs a command")
            elif re.search(r"(^|\s)--(query|output)\b", command):
                err("T104", f"steps[{i}]: a capture step stores the plain command; the tool adds --query and --output")
            name = capture.get("name")
            if name in captured:
                err("T115", f"steps[{i}]: {name} is captured twice")
            elif name:
                captured.append(name)
    later = [(f"cleanup[{i}]", s.get("command")) for i, s in enumerate(cleanup)]
    if verify:
        later.append(("verify", verify.get("command")))
    for where, command in later:
        if not command:
            continue
        for message in _form_errors(ctx, command, all_text):
            err("T104", f"{where}: {message}")
        for message in _banned(ctx, command):
            err("T105", f"{where}: {message}")
        for name in sorted(set(variable.findall(command))):
            if name[1:] not in captured:
                err("T115", f"{where}: {name} is used, but no step captures it")

    # T106, T116
    def patterns(key):
        return [p.replace("<task id>", re.escape(tid or "")) for p in (t.get(key) or [])]

    untaggable = list(t.get("untaggable_operations") or []) + ["mb"]
    prefix = t.get("name_prefix", "saa-")
    for i, step in enumerate(steps):
        command = step.get("command") or ""
        op = _operation(command)
        if not op or _create_verb(ctx, command) in (None, "put"):
            continue
        if op not in untaggable:
            # gate-break 51: the tag stands in the value of a tag option, not anywhere in the command
            tagged = _option_values(command, "tag")
            has_book = any(re.search(p, tagged) for p in patterns("tag_patterns"))
            has_task = any(re.search(p, tagged) for p in patterns("tag_task_patterns"))
            if not has_book or not has_task:
                missing = [name for name, ok in ((t.get("tag", "book=saa"), has_book), (f"task={tid}", has_task)) if not ok]
                err("T106", f"steps[{i}]: `{op}` lacks the tag " + " and ".join(missing) + " in a tag option")
        else:
            # gate-break 54: untaggable_rule of SPEC.json. A later step tags the resource, or its name starts with the prefix.
            names = [n for n in _resource_names(dict(step, capture=None)) if not n.startswith(("$", "<"))]
            tags_later = any(re.search(r"tag", _operation(s.get("command") or "") or "") for s in steps[i:])
            if names and not tags_later and not any(_has_prefix(n, prefix) for n in names):
                err("T106", f"steps[{i}]: `{op}` takes no tag: the name must start with {prefix}, or a later step must tag the resource")
        words = _words(command)
        for j, word in enumerate(words[:-1]):
            value = words[j + 1]
            if NAME_OPTION.match(word) and not value.startswith(("$", "<", "-")):
                if not (value.lstrip("/").startswith(prefix) or value.startswith("/saa/")):
                    warn("T116", f"steps[{i}]: the value of {word} does not start with {prefix}")

    # T107
    for message in _pairing(ctx, task):
        err("T107", message)

    # T108
    if kind in ("try", "lab") and verify and verify.get("command"):
        where = _option_values(verify["command"], "tag", "filter")     # gate-break 51: in a filter or tag option
        tagged = any(re.search(p, where) for p in patterns("verify_tag_patterns"))     # exemplar fix C7: task=<task id>
        if not tagged and not _verify_by_name(ctx, task, verify):     # 2026-10-12: or a read-only get on the saa- name
            err("T108", "the verify command does not filter by the tag " + t.get("tag", "book=saa") + f" or task={tid}, "
                "and is not a read-only command (get-, describe-, list-) that names a resource this task creates by its "
                + t.get("name_prefix", "saa-") + " name, with an expect")
        if not _read_only(verify["command"]):
            err("T108", "the verify command is not read-only")

    # T109
    amounts = {}
    for field in ("cost", "cost_if_forgotten"):
        text = str(task.get(field) or "")
        found = []
        for m in MONEY.finditer(text):      # gate-break 52: `4.50 USD`, `USD 4.50`, `5 dollars`, `20 cents`
            number = m.group(1) or m.group(2)
            value = float(number.replace(",", ""))
            if (m.group(3) or "").lower().startswith(("cent", "ct")):
                value, number = value / 100, f"{value / 100:.2f}"
            if value > 0:
                found.append(number)
        amounts[field] = found
        if kind in ("try", "lab") and MONEY_WORD.search(MONEY.sub(" ", text)):
            err("T109", f"`{field}` names money without an amount; write the amount with a $ sign")
    cost_facts = task.get("cost_facts") or []
    displays = []
    for fact_id in cost_facts:
        fact = ctx.fact(fact_id)
        if fact is None or fact.get("status") != "verified":
            err("T109", f"the cost fact {fact_id} is not a verified fact")
        elif fact.get("kind") not in ("price", "pricing-dimension"):
            err("T109", f"the cost fact {fact_id} is of kind {fact.get('kind')}, not price or pricing-dimension")
        else:
            displays += [str(v.get("display", "")) for v in fact.get("values", [])]
    for field, values in amounts.items():
        for amount in values:
            if not cost_facts:
                err("T109", f"`{field}` names ${amount} without a cost fact")
            elif not any(re.search(r"(?<![\d.,])" + re.escape(amount) + r"(?![\d]|[.,]\d)", d) for d in displays):
                err("T109", f"${amount} in `{field}` is in no display of the cost facts")
    cost_max = (t.get("types", {}).get(kind) or {}).get("cost_usd_max") if kind else None
    if cost_max is not None:
        for amount in amounts["cost"]:
            if float(amount.replace(",", "")) > cost_max:
                err("T109", f"the cost ${amount} is over the maximum ${cost_max} of a {kind}")

    # T110
    needs = t.get("break_it_step_needs") or ["predict", "expect", "explain"]
    for i, step in enumerate(steps):
        if not step.get("break_it"):
            continue
        for field in needs:
            if not (isinstance(step.get(field), str) and step[field].strip()):
                err("T110", f"steps[{i}]: a break-it step needs `{field}`")
        if i == len(steps) - 1:
            err("T110", f"steps[{i}]: a break-it step cannot be the last step; the fix is the next step")
        explain = step.get("explain")
        if isinstance(explain, str) and explain.strip():
            for message in _strict_text(ctx, explain, f"{tid}.steps[{i}].explain"):
                err("T110", f"steps[{i}].explain: {message}")
            for _, _, fact_id in FACT_LINK.findall(explain):
                if fact_id not in (task.get("facts") or []):
                    err("T110", f"steps[{i}].explain links {fact_id}, which is not in `facts`")

    # T111
    trap = task.get("trap")
    if trap is not None and trap not in ctx.traps():
        err("T111", f"unknown trap id {trap}")
    for fact_id in task.get("facts") or []:
        fact = ctx.fact(fact_id)
        if fact is None or fact.get("status") != "verified":
            err("T111", f"the fact {fact_id} is not verified")
    if not ctx.section_ok(task.get("section")):
        err("T111", f"the section {task.get('section')!r} does not resolve")
    for source in task.get("sources") or []:
        url = source.get("url") if isinstance(source, dict) else None
        if url and not ctx.url_known(url):
            err("T111", f"the source {url} is not in the corpus and is no evidence URL of a verified fact")

    # T112
    fields = [("title", task.get("title")), ("kills", task.get("kills")), ("cost", task.get("cost")),
              ("cost_if_forgotten", task.get("cost_if_forgotten")), ("read_only_alternative", task.get("read_only_alternative"))]
    fields += [(f"still_costs[{i}]", v) for i, v in enumerate(task.get("still_costs") or [])]
    for i, step in enumerate(steps):
        fields += [(f"steps[{i}].{k}", step.get(k)) for k in ("text", "expect", "predict", "explain")]
    fields += [(f"cleanup[{i}].text", s.get("text")) for i, s in enumerate(cleanup)]
    if verify:
        fields.append(("verify.expect", verify.get("expect")))
    for where, value in fields:
        if isinstance(value, str):
            for phrase in _banned_words(ctx, value):
                err("T112", f"{where}: banned word '{phrase}'")

    # T114
    if tid:
        report_path = common.REPORTS / "emulate" / f"{tid}.json"
        report = common.read_json(report_path)
        if report is not None:
            ctx.inputs.add(report_path)
            if report.get("result") == "fail":
                err("T114", "the emulation report has result fail")

    # T117
    for i, step in enumerate(steps):
        text = str(step.get("text") or "")
        if re.search(r"\bclick", text, re.I) or " > " in text:
            warn("T117", f"steps[{i}]: a click path in the step text")

    # T120
    template = task.get("template")
    if kind == "lab":
        if not template:
            err("T120", "a lab needs a `template`")
        elif not (common.BOOK / template).is_file():
            err("T120", f"the template {template} does not exist")
        else:
            ctx.inputs.add(common.BOOK / template)
    elif template:
        err("T120", f"a {kind or 'task'} has no template")
    return errors, warnings


# ---------------------------------------------------------------- chapter lint

def _cost_of(task: dict) -> float:
    values = [float(a.replace(",", "")) for a in DOLLAR.findall(str(task.get("cost") or ""))]
    return max(values) if values else 0.0


def lint_chapter(ch: dict, ship: bool = False, quick: bool = False) -> dict:
    """The result of `tasks lint CH`: {"chapter", "ok", "errors", "warnings", "counts"} plus "_inputs"."""
    ctx = _Ctx(ch, quick=quick)
    path = _tasks_path(ch)
    doc = common.read_json(path)
    errors, warnings = [], []
    if doc is not None:
        ctx.inputs.add(path)
    items = []
    if doc is not None:
        from saalib import schemas
        if not isinstance(doc, dict) or not isinstance(doc.get("items"), list):
            errors.append(_finding("T101", None, "tasks.json is not {v, chapter, items}", ctx.file))
        else:
            wrapper = {k: v for k, v in doc.items() if k != "items"}
            wrapper["items"] = []
            for message in schemas.validate(wrapper, "task"):
                errors.append(_finding("T101", None, "schema: " + message, ctx.file))
            if doc.get("chapter") != ch["slug"]:
                errors.append(_finding("T101", None, f"chapter is not {ch['slug']}", ctx.file))
            items = [t for t in doc["items"] if isinstance(t, dict)]
            if len(items) != len(doc["items"]):
                errors.append(_finding("T101", None, "an item is not an object", ctx.file))
    seen = set()
    for task in items:
        if task.get("id") in seen:
            errors.append(_finding("T101", task.get("id"), "the id is used twice", ctx.file))
        seen.add(task.get("id"))
        if task.get("status") in DEAD:
            continue
        item_errors, item_warnings = item_findings(ctx, task)
        errors += item_errors
        warnings += item_warnings

    live = [t for t in items if t.get("status") not in DEAD]
    counted = [t for t in live if t.get("status") == "ready"] if ship else live
    counts = {"total": len(items)}
    for status in ("candidate", "verified", "ready", "rejected", "retired"):
        counts[status] = sum(1 for t in items if t.get("status") == status)
    for kind in ("look", "try", "lab"):
        counts[kind] = sum(1 for t in counted if t.get("type") == kind)
    counts["break_it_steps"] = sum(1 for t in counted for s in (t.get("steps") or []) if isinstance(s, dict) and s.get("break_it"))
    counts["try_pass_route"] = sum(1 for t in counted if t.get("type") == "try" and t.get("pass_route") is True)
    counts["commands"] = len(chapter_commands(doc))

    # T201
    soft = errors if ship else warnings
    wanted = (_template(ch, ctx.spec).get("counts") or {}).get("tasks") or {}
    for kind in ("look", "try", "lab"):
        if kind in wanted and not _range_ok(counts[kind], wanted[kind]):
            soft.append(_finding("T201", None, f"{counts[kind]} {kind} tasks; the template asks for {_range_text(wanted[kind])}", ctx.file))
    if counts["break_it_steps"] < (wanted.get("break_it_steps_min") or 0):
        soft.append(_finding("T201", None, f"{counts['break_it_steps']} break-it steps; the template asks for at least {wanted['break_it_steps_min']}", ctx.file))
    if "try_pass_route" in wanted and not _range_ok(counts["try_pass_route"], wanted["try_pass_route"]):
        soft.append(_finding("T201", None, f"{counts['try_pass_route']} Try tasks with pass_route true; the template asks for {_range_text(wanted['try_pass_route'])}", ctx.file))
    for task in live:
        if task.get("type") == "look" and task.get("pass_route") is True:
            errors.append(_finding("T201", task.get("id"), "a look has pass_route false", ctx.file))

    # T113
    if counts["commands"]:
        report_path = common.REPORTS / "cli" / f"{ch['id']}.json"
        report = common.read_json(report_path)
        message = None
        if report is None:
            message = f"no CLI check report; run `tasks check-cli {ch['id']}`"
        else:
            ctx.inputs.add(report_path)
            if report.get("commands_sha256") != commands_sha256(doc):
                message = f"the CLI check report is older than the commands; run `tasks check-cli {ch['id']}`"
            elif not report.get("ok"):
                message = "the CLI check report is not ok"
            else:
                # gate-break 56: the report holds one checked row for every command, made with the pinned awscli.
                # (A file is no proof of a tool run; the finalize step runs `tasks check-cli` again.)
                rows = report.get("commands") if isinstance(report.get("commands"), list) else []
                checked = {r.get("command") for r in rows if isinstance(r, dict) and r.get("ok") is True and not r.get("errors")}
                missing = [c for c in dict.fromkeys(chapter_commands(doc)) if c not in checked]
                if missing:
                    message = (f"the CLI check report has no ok row for {len(missing)} of the commands "
                               f"(first: {missing[0][:60]}); run `tasks check-cli {ch['id']}`")
                elif report.get("awscli") != pinned_version("cli_model.py", "awscli"):
                    message = f"the CLI check report was not made with the pinned awscli; run `tasks check-cli {ch['id']}`"
        if message:
            soft.append(_finding("T113", None, message, ctx.file))

    inputs = [{"path": _rel(p), "sha256": common.sha256_file(p)} for p in sorted(ctx.inputs, key=str) if p.is_file()]
    return {"chapter": ch["id"], "ok": not errors, "errors": errors, "warnings": warnings, "counts": counts, "_inputs": inputs}


def _exit_for(result: dict) -> int:
    if result["errors"]:
        return common.EXIT_FAIL
    return common.EXIT_WARN if result["warnings"] else common.EXIT_OK


def gate_tasks(ch_id, quick=False, **options) -> dict:
    """Gate `tasks`: `tasks lint CH` (with ship=True: the --ship form that the counts gate uses)."""
    ch = common.chapter(ch_id)
    result = lint_chapter(ch, ship=bool(options.get("ship")), quick=quick)
    return {"gate": "tasks", "chapter": ch["id"], "ok": result["ok"], "exit": _exit_for(result),
            "errors": result["errors"], "warnings": result["warnings"], "counts": result["counts"],
            "inputs": result["_inputs"]}


def lint_all(ship: bool = False) -> dict:
    """Every chapter that has a tasks.json, plus T119 (the cost of all tasks)."""
    errors, warnings, rows = [], [], []
    total_cost, total_tasks = 0.0, 0
    for ch in common.chapters():
        doc = _load_doc(ch)
        if doc is None:
            continue
        result = lint_chapter(ch, ship=ship)
        errors += result["errors"]
        warnings += result["warnings"]
        rows.append({"chapter": ch["id"], "ok": result["ok"], "errors": len(result["errors"]),
                     "warnings": len(result["warnings"]), "tasks": result["counts"]["total"]})
        live = _live(doc)
        total_tasks += len(live)
        total_cost += sum(_cost_of(t) for t in live)
    limit = _spec().get("tasks", {}).get("book_cost_usd_max")
    if limit is not None and total_cost > limit + 1e-9:
        errors.append(_finding("T119", None, f"all tasks together cost ${total_cost:.2f}; the maximum is ${limit}"))
    return {"ok": not errors, "errors": errors, "warnings": warnings,
            "counts": {"chapters": len(rows), "tasks": total_tasks, "cost_usd": round(total_cost, 2)}, "chapters": rows}


# ---------------------------------------------------------------- output

def _line(finding: dict) -> str:
    where = finding.get("item") or finding.get("file") or "tasks"
    return f"{where}: {finding['code']} {finding['msg']}"


def _show(args, obj: dict, summary: str, findings=()) -> None:
    if getattr(args, "json", False):
        common.emit({k: v for k, v in obj.items() if not k.startswith("_")}, args)
        return
    lines = [summary] + [_line(f) for f in list(findings)[:40]]
    if len(findings) > 40:
        lines.append(f"... {len(findings) - 40} more findings (use --json --out FILE)")
    common.emit("\n".join(lines), args)


# ---------------------------------------------------------------- tasks lint

def cmd_lint(args) -> int:
    if args.all == bool(args.chapter):
        return common.fail("give one chapter or --all", common.EXIT_PRECONDITION)
    if args.all:
        result = lint_all(ship=args.ship)
        label = f"{result['counts']['chapters']} chapters, {result['counts']['tasks']} tasks"
    else:
        ch = common.chapter(args.chapter)
        result = lint_chapter(ch, ship=args.ship)
        label = f"chapter {ch['id']}, {result['counts']['total']} tasks"
    word = "FAIL" if result["errors"] else ("WARN" if result["warnings"] else "OK")
    summary = f"{word} tasks lint: {label}, {len(result['errors'])} errors, {len(result['warnings'])} warnings"
    _show(args, result, summary, result["errors"] + result["warnings"])
    return _exit_for(result)


# ---------------------------------------------------------------- tasks add, set-status

def _input_items(file_arg: str):
    from pathlib import Path
    path = Path(file_arg)
    if not path.is_absolute():
        path = common.REPO / path
    if not common.inside_book(path):
        return None, common.fail("--file must be inside the book folder", common.EXIT_POLICY)
    if not path.is_file():
        return None, common.fail(f"no file {common.rel(path)}", common.EXIT_PRECONDITION)
    try:
        data = common.read_json(path)
    except ValueError as exc:
        return None, common.fail(f"{common.rel(path)} is not JSON: {exc}", common.EXIT_FAIL)
    if isinstance(data, dict) and isinstance(data.get("items"), list):
        data = data["items"]
    items = data if isinstance(data, list) else [data]
    if not all(isinstance(i, dict) for i in items):
        return None, common.fail("the file must hold one object or an array of objects", common.EXIT_FAIL)
    return items, 0


def _mark_stale(ch_id: str, reason: str) -> None:
    try:
        from saalib import ledger
        ledger.mark_stale(ch_id, reason, item_stages=["tasks"])
    except Exception:
        pass


def cmd_add(args) -> int:
    ch = common.chapter(args.chapter)
    items, code = _input_items(args.file)
    if items is None:
        return code
    slug = ch["slug"]
    path = _tasks_path(ch)
    added, replaced, rejected, stale = [], [], [], False
    with common.file_lock(path):
        doc = common.read_json(path) or {"v": 1, "chapter": slug, "items": []}
        stored = doc.setdefault("items", [])
        ctx = _Ctx(ch)
        label = ctx.t.get("label")
        for index, raw in enumerate(items):
            task = dict(raw)
            task["chapter"] = slug
            tid = task.get("id")
            old = next((t for t in stored if t.get("id") == tid), None) if tid else None
            problems = []
            rev = 1
            if args.replace:
                if old is None:
                    problems.append(_finding("T101", tid, "--replace needs the id of a stored task", ctx.file))
                elif old.get("status") in DEAD:
                    problems.append(_finding("T101", tid, f"a {old.get('status')} task cannot be replaced", ctx.file))
                else:
                    rev = int(old.get("rev") or 1) + (0 if old.get("status") == "candidate" else 1)
            elif old is not None:
                problems.append(_finding("T101", tid, "the id exists; use --replace", ctx.file))
            if not tid:
                numbers = [int(t["id"][-2:]) for t in stored if re.fullmatch(re.escape(slug) + r"-t\d{2}", str(t.get("id")))]
                tid = f"{slug}-t{(max(numbers) if numbers else 0) + 1:02d}"
                task["id"] = tid
            task.update({"status": "candidate", "rev": rev, "label": label, "checked": common.today()})
            if not problems:
                problems = item_findings(ctx, task)[0]
            if problems:
                rejected.append({"index": index, "id": raw.get("id"), "errors": problems})
                continue
            if old is not None:
                stale = stale or old.get("status") != "candidate"
                stored[stored.index(old)] = task
                replaced.append(tid)
            else:
                stored.append(task)
                added.append(tid)
        if added or replaced:
            common.write_json(path, doc)
    if stale:
        _mark_stale(ch["id"], "task replaced: " + ", ".join(replaced))
    result = {"added": added, "replaced": replaced, "rejected": rejected}
    findings = [f for r in rejected for f in r["errors"]]
    _show(args, result, f"{'FAIL' if rejected else 'OK'} tasks add: {len(added)} added, {len(replaced)} replaced, {len(rejected)} rejected", findings)
    return common.EXIT_FAIL if rejected else common.EXIT_OK


def cmd_set_status(args) -> int:
    ch = common.chapter(args.chapter)
    path = _tasks_path(ch)
    done, refused = [], []
    with common.file_lock(path):
        doc = common.read_json(path)
        if doc is None:
            return common.fail(f"no {_rel(path)}", common.EXIT_PRECONDITION)
        ctx = _Ctx(ch)
        for tid in args.ids:
            task = next((t for t in doc.get("items", []) if t.get("id") == tid), None)
            if task is None:
                refused.append({"id": tid, "errors": [_finding("T101", tid, "unknown task id", ctx.file)]})
            elif args.status in DEAD and not args.reason:
                refused.append({"id": tid, "errors": [_finding("T101", tid, f"--status {args.status} needs --reason", ctx.file)]})
            else:
                problems = item_findings(ctx, task)[0] if args.status == "ready" else []
                if problems:
                    refused.append({"id": tid, "errors": problems})
                else:
                    task["status"] = args.status
                    done.append(tid)
        if done:
            common.write_json(path, doc)
    result = {"set": done, "refused": refused}
    findings = [f for r in refused for f in r["errors"]]
    _show(args, result, f"{'FAIL' if refused else 'OK'} tasks set-status {args.status}: {len(done)} set, {len(refused)} refused", findings)
    return common.EXIT_FAIL if refused else common.EXIT_OK


# ---------------------------------------------------------------- helpers run by uv

def _helper(name: str):
    return common.TOOLS / "helpers" / name


def pinned_version(helper: str, package: str) -> str:
    """The version of `package` pinned in the inline dependencies of a helper script."""
    text = _helper(helper).read_text(encoding="utf-8") if _helper(helper).is_file() else ""
    match = re.search(re.escape(package) + r"(?:\[[a-z,]+\])?==([0-9][0-9A-Za-z.]*)", text)
    return match.group(1) if match else "unknown"


def _run_uv(helper: str, payload, timeout: int = 900):
    """Run a helper through `uv run --script`, JSON in, JSON out. Raises HelperError (exit 5)."""
    script = _helper(helper)
    if not script.is_file():
        raise HelperError(f"no helper {common.rel(script)}")
    argv = ["uv", "run", "--quiet"] + (["--offline"] if os.environ.get("SAA_UV_OFFLINE") else []) + ["--script", str(script)]
    try:
        proc = subprocess.run(argv, input=json.dumps(payload), capture_output=True, text=True, timeout=timeout)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise HelperError(f"uv could not run {helper}: {exc}")
    if proc.returncode != 0:
        raise HelperError(f"{helper} ended with code {proc.returncode}: {proc.stderr.strip()[-400:]}")
    try:
        return json.loads(proc.stdout)
    except ValueError:
        raise HelperError(f"{helper} printed no JSON")


def _run_helper(commands: list) -> list:
    """One result per command from the offline AWS CLI command model. Tests patch this function."""
    return _run_uv("cli_model.py", commands)["results"]


def _run_emulator(payload: dict) -> dict:
    """Run one task against a local moto server. Tests patch this function."""
    return _run_uv("emulate.py", payload, timeout=1800)


# ---------------------------------------------------------------- tasks check-cli

def check_cli(ch_id, reference: bool = False):
    """Check every command of the chapter and write the report. Returns (exit code, report)."""
    ch = common.chapter(ch_id)
    doc = _load_doc(ch)
    t = _spec().get("tasks", {})
    commands = chapter_commands(doc)
    unique = list(dict.fromkeys(commands))
    try:
        results = _run_helper(unique) if unique else []
    except HelperError as exc:
        return common.EXIT_TRANSIENT, {"chapter": ch["id"], "ok": False, "error": str(exc)}
    rows = []
    for command, row in zip(unique, results):
        rows.append({"command": command, "service": row.get("service"), "operation": row.get("operation"),
                     "ok": bool(row.get("ok")), "errors": list(row.get("errors") or []),
                     "tag_options": list(row.get("tag_options") or [])})
    if len(rows) != len(unique):
        return common.EXIT_TRANSIENT, {"chapter": ch["id"], "ok": False, "error": "the helper returned another number of results"}

    if reference:
        try:
            from saalib import corpus
        except Exception as exc:
            return common.EXIT_PRECONDITION, {"chapter": ch["id"], "ok": False, "error": f"no corpus module: {exc}"}
        seen = {}
        for row in rows:
            if not row["ok"] or not row["service"] or not row["operation"] or not row["command"].startswith("aws "):
                continue
            page = f"{row['service']}/{row['operation'].replace(' ', '/')}"
            if page not in seen:
                url = f"https://docs.aws.amazon.com/cli/latest/reference/{page}.html"
                try:
                    final = str((corpus.fetch(url) or {}).get("final_url") or "")
                    last = row["operation"].split(" ")[-1]
                    seen[page] = None if final.endswith((f"/{last}.html", f"/{last}.md")) else f"no CLI reference page {url} (it leads to {final})"
                except Exception as exc:
                    if exc.__class__.__name__ == "TransientError":
                        return common.EXIT_TRANSIENT, {"chapter": ch["id"], "ok": False, "error": str(exc)}
                    seen[page] = f"no CLI reference page {url}: {exc}"
            if seen[page]:
                row["ok"] = False
                row["errors"].append(seen[page])

    # T118: the tag list of SPEC.json against the command model
    warnings = []
    regex = t.get("create_command_regex", r"^(create|copy|run|allocate|launch)-")
    untaggable = t.get("untaggable_operations") or []
    by_command = {row["command"]: row for row in rows}
    for task in _live(doc):
        for step in task.get("steps") or []:
            command = (step or {}).get("command") or ""
            op = _operation(command)
            row = by_command.get(command)
            if not op or not row or not row["ok"] or not re.search(regex, op):
                continue
            if op in untaggable and row["tag_options"]:
                warnings.append(_finding("T118", task.get("id"), f"`{row['service']} {op}` is listed as untaggable, but the CLI model has {', '.join(row['tag_options'])}"))
            elif op not in untaggable and not row["tag_options"]:
                warnings.append(_finding("T118", task.get("id"), f"`{row['service']} {op}` has no tag option in the CLI model and is not in untaggable_operations"))

    report = {"chapter": ch["id"], "awscli": pinned_version("cli_model.py", "awscli"), "checked": common.today(),
              "commands_sha256": commands_sha256(doc), "ok": all(r["ok"] for r in rows), "commands": rows, "warnings": warnings}
    common.write_json(common.REPORTS / "cli" / f"{ch['id']}.json", report)
    return (common.EXIT_OK if report["ok"] else common.EXIT_FAIL), report


def cmd_check_cli(args) -> int:
    if args.all == bool(args.chapter):
        return common.fail("give one chapter or --all", common.EXIT_PRECONDITION)
    targets = [c for c in common.chapters() if _load_doc(c) is not None] if args.all else [common.chapter(args.chapter)]
    reports, worst, lines = [], common.EXIT_OK, []
    for ch in targets:
        code, report = check_cli(ch["id"], reference=args.reference)
        if code in (common.EXIT_TRANSIENT, common.EXIT_PRECONDITION):
            return common.fail(report.get("error", "the helper did not run"), code)
        worst = max(worst, code)
        reports.append(report)
        for row in report["commands"]:
            for error in row["errors"]:
                lines.append(_finding("T113", None, f"{error}: {row['command'][:90]}", f"_build/reports/cli/{ch['id']}.json"))
        lines += report["warnings"]
    result = reports[0] if not args.all else {"ok": all(r["ok"] for r in reports), "chapters": reports}
    total = sum(len(r["commands"]) for r in reports)
    bad = sum(1 for r in reports for row in r["commands"] if not row["ok"])
    _show(args, result, f"{'FAIL' if worst else 'OK'} tasks check-cli: {total} commands, {bad} not ok (awscli {pinned_version('cli_model.py', 'awscli')})", lines)
    return worst


# ---------------------------------------------------------------- tasks emulate

def emulate_task(task: dict) -> dict:
    """Emulation report of one task: pass, fail or not-supported."""
    t = _spec().get("tasks", {})
    placeholder = re.compile(t.get("placeholder_regex", r"<[A-Z][A-Z0-9_]*>"))
    listed = commands_of(task)
    reason = None
    if not listed:
        reason = "the task has no command"
    elif any(not command.startswith("aws ") for _, command, _ in listed):
        reason = "a command is not an aws command"
    elif any(placeholder.search(command) for _, command, _ in listed):
        reason = "a command has a placeholder"
    if reason:
        return {"task": task.get("id"), "result": "not-supported", "steps": [], "note": reason}
    payload = {"task": task.get("id"),
               "steps": [{"command": s.get("command"), "capture": s.get("capture"), "break_it": bool(s.get("break_it"))}
                         for s in task.get("steps") or [] if s.get("command")],
               "cleanup": [s.get("command") for s in task.get("cleanup") or [] if s.get("command")],
               "verify": (task.get("verify") or {}).get("command")}
    out = _run_emulator(payload)
    return {"task": task.get("id"), "result": out.get("result"), "steps": out.get("steps", []), "note": out.get("note", "")}


def cmd_emulate(args) -> int:
    ch = common.chapter(args.chapter)
    tasks = [t for t in _live(_load_doc(ch)) if not args.task or t.get("id") == args.task]
    if not tasks:
        return common.fail("no such task", common.EXIT_PRECONDITION)
    reports = []
    for task in tasks:
        try:
            report = emulate_task(task)
        except HelperError as exc:
            return common.fail(str(exc), common.EXIT_TRANSIENT)
        if report["result"] not in ("pass", "fail", "not-supported"):
            return common.fail(f"the emulator returned no result for {task.get('id')}", common.EXIT_TRANSIENT)
        common.write_json(common.REPORTS / "emulate" / f"{task['id']}.json", report)
        reports.append(report)
    failed = [r for r in reports if r["result"] == "fail"]
    result = {"chapter": ch["id"], "ok": not failed, "tasks": reports}
    lines = [_finding("T114", r["task"], f"emulation {r['result']}" + (f": {r['note']}" if r.get("note") else "")) for r in reports]
    _show(args, result, f"{'FAIL' if failed else 'OK'} tasks emulate: " + ", ".join(f"{r['task']}={r['result']}" for r in reports), lines)
    return common.EXIT_FAIL if failed else common.EXIT_OK


# ---------------------------------------------------------------- registration

def register(subparsers) -> None:
    parser = subparsers.add_parser("tasks", help="hands-on tasks: add, lint, set-status, check-cli, emulate")
    sub = parser.add_subparsers(dest="tasks_cmd")
    parser.set_defaults(func=lambda a: (parser.print_help(), common.EXIT_PRECONDITION)[1])
    default_by = os.environ.get("SAA_AGENT", "unknown")

    p = sub.add_parser("add", help="add or replace tasks from a JSON file")
    p.add_argument("--chapter", required=True)
    p.add_argument("--file", required=True)
    p.add_argument("--replace", action="store_true")
    p.add_argument("--by", default=default_by)
    common.add_common_args(p)
    p.set_defaults(func=cmd_add)

    p = sub.add_parser("lint", help="check the tasks of a chapter (T rules)")
    p.add_argument("chapter", nargs="?")
    p.add_argument("--all", action="store_true")
    p.add_argument("--ship", action="store_true", help="T113 and T201 block")
    common.add_common_args(p)
    p.set_defaults(func=cmd_lint)

    p = sub.add_parser("set-status", help="set the status of tasks")
    p.add_argument("--chapter", required=True)
    p.add_argument("--status", required=True, choices=["ready", "verified", "retired", "rejected"])
    p.add_argument("ids", nargs="+", metavar="ID")
    p.add_argument("--by", default=default_by)
    p.add_argument("--reason")
    common.add_common_args(p)
    p.set_defaults(func=cmd_set_status)

    p = sub.add_parser("check-cli", help="check every command against the AWS CLI command model (offline)")
    p.add_argument("chapter", nargs="?")
    p.add_argument("--all", action="store_true")
    p.add_argument("--reference", action="store_true", help="also require the CLI reference page of each command")
    common.add_common_args(p)
    p.set_defaults(func=cmd_check_cli)

    p = sub.add_parser("emulate", help="optional: run a task against a local moto server")
    p.add_argument("chapter")
    p.add_argument("--task")
    common.add_common_args(p)
    p.set_defaults(func=cmd_emulate)
