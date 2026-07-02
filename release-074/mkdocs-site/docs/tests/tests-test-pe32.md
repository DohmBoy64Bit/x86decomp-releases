---
title: tests/test_pe32.py
description: 2 exact current test nodes
original_path: tests/tests-test-pe32.html
---

<a id="test-pe32tests-test-parse-minimal-i386-image"></a>
<a id="test-pe32tests-test-reject-non-pe"></a>

Section: Source-derived test reference

# `tests/test_pe32.py`

2 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `4952257965fe3a61bc43d6a099b190264e924ecc85fdc8ba4e42e4a32bdc79c4`.

Metadata: Toolkit behavior · line 13

### `PE32Tests::test_parse_minimal_i386_image`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `tempfile.TemporaryDirectory`, `build_minimal_pe32`, `parse_pe32`, `self.assertEqual`, `len`, `Path`

**Node ID:** `tests/test_pe32.py::PE32Tests::test_parse_minimal_i386_image`

Metadata: Toolkit behavior · line 25

### `PE32Tests::test_reject_non_pe`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `tempfile.TemporaryDirectory`, `path.write_bytes`, `Path`, `self.assertRaises`, `parse_pe32`

**Node ID:** `tests/test_pe32.py::PE32Tests::test_reject_non_pe`
