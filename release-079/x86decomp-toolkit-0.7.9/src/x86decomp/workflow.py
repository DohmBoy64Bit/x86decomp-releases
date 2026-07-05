"""Per-function decompilation mode and validation-state management.

The workflow intentionally keeps matching and functional progress independent.
A function can be byte matched but not functionally exercised, or behaviorally
validated without reproducing the original instruction stream.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import Path
from typing import Any

from .artifacts import function_id_from_rva
from .errors import ContractError
from .memory import ProjectMemory
from .util import load_json, utc_now, write_json


class DecompilationMode(StrEnum):
    """Enumerate the supported decompilation mode values.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    MATCHING = "matching"
    FUNCTIONAL = "functional"


class SourceStage(StrEnum):
    """Enumerate the supported source stage values.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    ORIGINAL_BYTES = "original_bytes"
    GENERATED_ASSEMBLY = "generated_assembly"
    DECOMPILER_CANDIDATE = "decompiler_candidate"
    HUMAN_CANDIDATE = "human_candidate"
    ACCEPTED_SOURCE = "accepted_source"


class MatchingStatus(StrEnum):
    """Enumerate the supported matching status values.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    NOT_STARTED = "not_started"
    DECOMPILED = "decompiled"
    COMPILES = "compiles"
    ABI_COMPATIBLE = "abi_compatible"
    INSTRUCTION_SIMILAR = "instruction_similar"
    BYTE_MATCHED = "byte_matched"
    IMAGE_INTEGRATED = "image_integrated"
    FULL_RELINK_VALIDATED = "full_relink_validated"
    BLOCKED = "blocked"


class FunctionalStatus(StrEnum):
    """Enumerate the supported functional status values.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    NOT_STARTED = "not_started"
    DECOMPILED = "decompiled"
    COMPILES = "compiles"
    ABI_COMPATIBLE = "abi_compatible"
    DIFFERENTIALLY_VALIDATED = "differentially_validated"
    SYMBOLICALLY_BOUNDED = "symbolically_bounded"
    INTEGRATION_VALIDATED = "integration_validated"
    BLOCKED = "blocked"


_MATCHING_ORDER = {value: index for index, value in enumerate(MatchingStatus)}
_FUNCTIONAL_ORDER = {value: index for index, value in enumerate(FunctionalStatus)}
# BLOCKED is not a monotonic completion step.
_MATCHING_ORDER[MatchingStatus.BLOCKED] = -1
_FUNCTIONAL_ORDER[FunctionalStatus.BLOCKED] = -1


@dataclass
class FunctionWorkflow:
    """Store the validated fields for function workflow records.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    function_id: str
    selected_modes: set[DecompilationMode] = field(
        default_factory=lambda: {DecompilationMode.MATCHING, DecompilationMode.FUNCTIONAL}
    )
    source_stage: SourceStage = SourceStage.ORIGINAL_BYTES
    matching_status: MatchingStatus = MatchingStatus.NOT_STARTED
    functional_status: FunctionalStatus = FunctionalStatus.NOT_STARTED
    active_candidate: str | None = None
    compiler_profile: str | None = None
    reports: dict[str, str] = field(default_factory=dict)
    blockers: list[str] = field(default_factory=list)
    updated_at: str = field(default_factory=utc_now)

    def to_dict(self) -> dict[str, Any]:
        """Convert dict.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        return {
            "schema_version": 2,
            "function_id": self.function_id,
            "selected_modes": sorted(mode.value for mode in self.selected_modes),
            "source_stage": self.source_stage.value,
            "matching_status": self.matching_status.value,
            "functional_status": self.functional_status.value,
            "active_candidate": self.active_candidate,
            "compiler_profile": self.compiler_profile,
            "reports": dict(sorted(self.reports.items())),
            "blockers": list(self.blockers),
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, value: Any) -> "FunctionWorkflow":
        """Build an object from dict.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if not isinstance(value, dict):
            raise ContractError("function workflow must be an object")
        function_id = value.get("function_id")
        if not isinstance(function_id, str) or not function_id.startswith("pe-rva:"):
            raise ContractError("invalid function_id in workflow")
        modes_raw = value.get("selected_modes", [])
        if not isinstance(modes_raw, list) or not modes_raw:
            raise ContractError("selected_modes must be a non-empty array")
        try:
            modes = {DecompilationMode(item) for item in modes_raw}
            return cls(
                function_id=function_id,
                selected_modes=modes,
                source_stage=SourceStage(value.get("source_stage", SourceStage.ORIGINAL_BYTES.value)),
                matching_status=MatchingStatus(
                    value.get("matching_status", MatchingStatus.NOT_STARTED.value)
                ),
                functional_status=FunctionalStatus(
                    value.get("functional_status", FunctionalStatus.NOT_STARTED.value)
                ),
                active_candidate=value.get("active_candidate"),
                compiler_profile=value.get("compiler_profile"),
                reports=dict(value.get("reports", {})),
                blockers=list(value.get("blockers", [])),
                updated_at=str(value.get("updated_at", utc_now())),
            )
        except (ValueError, TypeError) as exc:
            raise ContractError(f"invalid workflow enum or field: {exc}") from exc


