---
title: test-suite/tests/test_adapter_detection_resolution.py
description: 6 exact current test nodes
original_path: tests/test-suite-tests-test-adapter-detection-resolution.html
---

<a id="test-test-installed-adapter-never-prompts"></a>
<a id="test-test-missing-adapter-prompts-custom-path-then-accepts"></a>
<a id="test-test-missing-noninteractive-is-explicit-unresolved"></a>
<a id="test-test-environment-and-configured-root-detection"></a>
<a id="test-test-path-detection-preserves-symlink-argv0"></a>
<a id="test-test-missing-python-adapter-accepts-custom-interpreter"></a>

Section: Source-derived test reference

# `test-suite/tests/test_adapter_detection_resolution.py`

6 current test nodes in the Standalone verifier inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `d2b5626de04bac6ee52935b4db6e5437c56a6edf94ef300504008eccdf4d7812`.

Metadata: Standalone verifier · line 20

### `test_installed_adapter_never_prompts`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `AdapterSpec`, `_config`, `resolve_missing_adapters`, `prompts.append`, `AssertionError`, `Path`

**Node ID:** `test-suite/tests/test_adapter_detection_resolution.py::test_installed_adapter_never_prompts`

Metadata: Standalone verifier · line 34

### `test_missing_adapter_prompts_custom_path_then_accepts`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `executable.write_text`, `executable.chmod`, `AdapterSpec`, `_config`, `iter`, `resolve_missing_adapters`, `startswith`, `prompts.append`, `next`, `str`

**Node ID:** `test-suite/tests/test_adapter_detection_resolution.py::test_missing_adapter_prompts_custom_path_then_accepts`

Metadata: Standalone verifier · line 54

### `test_missing_noninteractive_is_explicit_unresolved`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `AdapterSpec`, `_config`, `resolve_missing_adapters`

**Node ID:** `test-suite/tests/test_adapter_detection_resolution.py::test_missing_noninteractive_is_explicit_unresolved`

Metadata: Standalone verifier · line 62

### `test_environment_and_configured_root_detection`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `tool.parent.mkdir`, `tool.write_text`, `tool.chmod`, `AdapterSpec`, `_config`, `monkeypatch.setenv`, `str`, `len`, `detect_adapter`, `detect_all`

**Node ID:** `test-suite/tests/test_adapter_detection_resolution.py::test_environment_and_configured_root_detection`

Metadata: Standalone verifier · line 79

### `test_path_detection_preserves_symlink_argv0`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `target.write_text`, `target.chmod`, `alias.symlink_to`, `monkeypatch.setenv`, `AdapterSpec`, `detect_adapter`, `str`, `_config`, `Path`

**Node ID:** `test-suite/tests/test_adapter_detection_resolution.py::test_path_detection_preserves_symlink_argv0`

Metadata: Standalone verifier · line 91

### `test_missing_python_adapter_accepts_custom_interpreter`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `AdapterSpec`, `_config`, `str`, `iter`, `resolve_missing_adapters`, `next`

**Node ID:** `test-suite/tests/test_adapter_detection_resolution.py::test_missing_python_adapter_accepts_custom_interpreter`
