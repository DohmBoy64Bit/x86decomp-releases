---
title: test-suite/tests/test_inventory_reports_process.py
description: 4 exact current test nodes
original_path: tests/test-suite-tests-test-inventory-reports-process.html
---

<a id="test-test-inventory-catalog-and-public-coverage"></a>
<a id="test-test-junit-process-logging-and-reports"></a>
<a id="test-test-suite-schemas-and-catalog-are-valid"></a>
<a id="test-test-recursive-inventory-includes-capability-packages-and-nested-schemas"></a>

Section: Source-derived test reference

# `test-suite/tests/test_inventory_reports_process.py`

4 current test nodes in the Standalone verifier inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `15d8fac0bc3a91ab86a6997e86618452b3b317fb57edacb787989539d8eb1f64`.

Metadata: Standalone verifier · line 30

### `test_inventory_catalog_and_public_coverage`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `_mini_toolkit`, `build_inventory`, `coverage.write_text`, `audit_public_symbol_execution`, `audit_catalog`, `json.dumps`, `str`

**Node ID:** `test-suite/tests/test_inventory_reports_process.py::test_inventory_catalog_and_public_coverage`

Metadata: Standalone verifier · line 51

### `test_junit_process_logging_and_reports`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `junit.write_text`, `parse_junit`, `configure_logging`, `logger.info`, `events.emit`, `run_process_test`, `RunSummary`, `write_json_report`, `write_markdown_report`, `write_html_report`, `write_adapter_report`, `is_file`, `blocked_result`, `str`, `ProbeResult`

**Node ID:** `test-suite/tests/test_inventory_reports_process.py::test_junit_process_logging_and_reports`

Metadata: Standalone verifier · line 79

### `test_suite_schemas_and_catalog_are_valid`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `schema_dir.is_dir`, `Path`, `json.loads`, `schema_dir.glob`, `str`, `catalog_path.read_text`, `resolve`, `check_schema`, `joinpath`, `path.read_text`, `validator_for`, `files`

**Node ID:** `test-suite/tests/test_inventory_reports_process.py::test_suite_schemas_and_catalog_are_valid`

Metadata: Standalone verifier · line 97

### `test_recursive_inventory_includes_capability_packages_and_nested_schemas`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `_mini_toolkit`, `package.mkdir`, `write_text`, `nested.mkdir`, `build_inventory`

**Node ID:** `test-suite/tests/test_inventory_reports_process.py::test_recursive_inventory_includes_capability_packages_and_nested_schemas`
