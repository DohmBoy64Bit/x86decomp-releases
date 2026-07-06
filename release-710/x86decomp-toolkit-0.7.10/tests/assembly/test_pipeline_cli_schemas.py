"""Verify the current toolkit behavior covered by `tests/assembly/test_pipeline_cli_schemas.py`."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from jsonschema import Draft202012Validator
import pytest

from x86decomp.contracts import ContractError
from x86decomp.errors import ExternalToolError

from x86decomp.cli import _build_parser, main as toolkit_main
from x86decomp.hybrid import _assembly_bytes, generate_hybrid_project
from x86decomp.assembly.cli import build_parser, main
from x86decomp.assembly.pipeline import AssemblyPipeline
from x86decomp.assembly.relocations import normalize_symbol_map, supported_relocations
from x86decomp.assembly.store import AssemblyStore

ROOT = Path(__file__).resolve().parents[2]


def _capstone_available() -> bool:
    """Return whether the optional Capstone decoder is importable."""
    return importlib.util.find_spec("capstone") is not None


def _leaf_commands(parser):
    """Support leaf commands processing for internal toolkit callers."""
    output = []
    def walk(current, prefix=()):
        """Execute the walk operation for the current toolkit workflow."""
        children = []
        for action in current._actions:
            if action.__class__.__name__ == "_SubParsersAction":
                children.extend(action.choices.items())
        if not children:
            if prefix:
                output.append(" ".join(prefix))
            return
        for name, child in children:
            walk(child, prefix + (name,))
    walk(parser)
    return output


def _manifest(tmp_path: Path) -> Path:
    """Support manifest processing for internal toolkit callers."""
    raw = tmp_path / "function.bin"
    raw.write_bytes(bytes.fromhex("e8fb0f0000c3"))
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps({
        "architecture": "x86",
        "image_base": 0,
        "functions": [
            {"function_id": "entry", "symbol": "sub_00001000", "rva": 0x1000, "bytes_path": "function.bin"},
            {"function_id": "target", "symbol": "sub_00002000", "rva": 0x2000, "code_hex": "c3"}
        ]
    }), encoding="utf-8")
    return path


def test_pipeline_all_three_formats_and_durable_reports(tmp_path: Path) -> None:
    """Verify pipeline all three formats and durable reports behavior."""
    manifest = _manifest(tmp_path)
    store = AssemblyStore(tmp_path / "project")
    api = AssemblyPipeline(store)
    formats = [("bytes", "byte-form"), ("mnemonic", "fully-mnemonic")]
    if _capstone_available():
        formats.insert(1, ("annotated", "annotated-byte-form"))
    else:
        with pytest.raises(ExternalToolError, match="Capstone is required"):
            api.batch(manifest, tmp_path / "annotated", asm_format="annotated")
    for asm_format, expected in formats:
        result = api.batch(manifest, tmp_path / asm_format, asm_format=asm_format)
        assert result["summary"]["total"] == 2
        if asm_format == "mnemonic" and not _capstone_available():
            assert "byte-form-fallback" in result["summary"]["counts"]
        else:
            assert expected in result["summary"]["counts"]
        assert api.report(result["run_id"])["status"] == "completed"
    assert len(api.list_runs()) >= 2
    assert ".byte" in (tmp_path / "bytes/src/asm/sub_00001000.S").read_text()
    if _capstone_available():
        assert "# x86decomp:" in (tmp_path / "annotated/src/asm/sub_00001000.S").read_text()
        assert "call sub_00002000" in (tmp_path / "mnemonic/src/asm/sub_00001000.S").read_text()
    else:
        assert ".byte" in (tmp_path / "mnemonic/src/asm/sub_00001000.S").read_text()


def test_assembly_project_cli_and_all_leaf_help(tmp_path: Path, capsys) -> None:
    """Verify assembly project cli and all leaf help behavior."""
    assert main(["--project", str(tmp_path), "project", "init"]) == 0
    check = json.loads(capsys.readouterr().out)
    assert check["release_version"] == "0.7.10"
    assert check["default_asm_format"] == "bytes"
    commands = _leaf_commands(build_parser())
    assert len(commands) == 12
    for command in commands:
        try:
            build_parser().parse_args(command.split() + ["--help"])
        except SystemExit as exc:
            assert exc.code == 0
        capsys.readouterr()


def test_main_cli_exposes_assembly_capabilities(capsys) -> None:
    """Verify main cli exposes assembly capabilities behavior."""
    choices = set(next(a for a in _build_parser()._actions if a.__class__.__name__ == "_SubParsersAction").choices)
    assert {'commands', 'asm', 'reloc', 'hybrid'} <= choices
    assert toolkit_main(["commands", "--owner", "assembly"]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["release"] == "0.7.10"
    assert payload["selected_route_count"] > 0
    assert {route["owner"] for route in payload["routes"]} == {"assembly"}


def test_assembly_schemas_and_symbol_map_contracts() -> None:
    """Verify assembly schemas and symbol map contracts behavior."""
    schemas = sorted((ROOT / "schemas/assembly").glob("*.schema.json"))
    assert len(schemas) == 5
    for path in schemas:
        Draft202012Validator.check_schema(json.loads(path.read_text()))
    normalized = normalize_symbol_map({"sub_1": "0x1000", "DAT_2": {"rva": 0x2000, "kind": "data"}})
    assert normalized["sub_1"].rva == 0x1000 and normalized["_sub_1"].rva == 0x1000
    assert "REL32" in supported_relocations()["x86"]
    assert "ADDR64" in supported_relocations()["x86_64"]


def test_store_keeps_all_prior_schema_layers(tmp_path: Path) -> None:
    """Verify store keeps all prior schema layers behavior."""
    check = AssemblyStore(tmp_path).check()
    assert check["passed"]
    assert check["schema_extension_version"] == 4
    assert check["reconstruction_schema_extension_version"] == 5
    assert check["native_schema_extension_version"] == 6
    assert check["assembly_schema_extension_version"] == 7


def test_pipeline_persists_relocation_evidence(tmp_path: Path) -> None:
    """Verify pipeline persists relocation evidence behavior."""
    manifest = _manifest(tmp_path)
    store = AssemblyStore(tmp_path / "project")
    result = AssemblyPipeline(store).batch(manifest, tmp_path / "out", asm_format="mnemonic")
    with store.connect() as connection:
        rows = connection.execute(
            "SELECT status,target_symbol,target_rva FROM assembly_relocation_resolutions ORDER BY relocation_offset"
        ).fetchall()
    if not _capstone_available():
        assert not rows
        assert result["summary"]["counts"].get("byte-form-fallback") == 2
        return
    assert rows and rows[0][0] == "resolved"
    assert rows[0][1] == "sub_00002000" and rows[0][2] == 0x2000
    assert result["summary"]["resolved_relocations"] >= 1


def test_hybrid_generate_keeps_bytes_default_and_allows_explicit_modes(tmp_path: Path) -> None:
    """Verify hybrid generate keeps bytes default and allows explicit modes behavior."""
    project = tmp_path / "project"
    artifact = project / "functions" / "f"
    artifact.mkdir(parents=True)
    code = bytes.fromhex("c3")
    (artifact / "body.bin").write_bytes(code)
    (artifact / "function.json").write_text(json.dumps({
        "id": "pe-rva:00001000",
        "entry_rva": 0x1000,
        "body_ranges": [{"file": "body.bin"}],
    }), encoding="utf-8")
    default = generate_hybrid_project(project, tmp_path / "bytes")
    assert default["asm_format"] == "bytes" and default["default_asm_format"] == "bytes"
    assert (tmp_path / "bytes/src/asm/sub_00001000.S").read_text() == _assembly_bytes(
        "sub_00001000", code, "x86"
    )
    if _capstone_available():
        annotated = generate_hybrid_project(project, tmp_path / "annotated", asm_format="annotated")
        assert annotated["asm_format"] == "annotated"
        assert "# x86decomp:" in (tmp_path / "annotated/src/asm/sub_00001000.S").read_text()
    else:
        with pytest.raises(ExternalToolError, match="Capstone is required"):
            generate_hybrid_project(project, tmp_path / "annotated", asm_format="annotated")
    mnemonic = generate_hybrid_project(project, tmp_path / "mnemonic", asm_format="mnemonic")
    assert mnemonic["asm_format"] == "mnemonic"
    text = (tmp_path / "mnemonic/src/asm/sub_00001000.S").read_text()
    assert ("ret" in text) if _capstone_available() else (".byte" in text)


def test_failed_batch_is_recorded_durably(tmp_path: Path) -> None:
    """Verify failed batch is recorded durably behavior."""
    project = tmp_path / "project"
    manifest = tmp_path / "bad-manifest.json"
    manifest.write_text(
        json.dumps({
            "architecture": "x86",
            "functions": [{"function_id": "bad", "symbol": "bad", "rva": "0x1000", "code_hex": "not-hex"}],
        }),
        encoding="utf-8",
    )
    pipeline = AssemblyPipeline(AssemblyStore(project))
    with pytest.raises(ContractError, match="invalid code_hex"):
        pipeline.batch(manifest, tmp_path / "out", asm_format="bytes")
    runs = pipeline.list_runs()
    assert len(runs) == 1
    assert runs[0]["status"] == "failed"
    assert runs[0]["summary"]["error_type"] == "ContractError"
    assert runs[0]["summary"]["total_completed"] == 0
