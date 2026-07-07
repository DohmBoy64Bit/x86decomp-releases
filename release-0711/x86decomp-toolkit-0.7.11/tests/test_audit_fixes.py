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
