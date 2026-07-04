from __future__ import annotations

import json
import os
from pathlib import Path

import pytest

from x86decomp.governance.changesets import ChangeSet
from x86decomp.contracts import ContractError
from x86decomp.governance.plugins import PluginRegistry
from x86decomp.governance.proofs import ProofBundle, ProofLedger
from x86decomp.governance.store import GovernanceStore
from x86decomp.governance.workers import WorkerRegistry


def test_proof_ledger_and_bundle(tmp_path: Path) -> None:
    store=GovernanceStore(tmp_path/"p"); ledger=ProofLedger(store)
    obligation=ledger.create_obligation("function","f","declared behavior","behaviorally_tested",assumptions=["bounded inputs"])
    ledger.add_result(obligation["obligation_id"],"behaviorally_tested","unicorn",{"cases":10,"universal_equivalence":False})
    assert ledger.evaluate(obligation["obligation_id"])["passed"]
    artifact=store.project_root/"reports"/"r.json"; artifact.parent.mkdir(parents=True); artifact.write_text("{}")
    bundle=tmp_path/"proof.xdp"; exported=ProofBundle.export(store,bundle,include_paths=[artifact],hmac_key=b"secret")
    assert exported["files"] >= 3
    assert ProofBundle.verify(bundle,hmac_key=b"secret")["passed"]
    assert not ProofBundle.verify(bundle,hmac_key=b"wrong")["passed"]


def test_proof_bundle_rejects_outside_artifact(tmp_path: Path) -> None:
    store=GovernanceStore(tmp_path/"p"); store.initialize(); outside=tmp_path/"outside"; outside.write_text("x")
    with pytest.raises(ContractError): ProofBundle.export(store,tmp_path/"x.zip",include_paths=[outside])


def _plugin(tmp_path: Path) -> tuple[Path,Path]:
    executable=tmp_path/"plugin.py"
    executable.write_text("#!/usr/bin/env python3\nimport json,sys\nr=json.load(sys.stdin)\nprint(json.dumps({'api_version':'1','result':{'capability':r['capability'],'ok':True}}))\n")
    executable.chmod(0o755)
    manifest=tmp_path/"plugin.json"; manifest.write_text(json.dumps({"name":"demo","version":"1.0","api_version":"1","executable":str(executable),"capabilities":["analyze"]}))
    return executable,manifest


def test_plugin_install_doctor_invoke(tmp_path: Path) -> None:
    executable,manifest=_plugin(tmp_path); api=PluginRegistry(GovernanceStore(tmp_path/"p")); plugin=api.install(manifest)
    assert api.doctor(plugin["plugin_id"])["passed"]
    assert api.invoke(plugin["plugin_id"],"analyze",{"x":1})["result"]["ok"]
    executable.write_text("changed")
    assert not api.doctor(plugin["plugin_id"])["passed"]


def test_plugin_rejects_undeclared_capability(tmp_path: Path) -> None:
    _,manifest=_plugin(tmp_path); api=PluginRegistry(GovernanceStore(tmp_path/"p")); plugin=api.install(manifest)
    with pytest.raises(ContractError): api.invoke(plugin["plugin_id"],"compile",{})


def test_worker_registry_selection_and_doctor(tmp_path: Path) -> None:
    api=WorkerRegistry(GovernanceStore(tmp_path/"p")); worker=api.register("linux",{"tools":["angr","clang"],"arch":"x86"},endpoint="https://worker.example",environment_sha256="a"*64)
    assert api.doctor(worker["worker_id"])["passed"]
    assert api.select({"arch":"x86","tools":["angr"]})["worker_id"] == worker["worker_id"]
    assert api.set_status(worker["worker_id"],"draining")["status"] == "draining"


def test_changeset_round_trip(tmp_path: Path) -> None:
    source=GovernanceStore(tmp_path/"a"); source.initialize(); source.audit("a","created","x",{"v":1})
    archive=tmp_path/"change.zip"; exported=ChangeSet.export(source,archive)
    assert exported["event_count"] == 1
    target=GovernanceStore(tmp_path/"b"); target.initialize(); applied=ChangeSet.apply(target,archive)
    assert applied["events"] == 1 and target.verify_audit_chain()["valid"]


def test_changeset_base_mismatch(tmp_path: Path) -> None:
    source=GovernanceStore(tmp_path/"a"); source.initialize(); source.audit("a","created","x",{})
    archive=tmp_path/"change.zip"; ChangeSet.export(source,archive)
    target=GovernanceStore(tmp_path/"b"); target.initialize(); target.audit("other","event",None,{})
    with pytest.raises(ContractError): ChangeSet.apply(target,archive)

def test_plugin_list_and_proof_inspect(tmp_path: Path) -> None:
    _,manifest=_plugin(tmp_path); api=PluginRegistry(GovernanceStore(tmp_path/"p")); api.install(manifest); assert len(api.list()) == 1
    bundle=tmp_path/"p.zip"; store=GovernanceStore(tmp_path/"q"); store.initialize(); ProofBundle.export(store,bundle)
    assert ProofBundle.inspect(bundle)["passed"]
