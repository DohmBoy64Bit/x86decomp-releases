"""Regression tests for the review-only audit remediation set."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tarfile
import tomllib
from pathlib import Path
from typing import Any, cast

import pytest

from x86decomp import __version__
from x86decomp.cli import _build_parser
from x86decomp.project_state import _extract_validated_backup

ROOT = Path(__file__).resolve().parents[1]


def _load_script(name: str) -> Any:
    """Load a repository script as a module for direct contract testing."""
    path = ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_cli_version_action_reports_release(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify the root CLI exposes the installed toolkit version and exits cleanly."""
    parser = _build_parser()
    with pytest.raises(SystemExit) as raised:
        parser.parse_args(["--version"])
    assert raised.value.code == 0
    assert capsys.readouterr().out == f"x86decomp {__version__}\n"


def test_backup_extraction_supports_pre_filter_python(tmp_path: Path) -> None:
    """Verify validated backups can use the Python 3.11.0 extraction signature."""

    class LegacyArchive:
        """Record extraction through the pre-3.11.4 TarFile signature."""

        def __init__(self) -> None:
            """Initialize the extraction call record."""
            self.destination: Path | None = None

        def extractall(self, path: Path) -> None:
            """Record the destination accepted by the legacy signature."""
            self.destination = path

    archive = LegacyArchive()
    _extract_validated_backup(cast(tarfile.TarFile, archive), tmp_path)
    assert archive.destination == tmp_path


def test_backup_extraction_uses_data_filter_when_available(tmp_path: Path) -> None:
    """Verify supported Python releases receive the hardened tar data filter."""

    class FilterArchive:
        """Record extraction through the filtered TarFile signature."""

        def __init__(self) -> None:
            """Initialize the extraction call record."""
            self.call: tuple[Path, str | None] | None = None

        def extractall(self, path: Path, *, filter: str | None = None) -> None:
            """Record the destination and filter selected by the helper."""
            self.call = (path, filter)

    archive = FilterArchive()
    _extract_validated_backup(cast(tarfile.TarFile, archive), tmp_path)
    assert archive.call == (tmp_path, "data")


def test_distributions_include_complete_apache_license() -> None:
    """Verify both distributions carry the complete Apache License 2.0 text."""
    root_license = (ROOT / "LICENSE").read_text(encoding="utf-8")
    suite_license = (ROOT / "test-suite" / "LICENSE").read_text(encoding="utf-8")
    assert root_license == suite_license
    assert "TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION" in root_license
    assert "9. Accepting Warranty or Additional Liability." in root_license
    assert len(root_license.encode("utf-8")) > 10_000
    assert (ROOT / "NOTICE").is_file()
    assert (ROOT / "test-suite" / "NOTICE").is_file()


def test_docstring_reports_are_deterministic_and_read_only() -> None:
    """Verify docstring report checking succeeds without rewriting sealed files."""
    targets = [ROOT / "DOCSTRING_AUDIT_0.7.11.json", ROOT / "DOCSTRING_AUDIT_0.7.11.md"]
    before = [path.read_bytes() for path in targets]
    completed = subprocess.run(
        [sys.executable, "scripts/audit-docstrings.py", "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
    assert [path.read_bytes() for path in targets] == before
    report = json.loads(targets[0].read_text(encoding="utf-8"))
    assert report["quality_checks"]["generic_docstring_occurrences"] == 0


def test_command_reference_covers_every_parser_node() -> None:
    """Verify every live parser node has arguments, contracts, safety, and an example."""
    reference = json.loads((ROOT / "docs" / "COMMAND_REFERENCE_0.7.11.json").read_text(encoding="utf-8"))
    records = reference["parser_nodes"]
    assert reference["root_command_count"] == 166
    assert reference["canonical_route_count"] == 239
    assert reference["parser_node_count"] == 405 == len(records)
    for record in records:
        assert record["summary"]
        assert isinstance(record["arguments"], list)
        assert record["success_output"]
        assert record["error_behavior"]
        assert record["safety_note"]
        assert record["real_world_use_case"]
        assert record["example"] == record["command"] + " --help"


def test_generated_command_reference_is_current() -> None:
    """Verify the committed command reference matches live parser metadata."""
    completed = subprocess.run(
        [sys.executable, "scripts/generate_command_reference.py", "--check"],
        cwd=ROOT,
        env={**dict(__import__("os").environ), "PYTHONPATH": str(ROOT / "src")},
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr


def test_packaged_self_test_sync_gate_detects_drift(tmp_path: Path) -> None:
    """Verify normalized-AST synchronization passes and detects a changed copy."""
    module = _load_script("verify_self_test_sync.py")
    assert module.verify(ROOT)["valid"]
    for name in module.PAIR_NAMES:
        source = ROOT / "test-suite" / "tests" / name
        canonical = tmp_path / "test-suite" / "tests" / name
        packaged = tmp_path / "test-suite" / "src" / "x86decomp_testkit" / "self_tests" / name
        canonical.parent.mkdir(parents=True, exist_ok=True)
        packaged.parent.mkdir(parents=True, exist_ok=True)
        canonical.write_bytes(source.read_bytes())
        packaged.write_bytes((ROOT / "test-suite" / "src" / "x86decomp_testkit" / "self_tests" / name).read_bytes())
    assert module.verify(tmp_path)["valid"]
    drifted = tmp_path / "test-suite" / "src" / "x86decomp_testkit" / "self_tests" / module.PAIR_NAMES[0]
    drifted.write_text(drifted.read_text(encoding="utf-8") + "\nDRIFT_SENTINEL = True\n", encoding="utf-8")
    result = module.verify(tmp_path)
    assert not result["valid"]
    assert result["failures"] == [f"normalized AST mismatch: {module.PAIR_NAMES[0]}"]


def test_declared_quality_tools_and_ci_gates_are_reproducible() -> None:
    """Verify documented development dependencies install every enforced quality gate."""
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    dev = project["project"]["optional-dependencies"]["dev"]
    assert any(item.startswith("ruff") for item in dev)
    assert any(item.startswith("pyright") for item in dev)
    assert project["tool"]["pyright"]["typeCheckingMode"] == "basic"
    assert project["tool"]["pyright"]["include"] == ["src"]
    makefile = (ROOT / "Makefile").read_text(encoding="utf-8")
    workflow = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    for target in ("lint:", "typecheck:", "self-test-sync:", "command-reference:"):
        assert target in makefile
    assert "python -m ruff check" in workflow
    assert "python -m pyright" in workflow
    assert 'python: ["3.11.0", "3.12", "3.13"]' in workflow


def test_release_text_files_have_no_trailing_whitespace() -> None:
    """Verify release-controlled text outside historical review evidence has clean line endings."""
    failures: list[str] = []
    historical_review = ROOT / "project-audit" / "review-only-2026-07-10"
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or historical_review in path.parents:
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for line_number, line in enumerate(lines, start=1):
            if line.endswith((" ", "\t")):
                failures.append(f"{path.relative_to(ROOT)}:{line_number}")
    assert not failures
