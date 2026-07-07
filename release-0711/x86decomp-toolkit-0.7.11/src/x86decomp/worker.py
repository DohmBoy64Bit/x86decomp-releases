"""Bounded command workers with explicit isolation and provenance.

The local worker provides resource and output bounds without pretending to be a
security boundary.  Container mode invokes Docker or Podman with a read-only
root, no network, dropped capabilities, and explicit mounts.
"""

from __future__ import annotations

import os
import platform
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

from .errors import ContractError, ExternalToolError
from .util import sha256_file, utc_now, write_json


@dataclass(frozen=True)
class WorkerLimits:
    """Store validated worker limits fields used by toolkit reports and adapters."""
    timeout_seconds: int = 300
    memory_bytes: int = 2 * 1024 * 1024 * 1024
    cpu_seconds: int = 300
    max_output_bytes: int = 16 * 1024 * 1024
    max_processes: int = 512

    def validate(self) -> None:
        """Validate validate for the current toolkit workflow."""
        for name, value in vars(self).items():
            if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
                raise ContractError(f"worker limit {name} must be a positive integer")


@dataclass(frozen=True)
class WorkerRequest:
    """Store validated worker request fields used by toolkit reports and adapters."""
    command: tuple[str, ...]
    working_directory: Path
    environment: dict[str, str] = field(default_factory=dict)
    input_files: tuple[Path, ...] = ()
    expected_outputs: tuple[Path, ...] = ()
    isolation: str = "local_bounded"
    container_image: str | None = None
    limits: WorkerLimits = WorkerLimits()


@dataclass(frozen=True)
class WorkerResult:
    """Store validated worker result fields used by toolkit reports and adapters."""
    status: str
    returncode: int | None
    started_at: str
    duration_seconds: float
    command: tuple[str, ...]
    isolation: str
    isolation_strength: str
    stdout_path: Path
    stderr_path: Path
    stdout_truncated: bool
    stderr_truncated: bool
    input_hashes: dict[str, str]
    output_hashes: dict[str, str]
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "schema_version": 1,
            "status": self.status,
            "returncode": self.returncode,
            "started_at": self.started_at,
            "duration_seconds": self.duration_seconds,
            "command": list(self.command),
            "isolation": self.isolation,
            "isolation_strength": self.isolation_strength,
            "stdout_path": str(self.stdout_path),
            "stderr_path": str(self.stderr_path),
            "stdout_truncated": self.stdout_truncated,
            "stderr_truncated": self.stderr_truncated,
            "input_hashes": self.input_hashes,
            "output_hashes": self.output_hashes,
            "error": self.error,
        }


def discover_worker_capabilities() -> dict[str, Any]:
    """Discover worker capabilities for the current toolkit workflow."""
    docker = shutil.which("docker")
    podman = shutil.which("podman")
    return {
        "platform": platform.platform(),
        "local_bounded": True,
        "posix_resource_limits": os.name == "posix",
        "container_runtime": "docker" if docker else "podman" if podman else None,
        "container_runtime_path": docker or podman,
        "network_namespace_enforced_in_local_mode": False,
        "container_network_none_supported": bool(docker or podman),
    }


def _bounded_environment(extra: dict[str, str], working_directory: Path) -> dict[str, str]:
    """Support bounded environment processing for internal toolkit callers."""
    allowed = {
        "PATH",
        "SYSTEMROOT",
        "WINDIR",
        "COMSPEC",
        "PATHEXT",
        "TEMP",
        "TMP",
        "HOME",
        "USERPROFILE",
        "LANG",
        "LC_ALL",
        "PYTHONPATH",
    }
    environment = {key: value for key, value in os.environ.items() if key in allowed}
    environment.update(
        {
            "PYTHONHASHSEED": "0",
            "SOURCE_DATE_EPOCH": "0",
            "TZ": "UTC",
            "X86DECOMP_WORKER_ROOT": str(working_directory),
            "OPENBLAS_NUM_THREADS": "1",
            "OMP_NUM_THREADS": "1",
            "MKL_NUM_THREADS": "1",
            "NUMEXPR_NUM_THREADS": "1",
        }
    )
    for key, value in extra.items():
        if not isinstance(key, str) or not isinstance(value, str) or "\x00" in key + value:
            raise ContractError("worker environment must contain valid strings")
        environment[key] = value
    return environment


