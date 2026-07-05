"""Provide x86decomp.governance.hypotheses functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, random_id, utc_now, validate_id
from .store import GovernanceStore

STATES = {
    "proposed",
    "scheduled",
    "testing",
    "supported",
    "contradicted",
    "accepted",
    "rejected",
    "superseded",
    "blocked",
}

_ALLOWED_TRANSITIONS = {
    "proposed": {"scheduled", "testing", "rejected", "superseded", "blocked"},
    "scheduled": {"testing", "proposed", "rejected", "superseded", "blocked"},
    "testing": {"supported", "contradicted", "scheduled", "blocked"},
    "supported": {"accepted", "testing", "contradicted", "rejected", "superseded", "blocked"},
    "contradicted": {"rejected", "testing", "superseded", "blocked"},
    "accepted": {"testing", "contradicted", "superseded", "blocked"},
    "rejected": {"testing", "superseded"},
    "superseded": set(),
    "blocked": {"proposed", "scheduled", "testing", "supported", "contradicted", "rejected"},
}


@dataclass(frozen=True)
class Hypothesis:
    """Store the validated fields for hypothesis records.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    hypothesis_id: str
    statement: str
    scope_kind: str
    scope_id: str
    state: str
    confidence: float
    origin: str
    locked: bool
    created_at: str
    updated_at: str
    disposition_reason: str | None


