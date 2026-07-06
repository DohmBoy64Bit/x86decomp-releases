"""Version-agnostic, manifest-driven objdiff CLI integration.

objdiff's CLI/configuration evolves independently. This adapter executes an explicit
argument array, captures provenance, and imports a declared JSON/text output without
hard-coding unstable flags. It is a real external-tool boundary, not a fake diff.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from .errors import ContractError, ExternalToolError
from .util import load_json, sha256_file, utc_now, write_json

_ALLOWED_TOKENS = {"{target}", "{candidate}", "{output}", "{workdir}"}


def _resolve_executable(value: Any) -> str:
    """Support resolve executable processing for internal toolkit callers."""
    if not isinstance(value, str) or not value:
        raise ContractError("objdiff executable must be a non-empty string")
    explicit = Path(value).expanduser()
    if explicit.is_absolute() or explicit.parent != Path("."):
        if not explicit.is_file():
            raise ExternalToolError(f"objdiff executable is unavailable: {explicit}")
        return str(explicit.resolve())
    found = shutil.which(value)
    if found is None:
        raise ExternalToolError(f"objdiff executable is unavailable: {value}")
    return found


def run_objdiff_manifest(
    manifest_path: Path,
    *,
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Run objdiff manifest for the current toolkit workflow."""
    manifest = load_json(manifest_path)
    if not isinstance(manifest, dict) or manifest.get("schema_version") != 1:
        raise ContractError("objdiff manifest must be a schema_version 1 object")
    base = manifest_path.resolve().parent
    executable = _resolve_executable(manifest.get("executable", "objdiff-cli"))
    target = (base / str(manifest.get("target"))).resolve()
    candidate = (base / str(manifest.get("candidate"))).resolve()
    for name, path in (("target", target), ("candidate", candidate)):
        if not path.is_file():
            raise ContractError(f"objdiff {name} is missing: {path}")
    arguments = manifest.get("arguments")
    if not isinstance(arguments, list) or not arguments or not all(isinstance(item, str) for item in arguments):
        raise ContractError("objdiff arguments must be a non-empty array of strings")
    joined = "\n".join(arguments)
    for required in ("{target}", "{candidate}"):
        if required not in joined:
            raise ContractError(f"objdiff arguments must include {required}")
    unknown = {
        token
        for argument in arguments
        for token in re.findall(r"\{[^{}]+\}", argument)
        if token not in _ALLOWED_TOKENS
    }
    if unknown:
        raise ContractError("unsupported objdiff argument token(s): " + ", ".join(sorted(unknown)))
    timeout = manifest.get("timeout_seconds", 300)
    if not isinstance(timeout, int) or timeout <= 0:
        raise ContractError("objdiff timeout_seconds must be positive")
    success_codes = manifest.get("success_exit_codes", [0])
    if not isinstance(success_codes, list) or not success_codes or not all(isinstance(item, int) for item in success_codes):
        raise ContractError("objdiff success_exit_codes must be a non-empty integer array")
    env_raw = manifest.get("environment", {})
    if not isinstance(env_raw, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in env_raw.items()):
        raise ContractError("objdiff environment must be string-to-string")

    with tempfile.TemporaryDirectory(prefix="x86decomp-objdiff-") as temp_name:
        workdir = Path(temp_name).resolve()
        output_value = manifest.get("output", "objdiff-output.json")
        if not isinstance(output_value, str) or not output_value:
            raise ContractError("objdiff output must be a non-empty string")
        output = (workdir / output_value).resolve()
        try:
            output.relative_to(workdir)
        except ValueError as exc:
            raise ContractError("objdiff output escapes work directory") from exc
        output.parent.mkdir(parents=True, exist_ok=True)
        substitutions = {
            "{target}": str(target),
            "{candidate}": str(candidate),
            "{output}": str(output),
            "{workdir}": str(workdir),
        }
        command = [executable]
        for argument in arguments:
            for token, replacement in substitutions.items():
                argument = argument.replace(token, replacement)
            command.append(argument)
        environment = os.environ.copy() if manifest.get("inherit_environment", True) else {}
        environment.update(env_raw)
        try:
            completed = subprocess.run(
                command,
                cwd=workdir,
                env=environment,
                capture_output=True,
                text=True,
                timeout=timeout,
                check=False,
            )
            timed_out = False
        except subprocess.TimeoutExpired as exc:
            completed = None
            timed_out = True
            stdout = exc.stdout.decode(errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
            stderr = exc.stderr.decode(errors="replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "")
        if completed is not None:
            return_code = completed.returncode
            stdout = completed.stdout
            stderr = completed.stderr
        else:
            return_code = None
        parsed_output: Any = None
        output_hash = None
        output_size = None
        if output.is_file():
            output_hash = sha256_file(output)
            output_size = output.stat().st_size
            if manifest.get("output_format", "json") == "json":
                try:
                    parsed_output = load_json(output)
                except Exception as exc:
                    raise ContractError(f"objdiff declared JSON output is invalid: {exc}") from exc
            else:
                parsed_output = output.read_text(encoding="utf-8", errors="replace")
        require_output = manifest.get("require_output", True)
        if not isinstance(require_output, bool):
            raise ContractError("objdiff require_output must be boolean")
        success = not timed_out and return_code in success_codes and (output.is_file() or not require_output)
        report = {
            "schema_version": 1,
            "created_at": utc_now(),
            "kind": "objdiff_external_run",
            "manifest": str(manifest_path.resolve()),
            "command": command,
            "executable": executable,
            "executable_sha256": sha256_file(Path(executable)),
            "target": str(target),
            "target_sha256": sha256_file(target),
            "candidate": str(candidate),
            "candidate_sha256": sha256_file(candidate),
            "return_code": return_code,
            "timed_out": timed_out,
            "stdout": stdout,
            "stderr": stderr,
            "output_sha256": output_hash,
            "output_size": output_size,
            "parsed_output": parsed_output,
            "success": success,
            "limitations": [
                "The adapter reports the configured objdiff process result; acceptance semantics remain project-defined.",
                "The manifest pins the exact arguments because objdiff CLI/configuration versions may differ.",
            ],
        }
        if report_path is not None:
            write_json(report_path, report)
        if not success:
            reason = "timeout" if timed_out else f"exit code {return_code}"
            raise ExternalToolError(f"objdiff invocation failed ({reason}): {stderr.strip()}")
        return report
