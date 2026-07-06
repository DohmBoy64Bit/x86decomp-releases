"""Provide the current runtime implementation for the `x86decomp.reconstruction.store` module."""
from __future__ import annotations

from typing import Any

from x86decomp.contracts import ContractError
from x86decomp.governance.store import GovernanceStore
from x86decomp.store_utils import decode_json_fields

SCHEMA_EXTENSION_VERSION = 5

_SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS reconstruction_metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS reconstruction_modules (
 module_id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE, kind TEXT NOT NULL,
 source_path TEXT, confidence REAL NOT NULL CHECK(confidence BETWEEN 0 AND 1),
 evidence_json TEXT NOT NULL, status TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS reconstruction_module_members (
 module_id TEXT NOT NULL REFERENCES reconstruction_modules(module_id) ON DELETE CASCADE,
 member_kind TEXT NOT NULL, member_id TEXT NOT NULL, ordinal INTEGER NOT NULL,
 evidence_json TEXT NOT NULL, PRIMARY KEY(module_id,member_kind,member_id)
);
CREATE TABLE IF NOT EXISTS reconstruction_translation_units (
 unit_id TEXT PRIMARY KEY, module_id TEXT REFERENCES reconstruction_modules(module_id) ON DELETE SET NULL,
 source_path TEXT NOT NULL UNIQUE, language TEXT NOT NULL, confidence REAL NOT NULL CHECK(confidence BETWEEN 0 AND 1),
 evidence_json TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS reconstruction_translation_unit_members (
 unit_id TEXT NOT NULL REFERENCES reconstruction_translation_units(unit_id) ON DELETE CASCADE,
 member_kind TEXT NOT NULL, member_id TEXT NOT NULL, linkage TEXT NOT NULL,
 ordinal INTEGER NOT NULL, PRIMARY KEY(unit_id,member_kind,member_id)
);
CREATE TABLE IF NOT EXISTS reconstruction_headers (
 header_id TEXT PRIMARY KEY, path TEXT NOT NULL UNIQUE, visibility TEXT NOT NULL,
 status TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS reconstruction_header_declarations (
 declaration_id TEXT PRIMARY KEY, header_id TEXT NOT NULL REFERENCES reconstruction_headers(header_id) ON DELETE CASCADE,
 symbol_id TEXT NOT NULL, declaration TEXT NOT NULL, declaration_kind TEXT NOT NULL,
 confidence REAL NOT NULL CHECK(confidence BETWEEN 0 AND 1), evidence_json TEXT NOT NULL,
 UNIQUE(header_id,symbol_id,declaration_kind)
);
CREATE TABLE IF NOT EXISTS reconstruction_include_edges (
 source_header_id TEXT NOT NULL REFERENCES reconstruction_headers(header_id) ON DELETE CASCADE,
 target_header_id TEXT NOT NULL REFERENCES reconstruction_headers(header_id) ON DELETE CASCADE,
 reason TEXT NOT NULL, PRIMARY KEY(source_header_id,target_header_id),
 CHECK(source_header_id <> target_header_id)
);
CREATE TABLE IF NOT EXISTS reconstruction_build_systems (
 build_id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE, mode TEXT NOT NULL,
 generator TEXT NOT NULL, output_root TEXT NOT NULL, metadata_json TEXT NOT NULL,
 created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS reconstruction_build_targets (
 target_id TEXT PRIMARY KEY, build_id TEXT NOT NULL REFERENCES reconstruction_build_systems(build_id) ON DELETE CASCADE,
 name TEXT NOT NULL, target_kind TEXT NOT NULL, output_name TEXT NOT NULL,
 sources_json TEXT NOT NULL, dependencies_json TEXT NOT NULL, UNIQUE(build_id,name)
);
CREATE TABLE IF NOT EXISTS reconstruction_build_variants (
 variant_id TEXT PRIMARY KEY, target_id TEXT NOT NULL REFERENCES reconstruction_build_targets(target_id) ON DELETE CASCADE,
 name TEXT NOT NULL, compiler TEXT NOT NULL, linker TEXT NOT NULL,
 compile_flags_json TEXT NOT NULL, link_flags_json TEXT NOT NULL, environment_json TEXT NOT NULL,
 UNIQUE(target_id,name)
);
CREATE TABLE IF NOT EXISTS reconstruction_build_validations (
 validation_id TEXT PRIMARY KEY, target_id TEXT NOT NULL REFERENCES reconstruction_build_targets(target_id) ON DELETE CASCADE,
 variant_id TEXT REFERENCES reconstruction_build_variants(variant_id) ON DELETE CASCADE,
 status TEXT NOT NULL, checks_json TEXT NOT NULL, created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS reconstruction_abi_contracts (
 contract_id TEXT PRIMARY KEY, subject_kind TEXT NOT NULL, subject_id TEXT NOT NULL,
 architecture TEXT NOT NULL, contract_json TEXT NOT NULL, evidence_json TEXT NOT NULL,
 status TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL,
 UNIQUE(subject_kind,subject_id,architecture)
);
CREATE TABLE IF NOT EXISTS reconstruction_source_provenance (
 provenance_id TEXT PRIMARY KEY, source_path TEXT NOT NULL, line_start INTEGER NOT NULL,
 line_end INTEGER NOT NULL, binary_id TEXT NOT NULL, address_start TEXT NOT NULL,
 address_end TEXT NOT NULL, evidence_json TEXT NOT NULL, confidence REAL NOT NULL CHECK(confidence BETWEEN 0 AND 1),
 created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS reconstruction_source_edits (
 edit_id TEXT PRIMARY KEY, source_path TEXT NOT NULL, before_sha256 TEXT,
 after_sha256 TEXT NOT NULL, semantic INTEGER NOT NULL CHECK(semantic IN (0,1)),
 affected_json TEXT NOT NULL, actor TEXT NOT NULL, created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS reconstruction_proof_invalidations (
 invalidation_id TEXT PRIMARY KEY, edit_id TEXT NOT NULL REFERENCES reconstruction_source_edits(edit_id) ON DELETE CASCADE,
 obligation_id TEXT NOT NULL, reason TEXT NOT NULL, status TEXT NOT NULL, created_at TEXT NOT NULL,
 UNIQUE(edit_id,obligation_id)
);
CREATE TABLE IF NOT EXISTS reconstruction_source_locks (
 source_path TEXT PRIMARY KEY, actor TEXT NOT NULL, reason TEXT NOT NULL, locked_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS reconstruction_generated_tests (
 generated_test_id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE, scope_kind TEXT NOT NULL,
 scope_id TEXT NOT NULL, test_kind TEXT NOT NULL, relative_path TEXT NOT NULL,
 content_sha256 TEXT NOT NULL, applicability_json TEXT NOT NULL, evidence_json TEXT NOT NULL,
 status TEXT NOT NULL, created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS reconstruction_compatibility_shims (
 shim_id TEXT PRIMARY KEY, subject_id TEXT NOT NULL, shim_kind TEXT NOT NULL,
 source_path TEXT NOT NULL, contract_json TEXT NOT NULL, status TEXT NOT NULL,
 created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS reconstruction_capsules (
 capsule_id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE, manifest_json TEXT NOT NULL,
 archive_path TEXT NOT NULL, archive_sha256 TEXT NOT NULL, status TEXT NOT NULL,
 created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS reconstruction_library_matches (
 match_id TEXT PRIMARY KEY, subject_id TEXT NOT NULL, library_name TEXT NOT NULL,
 version_range TEXT, confidence REAL NOT NULL CHECK(confidence BETWEEN 0 AND 1),
 evidence_json TEXT NOT NULL, disposition TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS reconstruction_security_findings (
 finding_id TEXT PRIMARY KEY, rule_id TEXT NOT NULL, severity TEXT NOT NULL,
 subject_id TEXT NOT NULL, summary TEXT NOT NULL, evidence_json TEXT NOT NULL,
 status TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS reconstruction_security_policies (
 policy_id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE, policy_json TEXT NOT NULL,
 created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS reconstruction_semantic_changesets (
 changeset_id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE, base_audit_hash TEXT,
 operations_json TEXT NOT NULL, status TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS reconstruction_merge_conflicts (
 conflict_id TEXT PRIMARY KEY, changeset_id TEXT NOT NULL REFERENCES reconstruction_semantic_changesets(changeset_id) ON DELETE CASCADE,
 conflict_kind TEXT NOT NULL, subject_id TEXT NOT NULL, details_json TEXT NOT NULL,
 status TEXT NOT NULL, resolution_json TEXT, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_reconstruction_members ON reconstruction_module_members(member_kind,member_id);
CREATE INDEX IF NOT EXISTS idx_reconstruction_provenance_source ON reconstruction_source_provenance(source_path,line_start,line_end);
CREATE INDEX IF NOT EXISTS idx_reconstruction_provenance_binary ON reconstruction_source_provenance(binary_id,address_start);
CREATE INDEX IF NOT EXISTS idx_reconstruction_findings ON reconstruction_security_findings(status,severity);
"""

class ReconstructionStore(GovernanceStore):
    """Project-scale schema layered on the governance store."""

    def initialize(self) -> None:
        """Initialize initialize for the current toolkit workflow."""
        super().initialize()
        with self.transaction() as connection:
            connection.executescript(_SCHEMA_SQL)
            row = connection.execute("SELECT value FROM reconstruction_metadata WHERE key='schema_extension_version'").fetchone()
            if row and int(row[0]) > SCHEMA_EXTENSION_VERSION:
                raise ContractError(f"project uses future reconstruction extension schema {row[0]}")
            connection.execute("INSERT INTO reconstruction_metadata(key,value) VALUES('schema_extension_version',?) ON CONFLICT(key) DO UPDATE SET value=excluded.value", (str(SCHEMA_EXTENSION_VERSION),))
            connection.execute("INSERT INTO reconstruction_metadata(key,value) VALUES('release_version','0.7.10') ON CONFLICT(key) DO UPDATE SET value=excluded.value")

    def check(self) -> dict[str, Any]:
        """Check check for the current toolkit workflow."""
        self.initialize()
        base = super().check()
        with self.connect() as connection:
            version = int(connection.execute("SELECT value FROM reconstruction_metadata WHERE key='schema_extension_version'").fetchone()[0])
            tables = int(connection.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name LIKE 'reconstruction_%'").fetchone()[0])
            counts = {row[0]: int(row[1]) for row in connection.execute("SELECT name,(SELECT COUNT(*) FROM pragma_table_info(name)) FROM sqlite_master WHERE type='table' AND name LIKE 'reconstruction_%' ORDER BY name")}
        return {
            **base,
            "release_version": "0.7.10",
            "reconstruction_schema_extension_version": version,
            "reconstruction_table_count": tables,
            "reconstruction_table_columns": counts,
            "passed": bool(base["passed"] and version == SCHEMA_EXTENSION_VERSION),
        }

    @staticmethod
    def decode(row: Any, *json_fields: str) -> dict[str, Any]:
        """Decode configured JSON columns from a SQLite row."""
        return decode_json_fields(row, *json_fields)
