"""Provide x86decomp.native.cli functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import argparse
import json
import sys
import subprocess
from pathlib import Path
from typing import Any

from x86decomp.contracts import ContractError
from .closed_loop import ClosedLoop
from .hybrid_composer import HybridComposer
from .matching import FunctionMatching, compare_function_bytes
from .pe_reconstruction import PEReconstruction
from .runtime import RuntimeValidation
from .slots import FunctionSlots
from .staging import StagingBridge
from .store import NativeStore
from .windows_tools import WindowsTools, discover_ghidra_launcher, write_response_file


def _json(raw: str | None, default: Any) -> Any:
    """Implement json.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if raw is None: return default
    try: return json.loads(raw)
    except json.JSONDecodeError as exc: raise ContractError(f"invalid JSON argument: {exc}") from exc


def _json_file(path: str) -> Any:
    """Implement json file.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _emit(value: Any) -> None:
    """Emit the requested operation.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if hasattr(value, "__dict__"): value = value.__dict__
    print(json.dumps(value, indent=2, sort_keys=True, default=str))


def build_parser(*, prog: str = "x86decomp-native") -> argparse.ArgumentParser:
    """Build parser.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    parser=argparse.ArgumentParser(prog=prog,description='x86decomp-toolkit 0.7.9 native PE reconstruction and closed-loop matching')
    parser.add_argument('--project',default='.',help='project root containing the additive SQLite state')
    parser.add_argument('--actor',default='analyst')
    sub=parser.add_subparsers(dest='group',required=True)

    project=sub.add_parser('project'); ps=project.add_subparsers(dest='action',required=True); ps.add_parser('init'); ps.add_parser('check')

    boundary=sub.add_parser('boundary'); bs=boundary.add_subparsers(dest='action',required=True)
    q=bs.add_parser('audit'); q.add_argument('inventory_json'); q.add_argument('--text-end-rva')
    q=bs.add_parser('audit-project'); q.add_argument('artifact_project'); q.add_argument('binary')
    q=bs.add_parser('list'); q.add_argument('--classification')
    q=bs.add_parser('show'); q.add_argument('function_id')
    q=bs.add_parser('export-ghidra-fixes'); q.add_argument('output')

    match=sub.add_parser('match'); ms=match.add_subparsers(dest='action',required=True)
    q=ms.add_parser('compare'); q.add_argument('original'); q.add_argument('candidate'); q.add_argument('--policy',default='trailing-padding',choices=['exact','trailing-padding']); q.add_argument('--pad-bytes-json'); q.add_argument('--protected-offsets-json')
    q=ms.add_parser('batch'); q.add_argument('original'); q.add_argument('candidates_json'); q.add_argument('--policy',default='trailing-padding',choices=['exact','trailing-padding']); q.add_argument('--pad-bytes-json')
    q=ms.add_parser('report'); q.add_argument('run_id')
    q=ms.add_parser('mismatches'); q.add_argument('run_id')

    hybrid=sub.add_parser('hybrid'); hs=hybrid.add_subparsers(dest='action',required=True)
    q=hs.add_parser('compose'); q.add_argument('run_id'); q.add_argument('output')
    q=hs.add_parser('verify'); q.add_argument('composition_id')

    pe=sub.add_parser('pe'); pes=pe.add_subparsers(dest='action',required=True)
    q=pes.add_parser('inventory'); q.add_argument('image')
    q=pes.add_parser('export-sections'); q.add_argument('image'); q.add_argument('output'); q.add_argument('--section',action='append')
    q=pes.add_parser('export-coff'); q.add_argument('image'); q.add_argument('output'); q.add_argument('--section',action='append')
    q=pes.add_parser('patch-plan'); q.add_argument('original'); q.add_argument('output'); q.add_argument('operations_json')
    q=pes.add_parser('patch-apply'); q.add_argument('plan_id')
    q=pes.add_parser('text-swap'); q.add_argument('original'); q.add_argument('replacement'); q.add_argument('output'); q.add_argument('--section-name',default='.text')

    staging=sub.add_parser('staging'); ss=staging.add_subparsers(dest='action',required=True)
    q=ss.add_parser('scan'); q.add_argument('sources',nargs='+')
    q=ss.add_parser('generate-context'); q.add_argument('output'); q.add_argument('sources',nargs='+')
    q=ss.add_parser('resolve'); q.add_argument('mapping_json')
    ss.add_parser('unresolved')
    q=ss.add_parser('compile-check'); q.add_argument('command_json'); q.add_argument('--cwd'); q.add_argument('--timeout',type=int,default=120)

    loop=sub.add_parser('loop'); ls=loop.add_subparsers(dest='action',required=True)
    q=ls.add_parser('run'); q.add_argument('function_id'); q.add_argument('source'); q.add_argument('compile_command_json'); q.add_argument('candidate'); q.add_argument('original'); q.add_argument('rva'); q.add_argument('slot_size',type=int); q.add_argument('--symbol'); q.add_argument('--policy',default='trailing-padding'); q.add_argument('--timeout',type=int,default=120); q.add_argument('--execute',action='store_true')
    q=ls.add_parser('show'); q.add_argument('loop_id')
    ls.add_parser('list')

    runtime=sub.add_parser('runtime'); rs=runtime.add_subparsers(dest='action',required=True)
    q=rs.add_parser('validate-image'); q.add_argument('image')
    q=rs.add_parser('launch'); q.add_argument('image'); q.add_argument('--argument',action='append',default=[]); q.add_argument('--timeout',type=int,default=10); q.add_argument('--execute',action='store_true')
    q=rs.add_parser('map-crash'); q.add_argument('rva')

    windows=sub.add_parser('windows'); ws=windows.add_subparsers(dest='action',required=True)
    q=ws.add_parser('doctor'); q.add_argument('--ghidra-home')
    q=ws.add_parser('discover-ghidra'); q.add_argument('--ghidra-home'); q.add_argument('--platform-name')
    q=ws.add_parser('response-file'); q.add_argument('output'); q.add_argument('arguments_json')
    return parser


def dispatch(args:argparse.Namespace)->Any:
    """Dispatch the requested operation.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    store=NativeStore(args.project); actor=args.actor
    if args.group=='project':
        if args.action=='init': store.initialize()
        return store.check()
    if args.group=='boundary':
        api=FunctionSlots(store)
        if args.action=='audit': return api.audit(_json_file(args.inventory_json),text_end_rva=None if args.text_end_rva is None else int(args.text_end_rva,0),actor=actor)
        if args.action=='audit-project': return api.audit_project(Path(args.artifact_project),Path(args.binary),actor=actor)
        if args.action=='list': return api.list(classification=args.classification)
        if args.action=='show': return api.show(args.function_id)
        return api.export_fixes(Path(args.output))
    if args.group=='match':
        if args.action=='compare': return compare_function_bytes(Path(args.original).read_bytes(),Path(args.candidate).read_bytes(),policy=args.policy,pad_bytes=_json(args.pad_bytes_json,[0,144,204]),protected_offsets=_json(args.protected_offsets_json,[]))
        api=FunctionMatching(store)
        if args.action=='batch': return api.batch(Path(args.original),_json_file(args.candidates_json),policy=args.policy,pad_bytes=_json(args.pad_bytes_json,[0,144,204]),actor=actor)
        if args.action=='report': return api.report(args.run_id)
        return api.mismatches(args.run_id)
    if args.group=='hybrid':
        api=HybridComposer(store)
        return api.compose(args.run_id,Path(args.output),actor=actor) if args.action=='compose' else api.verify(args.composition_id)
    if args.group=='pe':
        api=PEReconstruction(store)
        if args.action=='inventory': return api.inventory(Path(args.image))
        if args.action=='export-sections': return api.export_sections(Path(args.image),Path(args.output),names=args.section)
        if args.action=='export-coff': return api.export_coff(Path(args.image),Path(args.output),names=args.section)
        if args.action=='patch-plan': return api.create_plan(Path(args.original),Path(args.output),_json_file(args.operations_json),actor=actor)
        if args.action=='patch-apply': return api.apply_plan(args.plan_id,actor=actor)
        return api.text_swap(Path(args.original),Path(args.replacement),Path(args.output),section_name=args.section_name,actor=actor)
    if args.group=='staging':
        api=StagingBridge(store)
        if args.action=='scan': return api.scan([Path(item) for item in args.sources])
        if args.action=='generate-context': return api.generate_context([Path(item) for item in args.sources],Path(args.output),actor=actor)
        if args.action=='resolve': return api.resolve(_json_file(args.mapping_json),actor=actor)
        if args.action=='unresolved': return api.unresolved()
        return api.compile_check(_json(args.command_json,[]),cwd=None if args.cwd is None else Path(args.cwd),timeout_seconds=args.timeout)
    if args.group=='loop':
        api=ClosedLoop(store)
        if args.action=='run': return api.run(args.function_id,Path(args.source),_json(args.compile_command_json,[]),Path(args.candidate),Path(args.original),int(args.rva,0),args.slot_size,symbol=args.symbol,policy=args.policy,execute=args.execute,timeout_seconds=args.timeout,actor=actor)
        if args.action=='show': return api.show(args.loop_id)
        return api.list()
    if args.group=='runtime':
        api=RuntimeValidation(store)
        if args.action=='validate-image': return api.validate_image(Path(args.image),actor=actor)
        if args.action=='launch': return api.launch(Path(args.image),execute=args.execute,timeout_seconds=args.timeout,arguments=args.argument,actor=actor)
        return api.map_crash(int(args.rva,0))
    if args.group=='windows':
        if args.action=='doctor': return WindowsTools(store).doctor(ghidra_home=None if args.ghidra_home is None else Path(args.ghidra_home),actor=actor)
        if args.action=='discover-ghidra':
            path=discover_ghidra_launcher(None if args.ghidra_home is None else Path(args.ghidra_home),platform_name=args.platform_name); return {'path':None if path is None else str(path)}
        return write_response_file(Path(args.output),_json(args.arguments_json,[]))
    raise ContractError('unhandled native command')


def main(argv:list[str]|None=None)->int:
    """Run the command-line entry point.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    try:
        args=build_parser().parse_args(argv); _emit(dispatch(args)); return 0
    except (ContractError,KeyError,OSError,ValueError,subprocess.SubprocessError) as exc:
        print(json.dumps({'error':type(exc).__name__,'message':str(exc)},sort_keys=True),file=sys.stderr); return 2


if __name__=='__main__': raise SystemExit(main())
