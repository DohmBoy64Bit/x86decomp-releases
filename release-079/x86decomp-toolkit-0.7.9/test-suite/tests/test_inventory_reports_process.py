"""Provide test-suite.tests.test_inventory_reports_process functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import json
from pathlib import Path

from x86decomp_testkit.coverage_audit import audit_public_symbol_execution
from x86decomp_testkit.inventory import audit_catalog, build_inventory
from x86decomp_testkit.junit import parse_junit
from x86decomp_testkit.logging_utils import JsonlEventLogger, configure_logging
from x86decomp_testkit.models import ProbeResult, RunSummary, Status, TestResult as HarnessResult
from x86decomp_testkit.process import blocked_result, run_process_test
from x86decomp_testkit.reports import write_adapter_report, write_html_report, write_json_report, write_markdown_report


def _mini_toolkit(root: Path) -> Path:
    """Implement mini toolkit.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    package = root / "src" / "x86decomp"
    package.mkdir(parents=True)
    (package / "__init__.py").write_text("")
    (package / "demo.py").write_text("def public():\n    return 1\n")
    (package / "__main__.py").write_text(
        "import argparse\np=argparse.ArgumentParser()\ns=p.add_subparsers(dest='cmd')\ns.add_parser('one')\ns.add_parser('two')\np.parse_args()\n"
    )
    (root / "schemas").mkdir()
    (root / "schemas" / "a.schema.json").write_text('{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object"}')
    (root / "ghidra_scripts").mkdir()
    (root / "ghidra_scripts" / "A.java").write_text("class A {}")
    return root


def test_inventory_catalog_and_public_coverage(tmp_path: Path) -> None:
    """Verify inventory catalog and public coverage.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    root = _mini_toolkit(tmp_path / "toolkit")
    inventory = build_inventory(root)
    assert inventory["cli_commands"] == ["one", "two"]
    catalog = {
        "cli_commands": {"one": {}, "two": {}},
        "modules": {name: {} for name in inventory["modules"]},
        "schemas": inventory["schemas"],
        "ghidra_scripts": inventory["ghidra_scripts"],
        "all_function_symbols": [item["id"] for item in inventory["all_function_symbols"]],
    }
    assert audit_catalog(inventory, catalog)["passed"]
    coverage = tmp_path / "coverage.json"
    coverage.write_text(json.dumps({
        "files": {str(root / "src/x86decomp/demo.py"): {"executed_lines": [1, 2]}},
        "totals": {"percent_statements_covered": 100, "num_branches": 0, "covered_branches": 0},
    }))
    audit = audit_public_symbol_execution(root, coverage)
    assert audit["passed"]


def test_junit_process_logging_and_reports(tmp_path: Path) -> None:
    """Verify junit process logging and reports.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    junit = tmp_path / "junit.xml"
    junit.write_text('<testsuite tests="2" failures="1" errors="0" skipped="1"><testcase classname="a" name="ok"/><testcase classname="a" name="bad"><failure/></testcase><testcase classname="a" name="skip"><skipped/></testcase></testsuite>')
    parsed = parse_junit(junit)
    assert parsed["failures"] == 1 and parsed["skipped"] == 1

    logger, events = configure_logging(tmp_path / "logs", verbose=True)
    logger.info("hello")
    events.emit("custom", value=1)
    result = run_process_test(
        test_id="process:ok", suite="self", command=["python", "-c", "print('ok')"],
        cwd=tmp_path, output_directory=tmp_path / "run", timeout=10, event_logger=events,
    )
    assert result.status == Status.PASS
    assert blocked_result("b", "self", ["tool"]).status == Status.BLOCKED

    summary = RunSummary(
        run_id="run", toolkit_root=str(tmp_path), output_directory=str(tmp_path / "run"), strict=False,
        started_at="a", finished_at="b", adapter_results=[ProbeResult("tool", False)],
        capability_results=[],
        test_results=[result, blocked_result("b", "self", ["tool"])], inventory={}, configuration={},
    )
    write_json_report(summary, tmp_path / "report.json")
    write_markdown_report(summary, tmp_path / "report.md")
    write_html_report(summary, tmp_path / "report.html")
    write_adapter_report(summary.adapter_results, tmp_path / "adapters.json")
    for name in ("report.json", "report.md", "report.html", "adapters.json"):
        assert (tmp_path / name).is_file()

def test_suite_schemas_and_catalog_are_valid() -> None:
    """Verify suite schemas and catalog are valid.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    from importlib.resources import files
    from jsonschema.validators import validator_for
    import x86decomp_testkit

    suite_root = Path(x86decomp_testkit.__file__).resolve().parents[2]
    schema_dir = suite_root / "schemas"
    if schema_dir.is_dir():
        for path in schema_dir.glob("*.schema.json"):
            schema = json.loads(path.read_text())
            validator_for(schema).check_schema(schema)
    catalog_path = Path(str(files("x86decomp_testkit").joinpath("data/feature_catalog.json")))
    catalog = json.loads(catalog_path.read_text())
    assert catalog["toolkit_version"] == "0.7.9"
    assert catalog["entry_points"] == {"toolkit": "x86decomp", "test_suite": "x86decomp-test"}
    assert "compatibility_baseline" not in catalog


def test_recursive_inventory_includes_capability_packages_and_nested_schemas(tmp_path: Path) -> None:
    """Verify recursive inventory includes capability packages and nested schemas.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    root = _mini_toolkit(tmp_path / "toolkit")
    package = root / "src/x86decomp/capability"
    package.mkdir()
    (package / "__init__.py").write_text("", encoding="utf-8")
    (package / "api.py").write_text("class API:\n    def run(self):\n        return 1\n", encoding="utf-8")
    nested = root / "schemas/capability"
    nested.mkdir()
    (nested / "item.schema.json").write_text('{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object"}', encoding="utf-8")
    inventory = build_inventory(root)
    assert "x86decomp.capability" in inventory["modules"]
    assert "x86decomp.capability.api" in inventory["modules"]
    assert "x86decomp.capability.api:API.run" in {item["id"] for item in inventory["all_function_symbols"]}
    assert "capability/item.schema.json" in inventory["schemas"]
