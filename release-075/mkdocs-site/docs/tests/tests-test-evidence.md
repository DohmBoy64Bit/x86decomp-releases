---
title: tests/test_evidence.py
description: Source-derived reference for 2 collected test nodes.
---

# `tests/test_evidence.py`

**Collected nodes:** 2  
**Source SHA-256:** `4e8b73d7ad07cbce395ffe1267c272aeabdb861c0d198b6b8fcf5b448341b669`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_same_group_does_not_verify`

No test docstring is declared.

**Direct call names in source:** `EvidenceStore`, `Path`, `ids.append`, `range`, `self.assertNotEqual`, `self.assertTrue`, `store.add_evidence`, `store.create_claim`, `store.verify_claim`, `tempfile.TemporaryDirectory`  
**Node ID:** `tests/test_evidence.py::EvidenceTests::test_same_group_does_not_verify`  
**Area:** Toolkit behavior  
**Source line:** 48

## `test_three_independent_sources_verify_claim`

No test docstring is declared.

**Direct call names in source:** `EvidenceStore`, `Path`, `bytes`, `enumerate`, `evidence.append`, `path.write_bytes`, `self.assertEqual`, `store.add_evidence`, `store.create_claim`, `store.verify_claim`, `tempfile.TemporaryDirectory`  
**Node ID:** `tests/test_evidence.py::EvidenceTests::test_three_independent_sources_verify_claim`  
**Area:** Toolkit behavior  
**Source line:** 12
