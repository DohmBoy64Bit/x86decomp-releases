from __future__ import annotations

import json
from pathlib import Path

from x86decomp_testkit.config import TestConfig as HarnessConfig, load_config, save_config
from x86decomp_testkit.models import ProbeResult, RunSummary, Status, TestResult as HarnessResult, normalized_path


def test_config_roundtrip_and_relative_resolution(tmp_path: Path) -> None:
    path = tmp_path / "config.json"
    config = HarnessConfig(
        toolkit_root=tmp_path / "toolkit",
        output_root=tmp_path / "results",
        adapter_paths={"ghidra": "/opt/ghidra"},
        install_root=tmp_path / "tools",
        strict=False,
        interactive=False,
        allow_network=True,
        allow_install=True,
        allow_host_execution=True,
        timeout_seconds=123,
        line_coverage_floor=80,
        branch_coverage_floor=60,
        custom_environment={"A": "B"},
    )
    save_config(config, path)
    loaded = load_config(path)
    assert loaded.to_dict() == config.to_dict()
    raw = json.loads(path.read_text())
    raw["toolkit_root"] = "relative-toolkit"
    path.write_text(json.dumps(raw))
    assert load_config(path).toolkit_root == (tmp_path / "relative-toolkit").resolve()


def test_status_counts_and_strict_exit_code(tmp_path: Path) -> None:
    def result(status: Status) -> HarnessResult:
        return HarnessResult("id", "suite", status, "a", "b", 0, "summary")

    base = dict(
        run_id="run",
        toolkit_root=str(tmp_path),
        output_directory=str(tmp_path),
        started_at="a",
        finished_at="b",
        adapter_results=[ProbeResult("x", False)],
        capability_results=[],
        inventory={},
        configuration={},
    )
    assert RunSummary(strict=False, test_results=[result(Status.BLOCKED)], **base).exit_code() == 0
    assert RunSummary(strict=True, test_results=[result(Status.BLOCKED)], **base).exit_code() == 2
    assert RunSummary(strict=False, test_results=[result(Status.FAIL)], **base).exit_code() == 1
    assert RunSummary(strict=False, test_results=[result(Status.ERROR)], **base).exit_code() == 1
    assert normalized_path(tmp_path) == str(tmp_path.resolve())
