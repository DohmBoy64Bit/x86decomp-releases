---
title: tests/test_evidence.py
description: 2 exact current test nodes
original_path: tests/tests-test-evidence.html
---

<a id="test-evidencetests-test-three-independent-sources-verify-claim"></a>
<a id="test-evidencetests-test-same-group-does-not-verify"></a>

Section: Source-derived test reference

# `tests/test_evidence.py`

2 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `4e8b73d7ad07cbce395ffe1267c272aeabdb861c0d198b6b8fcf5b448341b669`.

Metadata: Toolkit behavior · line 12

### `EvidenceTests::test_three_independent_sources_verify_claim`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `tempfile.TemporaryDirectory`, `Path`, `EvidenceStore`, `enumerate`, `store.create_claim`, `store.verify_claim`, `self.assertEqual`, `path.write_bytes`, `evidence.append`, `bytes`, `store.add_evidence`

**Node ID:** `tests/test_evidence.py::EvidenceTests::test_three_independent_sources_verify_claim`

Metadata: Toolkit behavior · line 48

### `EvidenceTests::test_same_group_does_not_verify`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `tempfile.TemporaryDirectory`, `Path`, `EvidenceStore`, `range`, `store.create_claim`, `store.verify_claim`, `self.assertNotEqual`, `self.assertTrue`, `store.add_evidence`, `ids.append`

**Node ID:** `tests/test_evidence.py::EvidenceTests::test_same_group_does_not_verify`
