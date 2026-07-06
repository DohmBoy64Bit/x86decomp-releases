"""Evidence-gated human/AI work queue with validator acceptance rules."""

from __future__ import annotations

import json
import sqlite3
import uuid
from pathlib import Path
from typing import Any

from .errors import ContractError
from .util import utc_now

_SCHEMA = """
CREATE TABLE IF NOT EXISTS tasks (
  id TEXT PRIMARY KEY,
  function_id TEXT NOT NULL,
  mode TEXT NOT NULL CHECK(mode IN ('matching','functional')),
  kind TEXT NOT NULL,
  status TEXT NOT NULL CHECK(status IN ('queued','claimed','proposed','validating','accepted','rejected','blocked')),
  priority INTEGER NOT NULL,
  instructions TEXT NOT NULL,
  assignee TEXT,
  proposal_json TEXT,
  required_validators_json TEXT NOT NULL,
  validator_results_json TEXT NOT NULL DEFAULT '{}',
  evidence_ids_json TEXT NOT NULL DEFAULT '[]',
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_tasks_status_priority ON tasks(status, priority DESC, created_at);
"""


class WorkQueue:
    """Coordinate work queue behavior for the current toolkit workflow."""
    def __init__(self, path: Path):
        """Initialize the instance with validated constructor state."""
        self.path = path.resolve()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(self.path)
        self.db.row_factory = sqlite3.Row
        self.db.executescript(_SCHEMA)

    def close(self) -> None:
        """Execute the close operation for the current toolkit workflow."""
        self.db.close()

    def create(
        self,
        *,
        function_id: str,
        mode: str,
        kind: str,
        instructions: str,
        required_validators: list[str],
        priority: int = 0,
    ) -> dict[str, Any]:
        """Create create for the current toolkit workflow."""
        if mode not in ("matching", "functional"):
            raise ContractError("task mode must be matching or functional")
        if not instructions.strip() or not required_validators:
            raise ContractError("task requires instructions and at least one validator")
        task_id = f"task-{uuid.uuid4().hex}"
        now = utc_now()
        self.db.execute(
            "INSERT INTO tasks VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (task_id, function_id, mode, kind, "queued", priority, instructions, None, None, json.dumps(required_validators), "{}", "[]", now, now),
        )
        self.db.commit()
        return self.get(task_id)

    def get(self, task_id: str) -> dict[str, Any]:
        """Execute the get operation for the current toolkit workflow."""
        row = self.db.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()
        if row is None:
            raise ContractError(f"work task does not exist: {task_id}")
        result = dict(row)
        for key in ("proposal_json", "required_validators_json", "validator_results_json", "evidence_ids_json"):
            result[key[:-5] if key.endswith("_json") else key] = None if result[key] is None else json.loads(result[key])
            del result[key]
        return result

    def claim(self, task_id: str, assignee: str) -> dict[str, Any]:
        """Execute the claim operation for the current toolkit workflow."""
        if not assignee.strip():
            raise ContractError("assignee is required")
        cursor = self.db.execute("UPDATE tasks SET status='claimed',assignee=?,updated_at=? WHERE id=? AND status='queued'", (assignee, utc_now(), task_id))
        if cursor.rowcount != 1:
            raise ContractError("task is not queued")
        self.db.commit()
        return self.get(task_id)

    def propose(self, task_id: str, proposal: dict[str, Any], evidence_ids: list[str]) -> dict[str, Any]:
        """Execute the propose operation for the current toolkit workflow."""
        if not evidence_ids:
            raise ContractError("proposal requires evidence_ids; AI output alone is not evidence")
        cursor = self.db.execute(
            "UPDATE tasks SET status='proposed',proposal_json=?,evidence_ids_json=?,updated_at=? WHERE id=? AND status='claimed'",
            (json.dumps(proposal, sort_keys=True), json.dumps(evidence_ids), utc_now(), task_id),
        )
        if cursor.rowcount != 1:
            raise ContractError("task must be claimed before proposal")
        self.db.commit()
        return self.get(task_id)

    def record_validator(self, task_id: str, validator: str, report_path: str, passed: bool) -> dict[str, Any]:
        """Record validator for the current toolkit workflow."""
        task = self.get(task_id)
        if task["status"] not in ("proposed", "validating"):
            raise ContractError("task must have a proposal before validation")
        results = task["validator_results"]
        results[validator] = {"report_path": report_path, "passed": bool(passed), "recorded_at": utc_now()}
        required = task["required_validators"]
        all_recorded = all(name in results for name in required)
        all_passed = all(results.get(name, {}).get("passed") is True for name in required)
        status = "accepted" if all_recorded and all_passed else "rejected" if all_recorded else "validating"
        self.db.execute("UPDATE tasks SET status=?,validator_results_json=?,updated_at=? WHERE id=?", (status, json.dumps(results, sort_keys=True), utc_now(), task_id))
        self.db.commit()
        return self.get(task_id)

    def next(self, *, mode: str | None = None) -> dict[str, Any] | None:
        """Execute the next operation for the current toolkit workflow."""
        if mode is not None and mode not in ("matching", "functional"):
            raise ContractError("mode must be matching or functional")
        if mode is None:
            row = self.db.execute("SELECT id FROM tasks WHERE status='queued' ORDER BY priority DESC,created_at LIMIT 1").fetchone()
        else:
            row = self.db.execute("SELECT id FROM tasks WHERE status='queued' AND mode=? ORDER BY priority DESC,created_at LIMIT 1", (mode,)).fetchone()
        return None if row is None else self.get(row["id"])
