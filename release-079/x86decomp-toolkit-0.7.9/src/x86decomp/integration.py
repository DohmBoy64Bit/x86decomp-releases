"""Manifest-driven integration scenario runner.

This module performs real target/candidate process executions with explicit host
execution consent or an external isolation wrapper. It compares only declared
observations and never treats finite scenarios as universal equivalence proof.
"""

from __future__ import annotations

import base64
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from .errors import ContractError, ExternalToolError
from .util import load_json, sha256_bytes, sha256_file, utc_now, write_json

_ALLOWED_TOKENS = {"{artifact}", "{workdir}"}


def _require_string_list(value: Any, name: str, *, nonempty: bool = False) -> list[str]:
    """Implement require string list.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ContractError(f"{name} must be an array of strings")
    if nonempty and not value:
        raise ContractError(f"{name} must not be empty")
    return list(value)


def _resolve_existing(base: Path, value: Any, name: str) -> Path:
    """Resolve existing.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if not isinstance(value, str) or not value:
        raise ContractError(f"{name} must be a non-empty string")
    path = (base / value).resolve()
    if not path.is_file():
        raise ContractError(f"{name} does not exist or is not a file: {path}")
    return path


def _parse_stdin(base: Path, value: Any) -> bytes:
    """Parse stdin.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if value is None:
        return b""
    if not isinstance(value, dict):
        raise ContractError("stdin must be an object")
    present = [key for key in ("text", "base64", "file") if key in value]
    if len(present) != 1:
        raise ContractError("stdin must contain exactly one of text, base64, or file")
    key = present[0]
    raw = value[key]
    if not isinstance(raw, str):
        raise ContractError(f"stdin.{key} must be a string")
    if key == "text":
        return raw.encode("utf-8")
    if key == "base64":
        try:
            return base64.b64decode(raw, validate=True)
        except ValueError as exc:
            raise ContractError("stdin.base64 is invalid") from exc
    return _resolve_existing(base, raw, "stdin.file").read_bytes()


def _copy_fixtures(base: Path, workdir: Path, fixtures: Any) -> list[dict[str, Any]]:
    """Copy fixtures.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if fixtures is None:
        return []
    if not isinstance(fixtures, list):
        raise ContractError("fixtures must be an array")
    copied: list[dict[str, Any]] = []
    root = workdir.resolve()
    for index, item in enumerate(fixtures):
        if not isinstance(item, dict):
            raise ContractError(f"fixture {index} must be an object")
        source = _resolve_existing(base, item.get("source"), f"fixtures[{index}].source")
        destination_value = item.get("destination")
        if not isinstance(destination_value, str) or not destination_value:
            raise ContractError(f"fixtures[{index}].destination must be a non-empty string")
        destination = (workdir / destination_value).resolve()
        try:
            destination.relative_to(root)
        except ValueError as exc:
            raise ContractError(f"fixture destination escapes work directory: {destination_value}") from exc
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        copied.append(
            {
                "source": str(source),
                "source_sha256": sha256_file(source),
                "destination": destination_value,
            }
        )
    return copied


def _substitute_command(command: list[str], *, artifact: Path, workdir: Path) -> list[str]:
    """Implement substitute command.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    result: list[str] = []
    for argument in command:
        unknown = [
            token
            for token in argument.split()
            if token.startswith("{") and token.endswith("}") and token not in _ALLOWED_TOKENS
        ]
        if unknown:
            raise ContractError(f"unsupported integration command token(s): {', '.join(unknown)}")
        result.append(argument.replace("{artifact}", str(artifact)).replace("{workdir}", str(workdir)))
    return result


def _bounded_output(data: bytes, limit: int) -> dict[str, Any]:
    """Implement bounded output.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    shown = data[:limit]
    return {
        "sha256": sha256_bytes(data),
        "size": len(data),
        "truncated": len(data) > limit,
        "utf8": shown.decode("utf-8", errors="replace"),
        "captured_size": len(shown),
    }


