"""Verify the current toolkit behavior covered by `tests/native/test_slots_matching.py`."""
from pathlib import Path

from pe_fixture import build_minimal_pe32
from x86decomp.native.matching import FunctionMatching, compare_function_bytes
from x86decomp.native.slots import FunctionSlots
from x86decomp.native.store import NativeStore


def test_slot_audit_classifies_exact_padding_and_overlap(tmp_path:Path)->None:
    """Verify slot audit classifies exact padding and overlap behavior."""
    store=NativeStore(tmp_path/'project'); api=FunctionSlots(store)
    result=api.audit([
        {'function_id':'a','rva':0x1000,'body_size':0x10},
        {'function_id':'b','rva':0x1010,'body_size':0x08},
        {'function_id':'c','rva':0x1020,'body_size':0x20},
        {'function_id':'d','rva':0x1030,'body_size':0x10},
    ],text_end_rva=0x1040)
    assert result['counts']=={'exact':2,'padded':1,'overlap':1}
    assert api.show('c')['findings'][0]['finding_kind']=='overlap'
    output=tmp_path/'fixes.json'; assert api.export_fixes(output)['fix_count']==1


def test_padding_comparison_is_tail_only_and_protected_aware()->None:
    """Verify padding comparison is tail only and protected aware behavior."""
    assert compare_function_bytes(b'\x55\xc3\xcc\xcc',b'\x55\xc3\x90\x90',policy='trailing-padding')['classification']=='padding-normalized'
    assert compare_function_bytes(b'\x55\xcc\xc3',b'\x55\x90\xc3',policy='trailing-padding')['classification']=='mismatch'
    assert compare_function_bytes(b'\x55\xc3\xcc',b'\x55\xc3\x90',policy='trailing-padding',protected_offsets=[2])['classification']=='mismatch'


def test_batch_matching_records_safe_and_fallback(tmp_path:Path)->None:
    """Verify batch matching records safe and fallback behavior."""
    pe=build_minimal_pe32(tmp_path/'target.exe',b'\x55\xc3\xcc\xcc\x90\x90')
    good=tmp_path/'good.bin'; good.write_bytes(b'\x55\xc3\x90\x90')
    bad=tmp_path/'bad.bin'; bad.write_bytes(b'\x55\x55')
    api=FunctionMatching(NativeStore(tmp_path/'project'))
    report=api.batch(pe,[
        {'function_id':'good','rva':0x1000,'slot_size':4,'candidate_path':str(good)},
        {'function_id':'bad','rva':0x1004,'slot_size':2,'candidate_path':str(bad)},
    ])
    assert report['summary']['safe']==1 and report['summary']['fallback']==1
    assert len(api.mismatches(report['run_id']))==1


def test_short_candidate_requires_padding_only_remainder(tmp_path:Path)->None:
    """Verify short candidate requires padding only remainder behavior."""
    pe=build_minimal_pe32(tmp_path/'target.exe',b'\x55\xc3\x01\x02')
    short=tmp_path/'short.bin'; short.write_bytes(b'\x55\xc3')
    report=FunctionMatching(NativeStore(tmp_path/'project')).batch(pe,[
        {'function_id':'truncated','rva':0x1000,'slot_size':4,'candidate_path':str(short)},
    ])
    item=report['functions'][0]
    assert item['classification']=='truncated-nonpadding'
    assert not item['replacement_safe'] and not item['slot_remainder_is_padding']
