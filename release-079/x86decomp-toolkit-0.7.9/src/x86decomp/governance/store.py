"""Provide x86decomp.governance.store functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import contextlib
import json
import sqlite3
from collections.abc import Iterator
from pathlib import Path
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, sha256_bytes, utc_now

SCHEMA_EXTENSION_VERSION = 4

_SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS governance_metadata (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS governance_audit_events (
    sequence INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id TEXT NOT NULL UNIQUE,
    occurred_at TEXT NOT NULL,
    actor TEXT NOT NULL,
    category TEXT NOT NULL,
    subject_id TEXT,
    payload_json TEXT NOT NULL,
    previous_hash TEXT,
    event_hash TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS governance_campaigns (
    campaign_id TEXT PRIMARY KEY,
    goal TEXT NOT NULL,
    status TEXT NOT NULL,
    project_root TEXT NOT NULL,
    budget_json TEXT NOT NULL,
    used_json TEXT NOT NULL,
    policy_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    blocked_reason TEXT
);
CREATE TABLE IF NOT EXISTS governance_campaign_branches (
    branch_id TEXT PRIMARY KEY,
    campaign_id TEXT NOT NULL REFERENCES governance_campaigns(campaign_id) ON DELETE CASCADE,
    parent_branch_id TEXT REFERENCES governance_campaign_branches(branch_id),
    name TEXT NOT NULL,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE(campaign_id, name)
);
CREATE TABLE IF NOT EXISTS governance_planner_decisions (
    decision_id TEXT PRIMARY KEY,
    campaign_id TEXT NOT NULL REFERENCES governance_campaigns(campaign_id) ON DELETE CASCADE,
    branch_id TEXT REFERENCES governance_campaign_branches(branch_id),
    action_kind TEXT NOT NULL,
    subject_id TEXT,
    rationale_json TEXT NOT NULL,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS governance_hypotheses (
    hypothesis_id TEXT PRIMARY KEY,
    statement TEXT NOT NULL,
    scope_kind TEXT NOT NULL,
    scope_id TEXT NOT NULL,
    state TEXT NOT NULL,
    confidence REAL NOT NULL,
    origin TEXT NOT NULL,
    locked INTEGER NOT NULL DEFAULT 0 CHECK(locked IN (0,1)),
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    disposition_reason TEXT
);
CREATE TABLE IF NOT EXISTS governance_hypothesis_dependencies (
    hypothesis_id TEXT NOT NULL REFERENCES governance_hypotheses(hypothesis_id) ON DELETE CASCADE,
    depends_on_id TEXT NOT NULL REFERENCES governance_hypotheses(hypothesis_id) ON DELETE CASCADE,
    PRIMARY KEY(hypothesis_id, depends_on_id),
    CHECK(hypothesis_id <> depends_on_id)
);
CREATE TABLE IF NOT EXISTS governance_hypothesis_evidence (
    link_id TEXT PRIMARY KEY,
    hypothesis_id TEXT NOT NULL REFERENCES governance_hypotheses(hypothesis_id) ON DELETE CASCADE,
    evidence_id TEXT NOT NULL,
    stance TEXT NOT NULL CHECK(stance IN ('supports','contradicts','context')),
    weight REAL NOT NULL CHECK(weight >= 0.0 AND weight <= 1.0),
    evidence_kind TEXT NOT NULL,
    independence_group TEXT NOT NULL,
    artifact_sha256 TEXT,
    details_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE(hypothesis_id, evidence_id, stance)
);
CREATE TABLE IF NOT EXISTS governance_experiments (
    experiment_id TEXT PRIMARY KEY,
    hypothesis_id TEXT REFERENCES governance_hypotheses(hypothesis_id),
    campaign_id TEXT REFERENCES governance_campaigns(campaign_id),
    kind TEXT NOT NULL,
    status TEXT NOT NULL,
    inputs_json TEXT NOT NULL,
    outputs_json TEXT NOT NULL,
    started_at TEXT NOT NULL,
    finished_at TEXT
);
CREATE TABLE IF NOT EXISTS governance_candidates (
    candidate_id TEXT PRIMARY KEY,
    campaign_id TEXT REFERENCES governance_campaigns(campaign_id),
    branch_name TEXT NOT NULL,
    parent_candidate_id TEXT REFERENCES governance_candidates(candidate_id),
    state TEXT NOT NULL,
    objective_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    UNIQUE(campaign_id, branch_name)
);
CREATE TABLE IF NOT EXISTS governance_candidate_files (
    candidate_id TEXT NOT NULL REFERENCES governance_candidates(candidate_id) ON DELETE CASCADE,
    relative_path TEXT NOT NULL,
    content_sha256 TEXT NOT NULL,
    size_bytes INTEGER NOT NULL,
    artifact_path TEXT NOT NULL,
    PRIMARY KEY(candidate_id, relative_path)
);
CREATE TABLE IF NOT EXISTS governance_candidate_evaluations (
    evaluation_id TEXT PRIMARY KEY,
    candidate_id TEXT NOT NULL REFERENCES governance_candidates(candidate_id) ON DELETE CASCADE,
    metric TEXT NOT NULL,
    value REAL,
    status TEXT NOT NULL,
    details_json TEXT NOT NULL,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS governance_counterexamples (
    counterexample_id TEXT PRIMARY KEY,
    scope_kind TEXT NOT NULL,
    scope_id TEXT NOT NULL,
    original_sha256 TEXT NOT NULL,
    current_sha256 TEXT NOT NULL,
    payload_path TEXT NOT NULL,
    size_bytes INTEGER NOT NULL,
    state TEXT NOT NULL,
    predicate_json TEXT NOT NULL,
    provenance_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS governance_consensus_observations (
    observation_id TEXT PRIMARY KEY,
    subject_kind TEXT NOT NULL,
    subject_id TEXT NOT NULL,
    property_name TEXT NOT NULL,
    value_json TEXT NOT NULL,
    adapter_name TEXT NOT NULL,
    adapter_version TEXT NOT NULL,
    evidence_id TEXT NOT NULL,
    independence_group TEXT NOT NULL,
    confidence REAL NOT NULL CHECK(confidence >= 0.0 AND confidence <= 1.0),
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS governance_consensus_resolutions (
    resolution_id TEXT PRIMARY KEY,
    subject_kind TEXT NOT NULL,
    subject_id TEXT NOT NULL,
    property_name TEXT NOT NULL,
    selected_value_json TEXT NOT NULL,
    method TEXT NOT NULL,
    rationale TEXT NOT NULL,
    actor TEXT NOT NULL,
    locked INTEGER NOT NULL DEFAULT 0 CHECK(locked IN (0,1)),
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS governance_graph_nodes (
    node_id TEXT PRIMARY KEY,
    kind TEXT NOT NULL,
    label TEXT NOT NULL,
    attributes_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS governance_graph_edges (
    edge_id TEXT PRIMARY KEY,
    source_id TEXT NOT NULL REFERENCES governance_graph_nodes(node_id) ON DELETE CASCADE,
    target_id TEXT NOT NULL REFERENCES governance_graph_nodes(node_id) ON DELETE CASCADE,
    relation TEXT NOT NULL,
    attributes_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE(source_id, target_id, relation)
);
CREATE TABLE IF NOT EXISTS governance_review_items (
    review_id TEXT PRIMARY KEY,
    kind TEXT NOT NULL,
    subject_id TEXT NOT NULL,
    priority INTEGER NOT NULL,
    status TEXT NOT NULL,
    assigned_to TEXT,
    summary TEXT NOT NULL,
    details_json TEXT NOT NULL,
    locked INTEGER NOT NULL DEFAULT 0 CHECK(locked IN (0,1)),
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS governance_review_decisions (
    decision_id TEXT PRIMARY KEY,
    review_id TEXT NOT NULL REFERENCES governance_review_items(review_id) ON DELETE CASCADE,
    actor TEXT NOT NULL,
    decision TEXT NOT NULL,
    rationale TEXT NOT NULL,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS governance_binary_families (
    family_id TEXT PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS governance_family_members (
    member_id TEXT PRIMARY KEY,
    family_id TEXT NOT NULL REFERENCES governance_binary_families(family_id) ON DELETE CASCADE,
    label TEXT NOT NULL,
    file_sha256 TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    artifact_path TEXT NOT NULL,
    metadata_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE(family_id, label)
);
CREATE TABLE IF NOT EXISTS governance_family_correlations (
    correlation_id TEXT PRIMARY KEY,
    family_id TEXT NOT NULL REFERENCES governance_binary_families(family_id) ON DELETE CASCADE,
    left_member_id TEXT NOT NULL REFERENCES governance_family_members(member_id) ON DELETE CASCADE,
    right_member_id TEXT NOT NULL REFERENCES governance_family_members(member_id) ON DELETE CASCADE,
    algorithm TEXT NOT NULL,
    score REAL NOT NULL,
    details_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE(left_member_id, right_member_id, algorithm)
);
CREATE TABLE IF NOT EXISTS governance_proof_obligations (
    obligation_id TEXT PRIMARY KEY,
    scope_kind TEXT NOT NULL,
    scope_id TEXT NOT NULL,
    property_name TEXT NOT NULL,
    required_status TEXT NOT NULL,
    assumptions_json TEXT NOT NULL,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS governance_proof_results (
    result_id TEXT PRIMARY KEY,
    obligation_id TEXT NOT NULL REFERENCES governance_proof_obligations(obligation_id) ON DELETE CASCADE,
    status TEXT NOT NULL,
    validator TEXT NOT NULL,
    report_json TEXT NOT NULL,
    artifact_sha256 TEXT,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS governance_worker_profiles (
    worker_id TEXT PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    endpoint TEXT,
    status TEXT NOT NULL,
    capabilities_json TEXT NOT NULL,
    environment_sha256 TEXT,
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS governance_plugin_records (
    plugin_id TEXT PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    version TEXT NOT NULL,
    api_version TEXT NOT NULL,
    executable TEXT NOT NULL,
    executable_sha256 TEXT NOT NULL,
    capabilities_json TEXT NOT NULL,
    enabled INTEGER NOT NULL DEFAULT 1 CHECK(enabled IN (0,1)),
    installed_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS governance_changesets (
    changeset_id TEXT PRIMARY KEY,
    base_event_hash TEXT,
    tip_event_hash TEXT,
    manifest_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    applied_at TEXT
);
CREATE INDEX IF NOT EXISTS idx_governance_hypotheses_state ON governance_hypotheses(state);
CREATE INDEX IF NOT EXISTS idx_governance_consensus_subject ON governance_consensus_observations(subject_kind, subject_id, property_name);
CREATE INDEX IF NOT EXISTS idx_governance_review_status ON governance_review_items(status, priority DESC);
CREATE INDEX IF NOT EXISTS idx_governance_graph_out ON governance_graph_edges(source_id, relation);
CREATE INDEX IF NOT EXISTS idx_governance_graph_in ON governance_graph_edges(target_id, relation);
"""


