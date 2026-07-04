from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from x86decomp.contracts import ContractError
from x86decomp.local_llm import (
    create_profile as create_llm_profile,
    generate_candidate as generate_llm_candidate,
    load_job as load_llm_job,
    load_profile as load_llm_profile,
    probe_profile as probe_llm_profile,
    prompt_record as llm_prompt_record,
    provider_catalog as llm_provider_catalog,
    run_match_loop as run_llm_match_loop,
    verify_match_report as verify_llm_match_report,
)
from x86decomp.local_llm.profiles import public_profile as public_llm_profile
from x86decomp.util import write_json
from .abi_contracts import ABIContracts
from .builds import BuildManager
from .capsules import Capsules
from .generated_tests import GeneratedTests
from .headers import HeaderManager
from .libraries import LibraryRecognition
from .project_layout import ProjectLayout
from .provenance import ProvenanceLedger
from .security import SecurityReview
from .semantic_changesets import SemanticChangeSets
from .acceleration import (
    llm_job_from_function_packet, llm_job_from_range, llm_batch_create, llm_batch_match,
    candidate_promote, source_map_annotate, source_map_verify, module_assign, module_suggest,
    type_propagate, header_synthesize_project, vtable_recover, class_scaffold, diff_explain,
    triage_next, playability_smoke_plan, asset_inventory, mod_branch_init, regression_compare,
    function_discover, function_boundary_reconcile, function_list_sort, function_list_classify,
    pattern_catalog, pattern_scan, pattern_generate, pattern_match, pattern_promote,
    image_text_compose, text_swap_plan, text_swap_build, text_swap_inject, text_swap_verify,
    progress_reconcile, project_health, source_stage_classify,
    ghidra_mcp_probe, ghidra_mcp_functions, ghidra_mcp_decompile, ghidra_mcp_batch_decompile, ghidra_mcp_sync_names,
    compiler_rule_learn, compiler_rule_report, compiler_compare_flags,
    runtime_identify, runtime_quarantine, runtime_match_library, subsystem_detect, state_machine_detect,
    project_doctor_paths, script_port_audit, toolchain_hash_tree, toolchain_verify_local, toolchain_redact_package,
    decompiler_cleanup, candidate_search, release_goal_moddable_source,
)
from .store import ReconstructionStore


def _json(raw: str|None, default: Any) -> Any:
    if raw is None: return default
    try: return json.loads(raw)
    except json.JSONDecodeError as exc: raise ContractError(f'invalid JSON argument: {exc}') from exc

def _emit(value: Any) -> None:
    if hasattr(value,'__dict__'): value=value.__dict__
    print(json.dumps(value,indent=2,sort_keys=True,default=str))

def _store(args: argparse.Namespace) -> ReconstructionStore: return ReconstructionStore(args.project)

