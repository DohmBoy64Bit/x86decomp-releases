---
title: tests/test_project.py
description: 2 exact current test nodes
original_path: tests/tests-test-project.html
---

<a id="test-projecttests-test-initialize-and-verify"></a>
<a id="test-projecttests-test-detect-binary-tampering"></a>

Section: Source-derived test reference

# `tests/test_project.py`

2 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `04d73c197e4b7979731c140bef24e36ab323099e715d5462c95983a83d558c2b`.

Metadata: Toolkit behavior · line 12

### `ProjectTests::test_initialize_and_verify`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `tempfile.TemporaryDirectory`, `Path`, `build_minimal_pe32`, `initialize_project`, `self.assertTrue`, `self.assertEqual`, `verify_project`, `is_file`

**Node ID:** `tests/test_project.py::ProjectTests::test_initialize_and_verify`

Metadata: Toolkit behavior · line 24

### `ProjectTests::test_detect_binary_tampering`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `tempfile.TemporaryDirectory`, `Path`, `build_minimal_pe32`, `initialize_project`, `stored.write_bytes`, `verify_project`, `self.assertFalse`, `self.assertTrue`, `any`, `stored.read_bytes`

**Node ID:** `tests/test_project.py::ProjectTests::test_detect_binary_tampering`
