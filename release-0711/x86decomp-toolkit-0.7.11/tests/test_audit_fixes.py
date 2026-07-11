"""Regression tests for fixes made from the prior full code audit."""
from __future__ import annotations

import ast
from pathlib import Path

from x86decomp.reconstruction.acceleration import llm_batch_create
from x86decomp.service import create_app
from x86decomp.store_utils import decode_json_fields
from x86decomp_testkit.adapters import adapter_catalog

ROOT = Path(__file__).resolve().parents[1]


def test_optional_toolkit_extras_are_adapter_optional() -> None:
    """Verify optional toolkit extras are represented as optional adapters."""
    catalog = adapter_catalog()
    for adapter_id in ("capstone", "unicorn", "z3", "angr", "fastapi", "uvicorn", "lief"):
        assert catalog[adapter_id].optional is True
    assert catalog["z3"].pip_requirement == "z3-solver>=4.15,<5"


def test_service_index_uses_text_content_not_inner_html(tmp_path: Path) -> None:
    """Verify the local service UI avoids project-data insertion through innerHTML."""
    (tmp_path / "project.json").write_text('{"schema_version":1}', encoding="utf-8")
    html = create_app(tmp_path).routes[-1].endpoint()
    assert "innerHTML" not in html
    assert "textContent=JSON.stringify" in html
    assert "Content-Security-Policy" in html


def test_store_decode_json_fields_shared_helper() -> None:
    """Verify shared SQLite row JSON decoding behavior."""
    assert decode_json_fields({"details_json": "{\"ok\": true}", "name": "x"}, "details_json") == {
        "details": {"ok": True},
        "name": "x",
    }


def test_batch_create_records_secondary_manifest_id_errors(tmp_path: Path) -> None:
    """Verify corrupt manifests preserve the secondary id-read failure reason."""
    functions = tmp_path / "functions" / "bad"
    functions.mkdir(parents=True)
    (functions / "function.json").write_text("{", encoding="utf-8")
    report = llm_batch_create(tmp_path, tmp_path / "jobs", architecture="x86")
    assert report["blocked_count"] == 1
    assert report["blocked"][0]["function_id"] is None
    assert "function_id_error" in report["blocked"][0]


def test_no_template_docstring_phrases_remain() -> None:
    """Verify audited Python files no longer contain generated placeholder docstring phrasing."""
    forbidden = (
        "Parameters and return values follow the signature and runtime validation in the body.",
        "This module-level documentation was added during the complete",
        "Implement ",
    )
    offenders: list[str] = []
    for base in (ROOT / "src", ROOT / "test-suite" / "src", ROOT / "tests", ROOT / "scripts"):
        for path in base.rglob("*.py"):
            if "__pycache__" in path.parts:
                continue
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path.relative_to(ROOT)))
            for node in ast.walk(tree):
                if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                    doc = ast.get_docstring(node) or ""
                    if any(phrase in doc for phrase in forbidden):
                        name = "<module>" if isinstance(node, ast.Module) else node.name
                        line = 1 if isinstance(node, ast.Module) else node.lineno
                        offenders.append(f"{path.relative_to(ROOT)}:{line}:{name}")
    assert not offenders


def test_contract_error_has_one_public_identity() -> None:
    """Verify both legacy import paths expose the same contract-error class."""
    from x86decomp.contracts import ContractError as ContractsError
    from x86decomp.errors import ContractError as ErrorsError, X86DecompError

    assert ContractsError is ErrorsError
    assert issubclass(ErrorsError, X86DecompError)
    assert issubclass(ErrorsError, ValueError)


def test_root_cli_reports_missing_file_as_json(capsys) -> None:
    """Verify ordinary filesystem failures do not leak an interpreter traceback."""
    from x86decomp.cli import main

    code = main(["inspect-pe", "definitely-missing-input.exe"])
    captured = capsys.readouterr()
    assert code == 2
    payload = __import__("json").loads(captured.err)
    assert payload["error"] == "FileNotFoundError"
    assert "definitely-missing-input.exe" in payload["message"]
    assert "Traceback" not in captured.err


