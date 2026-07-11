"""Deterministic external compiler profile execution and cache keys."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from .errors import ContractError, ExternalToolError
from .util import canonical_json_bytes, load_json, sha256_bytes, sha256_file, utc_now, write_json

_ALLOWED_TOKENS = {"{source}", "{output}", "{workdir}"}


def load_profile(path: Path) -> dict[str, Any]:
    """Load profile."""
    value = load_json(path)
    if not isinstance(value, dict):
        raise ContractError("compiler profile must be a JSON object")
    required = ("schema_version", "id", "executable", "arguments", "timeout_seconds", "output_kind")
    for key in required:
        if key not in value:
            raise ContractError(f"compiler profile is missing {key}")
    if value["schema_version"] not in (1, 2):
        raise ContractError("unsupported compiler profile schema")
    if not isinstance(value["arguments"], list) or not all(isinstance(arg, str) for arg in value["arguments"]):
        raise ContractError("compiler profile arguments must be an array of strings")
    joined = "\n".join(value["arguments"])
    for token in ("{source}", "{output}"):
        if token not in joined:
            raise ContractError(f"compiler profile arguments must include {token}")
    unknown_tokens = {
        fragment
        for argument in value["arguments"]
        for fragment in re.findall(r"\{[^{}]+\}", argument)
        if fragment not in _ALLOWED_TOKENS
    }
    if unknown_tokens:
        raise ContractError("compiler profile contains unsupported substitution token(s): " + ", ".join(sorted(unknown_tokens)))
    if not isinstance(value["timeout_seconds"], int) or value["timeout_seconds"] <= 0:
        raise ContractError("timeout_seconds must be a positive integer")
    env = value.get("environment", {})
    if not isinstance(env, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in env.items()):
        raise ContractError("environment must be a string-to-string object")
    prefix = value.get("command_prefix", [])
    if not isinstance(prefix, list) or not all(isinstance(item, str) for item in prefix):
        raise ContractError("command_prefix must be an array of strings")
    if "family" in value and not isinstance(value["family"], str):
        raise ContractError("family must be a string")
    if "version" in value and not isinstance(value["version"], str):
        raise ContractError("version must be a string")
    return value


def _tool_version(executable: str, version_arguments: list[str] | None = None) -> str | None:
    """Query a compiler executable for its version string."""
    try:
        completed = subprocess.run(
            [executable, *(version_arguments or ["--version"])],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    output = (completed.stdout or completed.stderr).strip()
    return output.splitlines()[0] if output else None


def _resolve_executable(value: str) -> str:
    """Resolve executable."""
    explicit = Path(value).expanduser()
    if explicit.is_absolute() or explicit.parent != Path("."):
        if not explicit.is_file():
            raise ExternalToolError(f"compiler executable is not available: {explicit}")
        return str(explicit.resolve())
    discovered = shutil.which(value)
    if discovered is None:
        raise ExternalToolError(f"compiler executable is not available: {value}")
    return discovered


def compiler_cache_key(
    profile: dict[str, Any],
    *,
    executable_sha256: str,
    source_sha256: str,
    extra_arguments: list[str],
) -> str:
    """Build the deterministic cache key for a compiler invocation."""
    payload = {
        "profile": profile,
        "executable_sha256": executable_sha256,
        "source_sha256": source_sha256,
        "extra_arguments": extra_arguments,
    }
    return sha256_bytes(canonical_json_bytes(payload))


def run_compiler_profile(
    profile_path: Path,
    source: Path,
    output: Path,
    *,
    report_path: Path | None = None,
    extra_arguments: list[str] | None = None,
    working_directory: Path | None = None,
    cache_directory: Path | None = None,
) -> dict[str, Any]:
    """Run compiler profile."""
    profile = load_profile(profile_path)
    source = source.resolve()
    output = output.resolve()
    if not source.is_file():
        raise ContractError(f"source file does not exist: {source}")
    if source == output:
        raise ContractError("source and output must be different paths")
    executable = _resolve_executable(str(profile["executable"]))
    executable_hash = sha256_file(Path(executable))
    source_hash = sha256_file(source)
    extra = list(extra_arguments or [])
    if not all(isinstance(arg, str) for arg in extra):
        raise ContractError("extra_arguments must contain strings")
    cache_key = compiler_cache_key(
        profile,
        executable_sha256=executable_hash,
        source_sha256=source_hash,
        extra_arguments=extra,
    )
    if cache_directory is not None:
        cache_root = cache_directory.resolve() / cache_key
        cached_output = cache_root / "output.bin"
        cached_report = cache_root / "report.json"
        if cached_output.is_file() and cached_report.is_file():
            output.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(cached_output, output)
            report = load_json(cached_report)
            report["cache_hit"] = True
            report["output"] = str(output)
            if report_path is not None:
                write_json(report_path, report)
            return report

    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        if not output.is_file():
            raise ContractError(f"compiler output path is not a regular file: {output}")
        output.unlink()
    temporary_workdir: tempfile.TemporaryDirectory[str] | None = None
    if working_directory is None:
        temporary_workdir = tempfile.TemporaryDirectory(prefix="x86decomp-compile-")
        workdir = Path(temporary_workdir.name).resolve()
    else:
        workdir = working_directory.resolve()
        workdir.mkdir(parents=True, exist_ok=True)
    substitutions = {"{source}": str(source), "{output}": str(output), "{workdir}": str(workdir)}
    arguments = []
    for argument in profile["arguments"]:
        for token, replacement in substitutions.items():
            argument = argument.replace(token, replacement)
        arguments.append(argument)
    command = [*profile.get("command_prefix", []), executable, *arguments, *extra]
    if profile.get("inherit_environment", True):
        environment = os.environ.copy()
    else:
        environment = {}
    environment.update(profile.get("environment", {}))
    started_at = utc_now()
    try:
        try:
            completed = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=profile["timeout_seconds"],
                env=environment,
                cwd=workdir,
                check=False,
            )
            timed_out = False
        except subprocess.TimeoutExpired as exc:
            completed = None
            timed_out = True
            stdout = exc.stdout.decode(errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
            stderr = exc.stderr.decode(errors="replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "")
        if completed is not None:
            stdout = completed.stdout
            stderr = completed.stderr
            return_code = completed.returncode
        else:
            return_code = None
        report = {
            "schema_version": 2,
            "profile_id": profile["id"],
            "profile_path": str(profile_path.resolve()),
            "family": profile.get("family"),
            "version": profile.get("version"),
            "started_at": started_at,
            "finished_at": utc_now(),
            "command": command,
            "working_directory": str(workdir),
            "executable": executable,
            "executable_sha256": executable_hash,
            "executable_version": _tool_version(executable, profile.get("version_arguments")),
            "source": str(source),
            "source_sha256": source_hash,
            "output": str(output),
            "output_kind": profile["output_kind"],
            "extra_arguments": extra,
            "cache_key": cache_key,
            "cache_hit": False,
            "return_code": return_code,
            "timed_out": timed_out,
            "stdout": stdout,
            "stderr": stderr,
            "success": return_code == 0 and output.is_file(),
            "output_sha256": sha256_file(output) if output.is_file() else None,
            "output_size": output.stat().st_size if output.is_file() else None,
        }
        if report["success"] and cache_directory is not None:
            cache_root = cache_directory.resolve() / cache_key
            cache_root.mkdir(parents=True, exist_ok=True)
            shutil.copy2(output, cache_root / "output.bin")
            write_json(cache_root / "report.json", report)
        if report_path is not None:
            write_json(report_path, report)
        if not report["success"]:
            reason = "timed out" if timed_out else f"exit code {return_code}"
            raise ExternalToolError(f"compiler failed ({reason}); stderr: {stderr.strip()}")
        return report
    finally:
        if temporary_workdir is not None:
            temporary_workdir.cleanup()
