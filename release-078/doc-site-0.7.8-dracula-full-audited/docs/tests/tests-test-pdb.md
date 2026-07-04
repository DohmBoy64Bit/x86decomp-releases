---
title: tests/test_pdb.py
description: Source-derived reference for 2 collected test nodes.
---

# `tests/test_pdb.py`

**Collected nodes:** 2  
**Source SHA-256:** `a0966c606b191d2f1c18cc13e839f50919a8b55f937ac07694a324650200e9db`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_invalid_pdb_is_rejected`

No test docstring is declared.

**Direct call names in source:** `parse_pdb_bytes`, `pytest.raises`  
**Node ID:** `tests/test_pdb.py::test_invalid_pdb_is_rejected`  
**Area:** Toolkit behavior  
**Source line:** 14

## `test_real_lld_pdb_inventory_identity_and_bundle`

No test docstring is declared.

**Direct call names in source:** `any`, `create_test_bundle`, `inspect_test_bundle`, `module['object_file_name'].endswith`, `parse_pdb`, `parse_pdb(pdb, pe_path=image).to_dict`, `pytest.mark.skipif`, `shutil.which`, `source.write_text`, `str`, `subprocess.run`  
**Node ID:** `tests/test_pdb.py::test_real_lld_pdb_inventory_identity_and_bundle`  
**Area:** Toolkit behavior  
**Source line:** 23
