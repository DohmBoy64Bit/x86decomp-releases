"""Verify the current toolkit behavior covered by `tests/governance/test_governance_cli_schemas.py`."""
from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from x86decomp.governance.cli import build_parser, main

ROOT = Path(__file__).resolve().parents[2]


def test_every_governance_schema_meta_validates() -> None:
    """Verify every governance schema meta validates behavior."""
    files = sorted((ROOT / "schemas/governance").glob("*.json"))
    assert len(files) >= 10
    for path in files:
        Draft202012Validator.check_schema(json.loads(path.read_text()))


def test_governance_cli_help_and_init(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """Verify governance cli help and init behavior."""
    parser = build_parser()
    assert "campaign" in parser.format_help()
    assert main(["--project", str(tmp_path / "p"), "project", "init"]) == 0
    assert json.loads(capsys.readouterr().out)["passed"]


def test_governance_cli_hypothesis_flow(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """Verify governance cli hypothesis flow behavior."""
    project = tmp_path / "p"
    assert main(["--project", str(project), "hypothesis", "create", "x is unsigned", "function", "f", "--origin", "test"]) == 0
    created = json.loads(capsys.readouterr().out)
    assert created["state"] == "proposed"
    assert main(["--project", str(project), "hypothesis", "show", created["hypothesis_id"]]) == 0


def test_contract_helpers_and_cli_json_arg(tmp_path: Path) -> None:
    """Verify contract helpers and cli json arg behavior."""
    from x86decomp.cli_utils import parse_json_arg
    from x86decomp.contracts import atomic_write_bytes, atomic_write_json, dedupe_preserve, read_json, stable_id

    assert parse_json_arg('{"x":1}', {}) == {"x": 1}
    assert stable_id("x", 1) == stable_id("x", 1)
    raw = tmp_path / "raw"
    atomic_write_bytes(raw, b"abc")
    assert raw.read_bytes() == b"abc"
    document = tmp_path / "d.json"
    atomic_write_json(document, {"b": 2})
    assert read_json(document) == {"b": 2}
    assert dedupe_preserve(["a", "b", "a"]) == ["a", "b"]


def test_all_governance_leaf_commands_parse_help() -> None:
    """Verify all governance leaf commands parse help behavior."""
    parser = build_parser()
    leaves = []

    def walk(current, prefix=()):
        """Return the walk derived from `current`, `prefix`."""
        children = []
        for action in current._actions:
            if action.__class__.__name__ == "_SubParsersAction":
                children.extend(action.choices.items())
        if not children:
            leaves.append(prefix)
            return
        for name, child in children:
            walk(child, prefix + (name,))

    walk(parser)
    assert len(leaves) == 67
    for command in leaves:
        with pytest.raises(SystemExit) as caught:
            parser.parse_args([*command, "--help"])
        assert caught.value.code == 0
