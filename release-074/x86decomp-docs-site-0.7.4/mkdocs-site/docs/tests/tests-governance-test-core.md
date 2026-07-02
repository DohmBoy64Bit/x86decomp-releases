---
title: tests/governance/test_core.py
description: 17 exact current test nodes
original_path: tests/tests-governance-test-core.html
---

<a id="test-test-store-is-additive-and-audit-chain"></a>
<a id="test-test-audit-tamper-detected"></a>
<a id="test-test-hypothesis-gate-and-accept"></a>
<a id="test-test-hypothesis-contradiction-blocks-acceptance"></a>
<a id="test-test-hypothesis-dependency-cycle-rejected"></a>
<a id="test-test-campaign-lifecycle-and-planner"></a>
<a id="test-test-campaign-budget-blocks"></a>
<a id="test-test-campaign-branch"></a>
<a id="test-test-candidate-branch-compare-and-promotion"></a>
<a id="test-test-candidate-rejects-traversal"></a>
<a id="test-test-ddmin-and-counterexample-promotion"></a>
<a id="test-test-consensus-conflict-and-resolution"></a>
<a id="test-test-graph-impact"></a>
<a id="test-test-review-lock-resists-automation"></a>
<a id="test-test-family-correlation-is-bounded"></a>
<a id="test-test-remaining-public-list-snapshot-and-review-paths"></a>
<a id="test-test-family-report-path"></a>

Section: Source-derived test reference

# `tests/governance/test_core.py`

17 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `d2c62ade326140850549e48c1255cab3a45ec3f69d2374f4aff21380cd1ccc0d`.

Metadata: Toolkit behavior · line 24

### `test_store_is_additive_and_audit_chain`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `store`, `s.initialize`, `s.audit`, `s.connect`, `con.execute`, `con.commit`, `s.check`, `s.verify_audit_chain`, `fetchone`

**Node ID:** `tests/governance/test_core.py::test_store_is_additive_and_audit_chain`

Metadata: Toolkit behavior · line 36

### `test_audit_tamper_detected`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `store`, `s.initialize`, `s.audit`, `s.connect`, `con.execute`, `con.commit`, `s.verify_audit_chain`

**Node ID:** `tests/governance/test_core.py::test_audit_tamper_detected`

Metadata: Toolkit behavior · line 43

### `test_hypothesis_gate_and_accept`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `HypothesisLedger`, `ledger.create`, `enumerate`, `ledger.transition`, `store`, `ledger.attach_evidence`

**Node ID:** `tests/governance/test_core.py::test_hypothesis_gate_and_accept`

Metadata: Toolkit behavior · line 54

### `test_hypothesis_contradiction_blocks_acceptance`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `HypothesisLedger`, `ledger.create`, `range`, `ledger.attach_evidence`, `store`, `ledger.acceptance_gate`

**Node ID:** `tests/governance/test_core.py::test_hypothesis_contradiction_blocks_acceptance`

Metadata: Toolkit behavior · line 61

### `test_hypothesis_dependency_cycle_rejected`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `HypothesisLedger`, `ledger.create`, `ledger.add_dependency`, `store`, `pytest.raises`

**Node ID:** `tests/governance/test_core.py::test_hypothesis_dependency_cycle_rejected`

Metadata: Toolkit behavior · line 67

### `test_campaign_lifecycle_and_planner`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `store`, `CampaignEngine`, `api.create`, `api.start`, `api.plan_next`, `api.pause`, `api.resume`, `api.get`

**Node ID:** `tests/governance/test_core.py::test_campaign_lifecycle_and_planner`

Metadata: Toolkit behavior · line 75

### `test_campaign_budget_blocks`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `CampaignEngine`, `api.create`, `api.start`, `store`, `pytest.raises`, `api.plan_next`, `api.get`

**Node ID:** `tests/governance/test_core.py::test_campaign_budget_blocks`

Metadata: Toolkit behavior · line 81

### `test_campaign_branch`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `CampaignEngine`, `api.create`, `api.branch`, `store`

**Node ID:** `tests/governance/test_core.py::test_campaign_branch`

Metadata: Toolkit behavior · line 87

### `test_candidate_branch_compare_and_promotion`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `CandidateStore`, `source.write_text`, `api.create`, `api.add_file`, `api.record_evaluation`, `store`, `api.transition`, `api.compare`

**Node ID:** `tests/governance/test_core.py::test_candidate_branch_compare_and_promotion`

Metadata: Toolkit behavior · line 96

### `test_candidate_rejects_traversal`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `CandidateStore`, `f.write_text`, `api.create`, `store`, `pytest.raises`, `api.add_file`

**Node ID:** `tests/governance/test_core.py::test_candidate_rejects_traversal`

Metadata: Toolkit behavior · line 101

### `test_ddmin_and_counterexample_promotion`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `ddmin_bytes`, `CounterexampleStore`, `api.add`, `api.minimize`, `api.promote_to_regression`, `store`, `read_bytes`, `Path`

**Node ID:** `tests/governance/test_core.py::test_ddmin_and_counterexample_promotion`

Metadata: Toolkit behavior · line 111

### `test_consensus_conflict_and_resolution`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `ConsensusEngine`, `api.record`, `api.resolve`, `store`, `len`, `api.conflicts`, `api.explain`

**Node ID:** `tests/governance/test_core.py::test_consensus_conflict_and_resolution`

Metadata: Toolkit behavior · line 120

### `test_graph_impact`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `KnowledgeGraph`, `api.upsert_node`, `api.add_edge`, `api.impact`, `store`

**Node ID:** `tests/governance/test_core.py::test_graph_impact`

Metadata: Toolkit behavior · line 126

### `test_review_lock_resists_automation`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `ReviewQueue`, `api.create`, `api.decide`, `store`, `pytest.raises`

**Node ID:** `tests/governance/test_core.py::test_review_lock_resists_automation`

Metadata: Toolkit behavior · line 132

### `test_family_correlation_is_bounded`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `BinaryFamilyStore`, `api.create`, `a.write_bytes`, `b.write_bytes`, `api.add`, `api.correlate`, `store`, `pytest.approx`

**Node ID:** `tests/governance/test_core.py::test_family_correlation_is_bounded`

Metadata: Toolkit behavior · line 140

### `test_remaining_public_list_snapshot_and_review_paths`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `store`, `CampaignEngine`, `campaigns.create`, `campaigns.start`, `campaigns.plan_next`, `CandidateStore`, `candidates.create`, `CounterexampleStore`, `counterexamples.add`, `HypothesisLedger`, `hypotheses.create`, `ReviewQueue`, `reviews.create`, `reviews.lock`, `campaigns.stop`, `reviews.assign`, `campaigns.list`, `candidates.list`, `counterexamples.list`, `hypotheses.list`, `reviews.list`, `campaigns.snapshot`

**Node ID:** `tests/governance/test_core.py::test_remaining_public_list_snapshot_and_review_paths`

Metadata: Toolkit behavior · line 152

### `test_family_report_path`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `BinaryFamilyStore`, `api.create`, `f.write_bytes`, `api.add`, `api.report`, `store`, `len`

**Node ID:** `tests/governance/test_core.py::test_family_report_path`
