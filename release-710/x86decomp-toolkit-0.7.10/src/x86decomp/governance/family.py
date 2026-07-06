"""Provide the current runtime implementation for the `x86decomp.governance.family` module."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, random_id, sha256_file, utc_now
from .store import GovernanceStore


class BinaryFamilyStore:
    """Static, content-addressed related-binary correlation."""

    def __init__(self, store: GovernanceStore):
        """Initialize the instance with validated constructor state."""
        self.store = store
        self.store.initialize()
        self.root = self.store.project_root / "artifacts" / "governance" / "families"

    def create(self, name: str, *, actor: str = "analyst") -> dict[str, Any]:
        """Create create for the current toolkit workflow."""
        if not name.strip():
            raise ContractError("family name must not be empty")
        family_id = random_id("fam")
        with self.store.transaction() as connection:
            connection.execute("INSERT INTO governance_binary_families(family_id,name,created_at) VALUES(?,?,?)", (family_id, name.strip(), utc_now()))
            self.store.audit(actor, "family.create", family_id, {"name": name.strip()}, connection=connection)
        return self.get(family_id)

    def add(self, family_id: str, label: str, path: str | Path, *, metadata: dict[str, Any] | None = None, actor: str = "analyst") -> dict[str, Any]:
        """Execute the add operation for the current toolkit workflow."""
        source = Path(path).resolve()
        if not source.is_file() or source.is_symlink():
            raise ContractError("family member must be a regular non-symlink file")
        self.get(family_id)
        digest = sha256_file(source)
        destination = self.root / digest[:2] / digest
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.exists():
            destination.write_bytes(source.read_bytes())
        elif sha256_file(destination) != digest:
            raise ContractError("content store corruption")
        member_id = random_id("member")
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO governance_family_members(member_id,family_id,label,file_sha256,file_size,artifact_path,metadata_json,created_at) VALUES(?,?,?,?,?,?,?,?)",
                (member_id, family_id, label, digest, source.stat().st_size, destination.relative_to(self.store.project_root).as_posix(), canonical_json(metadata or {}), utc_now()),
            )
            self.store.audit(actor, "family.member.add", member_id, {"family_id": family_id, "label": label, "sha256": digest}, connection=connection)
        return self.member(member_id)

    @staticmethod
    def _block_fingerprints(data: bytes, block_size: int) -> set[bytes]:
        """Support block fingerprints processing for internal toolkit callers."""
        if block_size <= 0:
            raise ContractError("block_size must be positive")
        return {data[i:i + block_size] for i in range(0, len(data), block_size) if data[i:i + block_size]}

    def correlate(self, left_member_id: str, right_member_id: str, *, block_size: int = 64, actor: str = "system") -> dict[str, Any]:
        """Execute the correlate operation for the current toolkit workflow."""
        left, right = self.member(left_member_id), self.member(right_member_id)
        if left["family_id"] != right["family_id"]:
            raise ContractError("family members must belong to the same family")
        left_data = (self.store.project_root / left["artifact_path"]).read_bytes()
        right_data = (self.store.project_root / right["artifact_path"]).read_bytes()
        a, b = self._block_fingerprints(left_data, block_size), self._block_fingerprints(right_data, block_size)
        union = a | b
        score = 1.0 if not union else len(a & b) / len(union)
        details = {"block_size": block_size, "left_blocks": len(a), "right_blocks": len(b), "shared_blocks": len(a & b), "interpretation": "fixed-block Jaccard similarity; not function identity or semantic equivalence"}
        correlation_id = random_id("corr")
        ordered = sorted([left_member_id, right_member_id])
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO governance_family_correlations(correlation_id,family_id,left_member_id,right_member_id,algorithm,score,details_json,created_at) VALUES(?,?,?,?,?,?,?,?) "
                "ON CONFLICT(left_member_id,right_member_id,algorithm) DO UPDATE SET score=excluded.score,details_json=excluded.details_json,created_at=excluded.created_at",
                (correlation_id, left["family_id"], ordered[0], ordered[1], f"fixed-block-jaccard-{block_size}", score, canonical_json(details), utc_now()),
            )
            actual = connection.execute("SELECT correlation_id FROM governance_family_correlations WHERE left_member_id=? AND right_member_id=? AND algorithm=?", (ordered[0], ordered[1], f"fixed-block-jaccard-{block_size}")).fetchone()[0]
            self.store.audit(actor, "family.correlate", actual, {"left": ordered[0], "right": ordered[1], "score": score, "details": details}, connection=connection)
        return self.correlation(actual)

    def get(self, family_id: str) -> dict[str, Any]:
        """Execute the get operation for the current toolkit workflow."""
        with self.store.connect() as connection:
            row = connection.execute("SELECT * FROM governance_binary_families WHERE family_id=?", (family_id,)).fetchone()
        if not row:
            raise KeyError(family_id)
        return dict(row)

    def member(self, member_id: str) -> dict[str, Any]:
        """Execute the member operation for the current toolkit workflow."""
        with self.store.connect() as connection:
            row = connection.execute("SELECT * FROM governance_family_members WHERE member_id=?", (member_id,)).fetchone()
        if not row:
            raise KeyError(member_id)
        result = dict(row)
        result["metadata"] = json.loads(result.pop("metadata_json"))
        return result

    def correlation(self, correlation_id: str) -> dict[str, Any]:
        """Execute the correlation operation for the current toolkit workflow."""
        with self.store.connect() as connection:
            row = connection.execute("SELECT * FROM governance_family_correlations WHERE correlation_id=?", (correlation_id,)).fetchone()
        if not row:
            raise KeyError(correlation_id)
        result = dict(row)
        result["details"] = json.loads(result.pop("details_json"))
        return result

    def report(self, family_id: str) -> dict[str, Any]:
        """Execute the report operation for the current toolkit workflow."""
        family = self.get(family_id)
        with self.store.connect() as connection:
            family["members"] = [self.member(r[0]) for r in connection.execute("SELECT member_id FROM governance_family_members WHERE family_id=? ORDER BY label", (family_id,)).fetchall()]
            family["correlations"] = [self.correlation(r[0]) for r in connection.execute("SELECT correlation_id FROM governance_family_correlations WHERE family_id=? ORDER BY created_at", (family_id,)).fetchall()]
        family["non_claims"] = ["does not establish source identity", "does not establish semantic equivalence", "does not propagate facts without review"]
        return family
