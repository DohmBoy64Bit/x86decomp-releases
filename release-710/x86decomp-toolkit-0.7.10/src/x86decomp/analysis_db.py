"""SQLite-backed global symbol, type, reference, and constraint database."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any, Iterable

from .errors import ContractError
from .util import utc_now

_SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS entities (
  id TEXT PRIMARY KEY,
  kind TEXT NOT NULL CHECK(kind IN ('function','symbol','global','type','field','vtable','string')),
  name TEXT,
  address_rva INTEGER,
  provenance TEXT NOT NULL,
  confidence REAL CHECK(confidence IS NULL OR (confidence >= 0 AND confidence <= 1)),
  accepted INTEGER NOT NULL DEFAULT 0 CHECK(accepted IN (0,1)),
  metadata_json TEXT NOT NULL DEFAULT '{}',
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS references_graph (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  source_entity TEXT NOT NULL,
  target_entity TEXT,
  source_rva INTEGER,
  target_rva INTEGER,
  kind TEXT NOT NULL,
  provenance TEXT NOT NULL,
  metadata_json TEXT NOT NULL DEFAULT '{}',
  UNIQUE(source_entity, source_rva, target_rva, kind, provenance)
);
CREATE TABLE IF NOT EXISTS type_constraints (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  subject_entity TEXT NOT NULL,
  relation TEXT NOT NULL,
  object_value TEXT NOT NULL,
  evidence_id TEXT,
  provenance TEXT NOT NULL,
  confidence REAL CHECK(confidence IS NULL OR (confidence >= 0 AND confidence <= 1)),
  status TEXT NOT NULL CHECK(status IN ('proposed','consistent','conflicting','accepted','rejected')),
  created_at TEXT NOT NULL,
  UNIQUE(subject_entity, relation, object_value, provenance, evidence_id)
);
CREATE TABLE IF NOT EXISTS function_abi (
  function_id TEXT PRIMARY KEY,
  convention TEXT,
  return_type TEXT,
  signature TEXT,
  stack_cleanup INTEGER,
  variadic INTEGER,
  structure_return INTEGER,
  provenance TEXT NOT NULL,
  confidence REAL,
  metadata_json TEXT NOT NULL DEFAULT '{}',
  updated_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_entities_address ON entities(address_rva);
CREATE INDEX IF NOT EXISTS idx_refs_source ON references_graph(source_entity);
CREATE INDEX IF NOT EXISTS idx_refs_target ON references_graph(target_entity);
CREATE INDEX IF NOT EXISTS idx_constraints_subject ON type_constraints(subject_entity);
"""


