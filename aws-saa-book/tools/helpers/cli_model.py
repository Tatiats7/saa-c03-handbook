# /// script
# requires-python = ">=3.9"
# dependencies = ["awscli==1.46.1"]
# ///
"""Offline check of AWS CLI commands against the command model of the pinned awscli package.

Run by `saa.py tasks check-cli` as:  uv run --script aws-saa-book/tools/helpers/cli_model.py
Input (standard input): a JSON list of command strings.
Output (standard output): {"awscli": "<version>", "results": [{"command", "service", "operation",
"ok", "errors": [...], "tag_options": [...]}]}

It makes no AWS call and reads no credentials: the config and credential files are pointed at
/dev/null, the instance metadata lookup is off, and no command is ever executed. Only the
command table (service, operation, option names, required options) is read from the package.
"""
import json
import os
import re
import shlex
import sys

os.environ["AWS_CONFIG_FILE"] = os.devnull
os.environ["AWS_SHARED_CREDENTIALS_FILE"] = os.devnull
os.environ["AWS_EC2_METADATA_DISABLED"] = "true"
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
for _name in ("AWS_PROFILE", "AWS_DEFAULT_PROFILE", "AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN"):
    os.environ.pop(_name, None)

import awscli  # noqa: E402
from awscli.clidriver import create_clidriver  # noqa: E402

SKIP_REQUIRED_WHEN = {"--cli-input-json", "--cli-input-yaml", "--generate-cli-skeleton"}


def _subtable(command):
    """The subcommand table of a command object, or None when it has none."""
    getter = getattr(command, "_get_command_table", None)      # ServiceCommand
    if callable(getter):
        try:
            return getter()
        except Exception:
            return None
    table = getattr(command, "subcommand_table", None)         # BasicCommand (s3, configure, wait)
    if table:
        return table
    return None


def _arg_table(command):
    try:
        return dict(command.arg_table)
    except Exception:
        return None


SCALARS = {"string", "integer", "long", "float", "double", "timestamp", "blob", "character", "boolean"}


def _is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False


def _arity(arg):
    """How many words an option takes: 0 for a flag, 1 for a scalar, many for a list or a structure."""
    action = getattr(arg, "action", None)
    if action in ("store_true", "store_false", "version", "count"):
        return 0
    kind = getattr(arg, "cli_type_name", None)
    if kind == "boolean":
        return 0
    if getattr(arg, "nargs", None) in ("+", "*"):
        return 99
    if kind in SCALARS or getattr(arg, "choices", None):
        return 1
    if kind is None:
        return 1 if getattr(arg, "nargs", None) in (None, 1, "?") else 99
    return 99


def _members(shape):
    """The member names that a shorthand value may use for this shape, or None when any key is allowed."""
    try:
        kind = shape.type_name
        if kind == "list":
            return _members(shape.member)
        if kind == "structure":
            return set(shape.members)
    except Exception:
        return None
    return None


def _top_keys(value):
    """The keys of a shorthand value at the top level: `Name=a,Values=b` gives Name and Values; the keys inside
    [...] and {...} belong to nested shapes and are not checked."""
    keys, depth, start = [], 0, True
    i = 0
    while i < len(value):
        ch = value[i]
        if ch in "[{":
            depth += 1
        elif ch in "]}":
            depth = max(0, depth - 1)
        elif depth == 0 and ch == ",":
            start = True
            i += 1
            continue
        elif depth == 0 and start:
            match = re.match(r"([A-Za-z][A-Za-z0-9]*)=", value[i:])
            if match:
                keys.append(match.group(1))
                i += match.end()
                start = False
                continue
        if ch != " ":
            start = False
        i += 1
    return keys


def _is_positional(arg):
    """A positional argument of the command. Besides `positional_arg`, a StreamingOutputArgument (the <outfile>
    of `lambda invoke` or `s3api get-object`) is positional: its cli_name has no `--` prefix (CLI reference synopsis).
    fix-18, 2026-10-14: the helper read `response.json` as a stray word and asked for a `--outfile` the CLI lacks."""
    if getattr(arg, "positional_arg", False):
        return True
    name = getattr(arg, "cli_name", None)
    return isinstance(name, str) and bool(name) and not name.startswith("-")


