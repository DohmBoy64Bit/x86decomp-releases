---
title: tests/reconstruction/test_provenance_abi_tests.py
description: 3 exact current test nodes
original_path: tests/tests-reconstruction-test-provenance-abi-tests.html
---

<a id="test-test-provenance-round-trip-edit-reconciliation-and-locks"></a>
<a id="test-test-abi-contract-verification-comparison-and-explicit-shim"></a>
<a id="test-test-generated-tests-are-evidence-bound-and-counterexamples-promote"></a>

Section: Source-derived test reference

# `tests/reconstruction/test_provenance_abi_tests.py`

3 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `df4e2725330a4cfc5e4d6f5817d062bbcc6c9db120d0e5435a665d453910557d`.

Metadata: Toolkit behavior · line 16

### `test_provenance_round_trip_edit_reconciliation_and_locks`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `source.parent.mkdir`, `source.write_text`, `ReconstructionStore`, `ProvenanceLedger`, `api.record`, `api.lock`, `api.unlock`, `hexdigest`, `api.reconcile`, `is_file`, `pytest.raises`, `api.impact`, `hashlib.sha256`, `Path`, `api.source`, `api.binary`, `source.read_bytes`, `api.export`

**Node ID:** `tests/reconstruction/test_provenance_abi_tests.py::test_provenance_round_trip_edit_reconciliation_and_locks`

Metadata: Toolkit behavior · line 32

### `test_abi_contract_verification_comparison_and_explicit_shim`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `ABIContracts`, `api.recover`, `api.shim`, `is_file`, `ReconstructionStore`, `api.verify`, `api.compare`, `Path`, `api.export`

**Node ID:** `tests/reconstruction/test_provenance_abi_tests.py::test_abi_contract_verification_comparison_and_explicit_shim`

Metadata: Toolkit behavior · line 44

### `test_generated_tests_are_evidence_bound_and_counterexamples_promote`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `ReconstructionStore`, `GeneratedTests`, `api.synthesize`, `is_file`, `add`, `api.promote_counterexample`, `api.list`, `pytest.raises`, `api.add`, `api.explain`, `CounterexampleStore`

**Node ID:** `tests/reconstruction/test_provenance_abi_tests.py::test_generated_tests_are_evidence_bound_and_counterexamples_promote`
