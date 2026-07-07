"""Provide test-suite.tests.test_adapter_detection_resolution functionality for the x86decomp-toolkit 0.7.11 release.

This module-level documentation was added during the complete 0.7.11 code audit.
"""
from __future__ import annotations

import os
from pathlib import Path

import pytest

from x86decomp_testkit.adapters.detection import detect_adapter, detect_all
from x86decomp_testkit.adapters.installation import resolve_missing_adapters
from x86decomp_testkit.config import TestConfig as HarnessConfig
from x86decomp_testkit.models import AdapterKind, AdapterSpec


def _config(tmp_path: Path, **kwargs) -> HarnessConfig:
    """Implement config.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    defaults = dict(toolkit_root=tmp_path, output_root=tmp_path / "out", interactive=True, allow_install=False)
    defaults.update(kwargs)
    return HarnessConfig(**defaults)


def test_installed_adapter_never_prompts(tmp_path: Path) -> None:
    """Verify installed adapter never prompts.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    spec = AdapterSpec("python-self", "Python", AdapterKind.EXECUTABLE, ("test",), commands=(Path(os.sys.executable).name,), optional=False)
    config = _config(tmp_path)
    prompts: list[str] = []

    def prompt(text: str) -> str:
        """Implement prompt.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        prompts.append(text)
        raise AssertionError("installed adapter must not prompt")

    results = resolve_missing_adapters({spec.adapter_id: spec}, config, prompt=prompt)
    assert results[0].installed
    assert prompts == []


def test_missing_adapter_prompts_custom_path_then_accepts(tmp_path: Path) -> None:
    """Verify missing adapter prompts custom path then accepts.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    executable = tmp_path / "my-tool"
    executable.write_text("#!/bin/sh\necho 1.2.3\n", encoding="utf-8")
    executable.chmod(0o755)
    spec = AdapterSpec("custom", "Custom", AdapterKind.EXECUTABLE, ("test",), commands=("definitely-not-on-path-987",), optional=False)
    config = _config(tmp_path)
    answers = iter(["y", str(executable)])
    prompts: list[str] = []

    def prompt(text: str) -> str:
        """Implement prompt.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        prompts.append(text)
        return next(answers)

    results = resolve_missing_adapters({"custom": spec}, config, prompt=prompt)
    assert results[0].installed
    assert results[0].source == "configured-path"
    assert prompts[0].startswith("Is it already installed")
    assert "custom" in config.adapter_paths


def test_missing_noninteractive_is_explicit_unresolved(tmp_path: Path) -> None:
    """Verify missing noninteractive is explicit unresolved.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    spec = AdapterSpec("missing", "Missing", AdapterKind.EXECUTABLE, ("feature",), commands=("impossible-command-xyz",), optional=False)
    config = _config(tmp_path, interactive=False)
    result = resolve_missing_adapters({"missing": spec}, config)[0]
    assert not result.installed
    assert result.diagnostics


def test_environment_and_configured_root_detection(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Verify environment and configured root detection.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    root = tmp_path / "root"
    tool = root / "bin" / "tool"
    tool.parent.mkdir(parents=True)
    tool.write_text("#!/bin/sh\necho v1\n")
    tool.chmod(0o755)
    spec = AdapterSpec(
        "rooted", "Rooted", AdapterKind.DIRECTORY, ("test",), commands=("tool",),
        environment_variables=("ROOTED_HOME",), root_markers=("bin/tool",), optional=False,
    )
    config = _config(tmp_path)
    monkeypatch.setenv("ROOTED_HOME", str(root))
    assert detect_adapter(spec, config).source == "environment:ROOTED_HOME"
    config.adapter_paths["rooted"] = str(root)
    assert detect_adapter(spec, config).source == "configured-path"
    assert len(detect_all({"rooted": spec}, config)) == 1

def test_path_detection_preserves_symlink_argv0(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Verify path detection preserves symlink argv0.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if os.name == "nt":
        try:
            (tmp_path / "_sym_probe").symlink_to(tmp_path)
        except OSError:
            return  # Skip on Windows without Developer Mode
    target = tmp_path / "generic"
    target.write_text("#!/bin/sh\necho generic\n")
    target.chmod(0o755)
    alias = tmp_path / "special-link"
    alias.symlink_to(target)
    monkeypatch.setenv("PATH", str(tmp_path))
    spec = AdapterSpec("special", "Special", AdapterKind.EXECUTABLE, ("test",), commands=("special-link",), optional=False)
    result = detect_adapter(spec, _config(tmp_path))
    assert result.installed
    assert Path(result.path).name == "special-link"

def test_missing_python_adapter_accepts_custom_interpreter(tmp_path: Path) -> None:
    """Verify missing python adapter accepts custom interpreter.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    spec = AdapterSpec("pytest-custom", "pytest", AdapterKind.PYTHON, ("test",), python_modules=("pytest",), optional=False)
    config = _config(tmp_path)
    config.python_executable = str(tmp_path / "missing-python")
    answers = iter(["y", os.sys.executable])
    result = resolve_missing_adapters({spec.adapter_id: spec}, config, prompt=lambda _text: next(answers))[0]
    assert result.installed
    assert config.python_executable == os.sys.executable