def _row_to_hypothesis(row: sqlite3.Row) -> Hypothesis:
    """Implement row to hypothesis.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    return Hypothesis(
        hypothesis_id=row["hypothesis_id"],
        statement=row["statement"],
        scope_kind=row["scope_kind"],
        scope_id=row["scope_id"],
        state=row["state"],
        confidence=float(row["confidence"]),
        origin=row["origin"],
        locked=bool(row["locked"]),
        created_at=row["created_at"],
        updated_at=row["updated_at"],
        disposition_reason=row["disposition_reason"],
    )


class HypothesisLedger:
    """Represent hypothesis ledger state and behavior.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    def __init__(self, store: GovernanceStore):
        """Initialize the instance with the supplied constructor arguments.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.store = store
        self.store.initialize()

    def create(
        self,
        statement: str,
        scope_kind: str,
        scope_id: str,
        *,
        origin: str,
        actor: str = "system",
        hypothesis_id: str | None = None,
    ) -> Hypothesis:
        """Create the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if not statement.strip():
            raise ContractError("hypothesis statement must not be empty")
        hypothesis_id = validate_id(hypothesis_id or random_id("hyp"), field="hypothesis_id")
        now = utc_now()
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO governance_hypotheses(hypothesis_id,statement,scope_kind,scope_id,state,confidence,origin,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?)",
                (hypothesis_id, statement.strip(), scope_kind, scope_id, "proposed", 0.5, origin, now, now),
            )
            self.store.audit(actor, "hypothesis.create", hypothesis_id, {"statement": statement, "scope_kind": scope_kind, "scope_id": scope_id, "origin": origin}, connection=connection)
        return self.get(hypothesis_id)

    def get(self, hypothesis_id: str) -> Hypothesis:
        """Return the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.connect() as connection:
            row = connection.execute("SELECT * FROM governance_hypotheses WHERE hypothesis_id=?", (hypothesis_id,)).fetchone()
        if not row:
            raise KeyError(hypothesis_id)
        return _row_to_hypothesis(row)

    def list(self, *, state: str | None = None, scope_id: str | None = None) -> list[Hypothesis]:
        """List the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        clauses: list[str] = []
        args: list[Any] = []
        if state:
            if state not in STATES:
                raise ContractError(f"unknown hypothesis state: {state}")
            clauses.append("state=?")
            args.append(state)
        if scope_id:
            clauses.append("scope_id=?")
            args.append(scope_id)
        where = f" WHERE {' AND '.join(clauses)}" if clauses else ""
        with self.store.connect() as connection:
            rows = connection.execute(f"SELECT * FROM governance_hypotheses{where} ORDER BY created_at,hypothesis_id", args).fetchall()
        return [_row_to_hypothesis(row) for row in rows]

    def add_dependency(self, hypothesis_id: str, depends_on_id: str, *, actor: str = "system") -> None:
        """Add dependency.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if hypothesis_id == depends_on_id:
            raise ContractError("a hypothesis cannot depend on itself")
        self.get(hypothesis_id)
        self.get(depends_on_id)
        with self.store.transaction() as connection:
            connection.execute("INSERT OR IGNORE INTO governance_hypothesis_dependencies(hypothesis_id,depends_on_id) VALUES(?,?)", (hypothesis_id, depends_on_id))
            if self._has_dependency_cycle(connection, hypothesis_id):
                raise ContractError("dependency would create a cycle")
            self.store.audit(actor, "hypothesis.dependency.add", hypothesis_id, {"depends_on_id": depends_on_id}, connection=connection)

    def _has_dependency_cycle(self, connection: sqlite3.Connection, start_id: str) -> bool:
        """Implement has dependency cycle.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        row = connection.execute(
            "WITH RECURSIVE deps(id) AS ("
            " SELECT depends_on_id FROM governance_hypothesis_dependencies WHERE hypothesis_id=?"
            " UNION"
            " SELECT d.depends_on_id FROM governance_hypothesis_dependencies d JOIN deps ON d.hypothesis_id=deps.id"
            ") SELECT 1 FROM deps WHERE id=? LIMIT 1",
            (start_id, start_id),
        ).fetchone()
        return row is not None

    def attach_evidence(
        self,
        hypothesis_id: str,
        evidence_id: str,
        *,
        stance: str,
        weight: float,
        evidence_kind: str,
        independence_group: str,
        artifact_sha256: str | None = None,
        details: dict[str, Any] | None = None,
        actor: str = "system",
    ) -> dict[str, Any]:
        """Implement attach evidence.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if stance not in {"supports", "contradicts", "context"}:
            raise ContractError(f"invalid evidence stance: {stance}")
        if not 0.0 <= weight <= 1.0:
            raise ContractError("evidence weight must be in [0,1]")
        self.get(hypothesis_id)
        link_id = random_id("hev")
        now = utc_now()
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO governance_hypothesis_evidence(link_id,hypothesis_id,evidence_id,stance,weight,evidence_kind,independence_group,artifact_sha256,details_json,created_at) VALUES(?,?,?,?,?,?,?,?,?,?)",
                (link_id, hypothesis_id, evidence_id, stance, weight, evidence_kind, independence_group, artifact_sha256, canonical_json(details or {}), now),
            )
            confidence = self._recalculate_confidence(connection, hypothesis_id)
            connection.execute("UPDATE governance_hypotheses SET confidence=?,updated_at=? WHERE hypothesis_id=?", (confidence, now, hypothesis_id))
            self.store.audit(actor, "hypothesis.evidence.attach", hypothesis_id, {"evidence_id": evidence_id, "stance": stance, "weight": weight, "evidence_kind": evidence_kind, "independence_group": independence_group, "confidence": confidence}, connection=connection)
        return {"link_id": link_id, "confidence": confidence}

    def _recalculate_confidence(self, connection: sqlite3.Connection, hypothesis_id: str) -> float:
        """Implement recalculate confidence.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        rows = connection.execute("SELECT stance,weight,independence_group FROM governance_hypothesis_evidence WHERE hypothesis_id=?", (hypothesis_id,)).fetchall()
        group_support: dict[str, float] = {}
        group_contradiction: dict[str, float] = {}
        for row in rows:
            group = row["independence_group"]
            if row["stance"] == "supports":
                group_support[group] = max(group_support.get(group, 0.0), float(row["weight"]))
            elif row["stance"] == "contradicts":
                group_contradiction[group] = max(group_contradiction.get(group, 0.0), float(row["weight"]))
        support = sum(group_support.values())
        contradiction = sum(group_contradiction.values())
        # Bayesian-like bounded score with a neutral prior. Independence groups are
        # collapsed so correlated reports cannot inflate confidence by duplication.
        score = (1.0 + support) / (2.0 + support + contradiction)
        return round(min(0.999999, max(0.000001, score)), 6)

    def transition(self, hypothesis_id: str, new_state: str, *, reason: str, actor: str = "analyst", lock: bool | None = None) -> Hypothesis:
        """Implement transition.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if new_state not in STATES:
            raise ContractError(f"unknown hypothesis state: {new_state}")
        current = self.get(hypothesis_id)
        if current.locked and actor == "automation":
            raise ContractError("locked hypothesis cannot be changed by automation")
        if new_state != current.state and new_state not in _ALLOWED_TRANSITIONS[current.state]:
            raise ContractError(f"invalid transition {current.state!r} -> {new_state!r}")
        if new_state == "accepted":
            gate = self.acceptance_gate(hypothesis_id)
            if not gate["passed"]:
                raise ContractError("hypothesis acceptance gate failed: " + "; ".join(gate["failures"]))
        locked = current.locked if lock is None else bool(lock)
        now = utc_now()
        with self.store.transaction() as connection:
            connection.execute(
                "UPDATE governance_hypotheses SET state=?,disposition_reason=?,locked=?,updated_at=? WHERE hypothesis_id=?",
                (new_state, reason, int(locked), now, hypothesis_id),
            )
            self.store.audit(actor, "hypothesis.transition", hypothesis_id, {"old_state": current.state, "new_state": new_state, "reason": reason, "locked": locked}, connection=connection)
        return self.get(hypothesis_id)

    def acceptance_gate(self, hypothesis_id: str) -> dict[str, Any]:
        """Implement acceptance gate.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.get(hypothesis_id)
        with self.store.connect() as connection:
            evidence = connection.execute("SELECT * FROM governance_hypothesis_evidence WHERE hypothesis_id=?", (hypothesis_id,)).fetchall()
            deps = connection.execute(
                "SELECT h.hypothesis_id,h.state FROM governance_hypothesis_dependencies d JOIN governance_hypotheses h ON h.hypothesis_id=d.depends_on_id WHERE d.hypothesis_id=?",
                (hypothesis_id,),
            ).fetchall()
        support_groups = {row["independence_group"] for row in evidence if row["stance"] == "supports"}
        support_kinds = {row["evidence_kind"] for row in evidence if row["stance"] == "supports"}
        contradictions = [row["evidence_id"] for row in evidence if row["stance"] == "contradicts"]
        failures: list[str] = []
        if len(support_groups) < 3:
            failures.append("fewer than three independent supporting evidence groups")
        if len(support_kinds) < 2:
            failures.append("fewer than two supporting evidence kinds")
        if contradictions:
            failures.append("unresolved contradictory evidence: " + ", ".join(contradictions))
        unresolved_dependencies = [row["hypothesis_id"] for row in deps if row["state"] != "accepted"]
        if unresolved_dependencies:
            failures.append("dependencies not accepted: " + ", ".join(unresolved_dependencies))
        invalid_hashes = [row["evidence_id"] for row in evidence if row["artifact_sha256"] is not None and len(row["artifact_sha256"]) != 64]
        if invalid_hashes:
            failures.append("invalid artifact hashes: " + ", ".join(invalid_hashes))
        return {
            "passed": not failures,
            "failures": failures,
            "support_groups": sorted(support_groups),
            "support_kinds": sorted(support_kinds),
            "contradictions": contradictions,
            "dependencies": [{"hypothesis_id": row["hypothesis_id"], "state": row["state"]} for row in deps],
        }

    def describe(self, hypothesis_id: str) -> dict[str, Any]:
        """Implement describe.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        hypothesis = self.get(hypothesis_id)
        with self.store.connect() as connection:
            evidence = [dict(row) for row in connection.execute("SELECT * FROM governance_hypothesis_evidence WHERE hypothesis_id=? ORDER BY created_at", (hypothesis_id,)).fetchall()]
            dependencies = [row[0] for row in connection.execute("SELECT depends_on_id FROM governance_hypothesis_dependencies WHERE hypothesis_id=? ORDER BY depends_on_id", (hypothesis_id,)).fetchall()]
        for row in evidence:
            row["details"] = json.loads(row.pop("details_json"))
        return {"hypothesis": hypothesis.__dict__, "evidence": evidence, "dependencies": dependencies, "acceptance_gate": self.acceptance_gate(hypothesis_id)}
