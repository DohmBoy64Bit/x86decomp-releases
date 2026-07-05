"""Provide x86decomp.governance.candidates functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, ensure_relative_path, random_id, sha256_file, utc_now
from .store import GovernanceStore

CANDIDATE_STATES = {"active", "evaluating", "supported", "promoted", "discarded", "blocked"}


class CandidateStore:
    """Represent candidate store state and behavior.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    def __init__(self, store: GovernanceStore):
        """Initialize the instance with the supplied constructor arguments.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.store = store
        self.store.initialize()
        self.artifact_root = self.store.project_root / "artifacts" / "governance" / "sha256"

    def create(self, branch_name: str, *, campaign_id: str | None = None, parent_candidate_id: str | None = None, objective: dict[str, Any] | None = None, actor: str = "system") -> str:
        """Create the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if not branch_name.strip() or branch_name.startswith("/") or ".." in branch_name.split("/"):
            raise ContractError("invalid candidate branch name")
        if parent_candidate_id:
            self.get(parent_candidate_id)
        candidate_id = random_id("cand")
        now = utc_now()
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO governance_candidates(candidate_id,campaign_id,branch_name,parent_candidate_id,state,objective_json,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?)",
                (candidate_id, campaign_id, branch_name, parent_candidate_id, "active", canonical_json(objective or {}), now, now),
            )
            self.store.audit(actor, "candidate.create", candidate_id, {"branch_name": branch_name, "campaign_id": campaign_id, "parent_candidate_id": parent_candidate_id, "objective": objective or {}}, connection=connection)
        if parent_candidate_id:
            self._clone_files(parent_candidate_id, candidate_id, actor=actor)
        return candidate_id

    def _clone_files(self, parent_candidate_id: str, candidate_id: str, *, actor: str) -> None:
        """Implement clone files.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.transaction() as connection:
            rows = connection.execute("SELECT relative_path,content_sha256,size_bytes,artifact_path FROM governance_candidate_files WHERE candidate_id=?", (parent_candidate_id,)).fetchall()
            connection.executemany(
                "INSERT INTO governance_candidate_files(candidate_id,relative_path,content_sha256,size_bytes,artifact_path) VALUES(?,?,?,?,?)",
                [(candidate_id, row["relative_path"], row["content_sha256"], row["size_bytes"], row["artifact_path"]) for row in rows],
            )
            self.store.audit(actor, "candidate.clone_files", candidate_id, {"parent_candidate_id": parent_candidate_id, "file_count": len(rows)}, connection=connection)

    def add_file(self, candidate_id: str, source: str | Path, relative_path: str | Path, *, actor: str = "analyst") -> dict[str, Any]:
        """Add file.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.get(candidate_id)
        source_path = Path(source)
        if not source_path.is_file() or source_path.is_symlink():
            raise ContractError(f"candidate source must be a regular non-symlink file: {source_path}")
        relative = ensure_relative_path(relative_path).as_posix()
        digest = sha256_file(source_path)
        artifact = self.artifact_root / digest[:2] / digest[2:]
        artifact.parent.mkdir(parents=True, exist_ok=True)
        if artifact.exists():
            if sha256_file(artifact) != digest:
                raise ContractError(f"content-addressed artifact is corrupted: {artifact}")
        else:
            temp = artifact.with_suffix(".tmp")
            shutil.copyfile(source_path, temp)
            if sha256_file(temp) != digest:
                temp.unlink(missing_ok=True)
                raise ContractError("candidate artifact copy hash mismatch")
            temp.replace(artifact)
        size = source_path.stat().st_size
        now = utc_now()
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO governance_candidate_files(candidate_id,relative_path,content_sha256,size_bytes,artifact_path) VALUES(?,?,?,?,?) "
                "ON CONFLICT(candidate_id,relative_path) DO UPDATE SET content_sha256=excluded.content_sha256,size_bytes=excluded.size_bytes,artifact_path=excluded.artifact_path",
                (candidate_id, relative, digest, size, str(artifact.relative_to(self.store.project_root))),
            )
            connection.execute("UPDATE governance_candidates SET updated_at=? WHERE candidate_id=?", (now, candidate_id))
            self.store.audit(actor, "candidate.file.add", candidate_id, {"relative_path": relative, "content_sha256": digest, "size_bytes": size}, connection=connection)
        return {"candidate_id": candidate_id, "relative_path": relative, "content_sha256": digest, "size_bytes": size, "artifact_path": str(artifact)}

    def record_evaluation(self, candidate_id: str, metric: str, status: str, *, value: float | None = None, details: dict[str, Any] | None = None, actor: str = "validator") -> str:
        """Implement record evaluation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.get(candidate_id)
        if status not in {"pass", "fail", "unknown", "blocked"}:
            raise ContractError("evaluation status must be pass, fail, unknown, or blocked")
        evaluation_id = random_id("eval")
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO governance_candidate_evaluations(evaluation_id,candidate_id,metric,value,status,details_json,created_at) VALUES(?,?,?,?,?,?,?)",
                (evaluation_id, candidate_id, metric, value, status, canonical_json(details or {}), utc_now()),
            )
            state = "supported" if status == "pass" else "blocked" if status == "blocked" else "evaluating"
            connection.execute("UPDATE governance_candidates SET state=?,updated_at=? WHERE candidate_id=?", (state, utc_now(), candidate_id))
            self.store.audit(actor, "candidate.evaluation", candidate_id, {"evaluation_id": evaluation_id, "metric": metric, "value": value, "status": status, "details": details or {}}, connection=connection)
        return evaluation_id

    def compare(self, left_id: str, right_id: str) -> dict[str, Any]:
        """Compare the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        left = self.get(left_id)
        right = self.get(right_id)
        left_files = {row["relative_path"]: row for row in left["files"]}
        right_files = {row["relative_path"]: row for row in right["files"]}
        paths = sorted(set(left_files) | set(right_files))
        changes: list[dict[str, Any]] = []
        unchanged = 0
        for path in paths:
            left_row = left_files.get(path)
            right_row = right_files.get(path)
            if left_row and right_row and left_row["content_sha256"] == right_row["content_sha256"]:
                unchanged += 1
                continue
            changes.append({
                "relative_path": path,
                "left_sha256": left_row["content_sha256"] if left_row else None,
                "right_sha256": right_row["content_sha256"] if right_row else None,
                "change": "modified" if left_row and right_row else "removed" if left_row else "added",
            })
        return {"left": left_id, "right": right_id, "unchanged_files": unchanged, "changed_files": changes, "file_union_count": len(paths)}

    def transition(self, candidate_id: str, state: str, *, reason: str, actor: str = "analyst") -> dict[str, Any]:
        """Implement transition.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if state not in CANDIDATE_STATES:
            raise ContractError(f"invalid candidate state: {state}")
        current = self.get(candidate_id)
        allowed = {
            "active": {"evaluating", "supported", "discarded", "blocked"},
            "evaluating": {"supported", "active", "discarded", "blocked"},
            "supported": {"promoted", "evaluating", "discarded", "blocked"},
            "promoted": {"evaluating", "blocked"},
            "discarded": set(),
            "blocked": {"active", "evaluating", "supported", "discarded"},
        }
        if state != current["state"] and state not in allowed[current["state"]]:
            raise ContractError(f"invalid candidate transition {current['state']} -> {state}")
        if state == "promoted":
            passing = [item for item in current["evaluations"] if item["status"] == "pass"]
            failing = [item for item in current["evaluations"] if item["status"] == "fail"]
            if not passing or failing:
                raise ContractError("candidate promotion requires at least one passing evaluation and no failing evaluation")
        with self.store.transaction() as connection:
            connection.execute("UPDATE governance_candidates SET state=?,updated_at=? WHERE candidate_id=?", (state, utc_now(), candidate_id))
            self.store.audit(actor, "candidate.transition", candidate_id, {"old_state": current["state"], "new_state": state, "reason": reason}, connection=connection)
        return self.get(candidate_id)

    def get(self, candidate_id: str) -> dict[str, Any]:
        """Return the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.connect() as connection:
            row = connection.execute("SELECT * FROM governance_candidates WHERE candidate_id=?", (candidate_id,)).fetchone()
            if not row:
                raise KeyError(candidate_id)
            files = [dict(item) for item in connection.execute("SELECT * FROM governance_candidate_files WHERE candidate_id=? ORDER BY relative_path", (candidate_id,)).fetchall()]
            evaluations = [dict(item) for item in connection.execute("SELECT * FROM governance_candidate_evaluations WHERE candidate_id=? ORDER BY created_at", (candidate_id,)).fetchall()]
        result = dict(row)
        result["objective"] = json.loads(result.pop("objective_json"))
        for item in evaluations:
            item["details"] = json.loads(item.pop("details_json"))
        result["files"] = files
        result["evaluations"] = evaluations
        return result

    def list(self, *, campaign_id: str | None = None) -> list[dict[str, Any]]:
        """List the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        where = " WHERE campaign_id=?" if campaign_id else ""
        args = (campaign_id,) if campaign_id else ()
        with self.store.connect() as connection:
            ids = [row[0] for row in connection.execute(f"SELECT candidate_id FROM governance_candidates{where} ORDER BY created_at", args).fetchall()]
        return [self.get(candidate_id) for candidate_id in ids]