def _run_side(
    *,
    base: Path,
    scenario_id: str,
    side_name: str,
    spec: Any,
    wrapper_prefix: list[str],
    timeout_seconds: int,
    stdin_data: bytes,
    fixtures: Any,
    output_limit: int,
) -> tuple[dict[str, Any], Path]:
    """Run side.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if not isinstance(spec, dict):
        raise ContractError(f"scenario {scenario_id} {side_name} must be an object")
    artifact = _resolve_existing(base, spec.get("artifact"), f"scenario {scenario_id} {side_name}.artifact")
    command_raw = _require_string_list(spec.get("command"), f"scenario {scenario_id} {side_name}.command", nonempty=True)
    environment_raw = spec.get("environment", {})
    if not isinstance(environment_raw, dict) or not all(
        isinstance(key, str) and isinstance(value, str) for key, value in environment_raw.items()
    ):
        raise ContractError(f"scenario {scenario_id} {side_name}.environment must be string-to-string")
    inherit_environment = spec.get("inherit_environment", True)
    if not isinstance(inherit_environment, bool):
        raise ContractError(f"scenario {scenario_id} {side_name}.inherit_environment must be boolean")

    temporary = tempfile.TemporaryDirectory(prefix=f"x86decomp-integration-{scenario_id}-{side_name}-")
    workdir = Path(temporary.name).resolve()
    # Keep the TemporaryDirectory alive until after observations are captured by
    # attaching it to the report temporarily. It is removed before serialization.
    copied = _copy_fixtures(base, workdir, fixtures)
    command = [*wrapper_prefix, *_substitute_command(command_raw, artifact=artifact, workdir=workdir)]
    environment = os.environ.copy() if inherit_environment else {}
    environment.update(environment_raw)
    started_at = utc_now()
    try:
        try:
            completed = subprocess.run(
                command,
                input=stdin_data,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=workdir,
                env=environment,
                timeout=timeout_seconds,
                check=False,
            )
            timed_out = False
            return_code: int | None = completed.returncode
            stdout = completed.stdout
            stderr = completed.stderr
        except subprocess.TimeoutExpired as exc:
            timed_out = True
            return_code = None
            stdout = exc.stdout or b""
            stderr = exc.stderr or b""
        report = {
            "side": side_name,
            "artifact": str(artifact),
            "artifact_sha256": sha256_file(artifact),
            "command": command,
            "working_directory": str(workdir),
            "fixtures": copied,
            "started_at": started_at,
            "finished_at": utc_now(),
            "return_code": return_code,
            "timed_out": timed_out,
            "stdout": _bounded_output(stdout, output_limit),
            "stderr": _bounded_output(stderr, output_limit),
            "_stdout_bytes": stdout,
            "_stderr_bytes": stderr,
            "_temporary_directory": temporary,
        }
        return report, workdir
    except Exception:
        temporary.cleanup()
        raise


def _observe_file(workdir: Path, item: Any, *, side: str, index: int, output_limit: int) -> dict[str, Any]:
    """Implement observe file.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if not isinstance(item, dict):
        raise ContractError(f"observations.files[{index}] must be an object")
    relative = item.get("path")
    if not isinstance(relative, str) or not relative:
        raise ContractError(f"observations.files[{index}].path must be a non-empty string")
    mode = item.get("mode", "sha256")
    if mode not in ("sha256", "bytes", "text"):
        raise ContractError(f"observations.files[{index}].mode must be sha256, bytes, or text")
    optional = item.get("optional", False)
    if not isinstance(optional, bool):
        raise ContractError(f"observations.files[{index}].optional must be boolean")
    root = workdir.resolve()
    path = (workdir / relative).resolve()
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise ContractError(f"observed file escapes work directory: {relative}") from exc
    if not path.is_file():
        return {
            "side": side,
            "path": relative,
            "mode": mode,
            "optional": optional,
            "exists": False,
            "value": None,
        }
    data = path.read_bytes()
    if mode == "sha256":
        value: Any = sha256_bytes(data)
    elif mode == "bytes":
        value = {
            "sha256": sha256_bytes(data),
            "size": len(data),
            "base64": base64.b64encode(data[:output_limit]).decode("ascii"),
            "truncated": len(data) > output_limit,
        }
    else:
        value = {
            "sha256": sha256_bytes(data),
            "size": len(data),
            "utf8": data[:output_limit].decode("utf-8", errors="replace"),
            "truncated": len(data) > output_limit,
        }
    return {
        "side": side,
        "path": relative,
        "mode": mode,
        "optional": optional,
        "exists": True,
        "value": value,
    }


