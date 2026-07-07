"""Continuously buildable hybrid source-tree generation."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any, Mapping

from .errors import ContractError
from .util import load_json, utc_now, write_json
from .workflow import DecompilationMode, initialize_function_workflow


def _assembly_bytes(symbol: str, code: bytes, architecture: str) -> str:
    """Support assembly bytes processing for internal toolkit callers."""
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
    asm_format: str = "bytes",
    image_base: int = 0,
    assembler_command: list[str] | None = None,
    symbol_map: Mapping[str, Any] | list[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    """Generate a continuously buildable hybrid tree.

    ``bytes`` is the compatibility default and emits exact byte-form assembly.
    ``annotated`` retains those directives and appends ignored mnemonic comments.
    ``mnemonic`` uses the relocation-aware materializer and accepts source
    only after exact resolved-byte verification, with per-instruction byte fallback.
    """
    if architecture not in ("x86", "x86_64"):
        raise ContractError("hybrid architecture must be x86 or x86_64")
    if asm_format not in ("bytes", "annotated", "mnemonic"):
        raise ContractError("asm_format must be bytes, annotated, or mnemonic")
    if image_base < 0:
        raise ContractError("image_base must be non-negative")
    project_root = project_root.resolve()
    output_root = output_root.resolve()
    if output_root.exists() and any(output_root.iterdir()):
        if not overwrite:
            raise ContractError(f"hybrid output is not empty: {output_root}")
        shutil.rmtree(output_root)
    for directory in (
        "src/asm", "src/staging", "src/matched", "src/functional", "include",
        "build", "build/materialized", "build/resolved", "config", "config/original",
        "reports/asm", "tests",
    ):
        (output_root / directory).mkdir(parents=True, exist_ok=True)
    function_root = project_root / "functions"
    specs: list[dict[str, Any]] = []
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
            specs.append({
                "artifact": artifact,
                "manifest": manifest,
                "function_id": function_id,
                "rva": rva,
                "symbol": symbol,
                "code": code,
            })
    from .assembly.relocations import normalize_symbol_map
    effective_symbols: dict[str, dict[str, Any]] = {}
    if symbol_map is not None:
        for name, entry in normalize_symbol_map(symbol_map).items():
            if name.startswith("_") and name[1:] in effective_symbols:
                continue
            effective_symbols[name] = entry.to_dict()
    for spec in specs:
        name = str(spec["symbol"])
        rva = int(spec["rva"])
        existing = effective_symbols.get(name)
        if existing is not None and int(existing["rva"]) != rva:
            raise ContractError(f"symbol map conflicts with function RVA for {name}")
        effective_symbols[name] = {"rva": rva, "kind": "function"}
    functions: list[dict[str, Any]] = []
    object_targets: list[str] = []
    for spec in specs:
        artifact = Path(spec["artifact"])
        function_id = str(spec["function_id"])
        rva = int(spec["rva"])
        symbol = str(spec["symbol"])
        code = bytes(spec["code"])
        assembly_path = output_root / "src" / "asm" / f"{symbol}.S"
        original_path = output_root / "config" / "original" / f"{symbol}.bin"
        original_path.write_bytes(code)
        asm_report: dict[str, Any]
        if asm_format == "bytes":
            assembly_path.write_text(_assembly_bytes(symbol, code, architecture), encoding="utf-8")
            asm_report = {
                "format": "bytes",
                "classification": "byte-form",
                "exact_match": True,
                "input_sha256": __import__('hashlib').sha256(code).hexdigest(),
            }
        elif asm_format == "annotated":
            from .assembly.annotation import render_annotated_assembly
            source = render_annotated_assembly(
                symbol, code, architecture, base_address=image_base + rva
            )
            assembly_path.write_text(source, encoding="utf-8")
            asm_report = {
                "format": "annotated",
                "classification": "annotated-byte-form",
                "exact_match": True,
                "input_sha256": __import__('hashlib').sha256(code).hexdigest(),
            }
        else:
            from .assembly.materialize import materialize_function
            asm_report = materialize_function(
                code,
                symbol=symbol,
                rva=rva,
                architecture=architecture,
                symbol_map=effective_symbols,
                source_path=assembly_path,
                object_path=output_root / "build" / "materialized" / f"{symbol}.obj",
                resolved_path=output_root / "build" / "resolved" / f"{symbol}.bin",
                image_base=image_base,
                assembler_command=assembler_command,
            )
        report_path = output_root / "reports" / "asm" / f"{symbol}.json"
        write_json(report_path, asm_report)
        object_targets.append(f"build/{symbol}.o")
        decompiler_path = artifact / "decompiler.c"
        if decompiler_path.is_file():
            shutil.copy2(decompiler_path, output_root / "src" / "staging" / f"{symbol}.c")
        context_path = artifact / "context.h"
        if context_path.is_file():
            shutil.copy2(context_path, output_root / "include" / f"{symbol}_context.h")
        try:
            initialize_function_workflow(
                project_root,
                function_id=function_id,
                modes={DecompilationMode.MATCHING, DecompilationMode.FUNCTIONAL},
            )
        except ContractError as exc:
            if "already exists" not in str(exc):
                raise
        functions.append(
            {
                "function_id": function_id,
                "rva": rva,
                "symbol": symbol,
                "assembly": str(assembly_path.relative_to(output_root)),
                "bytes_path": str(original_path.relative_to(output_root)),
                "asm_report": str(report_path.relative_to(output_root)),
                "asm_format": asm_format,
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
        f"Assembly format: `{asm_format}`. The compatibility default is `bytes`.\n\n"
        "`src/asm` is the continuously buildable fallback generated from immutable function bytes.\n"
        "`src/staging` contains untrusted decompiler output and is not compiled automatically.\n"
        "Mnemonic sources are accepted only after relocation-aware exact-byte round-trip validation; "
        "unsupported encodings remain explicit `.byte` directives.\n"
        "Promote source into `src/matched` or `src/functional` only after the corresponding validator passes.\n",
        encoding="utf-8",
    )
    manifest = {
        "schema_version": 2,
        "created_at": utc_now(),
        "project_root": str(project_root),
        "architecture": architecture,
        "image_base": image_base,
        "asm_format": asm_format,
        "default_asm_format": "bytes",
        "symbol_map": effective_symbols,
        "functions": functions,
        "build": {"kind": "gnu-assembler-objects", "object_count": len(object_targets)},
    }
    write_json(output_root / "hybrid-project.json", manifest)
    return manifest
