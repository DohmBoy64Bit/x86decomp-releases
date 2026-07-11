"""Provide inventory support for the standalone verification harness."""
from __future__ import annotations

import ast
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class PublicSymbol:
    """Store validated public symbol fields used by toolkit reports and adapters."""
    module: str
    qualname: str
    kind: str
    line: int
    body_lines: tuple[int, ...]

    @property
    def symbol_id(self) -> str:
        """Return the stable ``module:qualname`` identifier for this symbol."""
        return f"{self.module}:{self.qualname}"

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "id": self.symbol_id,
            "module": self.module,
            "qualname": self.qualname,
            "kind": self.kind,
            "line": self.line,
            "body_lines": list(self.body_lines),
        }


def _direct_body_lines(node: ast.FunctionDef | ast.AsyncFunctionDef) -> tuple[int, ...]:
    """Return the line numbers of a function's direct, non-docstring statements.

    Args:
        node: The function definition to inspect.

    Returns:
        A tuple of statement line numbers, excluding a leading string-literal
        docstring statement.
    """
    lines: list[int] = []
    for statement in node.body:
        if (
            isinstance(statement, ast.Expr)
            and isinstance(statement.value, ast.Constant)
            and isinstance(statement.value.value, str)
        ):
            continue
        lines.append(statement.lineno)
    return tuple(lines)


def _python_files(toolkit_root: Path) -> list[Path]:
    """List the toolkit's Python source files under ``src/x86decomp``.

    Args:
        toolkit_root: Root directory of the toolkit checkout.

    Returns:
        A sorted list of ``.py`` paths, excluding ``__pycache__`` entries.

    Raises:
        FileNotFoundError: If the ``src/x86decomp`` package directory is absent.
    """
    package = toolkit_root / "src" / "x86decomp"
    if not package.is_dir():
        raise FileNotFoundError(f"toolkit package not found: {package}")
    return sorted(path for path in package.rglob("*.py") if "__pycache__" not in path.parts)


def _module_name(toolkit_root: Path, path: Path) -> str:
    """Compute the dotted module name for a source file.

    Args:
        toolkit_root: Root directory of the toolkit checkout.
        path: Path to a Python file inside the ``x86decomp`` package.

    Returns:
        The dotted module name, collapsing ``__init__`` to its package name.
    """
    package = toolkit_root / "src" / "x86decomp"
    relative = path.relative_to(package).with_suffix("")
    parts = list(relative.parts)
    if parts[-1] == "__init__":
        parts.pop()
    return ".".join(("x86decomp", *parts)) if parts else "x86decomp"


def _discover_symbols(toolkit_root: Path, *, public_only: bool) -> list[PublicSymbol]:
    """Collect functions, classes, and methods defined across the toolkit.

    Args:
        toolkit_root: Root directory of the toolkit checkout.
        public_only: If true, skip underscore-prefixed names; class symbols are
            emitted only in this mode.

    Returns:
        A list of ``PublicSymbol`` records for the discovered definitions.
    """
    symbols: list[PublicSymbol] = []
    for path in _python_files(toolkit_root):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        module = _module_name(toolkit_root, path)
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if public_only and node.name.startswith("_"):
                    continue
                symbols.append(PublicSymbol(module, node.name, "function", node.lineno, _direct_body_lines(node)))
            elif isinstance(node, ast.ClassDef):
                if public_only and node.name.startswith("_"):
                    continue
                if public_only:
                    symbols.append(PublicSymbol(module, node.name, "class", node.lineno, (node.lineno,)))
                for member in node.body:
                    if not isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        continue
                    if public_only and member.name.startswith("_"):
                        continue
                    symbols.append(
                        PublicSymbol(
                            module,
                            f"{node.name}.{member.name}",
                            "method",
                            member.lineno,
                            _direct_body_lines(member),
                        )
                    )
    return symbols


def discover_public_symbols(toolkit_root: Path) -> list[PublicSymbol]:
    """Return every public function, class, and method in the toolkit.

    Args:
        toolkit_root: Root directory of the toolkit checkout.

    Returns:
        A list of ``PublicSymbol`` records for non-underscore-prefixed names.
    """
    return _discover_symbols(toolkit_root, public_only=True)


def discover_all_function_symbols(toolkit_root: Path) -> list[PublicSymbol]:
    """Return every function and method symbol, public or private.

    Args:
        toolkit_root: Root directory of the toolkit checkout.

    Returns:
        A list of ``PublicSymbol`` records excluding class symbols.
    """
    return [symbol for symbol in _discover_symbols(toolkit_root, public_only=False) if symbol.kind != "class"]


def discover_modules(toolkit_root: Path) -> list[str]:
    """Return the sorted set of dotted module names in the toolkit package.

    Args:
        toolkit_root: Root directory of the toolkit checkout.

    Returns:
        A sorted list of unique module names.
    """
    return sorted({_module_name(toolkit_root, path) for path in _python_files(toolkit_root)})