def build_parser(*,prog:str='x86decomp-reconstruction')->argparse.ArgumentParser:
    parser=argparse.ArgumentParser(prog=prog,description='x86decomp-toolkit 0.7.8 project-scale reconstruction control plane')
    parser.add_argument('--project',default='.',help='project root (default: current directory)'); parser.add_argument('--actor',default='analyst')
    sub=parser.add_subparsers(dest='group',required=True)
    project=sub.add_parser('project'); ps=project.add_subparsers(dest='action',required=True)
    ps.add_parser('init'); ps.add_parser('check'); q=ps.add_parser('health'); q.add_argument('--output'); q=ps.add_parser('doctor-paths'); q.add_argument('root'); q.add_argument('--output')
    q=ps.add_parser('synthesize-layout'); q.add_argument('inventory_json')
    q=ps.add_parser('explain-boundaries'); q.add_argument('module_id')
    q=ps.add_parser('export'); q.add_argument('output')

    module=sub.add_parser('module'); ms=module.add_subparsers(dest='action',required=True)
    q=ms.add_parser('create'); q.add_argument('name'); q.add_argument('--kind',default='static-library'); q.add_argument('--source-path'); q.add_argument('--confidence',type=float,default=1.0); q.add_argument('--evidence-json')
    q=ms.add_parser('add-member'); q.add_argument('module_id'); q.add_argument('member_kind'); q.add_argument('member_id'); q.add_argument('--ordinal',type=int,default=0); q.add_argument('--evidence-json')
    q=ms.add_parser('show'); q.add_argument('module_id')
    ms.add_parser('list')
    q=ms.add_parser('create-unit'); q.add_argument('source_path'); q.add_argument('--module-id'); q.add_argument('--language',default='cpp'); q.add_argument('--confidence',type=float,default=1.0); q.add_argument('--evidence-json')
    q=ms.add_parser('add-unit-member'); q.add_argument('unit_id'); q.add_argument('member_kind'); q.add_argument('member_id'); q.add_argument('--linkage',default='external'); q.add_argument('--ordinal',type=int,default=0)
    q=ms.add_parser('show-unit'); q.add_argument('unit_id')
    q=ms.add_parser('assign'); q.add_argument('function_id'); q.add_argument('--module',required=True); q.add_argument('--class-name'); q.add_argument('--header'); q.add_argument('--source'); q.add_argument('--report')
    q=ms.add_parser('suggest'); q.add_argument('--output')

    headers=sub.add_parser('headers'); hs=headers.add_subparsers(dest='action',required=True)
    q=hs.add_parser('create'); q.add_argument('path'); q.add_argument('--visibility',default='private')
    q=hs.add_parser('declare'); q.add_argument('header_id'); q.add_argument('symbol_id'); q.add_argument('declaration'); q.add_argument('--kind',default='function'); q.add_argument('--confidence',type=float,default=1.0); q.add_argument('--evidence-json')
    q=hs.add_parser('include'); q.add_argument('source_header_id'); q.add_argument('target_header_id'); q.add_argument('--reason',required=True)
    hs.add_parser('cycles')
    q=hs.add_parser('synthesize'); q.add_argument('header_id'); q.add_argument('--output-root')
    q=hs.add_parser('validate'); q.add_argument('header_id')
    q=hs.add_parser('explain'); q.add_argument('header_id')
    q=hs.add_parser('synthesize-project'); q.add_argument('output'); q.add_argument('--module')

    build=sub.add_parser('build'); bs=build.add_subparsers(dest='action',required=True)
    q=bs.add_parser('create'); q.add_argument('name'); q.add_argument('--mode',required=True); q.add_argument('--generator',default='cmake'); q.add_argument('--output-root',default='build'); q.add_argument('--metadata-json')
    q=bs.add_parser('add-target'); q.add_argument('build_id'); q.add_argument('name'); q.add_argument('--kind',default='executable'); q.add_argument('--output-name'); q.add_argument('--sources-json'); q.add_argument('--dependencies-json')
    q=bs.add_parser('add-variant'); q.add_argument('target_id'); q.add_argument('name'); q.add_argument('--compiler',required=True); q.add_argument('--linker',required=True); q.add_argument('--compile-flags-json'); q.add_argument('--link-flags-json'); q.add_argument('--environment-json')
    q=bs.add_parser('show'); q.add_argument('build_id')
    q=bs.add_parser('generate'); q.add_argument('build_id'); q.add_argument('--output-root')
    q=bs.add_parser('validate'); q.add_argument('target_id'); q.add_argument('--variant-id')
    q=bs.add_parser('compare-modes'); q.add_argument('historical_build_id'); q.add_argument('portable_build_id')
    bs.add_parser('matrix')

    provenance=sub.add_parser('provenance'); prs=provenance.add_subparsers(dest='action',required=True)
    q=prs.add_parser('record'); q.add_argument('source_path'); q.add_argument('line_start',type=int); q.add_argument('line_end',type=int); q.add_argument('binary_id'); q.add_argument('address_start'); q.add_argument('address_end'); q.add_argument('--evidence-json',required=True); q.add_argument('--confidence',type=float,required=True)
    q=prs.add_parser('source'); q.add_argument('source_path'); q.add_argument('--line',type=int)
    q=prs.add_parser('binary'); q.add_argument('binary_id'); q.add_argument('--address')
    q=prs.add_parser('export'); q.add_argument('output')

    source=sub.add_parser('source'); ss=source.add_subparsers(dest='action',required=True)
    q=ss.add_parser('reconcile'); q.add_argument('path'); q.add_argument('--before-sha256'); q.add_argument('--semantic',choices=['true','false'])
    q=ss.add_parser('impact'); q.add_argument('path')
    q=ss.add_parser('lock'); q.add_argument('path'); q.add_argument('--reason',required=True)
    q=ss.add_parser('unlock'); q.add_argument('path')

    abi=sub.add_parser('abi'); ab=abi.add_subparsers(dest='action',required=True)
    q=ab.add_parser('recover'); q.add_argument('subject_kind'); q.add_argument('subject_id'); q.add_argument('architecture'); q.add_argument('contract_json'); q.add_argument('--evidence-json',required=True)
    q=ab.add_parser('show'); q.add_argument('contract_id')
    q=ab.add_parser('verify'); q.add_argument('contract_id')
    q=ab.add_parser('compare'); q.add_argument('left_id'); q.add_argument('right_id')
    q=ab.add_parser('export'); q.add_argument('contract_id'); q.add_argument('output')
    q=ab.add_parser('shim'); q.add_argument('contract_id'); q.add_argument('source_path'); q.add_argument('--kind',default='wrapped')

    tests=sub.add_parser('tests'); ts=tests.add_subparsers(dest='action',required=True)
    q=ts.add_parser('synthesize'); q.add_argument('scope_kind'); q.add_argument('scope_id'); q.add_argument('--name')
    q=ts.add_parser('promote-counterexample'); q.add_argument('counterexample_id'); q.add_argument('--name')
    q=ts.add_parser('add'); q.add_argument('name'); q.add_argument('scope_kind'); q.add_argument('scope_id'); q.add_argument('test_kind'); q.add_argument('relative_path'); q.add_argument('content_file'); q.add_argument('--applicability-json',required=True); q.add_argument('--evidence-json',required=True)
    ts.add_parser('list')
    q=ts.add_parser('explain'); q.add_argument('test_id')

    capsule=sub.add_parser('capsule'); cs=capsule.add_subparsers(dest='action',required=True)
    q=cs.add_parser('create'); q.add_argument('name'); q.add_argument('output'); q.add_argument('--include',action='append',default=[]); q.add_argument('--external-json')
    q=cs.add_parser('inspect'); q.add_argument('path')
    q=cs.add_parser('verify'); q.add_argument('path')
    q=cs.add_parser('reproduce'); q.add_argument('path'); q.add_argument('destination')

    library=sub.add_parser('library'); ls=library.add_subparsers(dest='action',required=True)
    q=ls.add_parser('identify'); q.add_argument('subject_id'); q.add_argument('library_name'); q.add_argument('--version-range'); q.add_argument('--confidence',type=float,required=True); q.add_argument('--evidence-json',required=True)
    q=ls.add_parser('candidates'); q.add_argument('subject_id')
    for action in ('accept','externalize','reconstruct','reject'):
        q=ls.add_parser(action); q.add_argument('match_id')

    security=sub.add_parser('security'); ses=security.add_subparsers(dest='action',required=True)
    q=ses.add_parser('scan'); q.add_argument('observations_json')
    q=ses.add_parser('finding'); q.add_argument('rule_id'); q.add_argument('severity'); q.add_argument('subject_id'); q.add_argument('summary'); q.add_argument('--evidence-json',required=True)
    q=ses.add_parser('policy'); q.add_argument('name'); q.add_argument('policy_json')
    ses.add_parser('report')

    llm=sub.add_parser('llm', description='bounded local-model C proposal and deterministic byte matching')
    lls=llm.add_subparsers(dest='action',required=True)
    lls.add_parser('providers', description='list built-in local-model provider presets')
    q=lls.add_parser('profile-create', description='create a validated local-model provider profile'); q.add_argument('provider',choices=[item['id'] for item in llm_provider_catalog()['providers']]); q.add_argument('output'); q.add_argument('--model',required=True); q.add_argument('--base-url'); q.add_argument('--id'); q.add_argument('--api-key-env'); q.add_argument('--allow-remote',action='store_true')
    q=lls.add_parser('profile-validate', description='validate a local-model provider profile'); q.add_argument('profile')
    q=lls.add_parser('probe', description='probe the provider model-list endpoint'); q.add_argument('profile')
    q=lls.add_parser('job-create', description='create a local-LLM job from a function packet'); q.add_argument('function_packet'); q.add_argument('output'); q.add_argument('--architecture',required=True,choices=['x86','x86_64']); q.add_argument('--image-base',type=lambda v:int(v,0),default=0); q.add_argument('--function-name'); q.add_argument('--symbol'); q.add_argument('--max-attempts',type=int,default=4); q.add_argument('--inline',action='store_true'); q.add_argument('--overwrite',action='store_true')
    q=lls.add_parser('job-from-range', description='create a local-LLM job from an explicit byte range'); q.add_argument('image'); q.add_argument('output'); q.add_argument('--rva',type=lambda v:int(v,0),required=True); q.add_argument('--size',type=lambda v:int(v,0),required=True); q.add_argument('--architecture',required=True,choices=['x86','x86_64']); q.add_argument('--function-name',required=True); q.add_argument('--symbol'); q.add_argument('--image-base',type=lambda v:int(v,0),default=0); q.add_argument('--mnemonics'); q.add_argument('--max-attempts',type=int,default=4); q.add_argument('--overwrite',action='store_true')
    q=lls.add_parser('batch-create', description='create local-LLM jobs for eligible project function packets'); q.add_argument('project_root'); q.add_argument('output_directory'); q.add_argument('--architecture',required=True,choices=['x86','x86_64']); q.add_argument('--image-base',type=lambda v:int(v,0),default=0); q.add_argument('--max-bytes',type=int,default=256); q.add_argument('--max-attempts',type=int,default=4); q.add_argument('--overwrite',action='store_true')
    q=lls.add_parser('prompt', description='materialize the deterministic prompt without contacting a model'); q.add_argument('job'); q.add_argument('output')
    q=lls.add_parser('generate', description='generate one uncompiled C proposal'); q.add_argument('profile'); q.add_argument('job'); q.add_argument('output'); q.add_argument('--report'); q.add_argument('--overwrite',action='store_true')
    q=lls.add_parser('cpp-generate', description='generate one bounded C++ proposal using a local-model profile'); q.add_argument('profile'); q.add_argument('job'); q.add_argument('output'); q.add_argument('--class-context'); q.add_argument('--report'); q.add_argument('--overwrite',action='store_true')
    q=lls.add_parser('match', description='run bounded generation, compilation, relocation resolution, and exact byte matching'); q.add_argument('profile'); q.add_argument('compiler_profile'); q.add_argument('job'); q.add_argument('output_directory'); q.add_argument('--max-attempts',type=int); q.add_argument('--overwrite',action='store_true')
    q=lls.add_parser('batch-match', description='run bounded match loops for a deterministic job queue'); q.add_argument('profile'); q.add_argument('compiler_profile'); q.add_argument('jobs'); q.add_argument('output_directory'); q.add_argument('--max-workers',type=int,default=1); q.add_argument('--max-attempts',type=int); q.add_argument('--overwrite',action='store_true')
    q=lls.add_parser('verify', description='verify a local-model byte-match report and accepted artifact hashes'); q.add_argument('report')

    candidate=sub.add_parser('candidate'); cas=candidate.add_subparsers(dest='action',required=True)
    q=cas.add_parser('promote'); q.add_argument('function_id'); q.add_argument('--candidate',required=True); q.add_argument('--report',required=True); q.add_argument('--stage',default='matched'); q.add_argument('--update-workflow',action='store_true'); q.add_argument('--update-build',action='store_true'); q.add_argument('--overwrite',action='store_true')
    q=cas.add_parser('search'); q.add_argument('--phase',action='append'); q.add_argument('--output')

    source_map=sub.add_parser('source-map'); sms=source_map.add_subparsers(dest='action',required=True)
    q=sms.add_parser('annotate'); q.add_argument('source_root'); q.add_argument('--binary',default='GAME'); q.add_argument('--report')
    q=sms.add_parser('verify'); q.add_argument('source_root'); q.add_argument('--report')

    type_group=sub.add_parser('type'); tys=type_group.add_subparsers(dest='action',required=True)
    q=tys.add_parser('propagate'); q.add_argument('--output')

    vtable=sub.add_parser('vtable'); vts=vtable.add_subparsers(dest='action',required=True)
    q=vts.add_parser('recover'); q.add_argument('image'); q.add_argument('--metadata-report'); q.add_argument('--output',required=True)

    class_group=sub.add_parser('class'); cls=class_group.add_subparsers(dest='action',required=True)
    q=cls.add_parser('scaffold'); q.add_argument('vtable_report'); q.add_argument('output'); q.add_argument('--headers')

    diff=sub.add_parser('diff'); dfs=diff.add_subparsers(dest='action',required=True)
    q=dfs.add_parser('explain'); q.add_argument('diff_report'); q.add_argument('--source'); q.add_argument('--output')

    triage=sub.add_parser('triage'); trs=triage.add_subparsers(dest='action',required=True)
    q=trs.add_parser('next'); q.add_argument('--goal',default='matching',choices=['matching','playable']); q.add_argument('--limit',type=int,default=25); q.add_argument('--output')

    playability=sub.add_parser('playability'); pls=playability.add_subparsers(dest='action',required=True)
    q=pls.add_parser('smoke-plan'); q.add_argument('target'); q.add_argument('output'); q.add_argument('--profile',default='windows-game')

    asset=sub.add_parser('asset'); ass=asset.add_subparsers(dest='action',required=True)
    q=ass.add_parser('inventory'); q.add_argument('root'); q.add_argument('--output')

    mod=sub.add_parser('mod'); mos=mod.add_subparsers(dest='action',required=True)
    q=mos.add_parser('branch-init'); q.add_argument('name'); q.add_argument('--baseline',required=True); q.add_argument('--output')

    regression=sub.add_parser('regression'); rgs=regression.add_subparsers(dest='action',required=True)
    q=rgs.add_parser('compare'); q.add_argument('baseline'); q.add_argument('modded'); q.add_argument('--allow'); q.add_argument('--output')

    function=sub.add_parser('function'); fs=function.add_subparsers(dest='action',required=True)
    q=fs.add_parser('discover'); q.add_argument('image'); q.add_argument('--profile',default='prologue',choices=['prologue','ret-boundary']); q.add_argument('--architecture',default='x86',choices=['x86','x86_64']); q.add_argument('--min-size',type=int,default=1); q.add_argument('--max-size',type=int,default=1048576); q.add_argument('--align',type=int,default=1); q.add_argument('--output')
    q=fs.add_parser('reconcile'); q.add_argument('reports',nargs='+'); q.add_argument('--output')
    q=fs.add_parser('sort'); q.add_argument('functions_json'); q.add_argument('--key',default='rva'); q.add_argument('--output')
    q=fs.add_parser('classify'); q.add_argument('functions_json'); q.add_argument('--output')

    pattern=sub.add_parser('pattern'); pts=pattern.add_subparsers(dest='action',required=True)
    q=pts.add_parser('catalog'); q.add_argument('--output')
    q=pts.add_parser('scan'); q.add_argument('root'); q.add_argument('--architecture',choices=['x86','x86_64']); q.add_argument('--output')
    q=pts.add_parser('generate'); q.add_argument('scan_report'); q.add_argument('output'); q.add_argument('--symbol-prefix',default='sub')
    q=pts.add_parser('match'); q.add_argument('generation_report'); q.add_argument('--output')
    q=pts.add_parser('promote'); q.add_argument('function_id'); q.add_argument('--candidate',required=True); q.add_argument('--report',required=True); q.add_argument('--stage',default='pattern'); q.add_argument('--output'); q.add_argument('--overwrite',action='store_true')

    image_text=sub.add_parser('image-text'); its=image_text.add_subparsers(dest='action',required=True)
    q=its.add_parser('compose'); q.add_argument('output'); q.add_argument('--function-list'); q.add_argument('--fallback-byte',type=lambda v:int(v,0),default=0xCC)

    text_swap=sub.add_parser('text-swap'); tss=text_swap.add_subparsers(dest='action',required=True)
    q=tss.add_parser('plan'); q.add_argument('original'); q.add_argument('replacement'); q.add_argument('output'); q.add_argument('--section-name',default='.text')
    q=tss.add_parser('build'); q.add_argument('replacement'); q.add_argument('output'); q.add_argument('--original',required=True); q.add_argument('--section-name',default='.text')
    q=tss.add_parser('inject'); q.add_argument('plan'); q.add_argument('--output')
    q=tss.add_parser('verify'); q.add_argument('plan'); q.add_argument('image'); q.add_argument('--output')

    progress=sub.add_parser('progress'); prs=progress.add_subparsers(dest='action',required=True)
    q=prs.add_parser('reconcile'); q.add_argument('--output')

    source_stage=sub.add_parser('source-stage'); sss=source_stage.add_subparsers(dest='action',required=True)
    q=sss.add_parser('classify'); q.add_argument('--output')

    ghidra_mcp=sub.add_parser('ghidra-mcp'); gms=ghidra_mcp.add_subparsers(dest='action',required=True)
    q=gms.add_parser('probe'); q.add_argument('url'); q.add_argument('--timeout',type=float,default=5.0); q.add_argument('--output')
    q=gms.add_parser('functions'); q.add_argument('url'); q.add_argument('--timeout',type=float,default=30.0); q.add_argument('--output')
    q=gms.add_parser('decompile'); q.add_argument('url'); q.add_argument('address'); q.add_argument('--timeout',type=float,default=60.0); q.add_argument('--output')
    q=gms.add_parser('batch-decompile'); q.add_argument('url'); q.add_argument('addresses'); q.add_argument('output'); q.add_argument('--timeout',type=float,default=60.0)
    q=gms.add_parser('sync-names'); q.add_argument('names_json'); q.add_argument('--output')

    compiler_rules=sub.add_parser('compiler-rules'); crs=compiler_rules.add_subparsers(dest='action',required=True)
    q=crs.add_parser('learn-rule'); q.add_argument('rule_id'); q.add_argument('observations'); q.add_argument('output')
    q=crs.add_parser('rule-report'); q.add_argument('rules',nargs='+'); q.add_argument('--output')
    q=crs.add_parser('compare-flags'); q.add_argument('reports',nargs='+'); q.add_argument('--output')

    runtime_accel=sub.add_parser('runtime-analysis'); ras=runtime_accel.add_subparsers(dest='action',required=True)
    q=ras.add_parser('identify'); q.add_argument('--output')
    q=ras.add_parser('quarantine'); q.add_argument('identification_report'); q.add_argument('--output')
    q=ras.add_parser('match-library'); q.add_argument('library_inventory'); q.add_argument('--output')

    subsystem=sub.add_parser('subsystem'); sus=subsystem.add_subparsers(dest='action',required=True)
    q=sus.add_parser('detect'); q.add_argument('root'); q.add_argument('--output')

    game_pattern=sub.add_parser('game-pattern'); gps=game_pattern.add_subparsers(dest='action',required=True)
    q=gps.add_parser('state-machine'); q.add_argument('root'); q.add_argument('--output')

    script_port=sub.add_parser('script-port'); sps=script_port.add_subparsers(dest='action',required=True)
    q=sps.add_parser('audit'); q.add_argument('root'); q.add_argument('--output')

    toolchain=sub.add_parser('toolchain'); tos=toolchain.add_subparsers(dest='action',required=True)
    q=tos.add_parser('hash-tree'); q.add_argument('root'); q.add_argument('output')
    q=tos.add_parser('verify-local'); q.add_argument('manifest'); q.add_argument('--output')
    q=tos.add_parser('redact-package'); q.add_argument('root'); q.add_argument('output'); q.add_argument('--manifest')

    decompiler=sub.add_parser('decompiler'); dcs=decompiler.add_subparsers(dest='action',required=True)
    q=dcs.add_parser('cleanup'); q.add_argument('input_file'); q.add_argument('output'); q.add_argument('--compiler',default='generic'); q.add_argument('--language',default='cpp'); q.add_argument('--locals-at-top',action='store_true')

    release_policy=sub.add_parser('release-policy'); rps=release_policy.add_subparsers(dest='action',required=True)
    q=rps.add_parser('moddable-source'); q.add_argument('--output')

    changeset=sub.add_parser('changeset'); ch=changeset.add_subparsers(dest='action',required=True)
    q=ch.add_parser('create'); q.add_argument('name'); q.add_argument('--base-audit-hash')
    q=ch.add_parser('add-operation'); q.add_argument('changeset_id'); q.add_argument('operation_json')
    q=ch.add_parser('merge'); q.add_argument('left_id'); q.add_argument('right_id'); q.add_argument('name')
    q=ch.add_parser('conflicts'); q.add_argument('changeset_id')
    q=ch.add_parser('rebase'); q.add_argument('changeset_id'); q.add_argument('new_base_hash')
    q=ch.add_parser('verify'); q.add_argument('changeset_id')
    q=ch.add_parser('show'); q.add_argument('changeset_id')
    return parser

