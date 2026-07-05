"""Provide x86decomp.governance.workers functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import json
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, random_id, utc_now
from .store import GovernanceStore

WORKER_STATES = {"active", "draining", "offline", "unhealthy"}


class WorkerRegistry:
    """Represent worker registry state and behavior.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    def __init__(self, store: GovernanceStore):
        """Initialize the instance with the supplied constructor arguments.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.store = store
        self.store.initialize()

    def register(self, name: str, capabilities: dict[str, Any], *, endpoint: str | None = None, environment_sha256: str | None = None, actor: str = "analyst") -> dict[str, Any]:
        """Register the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if environment_sha256 is not None and len(environment_sha256) != 64:
            raise ContractError("environment_sha256 must be a 64-character digest")
        if not isinstance(capabilities, dict) or not capabilities:
            raise ContractError("worker capabilities must be a non-empty object")
        worker_id = random_id("worker")
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO governance_worker_profiles(worker_id,name,endpoint,status,capabilities_json,environment_sha256,updated_at) VALUES(?,?,?,?,?,?,?)",
                (worker_id, name, endpoint, "active", canonical_json(capabilities), environment_sha256, utc_now()),
            )
            self.store.audit(actor, "worker.register", worker_id, {"name": name, "endpoint": endpoint, "capabilities": capabilities, "environment_sha256": environment_sha256}, connection=connection)
        return self.get(worker_id)

    def get(self, worker_id: str) -> dict[str, Any]:
        """Return the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.connect() as connection:
            row = connection.execute("SELECT * FROM governance_worker_profiles WHERE worker_id=?", (worker_id,)).fetchone()
        if not row:
            raise KeyError(worker_id)
        result = dict(row)
        result["capabilities"] = json.loads(result.pop("capabilities_json"))
        return result

    def list(self, *, status: str | None = None) -> list[dict[str, Any]]:
        """List the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if status and status not in WORKER_STATES:
            raise ContractError(f"invalid worker status: {status}")
        where, args = (" WHERE status=?", [status]) if status else ("", [])
        with self.store.connect() as connection:
            ids = [r[0] for r in connection.execute(f"SELECT worker_id FROM governance_worker_profiles{where} ORDER BY name", args).fetchall()]
        return [self.get(item) for item in ids]

    def select(self, required: dict[str, Any]) -> dict[str, Any]:
        """Select the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        candidates = []
        for worker in self.list(status="active"):
            capabilities = worker["capabilities"]
            if all(capabilities.get(key) == value or (isinstance(value, list) and all(v in capabilities.get(key, []) for v in value)) for key, value in required.items()):
                candidates.append(worker)
        if not candidates:
            raise ContractError("no active worker satisfies required capabilities")
        return sorted(candidates, key=lambda item: item["name"])[0]

    def set_status(self, worker_id: str, status: str, *, actor: str = "analyst") -> dict[str, Any]:
        """Set status.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if status not in WORKER_STATES:
            raise ContractError(f"invalid worker status: {status}")
        current = self.get(worker_id)
        with self.store.transaction() as connection:
            connection.execute("UPDATE governance_worker_profiles SET status=?,updated_at=? WHERE worker_id=?", (status, utc_now(), worker_id))
            self.store.audit(actor, "worker.status", worker_id, {"old": current["status"], "new": status}, connection=connection)
        return self.get(worker_id)

    def doctor(self, worker_id: str) -> dict[str, Any]:
        """Implement doctor.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        worker = self.get(worker_id)
        failures = []
        if worker["endpoint"] and not (worker["endpoint"].startswith("https://") or worker["endpoint"].startswith("unix://")):
            failures.append("remote endpoint must use https:// or unix://")
        if not worker["environment_sha256"]:
            failures.append("worker environment is not hash-pinned")
        return {"worker_id": worker_id, "passed": not failures, "failures": failures, "status": worker["status"], "capabilities": worker["capabilities"]}
