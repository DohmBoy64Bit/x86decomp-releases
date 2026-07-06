#!/usr/bin/env python3
"""Validate the complete current package, example, skill, and release contracts."""
from __future__ import annotations

import json
import re
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
CURRENT_VERSION = "0.7.10"


def load(path: Path):
    """Load load for the current toolkit workflow."""
    return json.loads(path.read_text(encoding="utf-8"))


def validate_schema_files() -> None:
    """Validate schema files for the current toolkit workflow."""
    for path in sorted(SCHEMAS.rglob("*.json")):
        Draft202012Validator.check_schema(load(path))


def validate_examples() -> None:
    """Validate examples for the current toolkit workflow."""
    pairs = [
        (ROOT / "examples/compiler-profiles/gcc-i686-object.json", SCHEMAS / "compiler-profile.schema.json"),
        (ROOT / "examples/validators/add_stack_harness.json", SCHEMAS / "execution-harness.schema.json"),
        (ROOT / "examples/abi/stdcall-two-ints.json", SCHEMAS / "abi-contract.schema.json"),
        (ROOT / "examples/labs/gcc-optimization-matrix.json", SCHEMAS / "compiler-lab.schema.json"),
        (ROOT / "examples/benchmarks/bounded-demo.json", SCHEMAS / "benchmark-corpus.schema.json"),
        (ROOT / "examples/relink/lld-link-x64.json", SCHEMAS / "relink-manifest.schema.json"),
        (ROOT / "examples/integration/bounded-demo.json", SCHEMAS / "integration-scenarios.schema.json"),
        (ROOT / "examples/symbolic/symbolic-alias-harness.json", SCHEMAS / "symbolic-memory-harness.schema.json"),
        (ROOT / "examples/test-bundle/x86decomp-test-bundle.json", SCHEMAS / "test-bundle.schema.json"),
        (ROOT / "examples/release/target-decisions.json", SCHEMAS / "target-decisions.schema.json"),
        (ROOT / "examples/local-llm/lm-studio-profile.json", SCHEMAS / "local-llm/profile.schema.json"),
        (ROOT / "examples/local-llm/ollama-profile.json", SCHEMAS / "local-llm/profile.schema.json"),
        (ROOT / "examples/local-llm/add-two-ints-job.json", SCHEMAS / "local-llm/job.schema.json"),
    ]
    for document_path, schema_path in pairs:
        Draft202012Validator(load(schema_path)).validate(load(document_path))


def validate_java_syntax() -> None:
    """Validate java syntax for the current toolkit workflow."""
    import javalang

    for path in sorted((ROOT / "ghidra_scripts").glob("*.java")):
        javalang.parse.parse(path.read_text(encoding="utf-8"))


def validate_skill_frontmatter() -> None:
    """Validate skill frontmatter for the current toolkit workflow."""
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
    if metadata["version"] != "7.5.0":
        raise ValueError("skill version must match the current operating contract")
    details = metadata["metadata"]
    expected = {
        "release_contract": CURRENT_VERSION,
        "unified_release": True,
        "toolkit_entry_point": "x86decomp",
        "test_suite_entry_point": "x86decomp-test",
        "modes": ["matching", "functional"],
        "architectures": ["x86", "x86_64"],
        "canonical_group_count": 59,
        "canonical_route_count": 239,
        "source_tree_upgrade_subsystem": False,
        "no_placeholder_policy": True,
    }
    for key, value in expected.items():
        if details.get(key) != value:
            raise ValueError(f"skill metadata {key} must be {value!r}")


def validate_current_release_shape() -> None:
    """Validate current release shape for the current toolkit workflow."""
    import tomllib

    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    suite = tomllib.loads((ROOT / "test-suite/pyproject.toml").read_text(encoding="utf-8"))
    if project["project"]["version"] != CURRENT_VERSION or suite["project"]["version"] != CURRENT_VERSION:
        raise ValueError("toolkit and test-suite versions must match 0.7.10")
    if project["project"].get("scripts") != {"x86decomp": "x86decomp.cli:main"}:
        raise ValueError("x86decomp must be the only toolkit executable")
    if suite["project"].get("scripts") != {"x86decomp-test": "x86decomp_testkit.cli:main"}:
        raise ValueError("x86decomp-test must be the only test-suite executable")

    forbidden_names = []
    for path in ROOT.rglob("*"):
        if any(part in {".pytest_cache", "__pycache__", "build", "dist", ".x86decomp-test-tools"} for part in path.parts):
            continue
        lowered = path.name.lower()
        if "upgrade_report" in lowered or re.search(r"(?:^|[-_.])v(?:0?[0-7][0-9]?|07[0-3])(?:[-_.]|$)", lowered):
            forbidden_names.append(path.relative_to(ROOT).as_posix())
    if forbidden_names:
        raise ValueError("forbidden release-specific paths: " + ", ".join(sorted(forbidden_names)))


def main() -> None:
    """Run the command-line entry point and return its process status."""
    validate_schema_files()
    validate_examples()
    validate_java_syntax()
    validate_skill_frontmatter()
    validate_current_release_shape()
    print("current contracts, examples, Java syntax, schemas, skill, and release shape passed")


if __name__ == "__main__":
    main()
