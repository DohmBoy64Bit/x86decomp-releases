---
title: tests/test_release_contract.py
description: Test source page for tests/test_release_contract.py.
---

# `tests/test_release_contract.py`

- SHA-256: `7995c16cc519ee1cdf6dd7fb7645cdc6642515da64bd43c4a57951437e17d6fa`
- Size: `10268` bytes
- Test functions: `9`

```python
"""Verify the current toolkit behavior covered by `tests/test_release_contract.py`."""
from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

import x86decomp
from x86decomp.canonical import canonical_groups, canonical_routes
from x86decomp.cli import _build_parser

ROOT = Path(__file__).resolve().parents[1]


def _commands() -> set[str]:
    """Support commands processing for internal toolkit callers."""
    parser = _build_parser()
    action = next(action for action in parser._actions if getattr(action, "choices", None))
    return set(action.choices)


def test_current_command_and_schema_contract() -> None:
    """Verify current command and schema contract behavior."""
    contract = json.loads((ROOT / "examples/contracts/command-surface.json").read_text())
    assert set(contract["commands"]).issubset(_commands())
    assert all((ROOT / "schemas" / name).is_file() for name in contract["schema_files"])
    assert len(canonical_groups()) == 59
    assert len(canonical_routes()) == 239


def test_schema_project_and_function_documents_remain_valid() -> None:
    """Verify schema project and function documents remain valid behavior."""
    project_schema = json.loads((ROOT / "schemas/project.schema.json").read_text())
    function_schema = json.loads((ROOT / "schemas/function.schema.json").read_text())
    project_document = {
        "schema_version": 1,
        "project_id": "x86d-0123456789abcdef-01234567",
        "created_at": "2026-06-28T00:00:00Z",
        "supported_scope": "native Windows PE32 x86",
        "binary": {"name": "target.exe", "source_kind": "copied", "path": "original/target.exe", "sha256": "0" * 64, "size": 1},
        "program_manifest": "analysis/program.json",
        "memory_ledger": "memory/events.jsonl",
        "function_root": "functions",
        "evidence_root": "evidence",
        "status": "initialized",
    }
    function_document = {
        "schema_version": 1, "id": "pe-rva:00001234", "entry": "00401234", "entry_rva": 0x1234,
        "name": "FUN_00401234", "name_source": "DEFAULT", "calling_convention": None,
        "signature": "undefined FUN_00401234(void)", "return_type": "undefined",
        "body_ranges": [{"start": "00401234", "end_inclusive": "00401234", "start_rva": 0x1234, "end_rva": 0x1235, "size": 1, "file": "ranges/0000.bin"}],
        "parameters": [],
    }
    Draft202012Validator(project_schema).validate(project_document)
    Draft202012Validator(function_schema).validate(function_document)


def test_ground_truth_sources_are_packaged_and_in_sync() -> None:
    """Verify ground truth sources are packaged and in sync behavior."""
    repository_sources = ROOT / "corpus/ground_truth_sources"
    package_sources = ROOT / "src/x86decomp/corpus/ground_truth_sources"
    repository = {path.name: path.read_bytes() for path in repository_sources.iterdir() if path.is_file()}
    packaged = {path.name: path.read_bytes() for path in package_sources.iterdir() if path.is_file()}
    assert packaged == repository
    assert len(packaged) == 24


def test_current_public_surface_contract() -> None:
    """Verify current public surface contract behavior."""
    contract = json.loads((ROOT / "examples/contracts/public-surface.json").read_text())
    assert set(contract["commands"]).issubset(_commands())
    assert all((ROOT / "schemas" / name).is_file() for name in contract["schema_files"])
    assert all((ROOT / "ghidra_scripts" / name).is_file() for name in contract["ghidra_scripts"])
    package_modules = set()
    for path in (ROOT / "src/x86decomp").rglob("*.py"):
        relative = path.relative_to(ROOT / "src/x86decomp").with_suffix("")
        parts = list(relative.parts)
        if parts[-1] == "__init__":
            parts.pop()
        package_modules.add(".".join(("x86decomp", *parts)) if parts else "x86decomp")
    assert set(contract["modules"]).issubset(package_modules)
    from x86decomp_testkit.adapters import adapter_catalog
    assert set(contract["adapter_ids"]).issubset(set(adapter_catalog()))
    assert x86decomp.__version__ == "0.7.11"


def test_exact_recursive_feature_catalog_matches_current_tree() -> None:
    """Verify exact recursive feature catalog matches current tree behavior."""
    from x86decomp_testkit.inventory import audit_catalog, build_inventory

    catalog = json.loads(
        (ROOT / "test-suite/src/x86decomp_testkit/data/feature_catalog.json").read_text(encoding="utf-8")
    )
    audit = audit_catalog(build_inventory(ROOT), catalog)
    assert audit["passed"], audit
    assert catalog["toolkit_version"] == "0.7.11"
    assert catalog["entry_points"] == {"toolkit": "x86decomp", "test_suite": "x86decomp-test"}
    assert "compatibility_baseline" not in catalog


def test_repository_contains_only_the_current_release_contract() -> None:
    """Verify repository contains only the current release contract behavior."""
    import re
    import tomllib

    prior_release_parts = (
        (0, 1, 0), (0, 2, 0), (0, 3, 0), (0, 3, 1), (0, 4, 0), (0, 5, 0),
        (0, 6, 0), (0, 7, 0), (0, 7, 1), (0, 7, 2), (0, 7, 3), (0, 7, 4),
    )
    prior_versions = tuple(".".join(str(part) for part in release) for release in prior_release_parts)
    prior_compact = tuple(f"v{major}{minor}{patch}" for major, minor, patch in prior_release_parts)
    old_tokens = prior_versions + tuple("v" + version for version in prior_versions) + prior_compact
    checked_suffixes = {".py", ".json", ".md", ".txt", ".toml", ".in", ".yml", ".yaml", ".cfg", ".sh"}
    violations: list[str] = []
    forbidden_paths: list[str] = []
    ignored_parts = {".pytest_cache", "__pycache__", "build", "dist", ".git", ".x86decomp-test-tools", "test-results"}
    for path in ROOT.rglob("*"):
        if any(part in ignored_parts or part.endswith(".egg-info") for part in path.parts):
            continue
        relative = path.relative_to(ROOT).as_posix()
        lowered = relative.lower()
        if path.is_dir() and re.search(r"(?:^|/)v(?:0?[0-7][0-9]?|07[0-3])(?:/|$)", lowered):
            forbidden_paths.append(relative)
        if path.is_file() and (
            "upgrade_report" in path.name.lower()
            or re.search(r"(?:^|[-_.])(?:apply|build)-.*(?:upgrade|overlay)", path.name.lower())
        ):
            forbidden_paths.append(relative)
        if not path.is_file() or (path.suffix.lower() not in checked_suffixes and path.name not in {"Makefile"}):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for token in old_tokens:
            if re.search(rf"(?<![0-9A-Za-z.]){re.escape(token)}(?![0-9A-Za-z.])", text):
                violations.append(f"{relative}: {token}")
    assert not forbidden_paths, forbidden_paths
    assert not violations, violations

    toolkit = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]
    suite = tomllib.loads((ROOT / "test-suite/pyproject.toml").read_text(encoding="utf-8"))["project"]
    assert toolkit["version"] == suite["version"] == "0.7.11"
    assert toolkit["scripts"] == {"x86decomp": "x86decomp.cli:main"}
    assert suite["scripts"] == {"x86decomp-test": "x86decomp_testkit.cli:main"}
    assert "upgrade" not in _commands()
    assert "compatibility-status" not in _commands()


def test_no_placeholder_implementations_in_current_python_sources() -> None:
    """Verify no placeholder implementations in current python sources behavior."""
    import ast

    findings: list[str] = []
    for base in (ROOT / "src", ROOT / "test-suite/src"):
        for path in base.rglob("*.py"):
            if "__pycache__" in path.parts:
                continue
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    body = [item for item in node.body if not (
                        isinstance(item, ast.Expr)
                        and isinstance(item.value, ast.Constant)
                        and isinstance(item.value.value, str)
                    )]
                    if len(body) == 1 and isinstance(body[0], ast.Pass):
                        findings.append(f"{path.relative_to(ROOT)}:{node.lineno}:{node.name}:pass")
                    if len(body) == 1 and isinstance(body[0], ast.Raise):
                        call = body[0].exc
                        if isinstance(call, ast.Call) and getattr(call.func, "id", None) == "NotImplementedError":
                            findings.append(f"{path.relative_to(ROOT)}:{node.lineno}:{node.name}:NotImplementedError")
    assert not findings, findings


def test_deterministic_source_hash_tool_detects_drift(tmp_path: Path) -> None:
    """Verify deterministic source hash tool detects drift behavior."""
    import importlib.util

    script = ROOT / "scripts/source_hashes.py"
    spec = importlib.util.spec_from_file_location("source_hashes", script)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    (tmp_path / "test-suite").mkdir()
    (tmp_path / "current.txt").write_text("current\n", encoding="utf-8")
    (tmp_path / "test-suite/current.txt").write_text("suite\n", encoding="utf-8")
    module.generate_all(tmp_path)
    assert module.verify_all(tmp_path)["valid"]
    (tmp_path / "PKG-INFO").write_text("generated package metadata\n", encoding="utf-8")
    assert module.verify_all(tmp_path)["valid"]
    (tmp_path / "current.txt").write_text("changed\n", encoding="utf-8")
    result = module.verify_all(tmp_path)
    assert not result["valid"]
    assert "hash mismatch: current.txt" in result["root"]["failures"]


def test_flat_compatibility_aliases_are_explicit() -> None:
    """Verify retained flat commands are marked as compatibility aliases."""
    parser = _build_parser()
    action = next(action for action in parser._actions if getattr(action, "choices", None))
    assert action.choices["hybrid-generate"].get_default("_compatibility_alias") == "hybrid generate"
    assert action.choices["project-check"].get_default("_compatibility_alias") == "project check"
```