class GovernanceStore:
    """Transactional governance extension store.

    Tables are namespaced so the extension can be added to the current project database
    without rewriting or dropping any legacy table.
    """

    def __init__(self, project_root: str | Path, *, database_path: str | Path | None = None):
        """Initialize the instance with the supplied constructor arguments.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.project_root = Path(project_root).resolve()
        self.database_path = Path(database_path).resolve() if database_path else self.project_root / "state" / "project-state.sqlite3"

    def initialize(self) -> None:
        """Initialize the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        self.project_root.mkdir(parents=True, exist_ok=True)
        with self.transaction() as connection:
            connection.executescript(_SCHEMA_SQL)
            existing = connection.execute("SELECT value FROM governance_metadata WHERE key='schema_extension_version'").fetchone()
            if existing and int(existing[0]) > SCHEMA_EXTENSION_VERSION:
                raise ContractError(f"project uses future governance extension schema {existing[0]}")
            connection.execute(
                "INSERT INTO governance_metadata(key,value) VALUES('schema_extension_version',?) "
                "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
                (str(SCHEMA_EXTENSION_VERSION),),
            )
            connection.execute(
                "INSERT INTO governance_metadata(key,value) VALUES('release_version','0.7.9') "
                "ON CONFLICT(key) DO UPDATE SET value=excluded.value"
            )

    def connect(self) -> sqlite3.Connection:
        """Implement connect.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        connection = sqlite3.connect(self.database_path, timeout=30.0)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys=ON")
        connection.execute("PRAGMA journal_mode=WAL")
        connection.execute("PRAGMA synchronous=FULL")
        connection.execute("PRAGMA busy_timeout=30000")
        return connection

    @contextlib.contextmanager
    def transaction(self, *, immediate: bool = True) -> Iterator[sqlite3.Connection]:
        """Implement transaction.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        connection = self.connect()
        try:
            connection.execute("BEGIN IMMEDIATE" if immediate else "BEGIN")
            yield connection
            connection.commit()
        except BaseException:
            connection.rollback()
            raise
        finally:
            connection.close()

    def audit(self, actor: str, category: str, subject_id: str | None, payload: dict[str, Any], *, connection: sqlite3.Connection | None = None) -> str:
        """Audit the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        owns_connection = connection is None
        if owns_connection:
            connection = self.connect()
            connection.execute("BEGIN IMMEDIATE")
        assert connection is not None
        try:
            previous = connection.execute("SELECT event_hash FROM governance_audit_events ORDER BY sequence DESC LIMIT 1").fetchone()
            previous_hash = previous[0] if previous else None
            occurred_at = utc_now()
            event_body = {
                "occurred_at": occurred_at,
                "actor": actor,
                "category": category,
                "subject_id": subject_id,
                "payload": payload,
                "previous_hash": previous_hash,
            }
            event_hash = sha256_bytes(canonical_json(event_body).encode("utf-8"))
            event_id = f"evt-{event_hash[:20]}"
            connection.execute(
                "INSERT INTO governance_audit_events(event_id,occurred_at,actor,category,subject_id,payload_json,previous_hash,event_hash) VALUES(?,?,?,?,?,?,?,?)",
                (event_id, occurred_at, actor, category, subject_id, canonical_json(payload), previous_hash, event_hash),
            )
            if owns_connection:
                connection.commit()
            return event_id
        except BaseException:
            if owns_connection:
                connection.rollback()
            raise
        finally:
            if owns_connection:
                connection.close()

    def verify_audit_chain(self) -> dict[str, Any]:
        """Verify audit chain.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.connect() as connection:
            rows = connection.execute("SELECT * FROM governance_audit_events ORDER BY sequence").fetchall()
        previous_hash: str | None = None
        failures: list[dict[str, Any]] = []
        for row in rows:
            body = {
                "occurred_at": row["occurred_at"],
                "actor": row["actor"],
                "category": row["category"],
                "subject_id": row["subject_id"],
                "payload": json.loads(row["payload_json"]),
                "previous_hash": row["previous_hash"],
            }
            expected = sha256_bytes(canonical_json(body).encode("utf-8"))
            if row["previous_hash"] != previous_hash or row["event_hash"] != expected:
                failures.append({"event_id": row["event_id"], "expected_hash": expected, "recorded_hash": row["event_hash"]})
            previous_hash = row["event_hash"]
        return {"valid": not failures, "events": len(rows), "tip_hash": previous_hash, "failures": failures}

    def check(self) -> dict[str, Any]:
        """Check the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.initialize()
        with self.connect() as connection:
            integrity = connection.execute("PRAGMA integrity_check").fetchall()
            version = connection.execute("SELECT value FROM governance_metadata WHERE key='schema_extension_version'").fetchone()[0]
            table_count = connection.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name LIKE 'governance_%'").fetchone()[0]
        audit = self.verify_audit_chain()
        return {
            "database": str(self.database_path),
            "schema_extension_version": int(version),
            "integrity": [row[0] for row in integrity],
            "governance_table_count": table_count,
            "audit_chain": audit,
            "passed": [row[0] for row in integrity] == ["ok"] and audit["valid"],
        }
