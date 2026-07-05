"""Provide tests.test_workqueue functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from pathlib import Path

from x86decomp.work_queue import WorkQueue


def test_work_queue_requires_validators(tmp_path: Path) -> None:
    """Verify work queue requires validators.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    q = WorkQueue(tmp_path / "q.db")
    try:
        task = q.create(function_id="pe-rva:00001000", mode="matching", kind="source", instructions="Draft candidate", required_validators=["compile", "diff"])
        q.claim(task["id"], "agent")
        q.propose(task["id"], {"source": "x.c"}, ["e1"])
        assert q.record_validator(task["id"], "compile", "compile.json", True)["status"] == "validating"
        assert q.record_validator(task["id"], "diff", "diff.json", True)["status"] == "accepted"
    finally:
        q.close()
