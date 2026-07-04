---
title: tests/governance/test_core.py
description: Source-derived reference for 17 collected test nodes.
---

# `tests/governance/test_core.py`

**Collected nodes:** 17  
**Source SHA-256:** `d2c62ade326140850549e48c1255cab3a45ec3f69d2374f4aff21380cd1ccc0d`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_store_is_additive_and_audit_chain`

No test docstring is declared.

**Direct call names in source:** `con.commit`, `con.execute`, `con.execute('SELECT value FROM legacy_data').fetchone`, `s.audit`, `s.check`, `s.connect`, `s.initialize`, `s.verify_audit_chain`, `store`  
**Node ID:** `tests/governance/test_core.py::test_store_is_additive_and_audit_chain`  
**Area:** Toolkit behavior  
**Source line:** 24

## `test_audit_tamper_detected`

No test docstring is declared.

**Direct call names in source:** `con.commit`, `con.execute`, `s.audit`, `s.connect`, `s.initialize`, `s.verify_audit_chain`, `store`  
**Node ID:** `tests/governance/test_core.py::test_audit_tamper_detected`  
**Area:** Toolkit behavior  
**Source line:** 36

## `test_hypothesis_gate_and_accept`

No test docstring is declared.

**Direct call names in source:** `HypothesisLedger`, `enumerate`, `ledger.attach_evidence`, `ledger.create`, `ledger.transition`, `store`  
**Node ID:** `tests/governance/test_core.py::test_hypothesis_gate_and_accept`  
**Area:** Toolkit behavior  
**Source line:** 43

## `test_hypothesis_contradiction_blocks_acceptance`

No test docstring is declared.

**Direct call names in source:** `HypothesisLedger`, `ledger.acceptance_gate`, `ledger.attach_evidence`, `ledger.create`, `range`, `store`  
**Node ID:** `tests/governance/test_core.py::test_hypothesis_contradiction_blocks_acceptance`  
**Area:** Toolkit behavior  
**Source line:** 54

## `test_hypothesis_dependency_cycle_rejected`

No test docstring is declared.

**Direct call names in source:** `HypothesisLedger`, `ledger.add_dependency`, `ledger.create`, `pytest.raises`, `store`  
**Node ID:** `tests/governance/test_core.py::test_hypothesis_dependency_cycle_rejected`  
**Area:** Toolkit behavior  
**Source line:** 61

## `test_campaign_lifecycle_and_planner`

No test docstring is declared.

**Direct call names in source:** `CampaignEngine`, `api.create`, `api.get`, `api.pause`, `api.plan_next`, `api.resume`, `api.start`, `store`  
**Node ID:** `tests/governance/test_core.py::test_campaign_lifecycle_and_planner`  
**Area:** Toolkit behavior  
**Source line:** 67

## `test_campaign_budget_blocks`

No test docstring is declared.

**Direct call names in source:** `CampaignEngine`, `api.create`, `api.get`, `api.plan_next`, `api.start`, `pytest.raises`, `store`  
**Node ID:** `tests/governance/test_core.py::test_campaign_budget_blocks`  
**Area:** Toolkit behavior  
**Source line:** 75

## `test_campaign_branch`

No test docstring is declared.

**Direct call names in source:** `CampaignEngine`, `api.branch`, `api.create`, `store`  
**Node ID:** `tests/governance/test_core.py::test_campaign_branch`  
**Area:** Toolkit behavior  
**Source line:** 81

## `test_candidate_branch_compare_and_promotion`

No test docstring is declared.

**Direct call names in source:** `CandidateStore`, `api.add_file`, `api.compare`, `api.create`, `api.record_evaluation`, `api.transition`, `source.write_text`, `store`  
**Node ID:** `tests/governance/test_core.py::test_candidate_branch_compare_and_promotion`  
**Area:** Toolkit behavior  
**Source line:** 87

## `test_candidate_rejects_traversal`

No test docstring is declared.

**Direct call names in source:** `CandidateStore`, `api.add_file`, `api.create`, `f.write_text`, `pytest.raises`, `store`  
**Node ID:** `tests/governance/test_core.py::test_candidate_rejects_traversal`  
**Area:** Toolkit behavior  
**Source line:** 96

## `test_ddmin_and_counterexample_promotion`

No test docstring is declared.

**Direct call names in source:** `CounterexampleStore`, `Path`, `Path(promoted['fixture']).read_bytes`, `api.add`, `api.minimize`, `api.promote_to_regression`, `ddmin_bytes`, `store`  
**Node ID:** `tests/governance/test_core.py::test_ddmin_and_counterexample_promotion`  
**Area:** Toolkit behavior  
**Source line:** 101

## `test_consensus_conflict_and_resolution`

No test docstring is declared.

**Direct call names in source:** `ConsensusEngine`, `api.conflicts`, `api.explain`, `api.record`, `api.resolve`, `len`, `store`  
**Node ID:** `tests/governance/test_core.py::test_consensus_conflict_and_resolution`  
**Area:** Toolkit behavior  
**Source line:** 111

## `test_graph_impact`

No test docstring is declared.

**Direct call names in source:** `KnowledgeGraph`, `api.add_edge`, `api.impact`, `api.upsert_node`, `store`  
**Node ID:** `tests/governance/test_core.py::test_graph_impact`  
**Area:** Toolkit behavior  
**Source line:** 120

## `test_review_lock_resists_automation`

No test docstring is declared.

**Direct call names in source:** `ReviewQueue`, `api.create`, `api.decide`, `pytest.raises`, `store`  
**Node ID:** `tests/governance/test_core.py::test_review_lock_resists_automation`  
**Area:** Toolkit behavior  
**Source line:** 126

## `test_family_correlation_is_bounded`

No test docstring is declared.

**Direct call names in source:** `BinaryFamilyStore`, `a.write_bytes`, `api.add`, `api.correlate`, `api.create`, `b.write_bytes`, `pytest.approx`, `store`  
**Node ID:** `tests/governance/test_core.py::test_family_correlation_is_bounded`  
**Area:** Toolkit behavior  
**Source line:** 132

## `test_remaining_public_list_snapshot_and_review_paths`

No test docstring is declared.

**Direct call names in source:** `CampaignEngine`, `CandidateStore`, `CounterexampleStore`, `HypothesisLedger`, `ReviewQueue`, `campaigns.create`, `campaigns.list`, `campaigns.plan_next`, `campaigns.snapshot`, `campaigns.start`, `campaigns.stop`, `candidates.create`, `candidates.list`, `counterexamples.add`, `counterexamples.list`, `hypotheses.create`, `hypotheses.list`, `reviews.assign`, `reviews.create`, `reviews.list`, `reviews.lock`, `store`  
**Node ID:** `tests/governance/test_core.py::test_remaining_public_list_snapshot_and_review_paths`  
**Area:** Toolkit behavior  
**Source line:** 140

## `test_family_report_path`

No test docstring is declared.

**Direct call names in source:** `BinaryFamilyStore`, `api.add`, `api.create`, `api.report`, `f.write_bytes`, `len`, `store`  
**Node ID:** `tests/governance/test_core.py::test_family_report_path`  
**Area:** Toolkit behavior  
**Source line:** 152
