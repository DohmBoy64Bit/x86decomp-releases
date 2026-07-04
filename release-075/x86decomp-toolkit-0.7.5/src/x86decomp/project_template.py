"""Grounded project-template generation from a verified target pack.

Templates create executable workflow/configuration surfaces, never fabricated
source code.  Unknown compiler, language, linker, or layout facts remain
explicitly unresolved and are not converted into fake profiles or build files.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .errors import ContractError
from .target_pack import load_target_pack, verify_target_pack
from .util import load_json, utc_now, write_json

_TEMPLATE_SCHEMA_VERSION = 1


def _artifact_roles(pack: dict[str, Any]) -> set[str]:
    return {str(item.get("role")) for item in pack.get("artifacts", []) if isinstance(item, dict)}


def derive_template_contract(target_pack: Path) -> dict[str, Any]:
    """Derive a target project shape only from recorded facts and decisions."""
    root = target_pack.resolve() if target_pack.is_dir() else target_pack.resolve().parent
    verification = verify_target_pack(root)
    if not verification["valid"]:
        raise ContractError("cannot derive a template from an invalid target pack")
    pack = load_target_pack(root)
    observations_path = root / "observations.json"
    observations = load_json(observations_path) if observations_path.is_file() else {"observations": {}}
    decisions = pack.get("decisions", {})
    roles = _artifact_roles(pack)
    preferred = decisions.get("preferred_mode", "both")
    modes = ["matching", "functional"] if preferred == "both" else [str(preferred)]
    source_language = str(decisions.get("source_language", "unknown"))
    compiler_known = all(str(decisions.get(key, "unknown")) != "unknown" for key in ("compiler_family", "compiler_version"))
    linker_known = str(decisions.get("linker_family", "unknown")) != "unknown"
    source_candidates = observations.get("observations", {}).get("source_language_candidates", [])
    matching = {
        "enabled": "matching" in modes,
        "hybrid_assembly_fallback": "matching" in modes,
        "object_comparison_ready": "coff_object" in roles,
        "linker_reconstruction_ready": {"linker_map", "coff_object"}.issubset(roles),
        "whole_image_comparison_ready": "rebuilt_image" in roles,
        "compiler_identity_confirmed": compiler_known,
        "linker_identity_confirmed": linker_known,
    }
    functional = {
        "enabled": "functional" in modes,
        "dynamic_harness_generation": "functional" in modes,
        "host_execution_authorized": bool(decisions.get("allow_host_execution", False)),
        "integration_scenarios_declared": False,
    }
    blockers: list[dict[str, str]] = []
    if matching["enabled"] and not compiler_known:
        blockers.append({"area": "matching", "fact": "compiler_identity", "reason": "compiler family/version is unknown"})
    if matching["enabled"] and not linker_known:
        blockers.append({"area": "matching", "fact": "linker_identity", "reason": "linker family is unknown"})
    if source_language == "unknown":
        blockers.append({"area": "candidate_generation", "fact": "source_language", "reason": "source language is unknown"})
    if functional["enabled"] and not functional["host_execution_authorized"]:
        blockers.append({"area": "functional", "fact": "host_execution_authorization", "reason": "native host execution was not authorized"})
    return {
        "schema_version": _TEMPLATE_SCHEMA_VERSION,
        "created_at": utc_now(),
        "target_id": pack["target_id"],
        "architecture": pack["architecture"],
        "image_kind": pack["image_kind"],
        "selected_modes": modes,
        "source_language_decision": source_language,
        "source_language_candidates": source_candidates,
        "matching": matching,
        "functional": functional,
        "artifact_roles": sorted(roles),
        "blockers": blockers,
        "truth_policy": {
            "generated_source_claimed": False,
            "compiler_inferred_without_evidence": False,
            "linker_inferred_without_evidence": False,
            "unknowns_preserved": True,
        },
    }


def _write_project_helper(path: Path) -> None:
    script = '''#!/usr/bin/env python3
"""Project-local helper for the generated x86decomp workflow."""
from __future__ import annotations
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "orchestration" / "pipelines" / "default.json"

def _x86decomp_command() -> list[str]:
    executable = shutil.which("x86decomp")
    if executable:
        return [executable]
    return [sys.executable, "-m", "x86decomp"]

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("check", "run", "status", "reproduce"))
    args = parser.parse_args()
    command = _x86decomp_command()
    if args.action == "check":
        command.extend(["project-check", str(ROOT)])
    elif args.action == "run":
        command.extend(["pipeline-run", str(ROOT), str(PIPELINE)])
    elif args.action == "status":
        manifest = json.loads(PIPELINE.read_text(encoding="utf-8"))
        command.extend(["pipeline-status", str(ROOT), manifest["pipeline_id"]])
    else:
        output = ROOT / "reports" / "reproducibility" / "manifest.json"
        command.extend(["reproduce-create", str(ROOT), str(output)])
    return subprocess.call(command, cwd=ROOT)

if __name__ == "__main__":
    raise SystemExit(main())
'''
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(script, encoding="utf-8")
    path.chmod(0o755)


def materialize_project_template(project_root: Path) -> dict[str, Any]:
    """Create a deterministic, non-fabricated project working layout."""
    root = project_root.resolve()
    target_pack = root / "target-pack"
    contract = derive_template_contract(target_pack)
    directories = (
        "src/matching",
        "src/functional",
        "src/asm",
        "include",
        "analysis/overrides",
        "compiler-profiles",
        "linker-layout",
        "tests/integration/scenarios",
        "tests/differential/harnesses",
        "reports/matching",
        "reports/functional",
        "reports/convergence",
        "reports/reproducibility",
        "scripts",
    )
    for directory in directories:
        (root / directory).mkdir(parents=True, exist_ok=True)
    write_json(root / "config" / "project-template.json", contract)
    write_json(
        root / "config" / "validation-policy.json",
        {
            "schema_version": 1,
            "matching": {
                "accept_only_with_validator_report": True,
                "byte_match_requires_relocation_scope": True,
                "whole_image_normalizations_must_be_declared": True,
            },
            "functional": {
                "accept_only_with_observation_scope": True,
                "symbolic_results_require_bounds": True,
                "integration_runs_require_explicit_execution_consent": True,
            },
            "evidence": {
                "verified_claim_minimum_independent_groups": 3,
                "contradictions_block_promotion": True,
            },
        },
    )
    _write_project_helper(root / "scripts" / "project.py")
    gitignore = """# Generated and local state\nbuild/\n.cache/\n*.pyc\n__pycache__/\n.pytest_cache/\n# User-owned proprietary toolchains are never committed\ntoolchains/\n# Original binaries/evidence remain local unless distribution is authorized\noriginal/*\n!original/.gitkeep\n"""
    (root / ".gitignore").write_text(gitignore, encoding="utf-8")
    (root / "original" / ".gitkeep").touch(exist_ok=True)
    next_steps = [
        "Run `python scripts/project.py check`.",
        "Resolve only facts listed in `config/project-template.json` blockers using evidence.",
        "Run `python scripts/project.py run`; missing adapters become explicit BLOCKED stages.",
    ]
    if contract["matching"]["linker_reconstruction_ready"]:
        next_steps.append("Generate a linker reconstruction plan from the supplied MAP and COFF evidence.")
    if contract["matching"]["whole_image_comparison_ready"]:
        next_steps.append("Run whole-image convergence against the supplied rebuilt image.")
    if contract["functional"]["enabled"]:
        next_steps.append("Declare ABI and pointer regions before generating differential harnesses.")
    write_json(root / "config" / "next-steps.json", {"schema_version": 1, "steps": next_steps})
    return {"project_root": str(root), "contract": contract, "directories_created": list(directories), "helper": "scripts/project.py"}
