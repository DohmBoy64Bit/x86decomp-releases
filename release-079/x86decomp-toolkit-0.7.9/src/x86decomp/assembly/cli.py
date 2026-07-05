"""Provide x86decomp.assembly.cli functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from x86decomp.hybrid import generate_hybrid_project
from x86decomp.contracts import ContractError, atomic_write_bytes

from .annotation import annotate_source, parse_byte_directives
from .materialize import materialize_function, verify_existing_source
from .pipeline import ASM_FORMATS, AssemblyPipeline
from .relocations import RelocationResolver, supported_relocations
from .store import AssemblyStore


def _json_file(path: str | Path) -> Any:
    """Implement json file.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ContractError(f"cannot read JSON {path}: {exc}") from exc


def _json_array(raw: str | None) -> list[str] | None:
    """Implement json array.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if raw is None:
        return None
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ContractError(f"invalid JSON command array: {exc}") from exc
    if not isinstance(value, list) or not value or not all(isinstance(item, str) for item in value):
        raise ContractError("assembler command must be a non-empty JSON array of strings")
    return list(value)


def _int(value: str) -> int:
    """Implement int.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    return int(value, 0)


def _emit(value: Any) -> None:
    """Emit the requested operation.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if isinstance(value, dict) and "resolved_bytes" in value:
        value = {key: item for key, item in value.items() if key != "resolved_bytes"}
    print(json.dumps(value, indent=2, sort_keys=True, default=str))


def build_parser(*, prog: str = "x86decomp-assembly") -> argparse.ArgumentParser:
    """Build parser.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    parser = argparse.ArgumentParser(
        prog=prog,
        description="x86decomp-toolkit 0.7.9 relocation-aware mnemonic assembly",
    )
    parser.add_argument("--project", default=".")
    parser.add_argument("--actor", default="analyst")
    sub = parser.add_subparsers(dest="group", required=True)

    project = sub.add_parser("project")
    ps = project.add_subparsers(dest="action", required=True)
    ps.add_parser("init")
    ps.add_parser("check")

    asm = sub.add_parser("asm")
    ass = asm.add_subparsers(dest="action", required=True)
    q = ass.add_parser("annotate")
    q.add_argument("source")
    q.add_argument("output")
    q.add_argument("--symbol", required=True)
    q.add_argument("--rva", type=_int, required=True)
    q.add_argument("--image-base", type=_int, default=0)
    q.add_argument("--architecture", choices=["x86", "x86_64"], default="x86")
    q = ass.add_parser("materialize")
    q.add_argument("input")
    q.add_argument("output_source")
    q.add_argument("output_object")
    q.add_argument("output_resolved")
    q.add_argument("--input-kind", choices=["bytes", "assembly"], default="bytes")
    q.add_argument("--symbol", required=True)
    q.add_argument("--rva", type=_int, required=True)
    q.add_argument("--image-base", type=_int, default=0)
    q.add_argument("--architecture", choices=["x86", "x86_64"], default="x86")
    q.add_argument("--symbol-map", required=True)
    q.add_argument("--assembler-command-json")
    q.add_argument("--timeout", type=int, default=60)
    q.add_argument("--report")
    q = ass.add_parser("verify-roundtrip")
    q.add_argument("source")
    q.add_argument("original")
    q.add_argument("output_object")
    q.add_argument("output_resolved")
    q.add_argument("--symbol", required=True)
    q.add_argument("--rva", type=_int, required=True)
    q.add_argument("--image-base", type=_int, default=0)
    q.add_argument("--architecture", choices=["x86", "x86_64"], default="x86")
    q.add_argument("--symbol-map", required=True)
    q.add_argument("--assembler-command-json")
    q.add_argument("--timeout", type=int, default=60)
    q.add_argument("--report")
    q = ass.add_parser("batch")
    q.add_argument("manifest")
    q.add_argument("output")
    q.add_argument("--format", dest="asm_format", choices=ASM_FORMATS, default="bytes")
    q.add_argument("--assembler-command-json")
    q.add_argument("--image-base", type=_int)
    q = ass.add_parser("report")
    q.add_argument("run_id")
    ass.add_parser("list")

    reloc = sub.add_parser("reloc")
    rs = reloc.add_subparsers(dest="action", required=True)
    q = rs.add_parser("inspect")
    q.add_argument("object")
    q.add_argument("--symbol")
    q = rs.add_parser("resolve")
    q.add_argument("object")
    q.add_argument("symbol")
    q.add_argument("base_rva", type=_int)
    q.add_argument("symbol_map")
    q.add_argument("output")
    q.add_argument("--image-base", type=_int, default=0)
    rs.add_parser("supported")

    hybrid = sub.add_parser("hybrid")
    hs = hybrid.add_subparsers(dest="action", required=True)
    q = hs.add_parser("generate")
    q.add_argument("source_project")
    q.add_argument("output")
    q.add_argument("--architecture", choices=["x86", "x86_64"], default="x86")
    q.add_argument("--asm-format", choices=ASM_FORMATS, default="bytes")
    q.add_argument("--image-base", type=_int, default=0)
    q.add_argument("--assembler-command-json")
    q.add_argument("--symbol-map")
    q.add_argument("--overwrite", action="store_true")
    return parser


