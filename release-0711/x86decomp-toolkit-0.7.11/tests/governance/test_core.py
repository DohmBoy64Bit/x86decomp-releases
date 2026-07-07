"""Verify the current toolkit behavior covered by `tests/governance/test_core.py`."""
from __future__ import annotations

from pathlib import Path

import pytest

from x86decomp.governance.campaigns import CampaignEngine
from x86decomp.governance.candidates import CandidateStore
from x86decomp.contracts import ContractError
from x86decomp.governance.consensus import ConsensusEngine
from x86decomp.governance.counterexamples import CounterexampleStore, ddmin_bytes
from x86decomp.governance.family import BinaryFamilyStore
from x86decomp.governance.hypotheses import HypothesisLedger
from x86decomp.governance.knowledge_graph import KnowledgeGraph
from x86decomp.governance.reviews import ReviewQueue
from x86decomp.governance.store import GovernanceStore


def store(tmp_path: Path) -> GovernanceStore:
    """Execute the store operation for the current toolkit workflow."""
    return GovernanceStore(tmp_path / "project")


def test_store_is_additive_and_audit_chain(tmp_path: Path) -> None:
    """Verify store is additive and audit chain behavior."""
    s = store(tmp_path); s.initialize()
    with s.connect() as con:
        con.execute("CREATE TABLE legacy_data(id INTEGER PRIMARY KEY, value TEXT)")
        con.execute("INSERT INTO legacy_data(value) VALUES('kept')"); con.commit()
    s.audit("test", "event", "subject", {"x": 1})
    assert s.check()["passed"]
    with s.connect() as con:
        assert con.execute("SELECT value FROM legacy_data").fetchone()[0] == "kept"
    assert s.verify_audit_chain()["events"] == 1


def test_audit_tamper_detected(tmp_path: Path) -> None:
    """Verify audit tamper detected behavior."""
    s=store(tmp_path); s.initialize(); s.audit("a","b",None,{"c":1})
    with s.connect() as con:
        con.execute("UPDATE governance_audit_events SET payload_json='{}'"); con.commit()
    assert not s.verify_audit_chain()["valid"]


def test_hypothesis_gate_and_accept(tmp_path: Path) -> None:
    """Verify hypothesis gate and accept behavior."""
    ledger=HypothesisLedger(store(tmp_path)); h=ledger.create("parameter is unsigned","function","f1",origin="analyst")
    for i,(kind,group) in enumerate([("static","ghidra"),("dynamic","unicorn"),("compiler","msvc")]):
        ledger.attach_evidence(h.hypothesis_id,f"ev{i}",stance="supports",weight=.9,evidence_kind=kind,independence_group=group)
    ledger.transition(h.hypothesis_id,"scheduled",reason="ready")
    ledger.transition(h.hypothesis_id,"testing",reason="running")
    ledger.transition(h.hypothesis_id,"supported",reason="results agree")
    accepted=ledger.transition(h.hypothesis_id,"accepted",reason="gate passed",lock=True)
    assert accepted.state == "accepted" and accepted.locked


def test_hypothesis_contradiction_blocks_acceptance(tmp_path: Path) -> None:
    """Verify hypothesis contradiction blocks acceptance behavior."""
    ledger=HypothesisLedger(store(tmp_path)); h=ledger.create("x","function","f",origin="test")
    for i in range(3): ledger.attach_evidence(h.hypothesis_id,f"s{i}",stance="supports",weight=1,evidence_kind="static" if i<2 else "dynamic",independence_group=f"g{i}")
    ledger.attach_evidence(h.hypothesis_id,"bad",stance="contradicts",weight=1,evidence_kind="dynamic",independence_group="g4")
    assert not ledger.acceptance_gate(h.hypothesis_id)["passed"]


def test_hypothesis_dependency_cycle_rejected(tmp_path: Path) -> None:
    """Verify hypothesis dependency cycle rejected behavior."""
    ledger=HypothesisLedger(store(tmp_path)); a=ledger.create("a","x","1",origin="t"); b=ledger.create("b","x","2",origin="t")
    ledger.add_dependency(a.hypothesis_id,b.hypothesis_id)
    with pytest.raises(ContractError): ledger.add_dependency(b.hypothesis_id,a.hypothesis_id)


def test_campaign_lifecycle_and_planner(tmp_path: Path) -> None:
    """Verify campaign lifecycle and planner behavior."""
    s=store(tmp_path); api=CampaignEngine(s); c=api.create("behavioral_equivalence",budget={"actions":2}); api.start(c["campaign_id"])
    first=api.plan_next(c["campaign_id"])
    assert first["action"] == "inventory_unknowns"
    assert api.get(c["campaign_id"])["used"]["actions"] == 1
    api.pause(c["campaign_id"]); assert api.resume(c["campaign_id"])["status"] == "running"


def test_campaign_budget_blocks(tmp_path: Path) -> None:
    """Verify campaign budget blocks behavior."""
    api=CampaignEngine(store(tmp_path)); c=api.create("types_and_symbols",budget={"actions":0}); api.start(c["campaign_id"])
    with pytest.raises(ContractError): api.plan_next(c["campaign_id"])
    assert api.get(c["campaign_id"])["status"] == "blocked"


def test_campaign_branch(tmp_path: Path) -> None:
    """Verify campaign branch behavior."""
    api=CampaignEngine(store(tmp_path)); c=api.create("byte_identical")
    branch=api.branch(c["campaign_id"],"type-layout-a")
    assert branch["name"] == "type-layout-a"


