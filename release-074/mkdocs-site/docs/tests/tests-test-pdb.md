---
title: tests/test_pdb.py
description: 2 exact current test nodes
original_path: tests/tests-test-pdb.html
---

<a id="test-test-invalid-pdb-is-rejected"></a>
<a id="test-test-real-lld-pdb-inventory-identity-and-bundle"></a>

Section: Source-derived test reference

# `tests/test_pdb.py`

2 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `a0966c606b191d2f1c18cc13e839f50919a8b55f937ac07694a324650200e9db`.

Metadata: Toolkit behavior · line 14

### `test_invalid_pdb_is_rejected`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `pytest.raises`, `parse_pdb_bytes`

**Node ID:** `tests/test_pdb.py::test_invalid_pdb_is_rejected`

Metadata: Toolkit behavior · line 23

### `test_real_lld_pdb_inventory_identity_and_bundle`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `pytest.mark.skipif`, `source.write_text`, `subprocess.run`, `to_dict`, `any`, `create_test_bundle`, `inspect_test_bundle`, `str`, `parse_pdb`, `endswith`, `shutil.which`

**Node ID:** `tests/test_pdb.py::test_real_lld_pdb_inventory_identity_and_bundle`