def _preexec(limits: WorkerLimits) -> Any:
    """Return the legacy resource-limit callback for API compatibility.

    The production launcher no longer passes this callback to ``Popen`` because
    Python code executed between fork and exec can deadlock in a process that
    has already initialized threads.  the exec-based resource wrapper applies the
    same limits in a fresh Python interpreter immediately before ``exec``.
    """
    if os.name != "posix":
        return None

    def apply() -> None:
        """Execute the apply operation for the current toolkit workflow."""
        import resource

        resource.setrlimit(resource.RLIMIT_CPU, (limits.cpu_seconds, limits.cpu_seconds + 1))
        resource.setrlimit(resource.RLIMIT_AS, (limits.memory_bytes, limits.memory_bytes))
        resource.setrlimit(resource.RLIMIT_NPROC, (limits.max_processes, limits.max_processes))
        resource.setrlimit(
            resource.RLIMIT_FSIZE,
            (limits.max_output_bytes * 4, limits.max_output_bytes * 4),
        )
        os.setsid()

    return apply


def _confined_paths(root: Path, values: tuple[Path, ...], *, must_exist: bool) -> tuple[Path, ...]:
    """Support confined paths processing for internal toolkit callers."""
    root = root.resolve()
    result: list[Path] = []
    for value in values:
        path = value if value.is_absolute() else root / value
        resolved = path.resolve(strict=False)
        try:
            resolved.relative_to(root)
        except ValueError as exc:
            raise ContractError(f"worker path escapes working directory: {value}") from exc
        if must_exist and (not resolved.is_file() or resolved.is_symlink()):
            raise ContractError(f"worker input must be a regular file: {resolved}")
        result.append(resolved)
    return tuple(result)


def _container_command(request: WorkerRequest, runtime: str) -> tuple[str, ...]:
    """Support container command processing for internal toolkit callers."""
    if request.container_image is None or not request.container_image.strip():
        raise ContractError("container isolation requires container_image")
    work = request.working_directory.resolve()
    command = [
        runtime,
        "run",
        "--rm",
        "--network=none",
        "--read-only",
        "--cap-drop=ALL",
        "--security-opt=no-new-privileges",
        f"--memory={request.limits.memory_bytes}",
        f"--pids-limit={request.limits.max_processes}",
        "--mount",
        f"type=bind,src={work},dst=/work",
        "--workdir=/work",
        "--tmpfs=/tmp:rw,noexec,nosuid,size=256m",
    ]
    for key, value in sorted(request.environment.items()):
        command.extend(["--env", f"{key}={value}"])
    command.extend([request.container_image, *request.command])
    return tuple(command)


