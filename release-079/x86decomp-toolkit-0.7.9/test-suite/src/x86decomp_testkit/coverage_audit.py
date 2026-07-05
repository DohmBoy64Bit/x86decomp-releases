"""Provide test-suite.x86decomp_testkit.coverage_audit functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .inventory import PublicSymbol, _direct_body_lines, discover_all_function_symbols, discover_public_symbols


def _coverage_file(files: dict[str, Any], toolkit_root: Path, module: str) -> dict[str, Any] | None:
    """Implement coverage file.
    
    Parameters and return values follow the signature and runtime validation in the body.
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
    """Audit public symbol execution.
    
    Parameters and return values follow the signature and runtime validation in the body.
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