def _state_path(project_root: Path, function_id: str) -> Path:
    """Implement state path.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    safe = function_id.replace(":", "_")
    return project_root.resolve() / "functions" / safe / "workflow.json"


def initialize_function_workflow(
    project_root: Path,
    *,
    function_id: str | None = None,
    rva: int | None = None,
    modes: set[DecompilationMode] | None = None,
) -> FunctionWorkflow:
    """Initialize function workflow.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if function_id is None:
        if rva is None:
            raise ContractError("function_id or rva is required")
        function_id = function_id_from_rva(rva)
    path = _state_path(project_root, function_id)
    if path.exists():
        raise ContractError(f"workflow already exists: {path}")
    workflow = FunctionWorkflow(function_id=function_id)
    if modes is not None:
        if not modes:
            raise ContractError("at least one decompilation mode is required")
        workflow.selected_modes = set(modes)
    path.parent.mkdir(parents=True, exist_ok=True)
    write_json(path, workflow.to_dict())
    ProjectMemory(project_root).append(
        actor="x86decomp",
        category="workflow",
        summary=f"Initialized function workflow for {function_id}.",
        details={"function_id": function_id, "modes": sorted(m.value for m in workflow.selected_modes)},
    )
    return workflow


def load_function_workflow(project_root: Path, function_id: str) -> FunctionWorkflow:
    """Load function workflow.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    path = _state_path(project_root, function_id)
    if not path.is_file():
        raise ContractError(f"missing function workflow: {path}")
    return FunctionWorkflow.from_dict(load_json(path))


def save_function_workflow(project_root: Path, workflow: FunctionWorkflow) -> None:
    """Save function workflow.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    workflow.updated_at = utc_now()
    write_json(_state_path(project_root, workflow.function_id), workflow.to_dict())


def update_function_workflow(
    project_root: Path,
    function_id: str,
    *,
    source_stage: SourceStage | None = None,
    matching_status: MatchingStatus | None = None,
    functional_status: FunctionalStatus | None = None,
    active_candidate: str | None = None,
    compiler_profile: str | None = None,
    report_kind: str | None = None,
    report_path: str | None = None,
    blocker: str | None = None,
    allow_regression: bool = False,
) -> FunctionWorkflow:
    """Update function workflow.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    workflow = load_function_workflow(project_root, function_id)
    if matching_status is not None:
        if DecompilationMode.MATCHING not in workflow.selected_modes:
            raise ContractError("matching status cannot change when matching mode is disabled")
        current = _MATCHING_ORDER[workflow.matching_status]
        requested = _MATCHING_ORDER[matching_status]
        if not allow_regression and requested >= 0 and current >= 0 and requested < current:
            raise ContractError("matching status regression requires allow_regression")
        workflow.matching_status = matching_status
    if functional_status is not None:
        if DecompilationMode.FUNCTIONAL not in workflow.selected_modes:
            raise ContractError("functional status cannot change when functional mode is disabled")
        current = _FUNCTIONAL_ORDER[workflow.functional_status]
        requested = _FUNCTIONAL_ORDER[functional_status]
        if not allow_regression and requested >= 0 and current >= 0 and requested < current:
            raise ContractError("functional status regression requires allow_regression")
        workflow.functional_status = functional_status
    if source_stage is not None:
        workflow.source_stage = source_stage
    if active_candidate is not None:
        workflow.active_candidate = active_candidate
    if compiler_profile is not None:
        workflow.compiler_profile = compiler_profile
    if report_kind is not None:
        if report_path is None:
            raise ContractError("report_path is required with report_kind")
        workflow.reports[report_kind] = report_path
    if blocker is not None and blocker not in workflow.blockers:
        workflow.blockers.append(blocker)
    save_function_workflow(project_root, workflow)
    ProjectMemory(project_root).append(
        actor="x86decomp",
        category="workflow",
        summary=f"Updated function workflow for {function_id}.",
        details=workflow.to_dict(),
    )
    return workflow
