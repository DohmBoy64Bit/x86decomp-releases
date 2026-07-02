---
title: tests/test_dynamorio.py
description: 2 exact current test nodes
original_path: tests/tests-test-dynamorio.html
---

<a id="test-test-parse-drcov-text"></a>
<a id="test-test-angr-backend-has-explicit-optional-dependency-error"></a>

Section: Source-derived test reference

# `tests/test_dynamorio.py`

2 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `0d182c7c06f6ab60b970935bef97e7327fd18744bdb5d29918a7193d330bde2e`.

Metadata: Toolkit behavior · line 13

### `test_parse_drcov_text`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `log.write_text`, `parse_drcov_text`, `endswith`

**Node ID:** `tests/test_dynamorio.py::test_parse_drcov_text`

Metadata: Toolkit behavior · line 32

### `test_angr_backend_has_explicit_optional_dependency_error`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `subprocess.run`, `importlib.util.find_spec`, `pytest.raises`, `angr_bounded_compare`

**Node ID:** `tests/test_dynamorio.py::test_angr_backend_has_explicit_optional_dependency_error`
