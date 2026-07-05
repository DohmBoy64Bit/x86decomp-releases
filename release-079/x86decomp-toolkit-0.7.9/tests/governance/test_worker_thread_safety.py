"""Provide tests.governance.test_worker_thread_safety functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest

from x86decomp.worker import WorkerLimits, WorkerRequest, execute_worker_request


def test_worker_uses_exec_wrapper_without_thread_unsafe_preexec(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Verify worker uses exec wrapper without thread unsafe preexec.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    observed: dict[str, object] = {}
    real_popen = subprocess.Popen

    def recording_popen(*args, **kwargs):
        """Implement recording popen.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        observed["preexec_fn"] = kwargs.get("preexec_fn")
        observed["start_new_session"] = kwargs.get("start_new_session")
        return real_popen(*args, **kwargs)

    monkeypatch.setattr("x86decomp.worker.subprocess.Popen", recording_popen)
    request = WorkerRequest(
        command=(sys.executable, "-c", "print('ok')"),
        working_directory=tmp_path / "work",
        limits=WorkerLimits(timeout_seconds=10, cpu_seconds=10),
    )
    result = execute_worker_request(request, log_directory=tmp_path / "logs")
    assert result.status == "passed"
    assert result.command == request.command
    assert observed["preexec_fn"] is None
    assert observed["start_new_session"] is (os.name == "posix")


def test_legacy_preexec_compatibility_callback_is_executable(monkeypatch) -> None:
    """Retain and directly exercise the 0.4 private callback without forking."""
    import os
    import sys
    from types import SimpleNamespace

    from x86decomp.worker import WorkerLimits, _preexec

    limits = WorkerLimits(
        cpu_seconds=7,
        memory_bytes=32 * 1024 * 1024,
        max_processes=3,
        max_output_bytes=4096,
    )
    callback = _preexec(limits)
    if os.name != "posix":
        assert callback is None
        return

    calls: list[tuple[object, tuple[int, int]]] = []
    fake_resource = SimpleNamespace(
        RLIMIT_CPU="cpu",
        RLIMIT_AS="as",
        RLIMIT_NPROC="nproc",
        RLIMIT_FSIZE="fsize",
        setrlimit=lambda key, value: calls.append((key, value)),
    )
    sessions: list[bool] = []
    monkeypatch.setitem(sys.modules, "resource", fake_resource)
    monkeypatch.setattr(os, "setsid", lambda: sessions.append(True))

    assert callback is not None
    callback()
    assert calls == [
        ("cpu", (7, 8)),
        ("as", (32 * 1024 * 1024, 32 * 1024 * 1024)),
        ("nproc", (3, 3)),
        ("fsize", (16384, 16384)),
    ]
    assert sessions == [True]
