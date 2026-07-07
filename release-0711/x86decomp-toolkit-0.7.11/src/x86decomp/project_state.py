"""Transactional project-state database, migrations, backup, and recovery.

This module is intentionally independent from the analysis and work-queue
SQLite databases.  It owns release/schema migration history, durable job state,
artifact references, and project integrity snapshots.
"""

from __future__ import annotations

import gzip
import json
import os
import shutil
import sqlite3
import tarfile
import tempfile
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator

from .content_store import ContentStore
from .errors import ContractError
from .util import canonical_json_bytes, load_json, sha256_bytes, sha256_file, utc_now, write_json

STATE_DB_SCHEMA_VERSION = 1
PROJECT_SCHEMA_VERSION = 3

_SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS schema_metadata (
    singleton INTEGER PRIMARY KEY CHECK (singleton = 1),
    schema_version INTEGER NOT NULL,
    toolkit_version TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS migrations (
    migration_id TEXT PRIMARY KEY,
    from_version INTEGER NOT NULL,
    to_version INTEGER NOT NULL,
    applied_at TEXT NOT NULL,
    pre_project_sha256 TEXT NOT NULL,
    post_project_sha256 TEXT NOT NULL,
    backup_path TEXT
);
CREATE TABLE IF NOT EXISTS project_snapshots (
    snapshot_id TEXT PRIMARY KEY,
    created_at TEXT NOT NULL,
    project_json_sha256 TEXT NOT NULL,
    binary_sha256 TEXT NOT NULL,
    state_json TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS artifact_references (
    reference TEXT PRIMARY KEY,
    sha256 TEXT NOT NULL,
    kind TEXT NOT NULL,
    owner TEXT NOT NULL,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS leases (
    lease_name TEXT PRIMARY KEY,
    owner TEXT NOT NULL,
    acquired_at TEXT NOT NULL,
    expires_at_epoch REAL NOT NULL
);
"""


@dataclass(frozen=True)
class ProjectCheck:
    """Immutable result of a project integrity check.

    Records overall validity (``valid``), the ordered ``failures`` and ``warnings``
    collected during the check, and the observed ``project_schema_version`` and
    ``state_db_schema_version`` (``None`` when they could not be read).
    """
    valid: bool
    failures: tuple[str, ...]
    warnings: tuple[str, ...]
    project_schema_version: int | None
    state_db_schema_version: int | None

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "valid": self.valid,
            "failures": list(self.failures),
            "warnings": list(self.warnings),
            "project_schema_version": self.project_schema_version,
            "state_db_schema_version": self.state_db_schema_version,
        }


class ProjectStateDatabase:
    """SQLite-backed store for project schema history, snapshots, and artifact references.

    Manages a WAL-mode connection that owns the schema-metadata, migrations,
    project-snapshot, artifact-reference, and lease tables. Usable as a context
    manager; validates the on-disk schema version on open.
    """
    def __init__(self, path: Path, *, toolkit_version: str = "0.7.11"):
        """Open (creating if needed) the project-state database at ``path``.

        Creates the parent directory, opens a WAL/synchronous-FULL connection, applies the
        schema, and inserts or validates the schema-metadata row.

        Args:
            path: Filesystem path to the SQLite database file.
            toolkit_version: Toolkit version recorded in schema metadata on first creation.

        Raises:
            ContractError: If the existing database schema version is not supported.
        """
        self.path = path.resolve()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(self.path, timeout=30.0, isolation_level=None)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA journal_mode=WAL")
        self.connection.execute("PRAGMA synchronous=FULL")
        self.connection.executescript(_SCHEMA)
        row = self.connection.execute("SELECT schema_version FROM schema_metadata WHERE singleton=1").fetchone()
        if row is None:
            self.connection.execute(
                "INSERT INTO schema_metadata(singleton,schema_version,toolkit_version,updated_at) VALUES(1,?,?,?)",
                (STATE_DB_SCHEMA_VERSION, toolkit_version, utc_now()),
            )
        elif int(row["schema_version"]) != STATE_DB_SCHEMA_VERSION:
            raise ContractError(f"unsupported project-state database schema: {row['schema_version']}")

    def close(self) -> None:
        """Close the underlying SQLite connection."""
        self.connection.close()

    def __enter__(self) -> "ProjectStateDatabase":
        """Enter the managed runtime context and return the active resource."""
        return self

    def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None:
        """Exit the managed runtime context and release owned resources."""
        self.close()

    @contextmanager
    def transaction(self, *, immediate: bool = True) -> Iterator[sqlite3.Connection]:
        """Run a block inside a SQLite transaction, committing on success.

        Args:
            immediate: If ``True``, begin with ``BEGIN IMMEDIATE`` to take a write lock
                eagerly; otherwise use a deferred ``BEGIN``.

        Yields:
            The active SQLite connection.

        Raises:
            Exception: Re-raises any exception from the block after issuing ``ROLLBACK``.
        """
        self.connection.execute("BEGIN IMMEDIATE" if immediate else "BEGIN")
        try:
            yield self.connection
        except Exception:
            self.connection.execute("ROLLBACK")
            raise
        else:
            self.connection.execute("COMMIT")

    def integrity_check(self) -> list[str]:
        """Run SQLite ``PRAGMA integrity_check`` on the database.

        Returns:
            The integrity-check result rows as strings (``["ok"]`` when healthy).
        """
        rows = self.connection.execute("PRAGMA integrity_check").fetchall()
        return [str(row[0]) for row in rows]

    def record_migration(
        self,
        *,
        migration_id: str,
        from_version: int,
        to_version: int,
        pre_hash: str,
        post_hash: str,
        backup_path: str | None,
    ) -> None:
        """Insert a migration audit row and refresh schema-metadata in one transaction.

        Args:
            migration_id: Unique identifier for the migration record.
            from_version: Project schema version migrated from.
            to_version: Project schema version migrated to.
            pre_hash: SHA-256 of ``project.json`` before the migration.
            post_hash: SHA-256 of ``project.json`` after the migration.
            backup_path: Path to the pre-migration backup, or ``None``.
        """
        with self.transaction():
            self.connection.execute(
                "INSERT INTO migrations VALUES(?,?,?,?,?,?,?)",
                (migration_id, from_version, to_version, utc_now(), pre_hash, post_hash, backup_path),
            )
            self.connection.execute(
                "UPDATE schema_metadata SET toolkit_version=?, updated_at=? WHERE singleton=1",
                ("0.7.11", utc_now()),
            )

    def snapshot(self, project_root: Path) -> dict[str, Any]:
        """Record an integrity snapshot of the project into the snapshots table.

        Args:
            project_root: Project root directory containing ``project.json``.

        Returns:
            A dictionary with the generated ``snapshot_id``, the ``project_json_sha256``,
            and the captured project ``state``.
        """
        root = project_root.resolve()
        project = load_json(root / "project.json")
        binary_path = Path(project["binary"]["path"])
        if not binary_path.is_absolute():
            binary_path = root / binary_path
        state = {
            "project_id": project["project_id"],
            "schema_version": project["schema_version"],
            "status": project["status"],
            "binary_path": str(binary_path),
        }
        project_hash = sha256_file(root / "project.json")
        snapshot_id = sha256_bytes(canonical_json_bytes({"project": project_hash, "state": state, "time": utc_now()}))[:24]
        with self.transaction():
            self.connection.execute(
                "INSERT INTO project_snapshots VALUES(?,?,?,?,?)",
                (snapshot_id, utc_now(), project_hash, project["binary"]["sha256"], json.dumps(state, sort_keys=True)),
            )
        return {"snapshot_id": snapshot_id, "project_json_sha256": project_hash, "state": state}

    def upsert_artifact_reference(self, reference: str, digest: str, kind: str, owner: str) -> None:
        """Insert or update an artifact reference row.

        Args:
            reference: Stable reference key for the artifact.
            digest: SHA-256 content digest of the artifact.
            kind: Artifact kind label.
            owner: Owner label for the artifact.
        """
        with self.transaction():
            self.connection.execute(
                "INSERT INTO artifact_references(reference,sha256,kind,owner,created_at) VALUES(?,?,?,?,?) "
                "ON CONFLICT(reference) DO UPDATE SET sha256=excluded.sha256,kind=excluded.kind,owner=excluded.owner,created_at=excluded.created_at",
                (reference, digest, kind, owner, utc_now()),
            )

    def artifact_digests(self) -> set[str]:
        """Return the set of SHA-256 digests recorded in the artifact-reference table.

        Returns:
            The distinct artifact content digests.
        """
        return {str(row[0]) for row in self.connection.execute("SELECT sha256 FROM artifact_references")}


def state_database_path(project_root: Path) -> Path:
    """Return the conventional project-state database path under ``project_root``.

    Args:
        project_root: Project root directory.

    Returns:
        The path ``<project_root>/state/project-state.sqlite3``.
    """
    return project_root.resolve() / "state" / "project-state.sqlite3"


def create_project_backup(project_root: Path, output: Path) -> dict[str, Any]:
    """Create a deterministic gzip tar backup without following symlinks."""
    root = project_root.resolve()
    if not (root / "project.json").is_file():
        raise ContractError("project backup requires project.json")
    output = output.resolve()
    if output.is_relative_to(root):
        raise ContractError("backup output must be outside the project tree")
    output.parent.mkdir(parents=True, exist_ok=True)
    entries: list[Path] = []
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ContractError(f"project contains a symlink and cannot be safely backed up: {path}")
        if path.is_file():
            entries.append(path)
    fd, temporary = tempfile.mkstemp(prefix=f".{output.name}.", dir=output.parent)
    os.close(fd)
    try:
        with open(temporary, "wb") as raw, gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as compressed:
            with tarfile.open(fileobj=compressed, mode="w", format=tarfile.PAX_FORMAT) as archive:
                for path in entries:
                    arcname = Path(root.name) / path.relative_to(root)
                    info = archive.gettarinfo(str(path), arcname=str(arcname))
                    info.uid = info.gid = 0
                    info.uname = info.gname = ""
                    info.mtime = 0
                    info.mode = 0o644
                    with path.open("rb") as handle:
                        archive.addfile(info, handle)
        os.replace(temporary, output)
    finally:
        Path(temporary).unlink(missing_ok=True)
    return {"path": str(output), "sha256": sha256_file(output), "file_count": len(entries), "size": output.stat().st_size}


def _migration_2_to_3(root: Path, project: dict[str, Any]) -> dict[str, Any]:
    """Apply the schema 2 to 3 project migration on disk.

    Creates the v3 directory layout, initializes the project-state database and content
    store, and returns the updated project mapping with v3 fields.

    Args:
        root: Resolved project root directory.
        project: Current (schema 2) project mapping.

    Returns:
        The updated project mapping with ``schema_version`` 3 and v3 layout fields.
    """
    for directory in (
        "state",
        "artifacts",
        "orchestration/pipelines",
        "orchestration/logs",
        "orchestration/work",
        "target-pack",
        "reports/reproducibility",
        "reports/convergence",
        "reports/security",
        "templates",
    ):
        (root / directory).mkdir(parents=True, exist_ok=True)
    with ProjectStateDatabase(state_database_path(root)):
        pass
    ContentStore(root / "artifacts")
    updated = dict(project)
    updated.update(
        {
            "schema_version": 3,
            "toolkit_release": "0.7.11",
            "project_state_database": "state/project-state.sqlite3",
            "content_store": "artifacts",
            "target_pack": updated.get("target_pack", "target-pack/target.toml"),
            "orchestration_root": "orchestration",
        }
    )
    return updated


def migrate_project(
    project_root: Path,
    *,
    dry_run: bool = False,
    backup_path: Path | None = None,
) -> dict[str, Any]:
    """Migrate ``project.json`` forward to schema version 3, with backup and audit.

    Supports migrating from schema 1 or 2; version 3 is a no-op. Unless ``dry_run`` is set,
    a pre-migration backup is created, the project file is rewritten, and the migration is
    recorded with a snapshot in the project-state database.

    Args:
        project_root: Project root directory containing ``project.json``.
        dry_run: If ``True``, compute and return the plan without modifying anything.
        backup_path: Optional explicit backup destination; defaults to a sibling of the root.

    Returns:
        A result dictionary describing the change, version transition, plan, and (when
        applied) backup and snapshot details.

    Raises:
        ContractError: If ``project.json`` is not an object or its schema version is unsupported.
    """
    root = project_root.resolve()
    project_path = root / "project.json"
    project = load_json(project_path)
    if not isinstance(project, dict):
        raise ContractError("project.json must contain an object")
    current = project.get("schema_version")
    if current not in (1, 2, 3):
        raise ContractError(f"unsupported project schema version: {current}")
    if current == 3:
        return {"changed": False, "from_version": 3, "to_version": 3, "dry_run": dry_run}
    plan = []
    working = dict(project)
    if current == 1:
        # Schema 1 predates mode-aware state.  Preserve fields and add v2 fields.
        architecture = working.get("architecture", "x86")
        working.update(
            {
                "schema_version": 2,
                "architecture": architecture,
                "default_modes": ["matching", "functional"],
                "analysis_database": working.get("analysis_database", "analysis/database/analysis.sqlite3"),
                "work_queue": working.get("work_queue", "work/tasks.sqlite3"),
            }
        )
        plan.append("1->2")
    working = _migration_2_to_3(root, working) if not dry_run else {**working, "schema_version": 3, "toolkit_release": "0.7.11"}
    plan.append("2->3")
    if dry_run:
        return {"changed": True, "from_version": current, "to_version": 3, "dry_run": True, "plan": plan, "project_preview": working}
    if backup_path is None:
        backup_path = root.parent / f"{root.name}-pre-migration-backup.tar.gz"
    backup = create_project_backup(root, backup_path)
    pre_hash = sha256_file(project_path)
    write_json(project_path, working)
    post_hash = sha256_file(project_path)
    with ProjectStateDatabase(state_database_path(root)) as database:
        database.record_migration(
            migration_id=f"project-{current}-to-3-{post_hash[:12]}",
            from_version=int(current),
            to_version=3,
            pre_hash=pre_hash,
            post_hash=post_hash,
            backup_path=backup["path"],
        )
        snapshot = database.snapshot(root)
    return {
        "changed": True,
        "from_version": current,
        "to_version": 3,
        "dry_run": False,
        "plan": plan,
        "backup": backup,
        "snapshot": snapshot,
    }


def check_project_state(project_root: Path) -> ProjectCheck:
    """Validate a project on disk and collect integrity failures and warnings.

    Checks the project schema version, binary presence and hash, the project-state
    database integrity and schema version, and the content store.

    Args:
        project_root: Project root directory to check.

    Returns:
        A :class:`ProjectCheck` summarizing validity, failures, warnings, and versions.
    """
    root = project_root.resolve()
    failures: list[str] = []
    warnings: list[str] = []
    project_version: int | None = None
    database_version: int | None = None
    try:
        project = load_json(root / "project.json")
        project_version = project.get("schema_version")
        if project_version != 3:
            failures.append(f"project schema is {project_version}; migrate to 3")
        binary = Path(project["binary"]["path"])
        if not binary.is_absolute():
            binary = root / binary
        if not binary.is_file():
            failures.append(f"binary is missing: {binary}")
        elif sha256_file(binary) != project["binary"]["sha256"]:
            failures.append("binary hash mismatch")
        state_path = root / str(project.get("project_state_database", "state/project-state.sqlite3"))
        if not state_path.is_file():
            failures.append("project-state database is missing")
        else:
            with ProjectStateDatabase(state_path) as database:
                rows = database.integrity_check()
                if rows != ["ok"]:
                    failures.extend(f"state database: {item}" for item in rows)
                row = database.connection.execute("SELECT schema_version FROM schema_metadata WHERE singleton=1").fetchone()
                database_version = int(row[0]) if row else None
        store_path = root / str(project.get("content_store", "artifacts"))
        if store_path.exists():
            result = ContentStore(store_path).verify()
            failures.extend(f"content store: {item}" for item in result["failures"])
        else:
            warnings.append("content store does not exist yet")
    except Exception as exc:
        failures.append(str(exc))
    return ProjectCheck(not failures, tuple(failures), tuple(warnings), project_version, database_version)


def repair_project_state(project_root: Path, *, dry_run: bool = True) -> dict[str, Any]:
    """Repair only reconstructible indexes; never rewrite evidence or binaries."""
    root = project_root.resolve()
    actions: list[dict[str, Any]] = []
    project = load_json(root / "project.json")
    state_path = root / str(project.get("project_state_database", "state/project-state.sqlite3"))
    if not state_path.exists():
        actions.append({"action": "create_project_state_database", "path": str(state_path)})
        if not dry_run:
            with ProjectStateDatabase(state_path):
                pass
    store_path = root / str(project.get("content_store", "artifacts"))
    if not store_path.exists():
        actions.append({"action": "create_content_store", "path": str(store_path)})
        if not dry_run:
            ContentStore(store_path)
    # Rebuild missing content-store references from state DB, but never delete.
    if state_path.exists() and store_path.exists():
        store = ContentStore(store_path)
        with ProjectStateDatabase(state_path) as database:
            rows = database.connection.execute("SELECT reference,sha256,kind,owner FROM artifact_references").fetchall()
            existing = json.loads(store.references_path.read_text(encoding="utf-8")).get("references", {})
            for row in rows:
                if row["reference"] not in existing:
                    actions.append({"action": "restore_artifact_reference", "reference": row["reference"], "sha256": row["sha256"]})
                    if not dry_run:
                        store.add_reference(row["reference"], row["sha256"], kind=row["kind"], owner=row["owner"])
    return {"dry_run": dry_run, "actions": actions, "changed": bool(actions) and not dry_run}


def project_gc(project_root: Path, *, dry_run: bool = True) -> dict[str, Any]:
    """Garbage-collect the project content store.

    Args:
        project_root: Project root directory containing ``project.json``.
        dry_run: If ``True``, report reclaimable objects without deleting them.

    Returns:
        The content store garbage-collection result dictionary.
    """
    root = project_root.resolve()
    project = load_json(root / "project.json")
    return ContentStore(root / str(project.get("content_store", "artifacts"))).garbage_collect(dry_run=dry_run)


def restore_project_backup(archive_path: Path, destination: Path) -> dict[str, Any]:
    """Safely restore a project backup into an empty destination."""
    archive_path = archive_path.resolve()
    destination = destination.resolve()
    if not archive_path.is_file() or archive_path.is_symlink():
        raise ContractError(f"backup archive is missing or unsafe: {archive_path}")
    if destination.exists() and any(destination.iterdir()):
        raise ContractError(f"restore destination is not empty: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f".{destination.name}.restore-", dir=destination.parent) as temporary:
        staging = Path(temporary)
        with tarfile.open(archive_path, "r:gz") as archive:
            members = archive.getmembers()
            if not members:
                raise ContractError("backup archive is empty")
            if len(members) > 100_000:
                raise ContractError("backup contains more than 100000 members")
            roots = {Path(member.name).parts[0] for member in members if Path(member.name).parts}
            if len(roots) != 1:
                raise ContractError("backup archive must contain exactly one project root")
            root_name = next(iter(roots))
            total = 0
            for member in members:
                path = Path(member.name)
                if path.is_absolute() or ".." in path.parts:
                    raise ContractError(f"unsafe backup member: {member.name}")
                if member.issym() or member.islnk() or member.isdev():
                    raise ContractError(f"unsupported backup member type: {member.name}")
                if member.size > 2 * 1024 * 1024 * 1024:
                    raise ContractError(f"backup member exceeds 2 GiB safety limit: {member.name}")
                total += max(member.size, 0)
                if total > 8 * 1024 * 1024 * 1024:
                    raise ContractError("backup expands beyond 8 GiB safety limit")
            archive.extractall(staging, filter="data")
        extracted_root = staging / root_name
        if not (extracted_root / "project.json").is_file():
            raise ContractError("backup does not contain project.json")
        destination.mkdir(parents=True, exist_ok=True)
        try:
            for item in extracted_root.iterdir():
                shutil.move(str(item), destination / item.name)
        except Exception:
            shutil.rmtree(destination, ignore_errors=True)
            raise
    check = check_project_state(destination)
    return {"restored": True, "destination": str(destination), "archive_sha256": sha256_file(archive_path), "check": check.to_dict()}
