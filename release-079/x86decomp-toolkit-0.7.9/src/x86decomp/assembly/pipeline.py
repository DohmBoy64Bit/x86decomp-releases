"""Provide x86decomp.assembly.pipeline functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from x86decomp.contracts import (
    ContractError,
    atomic_write_bytes,
    canonical_json,
    random_id,
    sha256_bytes,
    sha256_file,
    utc_now,
)

from .annotation import parse_byte_directives, render_annotated_assembly, render_byte_assembly
from .materialize import materialize_function
from .relocations import normalize_symbol_map
from .store import AssemblyStore

ASM_FORMATS = ("bytes", "annotated", "mnemonic")


def _load_json(path: Path) -> Any:
    """Load json.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ContractError(f"cannot read JSON {path}: {exc}") from exc


def _resolve_path(base: Path, raw: str | Path) -> Path:
    """Resolve path.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    path = Path(raw)
    return path.resolve() if path.is_absolute() else (base / path).resolve()


def _function_bytes(item: Mapping[str, Any], *, base: Path) -> bytes:
    """Implement function bytes.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if item.get("code_hex") is not None:
        try:
            return bytes.fromhex(str(item["code_hex"]))
        except ValueError as exc:
            raise ContractError(f"invalid code_hex for {item.get('function_id')}") from exc
    if item.get("bytes_path") is not None:
        path = _resolve_path(base, str(item["bytes_path"]))
        if not path.is_file():
            raise ContractError(f"function bytes do not exist: {path}")
        return path.read_bytes()
    if item.get("assembly") is not None:
        path = _resolve_path(base, str(item["assembly"]))
        if not path.is_file():
            raise ContractError(f"assembly source does not exist: {path}")
        return parse_byte_directives(path.read_text(encoding="utf-8"))
    raise ContractError(f"function {item.get('function_id')} requires code_hex, bytes_path, or assembly")


