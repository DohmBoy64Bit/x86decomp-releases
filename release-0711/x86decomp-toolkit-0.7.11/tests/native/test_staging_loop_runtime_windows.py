"""Verify the current toolkit behavior covered by `tests/native/test_staging_loop_runtime_windows.py`."""
import json
import sys
from pathlib import Path

import pytest

from pe_fixture import build_minimal_pe32
from x86decomp.contracts import ContractError
from x86decomp.native.closed_loop import ClosedLoop
from x86decomp.native.runtime import RuntimeValidation
from x86decomp.native.staging import StagingBridge
from x86decomp.native.store import NativeStore
from x86decomp.native.windows_tools import discover_ghidra_launcher, write_response_file


def test_staging_context_resolution_and_compile_check(tmp_path:Path)->None:
    """Verify staging context resolution and compile check behavior."""
    source=tmp_path/'ghidra.c'; source.write_text('undefined4 FUN_401000(void){ return DAT_402000; }')
    api=StagingBridge(NativeStore(tmp_path/'project')); result=api.generate_context([source],tmp_path/'context.h')
    assert result['output']==str((tmp_path/'context.h').resolve()) and result['sha256']
    assert 'typedef uint32_t undefined4;' in (tmp_path/'context.h').read_text()
    assert len(api.unresolved())==2
    mapping=tmp_path/'map.json'; mapping.write_text(json.dumps({'FUN_401000':'extern uint32_t FUN_401000(void);','DAT_402000':'extern uint32_t DAT_402000;'}))
    assert api.resolve(json.loads(mapping.read_text()))['count']==2 and api.unresolved()==[]
    assert api.compile_check([sys.executable,'-c','print(1)'])['passed']


def test_closed_loop_requires_consent_and_records_verified_result(tmp_path:Path)->None:
    """Verify closed loop requires consent and records verified result behavior."""
    original=build_minimal_pe32(tmp_path/'target.exe',b'\x55\xc3')
    source=tmp_path/'source.c'; source.write_text('int f(void){return 0;}')
    candidate=tmp_path/'candidate.bin'; command=[sys.executable,'-c',f"from pathlib import Path; Path(r'{candidate}').write_bytes(bytes.fromhex('55c3'))"]
    api=ClosedLoop(NativeStore(tmp_path/'project'))
    with pytest.raises(ContractError): api.run('f',source,command,candidate,original,0x1000,2)
    result=api.run('f',source,command,candidate,original,0x1000,2,execute=True)
    assert result['status']=='verified' and api.show(result['loop_id'])['status']=='verified'


def test_runtime_static_validation_and_crash_mapping(tmp_path:Path)->None:
    """Verify runtime static validation and crash mapping behavior."""
    image=build_minimal_pe32(tmp_path/'target.exe')
    store=NativeStore(tmp_path/'project')
    from x86decomp.native.slots import FunctionSlots
    FunctionSlots(store).audit([{'function_id':'entry','rva':0x1000,'body_size':7}],text_end_rva=0x1010)
    api=RuntimeValidation(store); result=api.validate_image(image)
    assert result['checks']['entry_point_mapped'] and api.map_crash(0x1002)['function_id']=='entry'
    with pytest.raises(ContractError): api.launch(image)


def test_windows_launcher_prefers_batch_on_windows_and_response_files(tmp_path:Path)->None:
    """Verify windows launcher prefers batch on windows and response files behavior."""
    home=tmp_path/'Ghidra'; support=home/'support'; support.mkdir(parents=True)
    (support/'analyzeHeadless').write_text('unix'); (support/'analyzeHeadless.bat').write_text('windows')
    assert discover_ghidra_launcher(home,platform_name='nt').name=='analyzeHeadless.bat'
    assert discover_ghidra_launcher(home,platform_name='posix').name=='analyzeHeadless'
    result=write_response_file(tmp_path/'args.rsp',['a','path with spaces'])
    assert result['argument_count']==2 and '"path with spaces"' in (tmp_path/'args.rsp').read_text()
