---
title: test-suite/tests/test_inventory_reports_process.py
description: Source-derived reference for 4 collected test nodes.
---

# `test-suite/tests/test_inventory_reports_process.py`

**Collected nodes:** 4  
**Source SHA-256:** `595ddc6f032d215d6def4318ffd107b71d9736147b8383fecc9a4cf5903c06e9`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_inventory_catalog_and_public_coverage`

No test docstring is declared.

**Direct call names in source:** `_mini_toolkit`, `audit_catalog`, `audit_public_symbol_execution`, `build_inventory`, `coverage.write_text`, `json.dumps`, `str`  
**Node ID:** `tests/test_inventory_reports_process.py::test_inventory_catalog_and_public_coverage`  
**Area:** Standalone verification harness  
**Source line:** 30

## `test_junit_process_logging_and_reports`

No test docstring is declared.

**Direct call names in source:** `(tmp_path / name).is_file`, `ProbeResult`, `RunSummary`, `blocked_result`, `configure_logging`, `events.emit`, `junit.write_text`, `logger.info`, `parse_junit`, `run_process_test`, `str`, `write_adapter_report`, `write_html_report`, `write_json_report`, `write_markdown_report`  
**Node ID:** `tests/test_inventory_reports_process.py::test_junit_process_logging_and_reports`  
**Area:** Standalone verification harness  
**Source line:** 51

## `test_suite_schemas_and_catalog_are_valid`

No test docstring is declared.

**Direct call names in source:** `Path`, `Path(x86decomp_testkit.__file__).resolve`, `catalog_path.read_text`, `files`, `files('x86decomp_testkit').joinpath`, `json.loads`, `path.read_text`, `schema_dir.glob`, `schema_dir.is_dir`, `str`, `validator_for`, `validator_for(schema).check_schema`  
**Node ID:** `tests/test_inventory_reports_process.py::test_suite_schemas_and_catalog_are_valid`  
**Area:** Standalone verification harness  
**Source line:** 79

## `test_recursive_inventory_includes_capability_packages_and_nested_schemas`

No test docstring is declared.

**Direct call names in source:** `(nested / 'item.schema.json').write_text`, `(package / '__init__.py').write_text`, `(package / 'api.py').write_text`, `_mini_toolkit`, `build_inventory`, `nested.mkdir`, `package.mkdir`  
**Node ID:** `tests/test_inventory_reports_process.py::test_recursive_inventory_includes_capability_packages_and_nested_schemas`  
**Area:** Standalone verification harness  
**Source line:** 97
