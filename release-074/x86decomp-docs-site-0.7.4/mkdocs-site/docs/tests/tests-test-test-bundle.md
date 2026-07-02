---
title: tests/test_test_bundle.py
description: 5 exact current test nodes
original_path: tests/tests-test-test-bundle.html
---

<a id="test-test-static-test-bundle-inspection"></a>
<a id="test-test-test-bundle-hash-is-enforced"></a>
<a id="test-test-test-bundle-rejects-path-traversal"></a>
<a id="test-test-test-bundle-requires-authorization"></a>
<a id="test-test-create-test-bundle-round-trip"></a>

Section: Source-derived test reference

# `tests/test_test_bundle.py`

5 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `e07c08f3155c6ab4b45329aa9076a42632affa7d2c12daa2d70f8657e77e9af6`.

Metadata: Toolkit behavior · line 39

### `test_static_test_bundle_inspection`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `inspect_test_bundle`, `report_path.is_file`, `_bundle`

**Node ID:** `tests/test_test_bundle.py::test_static_test_bundle_inspection`

Metadata: Toolkit behavior · line 49

### `test_test_bundle_hash_is_enforced`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `pytest.raises`, `inspect_test_bundle`, `_bundle`

**Node ID:** `tests/test_test_bundle.py::test_test_bundle_hash_is_enforced`

Metadata: Toolkit behavior · line 54

### `test_test_bundle_rejects_path_traversal`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `zipfile.ZipFile`, `archive.writestr`, `pytest.raises`, `inspect_test_bundle`, `json.dumps`

**Node ID:** `tests/test_test_bundle.py::test_test_bundle_rejects_path_traversal`

Metadata: Toolkit behavior · line 69

### `test_test_bundle_requires_authorization`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `zipfile.ZipFile`, `archive.writestr`, `archive.write`, `pytest.raises`, `inspect_test_bundle`, `json.dumps`

**Node ID:** `tests/test_test_bundle.py::test_test_bundle_requires_authorization`

Metadata: Toolkit behavior · line 84

### `test_create_test_bundle_round_trip`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `create_test_bundle`, `inspect_test_bundle`

**Node ID:** `tests/test_test_bundle.py::test_create_test_bundle_round_trip`
