"""Compute and record governance consensus decisions."""
from __future__ import annotations

import json
from collections import defaultdict
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, random_id, utc_now
from .store import GovernanceStore


class ConsensusEngine:
    """Manage ConsensusEngine through `record`, `scan`, `conflicts`."""
    def __init__(self, store: GovernanceStore):
        """Initialize ConsensusEngine with `store`."""
        self.store = store
        self.store.initialize()

    def record(self, subject_kind: str, subject_id: str, property_name: str, value: Any, *, adapter_name: str, adapter_version: str, evidence_id: str, independence_group: str, confidence: float = 1.0, actor: str = "adapter") -> str:
        """Record data in consensus engine."""
        if not 0.0 <= confidence <= 1.0:
            raise ContractError("confidence must be in [0,1]")
        observation_id = random_id("obs")
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO governance_consensus_observations(observation_id,subject_kind,subject_id,property_name,value_json,adapter_name,adapter_version,evidence_id,independence_group,confidence,created_at) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                (observation_id, subject_kind, subject_id, property_name, canonical_json(value), adapter_name, adapter_version, evidence_id, independence_group, confidence, utc_now()),
            )
            self.store.audit(actor, "consensus.observation", observation_id, {"subject_kind": subject_kind, "subject_id": subject_id, "property_name": property_name, "value": value, "adapter_name": adapter_name, "adapter_version": adapter_version, "evidence_id": evidence_id, "independence_group": independence_group, "confidence": confidence}, connection=connection)
        return observation_id

    def scan(self, *, subject_kind: str | None = None, subject_id: str | None = None) -> list[dict[str, Any]]:
        """Scan consensus engine."""
        clauses: list[str] = []
        args: list[Any] = []
        if subject_kind:
            clauses.append("subject_kind=?")
            args.append(subject_kind)
        if subject_id:
            clauses.append("subject_id=?")
            args.append(subject_id)
        where = f" WHERE {' AND '.join(clauses)}" if clauses else ""
        with self.store.connect() as connection:
            rows = connection.execute(f"SELECT * FROM governance_consensus_observations{where} ORDER BY subject_kind,subject_id,property_name,created_at", args).fetchall()
        groups: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
        for row in rows:
            item = dict(row)
            item["value"] = json.loads(item.pop("value_json"))
            groups[(row["subject_kind"], row["subject_id"], row["property_name"])].append(item)
        results: list[dict[str, Any]] = []
        for key, observations in groups.items():
            values: dict[str, dict[str, Any]] = {}
            for item in observations:
                key_json = canonical_json(item["value"])
                record = values.setdefault(key_json, {"value": item["value"], "groups": {}, "adapters": []})
                record["groups"][item["independence_group"]] = max(record["groups"].get(item["independence_group"], 0.0), float(item["confidence"]))
                record["adapters"].append({"name": item["adapter_name"], "version": item["adapter_version"], "evidence_id": item["evidence_id"]})
            ranked = sorted(
                [
                    {"value": record["value"], "score": round(sum(record["groups"].values()), 6), "independence_groups": sorted(record["groups"]), "adapters": record["adapters"]}
                    for record in values.values()
                ],
                key=lambda item: (-item["score"], canonical_json(item["value"])),
            )
            results.append({
                "subject_kind": key[0],
                "subject_id": key[1],
                "property_name": key[2],
                "status": "agreement" if len(ranked) == 1 else "conflict",
                "ranked_values": ranked,
                "observation_count": len(observations),
            })
        return results

    def conflicts(self) -> list[dict[str, Any]]:
        """Return the conflicts for this ConsensusEngine."""
        return [item for item in self.scan() if item["status"] == "conflict"]

    def resolve(self, subject_kind: str, subject_id: str, property_name: str, selected_value: Any, *, method: str, rationale: str, actor: str = "analyst", lock: bool = False) -> str:
        """Resolve consensus engine data."""
        scans = [item for item in self.scan(subject_kind=subject_kind, subject_id=subject_id) if item["property_name"] == property_name]
        if not scans:
            raise ContractError("no observations exist for consensus subject")
        represented = {canonical_json(item["value"]) for item in scans[0]["ranked_values"]}
        if canonical_json(selected_value) not in represented:
            raise ContractError("selected resolution value was not observed")
        if method not in {"analyst", "evidence_weighted", "external_proof"}:
            raise ContractError("unsupported resolution method")
        resolution_id = random_id("res")
        with self.store.transaction() as connection:
            existing = connection.execute("SELECT * FROM governance_consensus_resolutions WHERE subject_kind=? AND subject_id=? AND property_name=? ORDER BY created_at DESC LIMIT 1", (subject_kind, subject_id, property_name)).fetchone()
            if existing and existing["locked"] and actor == "automation":
                raise ContractError("locked consensus resolution cannot be overwritten by automation")
            connection.execute(
                "INSERT INTO governance_consensus_resolutions(resolution_id,subject_kind,subject_id,property_name,selected_value_json,method,rationale,actor,locked,created_at) VALUES(?,?,?,?,?,?,?,?,?,?)",
                (resolution_id, subject_kind, subject_id, property_name, canonical_json(selected_value), method, rationale, actor, int(lock), utc_now()),
            )
            self.store.audit(actor, "consensus.resolve", resolution_id, {"subject_kind": subject_kind, "subject_id": subject_id, "property_name": property_name, "selected_value": selected_value, "method": method, "rationale": rationale, "locked": lock}, connection=connection)
        return resolution_id

    def explain(self, subject_kind: str, subject_id: str, property_name: str) -> dict[str, Any]:
        """Explain ConsensusEngine for ConsensusEngine."""
        scan = next((item for item in self.scan(subject_kind=subject_kind, subject_id=subject_id) if item["property_name"] == property_name), None)
        if not scan:
            raise KeyError((subject_kind, subject_id, property_name))
        with self.store.connect() as connection:
            rows = connection.execute("SELECT * FROM governance_consensus_resolutions WHERE subject_kind=? AND subject_id=? AND property_name=? ORDER BY created_at", (subject_kind, subject_id, property_name)).fetchall()
        resolutions: list[dict[str, Any]] = []
        for row in rows:
            item = dict(row)
            item["selected_value"] = json.loads(item.pop("selected_value_json"))
            item["locked"] = bool(item["locked"])
            resolutions.append(item)
        return {"analysis": scan, "resolutions": resolutions, "resolution": resolutions[-1] if resolutions else None}
