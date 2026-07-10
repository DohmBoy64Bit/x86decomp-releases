---
title: tests/test_second_audit_fixes.py
description: Test source page for tests/test_second_audit_fixes.py.
---

# `tests/test_second_audit_fixes.py`

- SHA-256: `637f0a226e118e451f9cf2e2656a44b1ff96529cd1aae1c449d4f03541cf2a56`
- Size: `10126` bytes
- Test functions: `7`

```python
"""Regression tests for the second-audit fix release transaction."""
from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import threading
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Iterator

import pytest

from x86decomp.local_llm import create_profile
from x86decomp.util import write_json

ROOT = Path(__file__).resolve().parents[1]


class _ScriptedHandler(BaseHTTPRequestHandler):
    """Serve scripted JSON responses for command-level local-model tests."""

    script: list[tuple[int, dict[str, str], dict[str, Any]]] = []
    requests: list[dict[str, Any]] = []

    def log_message(self, format: str, *args: object) -> None:
        """Suppress noisy HTTP server logs during tests."""

    def _respond(self) -> None:
        """Handle one scripted GET or POST request."""
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length) if length else b""
        parsed: Any = json.loads(body.decode("utf-8")) if body else None
        type(self).requests.append({"method": self.command, "path": self.path, "body": parsed})
        status, headers, payload = type(self).script.pop(0)
        encoded = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        for key, value in headers.items():
            self.send_header(key, value)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    do_GET = _respond
    do_POST = _respond


@contextmanager
def _server(script: list[tuple[int, dict[str, str], dict[str, Any]]]) -> Iterator[str]:
    """Run a loopback scripted HTTP server for one test."""
    handler = type("ScriptedHandler", (_ScriptedHandler,), {"script": list(script), "requests": []})
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        thread.join(timeout=5)
        server.server_close()


def _run_cli(*args: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    """Run the root x86decomp CLI from the source tree."""
    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT / "src")
    return subprocess.run(
        [sys.executable, "-m", "x86decomp.cli", *args],
        cwd=cwd,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def _write_job(path: Path) -> None:
    """Write a minimal local-LLM job used by prompt and generation commands."""
    write_json(
        path,
        {
            "schema_version": 1,
            "id": "add-two-ints",
            "function_name": "target_add",
            "symbol": "target_add",
            "architecture": "x86",
            "mnemonics": "mov eax, [esp+4]\nadd eax, [esp+8]\nret",
            "target_bytes_hex": "8b44240403442408c3",
            "base_rva": 4096,
            "image_base": 4194304,
            "abi": {
                "calling_convention": "cdecl",
                "return_type": "signed 32-bit integer",
                "parameters": ["signed 32-bit integer a", "signed 32-bit integer b"],
            },
            "evidence": {"analyst_notes": "bounded fixture"},
            "max_attempts": 2,
        },
    )


def test_root_plugin_validate_returns_json_without_name_error(tmp_path: Path) -> None:
    """Verify the canonical plugin validate route no longer crashes on missing json import."""
    executable = tmp_path / "plugin.py"
    executable.write_text("#!/usr/bin/env python3\nprint('ok')\n", encoding="utf-8")
    manifest = tmp_path / "plugin.json"
    write_json(
        manifest,
        {
            "name": "demo",
            "version": "1.0",
            "api_version": "1",
            "executable": str(executable),
            "capabilities": ["analyze"],
        },
    )
    result = _run_cli("plugin", "--project", str(tmp_path / "project"), "validate", str(manifest), cwd=ROOT)
    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["passed"] is True
    assert "NameError" not in result.stderr


def test_root_llm_prompt_writes_prompt_file(tmp_path: Path) -> None:
    """Verify the canonical llm prompt route writes deterministic prompt JSON."""
    job = tmp_path / "job.json"
    output = tmp_path / "prompt.json"
    _write_job(job)
    result = _run_cli("llm", "--project", str(tmp_path), "prompt", str(job), str(output), cwd=ROOT)
    assert result.returncode == 0, result.stderr
    assert output.is_file()
    prompt = json.loads(output.read_text(encoding="utf-8"))
    assert prompt["schema_version"] == 1
    assert prompt["job_id"] == "add-two-ints"
    assert "prompt_sha256" in prompt


def test_root_llm_generate_report_writes_report_file(tmp_path: Path) -> None:
    """Verify llm generate --report uses the shared JSON writer instead of a missing symbol."""
    job = tmp_path / "job.json"
    profile = tmp_path / "profile.json"
    output = tmp_path / "candidate.c"
    report = tmp_path / "generation.json"
    _write_job(job)
    payload = {
        "status": "proposed",
        "c_source": "int target_add(int a, int b) { return a + b; }\n",
        "assumptions": ["bounded command fixture"],
        "rationale": "The function adds two integer parameters.",
    }
    with _server([(200, {}, {"choices": [{"message": {"content": json.dumps(payload)}}]})]) as base_url:
        create_profile(
            "openai-compatible",
            profile,
            model="test-model",
            base_url=f"{base_url}/v1",
        )
        result = _run_cli(
            "llm", "--project", str(tmp_path), "generate", str(profile), str(job), str(output), "--report", str(report), cwd=ROOT
        )
    assert result.returncode == 0, result.stderr
    assert output.read_text(encoding="utf-8") == payload["c_source"]
    written = json.loads(report.read_text(encoding="utf-8"))
    assert written["kind"] == "local_llm_generation"
    assert written["claim"] == "proposal_only"



def test_root_llm_cpp_generate_report_writes_report_file(tmp_path: Path) -> None:
    """Verify llm cpp-generate --report writes the bounded proposal report."""
    job = tmp_path / "job.json"
    profile = tmp_path / "profile.json"
    output = tmp_path / "candidate.cpp"
    report = tmp_path / "cpp-generation.json"
    _write_job(job)
    payload = {
        "status": "proposed",
        "c_source": "int target_add(int a, int b) { return a + b; }\n",
        "assumptions": ["bounded command fixture"],
        "rationale": "The function adds two integer parameters.",
    }
    with _server([(200, {}, {"choices": [{"message": {"content": json.dumps(payload)}}]})]) as base_url:
        create_profile(
            "openai-compatible",
            profile,
            model="test-model",
            base_url=f"{base_url}/v1",
        )
        result = _run_cli(
            "llm",
            "--project",
            str(tmp_path),
            "cpp-generate",
            str(profile),
            str(job),
            str(output),
            "--report",
            str(report),
            cwd=ROOT,
        )
    assert result.returncode == 0, result.stderr
    written = json.loads(report.read_text(encoding="utf-8"))
    assert written["language"] == "cpp"
    assert written["claim"] == "proposal_only_cpp_uncompiled"

def test_reconstruction_cli_error_handler_emits_json(tmp_path: Path) -> None:
    """Verify reconstruction CLI handled errors are emitted as JSON, not NameError."""
    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT / "src")
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "x86decomp.reconstruction.cli",
            "llm",
            "prompt",
            str(tmp_path / "missing-job.json"),
            str(tmp_path / "prompt.json"),
        ],
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    assert result.returncode == 2
    payload = json.loads(result.stderr)
    assert payload["error"] in {"ContractError", "FileNotFoundError", "OSError"}
    assert "NameError" not in result.stderr


def test_validate_contracts_missing_javalang_message(monkeypatch: pytest.MonkeyPatch) -> None:
    """Verify validate-contracts reports a clear missing-javalang diagnostic."""
    module_path = ROOT / "scripts" / "validate-contracts.py"
    spec = importlib.util.spec_from_file_location("validate_contracts_under_test", module_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    real_import = __import__

    def blocked_import(name: str, *args: Any, **kwargs: Any) -> Any:
        """Raise ModuleNotFoundError only for the simulated javalang import."""
        if name == "javalang":
            raise ModuleNotFoundError("No module named 'javalang'")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr("builtins.__import__", blocked_import)
    with pytest.raises(RuntimeError, match="missing validation dependency: install the dev extra"):
        module.validate_java_syntax()


def test_plan_only_command_help_is_explicit(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify action-named plan-only commands advertise that they do not mutate state."""
    from x86decomp.reconstruction.cli import build_parser

    for argv, phrase in (
        (["candidate", "search", "--help"], "plan only"),
        (["type", "propagate", "--help"], "no source edits"),
        (["triage", "next", "--help"], "plan only"),
    ):
        with pytest.raises(SystemExit):
            build_parser().parse_args(argv)
        captured = capsys.readouterr()
        assert phrase in captured.out
```