def test_every_root_command_has_help_text() -> None:
    """Verify every registered root command contributes a useful help row."""
    from x86decomp.cli import _build_parser

    parser = _build_parser()
    subparsers = next(action for action in parser._actions if getattr(action, "choices", None))
    help_by_name = {action.dest: action.help for action in subparsers._choices_actions}
    assert set(help_by_name) == set(subparsers.choices)
    assert all(text and text != "==SUPPRESS==" for text in help_by_name.values())


def test_workflow_function_id_rejects_path_traversal(tmp_path: Path) -> None:
    """Verify workflow identifiers cannot select paths outside the functions directory."""
    import pytest

    from x86decomp.errors import ContractError
    from x86decomp.workflow import load_function_workflow

    for function_id in ("../escape", "pe-rva:00000000/../../escape", "pe-rva:0000000g"):
        with pytest.raises(ContractError, match="pe-rva:XXXXXXXX"):
            load_function_workflow(tmp_path, function_id)


def test_service_requires_explicit_remote_bind(monkeypatch, tmp_path: Path) -> None:
    """Verify a non-loopback service bind is rejected before Uvicorn starts."""
    import pytest

    from x86decomp.errors import ContractError
    from x86decomp.service import run_service

    called: list[dict[str, object]] = []

    class UvicornStub:
        """Record attempted Uvicorn starts without opening a socket."""

        @staticmethod
        def run(app, *, host: str, port: int) -> None:
            """Record the application and bind parameters."""
            called.append({"app": app, "host": host, "port": port})

    monkeypatch.setitem(__import__("sys").modules, "uvicorn", UvicornStub)
    with pytest.raises(ContractError, match="--allow-remote"):
        run_service(tmp_path, host="0.0.0.0")
    assert called == []


def test_analysis_query_is_read_only_and_row_bounded(tmp_path: Path) -> None:
    """Verify ad-hoc database queries cannot mutate data or return unbounded rows."""
    import pytest

    from x86decomp.analysis_db import AnalysisDatabase
    from x86decomp.errors import ContractError

    with AnalysisDatabase(tmp_path / "analysis.sqlite3") as database:
        database.upsert_entity(
            entity_id="function-a",
            kind="function",
            name="a",
            address_rva=1,
            provenance="test",
        )
        database.connection.commit()
        assert database.query("SELECT id FROM entities") == [{"id": "function-a"}]
        with pytest.raises(ContractError, match="SELECT statements only"):
            database.query("UPDATE entities SET name='changed'")
        with pytest.raises(ContractError, match="row limit"):
            database.query(
                "SELECT 1 AS value UNION ALL SELECT 2 UNION ALL SELECT 3",
                max_rows=2,
            )


def test_claim_verification_exposes_public_verification_status(tmp_path: Path) -> None:
    """Verify claim results use the declared VerificationStatus contract."""
    from x86decomp.evidence import EvidenceStore
    from x86decomp.models import VerificationStatus

    store = EvidenceStore(tmp_path)
    claim = store.create_claim(subject="f", predicate="is", object_value="known")
    result = store.verify_claim(claim.id)
    assert result["verification_status"] == VerificationStatus.FAILED.value


def test_canonical_parser_builders_are_cached() -> None:
    """Verify canonical parser discovery is built once per process."""
    from x86decomp import canonical

    canonical._source_parsers.cache_clear()
    first = canonical._source_parsers()
    second = canonical._source_parsers()
    assert first is second
    assert canonical._source_parsers.cache_info().hits >= 1


def test_importing_package_main_module_does_not_execute_cli(monkeypatch) -> None:
    """Verify importing the module entry point has no command-line side effect."""
    import importlib
    import sys

    import x86decomp.cli

    called: list[object] = []
    monkeypatch.setattr(x86decomp.cli, "main", lambda argv=None: called.append(argv) or 0)
    sys.modules.pop("x86decomp.__main__", None)
    importlib.import_module("x86decomp.__main__")
    assert called == []
