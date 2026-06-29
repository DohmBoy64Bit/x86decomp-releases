#!/usr/bin/env python3
"""Validate package JSON/YAML-independent contracts and representative examples."""
from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate_schema_files() -> None:
    for path in sorted(SCHEMAS.glob("*.json")):
        schema = load(path)
        Draft202012Validator.check_schema(schema)


def validate_examples() -> None:
    pairs = [
        (ROOT / "examples/compiler-profiles/gcc-i686-object.json", SCHEMAS / "compiler-profile.schema.json"),
        (ROOT / "examples/validators/add_stack_harness.json", SCHEMAS / "execution-harness.schema.json"),
        (ROOT / "examples/abi/stdcall-two-ints.json", SCHEMAS / "abi-contract.schema.json"),
        (ROOT / "examples/labs/gcc-optimization-matrix.json", SCHEMAS / "compiler-lab.schema.json"),
        (ROOT / "examples/benchmarks/bounded-demo.json", SCHEMAS / "benchmark-corpus.schema.json"),
        (ROOT / "examples/relink/lld-link-x64.json", SCHEMAS / "relink-manifest.schema.json"),
        (ROOT / "examples/integration/bounded-demo.json", SCHEMAS / "integration-scenarios.schema.json"),
        (ROOT / "examples/v0.3/symbolic-alias-harness.json", SCHEMAS / "symbolic-memory-harness.schema.json"),
        (ROOT / "examples/test-bundle/x86decomp-test-bundle.json", SCHEMAS / "test-bundle.schema.json"),
        (ROOT / "examples/v0.4/target-decisions.json", SCHEMAS / "target-decisions.schema.json"),
    ]
    for document_path, schema_path in pairs:
        Draft202012Validator(load(schema_path)).validate(load(document_path))


def validate_java_syntax() -> None:
    import javalang
    for path in sorted((ROOT / "ghidra_scripts").glob("*.java")):
        javalang.parse.parse(path.read_text(encoding="utf-8"))



def validate_skill_frontmatter() -> None:
    import yaml

    path = ROOT / "skills" / "x86decomp" / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("skill must begin with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("skill frontmatter is not closed")
    metadata = yaml.safe_load(text[4:end])
    if not isinstance(metadata, dict):
        raise ValueError("skill frontmatter must be a mapping")
    for key in ("name", "description", "version", "license", "compatibility", "metadata", "tags"):
        if key not in metadata:
            raise ValueError(f"skill frontmatter is missing {key}")
    if metadata["version"] != "4.0.0":
        raise ValueError("skill version must match the 4.0.0 operating contract")
    modes = metadata.get("metadata", {}).get("modes")
    if modes != ["matching", "functional"]:
        raise ValueError("skill frontmatter must declare matching and functional modes")
    architectures = metadata.get("metadata", {}).get("architectures")
    if architectures != ["x86", "x86_64"]:
        raise ValueError("skill frontmatter must declare x86 and x86_64")
    if metadata.get("metadata", {}).get("release_contract") != "0.4.0":
        raise ValueError("skill release_contract must match package 0.4.0")


def main() -> None:
    validate_schema_files()
    validate_examples()
    validate_java_syntax()
    validate_skill_frontmatter()
    print("contract, example, Java syntax, and skill frontmatter validation passed")


if __name__ == "__main__":
    main()
