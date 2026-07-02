---
title: tests/governance/test_proof_plugin_worker.py
description: 8 exact current test nodes
original_path: tests/tests-governance-test-proof-plugin-worker.html
---

<a id="test-test-proof-ledger-and-bundle"></a>
<a id="test-test-proof-bundle-rejects-outside-artifact"></a>
<a id="test-test-plugin-install-doctor-invoke"></a>
<a id="test-test-plugin-rejects-undeclared-capability"></a>
<a id="test-test-worker-registry-selection-and-doctor"></a>
<a id="test-test-changeset-round-trip"></a>
<a id="test-test-changeset-base-mismatch"></a>
<a id="test-test-plugin-list-and-proof-inspect"></a>

Section: Source-derived test reference

# `tests/governance/test_proof_plugin_worker.py`

8 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `1cf8e1e2877783f7375ac2a2305fa708eafecc1591cc27e6b54d026bc6b03829`.

Metadata: Toolkit behavior · line 17

### `test_proof_ledger_and_bundle`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `GovernanceStore`, `ProofLedger`, `ledger.create_obligation`, `ledger.add_result`, `artifact.parent.mkdir`, `artifact.write_text`, `ProofBundle.export`, `ledger.evaluate`, `ProofBundle.verify`

**Node ID:** `tests/governance/test_proof_plugin_worker.py::test_proof_ledger_and_bundle`

Metadata: Toolkit behavior · line 29

### `test_proof_bundle_rejects_outside_artifact`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `GovernanceStore`, `store.initialize`, `outside.write_text`, `pytest.raises`, `ProofBundle.export`

**Node ID:** `tests/governance/test_proof_plugin_worker.py::test_proof_bundle_rejects_outside_artifact`

Metadata: Toolkit behavior · line 42

### `test_plugin_install_doctor_invoke`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `_plugin`, `PluginRegistry`, `api.install`, `executable.write_text`, `GovernanceStore`, `api.doctor`, `api.invoke`

**Node ID:** `tests/governance/test_proof_plugin_worker.py::test_plugin_install_doctor_invoke`

Metadata: Toolkit behavior · line 50

### `test_plugin_rejects_undeclared_capability`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `_plugin`, `PluginRegistry`, `api.install`, `GovernanceStore`, `pytest.raises`, `api.invoke`

**Node ID:** `tests/governance/test_proof_plugin_worker.py::test_plugin_rejects_undeclared_capability`

Metadata: Toolkit behavior · line 55

### `test_worker_registry_selection_and_doctor`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `WorkerRegistry`, `api.register`, `GovernanceStore`, `api.doctor`, `api.select`, `api.set_status`

**Node ID:** `tests/governance/test_proof_plugin_worker.py::test_worker_registry_selection_and_doctor`

Metadata: Toolkit behavior · line 62

### `test_changeset_round_trip`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `GovernanceStore`, `source.initialize`, `source.audit`, `ChangeSet.export`, `target.initialize`, `ChangeSet.apply`, `target.verify_audit_chain`

**Node ID:** `tests/governance/test_proof_plugin_worker.py::test_changeset_round_trip`

Metadata: Toolkit behavior · line 70

### `test_changeset_base_mismatch`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `GovernanceStore`, `source.initialize`, `source.audit`, `ChangeSet.export`, `target.initialize`, `target.audit`, `pytest.raises`, `ChangeSet.apply`

**Node ID:** `tests/governance/test_proof_plugin_worker.py::test_changeset_base_mismatch`

Metadata: Toolkit behavior · line 76

### `test_plugin_list_and_proof_inspect`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `_plugin`, `PluginRegistry`, `api.install`, `GovernanceStore`, `store.initialize`, `ProofBundle.export`, `len`, `ProofBundle.inspect`, `api.list`

**Node ID:** `tests/governance/test_proof_plugin_worker.py::test_plugin_list_and_proof_inspect`
