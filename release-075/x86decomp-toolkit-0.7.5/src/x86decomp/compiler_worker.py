"""Isolated compiler-worker facade.

The facade copies declared inputs into an ephemeral workspace and invokes the
normal compiler profile through a bounded local or container worker.  Local mode
is explicitly not a security boundary; container mode is the production
isolation option.
"""

from __future__ import annotations

import os
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any

from .compiler import load_profile
from .errors import ContractError, ExternalToolError
from .util import load_json, sha256_file, utc_now, write_json
from .worker import WorkerLimits, WorkerRequest, execute_worker_request


def run_compiler_worker(
    profile_path: Path,
    source_path: Path,
    output_path: Path,
    *,
    isolation: str = "local_bounded",
    container_image: str | None = None,
    cache_directory: Path | None = None,
    report_path: Path | None = None,
    limits: WorkerLimits | None = None,
) -> dict[str, Any]:
    profile_path = profile_path.resolve()
    source_path = source_path.resolve()
    output_path = output_path.resolve()
    load_profile(profile_path)
    if not source_path.is_file() or source_path.is_symlink():
        raise ContractError("compiler-worker source must be a regular file")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="x86decomp-compiler-worker-") as temporary:
        work = Path(temporary)
        profile_copy = work / "inputs" / "profile.json"
        source_copy = work / "inputs" / source_path.name
        profile_copy.parent.mkdir(parents=True)
        shutil.copy2(profile_path, profile_copy)
        shutil.copy2(source_path, source_copy)
        worker_output = work / "outputs" / output_path.name
        compiler_report = work / "outputs" / "compiler-report.json"
        worker_output.parent.mkdir(parents=True)
        package_source = Path(__file__).resolve().parent
        runtime_root = work / "runtime"
        shutil.copytree(package_source, runtime_root / "x86decomp", symlinks=False)
        if isolation == "container":
            # The complete pure-Python runtime is copied into the mounted work
            # directory.  No host source path or host Python executable is
            # assumed to exist inside the image.
            command = [
                "python3",
                "-S",
                "-m",
                "x86decomp",
                "compile",
                "/work/inputs/profile.json",
                f"/work/inputs/{source_path.name}",
                f"/work/outputs/{output_path.name}",
                "--report",
                "/work/outputs/compiler-report.json",
            ]
            environment = {"PYTHONPATH": "/work/runtime"}
            if cache_directory is not None:
                container_cache = work / "cache"
                if cache_directory.exists():
                    shutil.copytree(cache_directory.resolve(), container_cache, dirs_exist_ok=True, symlinks=False)
                command.extend(["--cache", "/work/cache"])
        else:
            command = [
                sys.executable,
                "-S",
                "-m",
                "x86decomp",
                "compile",
                str(profile_copy),
                str(source_copy),
                str(worker_output),
                "--report",
                str(compiler_report),
            ]
            environment = {"PYTHONPATH": str(runtime_root)}
            if cache_directory is not None:
                command.extend(["--cache", str(cache_directory.resolve())])
        request = WorkerRequest(
            command=tuple(command),
            working_directory=work,
            input_files=(profile_copy.relative_to(work), source_copy.relative_to(work)),
            expected_outputs=(worker_output.relative_to(work), compiler_report.relative_to(work)),
            isolation=isolation,
            container_image=container_image,
            environment=environment,
            limits=limits or WorkerLimits(timeout_seconds=int(load_profile(profile_path)["timeout_seconds"]) + 30),
        )
        worker_result = execute_worker_request(request, log_directory=work / "logs")
        if worker_result.status != "passed":
            result = {
                "schema_version": 1,
                "kind": "compiler_worker",
                "created_at": utc_now(),
                "success": False,
                "isolation": isolation,
                "worker": worker_result.to_dict(),
                "compiler": None,
            }
            if report_path is not None:
                write_json(report_path, result)
            raise ExternalToolError(f"compiler worker failed: {worker_result.error or worker_result.status}")
        shutil.copy2(worker_output, output_path)
        if isolation == "container" and cache_directory is not None and (work / "cache").is_dir():
            cache_directory.resolve().mkdir(parents=True, exist_ok=True)
            shutil.copytree(work / "cache", cache_directory.resolve(), dirs_exist_ok=True, symlinks=False)
        compiler = load_json(compiler_report)
        result = {
            "schema_version": 1,
            "kind": "compiler_worker",
            "created_at": utc_now(),
            "success": True,
            "isolation": isolation,
            "worker": worker_result.to_dict(),
            "compiler": compiler,
            "output": str(output_path),
            "output_sha256": sha256_file(output_path),
        }
        if report_path is not None:
            write_json(report_path, result)
        return result
