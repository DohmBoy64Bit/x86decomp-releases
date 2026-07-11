"""Verify the current toolkit behavior covered by `tests/native/test_pe_hybrid.py`."""
from pathlib import Path

from pe_fixture import build_minimal_pe32, build_minimal_pe64
from x86decomp.pe import parse_pe
from x86decomp.native.hybrid_composer import HybridComposer
from x86decomp.native.matching import FunctionMatching
from x86decomp.native.pe_reconstruction import PEReconstruction, apply_operations, plan_patch
from x86decomp.native.store import NativeStore


def test_safe_patch_and_text_swap_preserve_pe_container(tmp_path:Path)->None:
    """Verify safe patch and text swap preserve pe container behavior."""
    original=build_minimal_pe32(tmp_path/'original.exe',b'\x55\xc3\xcc\xcc')
    store=NativeStore(tmp_path/'project'); api=PEReconstruction(store)
    replacement=tmp_path/'text.bin'; replacement.write_bytes(b'\x31\xc0\xc3')
    output=tmp_path/'swapped.exe'; result=api.text_swap(original,replacement,output)
    assert result['size_preserved'] and result['virtual_size_preserved'] and result['raw_size_preserved']
    assert parse_pe(output).entry_rva==0x1000
    original_bytes=original.read_bytes(); operations=[{'offset':0x200,'expected_hex':original_bytes[0x200:0x202].hex(),'replacement_hex':'9090'}]
    assert apply_operations(original_bytes,plan_patch(original_bytes,operations))[0x200:0x202]==b'\x90\x90'


def test_section_export_and_synthetic_coff_for_pe32_and_pe64(tmp_path:Path)->None:
    """Verify section export and synthetic coff for pe32 and pe64 behavior."""
    for name,builder in [('x86',build_minimal_pe32),('x64',build_minimal_pe64)]:
        image=builder(tmp_path/f'{name}.exe'); api=PEReconstruction(NativeStore(tmp_path/f'p-{name}'))
        exported=api.export_sections(image,tmp_path/f'sections-{name}'); assert exported['sections'][0]['name']=='.text'
        coff=api.export_coff(image,tmp_path/f'coff-{name}',names=['.text']); assert len(coff['objects'])==1


def test_hybrid_composer_promotes_only_verified_candidates(tmp_path:Path)->None:
    """Verify hybrid composer promotes only verified candidates behavior."""
    original=build_minimal_pe32(tmp_path/'original.exe',b'\x55\xc3\xcc\xcc\x90\x90')
    good=tmp_path/'good.bin'; good.write_bytes(b'\x55\xc3\x90\x90')
    bad=tmp_path/'bad.bin'; bad.write_bytes(b'\x55\x55')
    store=NativeStore(tmp_path/'project')
    match=FunctionMatching(store).batch(
        original,
        [
            {'function_id':'good','rva':0x1000,'slot_size':4,'candidate_path':str(good)},
            {'function_id':'bad','rva':0x1004,'slot_size':2,'candidate_path':str(bad)},
        ],
    )
    result=HybridComposer(store).compose(match['run_id'],tmp_path/'hybrid.exe')
    assert result['promoted_count']==1 and result['fallback_count']==1 and result['container_size_preserved']
    payload=(tmp_path/'hybrid.exe').read_bytes(); assert payload[0x200:0x204]==good.read_bytes(); assert payload[0x204:0x206]==original.read_bytes()[0x204:0x206]


def test_hybrid_composer_rejects_candidate_changed_after_match(tmp_path:Path)->None:
    """Verify hybrid composer rejects candidate changed after match behavior."""
    from x86decomp.contracts import ContractError
    import pytest
    original=build_minimal_pe32(tmp_path/'original.exe',b'\x55\xc3')
    candidate=tmp_path/'candidate.bin'; candidate.write_bytes(b'\x55\xc3')
    store=NativeStore(tmp_path/'project')
    run=FunctionMatching(store).batch(original,[
        {'function_id':'entry','rva':0x1000,'slot_size':2,'candidate_path':str(candidate)},
    ])
    candidate.write_bytes(b'\x90\x90')
    with pytest.raises(ContractError,match='candidate changed'):
        HybridComposer(store).compose(run['run_id'],tmp_path/'hybrid.exe')
