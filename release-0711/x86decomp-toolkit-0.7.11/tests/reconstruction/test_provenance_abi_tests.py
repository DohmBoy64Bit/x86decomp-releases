"""Verify the current toolkit behavior covered by `tests/reconstruction/test_provenance_abi_tests.py`."""
from __future__ import annotations

from pathlib import Path
import hashlib
import pytest

from x86decomp.contracts import ContractError
from x86decomp.governance.counterexamples import CounterexampleStore
from x86decomp.reconstruction.abi_contracts import ABIContracts
from x86decomp.reconstruction.generated_tests import GeneratedTests
from x86decomp.reconstruction.provenance import ProvenanceLedger
from x86decomp.reconstruction.store import ReconstructionStore


def test_provenance_round_trip_edit_reconciliation_and_locks(tmp_path: Path) -> None:
    """Verify provenance round trip edit reconciliation and locks behavior."""
    source=tmp_path/'src/unit.c'; source.parent.mkdir(); source.write_text('int f(void){return 1;}\n')
    store=ReconstructionStore(tmp_path); api=ProvenanceLedger(store)
    record=api.record('src/unit.c',1,1,'target.exe','0x401000','0x40100f',evidence=[{'kind':'static-dataflow'}],confidence=.9)
    assert api.source('src/unit.c',1)[0]['provenance_id']==record['provenance_id']
    assert api.binary('target.exe','0x401005')[0]['source_path']=='src/unit.c'
    api.lock('src/unit.c',reason='analyst review')
    with pytest.raises(ContractError): api.reconcile('src/unit.c')
    api.unlock('src/unit.c')
    before=hashlib.sha256(source.read_bytes()).hexdigest(); source.write_text('int f(void){return 2;}\n')
    edit=api.reconcile('src/unit.c',before_sha256=before)
    assert edit['semantic'] and edit['affected']==['target.exe:0x401000-0x40100f']
    assert api.impact('src/unit.c')['proofs_must_be_revalidated']
    assert Path(api.export(tmp_path/'prov.json')['path']).is_file()


def test_abi_contract_verification_comparison_and_explicit_shim(tmp_path: Path) -> None:
    """Verify abi contract verification comparison and explicit shim behavior."""
    api=ABIContracts(ReconstructionStore(tmp_path))
    contract={'calling_convention':'cdecl','parameters':[{'type':'int'}],'return_type':'int','stack_cleanup':'caller'}
    left=api.recover('function','f','x86',contract,evidence=[{'kind':'callsite-width'}])
    right=api.recover('function','g','x86',{**contract,'return_type':'unsigned int'},evidence=[{'kind':'dynamic-trace'}])
    assert api.verify(left['contract_id'])['passed']
    assert not api.compare(left['contract_id'],right['contract_id'])['compatible']
    shim=api.shim(left['contract_id'],'src/shims/f.c',shim_kind='wrapped')
    assert shim['shim_kind']=='wrapped'
    assert Path(api.export(left['contract_id'],tmp_path/'abi.json')['path']).is_file()


def test_generated_tests_are_evidence_bound_and_counterexamples_promote(tmp_path: Path) -> None:
    """Verify generated tests are evidence bound and counterexamples promote behavior."""
    store=ReconstructionStore(tmp_path); api=GeneratedTests(store)
    item=api.synthesize('function','sub_401000')
    assert (tmp_path/item['relative_path']).is_file()
    assert api.explain(item['generated_test_id'])['protects']=='function:sub_401000'
    counterexample_id=CounterexampleStore(store).add('function','sub_401000',b'failure',predicate={'kind':'mismatch'})
    promoted=api.promote_counterexample(counterexample_id)
    assert promoted in api.list()
    assert promoted['evidence'][0]['kind']=='governance-counterexample'
    with pytest.raises(KeyError): api.promote_counterexample('missing-counterexample')
    with pytest.raises(ContractError):
        api.add('bad','function','f','unit','tests/generated/test_bad.py','def test_x(): pass\n',applicability={},evidence=[])
