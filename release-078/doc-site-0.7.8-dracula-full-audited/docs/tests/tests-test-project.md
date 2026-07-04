---
title: tests/test_project.py
description: Source-derived reference for 2 collected test nodes.
---

# `tests/test_project.py`

**Collected nodes:** 2  
**Source SHA-256:** `04d73c197e4b7979731c140bef24e36ab323099e715d5462c95983a83d558c2b`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_detect_binary_tampering`

No test docstring is declared.

**Direct call names in source:** `Path`, `any`, `build_minimal_pe32`, `initialize_project`, `self.assertFalse`, `self.assertTrue`, `stored.read_bytes`, `stored.write_bytes`, `tempfile.TemporaryDirectory`, `verify_project`  
**Node ID:** `tests/test_project.py::ProjectTests::test_detect_binary_tampering`  
**Area:** Toolkit behavior  
**Source line:** 24

## `test_initialize_and_verify`

No test docstring is declared.

**Direct call names in source:** `(project_root / 'analysis' / 'program.json').is_file`, `(project_root / 'project.json').is_file`, `Path`, `build_minimal_pe32`, `initialize_project`, `self.assertEqual`, `self.assertTrue`, `tempfile.TemporaryDirectory`, `verify_project`  
**Node ID:** `tests/test_project.py::ProjectTests::test_initialize_and_verify`  
**Area:** Toolkit behavior  
**Source line:** 12