class AnalysisDatabase:
    """Coordinate analysis database behavior for the current toolkit workflow."""
    def __init__(self, path: Path):
        """Initialize the instance with validated constructor state."""
        self.path = path.resolve()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(self.path)
        self.connection.row_factory = sqlite3.Row
        self.connection.executescript(_SCHEMA)

    def close(self) -> None:
        """Execute the close operation for the current toolkit workflow."""
        self.connection.close()

    def __enter__(self) -> "AnalysisDatabase":
        """Enter the managed runtime context and return the active resource."""
        return self

    def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None:
        """Exit the managed runtime context and release owned resources."""
        if exc is None:
            self.connection.commit()
        else:
            self.connection.rollback()
        self.close()

    def upsert_entity(
        self,
        *,
        entity_id: str,
        kind: str,
        name: str | None,
        address_rva: int | None,
        provenance: str,
        confidence: float | None = None,
        accepted: bool = False,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """Execute the upsert entity operation for the current toolkit workflow."""
        if kind not in {"function", "symbol", "global", "type", "field", "vtable", "string"}:
            raise ContractError(f"unsupported entity kind: {kind}")
        if confidence is not None and not 0 <= confidence <= 1:
            raise ContractError("confidence must be between 0 and 1")
        now = utc_now()
        self.connection.execute(
            """
            INSERT INTO entities(id,kind,name,address_rva,provenance,confidence,accepted,metadata_json,created_at,updated_at)
            VALUES(?,?,?,?,?,?,?,?,?,?)
            ON CONFLICT(id) DO UPDATE SET
              kind=excluded.kind,name=excluded.name,address_rva=excluded.address_rva,
              provenance=excluded.provenance,confidence=excluded.confidence,accepted=excluded.accepted,
              metadata_json=excluded.metadata_json,updated_at=excluded.updated_at
            """,
            (entity_id, kind, name, address_rva, provenance, confidence, int(accepted), json.dumps(metadata or {}, sort_keys=True), now, now),
        )

    def add_reference(
        self,
        *,
        source_entity: str,
        target_entity: str | None,
        source_rva: int | None,
        target_rva: int | None,
        kind: str,
        provenance: str,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """Execute the add reference operation for the current toolkit workflow."""
        self.connection.execute(
            """INSERT OR IGNORE INTO references_graph
            (source_entity,target_entity,source_rva,target_rva,kind,provenance,metadata_json)
            VALUES(?,?,?,?,?,?,?)""",
            (source_entity, target_entity, source_rva, target_rva, kind, provenance, json.dumps(metadata or {}, sort_keys=True)),
        )

    def add_type_constraint(
        self,
        *,
        subject_entity: str,
        relation: str,
        object_value: str,
        provenance: str,
        evidence_id: str | None = None,
        confidence: float | None = None,
        status: str = "proposed",
    ) -> int:
        """Execute the add type constraint operation for the current toolkit workflow."""
        if status not in {"proposed", "consistent", "conflicting", "accepted", "rejected"}:
            raise ContractError("invalid type constraint status")
        cursor = self.connection.execute(
            """INSERT OR IGNORE INTO type_constraints
            (subject_entity,relation,object_value,evidence_id,provenance,confidence,status,created_at)
            VALUES(?,?,?,?,?,?,?,?)""",
            (subject_entity, relation, object_value, evidence_id, provenance, confidence, status, utc_now()),
        )
        return int(cursor.lastrowid or 0)

    def detect_constraint_conflicts(self, subject_entity: str, relation: str) -> list[dict[str, Any]]:
        """Execute the detect constraint conflicts operation for the current toolkit workflow."""
        rows = self.connection.execute(
            """SELECT object_value, COUNT(*) AS count, GROUP_CONCAT(provenance) AS provenances
               FROM type_constraints WHERE subject_entity=? AND relation=? AND status NOT IN ('rejected')
               GROUP BY object_value ORDER BY object_value""",
            (subject_entity, relation),
        ).fetchall()
        values = [dict(row) for row in rows]
        if len(values) > 1:
            self.connection.execute(
                "UPDATE type_constraints SET status='conflicting' WHERE subject_entity=? AND relation=? AND status NOT IN ('accepted','rejected')",
                (subject_entity, relation),
            )
        return values

    def accept_constraint(self, constraint_id: int) -> None:
        """Execute the accept constraint operation for the current toolkit workflow."""
        row = self.connection.execute("SELECT * FROM type_constraints WHERE id=?", (constraint_id,)).fetchone()
        if row is None:
            raise ContractError(f"type constraint does not exist: {constraint_id}")
        conflicts = self.connection.execute(
            """SELECT id FROM type_constraints WHERE subject_entity=? AND relation=? AND object_value<>? AND status NOT IN ('rejected')""",
            (row["subject_entity"], row["relation"], row["object_value"]),
        ).fetchall()
        if conflicts:
            raise ContractError("cannot accept a type constraint while contradictory constraints remain")
        self.connection.execute("UPDATE type_constraints SET status='accepted' WHERE id=?", (constraint_id,))

    def ingest_function_artifact(self, artifact_dir: Path, *, image_base: int = 0) -> dict[str, int]:
        """Execute the ingest function artifact operation for the current toolkit workflow."""
        manifest_path = artifact_dir / "function.json"
        if not manifest_path.is_file():
            raise ContractError(f"missing function.json: {manifest_path}")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        function_id = manifest.get("id")
        if not isinstance(function_id, str):
            raise ContractError("function artifact id is missing")
        self.upsert_entity(
            entity_id=function_id,
            kind="function",
            name=manifest.get("qualified_name") or manifest.get("name"),
            address_rva=manifest.get("entry_rva"),
            provenance="ghidra",
            metadata=manifest,
        )
        self.connection.execute(
            """INSERT INTO function_abi(function_id,convention,return_type,signature,stack_cleanup,variadic,structure_return,provenance,confidence,metadata_json,updated_at)
            VALUES(?,?,?,?,?,?,?,?,?,?,?)
            ON CONFLICT(function_id) DO UPDATE SET convention=excluded.convention,return_type=excluded.return_type,
              signature=excluded.signature,provenance=excluded.provenance,metadata_json=excluded.metadata_json,updated_at=excluded.updated_at""",
            (function_id, manifest.get("calling_convention"), manifest.get("return_type"), manifest.get("signature"), None, None, None, "ghidra", None, "{}", utc_now()),
        )
        reference_count = 0
        refs_path = artifact_dir / "references.jsonl"
        if refs_path.is_file():
            for line in refs_path.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                ref = json.loads(line)
                target_name = ref.get("destination_function")
                target_entity = None
                if target_name:
                    target_entity = f"name:{target_name}"
                    self.upsert_entity(entity_id=target_entity, kind="symbol", name=target_name, address_rva=None, provenance="ghidra-reference")
                from_text = str(ref.get("from", "0"))
                to_text = str(ref.get("to", "0"))
                try:
                    source_rva = int(from_text, 16) - image_base
                    target_rva = int(to_text, 16) - image_base
                except ValueError:
                    source_rva = target_rva = None
                self.add_reference(
                    source_entity=function_id,
                    target_entity=target_entity,
                    source_rva=source_rva,
                    target_rva=target_rva,
                    kind=str(ref.get("type", "unknown")),
                    provenance="ghidra",
                    metadata=ref,
                )
                reference_count += 1
        self.connection.commit()
        return {"functions": 1, "references": reference_count}

    def query(self, sql: str, parameters: Iterable[Any] = ()) -> list[dict[str, Any]]:
        """Execute the query operation for the current toolkit workflow."""
        normalized = sql.lstrip().lower()
        if not normalized.startswith("select"):
            raise ContractError("analysis database query permits SELECT statements only")
        return [dict(row) for row in self.connection.execute(sql, tuple(parameters)).fetchall()]
