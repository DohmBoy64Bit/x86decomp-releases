---
title: tests/native/test_cli_schemas.py
description: Source-derived reference for 4 collected test nodes.
---

# `tests/native/test_cli_schemas.py`

**Collected nodes:** 4  
**Source SHA-256:** `7cc3fd0822bdffd81b3423924fb7000415b08cd60cfa14d88aa2d98df34a78fc`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_native_project_init_and_all_leaf_help`

No test docstring is declared.

**Direct call names in source:** `_leaf_commands`, `build_parser`, `capsys.readouterr`, `command.split`, `json.loads`, `len`, `main`, `parser.parse_args`, `str`  
**Node ID:** `tests/native/test_cli_schemas.py::test_native_project_init_and_all_leaf_help`  
**Area:** Toolkit behavior  
**Source line:** 26

## `test_main_cli_exposes_native_capabilities`

No test docstring is declared.

**Direct call names in source:** `_build_parser`, `capsys.readouterr`, `json.loads`, `next`, `set`, `toolkit_main`  
**Node ID:** `tests/native/test_cli_schemas.py::test_main_cli_exposes_native_capabilities`  
**Area:** Toolkit behavior  
**Source line:** 36

## `test_native_schemas_meta_validate`

No test docstring is declared.

**Direct call names in source:** `(ROOT / 'schemas/native').glob`, `Draft202012Validator.check_schema`, `json.loads`, `len`, `path.read_text`, `sorted`  
**Node ID:** `tests/native/test_cli_schemas.py::test_native_schemas_meta_validate`  
**Area:** Toolkit behavior  
**Source line:** 46

## `test_native_store_keeps_all_prior_schema_layers`

No test docstring is declared.

**Direct call names in source:** `NativeStore`, `NativeStore(tmp_path).check`  
**Node ID:** `tests/native/test_cli_schemas.py::test_native_store_keeps_all_prior_schema_layers`  
**Area:** Toolkit behavior  
**Source line:** 51
