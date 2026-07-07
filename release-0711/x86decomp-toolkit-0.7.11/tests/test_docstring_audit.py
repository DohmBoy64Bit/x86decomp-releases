"""Regression tests for complete 0.7.11 docstring coverage."""
from __future__ import annotations

import ast
import json
from pathlib import Path

from x86decomp.canonical import canonical_groups, canonical_routes
from x86decomp.cli import _build_parser

ROOT = Path(__file__).resolve().parents[1]
PYTHON_ROOTS = (
    ROOT / "src",
    ROOT / "tests",
    ROOT / "test-suite" / "src",
    ROOT / "test-suite" / "tests",
    ROOT / "scripts",
    ROOT / "ghidra_scripts",
)
IGNORED_PARTS = {"build", "dist", ".pytest_cache", "__pycache__"}


def _python_files() -> list[Path]:
    """Return editable Python files covered by the release docstring audit."""
    files: list[Path] = []
    for base in PYTHON_ROOTS:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.py")):
            if any(part in IGNORED_PARTS for part in path.relative_to(ROOT).parts):
                continue
            files.append(path)
    return files


def test_every_python_symbol_has_a_docstring() -> None:
    """Verify every audited module, class, function, and method has a docstring."""
    missing: list[str] = []
    for path in _python_files():
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path.relative_to(ROOT)))
        if ast.get_docstring(tree) is None:
            missing.append(f"{path.relative_to(ROOT)}:<module>")
        for node in ast.walk(tree):
            if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                if ast.get_docstring(node) is None:
                    missing.append(f"{path.relative_to(ROOT)}:{node.lineno}:{node.name}")
    assert not missing


def test_docstring_audit_report_matches_current_release() -> None:
    """Verify the persisted docstring audit report records complete coverage."""
    report = json.loads((ROOT / "DOCSTRING_AUDIT_0.7.11.json").read_text(encoding="utf-8"))
    assert report["release"] == "0.7.11"
    assert report["missing_docstrings"] == []
    coverage = report["python_docstring_coverage"]
    assert coverage["modules_total"] == coverage["modules_with_docstrings"]
    assert coverage["classes_total"] == coverage["classes_with_docstrings"]
    assert coverage["functions_total"] == coverage["functions_with_docstrings"]


def test_command_reference_matches_canonical_surface() -> None:
    """Verify the command reference remains synchronized with the live command surface."""
    reference = json.loads((ROOT / "docs" / "COMMAND_REFERENCE_0.7.11.json").read_text(encoding="utf-8"))
    parser = _build_parser()
    root_action = next(action for action in parser._actions if getattr(action, "choices", None))
    assert reference["root_command_count"] == len(root_action.choices)
    assert reference["canonical_group_count"] == len(canonical_groups())
    assert reference["canonical_route_count"] == len(canonical_routes())
