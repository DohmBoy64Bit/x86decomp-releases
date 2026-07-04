#!/usr/bin/env python3
"""Synchronize exact current release inventories from the live source tree."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "test-suite" / "src"))

from x86decomp.canonical import canonical_groups, canonical_routes  # noqa: E402
from x86decomp.cli import _build_parser  # noqa: E402
from x86decomp_testkit.adapters import adapter_catalog  # noqa: E402
from x86decomp_testkit.inventory import build_inventory  # noqa: E402

VERSION = "0.7.5"


def write(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def root_commands() -> list[str]:
    parser = _build_parser()
    action = next(action for action in parser._actions if getattr(action, "choices", None))
    return sorted(action.choices)


def module_area(name: str) -> str:
    if name.startswith("x86decomp.assembly"):
        return "assembly"
    if name.startswith("x86decomp.governance"):
        return "governance"
    if name.startswith("x86decomp.native"):
        return "native"
    if name.startswith("x86decomp.reconstruction"):
        return "reconstruction"
    if name.startswith("x86decomp.local_llm"):
        return "local-llm"
    return "core"


def main() -> None:
    inventory = build_inventory(ROOT)
    commands = root_commands()
    groups = list(canonical_groups())
    routes = list(canonical_routes())
    adapters = sorted(adapter_catalog())
    schemas = inventory["schemas"]
    modules = inventory["modules"]
    function_ids = sorted(item["id"] for item in inventory["all_function_symbols"])

    catalog_path = ROOT / "test-suite/src/x86decomp_testkit/data/feature_catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    catalog.update(
        {
            "toolkit_version": VERSION,
            "cli_commands": {
                command: {"interface": "x86decomp", "status": "current"}
                for command in commands
            },
            "canonical_groups": groups,
            "canonical_routes": routes,
            "modules": {
                module: {"area": module_area(module), "status": "current"}
                for module in modules
            },
            "all_function_symbols": function_ids,
            "schemas": schemas,
            "ghidra_scripts": inventory["ghidra_scripts"],
            "adapters": adapters,
        }
    )
    write(catalog_path, catalog)

    command_surface = {
        "release": VERSION,
        "commands": commands,
        "canonical_groups": groups,
        "canonical_route_count": len(routes),
        "schema_files": schemas,
    }
    write(ROOT / "examples/contracts/command-surface.json", command_surface)

    public_surface = {
        "schema_version": 1,
        "toolkit_version": VERSION,
        "purpose": "Exact current unified public surface",
        "entry_points": {"toolkit": "x86decomp", "test_suite": "x86decomp-test"},
        "commands": commands,
        "canonical_groups": groups,
        "canonical_routes": routes,
        "modules": {
            module: {"area": module_area(module), "status": "current"}
            for module in modules
        },
        "schema_files": schemas,
        "ghidra_scripts": inventory["ghidra_scripts"],
        "adapter_ids": adapters,
        "workflow_states": catalog["workflow_states"],
    }
    write(ROOT / "examples/contracts/public-surface.json", public_surface)

    summary = {
        "version": VERSION,
        "root_commands": len(commands),
        "canonical_groups": len(groups),
        "canonical_routes": len(routes),
        "modules": len(modules),
        "functions_and_methods": len(function_ids),
        "schemas": len(schemas),
        "ghidra_scripts": len(inventory["ghidra_scripts"]),
        "adapters": len(adapters),
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
