"""Provide coverage audit support for the standalone verification harness."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .inventory import discover_all_function_symbols


def _coverage_file(files: dict[str, Any], toolkit_root: Path, module: str) -> dict[str, Any] | None:
    """Locate the coverage entry for a module within a coverage ``files`` mapping.

    Tries the relative ``src`` path, the absolute path, and the resolved absolute path, then falls
    back to matching any key that ends with the normalized relative path.

    Args:
        files: Mapping of file path to per-file coverage data from a coverage.py JSON report.
        toolkit_root: Root directory used to build absolute path candidates.
        module: Dotted module name to resolve to a source file.

    Returns:
        The coverage data for the module, or ``None`` if no matching file is present.
    """
    relative = "src/" + module.replace(".", "/") + ".py"
    candidates = [relative, str(toolkit_root / relative), str((toolkit_root / relative).resolve())]
    for candidate in candidates:
        if candidate in files:
            return files[candidate]
    normalized = relative.replace("\\", "/")
    for key, value in files.items():
        if key.replace("\\", "/").endswith(normalized):
            return value
    return None


def audit_public_symbol_execution(toolkit_root: Path, coverage_json: Path) -> dict[str, Any]:
    """Check that every discovered function symbol executed at least one line under coverage.

    Classes and enums must have their declaration line covered on import; functions and methods
    must have at least one body line covered.

    Args:
        toolkit_root: Root directory whose source symbols are enumerated.
        coverage_json: Path to a coverage.py JSON report.

    Returns:
        An audit dictionary reporting the symbol counts, the identifiers of any unexecuted
        symbols, overall pass/fail, and line/branch coverage totals.
    """
    payload = json.loads(coverage_json.read_text(encoding="utf-8"))
    files = payload.get("files", {})
    symbols = discover_all_function_symbols(toolkit_root)
    results: list[dict[str, Any]] = []
    missing: list[str] = []
    for symbol in symbols:
        coverage = _coverage_file(files, toolkit_root, symbol.module)
        executed = set(coverage.get("executed_lines", [])) if coverage else set()
        # Classes/enums are declarations rather than callable bodies. Their declaration
        # must execute on import. Functions/methods must execute one direct body line.
        required_lines = set(symbol.body_lines or (symbol.line,))
        covered_lines = sorted(required_lines & executed)
        passed = bool(covered_lines)
        record = {
            **symbol.to_dict(),
            "passed": passed,
            "covered_lines": covered_lines,
            "coverage_file_found": coverage is not None,
        }
        results.append(record)
        if not passed:
            missing.append(symbol.symbol_id)
    totals = payload.get("totals", {})
    return {
        "schema_version": 1,
        "function_symbol_count": len(results),
        "executed_function_symbol_count": len(results) - len(missing),
        "missing_function_symbols": missing,
        "public_symbol_count": len(results),
        "executed_public_symbol_count": len(results) - len(missing),
        "missing_public_symbols": missing,
        "passed": not missing,
        "line_percent": float(totals.get("percent_statements_covered", totals.get("percent_covered", 0.0))),
        "branch_count": int(totals.get("num_branches", 0)),
        "covered_branch_count": int(totals.get("covered_branches", 0)),
        "symbols": results,
    }
