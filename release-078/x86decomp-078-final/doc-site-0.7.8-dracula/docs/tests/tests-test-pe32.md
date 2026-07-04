---
title: tests/test_pe32.py
description: Source-derived reference for 2 collected test nodes.
---

# `tests/test_pe32.py`

**Collected nodes:** 2  
**Source SHA-256:** `4952257965fe3a61bc43d6a099b190264e924ecc85fdc8ba4e42e4a32bdc79c4`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_parse_minimal_i386_image`

No test docstring is declared.

**Direct call names in source:** `Path`, `build_minimal_pe32`, `len`, `parse_pe32`, `self.assertEqual`, `tempfile.TemporaryDirectory`  
**Node ID:** `tests/test_pe32.py::PE32Tests::test_parse_minimal_i386_image`  
**Area:** Toolkit behavior  
**Source line:** 13

## `test_reject_non_pe`

No test docstring is declared.

**Direct call names in source:** `Path`, `parse_pe32`, `path.write_bytes`, `self.assertRaises`, `tempfile.TemporaryDirectory`  
**Node ID:** `tests/test_pe32.py::PE32Tests::test_reject_non_pe`  
**Area:** Toolkit behavior  
**Source line:** 25