def _compare_stream(name: str, mode: Any, target: bytes, candidate: bytes) -> dict[str, Any] | None:
    """Compare stream.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if mode in (None, "ignore"):
        return None
    if mode not in ("exact", "sha256"):
        raise ContractError(f"observations.{name} must be ignore, exact, or sha256")
    if mode == "exact":
        equal = target == candidate
        target_value: Any = {"sha256": sha256_bytes(target), "size": len(target)}
        candidate_value: Any = {"sha256": sha256_bytes(candidate), "size": len(candidate)}
    else:
        target_value = sha256_bytes(target)
        candidate_value = sha256_bytes(candidate)
        equal = target_value == candidate_value
    return {
        "observation": name,
        "mode": mode,
        "equal": equal,
        "target": target_value,
        "candidate": candidate_value,
    }


def run_integration_scenarios(
    manifest_path: Path,
    *,
    allow_host_execution: bool = False,
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Execute and compare all declared integration scenarios.

    Host execution is rejected unless both the manifest selects ``host_explicit`` and
    the caller supplies ``allow_host_execution=True``. ``external_wrapper`` requires a
    non-empty wrapper command but the toolkit cannot independently prove the wrapper is
    a complete sandbox; this limitation is recorded in the report.
    """

    manifest = load_json(manifest_path)
    if not isinstance(manifest, dict):
        raise ContractError("integration manifest must be an object")
    if manifest.get("schema_version") != 1:
        raise ContractError("unsupported integration manifest schema_version")
    base = manifest_path.resolve().parent
    execution = manifest.get("execution")
    if not isinstance(execution, dict):
        raise ContractError("integration execution must be an object")
    execution_mode = execution.get("mode")
    if execution_mode == "host_explicit":
        if not allow_host_execution:
            raise ContractError(
                "host integration execution requires the explicit --allow-host-execution flag"
            )
        if execution.get("acknowledge_untrusted_code_risk") is not True:
            raise ContractError(
                "host_explicit execution requires acknowledge_untrusted_code_risk=true"
            )
        wrapper_prefix: list[str] = []
    elif execution_mode == "external_wrapper":
        wrapper_prefix = _require_string_list(
            execution.get("command_prefix"), "execution.command_prefix", nonempty=True
        )
    else:
        raise ContractError("execution.mode must be host_explicit or external_wrapper")

    scenarios = manifest.get("scenarios")
    if not isinstance(scenarios, list) or not scenarios:
        raise ContractError("integration scenarios must be a non-empty array")
    output_limit = manifest.get("captured_output_limit", 1024 * 1024)
    if not isinstance(output_limit, int) or output_limit <= 0:
        raise ContractError("captured_output_limit must be a positive integer")

    results: list[dict[str, Any]] = []
    for index, scenario in enumerate(scenarios):
        if not isinstance(scenario, dict):
            raise ContractError(f"integration scenario {index} must be an object")
        scenario_id = scenario.get("id")
        if not isinstance(scenario_id, str) or not scenario_id:
            raise ContractError(f"integration scenario {index}.id must be a non-empty string")
        timeout_seconds = scenario.get("timeout_seconds", 60)
        if not isinstance(timeout_seconds, int) or timeout_seconds <= 0:
            raise ContractError(f"scenario {scenario_id}.timeout_seconds must be positive")
        stdin_data = _parse_stdin(base, scenario.get("stdin"))
        target_report: dict[str, Any] | None = None
        candidate_report: dict[str, Any] | None = None
        try:
            target_report, target_workdir = _run_side(
                base=base,
                scenario_id=scenario_id,
                side_name="target",
                spec=scenario.get("target"),
                wrapper_prefix=wrapper_prefix,
                timeout_seconds=timeout_seconds,
                stdin_data=stdin_data,
                fixtures=scenario.get("fixtures"),
                output_limit=output_limit,
            )
            candidate_report, candidate_workdir = _run_side(
                base=base,
                scenario_id=scenario_id,
                side_name="candidate",
                spec=scenario.get("candidate"),
                wrapper_prefix=wrapper_prefix,
                timeout_seconds=timeout_seconds,
                stdin_data=stdin_data,
                fixtures=scenario.get("fixtures"),
                output_limit=output_limit,
            )
            observations = scenario.get("observations", {})
            if not isinstance(observations, dict):
                raise ContractError(f"scenario {scenario_id}.observations must be an object")
            comparisons: list[dict[str, Any]] = []
            if observations.get("exit_code", True):
                comparisons.append(
                    {
                        "observation": "exit_code",
                        "mode": "exact",
                        "equal": target_report["return_code"] == candidate_report["return_code"],
                        "target": target_report["return_code"],
                        "candidate": candidate_report["return_code"],
                    }
                )
            stdout_comparison = _compare_stream(
                "stdout",
                observations.get("stdout", "exact"),
                target_report["_stdout_bytes"],
                candidate_report["_stdout_bytes"],
            )
            if stdout_comparison is not None:
                comparisons.append(stdout_comparison)
            stderr_comparison = _compare_stream(
                "stderr",
                observations.get("stderr", "exact"),
                target_report["_stderr_bytes"],
                candidate_report["_stderr_bytes"],
            )
            if stderr_comparison is not None:
                comparisons.append(stderr_comparison)

            files = observations.get("files", [])
            if not isinstance(files, list):
                raise ContractError(f"scenario {scenario_id}.observations.files must be an array")
            file_observations: list[dict[str, Any]] = []
            for file_index, file_contract in enumerate(files):
                target_file = _observe_file(
                    target_workdir,
                    file_contract,
                    side="target",
                    index=file_index,
                    output_limit=output_limit,
                )
                candidate_file = _observe_file(
                    candidate_workdir,
                    file_contract,
                    side="candidate",
                    index=file_index,
                    output_limit=output_limit,
                )
                optional = bool(target_file["optional"])
                equal = (
                    target_file["exists"] == candidate_file["exists"]
                    and target_file["value"] == candidate_file["value"]
                )
                if optional and not target_file["exists"] and not candidate_file["exists"]:
                    equal = True
                comparison = {
                    "observation": f"file:{target_file['path']}",
                    "mode": target_file["mode"],
                    "optional": optional,
                    "equal": equal,
                    "target": target_file,
                    "candidate": candidate_file,
                }
                comparisons.append(comparison)
                file_observations.append(comparison)

            timed_out = bool(target_report["timed_out"] or candidate_report["timed_out"])
            equivalent = not timed_out and all(item["equal"] for item in comparisons)
            # Remove process-only values before serialization.
            target_report.pop("_stdout_bytes", None)
            target_report.pop("_stderr_bytes", None)
            candidate_report.pop("_stdout_bytes", None)
            candidate_report.pop("_stderr_bytes", None)
            result = {
                "id": scenario_id,
                "equivalent_for_scenario": equivalent,
                "timed_out": timed_out,
                "target": target_report,
                "candidate": candidate_report,
                "comparisons": comparisons,
                "file_observations": file_observations,
                "limitations": [
                    "Result applies only to the declared scenario, inputs, environment, and observations.",
                    "The toolkit does not infer unobserved process state or universal equivalence.",
                ],
            }
            results.append(result)
        finally:
            for report in (target_report, candidate_report):
                if report is not None:
                    temporary = report.pop("_temporary_directory", None)
                    if temporary is not None:
                        temporary.cleanup()

    passed = sum(1 for result in results if result["equivalent_for_scenario"])
    report = {
        "schema_version": 1,
        "created_at": utc_now(),
        "kind": "integration_scenarios",
        "name": manifest.get("name"),
        "execution": {
            "mode": execution_mode,
            "wrapper_prefix": wrapper_prefix,
            "host_execution_explicitly_allowed": allow_host_execution,
            "isolation_verified_by_toolkit": False,
        },
        "scenario_count": len(results),
        "passed_count": passed,
        "failed_count": len(results) - passed,
        "all_scenarios_equivalent": passed == len(results),
        "scenarios": results,
        "limitations": [
            "Finite integration scenarios are not proof of equivalence for all inputs or environments.",
            "External-wrapper isolation is declared by the manifest and is not independently certified by this runner.",
        ],
    }
    if report_path is not None:
        write_json(report_path, report)
    return report
