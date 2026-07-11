"""Persist assembly reconstruction runs, source units, and verification results."""
from __future__ import annotations

from typing import Any

from x86decomp.contracts import ContractError
from x86decomp.native.store import NativeStore
from x86decomp.store_utils import decode_json_fields

SCHEMA_EXTENSION_VERSION = 7

_SCHEMA_SQL = r'''
CREATE TABLE IF NOT EXISTS assembly_metadata (
 key TEXT PRIMARY KEY, value TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS assembly_asm_runs (
 run_id TEXT PRIMARY KEY, asm_format TEXT NOT NULL,
 architecture TEXT NOT NULL, source_root TEXT, output_root TEXT NOT NULL,
 symbol_map_sha256 TEXT, status TEXT NOT NULL, summary_json TEXT NOT NULL,
 created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS assembly_asm_functions (
 result_id TEXT PRIMARY KEY,
 run_id TEXT NOT NULL REFERENCES assembly_asm_runs(run_id) ON DELETE CASCADE,
 function_id TEXT NOT NULL, symbol TEXT NOT NULL, rva INTEGER NOT NULL,
 input_sha256 TEXT NOT NULL, source_path TEXT NOT NULL, source_sha256 TEXT NOT NULL,
 object_path TEXT, resolved_path TEXT, resolved_sha256 TEXT,
 instruction_count INTEGER NOT NULL, mnemonic_count INTEGER NOT NULL,
 byte_escape_count INTEGER NOT NULL, relocation_count INTEGER NOT NULL,
 resolved_relocation_count INTEGER NOT NULL, unresolved_relocation_count INTEGER NOT NULL,
 exact_match INTEGER NOT NULL CHECK(exact_match IN (0,1)),
 classification TEXT NOT NULL, details_json TEXT NOT NULL, created_at TEXT NOT NULL,
 UNIQUE(run_id,function_id)
);
CREATE TABLE IF NOT EXISTS assembly_relocation_resolutions (
 resolution_id TEXT PRIMARY KEY, result_id TEXT,
 object_path TEXT NOT NULL, object_sha256 TEXT NOT NULL,
 symbol TEXT NOT NULL, section_name TEXT NOT NULL, relocation_offset INTEGER NOT NULL,
 relocation_type TEXT NOT NULL, target_symbol TEXT,
 target_rva INTEGER, computed_value INTEGER, status TEXT NOT NULL,
 details_json TEXT NOT NULL, created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_assembly_asm_run_format ON assembly_asm_runs(asm_format,status);
CREATE INDEX IF NOT EXISTS idx_assembly_asm_function_class ON assembly_asm_functions(classification,exact_match);
CREATE INDEX IF NOT EXISTS idx_assembly_relocation_status ON assembly_relocation_resolutions(status,relocation_type);
'''


class AssemblyStore(NativeStore):
    """Additive relocation-aware assembly schema layered on the current native reconstruction state."""

    def initialize(self) -> None:
        """Initialize assembly store storage."""
        super().initialize()
        with self.transaction() as connection:
            connection.executescript(_SCHEMA_SQL)
            row = connection.execute(
                "SELECT value FROM assembly_metadata WHERE key='schema_extension_version'"
            ).fetchone()
            if row and int(row[0]) > SCHEMA_EXTENSION_VERSION:
                raise ContractError(f"project uses future assembly extension schema {row[0]}")
            values = {
                "schema_extension_version": str(SCHEMA_EXTENSION_VERSION),
                "release_version": "0.7.11",
                "default_asm_format": "bytes",
            }
            for key, value in values.items():
                connection.execute(
                    "INSERT INTO assembly_metadata(key,value) VALUES(?,?) "
                    "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
                    (key, value),
                )

    def check(self) -> dict[str, Any]:
        """Check assembly store state."""
        self.initialize()
        base = super().check()
        with self.connect() as connection:
            version = int(
                connection.execute(
                    "SELECT value FROM assembly_metadata WHERE key='schema_extension_version'"
                ).fetchone()[0]
            )
            tables = int(
                connection.execute(
                    "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name LIKE 'assembly_%'"
                ).fetchone()[0]
            )
            default_format = str(
                connection.execute(
                    "SELECT value FROM assembly_metadata WHERE key='default_asm_format'"
                ).fetchone()[0]
            )
        return {
            **base,
            "release_version": "0.7.11",
            "assembly_schema_extension_version": version,
            "assembly_table_count": tables,
            "default_asm_format": default_format,
            "passed": bool(
                base["passed"]
                and version == SCHEMA_EXTENSION_VERSION
                and default_format == "bytes"
            ),
        }

    @staticmethod
    def decode(row: Any, *json_fields: str) -> dict[str, Any]:
        """Decode configured JSON columns from a SQLite row."""
        return decode_json_fields(row, *json_fields)
