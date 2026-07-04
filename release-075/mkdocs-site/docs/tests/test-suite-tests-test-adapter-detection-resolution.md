---
title: test-suite/tests/test_adapter_detection_resolution.py
description: Source-derived reference for 6 collected test nodes.
---

# `test-suite/tests/test_adapter_detection_resolution.py`

**Collected nodes:** 6  
**Source SHA-256:** `bb43b876b5eaaa74b2628c333716d035dcea15ae5231560b06bce4813abfb560`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_installed_adapter_never_prompts`

No test docstring is declared.

**Direct call names in source:** `AdapterSpec`, `AssertionError`, `Path`, `_config`, `prompts.append`, `resolve_missing_adapters`  
**Node ID:** `tests/test_adapter_detection_resolution.py::test_installed_adapter_never_prompts`  
**Area:** Standalone verification harness  
**Source line:** 20

## `test_missing_adapter_prompts_custom_path_then_accepts`

No test docstring is declared.

**Direct call names in source:** `AdapterSpec`, `_config`, `executable.chmod`, `executable.write_text`, `iter`, `next`, `prompts.append`, `prompts[0].startswith`, `resolve_missing_adapters`, `str`  
**Node ID:** `tests/test_adapter_detection_resolution.py::test_missing_adapter_prompts_custom_path_then_accepts`  
**Area:** Standalone verification harness  
**Source line:** 34

## `test_missing_noninteractive_is_explicit_unresolved`

No test docstring is declared.

**Direct call names in source:** `AdapterSpec`, `_config`, `resolve_missing_adapters`  
**Node ID:** `tests/test_adapter_detection_resolution.py::test_missing_noninteractive_is_explicit_unresolved`  
**Area:** Standalone verification harness  
**Source line:** 54

## `test_environment_and_configured_root_detection`

No test docstring is declared.

**Direct call names in source:** `AdapterSpec`, `_config`, `detect_adapter`, `detect_all`, `len`, `monkeypatch.setenv`, `str`, `tool.chmod`, `tool.parent.mkdir`, `tool.write_text`  
**Node ID:** `tests/test_adapter_detection_resolution.py::test_environment_and_configured_root_detection`  
**Area:** Standalone verification harness  
**Source line:** 62

## `test_path_detection_preserves_symlink_argv0`

No test docstring is declared.

**Direct call names in source:** `(tmp_path / '_sym_probe').symlink_to`, `AdapterSpec`, `Path`, `_config`, `alias.symlink_to`, `detect_adapter`, `monkeypatch.setenv`, `str`, `target.chmod`, `target.write_text`  
**Node ID:** `tests/test_adapter_detection_resolution.py::test_path_detection_preserves_symlink_argv0`  
**Area:** Standalone verification harness  
**Source line:** 79

## `test_missing_python_adapter_accepts_custom_interpreter`

No test docstring is declared.

**Direct call names in source:** `AdapterSpec`, `_config`, `iter`, `next`, `resolve_missing_adapters`, `str`  
**Node ID:** `tests/test_adapter_detection_resolution.py::test_missing_python_adapter_accepts_custom_interpreter`  
**Area:** Standalone verification harness  
**Source line:** 96