def execute_worker_request(
    request: WorkerRequest,
    *,
    log_directory: Path,
    report_path: Path | None = None,
    cancel_check: Callable[[], bool] | None = None,
) -> WorkerResult:
    """Execute the execute worker request operation for the current toolkit workflow."""
    request.limits.validate()
    if not request.command or not all(isinstance(item, str) and item and "\x00" not in item for item in request.command):
        raise ContractError("worker command must be a non-empty string array")
    work = request.working_directory.resolve()
    work.mkdir(parents=True, exist_ok=True)
    inputs = _confined_paths(work, request.input_files, must_exist=True)
    outputs = _confined_paths(work, request.expected_outputs, must_exist=False)
    input_hashes = {str(path.relative_to(work)): sha256_file(path) for path in inputs}
    log_directory = log_directory.resolve()
    log_directory.mkdir(parents=True, exist_ok=True)
    stdout_path = log_directory / "stdout.log"
    stderr_path = log_directory / "stderr.log"
    started = utc_now()
    start = time.monotonic()
    if request.isolation == "local_bounded":
        command = request.command
        isolation_strength = "resource_bounded_not_security_boundary"
        cwd = work
        environment = _bounded_environment(request.environment, work)
    elif request.isolation == "container":
        runtime = shutil.which("docker") or shutil.which("podman")
        if runtime is None:
            raise ExternalToolError("container worker requires Docker or Podman")
        command = _container_command(request, runtime)
        isolation_strength = "container_network_none_read_only_root"
        cwd = work
        environment = _bounded_environment({}, work)
    else:
        raise ContractError("worker isolation must be local_bounded or container")

    def resource_wrapped_command(value: tuple[str, ...]) -> tuple[str, ...]:
        """Execute the resource wrapped command operation for the current toolkit workflow."""
        if os.name != "posix":
            return value
        wrapper = (
            "import os,resource,sys;"
            "memory,cpu,processes,file_size=map(int,sys.argv[1:5]);"
            "resource.setrlimit(resource.RLIMIT_CPU,(cpu,cpu+1));"
            "resource.setrlimit(resource.RLIMIT_AS,(memory,memory));"
            "resource.setrlimit(resource.RLIMIT_NPROC,(processes,processes));"
            "resource.setrlimit(resource.RLIMIT_FSIZE,(file_size,file_size));"
            "argv=sys.argv[5:];"
            "os.execvpe(argv[0],argv,os.environ)"
        )
        return (
            sys.executable,
            "-c",
            wrapper,
            str(request.limits.memory_bytes),
            str(request.limits.cpu_seconds),
            str(request.limits.max_processes),
            str(request.limits.max_output_bytes * 4),
            *value,
        )

    launch_command = resource_wrapped_command(tuple(command))
    status = "error"
    returncode: int | None = None
    error: str | None = None
    stdout_truncated = stderr_truncated = False
    with tempfile.TemporaryDirectory(prefix="x86decomp-worker-capture-", dir=log_directory) as capture:
        raw_stdout = Path(capture) / "stdout.bin"
        raw_stderr = Path(capture) / "stderr.bin"
        try:
            with raw_stdout.open("wb") as out, raw_stderr.open("wb") as err:
                process = subprocess.Popen(
                    list(launch_command),
                    cwd=cwd,
                    env=environment,
                    stdin=subprocess.DEVNULL,
                    stdout=out,
                    stderr=err,
                    shell=False,
                    preexec_fn=None,
                    start_new_session=os.name == "posix",
                )
                deadline = time.monotonic() + request.limits.timeout_seconds
                while True:
                    try:
                        returncode = process.wait(timeout=min(0.25, max(0.01, deadline - time.monotonic())))
                        status = "passed" if returncode == 0 else "failed"
                        break
                    except subprocess.TimeoutExpired:
                        cancelled = cancel_check is not None and bool(cancel_check())
                        timed_out = time.monotonic() >= deadline
                        if not cancelled and not timed_out:
                            continue
                        status = "cancelled" if cancelled else "timeout"
                        error = "worker cancellation requested" if cancelled else f"worker exceeded {request.limits.timeout_seconds} seconds"
                        if os.name == "posix":
                            try:
                                os.killpg(process.pid, signal.SIGKILL)
                            except ProcessLookupError:
                                pass
                        else:
                            process.kill()
                        process.wait()
                        returncode = process.returncode
                        break
        except OSError as exc:
            error = str(exc)
            status = "error"
        for source, destination, flag_name in (
            (raw_stdout, stdout_path, "stdout"),
            (raw_stderr, stderr_path, "stderr"),
        ):
            data = source.read_bytes() if source.exists() else b""
            truncated = len(data) > request.limits.max_output_bytes
            if truncated:
                data = data[: request.limits.max_output_bytes] + b"\n[output truncated]\n"
            destination.write_bytes(data)
            if flag_name == "stdout":
                stdout_truncated = truncated
            else:
                stderr_truncated = truncated
    output_hashes: dict[str, str] = {}
    if status == "passed":
        missing = [path for path in outputs if not path.is_file()]
        if missing:
            status = "failed"
            error = "expected outputs missing: " + ", ".join(str(path) for path in missing)
        else:
            output_hashes = {str(path.relative_to(work)): sha256_file(path) for path in outputs}
    result = WorkerResult(
        status=status,
        returncode=returncode,
        started_at=started,
        duration_seconds=round(time.monotonic() - start, 6),
        command=tuple(command),
        isolation=request.isolation,
        isolation_strength=isolation_strength,
        stdout_path=stdout_path,
        stderr_path=stderr_path,
        stdout_truncated=stdout_truncated,
        stderr_truncated=stderr_truncated,
        input_hashes=input_hashes,
        output_hashes=output_hashes,
        error=error,
    )
    if report_path is not None:
        write_json(report_path, result.to_dict())
    return result
