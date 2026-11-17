"""A small JSON Schema validator (standard library only) for the diagram spec.

Supports the subset the book's schemas use: type, enum, const, required, properties,
additionalProperties (false or schema), items, minItems, maxItems, minLength, maxLength, pattern,
minimum, maximum, $ref to "#/..." pointers, allOf, anyOf and oneOf. For a oneOf whose branches
carry properties.kind.const, the branch is chosen by the instance's "kind", so errors stay precise.
"""
from __future__ import annotations

import re

from .. import common

_TYPES = {
    "object": dict, "array": list, "string": str, "boolean": bool, "null": type(None),
}


def schema_path():
    return common.SCHEMA_DIR / "diagram.schema.json"


def load_schema() -> dict:
    schema = common.read_json(schema_path())
    if schema is None:
        # a sandbox --book-dir may not carry the schema; fall back to the real book
        schema = common.read_json(common.REAL_BOOK / "_build" / "schemas" / "diagram.schema.json")
    if schema is None:
        raise SystemExit(common.fail("diagram.schema.json not found", common.EXIT_PRECONDITION))
    return schema


def _type_ok(value, name: str) -> bool:
    if name == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if name == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return isinstance(value, _TYPES[name])


def _resolve(root: dict, ref: str) -> dict:
    if not ref.startswith("#/"):
        raise ValueError(f"unsupported $ref {ref!r}")
    node = root
    for part in ref[2:].split("/"):
        node = node[part.replace("~1", "/").replace("~0", "~")]
    return node


def _kind_const(root: dict, branch: dict):
    while "$ref" in branch:
        branch = _resolve(root, branch["$ref"])
    return branch.get("properties", {}).get("kind", {}).get("const")


def validate(instance, schema: dict = None, root: dict = None, path: str = "$") -> list:
    """Return a list of error strings; empty means valid."""
    if schema is None:
        schema = load_schema()
    if root is None:
        root = schema
    errors = []
    if "$ref" in schema:
        errors += validate(instance, _resolve(root, schema["$ref"]), root, path)
    if "type" in schema:
        names = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(_type_ok(instance, n) for n in names):
            return errors + [f"{path}: expected {' or '.join(names)}, got {type(instance).__name__}"]
    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: must be {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: {instance!r} is not one of {schema['enum']}")
    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            errors.append(f"{path}: shorter than {schema['minLength']} characters")
        if "maxLength" in schema and len(instance) > schema["maxLength"]:
            errors.append(f"{path}: longer than {schema['maxLength']} characters")
        if "pattern" in schema and not re.search(schema["pattern"], instance):
            errors.append(f"{path}: {instance!r} does not match {schema['pattern']}")
    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            errors.append(f"{path}: below the minimum {schema['minimum']}")
        if "maximum" in schema and instance > schema["maximum"]:
            errors.append(f"{path}: above the maximum {schema['maximum']}")
    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            errors.append(f"{path}: fewer than {schema['minItems']} items")
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            errors.append(f"{path}: more than {schema['maxItems']} items")
        if "items" in schema:
            for i, item in enumerate(instance):
                errors += validate(item, schema["items"], root, f"{path}[{i}]")
    if isinstance(instance, dict):
        props = schema.get("properties", {})
        for key in schema.get("required", []):
            if key not in instance:
                errors.append(f"{path}: missing required property {key!r}")
        for key, value in instance.items():
            if key in props:
                errors += validate(value, props[key], root, f"{path}.{key}")
            elif "additionalProperties" in schema:
                extra = schema["additionalProperties"]
                if extra is False:
                    errors.append(f"{path}: unknown property {key!r}")
                elif isinstance(extra, dict):
                    errors += validate(value, extra, root, f"{path}.{key}")
    for sub in schema.get("allOf", []):
        errors += validate(instance, sub, root, path)
    if "anyOf" in schema:
        results = [validate(instance, sub, root, path) for sub in schema["anyOf"]]
        if not any(not r for r in results):
            errors += min(results, key=len)
    if "oneOf" in schema:
        branches = schema["oneOf"]
        kinds = [_kind_const(root, b) for b in branches]
        if isinstance(instance, dict) and all(kinds):
            kind = instance.get("kind")
            if kind in kinds:
                errors += validate(instance, branches[kinds.index(kind)], root, path)
            elif not errors:
                errors.append(f"{path}: kind {kind!r} is not supported yet (supported: {', '.join(kinds)})")
        else:
            results = [validate(instance, sub, root, path) for sub in branches]
            passed = sum(1 for r in results if not r)
            if passed == 0:
                errors += min(results, key=len)
            elif passed > 1:
                errors.append(f"{path}: matches more than one alternative")
    return errors