def _symbol_map(
    functions: list[Mapping[str, Any]],
    supplemental: Mapping[str, Any] | list[Mapping[str, Any]] | None = None,
) -> dict[str, dict[str, Any]]:
    """Implement symbol map.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    result: dict[str, dict[str, Any]] = {}
    if supplemental is not None:
        for name, entry in normalize_symbol_map(supplemental).items():
            # Store one canonical spelling; normalize_symbol_map will recreate
            # underscore aliases at resolution time.
            if name.startswith("_") and name[1:] in result:
                continue
            result[name] = entry.to_dict()
    for item in functions:
        symbol = str(item["symbol"])
        raw_rva = item["rva"]
        rva = int(raw_rva, 0) if isinstance(raw_rva, str) else int(raw_rva)
        current = result.get(symbol)
        if current is not None and int(current["rva"]) != rva:
            raise ContractError(f"symbol map conflicts with function RVA for {symbol}")
        result[symbol] = {"rva": rva, "kind": "function"}
    return result


class AssemblyPipeline:
    """Represent assembly pipeline state and behavior.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    def __init__(self, store: AssemblyStore):
        """Initialize the instance with the supplied constructor arguments.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.store = store
        store.initialize()

    def batch(
        self,
        manifest_path: Path,
        output_root: Path,
        *,
        asm_format: str = "bytes",
        assembler_command: Sequence[str] | None = None,
        image_base: int | None = None,
        actor: str = "analyst",
    ) -> dict[str, Any]:
        """Implement batch.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if asm_format not in ASM_FORMATS:
            raise ContractError(f"asm format must be one of {ASM_FORMATS}")
        manifest_path = manifest_path.resolve()
        manifest = _load_json(manifest_path)
        if not isinstance(manifest, Mapping) or not isinstance(manifest.get("functions"), list):
            raise ContractError("assembly manifest requires a functions list")
        functions = [item for item in manifest["functions"] if isinstance(item, Mapping)]
        if len(functions) != len(manifest["functions"]):
            raise ContractError("every assembly manifest function must be an object")
        architecture = str(manifest.get("architecture", "x86"))
        if architecture not in {"x86", "x86_64"}:
            raise ContractError("manifest architecture must be x86 or x86_64")
        effective_image_base = int(manifest.get("image_base", 0) if image_base is None else image_base)
        supplemental = manifest.get("symbol_map")
        if supplemental is not None and not isinstance(supplemental, (Mapping, list)):
            raise ContractError("manifest symbol_map must be an object or list")
        symbols = _symbol_map(functions, supplemental)
        output_root = output_root.resolve()
        asm_root = output_root / "src" / "asm"
        object_root = output_root / "build" / "objects"
        resolved_root = output_root / "build" / "resolved"
        report_root = output_root / "reports"
        for path in (asm_root, object_root, resolved_root, report_root):
            path.mkdir(parents=True, exist_ok=True)
        run_id = random_id("asmrun")
        now = utc_now()
        symbol_map_payload = canonical_json(symbols).encode("utf-8")
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO assembly_asm_runs("
                "run_id,asm_format,architecture,source_root,output_root,symbol_map_sha256,"
                "status,summary_json,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?,?)",
                (
                    run_id,
                    asm_format,
                    architecture,
                    str(manifest_path.parent),
                    str(output_root),
                    sha256_bytes(symbol_map_payload),
                    "running",
                    "{}",
                    now,
                    now,
                ),
            )
        try:
            results: list[dict[str, Any]] = []
            for item in functions:
                function_id = str(item["function_id"])
                symbol = str(item["symbol"])
                raw_rva = item["rva"]
                rva = int(raw_rva, 0) if isinstance(raw_rva, str) else int(raw_rva)
                code = _function_bytes(item, base=manifest_path.parent)
                source_path = asm_root / f"{symbol}.S"
                object_path: Path | None = None
                resolved_path: Path | None = None
                if asm_format == "bytes":
                    source = render_byte_assembly(symbol, code, architecture)
                    atomic_write_bytes(source_path, source.encode("utf-8"))
                    result: dict[str, Any] = {
                        "format": "bytes",
                        "classification": "byte-form",
                        "instruction_count": 0,
                        "mnemonic_count": 0,
                        "byte_escape_count": len(code),
                        "byte_escape_bytes": len(code),
                        "relocation_count": 0,
                        "resolved_relocation_count": 0,
                        "unresolved_relocation_count": 0,
                        "exact_match": True,
                        "resolved_sha256": sha256_bytes(code),
                    }
                elif asm_format == "annotated":
                    source = render_annotated_assembly(
                        symbol,
                        code,
                        architecture,
                        base_address=effective_image_base + rva,
                    )
                    atomic_write_bytes(source_path, source.encode("utf-8"))
                    result = {
                        "format": "annotated",
                        "classification": "annotated-byte-form",
                        "instruction_count": source.count("# x86decomp:"),
                        "mnemonic_count": 0,
                        "byte_escape_count": len(code),
                        "byte_escape_bytes": len(code),
                        "relocation_count": 0,
                        "resolved_relocation_count": 0,
                        "unresolved_relocation_count": 0,
                        "exact_match": True,
                        "resolved_sha256": sha256_bytes(code),
                    }
                else:
                    object_path = object_root / f"{symbol}.obj"
                    resolved_path = resolved_root / f"{symbol}.bin"
                    result = materialize_function(
                        code,
                        symbol=symbol,
                        rva=rva,
                        architecture=architecture,
                        symbol_map=symbols,
                        source_path=source_path,
                        object_path=object_path,
                        resolved_path=resolved_path,
                        image_base=effective_image_base,
                        assembler_command=assembler_command,
                    )
                result_id = random_id("asmfn")
                details = {
                    **result,
                    "function_id": function_id,
                    "input_sha256": sha256_bytes(code),
                    "source_sha256": sha256_file(source_path),
                }
                report_path = report_root / f"{symbol}.json"
                atomic_write_bytes(
                    report_path,
                    (json.dumps(details, indent=2, sort_keys=True, default=str) + "\n").encode("utf-8"),
                )
                with self.store.transaction() as connection:
                    connection.execute(
                        "INSERT INTO assembly_asm_functions("
                        "result_id,run_id,function_id,symbol,rva,input_sha256,source_path,source_sha256,"
                        "object_path,resolved_path,resolved_sha256,instruction_count,mnemonic_count,"
                        "byte_escape_count,relocation_count,resolved_relocation_count,"
                        "unresolved_relocation_count,exact_match,classification,details_json,created_at) "
                        "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (
                            result_id,
                            run_id,
                            function_id,
                            symbol,
                            rva,
                            sha256_bytes(code),
                            str(source_path),
                            sha256_file(source_path),
                            None if object_path is None else str(object_path),
                            None if resolved_path is None else str(resolved_path),
                            result.get("resolved_sha256"),
                            int(result["instruction_count"]),
                            int(result["mnemonic_count"]),
                            int(result["byte_escape_count"]),
                            int(result["relocation_count"]),
                            int(result["resolved_relocation_count"]),
                            int(result["unresolved_relocation_count"]),
                            int(bool(result["exact_match"])),
                            str(result["classification"]),
                            canonical_json(details),
                            utc_now(),
                        ),
                    )
                    self.store.audit(
                        actor,
                        "assembly.asm.function",
                        result_id,
                        {
                            "function_id": function_id,
                            "format": asm_format,
                            "classification": result["classification"],
                            "exact_match": bool(result["exact_match"]),
                        },
                        connection=connection,
                    )
                    if object_path is not None:
                        for relocation in result.get("relocations", []):
                            connection.execute(
                                "INSERT INTO assembly_relocation_resolutions("
                                "resolution_id,result_id,object_path,object_sha256,symbol,section_name,"
                                "relocation_offset,relocation_type,target_symbol,target_rva,computed_value,"
                                "status,details_json,created_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                (
                                    random_id("reloc"), result_id, str(object_path), sha256_file(object_path),
                                    symbol, ".text", int(relocation["offset"]), str(relocation["type"]),
                                    relocation.get("target_symbol"), relocation.get("target_rva"),
                                    relocation.get("computed_value"), str(relocation["status"]),
                                    canonical_json(relocation), utc_now(),
                                ),
                            )
                results.append({"result_id": result_id, **details, "report": str(report_path)})
            counts: dict[str, int] = {}
            for item in results:
                classification = str(item["classification"])
                counts[classification] = counts.get(classification, 0) + 1
            summary = {
                "total": len(results),
                "format": asm_format,
                "counts": counts,
                "exact": sum(1 for item in results if item["exact_match"]),
                "mnemonic_instructions": sum(int(item["mnemonic_count"]) for item in results),
                "byte_escapes": sum(int(item["byte_escape_count"]) for item in results),
                "byte_escape_bytes": sum(int(item.get("byte_escape_bytes", 0)) for item in results),
                "resolved_relocations": sum(int(item["resolved_relocation_count"]) for item in results),
                "unresolved_relocations": sum(int(item["unresolved_relocation_count"]) for item in results),
            }
            with self.store.transaction() as connection:
                connection.execute(
                    "UPDATE assembly_asm_runs SET status='completed',summary_json=?,updated_at=? WHERE run_id=?",
                    (canonical_json(summary), utc_now(), run_id),
                )
                self.store.audit(actor, "assembly.asm.batch", run_id, summary, connection=connection)
            return {"run_id": run_id, "summary": summary, "functions": results}
        except BaseException as exc:
            failure = {
                "total_completed": len(locals().get("results", [])),
                "format": asm_format,
                "error_type": type(exc).__name__,
                "error": str(exc),
            }
            with self.store.transaction() as connection:
                connection.execute(
                    "UPDATE assembly_asm_runs SET status='failed',summary_json=?,updated_at=? WHERE run_id=?",
                    (canonical_json(failure), utc_now(), run_id),
                )
                self.store.audit(actor, "assembly.asm.batch.failed", run_id, failure, connection=connection)
            raise

    def report(self, run_id: str) -> dict[str, Any]:
        """Report the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.connect() as connection:
            run = connection.execute(
                "SELECT * FROM assembly_asm_runs WHERE run_id=?", (run_id,)
            ).fetchone()
            if run is None:
                raise KeyError(run_id)
            result = self.store.decode(run, "summary_json")
            result["functions"] = [
                self.store.decode(row, "details_json")
                for row in connection.execute(
                    "SELECT * FROM assembly_asm_functions WHERE run_id=? ORDER BY rva", (run_id,)
                )
            ]
            return result

    def list_runs(self) -> list[dict[str, Any]]:
        """List runs.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.connect() as connection:
            return [
                self.store.decode(row, "summary_json")
                for row in connection.execute(
                    "SELECT * FROM assembly_asm_runs ORDER BY created_at,run_id"
                )
            ]