def test_candidate_branch_compare_and_promotion(tmp_path: Path) -> None:
    """Verify candidate branch compare and promotion behavior."""
    api=CandidateStore(store(tmp_path)); source=tmp_path/"a.c"; source.write_text("int x;\n")
    a=api.create("main"); api.add_file(a,source,"src/a.c")
    b=api.create("variant",parent_candidate_id=a); source.write_text("unsigned x;\n"); api.add_file(b,source,"src/a.c")
    assert api.compare(a,b)["changed_files"][0]["change"] == "modified"
    api.record_evaluation(b,"dynamic","pass",value=1)
    assert api.transition(b,"promoted",reason="validated")["state"] == "promoted"


def test_candidate_rejects_traversal(tmp_path: Path) -> None:
    """Verify candidate rejects traversal behavior."""
    api=CandidateStore(store(tmp_path)); f=tmp_path/"x"; f.write_text("x"); c=api.create("main")
    with pytest.raises(ContractError): api.add_file(c,f,"../x")


def test_ddmin_and_counterexample_promotion(tmp_path: Path) -> None:
    """Verify ddmin and counterexample promotion behavior."""
    result, tests=ddmin_bytes(b"AAAAFAILBBBB",lambda b:b"FAIL" in b)
    assert result == b"FAIL" and tests > 0
    api=CounterexampleStore(store(tmp_path)); ident=api.add("function","f",b"AAAAFAILBBBB",predicate={"kind":"contains","value":"FAIL"})
    minimized=api.minimize(ident,lambda b:b"FAIL" in b)
    assert minimized["new_size"] == 4
    promoted=api.promote_to_regression(ident,tmp_path/"regressions")
    assert Path(promoted["fixture"]).read_bytes() == b"FAIL"


def test_consensus_conflict_and_resolution(tmp_path: Path) -> None:
    """Verify consensus conflict and resolution behavior."""
    api=ConsensusEngine(store(tmp_path))
    api.record("function","f","end",10,adapter_name="A",adapter_version="1",evidence_id="e1",independence_group="a")
    api.record("function","f","end",12,adapter_name="B",adapter_version="1",evidence_id="e2",independence_group="b")
    assert len(api.conflicts()) == 1
    api.resolve("function","f","end",10,method="analyst",rationale="exception metadata",lock=True)
    assert api.explain("function","f","end")["resolution"]["locked"] is True


def test_graph_impact(tmp_path: Path) -> None:
    """Verify graph impact behavior."""
    api=KnowledgeGraph(store(tmp_path)); api.upsert_node("type:T","type","T"); api.upsert_node("func:F","function","F"); api.add_edge("type:T","func:F","affects")
    report=api.impact("type:T")
    assert {n["node"]["node_id"] for n in report["nodes"]} == {"type:T","func:F"}


def test_review_lock_resists_automation(tmp_path: Path) -> None:
    """Verify review lock resists automation behavior."""
    api=ReviewQueue(store(tmp_path)); rid=api.create("conflict","f","resolve",priority=90)
    api.decide(rid,"accept","human reviewed",lock=True)
    with pytest.raises(ContractError): api.decide(rid,"reject","automation changed mind",actor="automation")


def test_family_correlation_is_bounded(tmp_path: Path) -> None:
    """Verify family correlation is bounded behavior."""
    api=BinaryFamilyStore(store(tmp_path)); fam=api.create("game")
    a=tmp_path/"a.bin"; b=tmp_path/"b.bin"; a.write_bytes(b"A"*64+b"B"*64); b.write_bytes(b"A"*64+b"C"*64)
    ma=api.add(fam["family_id"],"1.0",a); mb=api.add(fam["family_id"],"1.1",b)
    corr=api.correlate(ma["member_id"],mb["member_id"],block_size=64)
    assert corr["score"] == pytest.approx(1/3)
    assert "not function identity" in corr["details"]["interpretation"]

def test_remaining_public_list_snapshot_and_review_paths(tmp_path: Path) -> None:
    """Verify remaining public list snapshot and review paths behavior."""
    s=store(tmp_path)
    campaigns=CampaignEngine(s); c=campaigns.create("recover_function"); campaigns.start(c["campaign_id"])
    campaigns.plan_next(c["campaign_id"]); assert campaigns.snapshot(c["campaign_id"])["branches"][0]["name"] == "main"
    assert campaigns.list()[0]["campaign_id"] == c["campaign_id"]
    assert campaigns.stop(c["campaign_id"])["status"] == "stopped"
    candidates=CandidateStore(s); cid=candidates.create("main"); assert candidates.list()[0]["candidate_id"] == cid
    counterexamples=CounterexampleStore(s); xid=counterexamples.add("function","f",b"X",predicate={"kind":"always"}); assert counterexamples.list()[0]["counterexample_id"] == xid
    hypotheses=HypothesisLedger(s); hid=hypotheses.create("h","function","f",origin="test"); assert hypotheses.list()[0].hypothesis_id == hid.hypothesis_id
    reviews=ReviewQueue(s); rid=reviews.create("type","T","review type"); assert reviews.assign(rid,"alice")["assigned_to"] == "alice"; assert reviews.lock(rid)["locked"]; assert reviews.list()[0]["review_id"] == rid


def test_family_report_path(tmp_path: Path) -> None:
    """Verify family report path behavior."""
    api=BinaryFamilyStore(store(tmp_path)); fam=api.create("related"); f=tmp_path/"x"; f.write_bytes(b"x"); api.add(fam["family_id"],"one",f)
    report=api.report(fam["family_id"]); assert len(report["members"]) == 1 and report["non_claims"]
