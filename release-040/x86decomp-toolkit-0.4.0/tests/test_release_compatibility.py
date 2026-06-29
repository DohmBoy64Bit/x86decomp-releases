from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

from x86decomp.cli import _build_parser

ROOT = Path(__file__).resolve().parents[1]


def _commands() -> set[str]:
    parser = _build_parser()
    action = next(action for action in parser._actions if getattr(action, "choices", None))
    return set(action.choices)


def test_v020_command_and_schema_surface_is_preserved() -> None:
    contract = json.loads((ROOT / "examples/compatibility/v0.2-command-surface.json").read_text())
    assert set(contract["commands"]).issubset(_commands())
    assert all((ROOT / "schemas" / name).is_file() for name in contract["schema_files"])


def test_schema_v1_project_and_function_documents_remain_valid() -> None:
    project_schema = json.loads((ROOT / "schemas/project.schema.json").read_text())
    function_schema = json.loads((ROOT / "schemas/function.schema.json").read_text())
    project_v1 = {
        "schema_version": 1,
        "project_id": "x86d-0123456789abcdef-01234567",
        "created_at": "2026-06-28T00:00:00Z",
        "supported_scope": "native Windows PE32 x86",
        "binary": {
            "name": "target.exe",
            "source_kind": "copied",
            "path": "original/target.exe",
            "sha256": "0" * 64,
            "size": 1,
        },
        "program_manifest": "analysis/program.json",
        "memory_ledger": "memory/events.jsonl",
        "function_root": "functions",
        "evidence_root": "evidence",
        "status": "initialized",
    }
    function_v1 = {
        "schema_version": 1,
        "id": "pe-rva:00001234",
        "entry": "00401234",
        "entry_rva": 0x1234,
        "name": "FUN_00401234",
        "name_source": "DEFAULT",
        "calling_convention": None,
        "signature": "undefined FUN_00401234(void)",
        "return_type": "undefined",
        "body_ranges": [{
            "start": "00401234",
            "end_inclusive": "00401234",
            "start_rva": 0x1234,
            "end_rva": 0x1235,
            "size": 1,
            "file": "ranges/0000.bin",
        }],
        "parameters": [],
    }
    Draft202012Validator(project_schema).validate(project_v1)
    Draft202012Validator(function_schema).validate(function_v1)


def test_ground_truth_sources_are_packaged_and_in_sync() -> None:
    repository_sources = ROOT / "corpus/ground_truth_sources"
    package_sources = ROOT / "src/x86decomp/corpus/ground_truth_sources"
    repository = {path.name: path.read_bytes() for path in repository_sources.iterdir() if path.is_file()}
    packaged = {path.name: path.read_bytes() for path in package_sources.iterdir() if path.is_file()}
    assert packaged == repository
    assert len(packaged) == 24


def test_v031_public_release_surface_is_preserved() -> None:
    """Version 0.4 must retain every externally discoverable 0.3.1 surface."""
    contract = json.loads((ROOT / "examples/compatibility/v0.3.1-surface.json").read_text())

    assert set(contract["commands"]).issubset(_commands())
    assert all((ROOT / "schemas" / name).is_file() for name in contract["schema_files"])
    assert all((ROOT / "ghidra_scripts" / name).is_file() for name in contract["ghidra_scripts"])

    package_modules = {
        "x86decomp." + path.stem
        for path in (ROOT / "src/x86decomp").glob("*.py")
        if path.stem not in {"__init__", "__main__"}
    }
    package_modules.update({"x86decomp.__init__", "x86decomp.__main__"})
    assert set(contract["modules"]).issubset(package_modules)

    from x86decomp_testkit.adapters import adapter_catalog

    assert set(contract["adapter_ids"]).issubset(set(adapter_catalog()))
