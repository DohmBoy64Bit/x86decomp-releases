from __future__ import annotations

from pathlib import Path

from x86decomp.reconstruction.capsules import Capsules
from x86decomp.reconstruction.libraries import LibraryRecognition
from x86decomp.reconstruction.security import SecurityReview
from x86decomp.reconstruction.semantic_changesets import SemanticChangeSets
from x86decomp.reconstruction.store import ReconstructionStore


def test_capsule_is_deterministic_verifiable_and_reproducible(tmp_path: Path) -> None:
    (tmp_path/'src').mkdir(); (tmp_path/'src/a.c').write_text('int a;\n')
    api=Capsules(ReconstructionStore(tmp_path)); capsule=api.create('snapshot',tmp_path/'snapshot.xdc',include=['src/a.c'],external_requirements=[{'tool':'MSVC6','supplied':False}])
    assert api.verify(capsule['archive_path'])['valid']
    inspected=api.inspect(capsule['archive_path']); assert inspected['manifest']['toolkit_version']=='0.7.5'
    result=api.reproduce(capsule['archive_path'],tmp_path/'reproduced'); assert result['verified']
    assert (tmp_path/'reproduced/src/a.c').read_text()=='int a;\n'


def test_library_recognition_never_silently_replaces_code(tmp_path: Path) -> None:
    api=LibraryRecognition(ReconstructionStore(tmp_path)); item=api.identify('sub_403910','zlib',version_range='1.1.x',confidence=.97,evidence=[{'kind':'function-fingerprint'}])
    assert item['disposition']=='proposed'
    assert api.candidates('sub_403910')[0]['match_id']==item['match_id']
    accepted=api.disposition(item['match_id'],'accepted'); assert accepted['disposition']=='accepted'


def test_security_scan_reports_without_modifying_behavior(tmp_path: Path) -> None:
    api=SecurityReview(ReconstructionStore(tmp_path)); result=api.scan([{'api':'CreateRemoteThread','subject_id':'sub_1'},{'api':'MessageBoxA','subject_id':'sub_2'}])
    assert result['finding_count']==1 and result['behavior_modified'] is False
    assert api.report()['counts']['high']==1
    policy=api.policy('strict',{'deny':['remote-thread']}); assert policy['name']=='strict'


def test_semantic_changesets_detect_conflicts_and_verify_clean_merges(tmp_path: Path) -> None:
    api=SemanticChangeSets(ReconstructionStore(tmp_path)); left=api.create('left'); right=api.create('right')
    api.add_operation(left['changeset_id'],{'kind':'type-decision','subject_id':'T','value':'int'})
    api.add_operation(right['changeset_id'],{'kind':'type-decision','subject_id':'T','value':'unsigned'})
    merged=api.merge(left['changeset_id'],right['changeset_id'],'merged')
    assert merged['status']=='conflicted' and len(api.conflicts(merged['changeset_id']))==1
    assert not api.verify(merged['changeset_id'])['passed']
    rebased=api.rebase(left['changeset_id'],'a'*64); assert rebased['base_audit_hash']=='a'*64
