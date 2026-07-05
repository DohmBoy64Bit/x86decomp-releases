"""Safe command construction for Ghidra headless analysis."""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any

from .errors import ContractError, ExternalToolError
from .tools import discover_analyze_headless
from .util import utc_now, write_json


def build_export_command(
    *,
    binary: Path,
    ghidra_project_dir: Path,
    ghidra_project_name: str,
    scripts_dir: Path,
    output_dir: Path,
    ghidra_home: Path | None = None,
    overwrite: bool = False,
    function_selector: str = "all",
) -> list[str]:
    """Build export command.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    executable = discover_analyze_headless(ghidra_home)
    if executable is None:
        raise ExternalToolError("Ghidra analyzeHeadless was not found; set GHIDRA_HOME")
    if not binary.is_file():
        raise ContractError(f"binary does not exist: {binary}")
    if not scripts_dir.is_dir():
        raise ContractError(f"Ghidra scripts directory does not exist: {scripts_dir}")
    for required_script in ("ExportProjectManifest.java", "ExportFunctionArtifacts.java"):
        if not (scripts_dir / required_script).is_file():
            raise ContractError(f"required Ghidra script is missing: {required_script}")
    if not ghidra_project_name.strip() or any(ch in ghidra_project_name for ch in "/\\"):
        raise ContractError("ghidra_project_name must be a simple non-empty name")
    ghidra_project_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    command = [
        str(executable),
        str(ghidra_project_dir.resolve()),
        ghidra_project_name,
        "-import",
        str(binary.resolve()),
    ]
    if overwrite:
        command.append("-overwrite")
    command.extend(
        [
            "-scriptPath",
            str(scripts_dir.resolve()),
            "-postScript",
            "ExportProjectManifest.java",
            str(output_dir.resolve()),
            "-postScript",
            "ExportFunctionArtifacts.java",
            str(output_dir.resolve()),
            function_selector,
        ]
    )
    return command


def run_export(command: list[str], *, timeout_seconds: int, report_path: Path | None = None) -> dict[str, Any]:
    """Run export.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if timeout_seconds <= 0:
        raise ContractError("timeout_seconds must be positive")
    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            check=False,
        )
        report = {
            "schema_version": 1,
            "finished_at": utc_now(),
            "command": command,
            "return_code": completed.returncode,
            "stdout": completed.stdout,
            "stderr": completed.stderr,
            "success": completed.returncode == 0,
            "timed_out": False,
        }
    except subprocess.TimeoutExpired as exc:
        report = {
            "schema_version": 1,
            "finished_at": utc_now(),
            "command": command,
            "return_code": None,
            "stdout": exc.stdout.decode(errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or ""),
            "stderr": exc.stderr.decode(errors="replace") if isinstance(exc.stderr, bytes) else (exc.stderr or ""),
            "success": False,
            "timed_out": True,
        }
    if report_path is not None:
        write_json(report_path, report)
    if not report["success"]:
        raise ExternalToolError(
            "Ghidra headless export failed: "
            + ("timeout" if report["timed_out"] else f"exit code {report['return_code']}")
        )
    return report
