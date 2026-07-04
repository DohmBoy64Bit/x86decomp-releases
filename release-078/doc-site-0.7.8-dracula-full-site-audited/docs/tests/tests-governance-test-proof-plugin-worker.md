---
title: tests/governance/test_proof_plugin_worker.py
description: Source-derived reference for 8 collected test nodes.
---

# `tests/governance/test_proof_plugin_worker.py`

**Collected nodes:** 8  
**Source SHA-256:** `1cf8e1e2877783f7375ac2a2305fa708eafecc1591cc27e6b54d026bc6b03829`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_proof_ledger_and_bundle`

No test docstring is declared.

**Direct call names in source:** `GovernanceStore`, `ProofBundle.export`, `ProofBundle.verify`, `ProofLedger`, `artifact.parent.mkdir`, `artifact.write_text`, `ledger.add_result`, `ledger.create_obligation`, `ledger.evaluate`  
**Node ID:** `tests/governance/test_proof_plugin_worker.py::test_proof_ledger_and_bundle`  
**Area:** Toolkit behavior  
**Source line:** 17

## `test_proof_bundle_rejects_outside_artifact`

No test docstring is declared.

**Direct call names in source:** `GovernanceStore`, `ProofBundle.export`, `outside.write_text`, `pytest.raises`, `store.initialize`  
**Node ID:** `tests/governance/test_proof_plugin_worker.py::test_proof_bundle_rejects_outside_artifact`  
**Area:** Toolkit behavior  
**Source line:** 29

## `test_plugin_install_doctor_invoke`

No test docstring is declared.

**Direct call names in source:** `GovernanceStore`, `PluginRegistry`, `_plugin`, `api.doctor`, `api.install`, `api.invoke`, `executable.write_text`  
**Node ID:** `tests/governance/test_proof_plugin_worker.py::test_plugin_install_doctor_invoke`  
**Area:** Toolkit behavior  
**Source line:** 42

## `test_plugin_rejects_undeclared_capability`

No test docstring is declared.

**Direct call names in source:** `GovernanceStore`, `PluginRegistry`, `_plugin`, `api.install`, `api.invoke`, `pytest.raises`  
**Node ID:** `tests/governance/test_proof_plugin_worker.py::test_plugin_rejects_undeclared_capability`  
**Area:** Toolkit behavior  
**Source line:** 50

## `test_worker_registry_selection_and_doctor`

No test docstring is declared.

**Direct call names in source:** `GovernanceStore`, `WorkerRegistry`, `api.doctor`, `api.register`, `api.select`, `api.set_status`  
**Node ID:** `tests/governance/test_proof_plugin_worker.py::test_worker_registry_selection_and_doctor`  
**Area:** Toolkit behavior  
**Source line:** 55

## `test_changeset_round_trip`

No test docstring is declared.

**Direct call names in source:** `ChangeSet.apply`, `ChangeSet.export`, `GovernanceStore`, `source.audit`, `source.initialize`, `target.initialize`, `target.verify_audit_chain`  
**Node ID:** `tests/governance/test_proof_plugin_worker.py::test_changeset_round_trip`  
**Area:** Toolkit behavior  
**Source line:** 62

## `test_changeset_base_mismatch`

No test docstring is declared.

**Direct call names in source:** `ChangeSet.apply`, `ChangeSet.export`, `GovernanceStore`, `pytest.raises`, `source.audit`, `source.initialize`, `target.audit`, `target.initialize`  
**Node ID:** `tests/governance/test_proof_plugin_worker.py::test_changeset_base_mismatch`  
**Area:** Toolkit behavior  
**Source line:** 70

## `test_plugin_list_and_proof_inspect`

No test docstring is declared.

**Direct call names in source:** `GovernanceStore`, `PluginRegistry`, `ProofBundle.export`, `ProofBundle.inspect`, `_plugin`, `api.install`, `api.list`, `len`, `store.initialize`  
**Node ID:** `tests/governance/test_proof_plugin_worker.py::test_plugin_list_and_proof_inspect`  
**Area:** Toolkit behavior  
**Source line:** 76
