"""Provide test-suite.tests.test_cli_and_installation functionality for the x86decomp-toolkit 0.7.11 release.

This module-level documentation was added during the complete 0.7.11 code audit.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from x86decomp_testkit import cli
from x86decomp_testkit.adapters import installation
from x86decomp_testkit.config import TestConfig as HarnessConfig
from x86decomp_testkit.models import AdapterKind, AdapterSpec


def test_cli_init_config_catalog_and_missing_config(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """Verify cli init config catalog and missing config.

    Parameters and return values follow the signature and runtime validation in the body.
    """
    config = tmp_path / "config.json"
    assert cli.main(["init-config", "--toolkit-root", str(tmp_path), "--config", str(config), "--non-interactive", "--non-strict"]) == 0
    assert config.is_file()
    assert cli.main(["catalog"]) == 0
    assert cli.main(["inventory", "--config", str(tmp_path / "missing.json")]) == 1
    assert "configuration does not exist" in capsys.readouterr().err


def test_install_python_command_and_failure(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Verify install python command and failure.

    Parameters and return values follow the signature and runtime validation in the body.
    """
    spec = AdapterSpec("p", "P", AdapterKind.PYTHON, ("test",), python_modules=("p",), pip_requirement="p==1", optional=False)
    config = HarnessConfig(tmp_path, tmp_path / "out", python_executable="python")
    commands: list[list[str]] = []

    def run_ok(command, check=False):
        """Run ok.

        Parameters and return values follow the signature and runtime validation in the body.
        """
        commands.append(command)
        return subprocess.CompletedProcess(command, 0)

    monkeypatch.setattr(installation.subprocess, "run", run_ok)
    installation.install_python_adapter(spec, config)
    assert commands == [["python", "-m", "pip", "install", "p==1"]]

    def run_bad(command, check=False):
        """Run bad.

        Parameters and return values follow the signature and runtime validation in the body.
        """
        return subprocess.CompletedProcess(command, 7)

    monkeypatch.setattr(installation.subprocess, "run", run_bad)
    with pytest.raises(RuntimeError, match="exit code 7"):
        installation.install_python_adapter(spec, config)