def _positional_room(args):
    room = 0
    for arg in args.values():
        if _is_positional(arg):
            nargs = getattr(arg, "nargs", None)
            room += nargs if isinstance(nargs, int) else (99 if nargs in ("+", "*") else 1)
    return room


def _value_errors(name, arg, given):
    """Enum values and shorthand keys of one option (gate-break 55)."""
    errors = []
    choices = getattr(arg, "choices", None)
    model = getattr(arg, "argument_model", None)
    enum = list(choices or getattr(model, "enum", None) or [])
    if enum and _arity(arg) == 1:
        for value in given:
            if value not in enum and not value.startswith(("$", "<")):
                errors.append(f"--{name}: {value!r} is not one of {', '.join(map(str, enum[:8]))}")
    members = _members(model) if model is not None else None
    if members:
        for value in given:
            if value[:1] in "{[" or value.startswith(("file://", "fileb://", "$", "<")):
                continue        # JSON, a file or a placeholder: not shorthand
            for key in _top_keys(value):
                if key not in members:
                    errors.append(f"--{name}: unknown key {key!r} (the model has {', '.join(sorted(members)[:8])})")
    return errors


def _output_shape(command_obj):
    for attr in ("_operation_model", "operation_model"):
        model = getattr(command_obj, attr, None)
        if model is not None:
            return getattr(model, "output_shape", None)
    return None


def _walk_query(node, shape, errors):
    """Follow a JMESPath syntax tree through the output shape; report a field that the shape does not have.
    Returns the shape the node selects, or None when it cannot be told."""
    kind, children = node.get("type"), node.get("children", [])
    if kind == "field":
        if shape is None or getattr(shape, "type_name", None) != "structure":
            return None
        if node["value"] not in shape.members:
            errors.append(f"--query: the output has no field {node['value']!r} here (it has {', '.join(sorted(shape.members)[:8])})")
            return None
        return shape.members[node["value"]]
    if kind in ("subexpression", "index_expression", "pipe"):
        for child in children:
            shape = _walk_query(child, shape, errors)
        return shape
    if kind in ("projection", "flatten", "value_projection", "filter_projection"):
        left = _walk_query(children[0], shape, errors) if children else shape
        if kind == "flatten":
            return left
        inner = getattr(left, "member", None) if left is not None and getattr(left, "type_name", None) == "list" else None
        if left is not None and getattr(left, "type_name", None) == "map":
            inner = getattr(left, "value", None)
        for child in children[2:]:
            _walk_query(child, inner, errors)
        _walk_query(children[1], inner, errors) if len(children) > 1 else None
        return None
    if kind in ("index", "slice"):
        return getattr(shape, "member", None) if shape is not None and getattr(shape, "type_name", None) == "list" else None
    if kind in ("identity", "current"):
        return shape
    if kind in ("multi_select_list", "multi_select_dict", "key_val_pair", "comparator", "or_expression", "and_expression",
                "not_expression"):
        for child in children:
            _walk_query(child, shape, errors)
        return None
    return None        # literal, function_expression, expref: not checked


def _query_errors(expression, command_obj):
    """--query: the expression compiles, and its fields exist in the output of the operation (gate-break 55)."""
    try:
        import jmespath
        tree = jmespath.compile(expression).parsed
    except ImportError:
        return []
    except Exception as exc:
        return [f"--query does not compile: {str(exc).splitlines()[0][:120]}"]
    errors = []
    try:
        shape = _output_shape(command_obj)
        if shape is not None:
            _walk_query(tree, shape, errors)
    except Exception:
        return []
    return errors[:3]