def discover_schemas(toolkit_root: Path) -> list[str]:
    """List the JSON schema files bundled under the toolkit ``schemas`` tree.

    Args:
        toolkit_root: Root directory of the toolkit checkout.

    Returns:
        A sorted list of ``*.schema.json`` paths relative to ``schemas``.
    """
    directory = toolkit_root / "schemas"
    return [path.relative_to(directory).as_posix() for path in sorted(directory.rglob("*.schema.json"))]


def discover_ghidra_scripts(toolkit_root: Path) -> list[str]:
    """List the Ghidra script file names under ``ghidra_scripts``.

    Args:
        toolkit_root: Root directory of the toolkit checkout.

    Returns:
        A sorted list of ``*.java`` file names.
    """
    directory = toolkit_root / "ghidra_scripts"
    return [path.name for path in sorted(directory.glob("*.java"))]


def discover_cli_commands(toolkit_root: Path, python_executable: str = sys.executable) -> list[str]:
    """Extract the toolkit's CLI subcommand names from ``--help`` output.

    Args:
        toolkit_root: Root directory of the toolkit checkout.
        python_executable: Interpreter used to invoke ``x86decomp --help``.

    Returns:
        A sorted list of the argparse subcommand names.

    Raises:
        RuntimeError: If the help invocation exits non-zero or its output does
            not contain the argparse command set.
    """
    environment = {**os.environ, "PYTHONPATH": str(toolkit_root / "src")}
    completed = subprocess.run(
        [python_executable, "-m", "x86decomp", "--help"],
        cwd=toolkit_root,
        env=environment,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=60,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(f"failed to query CLI commands: {completed.stderr}")
    match = re.search(r"\{([^}]+)\}", completed.stdout)
    if not match:
        raise RuntimeError("could not locate argparse command set in x86decomp --help")
    return sorted({item.strip() for item in match.group(1).split(",") if item.strip()})


def build_inventory(toolkit_root: Path, python_executable: str = sys.executable) -> dict[str, Any]:
    """Assemble a full discovery inventory of the toolkit surface.

    Args:
        toolkit_root: Root directory of the toolkit checkout.
        python_executable: Interpreter used to query CLI commands.

    Returns:
        A mapping describing modules, public and all-function symbols, CLI
        commands, schemas, and Ghidra scripts.
    """
    symbols = discover_public_symbols(toolkit_root)
    all_functions = discover_all_function_symbols(toolkit_root)
    return {
        "schema_version": 1,
        "modules": discover_modules(toolkit_root),
        "public_symbols": [symbol.to_dict() for symbol in symbols],
        "all_function_symbols": [symbol.to_dict() for symbol in all_functions],
        "cli_commands": discover_cli_commands(toolkit_root, python_executable),
        "schemas": discover_schemas(toolkit_root),
        "ghidra_scripts": discover_ghidra_scripts(toolkit_root),
    }


def load_feature_catalog(path: Path) -> dict[str, Any]:
    """Load a feature catalog JSON document from disk.

    Args:
        path: Path to the catalog JSON file.

    Returns:
        The parsed catalog mapping.

    Raises:
        ValueError: If the document does not decode to a JSON object.
    """
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("feature catalog must be an object")
    return data


def audit_catalog(inventory: dict[str, Any], catalog: dict[str, Any]) -> dict[str, Any]:
    """Compare a discovered inventory against a feature catalog.

    Args:
        inventory: The inventory produced by :func:`build_inventory`.
        catalog: The feature catalog to reconcile against.

    Returns:
        A mapping with a ``passed`` flag and, for commands, modules, schemas,
        Ghidra scripts, and function symbols, the sets that are uncataloged or
        stale relative to the discovered inventory.
    """
    catalog_commands = set(catalog.get("cli_commands", {}))
    discovered_commands = set(inventory["cli_commands"])
    catalog_modules = set(catalog.get("modules", {}))
    discovered_modules = set(inventory["modules"])
    catalog_schemas = set(catalog.get("schemas", []))
    discovered_schemas = set(inventory["schemas"])
    catalog_ghidra = set(catalog.get("ghidra_scripts", []))
    discovered_ghidra = set(inventory["ghidra_scripts"])
    catalog_functions = set(catalog.get("all_function_symbols", []))
    discovered_functions = {item["id"] for item in inventory.get("all_function_symbols", [])}
    differences = {
        "uncataloged_commands": sorted(discovered_commands - catalog_commands),
        "stale_commands": sorted(catalog_commands - discovered_commands),
        "uncataloged_modules": sorted(discovered_modules - catalog_modules),
        "stale_modules": sorted(catalog_modules - discovered_modules),
        "uncataloged_schemas": sorted(discovered_schemas - catalog_schemas),
        "stale_schemas": sorted(catalog_schemas - discovered_schemas),
        "uncataloged_ghidra_scripts": sorted(discovered_ghidra - catalog_ghidra),
        "stale_ghidra_scripts": sorted(catalog_ghidra - discovered_ghidra),
        "uncataloged_function_symbols": sorted(discovered_functions - catalog_functions),
        "stale_function_symbols": sorted(catalog_functions - discovered_functions),
    }
    return {"passed": not any(differences.values()), **differences}
