from __future__ import annotations

import json
from typing import Any

from x86decomp.contracts import ContractError
from x86decomp.reconstruction.store import ReconstructionStore

SCHEMA_EXTENSION_VERSION = 6

_SCHEMA_SQL = r'''
CREATE TABLE IF NOT EXISTS native_metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS native_function_slots (
 slot_id TEXT PRIMARY KEY, function_id TEXT NOT NULL UNIQUE, rva INTEGER NOT NULL,
 body_size INTEGER NOT NULL, slot_size INTEGER NOT NULL, slot_end_rva INTEGER NOT NULL,
 classification TEXT NOT NULL, boundary_confidence REAL NOT NULL CHECK(boundary_confidence BETWEEN 0 AND 1),
 evidence_json TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS native_boundary_findings (
 finding_id TEXT PRIMARY KEY, function_id TEXT NOT NULL, finding_kind TEXT NOT NULL,
 severity TEXT NOT NULL, details_json TEXT NOT NULL, status TEXT NOT NULL,
 created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS native_match_runs (
 run_id TEXT PRIMARY KEY, original_path TEXT NOT NULL, original_sha256 TEXT NOT NULL,
 comparison_policy TEXT NOT NULL, pad_bytes_json TEXT NOT NULL, status TEXT NOT NULL,
 summary_json TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS native_function_matches (
 match_id TEXT PRIMARY KEY, run_id TEXT NOT NULL REFERENCES native_match_runs(run_id) ON DELETE CASCADE,
 function_id TEXT NOT NULL, rva INTEGER NOT NULL, slot_size INTEGER NOT NULL,
 candidate_path TEXT, candidate_sha256 TEXT, candidate_size INTEGER,
 classification TEXT NOT NULL, first_mismatch INTEGER, replacement_safe INTEGER NOT NULL CHECK(replacement_safe IN (0,1)),
 details_json TEXT NOT NULL, created_at TEXT NOT NULL, UNIQUE(run_id,function_id)
);
CREATE TABLE IF NOT EXISTS native_patch_plans (
 plan_id TEXT PRIMARY KEY, original_path TEXT NOT NULL, original_sha256 TEXT NOT NULL,
 output_path TEXT NOT NULL, operations_json TEXT NOT NULL, status TEXT NOT NULL,
 created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS native_hybrid_compositions (
 composition_id TEXT PRIMARY KEY, run_id TEXT NOT NULL REFERENCES native_match_runs(run_id),
 original_path TEXT NOT NULL, output_path TEXT NOT NULL, output_sha256 TEXT NOT NULL,
 promoted_count INTEGER NOT NULL, fallback_count INTEGER NOT NULL,
 preserved_sections_json TEXT NOT NULL, report_json TEXT NOT NULL, created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS native_staging_symbols (
 symbol_id TEXT PRIMARY KEY, symbol_name TEXT NOT NULL UNIQUE, symbol_kind TEXT NOT NULL,
 declaration TEXT NOT NULL, source TEXT NOT NULL, confidence REAL NOT NULL CHECK(confidence BETWEEN 0 AND 1),
 status TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS native_loop_runs (
 loop_id TEXT PRIMARY KEY, function_id TEXT NOT NULL, source_path TEXT NOT NULL,
 compile_command_json TEXT NOT NULL, candidate_path TEXT NOT NULL, comparison_policy TEXT NOT NULL,
 status TEXT NOT NULL, result_json TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS native_runtime_validations (
 validation_id TEXT PRIMARY KEY, image_path TEXT NOT NULL, image_sha256 TEXT NOT NULL,
 validation_kind TEXT NOT NULL, status TEXT NOT NULL, checks_json TEXT NOT NULL,
 execution_authorized INTEGER NOT NULL CHECK(execution_authorized IN (0,1)), created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS native_windows_tools (
 tool_id TEXT PRIMARY KEY, tool_name TEXT NOT NULL UNIQUE, path TEXT,
 available INTEGER NOT NULL CHECK(available IN (0,1)), version TEXT, details_json TEXT NOT NULL,
 checked_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_native_slots_rva ON native_function_slots(rva);
CREATE INDEX IF NOT EXISTS idx_native_matches_run_class ON native_function_matches(run_id,classification);
CREATE INDEX IF NOT EXISTS idx_native_boundary_status ON native_boundary_findings(status,severity);
'''


class NativeStore(ReconstructionStore):
    """Native-PE reconstruction schema layered on current reconstruction data."""

    def initialize(self) -> None:
        super().initialize()
        with self.transaction() as connection:
            connection.executescript(_SCHEMA_SQL)
            row = connection.execute("SELECT value FROM native_metadata WHERE key='schema_extension_version'").fetchone()
            if row and int(row[0]) > SCHEMA_EXTENSION_VERSION:
                raise ContractError(f"project uses future native extension schema {row[0]}")
            values = {
                "schema_extension_version": str(SCHEMA_EXTENSION_VERSION),
                "release_version": "0.7.8",
            }
            for key, value in values.items():
                connection.execute(
                    "INSERT INTO native_metadata(key,value) VALUES(?,?) "
                    "ON CONFLICT(key) DO UPDATE SET value=excluded.value", (key, value)
                )

    def check(self) -> dict[str, Any]:
        self.initialize()
        base = super().check()
        with self.connect() as connection:
            version = int(connection.execute(
                "SELECT value FROM native_metadata WHERE key='schema_extension_version'"
            ).fetchone()[0])
            tables = int(connection.execute(
                "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name LIKE 'native_%'"
            ).fetchone()[0])
            counts = {
                row[0]: int(row[1])
                for row in connection.execute(
                    "SELECT name,(SELECT COUNT(*) FROM pragma_table_info(name)) "
                    "FROM sqlite_master WHERE type='table' AND name LIKE 'native_%' ORDER BY name"
                )
            }
        return {
            **base,
            "release_version": "0.7.8",
            "native_schema_extension_version": version,
            "native_table_count": tables,
            "native_table_columns": counts,
            "passed": bool(base["passed"] and version == SCHEMA_EXTENSION_VERSION),
        }

    @staticmethod
    def decode(row: Any, *json_fields: str) -> dict[str, Any]:
        result = dict(row)
        for field in json_fields:
            if field in result:
                raw = result.pop(field)
                result[field[:-5] if field.endswith("_json") else field] = None if raw is None else json.loads(raw)
        return result
