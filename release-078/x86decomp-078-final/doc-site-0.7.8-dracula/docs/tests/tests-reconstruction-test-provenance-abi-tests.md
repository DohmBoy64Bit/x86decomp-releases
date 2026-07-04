---
title: tests/reconstruction/test_provenance_abi_tests.py
description: Source-derived reference for 3 collected test nodes.
---

# `tests/reconstruction/test_provenance_abi_tests.py`

**Collected nodes:** 3  
**Source SHA-256:** `df4e2725330a4cfc5e4d6f5817d062bbcc6c9db120d0e5435a665d453910557d`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_provenance_round_trip_edit_reconciliation_and_locks`

No test docstring is declared.

**Direct call names in source:** `Path`, `Path(api.export(tmp_path / 'prov.json')['path']).is_file`, `ProvenanceLedger`, `ReconstructionStore`, `api.binary`, `api.export`, `api.impact`, `api.lock`, `api.reconcile`, `api.record`, `api.source`, `api.unlock`, `hashlib.sha256`, `hashlib.sha256(source.read_bytes()).hexdigest`, `pytest.raises`, `source.parent.mkdir`, `source.read_bytes`, `source.write_text`  
**Node ID:** `tests/reconstruction/test_provenance_abi_tests.py::test_provenance_round_trip_edit_reconciliation_and_locks`  
**Area:** Toolkit behavior  
**Source line:** 16

## `test_abi_contract_verification_comparison_and_explicit_shim`

No test docstring is declared.

**Direct call names in source:** `ABIContracts`, `Path`, `Path(api.export(left['contract_id'], tmp_path / 'abi.json')['path']).is_file`, `ReconstructionStore`, `api.compare`, `api.export`, `api.recover`, `api.shim`, `api.verify`  
**Node ID:** `tests/reconstruction/test_provenance_abi_tests.py::test_abi_contract_verification_comparison_and_explicit_shim`  
**Area:** Toolkit behavior  
**Source line:** 32

## `test_generated_tests_are_evidence_bound_and_counterexamples_promote`

No test docstring is declared.

**Direct call names in source:** `(tmp_path / item['relative_path']).is_file`, `CounterexampleStore`, `CounterexampleStore(store).add`, `GeneratedTests`, `ReconstructionStore`, `api.add`, `api.explain`, `api.list`, `api.promote_counterexample`, `api.synthesize`, `pytest.raises`  
**Node ID:** `tests/reconstruction/test_provenance_abi_tests.py::test_generated_tests_are_evidence_bound_and_counterexamples_promote`  
**Area:** Toolkit behavior  
**Source line:** 44
