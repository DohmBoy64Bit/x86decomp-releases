"""Provide tests.test_integration functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

from x86decomp.errors import ContractError
from x86decomp.integration import run_integration_scenarios


def _write_program(path: Path, expression: str) -> None:
    """Write program.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    path.write_text(
        "from pathlib import Path\n"
        "import sys\n"
        "value = sys.stdin.read().strip()\n"
        f"result = {expression}\n"
        "Path('result.txt').write_text(result + '\\n', encoding='utf-8')\n"
        "print(result)\n",
        encoding="utf-8",
    )


def _manifest(tmp_path: Path, candidate_expression: str) -> Path:
    """Implement manifest.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    tmp_path.mkdir(parents=True, exist_ok=True)
    target = tmp_path / "target.py"
    candidate = tmp_path / "candidate.py"
    _write_program(target, "value.upper()")
    _write_program(candidate, candidate_expression)
    manifest = tmp_path / "integration.json"
    manifest.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "name": "test",
                "execution": {
                    "mode": "host_explicit",
                    "acknowledge_untrusted_code_risk": True,
                },
                "scenarios": [
                    {
                        "id": "case",
                        "stdin": {"text": "hello"},
                        "target": {
                            "artifact": "target.py",
                            "command": [sys.executable, "{artifact}"],
                        },
                        "candidate": {
                            "artifact": "candidate.py",
                            "command": [sys.executable, "{artifact}"],
                        },
                        "observations": {
                            "exit_code": True,
                            "stdout": "exact",
                            "stderr": "exact",
                            "files": [{"path": "result.txt", "mode": "text"}],
                        },
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    return manifest


def test_integration_requires_explicit_host_consent(tmp_path: Path) -> None:
    """Verify integration requires explicit host consent.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    manifest = _manifest(tmp_path, "value.upper()")
    with pytest.raises(ContractError):
        run_integration_scenarios(manifest)


def test_integration_equivalence_and_difference(tmp_path: Path) -> None:
    """Verify integration equivalence and difference.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    equal_manifest = _manifest(tmp_path / "equal", "value.upper()")
    equal = run_integration_scenarios(equal_manifest, allow_host_execution=True)
    assert equal["all_scenarios_equivalent"]
    assert equal["passed_count"] == 1

    different_manifest = _manifest(tmp_path / "different", "value.lower()")
    different = run_integration_scenarios(different_manifest, allow_host_execution=True)
    assert not different["all_scenarios_equivalent"]
    assert any(not item["equal"] for item in different["scenarios"][0]["comparisons"])
