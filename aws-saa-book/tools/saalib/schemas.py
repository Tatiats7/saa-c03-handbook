"""Shared JSON Schema subset validator. Standard library only. No subcommand (no register()).

Every module validates its data with this one function, so "schema-checked" means the same
thing everywhere:

    from saalib import schemas
    errors = schemas.validate(obj, "fact")            # [] when valid
    errors = schemas.validate(doc, "question")        # a whole questions.json document
    errors = schemas.validate(item, "question", "question")   # one item, against $defs.question

Supported keywords are exactly the list in SPEC.json under data_files.schema_keywords_used:
$ref (local, "#/..."), type (name or list), const, enum, pattern (re.search), minLength,
maxLength, minimum, maximum, minItems, maxItems, uniqueItems, items, properties, required,
additionalProperties (only `false` is enforced). Schemas live in common.SCHEMA_DIR as
<name>.schema.json; when a sandbox has no schema folder, the real one is used.
"""
from __future__ import annotations

import json
import re

from saalib import common

_TYPES = {"object": dict, "array": list, "string": str, "boolean": bool, "null": type(None)}
_cache: dict = {}


def load(name: str) -> dict:
    """Load <name>.schema.json from the sandbox schema folder, else from the real book."""
    for base in (common.SCHEMA_DIR, common.REAL_BOOK / "_build" / "schemas"):
        path = base / f"{name}.schema.json"
        if path.exists():
            key = str(path)
            if key not in _cache:
                _cache[key] = common.read_json(path)
            return _cache[key]
    raise FileNotFoundError(f"no schema {name}.schema.json")


def _type_ok(value, name: str) -> bool:
    if name == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if name == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return isinstance(value, _TYPES[name])


def check(value, schema: dict, root: dict, path: str = "$") -> list:
    """Return a list of error strings (empty when valid)."""
    if "$ref" in schema:
        target = root
        for part in schema["$ref"].lstrip("#/").split("/"):
            target = target[part]
        return check(value, target, root, path)
    errors = []
    if "type" in schema:
        names = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(_type_ok(value, n) for n in names):
            return [f"{path}: expected {'|'.join(names)}, got {type(value).__name__}"]
    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: must equal {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: {value!r} not in enum")
    if isinstance(value, str):
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(f"{path}: {value!r} does not match {schema['pattern']}")
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{path}: shorter than {schema['minLength']}")
        if "maxLength" in schema and len(value) > schema["maxLength"]:
            errors.append(f"{path}: longer than {schema['maxLength']}")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{path}: below minimum {schema['minimum']}")
        if "maximum" in schema and value > schema["maximum"]:
            errors.append(f"{path}: above maximum {schema['maximum']}")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path}: fewer than {schema['minItems']} items")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errors.append(f"{path}: more than {schema['maxItems']} items")
        if schema.get("uniqueItems") and len({json.dumps(v, sort_keys=True) for v in value}) != len(value):
            errors.append(f"{path}: items are not unique")
        if "items" in schema:
            for i, item in enumerate(value):
                errors += check(item, schema["items"], root, f"{path}[{i}]")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}: missing {key}")
        props = schema.get("properties", {})
        for key, sub in value.items():
            if key in props:
                errors += check(sub, props[key], root, f"{path}.{key}")
            elif schema.get("additionalProperties") is False:
                errors.append(f"{path}: unknown key {key}")
    return errors


def validate(value, name: str, definition: str | None = None) -> list:
    """Validate against <name>.schema.json, or against its $defs.<definition>."""
    root = load(name)
    schema = root["$defs"][definition] if definition else root
    return check(value, schema, root)
