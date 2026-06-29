from __future__ import annotations

import argparse
import ast
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class PublicSymbol:
    module: str
    qualname: str
    kind: str
    line: int
    body_lines: tuple[int, ...]

    @property
    def symbol_id(self) -> str:
        return f"{self.module}:{self.qualname}"

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.symbol_id,
            "module": self.module,
            "qualname": self.qualname,
            "kind": self.kind,
            "line": self.line,
            "body_lines": list(self.body_lines),
        }


def _direct_body_lines(node: ast.FunctionDef | ast.AsyncFunctionDef) -> tuple[int, ...]:
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


def discover_public_symbols(toolkit_root: Path) -> list[PublicSymbol]:
    package = toolkit_root / "src" / "x86decomp"
    if not package.is_dir():
        raise FileNotFoundError(f"toolkit package not found: {package}")
    symbols: list[PublicSymbol] = []
    for path in sorted(package.glob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        module = f"x86decomp.{path.stem}"
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and not node.name.startswith("_"):
                symbols.append(PublicSymbol(module, node.name, "function", node.lineno, _direct_body_lines(node)))
            elif isinstance(node, ast.ClassDef) and not node.name.startswith("_"):
                symbols.append(PublicSymbol(module, node.name, "class", node.lineno, (node.lineno,)))
                for member in node.body:
                    if isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef)) and not member.name.startswith("_"):
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



def discover_all_function_symbols(toolkit_root: Path) -> list[PublicSymbol]:
    package = toolkit_root / "src" / "x86decomp"
    if not package.is_dir():
        raise FileNotFoundError(f"toolkit package not found: {package}")
    symbols: list[PublicSymbol] = []
    for path in sorted(package.glob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        module = f"x86decomp.{path.stem}"
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                symbols.append(PublicSymbol(module, node.name, "function", node.lineno, _direct_body_lines(node)))
            elif isinstance(node, ast.ClassDef):
                for member in node.body:
                    if isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        symbols.append(PublicSymbol(module, f"{node.name}.{member.name}", "method", member.lineno, _direct_body_lines(member)))
    return symbols

def discover_modules(toolkit_root: Path) -> list[str]:
    package = toolkit_root / "src" / "x86decomp"
    return [f"x86decomp.{path.stem}" for path in sorted(package.glob("*.py")) if path.name != "__pycache__"]


def discover_schemas(toolkit_root: Path) -> list[str]:
    directory = toolkit_root / "schemas"
    return [path.name for path in sorted(directory.glob("*.schema.json"))]


def discover_ghidra_scripts(toolkit_root: Path) -> list[str]:
    directory = toolkit_root / "ghidra_scripts"
    return [path.name for path in sorted(directory.glob("*.java"))]


def discover_cli_commands(toolkit_root: Path, python_executable: str = sys.executable) -> list[str]:
    environment = {**__import__("os").environ, "PYTHONPATH": str(toolkit_root / "src")}
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
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("feature catalog must be an object")
    return data


def audit_catalog(inventory: dict[str, Any], catalog: dict[str, Any]) -> dict[str, Any]:
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
    return {
        "passed": not any(
            (
                discovered_commands - catalog_commands,
                catalog_commands - discovered_commands,
                discovered_modules - catalog_modules,
                catalog_modules - discovered_modules,
                discovered_schemas - catalog_schemas,
                catalog_schemas - discovered_schemas,
                discovered_ghidra - catalog_ghidra,
                catalog_ghidra - discovered_ghidra,
                discovered_functions - catalog_functions,
                catalog_functions - discovered_functions,
            )
        ),
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
