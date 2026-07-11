"""Provide process support for the standalone verification harness."""
from __future__ import annotations

import os
import subprocess
import time
from pathlib import Path
from typing import Mapping

from .logging_utils import JsonlEventLogger
from .models import Status, TestResult
from .timeutil import utc_now


def run_process_test(
    *,
    test_id: str,
    suite: str,
    command: list[str],
    cwd: Path,
    output_directory: Path,
    timeout: int,
    environment: Mapping[str, str] | None = None,
    required_adapters: list[str] | None = None,
    event_logger: JsonlEventLogger | None = None,
    accepted_return_codes: tuple[int, ...] = (0,),
) -> TestResult:
    """Run process test."""
    started_at = utc_now()
    started = time.monotonic()
    test_directory = output_directory / "tests" / test_id.replace("/", "_").replace(":", "_")
    test_directory.mkdir(parents=True, exist_ok=True)
    stdout_path = test_directory / "stdout.log"
    stderr_path = test_directory / "stderr.log"
    effective_environment = dict(os.environ)
    if environment:
        effective_environment.update(environment)
    if event_logger:
        event_logger.emit("test.started", test_id=test_id, suite=suite, command=command, cwd=str(cwd))
    try:
        with stdout_path.open("w", encoding="utf-8") as stdout, stderr_path.open("w", encoding="utf-8") as stderr:
            completed = subprocess.run(
                command,
                cwd=cwd,
                env=effective_environment,
                stdout=stdout,
                stderr=stderr,
                text=True,
                timeout=timeout,
                check=False,
            )
        status = Status.PASS if completed.returncode in accepted_return_codes else Status.FAIL
        summary = (
            f"command returned accepted exit code {completed.returncode}"
            if status == Status.PASS
            else f"command returned exit code {completed.returncode}"
        )
        return_code = completed.returncode
        details = {}
    except subprocess.TimeoutExpired as exc:
        status = Status.FAIL
        summary = f"command timed out after {timeout} seconds"
        return_code = None
        details = {"timeout": timeout, "error": str(exc)}
    except Exception as exc:
        status = Status.ERROR
        summary = f"process launch failed: {exc}"
        return_code = None
        details = {"error": repr(exc)}
    finished = time.monotonic()
    result = TestResult(
        test_id=test_id,
        suite=suite,
        status=status,
        started_at=started_at,
        finished_at=utc_now(),
        duration_seconds=finished - started,
        summary=summary,
        command=command,
        return_code=return_code,
        stdout_path=str(stdout_path),
        stderr_path=str(stderr_path),
        details=details,
        required_adapters=required_adapters or [],
    )
    if event_logger:
        event_logger.emit("test.finished", result=result.to_dict())
    return result


def blocked_result(test_id: str, suite: str, missing_adapters: list[str], summary: str | None = None) -> TestResult:
    """Build a blocked test result that names all unavailable required adapters."""
    now = utc_now()
    return TestResult(
        test_id=test_id,
        suite=suite,
        status=Status.BLOCKED,
        started_at=now,
        finished_at=now,
        duration_seconds=0.0,
        summary=summary or f"required adapters unresolved: {', '.join(missing_adapters)}",
        details={"missing_adapters": missing_adapters},
        required_adapters=missing_adapters,
    )
