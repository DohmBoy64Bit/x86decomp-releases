"""Manifest-driven full-image relink backend.

The backend performs a real linker invocation using user-supplied objects and a
linker profile. It does not claim to infer the original linker script or object
partitioning automatically.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path
from typing import Any

from .diffing import compare_files
from .image_match import compare_whole_images
from .linker_layout import reconstruct_linker_layout
from .errors import ContractError, ExternalToolError
from .util import load_json, sha256_file, utc_now, write_json


def run_full_relink(manifest_path: Path, *, report_path: Path | None = None) -> dict[str, Any]:
    manifest = load_json(manifest_path)
    if not isinstance(manifest, dict):
        raise ContractError("relink manifest must be an object")
    base = manifest_path.resolve().parent
    executable_value = str(manifest.get("linker"))
    explicit = Path(executable_value).expanduser()
    if explicit.is_absolute() or explicit.parent != Path("."):
        linker = str(explicit.resolve()) if explicit.is_file() else None
    else:
        linker = shutil.which(executable_value)
    if linker is None:
        raise ExternalToolError(f"linker executable is unavailable: {executable_value}")
    objects_raw = manifest.get("objects")
    if not isinstance(objects_raw, list) or not objects_raw:
        raise ContractError("relink objects must be a non-empty array")
    objects = [(base / str(item)).resolve() for item in objects_raw]
    for obj in objects:
        if not obj.is_file():
            raise ContractError(f"relink object is missing: {obj}")
    output = (base / str(manifest["output"])).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()
    arguments_raw = manifest.get("arguments")
    if not isinstance(arguments_raw, list) or not all(isinstance(item, str) for item in arguments_raw):
        raise ContractError("relink arguments must be an array of strings")
    substitutions = {
        "{output}": str(output),
        "{objects}": "\n".join(str(item) for item in objects),
    }
    response_file = output.parent / "objects.rsp"
    response_file.write_text("\n".join(f'"{item}"' for item in objects) + "\n", encoding="utf-8")
    substitutions["{response_file}"] = str(response_file)
    command = [linker]
    for argument in arguments_raw:
        if argument == "{objects}":
            command.extend(str(item) for item in objects)
            continue
        for token, replacement in substitutions.items():
            argument = argument.replace(token, replacement)
        command.append(argument)
    environment = os.environ.copy() if manifest.get("inherit_environment", True) else {}
    env_raw = manifest.get("environment", {})
    if not isinstance(env_raw, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in env_raw.items()):
        raise ContractError("relink environment must be a string-to-string object")
    environment.update(env_raw)
    timeout = manifest.get("timeout_seconds", 300)
    if not isinstance(timeout, int) or timeout <= 0:
        raise ContractError("relink timeout_seconds must be positive")
    completed = subprocess.run(command, capture_output=True, text=True, timeout=timeout, env=environment, cwd=base, check=False)
    success = completed.returncode == 0 and output.is_file()
    comparison = None
    whole_image_match = None
    layout_reconstruction = None
    reference = manifest.get("reference_image")
    reference_path = None if reference is None else (base / str(reference)).resolve()
    if success and reference_path is not None:
        comparison = compare_files(reference_path, output)
        profile_value = manifest.get("layout_profile")
        profile_path = None if profile_value is None else (base / str(profile_value)).resolve()
        whole_image_match = compare_whole_images(
            reference_path,
            output,
            profile_path=profile_path,
        )
    map_value = manifest.get("map_file")
    if success and map_value is not None and reference_path is not None:
        supplied_objects = manifest.get("layout_objects", manifest.get("objects", []))
        if not isinstance(supplied_objects, list):
            raise ContractError("relink layout_objects must be an array")
        layout_reconstruction = reconstruct_linker_layout(
            reference_path,
            (base / str(map_value)).resolve(),
            object_paths=[(base / str(item)).resolve() for item in supplied_objects],
        )
    report = {
        "schema_version": 1,
        "created_at": utc_now(),
        "kind": "full_relink",
        "command": command,
        "linker": linker,
        "linker_sha256": sha256_file(Path(linker)),
        "objects": [{"path": str(path), "sha256": sha256_file(path)} for path in objects],
        "output": str(output),
        "output_sha256": sha256_file(output) if output.is_file() else None,
        "return_code": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "success": success,
        "reference_comparison": comparison,
        "whole_image_match": whole_image_match,
        "layout_reconstruction": layout_reconstruction,
        "original_linker_reconstruction_claimed": bool(layout_reconstruction and not layout_reconstruction.get("unresolved")),
    }
    if report_path is not None:
        write_json(report_path, report)
    if not success:
        raise ExternalToolError(f"linker failed with exit code {completed.returncode}: {completed.stderr.strip()}")
    return report
