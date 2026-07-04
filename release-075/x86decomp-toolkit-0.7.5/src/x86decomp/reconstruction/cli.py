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
    parser=argparse.ArgumentParser(prog=prog,description='x86decomp-toolkit 0.7.5 project-scale reconstruction control plane')
    parser.add_argument('--project',default='.',help='project root (default: current directory)'); parser.add_argument('--actor',default='analyst')
    sub=parser.add_subparsers(dest='group',required=True)
    project=sub.add_parser('project'); ps=project.add_subparsers(dest='action',required=True)
    ps.add_parser('init'); ps.add_parser('check')
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

    headers=sub.add_parser('headers'); hs=headers.add_subparsers(dest='action',required=True)
    q=hs.add_parser('create'); q.add_argument('path'); q.add_argument('--visibility',default='private')
    q=hs.add_parser('declare'); q.add_argument('header_id'); q.add_argument('symbol_id'); q.add_argument('declaration'); q.add_argument('--kind',default='function'); q.add_argument('--confidence',type=float,default=1.0); q.add_argument('--evidence-json')
    q=hs.add_parser('include'); q.add_argument('source_header_id'); q.add_argument('target_header_id'); q.add_argument('--reason',required=True)
    hs.add_parser('cycles')
    q=hs.add_parser('synthesize'); q.add_argument('header_id'); q.add_argument('--output-root')
    q=hs.add_parser('validate'); q.add_argument('header_id')
    q=hs.add_parser('explain'); q.add_argument('header_id')

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
    q=lls.add_parser('prompt', description='materialize the deterministic prompt without contacting a model'); q.add_argument('job'); q.add_argument('output')
    q=lls.add_parser('generate', description='generate one uncompiled C proposal'); q.add_argument('profile'); q.add_argument('job'); q.add_argument('output'); q.add_argument('--report'); q.add_argument('--overwrite',action='store_true')
    q=lls.add_parser('match', description='run bounded generation, compilation, relocation resolution, and exact byte matching'); q.add_argument('profile'); q.add_argument('compiler_profile'); q.add_argument('job'); q.add_argument('output_directory'); q.add_argument('--max-attempts',type=int); q.add_argument('--overwrite',action='store_true')
    q=lls.add_parser('verify', description='verify a local-model byte-match report and accepted artifact hashes'); q.add_argument('report')

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
        return api.show_translation_unit(args.unit_id)
    if args.group=='headers':
        api=HeaderManager(store)
        if args.action=='create': return api.create(args.path,visibility=args.visibility,actor=actor)
        if args.action=='declare': return api.declare(args.header_id,args.symbol_id,args.declaration,kind=args.kind,confidence=args.confidence,evidence=_json(args.evidence_json,[]),actor=actor)
        if args.action=='include': return api.include(args.source_header_id,args.target_header_id,reason=args.reason,actor=actor)
        if args.action=='cycles': return api.cycles()
        if args.action=='synthesize': return api.synthesize(args.header_id,output_root=args.output_root)
        if args.action=='validate': return api.validate(args.header_id)
        return api.show(args.header_id)
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
        if args.action=='prompt':
            record=llm_prompt_record(load_llm_job(Path(args.job))); write_json(Path(args.output),record); return record
        if args.action=='generate':
            result=generate_llm_candidate(Path(args.profile),Path(args.job),Path(args.output),overwrite=args.overwrite)
            if args.report: write_json(Path(args.report),result)
            return result
        if args.action=='match': return run_llm_match_loop(Path(args.profile),Path(args.compiler_profile),Path(args.job),Path(args.output_directory),max_attempts=args.max_attempts,overwrite=args.overwrite)
        return verify_llm_match_report(Path(args.report))
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
