"""Continuously buildable hybrid source-tree generation."""

from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

from .errors import ContractError
from .util import load_json, utc_now, write_json
from .workflow import DecompilationMode, initialize_function_workflow


def _assembly_bytes(symbol: str, code: bytes, architecture: str) -> str:
    directives = [".text", ".code32" if architecture == "x86" else ".code64", f".globl {symbol}", f"{symbol}:"]
    for offset in range(0, len(code), 16):
        chunk = code[offset : offset + 16]
        directives.append("  .byte " + ", ".join(f"0x{value:02x}" for value in chunk))
    directives.append("")
    return "\n".join(directives)


def generate_hybrid_project(
    project_root: Path,
    output_root: Path,
    *,
    architecture: str = "x86",
    overwrite: bool = False,
) -> dict[str, Any]:
    if architecture not in ("x86", "x86_64"):
        raise ContractError("hybrid architecture must be x86 or x86_64")
    project_root = project_root.resolve()
    output_root = output_root.resolve()
    if output_root.exists() and any(output_root.iterdir()):
        if not overwrite:
            raise ContractError(f"hybrid output is not empty: {output_root}")
        shutil.rmtree(output_root)
    for directory in (
        "src/asm", "src/staging", "src/matched", "src/functional", "include", "build", "config", "tests"
    ):
        (output_root / directory).mkdir(parents=True, exist_ok=True)
    function_root = project_root / "functions"
    functions: list[dict[str, Any]] = []
    object_targets: list[str] = []
    if function_root.is_dir():
        for artifact in sorted(path for path in function_root.iterdir() if path.is_dir()):
            manifest_path = artifact / "function.json"
            if not manifest_path.is_file():
                continue
            manifest = load_json(manifest_path)
            function_id = str(manifest["id"])
            rva = int(manifest["entry_rva"])
            symbol = f"sub_{rva:08x}"
            range_records = manifest.get("body_ranges", [])
            if not range_records:
                raise ContractError(f"function artifact has no body ranges: {artifact}")
            code = b"".join((artifact / str(record["file"])).read_bytes() for record in range_records)
            assembly_path = output_root / "src" / "asm" / f"{symbol}.S"
            assembly_path.write_text(_assembly_bytes(symbol, code, architecture), encoding="utf-8")
            object_targets.append(f"build/{symbol}.o")
            decompiler_path = artifact / "decompiler.c"
            if decompiler_path.is_file():
                shutil.copy2(decompiler_path, output_root / "src" / "staging" / f"{symbol}.c")
            context_path = artifact / "context.h"
            if context_path.is_file():
                shutil.copy2(context_path, output_root / "include" / f"{symbol}_context.h")
            try:
                initialize_function_workflow(project_root, function_id=function_id, modes={DecompilationMode.MATCHING, DecompilationMode.FUNCTIONAL})
            except ContractError as exc:
                if "already exists" not in str(exc):
                    raise
            functions.append(
                {
                    "function_id": function_id,
                    "rva": rva,
                    "symbol": symbol,
                    "assembly": str(assembly_path.relative_to(output_root)),
                    "staging_source": f"src/staging/{symbol}.c" if decompiler_path.is_file() else None,
                    "active_build_form": "assembly",
                    "source_of_truth": "original function body ranges exported by Ghidra",
                }
            )
    mkdir_cmd = "-@mkdir build"
    make_lines = [
        "PYTHON ?= python3",
        "CC := gcc",
        "ARCHFLAGS := -m32" if architecture == "x86" else "ARCHFLAGS := -m64",
        "ASFLAGS ?= $(ARCHFLAGS) -c",
        "OBJECTS := " + " ".join(object_targets),
        "",
        ".PHONY: all clean verify",
        "all: $(OBJECTS)",
        "",
        "build/%.o: src/asm/%.S",
        "\t" + mkdir_cmd,
        "\t$(CC) $(ASFLAGS) $< -o $@",
        "",
        "verify:",
        "\t$(PYTHON) -m x86decomp verify-project " + str(project_root),
        "",
        "clean:",
        "\trm -rf build/*.o",
        "",
    ]
    (output_root / "Makefile").write_text("\n".join(make_lines), encoding="utf-8")
    (output_root / "README.md").write_text(
        "# Generated hybrid decompilation project\n\n"
        "`src/asm` is the continuously buildable fallback generated from immutable function bytes.\n"
        "`src/staging` contains untrusted decompiler output and is not compiled automatically.\n"
        "Promote source into `src/matched` or `src/functional` only after the corresponding validator passes.\n",
        encoding="utf-8",
    )
    manifest = {
        "schema_version": 1,
        "created_at": utc_now(),
        "project_root": str(project_root),
        "architecture": architecture,
        "functions": functions,
        "build": {"kind": "gnu-assembler-objects", "object_count": len(object_targets)},
    }
    write_json(output_root / "hybrid-project.json", manifest)
    return manifest
