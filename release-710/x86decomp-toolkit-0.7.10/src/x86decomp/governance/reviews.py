"""Provide the current runtime implementation for the `x86decomp.governance.reviews` module."""
from __future__ import annotations

import json
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, random_id, utc_now
from .store import GovernanceStore

REVIEW_STATES = {"open", "assigned", "accepted", "rejected", "needs_evidence", "superseded"}


class ReviewQueue:
    """Coordinate review queue behavior for the current toolkit workflow."""
    def __init__(self, store: GovernanceStore):
        """Initialize the instance with validated constructor state."""
        self.store = store
        self.store.initialize()

    def create(self, kind: str, subject_id: str, summary: str, *, priority: int = 50, details: dict[str, Any] | None = None, actor: str = "system") -> str:
        """Create create for the current toolkit workflow."""
        if not 0 <= priority <= 100:
            raise ContractError("review priority must be in [0,100]")
        review_id = random_id("rev")
        now = utc_now()
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO governance_review_items(review_id,kind,subject_id,priority,status,summary,details_json,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?)",
                (review_id, kind, subject_id, priority, "open", summary, canonical_json(details or {}), now, now),
            )
            self.store.audit(actor, "review.create", review_id, {"kind": kind, "subject_id": subject_id, "priority": priority, "summary": summary}, connection=connection)
        return review_id

    def assign(self, review_id: str, assignee: str, *, actor: str = "analyst") -> dict[str, Any]:
        """Execute the assign operation for the current toolkit workflow."""
        if not assignee.strip():
            raise ContractError("assignee must not be empty")
        now = utc_now()
        with self.store.transaction() as connection:
            row = connection.execute("SELECT * FROM governance_review_items WHERE review_id=?", (review_id,)).fetchone()
            if not row:
                raise KeyError(review_id)
            if row["status"] not in {"open", "assigned", "needs_evidence"}:
                raise ContractError(f"cannot assign review in state {row['status']}")
            connection.execute("UPDATE governance_review_items SET assigned_to=?,status='assigned',updated_at=? WHERE review_id=?", (assignee, now, review_id))
            self.store.audit(actor, "review.assign", review_id, {"assignee": assignee}, connection=connection)
        return self.get(review_id)

    def decide(self, review_id: str, decision: str, rationale: str, *, actor: str = "analyst", lock: bool = False) -> dict[str, Any]:
        """Execute the decide operation for the current toolkit workflow."""
        state_map = {"accept": "accepted", "reject": "rejected", "request_evidence": "needs_evidence", "supersede": "superseded"}
        if decision not in state_map:
            raise ContractError(f"invalid review decision: {decision}")
        if not rationale.strip():
            raise ContractError("review decision requires a rationale")
        now = utc_now()
        decision_id = random_id("rdec")
        with self.store.transaction() as connection:
            row = connection.execute("SELECT * FROM governance_review_items WHERE review_id=?", (review_id,)).fetchone()
            if not row:
                raise KeyError(review_id)
            if row["locked"] and actor == "automation":
                raise ContractError("locked review cannot be changed by automation")
            connection.execute(
                "INSERT INTO governance_review_decisions(decision_id,review_id,actor,decision,rationale,created_at) VALUES(?,?,?,?,?,?)",
                (decision_id, review_id, actor, decision, rationale, now),
            )
            connection.execute(
                "UPDATE governance_review_items SET status=?,locked=?,updated_at=? WHERE review_id=?",
                (state_map[decision], int(lock or bool(row["locked"])), now, review_id),
            )
            self.store.audit(actor, "review.decision", review_id, {"decision_id": decision_id, "decision": decision, "rationale": rationale, "locked": lock}, connection=connection)
        return self.get(review_id)

    def lock(self, review_id: str, *, actor: str = "analyst") -> dict[str, Any]:
        """Execute the lock operation for the current toolkit workflow."""
        with self.store.transaction() as connection:
            row = connection.execute("SELECT review_id FROM governance_review_items WHERE review_id=?", (review_id,)).fetchone()
            if not row:
                raise KeyError(review_id)
            connection.execute("UPDATE governance_review_items SET locked=1,updated_at=? WHERE review_id=?", (utc_now(), review_id))
            self.store.audit(actor, "review.lock", review_id, {}, connection=connection)
        return self.get(review_id)

    def get(self, review_id: str) -> dict[str, Any]:
        """Execute the get operation for the current toolkit workflow."""
        with self.store.connect() as connection:
            row = connection.execute("SELECT * FROM governance_review_items WHERE review_id=?", (review_id,)).fetchone()
            if not row:
                raise KeyError(review_id)
            decisions = [dict(item) for item in connection.execute("SELECT * FROM governance_review_decisions WHERE review_id=? ORDER BY created_at", (review_id,)).fetchall()]
        result = dict(row)
        result["details"] = json.loads(result.pop("details_json"))
        result["locked"] = bool(result["locked"])
        result["decisions"] = decisions
        return result

    def list(self, *, status: str | None = None, limit: int = 100) -> list[dict[str, Any]]:
        """Execute the list operation for the current toolkit workflow."""
        if status and status not in REVIEW_STATES:
            raise ContractError(f"invalid review status: {status}")
        if not 1 <= limit <= 1000:
            raise ContractError("limit must be in [1,1000]")
        where = " WHERE status=?" if status else ""
        args = [status] if status else []
        args.append(limit)
        with self.store.connect() as connection:
            rows = connection.execute(f"SELECT * FROM governance_review_items{where} ORDER BY priority DESC,created_at LIMIT ?", args).fetchall()
        result: list[dict[str, Any]] = []
        for row in rows:
            item = dict(row)
            item["details"] = json.loads(item.pop("details_json"))
            item["locked"] = bool(item["locked"])
            result.append(item)
        return result