def dispatch(args: argparse.Namespace) -> Any:
    """Dispatch the requested operation.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    store = AssemblyStore(args.project)
    if args.group == "project":
        if args.action == "init":
            store.initialize()
        return store.check()
    if args.group == "asm":
        if args.action == "annotate":
            return annotate_source(
                Path(args.source),
                Path(args.output),
                symbol=args.symbol,
                architecture=args.architecture,
                base_address=args.image_base + args.rva,
            )
        if args.action == "materialize":
            input_path = Path(args.input)
            code = (
                input_path.read_bytes()
                if args.input_kind == "bytes"
                else parse_byte_directives(input_path.read_text(encoding="utf-8"))
            )
            result = materialize_function(
                code,
                symbol=args.symbol,
                rva=args.rva,
                architecture=args.architecture,
                symbol_map=_json_file(args.symbol_map),
                source_path=Path(args.output_source),
                object_path=Path(args.output_object),
                resolved_path=Path(args.output_resolved),
                image_base=args.image_base,
                assembler_command=_json_array(args.assembler_command_json),
                timeout_seconds=args.timeout,
            )
            if args.report:
                atomic_write_bytes(
                    args.report,
                    (json.dumps(result, indent=2, sort_keys=True, default=str) + "\n").encode(),
                )
            return result
        if args.action == "verify-roundtrip":
            result = verify_existing_source(
                Path(args.source),
                Path(args.original).read_bytes(),
                symbol=args.symbol,
                rva=args.rva,
                architecture=args.architecture,
                symbol_map=_json_file(args.symbol_map),
                object_path=Path(args.output_object),
                resolved_path=Path(args.output_resolved),
                image_base=args.image_base,
                assembler_command=_json_array(args.assembler_command_json),
                timeout_seconds=args.timeout,
            )
            if args.report:
                atomic_write_bytes(
                    args.report,
                    (json.dumps(result, indent=2, sort_keys=True, default=str) + "\n").encode(),
                )
            return result
        api = AssemblyPipeline(store)
        if args.action == "batch":
            return api.batch(
                Path(args.manifest),
                Path(args.output),
                asm_format=args.asm_format,
                assembler_command=_json_array(args.assembler_command_json),
                image_base=args.image_base,
                actor=args.actor,
            )
        if args.action == "report":
            return api.report(args.run_id)
        return api.list_runs()
    if args.group == "reloc":
        api = RelocationResolver()
        if args.action == "inspect":
            return api.inspect(Path(args.object), symbol=args.symbol)
        if args.action == "supported":
            return supported_relocations()
        return api.resolve(
            Path(args.object),
            symbol=args.symbol,
            base_rva=args.base_rva,
            symbol_map=_json_file(args.symbol_map),
            image_base=args.image_base,
            output_path=Path(args.output),
        )
    if args.group == "hybrid":
        return generate_hybrid_project(
            Path(args.source_project),
            Path(args.output),
            architecture=args.architecture,
            overwrite=args.overwrite,
            asm_format=args.asm_format,
            image_base=args.image_base,
            assembler_command=_json_array(args.assembler_command_json),
            symbol_map=None if args.symbol_map is None else _json_file(args.symbol_map),
        )
    raise ContractError("unhandled assembly command")


def main(argv: list[str] | None = None) -> int:
    """Run the command-line entry point.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    parser = build_parser()
    try:
        args = parser.parse_args(argv)
        _emit(dispatch(args))
        return 0
    except (ContractError, KeyError, OSError, ValueError, subprocess.SubprocessError) as exc:  # type: ignore[name-defined]
        print(json.dumps({"error": type(exc).__name__, "message": str(exc)}, sort_keys=True), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