def check(command, top, global_args):
    result = {"command": command, "service": None, "operation": None, "ok": False, "errors": [], "tag_options": []}
    try:
        words = shlex.split(command)
    except ValueError as exc:
        result["errors"].append(f"cannot split the command: {exc}")
        return result
    if not words or words[0] != "aws":
        result["ok"] = True
        result["skipped"] = "not an aws command"
        return result
    rest = words[1:]
    # global options can stand before the service name
    i = 0
    while i < len(rest) and rest[i].startswith("--"):
        name = rest[i][2:].split("=", 1)[0]
        arg = global_args.get(name)
        if arg is None:
            result["errors"].append(f"unknown option --{name}")
            return result
        takes_value = getattr(arg, "action", "store") not in ("store_true", "store_false", "version")
        i += 1 if ("=" in rest[i] or not takes_value) else 2
    rest = rest[i:]
    if not rest:
        result["errors"].append("no service")
        return result
    service = rest[0]
    result["service"] = service
    if service not in top:
        result["errors"].append(f"unknown service {service}")
        return result
    command_obj = top[service]
    path = []
    j = 1
    while True:
        table = _subtable(command_obj)
        if not table:
            break
        if j >= len(rest) or rest[j].startswith("-"):
            result["errors"].append(f"no operation after {' '.join([service] + path)}")
            return result
        if rest[j] not in table:
            result["operation"] = " ".join(path + [rest[j]])
            result["errors"].append(f"unknown operation {rest[j]}")
            return result
        path.append(rest[j])
        command_obj = table[rest[j]]
        j += 1
    result["operation"] = " ".join(path) if path else None
    args = _arg_table(command_obj)
    if args is None:
        result["errors"].append("the command model has no option table for this command")
        return result
    result["tag_options"] = sorted("--" + name for name in args if "tag" in name.lower())
    used = set()
    # gate-break 55: every word after the operation is an option, a value of the option before it, or a
    # positional argument of the command. `-filters`, a bare `filters` and a second value of a one-value option
    # are errors, and so are unknown shorthand keys, unknown enum values and a --query that cannot be compiled
    # or that names a field the output does not have.
    positional = _positional_room(args)
    stray, current, values = [], None, {}
    for token in rest[j:]:
        if token.startswith("--") and len(token) > 2:
            name, eq, inline = token[2:].partition("=")
            used.add("--" + name)
            arg = args.get(name) or global_args.get(name)
            if arg is None:
                close = sorted(n for n in args if n.startswith(name) or name.startswith(n))[:3]
                hint = f" (the model has {', '.join('--' + n for n in close)})" if close else ""
                result["errors"].append(f"unknown option --{name}{hint}")
                current = ("?", None, 99)
                continue
            current = (name, arg, _arity(arg))
            values.setdefault(name, [])
            if eq:
                values[name].append(inline)
        elif current is not None and len(values.get(current[0], [])) < current[2]:
            values.setdefault(current[0], []).append(token)
        else:
            stray.append(token)
    if len(stray) > positional:
        for token in stray[positional:]:
            what = "a single dash; options start with --" if token.startswith("-") and not _is_number(token) else "not an option and not the value of one"
            result["errors"].append(f"unexpected word {token!r} ({what})")
    for name, given in values.items():
        arg = args.get(name) or global_args.get(name)
        if arg is None:
            continue
        try:
            result["errors"] += _value_errors(name, arg, given)
        except Exception:       # a shape that this helper does not understand is not an error of the command
            pass
    if values.get("query"):
        result["errors"] += _query_errors(values["query"][0], command_obj)
    if "query" in values and not values["query"]:
        result["errors"].append("--query has no value")
    if not (used & SKIP_REQUIRED_WHEN):
        for name, arg in sorted(args.items()):
            # a required boolean is also given by its negated form (--no-<name>), as the CLI reference shows
            if getattr(arg, "required", False) and not _is_positional(arg) and "--" + name not in used \
                    and "--no-" + name not in used:
                result["errors"].append(f"missing required option --{name}")
    result["ok"] = not result["errors"]
    return result


def main():
    commands = json.load(sys.stdin)
    if not isinstance(commands, list):
        raise SystemExit("input must be a JSON list of command strings")
    driver = create_clidriver()
    top = driver._get_command_table()
    global_args = driver._get_argument_table()
    results = [check(str(c), top, global_args) for c in commands]
    json.dump({"awscli": awscli.__version__, "results": results}, sys.stdout, indent=1)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
