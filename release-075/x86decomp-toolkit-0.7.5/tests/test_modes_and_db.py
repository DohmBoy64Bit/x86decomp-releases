from pathlib import Path

import pytest

from x86decomp.analysis_db import AnalysisDatabase
from x86decomp.errors import ContractError
from x86decomp.workflow import DecompilationMode, MatchingStatus, initialize_function_workflow, update_function_workflow
from x86decomp.project import initialize_project
from pe_fixture import build_minimal_pe32


def test_independent_modes_and_monotonic_state(tmp_path: Path) -> None:
    project = tmp_path / "p"
    initialize_project(build_minimal_pe32(tmp_path / "a.exe"), project)
    state = initialize_function_workflow(project, rva=0x1000, modes={DecompilationMode.MATCHING, DecompilationMode.FUNCTIONAL})
    assert state.matching_status.value == "not_started"
    state = update_function_workflow(project, state.function_id, matching_status=MatchingStatus.COMPILES)
    assert state.matching_status == MatchingStatus.COMPILES
    assert state.functional_status.value == "not_started"
    with pytest.raises(ContractError):
        update_function_workflow(project, state.function_id, matching_status=MatchingStatus.DECOMPILED)


def test_type_constraint_conflict_gate(tmp_path: Path) -> None:
    with AnalysisDatabase(tmp_path / "a.db") as db:
        first = db.add_type_constraint(subject_entity="f", relation="return_type", object_value="int", provenance="ghidra")
        db.add_type_constraint(subject_entity="f", relation="return_type", object_value="float", provenance="compiler")
        assert len(db.detect_constraint_conflicts("f", "return_type")) == 2
        with pytest.raises(ContractError):
            db.accept_constraint(first)
