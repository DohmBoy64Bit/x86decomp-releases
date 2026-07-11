#!/usr/bin/env python3
"""Verify that packaged self-tests match their canonical checkout tests."""
from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
PAIR_NAMES = (
    "test_adapter_capabilities.py",
    "test_adapter_detection_resolution.py",
    "test_archive_security.py",
    "test_cli_and_installation.py",
    "test_config_models.py",
    "test_inventory_reports_process.py",
)


class _DocstringStripper(ast.NodeTransformer):
    """Remove docstring expressions before comparing executable test structure."""

    @staticmethod
    def _without_docstring(body: list[ast.stmt]) -> list[ast.stmt]:
        """Return a statement list with its leading docstring expression removed."""
        if body and isinstance(body[0], ast.Expr):
            value = body[0].value
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                return body[1:]
        return body

    def visit_Module(self, node: ast.Module) -> ast.AST:
        """Strip the module docstring and recurse into child definitions."""
        node.body = self._without_docstring(node.body)
        return self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> ast.AST:
        """Strip a class docstring and recurse into methods."""
        node.body = self._without_docstring(node.body)
        return self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
        """Strip a function docstring and recurse into nested definitions."""
        node.body = self._without_docstring(node.body)
        return self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> ast.AST:
        """Strip an async-function docstring and recurse into nested definitions."""
        node.body = self._without_docstring(node.body)
        return self.generic_visit(node)


def normalized_ast(path: Path) -> str:
    """Return a location-independent AST dump for executable test behavior."""
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    stripped = _DocstringStripper().visit(tree)
    ast.fix_missing_locations(stripped)
    return ast.dump(stripped, annotate_fields=True, include_attributes=False)


def verify(root: Path = ROOT) -> dict[str, object]:
    """Compare all canonical and packaged self-test pairs by normalized AST."""
    root = root.resolve()
    records: list[dict[str, object]] = []
    failures: list[str] = []
    for name in PAIR_NAMES:
        canonical = root / "test-suite" / "tests" / name
        packaged = root / "test-suite" / "src" / "x86decomp_testkit" / "self_tests" / name
        missing = [str(path.relative_to(root)) for path in (canonical, packaged) if not path.is_file()]
        if missing:
            failures.append(f"missing test copy: {', '.join(missing)}")
            records.append({"name": name, "synchronized": False, "missing": missing})
            continue
        canonical_ast = normalized_ast(canonical)
        packaged_ast = normalized_ast(packaged)
        synchronized = canonical_ast == packaged_ast
        if not synchronized:
            failures.append(f"normalized AST mismatch: {name}")
        records.append(
            {
                "name": name,
                "canonical": canonical.relative_to(root).as_posix(),
                "packaged": packaged.relative_to(root).as_posix(),
                "synchronized": synchronized,
            }
        )
    return {
        "schema_version": 1,
        "pair_count": len(PAIR_NAMES),
        "synchronized_count": sum(bool(record.get("synchronized")) for record in records),
        "valid": not failures,
        "failures": failures,
        "pairs": records,
    }


def main(argv: Iterable[str] | None = None) -> int:
    """Run the synchronization check and print its machine-readable result."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(list(argv) if argv is not None else None)
    result = verify(args.root)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
