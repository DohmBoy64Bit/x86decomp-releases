"""Register and dispatch evidence-governance CLI commands."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from x86decomp.cli_utils import parse_json_arg, run_cli
from x86decomp.contracts import ContractError

from .campaigns import CampaignEngine
from .candidates import CandidateStore
from .changesets import ChangeSet
from .consensus import ConsensusEngine
from .counterexamples import CounterexampleStore
from .family import BinaryFamilyStore
from .hypotheses import HypothesisLedger
from .knowledge_graph import KnowledgeGraph
from .plugins import PluginRegistry
from .proofs import ProofBundle, ProofLedger
from .reviews import ReviewQueue
from .store import GovernanceStore
from .workers import WorkerRegistry



def _store(args: argparse.Namespace) -> GovernanceStore:
    """Open the project store requested by parsed command arguments."""
    return GovernanceStore(args.project)


def build_parser(*, prog: str = "x86decomp-governance") -> argparse.ArgumentParser:
    """Build the argparse parser for this command surface."""
    parser = argparse.ArgumentParser(prog=prog, description="x86decomp-toolkit 0.7.11 evidence-driven convergence control plane")
    parser.add_argument("--project", default=".", help="project root (default: current directory)")
    parser.add_argument("--actor", default="analyst")
    sub = parser.add_subparsers(dest="group", required=True)

    project = sub.add_parser("project"); psub = project.add_subparsers(dest="action", required=True)
    psub.add_parser("init"); psub.add_parser("check")

    campaign = sub.add_parser("campaign"); csub = campaign.add_subparsers(dest="action", required=True)
    p=csub.add_parser("create"); p.add_argument("goal"); p.add_argument("--budget-json"); p.add_argument("--policy-json")
    for name in ("start","pause","resume","stop","status","snapshot","plan"): p=csub.add_parser(name); p.add_argument("campaign_id")
    p=csub.add_parser("list")
    p=csub.add_parser("branch"); p.add_argument("campaign_id"); p.add_argument("name"); p.add_argument("--parent")

    hypothesis = sub.add_parser("hypothesis"); hsub = hypothesis.add_subparsers(dest="action", required=True)
    p=hsub.add_parser("create"); p.add_argument("statement"); p.add_argument("scope_kind"); p.add_argument("scope_id"); p.add_argument("--origin", required=True)
    p=hsub.add_parser("list"); p.add_argument("--state"); p.add_argument("--scope-id")
    p=hsub.add_parser("show"); p.add_argument("hypothesis_id")
    p=hsub.add_parser("dependency"); p.add_argument("hypothesis_id"); p.add_argument("depends_on_id")
    p=hsub.add_parser("evidence"); p.add_argument("hypothesis_id"); p.add_argument("evidence_id"); p.add_argument("--stance", required=True); p.add_argument("--weight", type=float, required=True); p.add_argument("--kind", required=True); p.add_argument("--group", required=True); p.add_argument("--artifact-sha256"); p.add_argument("--details-json")
    p=hsub.add_parser("transition"); p.add_argument("hypothesis_id"); p.add_argument("state"); p.add_argument("--reason", required=True); p.add_argument("--lock", action="store_true")
    p=hsub.add_parser("gate"); p.add_argument("hypothesis_id")

    candidate = sub.add_parser("candidate"); dsub = candidate.add_subparsers(dest="action", required=True)
    p=dsub.add_parser("create"); p.add_argument("branch_name"); p.add_argument("--campaign-id"); p.add_argument("--parent"); p.add_argument("--objective-json")
    p=dsub.add_parser("add-file"); p.add_argument("candidate_id"); p.add_argument("source"); p.add_argument("relative_path")
    p=dsub.add_parser("evaluate"); p.add_argument("candidate_id"); p.add_argument("metric"); p.add_argument("status"); p.add_argument("--value", type=float); p.add_argument("--details-json")
    p=dsub.add_parser("compare"); p.add_argument("left_id"); p.add_argument("right_id")
    p=dsub.add_parser("transition"); p.add_argument("candidate_id"); p.add_argument("state"); p.add_argument("--reason", required=True)
    p=dsub.add_parser("show"); p.add_argument("candidate_id")
    p=dsub.add_parser("list"); p.add_argument("--campaign-id")

    cex = sub.add_parser("counterexample"); xsub = cex.add_subparsers(dest="action", required=True)
    p=xsub.add_parser("add"); p.add_argument("scope_kind"); p.add_argument("scope_id"); p.add_argument("payload"); p.add_argument("--predicate-json", required=True); p.add_argument("--provenance-json")
    p=xsub.add_parser("show"); p.add_argument("counterexample_id")
    xsub.add_parser("list")
    p=xsub.add_parser("promote"); p.add_argument("counterexample_id"); p.add_argument("destination")

    consensus = sub.add_parser("consensus"); ssub = consensus.add_subparsers(dest="action", required=True)
    p=ssub.add_parser("record"); p.add_argument("subject_kind"); p.add_argument("subject_id"); p.add_argument("property_name"); p.add_argument("value_json"); p.add_argument("--adapter", required=True); p.add_argument("--adapter-version", required=True); p.add_argument("--evidence-id", required=True); p.add_argument("--group", required=True); p.add_argument("--confidence", type=float, default=1.0)
    p=ssub.add_parser("scan"); p.add_argument("--subject-kind"); p.add_argument("--subject-id")
    ssub.add_parser("conflicts")
    p=ssub.add_parser("resolve"); p.add_argument("subject_kind"); p.add_argument("subject_id"); p.add_argument("property_name"); p.add_argument("selected_value_json"); p.add_argument("--method", required=True); p.add_argument("--rationale", required=True); p.add_argument("--lock", action="store_true")
    p=ssub.add_parser("explain"); p.add_argument("subject_kind"); p.add_argument("subject_id"); p.add_argument("property_name")

    graph = sub.add_parser("graph"); gsub = graph.add_subparsers(dest="action", required=True)
    p=gsub.add_parser("node"); p.add_argument("node_id"); p.add_argument("kind"); p.add_argument("label"); p.add_argument("--attributes-json")
    p=gsub.add_parser("edge"); p.add_argument("source_id"); p.add_argument("target_id"); p.add_argument("relation"); p.add_argument("--attributes-json")
    p=gsub.add_parser("impact"); p.add_argument("node_id"); p.add_argument("--direction", default="outbound"); p.add_argument("--max-depth", type=int, default=8); p.add_argument("--relations")

    review = sub.add_parser("review"); rsub = review.add_subparsers(dest="action", required=True)
    p=rsub.add_parser("create"); p.add_argument("kind"); p.add_argument("subject_id"); p.add_argument("summary"); p.add_argument("--priority", type=int, default=50); p.add_argument("--details-json")
    p=rsub.add_parser("list"); p.add_argument("--status"); p.add_argument("--limit", type=int, default=100)
    p=rsub.add_parser("show"); p.add_argument("review_id")
    p=rsub.add_parser("assign"); p.add_argument("review_id"); p.add_argument("assignee")
    p=rsub.add_parser("decide"); p.add_argument("review_id"); p.add_argument("decision"); p.add_argument("--rationale", required=True); p.add_argument("--lock", action="store_true")
    p=rsub.add_parser("lock"); p.add_argument("review_id")

    family = sub.add_parser("family"); fsub = family.add_subparsers(dest="action", required=True)
    p=fsub.add_parser("create"); p.add_argument("name")
    p=fsub.add_parser("add"); p.add_argument("family_id"); p.add_argument("label"); p.add_argument("path"); p.add_argument("--metadata-json")
    p=fsub.add_parser("correlate"); p.add_argument("left_member_id"); p.add_argument("right_member_id"); p.add_argument("--block-size", type=int, default=64)
    p=fsub.add_parser("report"); p.add_argument("family_id")

    proof = sub.add_parser("proof"); osub = proof.add_subparsers(dest="action", required=True)
    p=osub.add_parser("obligation"); p.add_argument("scope_kind"); p.add_argument("scope_id"); p.add_argument("property_name"); p.add_argument("required_status"); p.add_argument("--assumptions-json")
    p=osub.add_parser("result"); p.add_argument("obligation_id"); p.add_argument("status"); p.add_argument("validator"); p.add_argument("report_json"); p.add_argument("--artifact-sha256")
    p=osub.add_parser("evaluate"); p.add_argument("obligation_id")
    p=osub.add_parser("export"); p.add_argument("output"); p.add_argument("--include", action="append", default=[])
    p=osub.add_parser("verify"); p.add_argument("path")
    p=osub.add_parser("inspect"); p.add_argument("path")

    worker = sub.add_parser("worker"); wsub = worker.add_subparsers(dest="action", required=True)
    p=wsub.add_parser("register"); p.add_argument("name"); p.add_argument("capabilities_json"); p.add_argument("--endpoint"); p.add_argument("--environment-sha256")
    p=wsub.add_parser("list"); p.add_argument("--status")
    p=wsub.add_parser("doctor"); p.add_argument("worker_id")
    p=wsub.add_parser("status"); p.add_argument("worker_id"); p.add_argument("status")
    p=wsub.add_parser("select"); p.add_argument("required_json")

    plugin = sub.add_parser("plugin"); lsub = plugin.add_subparsers(dest="action", required=True)
    p=lsub.add_parser("validate"); p.add_argument("manifest")
    p=lsub.add_parser("install"); p.add_argument("manifest")
    lsub.add_parser("list")
    p=lsub.add_parser("doctor"); p.add_argument("plugin_id")
    p=lsub.add_parser("invoke"); p.add_argument("plugin_id"); p.add_argument("capability"); p.add_argument("request_json"); p.add_argument("--timeout", type=int, default=60)

    change = sub.add_parser("changeset"); qsub = change.add_subparsers(dest="action", required=True)
    p=qsub.add_parser("export"); p.add_argument("output"); p.add_argument("--after-hash")
    p=qsub.add_parser("inspect"); p.add_argument("path")
    p=qsub.add_parser("apply"); p.add_argument("path")
    return parser


def dispatch(args: argparse.Namespace) -> Any:
    """Dispatch parsed command arguments to the matching implementation."""
    store = _store(args); actor = args.actor
    if args.group == "project":
        if args.action == "init": store.initialize(); return store.check()
        return store.check()
    if args.group == "campaign":
        api=CampaignEngine(store)
        if args.action=="create": return api.create(args.goal,budget=parse_json_arg(args.budget_json,{}),policy=parse_json_arg(args.policy_json,{}),actor=actor)
        if args.action=="list": return api.list()
        if args.action=="branch": return api.branch(args.campaign_id,args.name,parent_branch_id=args.parent,actor=actor)
        if args.action=="status": return api.get(args.campaign_id)
        if args.action=="snapshot": return api.snapshot(args.campaign_id)
        if args.action=="plan": return api.plan_next(args.campaign_id,actor=actor)
        return getattr(api,args.action)(args.campaign_id,actor=actor)
    if args.group == "hypothesis":
        api=HypothesisLedger(store)
        if args.action=="create": return api.create(args.statement,args.scope_kind,args.scope_id,origin=args.origin,actor=actor).__dict__
        if args.action=="list": return [x.__dict__ for x in api.list(state=args.state,scope_id=args.scope_id)]
        if args.action=="show": return api.describe(args.hypothesis_id)
        if args.action=="dependency": api.add_dependency(args.hypothesis_id,args.depends_on_id,actor=actor); return api.describe(args.hypothesis_id)
        if args.action=="evidence": return api.attach_evidence(args.hypothesis_id,args.evidence_id,stance=args.stance,weight=args.weight,evidence_kind=args.kind,independence_group=args.group,artifact_sha256=args.artifact_sha256,details=parse_json_arg(args.details_json,{}),actor=actor)
        if args.action=="transition": return api.transition(args.hypothesis_id,args.state,reason=args.reason,actor=actor,lock=args.lock).__dict__
        return api.acceptance_gate(args.hypothesis_id)
    if args.group == "candidate":
        api=CandidateStore(store)
        if args.action=="create": cid=api.create(args.branch_name,campaign_id=args.campaign_id,parent_candidate_id=args.parent,objective=parse_json_arg(args.objective_json,{}),actor=actor); return api.get(cid)
        if args.action=="add-file": return api.add_file(args.candidate_id,args.source,args.relative_path,actor=actor)
        if args.action=="evaluate": eid=api.record_evaluation(args.candidate_id,args.metric,args.status,value=args.value,details=parse_json_arg(args.details_json,{}),actor=actor); return {"evaluation_id":eid,"candidate":api.get(args.candidate_id)}
        if args.action=="compare": return api.compare(args.left_id,args.right_id)
        if args.action=="transition": return api.transition(args.candidate_id,args.state,reason=args.reason,actor=actor)
        if args.action=="show": return api.get(args.candidate_id)
        return api.list(campaign_id=args.campaign_id)
    if args.group == "counterexample":
        api=CounterexampleStore(store)
        if args.action=="add": cid=api.add(args.scope_kind,args.scope_id,args.payload,predicate=parse_json_arg(args.predicate_json,{}),provenance=parse_json_arg(args.provenance_json,{}),actor=actor); return api.get(cid)
        if args.action=="show": return api.get(args.counterexample_id)
        if args.action=="list": return api.list()
        return api.promote_to_regression(args.counterexample_id,args.destination,actor=actor)
    if args.group == "consensus":
        api=ConsensusEngine(store)
        if args.action=="record": oid=api.record(args.subject_kind,args.subject_id,args.property_name,parse_json_arg(args.value_json,None),adapter_name=args.adapter,adapter_version=args.adapter_version,evidence_id=args.evidence_id,independence_group=args.group,confidence=args.confidence,actor=actor); return {"observation_id":oid}
        if args.action=="scan": return api.scan(subject_kind=args.subject_kind,subject_id=args.subject_id)
        if args.action=="conflicts": return api.conflicts()
        if args.action=="resolve": rid=api.resolve(args.subject_kind,args.subject_id,args.property_name,parse_json_arg(args.selected_value_json,None),method=args.method,rationale=args.rationale,actor=actor,lock=args.lock); return {"resolution_id":rid}
        return api.explain(args.subject_kind,args.subject_id,args.property_name)
    if args.group == "graph":
        api=KnowledgeGraph(store)
        if args.action=="node": return api.upsert_node(args.node_id,args.kind,args.label,attributes=parse_json_arg(args.attributes_json,{}),actor=actor)
        if args.action=="edge": return {"edge_id":api.add_edge(args.source_id,args.target_id,args.relation,attributes=parse_json_arg(args.attributes_json,{}),actor=actor)}
        return api.impact(args.node_id,direction=args.direction,max_depth=args.max_depth,relations=set(args.relations.split(",")) if args.relations else None)
    if args.group == "review":
        api=ReviewQueue(store)
        if args.action=="create": rid=api.create(args.kind,args.subject_id,args.summary,priority=args.priority,details=parse_json_arg(args.details_json,{}),actor=actor); return api.get(rid)
        if args.action=="list": return api.list(status=args.status,limit=args.limit)
        if args.action=="show": return api.get(args.review_id)
        if args.action=="assign": return api.assign(args.review_id,args.assignee,actor=actor)
        if args.action=="decide": return api.decide(args.review_id,args.decision,args.rationale,actor=actor,lock=args.lock)
        return api.lock(args.review_id,actor=actor)
    if args.group == "family":
        api=BinaryFamilyStore(store)
        if args.action=="create": return api.create(args.name,actor=actor)
        if args.action=="add": return api.add(args.family_id,args.label,args.path,metadata=parse_json_arg(args.metadata_json,{}),actor=actor)
        if args.action=="correlate": return api.correlate(args.left_member_id,args.right_member_id,block_size=args.block_size,actor=actor)
        return api.report(args.family_id)
    if args.group == "proof":
        ledger=ProofLedger(store)
        if args.action=="obligation": return ledger.create_obligation(args.scope_kind,args.scope_id,args.property_name,args.required_status,assumptions=parse_json_arg(args.assumptions_json,[]),actor=actor)
        if args.action=="result": return ledger.add_result(args.obligation_id,args.status,args.validator,parse_json_arg(args.report_json,{}),artifact_sha256=args.artifact_sha256,actor=actor)
        if args.action=="evaluate": return ledger.evaluate(args.obligation_id)
        if args.action=="export": return ProofBundle.export(store,args.output,include_paths=args.include)
        if args.action=="verify": return ProofBundle.verify(args.path)
        return ProofBundle.inspect(args.path)
    if args.group == "worker":
        api=WorkerRegistry(store)
        if args.action=="register": return api.register(args.name,parse_json_arg(args.capabilities_json,{}),endpoint=args.endpoint,environment_sha256=args.environment_sha256,actor=actor)
        if args.action=="list": return api.list(status=args.status)
        if args.action=="doctor": return api.doctor(args.worker_id)
        if args.action=="status": return api.set_status(args.worker_id,args.status,actor=actor)
        return api.select(parse_json_arg(args.required_json,{}))
    if args.group == "plugin":
        api=PluginRegistry(store)
        if args.action=="validate": return api.validate_manifest(json.loads(Path(args.manifest).read_text()))
        if args.action=="install": return api.install(args.manifest,actor=actor)
        if args.action=="list": return api.list()
        if args.action=="doctor": return api.doctor(args.plugin_id)
        return api.invoke(args.plugin_id,args.capability,parse_json_arg(args.request_json,{}),timeout_seconds=args.timeout,actor=actor)
    if args.group == "changeset":
        if args.action=="export": return ChangeSet.export(store,args.output,after_hash=args.after_hash)
        if args.action=="inspect": return ChangeSet.inspect(args.path)
        return ChangeSet.apply(store,args.path,actor=actor)
    raise ContractError("unhandled command")


def main(argv: list[str] | None = None) -> int:
    """Run the governance command-line entry point and return its exit status.

    Delegates to :func:`x86decomp.cli_utils.run_cli`, which builds the parser,
    parses ``argv``, dispatches the command, emits the JSON result, and reports
    expected user-facing errors as a structured diagnostic with exit code ``2``.

    Args:
        argv: Argument vector to parse, or ``None`` to use ``sys.argv[1:]``.

    Returns:
        ``0`` on success, or ``2`` when an expected error is reported.
    """
    return run_cli(build_parser, dispatch, argv)


if __name__ == "__main__":
    raise SystemExit(main())
