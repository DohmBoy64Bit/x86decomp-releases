"""Create local decomp.me-style function packets without uploading data."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

from .artifacts import validate_function_manifest
from .errors import ContractError
from .util import load_json, sha256_file, utc_now, write_json


def _copy_required(source: Path, destination: Path, name: str) -> dict[str, Any]:
    """Copy required."""
    path = source / name
    if not path.is_file():
        raise ContractError(f"function artifact is missing {name}: {path}")
    out = destination / name
    shutil.copy2(path, out)
    return {"path": name, "sha256": sha256_file(out), "size": out.stat().st_size}


def create_decompme_packet(
    function_artifact: Path,
    output_directory: Path,
    *,
    overwrite: bool = False,
) -> dict[str, Any]:
    """Build a local, reviewable function packet.

    The packet intentionally does not contact decomp.me. Ghidra's human-readable
    listing is retained as source material and is labeled non-canonical because
    decomp.me/compiler syntax may require target-specific conversion.
    """

    source = function_artifact.resolve()
    manifest_path = source / "function.json"
    if not manifest_path.is_file():
        raise ContractError(f"missing function.json: {manifest_path}")
    manifest = validate_function_manifest(load_json(manifest_path))
    destination = output_directory.resolve()
    if destination.exists():
        if not overwrite:
            raise ContractError(f"output directory already exists: {destination}")
        if destination.is_file() or destination.is_symlink():
            raise ContractError(f"output path is not a normal directory: {destination}")
        shutil.rmtree(destination)
    destination.mkdir(parents=True)

    files: list[dict[str, Any]] = []
    files.append(_copy_required(source, destination, "listing.asm"))
    files.append(_copy_required(source, destination, "decompiler.c"))
    files.append(_copy_required(source, destination, "context.h"))
    files.append(_copy_required(source, destination, "references.jsonl"))
    files.append(_copy_required(source, destination, "function.json"))

    target_asm = destination / "target_asm_ghidra.txt"
    shutil.copy2(destination / "listing.asm", target_asm)
    files.append(
        {
            "path": target_asm.name,
            "sha256": sha256_file(target_asm),
            "size": target_asm.stat().st_size,
        }
    )
    scratch = destination / "scratch.md"
    scratch.write_text(
        "# Local decomp.me-style packet\n\n"
        f"- Function: `{manifest['id']}`\n"
        f"- Name: `{manifest.get('name', '')}`\n"
        "- Upload: not performed by this toolkit\n"
        "- Target assembly: `target_asm_ghidra.txt`\n"
        "- Context: `context.h`\n"
        "- Starting candidate: `decompiler.c`\n\n"
        "Ghidra listing text is a display artifact, not canonical reassemblable GAS. "
        "Convert syntax and references for the selected compiler/decomp.me platform, "
        "then validate against exact range bytes and the executable-aware diff.\n",
        encoding="utf-8",
    )
    files.append({"path": scratch.name, "sha256": sha256_file(scratch), "size": scratch.stat().st_size})

    packet = {
        "schema_version": 1,
        "created_at": utc_now(),
        "kind": "local_decompme_function_packet",
        "function_id": manifest["id"],
        "source_artifact": str(source),
        "output_directory": str(destination),
        "files": files,
        "uploaded": False,
        "limitations": [
            "Ghidra listing syntax may require conversion before use by a compiler or hosted scratch service.",
            "Decompiler C and generated context are proposals, not recovered original source.",
        ],
    }
    write_json(destination / "packet.json", packet)
    return packet
