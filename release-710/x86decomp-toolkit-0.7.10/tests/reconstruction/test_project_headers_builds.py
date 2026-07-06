"""Verify the current toolkit behavior covered by `tests/reconstruction/test_project_headers_builds.py`."""
from __future__ import annotations

from pathlib import Path
import pytest

from x86decomp.contracts import ContractError
from x86decomp.reconstruction.builds import BuildManager
from x86decomp.reconstruction.headers import HeaderManager
from x86decomp.reconstruction.project_layout import ProjectLayout
from x86decomp.reconstruction.store import ReconstructionStore


def test_store_is_additive_and_layout_is_evidence_labeled(tmp_path: Path) -> None:
    """Verify store is additive and layout is evidence labeled behavior."""
    store=ReconstructionStore(tmp_path); check=store.check()
    assert check['passed'] and check['schema_extension_version']==4 and check['reconstruction_schema_extension_version']==5
    layout=ProjectLayout(store)
    result=layout.synthesize([
        {'id':'f1','kind':'function','object_file':'renderer.obj'},
        {'id':'f2','kind':'function','object_file':'renderer.obj'},
        {'id':'f3','kind':'function'},
    ])
    assert result['input_count']==3 and result['unknown_group_present']
    assert len(result['modules'])==2
    explained=layout.explain_boundaries(result['modules'][0]['module_id'])
    assert 'not original-source attribution' in explained['claim']
    unit=layout.create_translation_unit('src/renderer.cpp',module_id=result['modules'][0]['module_id'],evidence=[{'kind':'object-order'}])
    unit=layout.add_translation_unit_member(unit['unit_id'],'function','f1',linkage='external')
    assert unit['members'][0]['member_id']=='f1'
    exported=layout.export(tmp_path/'layout.json'); assert Path(exported['path']).is_file()


def test_headers_reject_cycles_and_generate_compileable_shape(tmp_path: Path) -> None:
    """Verify headers reject cycles and generate compileable shape behavior."""
    api=HeaderManager(ReconstructionStore(tmp_path))
    a=api.create('include/a.h',visibility='public'); b=api.create('include/b.h')
    api.declare(a['header_id'],'foo','int foo(void);',evidence=[{'kind':'callsite'}])
    api.include(a['header_id'],b['header_id'],reason='type dependency')
    with pytest.raises(ContractError): api.include(b['header_id'],a['header_id'],reason='would cycle')
    assert api.cycles()==[]
    generated=api.synthesize(a['header_id'],output_root=tmp_path)
    text=Path(generated['written_to']).read_text()
    assert '#include "include/b.h"' in text and 'int foo(void);' in text
    assert api.validate(a['header_id'])['passed']


def test_historical_and_portable_build_modes_remain_distinct(tmp_path: Path) -> None:
    """Verify historical and portable build modes remain distinct behavior."""
    (tmp_path/'src').mkdir(); (tmp_path/'src/main.c').write_text('int main(void){return 0;}\n')
    api=BuildManager(ReconstructionStore(tmp_path))
    historical=api.create('historical',mode='historical',generator='response-file')
    ht=api.add_target(historical['build_id'],'app',sources=['src/main.c'])
    hv=api.add_variant(ht['target_id'],'release',compiler='cl.exe 12.00',linker='link.exe 6.00')
    assert api.validate(ht['target_id'],hv['variant_id'])['status']=='passed'
    portable=api.create('portable',mode='portable',generator='cmake')
    pt=api.add_target(portable['build_id'],'app',sources=['src/main.c'])
    api.add_variant(pt['target_id'],'release',compiler='clang',linker='lld-link')
    generated=api.generate(portable['build_id'],output_root=tmp_path/'portable')
    assert Path(generated['path']).name=='CMakeLists.txt'
    comparison=api.compare_modes(historical['build_id'],portable['build_id'])
    assert comparison['claims_separated'] and comparison['shared_targets']==['app']
    assert 'app' in api.matrix()['matrix']