def dispatch(args:argparse.Namespace)->Any:
    store=_store(args); actor=args.actor
    if args.group=='project':
        if args.action=='init': store.initialize(); return store.check()
        if args.action=='check': return store.check()
        if args.action=='health': return project_health(Path(args.project), output=None if args.output is None else Path(args.output))
        if args.action=='doctor-paths': return project_doctor_paths(Path(args.root), output=None if args.output is None else Path(args.output))
        api=ProjectLayout(store)
        if args.action=='synthesize-layout': return api.synthesize(_json(args.inventory_json,[]),actor=actor)
        if args.action=='explain-boundaries': return api.explain_boundaries(args.module_id)
        return api.export(args.output)
    if args.group=='module':
        api=ProjectLayout(store)
        if args.action=='create': return api.create_module(args.name,kind=args.kind,source_path=args.source_path,confidence=args.confidence,evidence=_json(args.evidence_json,[]),actor=actor)
        if args.action=='add-member': return api.add_member(args.module_id,args.member_kind,args.member_id,ordinal=args.ordinal,evidence=_json(args.evidence_json,[]),actor=actor)
        if args.action=='show': return api.show_module(args.module_id)
        if args.action=='list': return api.list_modules()
        if args.action=='create-unit': return api.create_translation_unit(args.source_path,module_id=args.module_id,language=args.language,confidence=args.confidence,evidence=_json(args.evidence_json,[]),actor=actor)
        if args.action=='add-unit-member': return api.add_translation_unit_member(args.unit_id,args.member_kind,args.member_id,linkage=args.linkage,ordinal=args.ordinal,actor=actor)
        if args.action=='show-unit': return api.show_translation_unit(args.unit_id)
        if args.action=='assign': return module_assign(Path(args.project), args.function_id, module=args.module, class_name=args.class_name, header=args.header, source=args.source, report_path=None if args.report is None else Path(args.report))
        return module_suggest(Path(args.project), output=None if args.output is None else Path(args.output))
    if args.group=='headers':
        api=HeaderManager(store)
        if args.action=='create': return api.create(args.path,visibility=args.visibility,actor=actor)
        if args.action=='declare': return api.declare(args.header_id,args.symbol_id,args.declaration,kind=args.kind,confidence=args.confidence,evidence=_json(args.evidence_json,[]),actor=actor)
        if args.action=='include': return api.include(args.source_header_id,args.target_header_id,reason=args.reason,actor=actor)
        if args.action=='cycles': return api.cycles()
        if args.action=='synthesize': return api.synthesize(args.header_id,output_root=args.output_root)
        if args.action=='validate': return api.validate(args.header_id)
        if args.action=='explain': return api.show(args.header_id)
        return header_synthesize_project(Path(args.project), Path(args.output), module=args.module)
    if args.group=='build':
        api=BuildManager(store)
        if args.action=='create': return api.create(args.name,mode=args.mode,generator=args.generator,output_root=args.output_root,metadata=_json(args.metadata_json,{}),actor=actor)
        if args.action=='add-target': return api.add_target(args.build_id,args.name,kind=args.kind,output_name=args.output_name,sources=_json(args.sources_json,[]),dependencies=_json(args.dependencies_json,[]),actor=actor)
        if args.action=='add-variant': return api.add_variant(args.target_id,args.name,compiler=args.compiler,linker=args.linker,compile_flags=_json(args.compile_flags_json,[]),link_flags=_json(args.link_flags_json,[]),environment=_json(args.environment_json,{}),actor=actor)
        if args.action=='show': return api.show(args.build_id)
        if args.action=='generate': return api.generate(args.build_id,output_root=args.output_root)
        if args.action=='validate': return api.validate(args.target_id,args.variant_id,actor=actor)
        if args.action=='compare-modes': return api.compare_modes(args.historical_build_id,args.portable_build_id)
        return api.matrix()
    if args.group=='provenance':
        api=ProvenanceLedger(store)
        if args.action=='record': return api.record(args.source_path,args.line_start,args.line_end,args.binary_id,args.address_start,args.address_end,evidence=_json(args.evidence_json,[]),confidence=args.confidence,actor=actor)
        if args.action=='source': return api.source(args.source_path,args.line)
        if args.action=='binary': return api.binary(args.binary_id,args.address)
        return api.export(args.output)
    if args.group=='source':
        api=ProvenanceLedger(store)
        if args.action=='reconcile': return api.reconcile(args.path,before_sha256=args.before_sha256,semantic=None if args.semantic is None else args.semantic=='true',actor=actor)
        if args.action=='impact': return api.impact(args.path)
        if args.action=='lock': return api.lock(args.path,reason=args.reason,actor=actor)
        return api.unlock(args.path,actor=actor)
    if args.group=='abi':
        api=ABIContracts(store)
        if args.action=='recover': return api.recover(args.subject_kind,args.subject_id,args.architecture,_json(args.contract_json,{}),evidence=_json(args.evidence_json,[]),actor=actor)
        if args.action=='show': return api.get(args.contract_id)
        if args.action=='verify': return api.verify(args.contract_id)
        if args.action=='compare': return api.compare(args.left_id,args.right_id)
        if args.action=='export': return api.export(args.contract_id,args.output)
        return api.shim(args.contract_id,args.source_path,shim_kind=args.kind,actor=actor)
    if args.group=='tests':
        api=GeneratedTests(store)
        if args.action=='synthesize': return api.synthesize(args.scope_kind,args.scope_id,name=args.name,actor=actor)
        if args.action=='promote-counterexample': return api.promote_counterexample(args.counterexample_id,name=args.name,actor=actor)
        if args.action=='add': return api.add(args.name,args.scope_kind,args.scope_id,args.test_kind,args.relative_path,Path(args.content_file).read_text(encoding='utf-8'),applicability=_json(args.applicability_json,{}),evidence=_json(args.evidence_json,[]),actor=actor)
        if args.action=='list': return api.list()
        return api.explain(args.test_id)
    if args.group=='capsule':
        api=Capsules(store)
        if args.action=='create': return api.create(args.name,args.output,include=args.include,external_requirements=_json(args.external_json,[]),actor=actor)
        if args.action=='inspect': return api.inspect(args.path)
        if args.action=='verify': return api.verify(args.path)
        return api.reproduce(args.path,args.destination)
    if args.group=='library':
        api=LibraryRecognition(store)
        if args.action=='identify': return api.identify(args.subject_id,args.library_name,version_range=args.version_range,confidence=args.confidence,evidence=_json(args.evidence_json,[]),actor=actor)
        if args.action=='candidates': return api.candidates(args.subject_id)
        disposition={'accept':'accepted','externalize':'externalized','reconstruct':'reconstruct','reject':'rejected'}[args.action]
        return api.disposition(args.match_id,disposition,actor=actor)
    if args.group=='security':
        api=SecurityReview(store)
        if args.action=='scan': return api.scan(_json(args.observations_json,[]),actor=actor)
        if args.action=='finding': return api.finding(args.rule_id,args.severity,args.subject_id,args.summary,evidence=_json(args.evidence_json,[]),actor=actor)
        if args.action=='policy': return api.policy(args.name,_json(args.policy_json,{}),actor=actor)
        return api.report()
    if args.group=='llm':
        if args.action=='providers': return llm_provider_catalog()
        if args.action=='profile-create': return create_llm_profile(args.provider,Path(args.output),model=args.model,base_url=args.base_url,profile_id=args.id,api_key_env=args.api_key_env,allow_remote=args.allow_remote)
        if args.action=='profile-validate': return public_llm_profile(load_llm_profile(Path(args.profile)))
        if args.action=='probe': return probe_llm_profile(load_llm_profile(Path(args.profile)))
        if args.action=='job-create': return llm_job_from_function_packet(Path(args.function_packet), Path(args.output), architecture=args.architecture, image_base=args.image_base, function_name=args.function_name, symbol=args.symbol, max_attempts=args.max_attempts, inline=args.inline, overwrite=args.overwrite)
        if args.action=='job-from-range': return llm_job_from_range(Path(args.image), Path(args.output), rva=args.rva, size=args.size, architecture=args.architecture, function_name=args.function_name, symbol=args.symbol, image_base=args.image_base, mnemonics=None if args.mnemonics is None else Path(args.mnemonics), max_attempts=args.max_attempts, overwrite=args.overwrite)
        if args.action=='batch-create': return llm_batch_create(Path(args.project_root), Path(args.output_directory), architecture=args.architecture, image_base=args.image_base, max_bytes=args.max_bytes, max_attempts=args.max_attempts, overwrite=args.overwrite)
        if args.action=='prompt':
            record=llm_prompt_record(load_llm_job(Path(args.job))); write_json(Path(args.output),record); return record
        if args.action=='generate':
            result=generate_llm_candidate(Path(args.profile),Path(args.job),Path(args.output),overwrite=args.overwrite)
            if args.report: write_json(Path(args.report),result)
            return result
        if args.action=='cpp-generate':
            result=generate_llm_candidate(Path(args.profile),Path(args.job),Path(args.output),overwrite=args.overwrite)
            result['language']='cpp'; result['claim']='proposal_only_cpp_uncompiled'
            if args.report: write_json(Path(args.report),result)
            return result
        if args.action=='match': return run_llm_match_loop(Path(args.profile),Path(args.compiler_profile),Path(args.job),Path(args.output_directory),max_attempts=args.max_attempts,overwrite=args.overwrite)
        if args.action=='batch-match': return llm_batch_match(Path(args.profile), Path(args.compiler_profile), Path(args.jobs), Path(args.output_directory), max_workers=args.max_workers, max_attempts=args.max_attempts, overwrite=args.overwrite)
        return verify_llm_match_report(Path(args.report))
    if args.group=='candidate':
        if args.action=='search': return candidate_search(Path(args.project), output=None if args.output is None else Path(args.output), phases=args.phase)
        return candidate_promote(Path(args.project), args.function_id, Path(args.candidate), Path(args.report), stage=args.stage, update_build=args.update_build, update_workflow=args.update_workflow, overwrite=args.overwrite)
    if args.group=='source-map':
        if args.action=='annotate': return source_map_annotate(Path(args.project), Path(args.source_root), binary=args.binary, report_path=None if args.report is None else Path(args.report))
        return source_map_verify(Path(args.project), Path(args.source_root), report_path=None if args.report is None else Path(args.report))
    if args.group=='type': return type_propagate(Path(args.project), output=None if args.output is None else Path(args.output))
    if args.group=='vtable': return vtable_recover(Path(args.project), Path(args.image), Path(args.output), metadata_report=None if args.metadata_report is None else Path(args.metadata_report))
    if args.group=='class': return class_scaffold(Path(args.project), Path(args.vtable_report), Path(args.output), headers=None if args.headers is None else Path(args.headers))
    if args.group=='diff': return diff_explain(Path(args.diff_report), source=None if args.source is None else Path(args.source), output=None if args.output is None else Path(args.output))
    if args.group=='triage': return triage_next(Path(args.project), goal=args.goal, limit=args.limit, output=None if args.output is None else Path(args.output))
    if args.group=='playability': return playability_smoke_plan(Path(args.project), Path(args.target), Path(args.output), profile=args.profile)
    if args.group=='asset': return asset_inventory(Path(args.root), output=None if args.output is None else Path(args.output))
    if args.group=='mod': return mod_branch_init(Path(args.project), args.name, baseline=Path(args.baseline), output=None if args.output is None else Path(args.output))
    if args.group=='regression': return regression_compare(Path(args.baseline), Path(args.modded), allow=None if args.allow is None else Path(args.allow), output=None if args.output is None else Path(args.output))
    if args.group=='function':
        if args.action=='discover': return function_discover(Path(args.image), output=None if args.output is None else Path(args.output), profile=args.profile, architecture=args.architecture, min_size=args.min_size, max_size=args.max_size, align=args.align)
        if args.action=='reconcile': return function_boundary_reconcile([Path(p) for p in args.reports], output=None if args.output is None else Path(args.output))
        if args.action=='sort': return function_list_sort(Path(args.functions_json), output=None if args.output is None else Path(args.output), key=args.key)
        return function_list_classify(Path(args.functions_json), output=None if args.output is None else Path(args.output))
    if args.group=='pattern':
        if args.action=='catalog': return pattern_catalog(output=None if args.output is None else Path(args.output))
        if args.action=='scan': return pattern_scan(Path(args.root), output=None if args.output is None else Path(args.output), architecture=args.architecture)
        if args.action=='generate': return pattern_generate(Path(args.scan_report), Path(args.output), symbol_prefix=args.symbol_prefix)
        if args.action=='match': return pattern_match(Path(args.generation_report), output=None if args.output is None else Path(args.output))
        return pattern_promote(Path(args.project), args.function_id, Path(args.candidate), Path(args.report), stage=args.stage, output=None if args.output is None else Path(args.output), overwrite=args.overwrite)
    if args.group=='image-text': return image_text_compose(Path(args.project), Path(args.output), function_list=None if args.function_list is None else Path(args.function_list), fallback_byte=args.fallback_byte)
    if args.group=='text-swap':
        if args.action=='plan': return text_swap_plan(Path(args.original), Path(args.replacement), Path(args.output), section_name=args.section_name)
        if args.action=='build': return text_swap_build(Path(args.project), Path(args.replacement), Path(args.output), original=Path(args.original), section_name=args.section_name)
        if args.action=='inject': return text_swap_inject(Path(args.plan), output=None if args.output is None else Path(args.output))
        return text_swap_verify(Path(args.plan), Path(args.image), output=None if args.output is None else Path(args.output))
    if args.group=='progress': return progress_reconcile(Path(args.project), output=None if args.output is None else Path(args.output))
    if args.group=='source-stage': return source_stage_classify(Path(args.project), output=None if args.output is None else Path(args.output))
    if args.group=='ghidra-mcp':
        if args.action=='probe': return ghidra_mcp_probe(args.url, output=None if args.output is None else Path(args.output), timeout=args.timeout)
        if args.action=='functions': return ghidra_mcp_functions(args.url, output=None if args.output is None else Path(args.output), timeout=args.timeout)
        if args.action=='decompile': return ghidra_mcp_decompile(args.url, args.address, output=None if args.output is None else Path(args.output), timeout=args.timeout)
        if args.action=='batch-decompile': return ghidra_mcp_batch_decompile(args.url, Path(args.addresses), Path(args.output), timeout=args.timeout)
        return ghidra_mcp_sync_names(Path(args.project), Path(args.names_json), output=None if args.output is None else Path(args.output))
    if args.group=='compiler-rules':
        if args.action=='learn-rule': return compiler_rule_learn(args.rule_id, Path(args.observations), Path(args.output))
        if args.action=='rule-report': return compiler_rule_report([Path(p) for p in args.rules], output=None if args.output is None else Path(args.output))
        return compiler_compare_flags([Path(p) for p in args.reports], output=None if args.output is None else Path(args.output))
    if args.group=='runtime-analysis':
        if args.action=='identify': return runtime_identify(Path(args.project), output=None if args.output is None else Path(args.output))
        if args.action=='quarantine': return runtime_quarantine(Path(args.project), Path(args.identification_report), output=None if args.output is None else Path(args.output))
        return runtime_match_library(Path(args.project), Path(args.library_inventory), output=None if args.output is None else Path(args.output))
    if args.group=='subsystem': return subsystem_detect(Path(args.root), output=None if args.output is None else Path(args.output))
    if args.group=='game-pattern': return state_machine_detect(Path(args.root), output=None if args.output is None else Path(args.output))
    if args.group=='script-port': return script_port_audit(Path(args.root), output=None if args.output is None else Path(args.output))
    if args.group=='toolchain':
        if args.action=='hash-tree': return toolchain_hash_tree(Path(args.root), Path(args.output))
        if args.action=='verify-local': return toolchain_verify_local(Path(args.manifest), output=None if args.output is None else Path(args.output))
        return toolchain_redact_package(Path(args.root), Path(args.output), manifest=None if args.manifest is None else Path(args.manifest))
    if args.group=='decompiler': return decompiler_cleanup(Path(args.input_file), Path(args.output), compiler=args.compiler, language=args.language, locals_at_top=args.locals_at_top)
    if args.group=='release-policy': return release_goal_moddable_source(Path(args.project), output=None if args.output is None else Path(args.output))
    if args.group=='changeset':
        api=SemanticChangeSets(store)
        if args.action=='create': return api.create(args.name,base_audit_hash=args.base_audit_hash,actor=actor)
        if args.action=='add-operation': return api.add_operation(args.changeset_id,_json(args.operation_json,{}),actor=actor)
        if args.action=='merge': return api.merge(args.left_id,args.right_id,args.name,actor=actor)
        if args.action=='conflicts': return api.conflicts(args.changeset_id)
        if args.action=='rebase': return api.rebase(args.changeset_id,args.new_base_hash,actor=actor)
        if args.action=='verify': return api.verify(args.changeset_id)
        return api.get(args.changeset_id)
    raise ContractError('unhandled command')

def main(argv:list[str]|None=None)->int:
    parser=build_parser()
    try: args=parser.parse_args(argv); _emit(dispatch(args)); return 0
    except (ContractError,KeyError,OSError,ValueError) as exc:
        print(json.dumps({'error':type(exc).__name__,'message':str(exc)},sort_keys=True),file=sys.stderr); return 2

if __name__=='__main__': raise SystemExit(main())
