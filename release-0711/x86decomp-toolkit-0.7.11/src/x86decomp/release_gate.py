"""Target release acceptance gate.

The gate aggregates exact project-state, evidence, workflow, pipeline,
reproducibility, security, and image-convergence records.  It never upgrades a
missing report into a pass and never treats the three-source rule as a guarantee
of semantic truth.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

from .evidence import EvidenceStore
from .project_state import check_project_state
from .reproducibility import verify_reproduction_manifest
from .target_pack import verify_target_pack
from .util import load_json, utc_now, write_json

_MATCHING_ORDER = (
    "not_started", "decompiled", "compiles", "abi_compatible", "instruction_similar",
    "byte_matched", "image_integrated", "full_relink_validated",
)
_FUNCTIONAL_ORDER = (
    "not_started", "decompiled", "compiles", "abi_compatible", "differentially_validated",
    "symbolically_bounded", "integration_validated",
)


def _workflow_gate(root: Path, acceptance: dict[str, Any]) -> dict[str, Any]:
    """Evaluate workflow acceptance evidence required by the release gate."""
    matching_minimum = acceptance.get("matching", {}).get("minimum_state", "byte_matched")
    functional_minimum = acceptance.get("functional", {}).get("minimum_state", "differentially_validated")
    matching_index = _MATCHING_ORDER.index(matching_minimum)
    functional_index = _FUNCTIONAL_ORDER.index(functional_minimum)
    failures: list[str] = []
    records: list[dict[str, Any]] = []
    for path in sorted((root / "functions").glob("pe-rva_*/workflow.json")):
        workflow = load_json(path)
        function_id = workflow.get("function_id", path.parent.name)
        mode_values = workflow.get("modes", {})
        record = {"function_id": function_id, "matching": None, "functional": None}
        if "matching" in mode_values:
            status = mode_values["matching"].get("status", "not_started")
            record["matching"] = status
            if status == "blocked" or status not in _MATCHING_ORDER or _MATCHING_ORDER.index(status) < matching_index:
                failures.append(f"{function_id}: matching status {status!r} is below {matching_minimum!r}")
        if "functional" in mode_values:
            status = mode_values["functional"].get("status", "not_started")
            record["functional"] = status
            if status == "blocked" or status not in _FUNCTIONAL_ORDER or _FUNCTIONAL_ORDER.index(status) < functional_index:
                failures.append(f"{function_id}: functional status {status!r} is below {functional_minimum!r}")
        records.append(record)
    return {
        "matching_minimum": matching_minimum,
        "functional_minimum": functional_minimum,
        "workflow_count": len(records),
        "records": records,
        "failures": failures,
        "passed": not failures,
    }


def _claim_gate(root: Path) -> dict[str, Any]:
    """Claim gate."""
    store = EvidenceStore(root)
    results: list[dict[str, Any]] = []
    failures: list[str] = []
    for path in sorted(store.claims_dir.glob("*.json")):
        claim_id = path.stem
        result = store.verify_claim(claim_id)
        results.append(result)
        if result["state"] != "verified":
            failures.append(f"claim {claim_id} is {result['state']}: {', '.join(result['failures'])}")
    return {"claim_count": len(results), "results": results, "failures": failures, "passed": not failures}


def _pipeline_gate(root: Path) -> dict[str, Any]:
    """Evaluate persisted reconstruction-pipeline evidence required for release."""
    database = root / "orchestration" / "orchestrator.sqlite3"
    if not database.is_file():
        return {"pipeline_count": 0, "pipelines": [], "failures": [], "passed": True}
    connection = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        pipelines = [dict(row) for row in connection.execute("SELECT pipeline_id,status,manifest_sha256,updated_at FROM pipelines ORDER BY pipeline_id")]
    finally:
        connection.close()
    failures = [f"pipeline {item['pipeline_id']} is {item['status']}" for item in pipelines if item["status"] != "succeeded"]
    return {"pipeline_count": len(pipelines), "pipelines": pipelines, "failures": failures, "passed": not failures}


def evaluate_release_gate(
    project_root: Path,
    *,
    reproduction_manifest: Path | None = None,
    security_report: Path | None = None,
    convergence_report: Path | None = None,
    require_workflows: bool = False,
    require_verified_claims: bool = False,
    require_succeeded_pipelines: bool = False,
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Evaluate release gate."""
    root = project_root.resolve()
    checks: dict[str, Any] = {}
    failures: list[str] = []
    state = check_project_state(root).to_dict()
    checks["project_state"] = state
    if not state["valid"]:
        failures.extend(f"project state: {item}" for item in state["failures"])
    target_root = root / "target-pack"
    target = verify_target_pack(target_root) if (target_root / "target.toml").is_file() else {"valid": False, "failures": ["target pack missing"]}
    checks["target_pack"] = target
    if not target["valid"]:
        failures.extend(f"target pack: {item}" for item in target["failures"])
    acceptance_path = target_root / "acceptance.json"
    acceptance = load_json(acceptance_path) if acceptance_path.is_file() else {"matching": {}, "functional": {}}
    workflows = _workflow_gate(root, acceptance)
    checks["workflows"] = workflows
    if require_workflows and workflows["workflow_count"] == 0:
        failures.append("no function workflows exist")
    failures.extend(f"workflow: {item}" for item in workflows["failures"])
    claims = _claim_gate(root)
    checks["claims"] = claims
    if require_verified_claims and claims["claim_count"] == 0:
        failures.append("no claims exist")
    failures.extend(f"evidence: {item}" for item in claims["failures"])
    pipelines = _pipeline_gate(root)
    checks["pipelines"] = pipelines
    if require_succeeded_pipelines and pipelines["pipeline_count"] == 0:
        failures.append("no durable pipelines exist")
    if require_succeeded_pipelines:
        failures.extend(f"orchestration: {item}" for item in pipelines["failures"])
    if reproduction_manifest is not None:
        reproduction = verify_reproduction_manifest(root, reproduction_manifest)
        checks["reproduction"] = reproduction
        if not reproduction["reproducible"]:
            failures.extend(f"reproduction: {item}" for item in reproduction["failures"])
    if security_report is not None:
        security = load_json(security_report)
        checks["security"] = security
        if not security.get("passed", False):
            failures.append("security report did not pass")
    if convergence_report is not None:
        convergence = load_json(convergence_report)
        checks["convergence"] = convergence
        if not convergence.get("complete", False):
            failures.append("whole-image convergence is not complete")
    report = {
        "schema_version": 1,
        "kind": "target_release_gate",
        "created_at": utc_now(),
        "project_root": str(root),
        "checks": checks,
        "requirements": {
            "require_workflows": require_workflows,
            "require_verified_claims": require_verified_claims,
            "require_succeeded_pipelines": require_succeeded_pipelines,
            "reproduction_manifest_required": reproduction_manifest is not None,
            "security_report_required": security_report is not None,
            "convergence_report_required": convergence_report is not None,
        },
        "failures": failures,
        "passed": not failures,
        "truth_statement": "Passing means only that the declared project release contracts were satisfied; it is not proof of original-source recovery or universal semantic equivalence.",
    }
    if report_path is not None:
        write_json(report_path, report)
    return report
