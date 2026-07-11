"""Durable, resumable pipeline orchestration.

Pipeline stages are concrete command executions or explicit evidence gates.  A
stage is never represented by an unimplemented placeholder.  Missing tools or
unmet evidence produce a durable BLOCKED state with an actionable reason.
"""

from __future__ import annotations

import json
import os
import sqlite3
import sys
import time
import uuid
from datetime import datetime, timezone
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Any, Iterable

from .errors import ContractError
from .content_store import ContentStore
from .evidence import EvidenceStore
from .project_state import ProjectStateDatabase, state_database_path
from .util import canonical_json_bytes, copy_file_atomic, load_json, sha256_bytes, sha256_file, utc_now, write_json
from .worker import WorkerLimits, WorkerRequest, execute_worker_request

ORCHESTRATOR_SCHEMA_VERSION = 1


class JobState(StrEnum):
    """Enumerate the lifecycle states a pipeline job can occupy."""
    PENDING = "pending"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    BLOCKED = "blocked"
    CANCELLED = "cancelled"


_SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS pipelines (
    pipeline_id TEXT PRIMARY KEY,
    manifest_sha256 TEXT NOT NULL,
    manifest_path TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    status TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS jobs (
    job_id TEXT PRIMARY KEY,
    pipeline_id TEXT NOT NULL REFERENCES pipelines(pipeline_id) ON DELETE CASCADE,
    stage_id TEXT NOT NULL,
    stage_index INTEGER NOT NULL,
    kind TEXT NOT NULL,
    state TEXT NOT NULL,
    idempotency_key TEXT NOT NULL,
    attempt INTEGER NOT NULL DEFAULT 0,
    command_json TEXT,
    dependencies_json TEXT NOT NULL,
    inputs_json TEXT NOT NULL,
    outputs_json TEXT NOT NULL,
    result_json TEXT,
    error TEXT,
    created_at TEXT NOT NULL,
    started_at TEXT,
    finished_at TEXT,
    cancel_requested INTEGER NOT NULL DEFAULT 0,
    runner_id TEXT,
    heartbeat_at TEXT,
    UNIQUE(pipeline_id, stage_id)
);
CREATE INDEX IF NOT EXISTS jobs_state_idx ON jobs(pipeline_id,state,stage_index);
CREATE TABLE IF NOT EXISTS job_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id TEXT NOT NULL REFERENCES jobs(job_id) ON DELETE CASCADE,
    created_at TEXT NOT NULL,
    event TEXT NOT NULL,
    details_json TEXT NOT NULL
);
"""


@dataclass(frozen=True)
class PipelineStage:
    """Store validated pipeline stage fields used by toolkit reports and adapters."""
    stage_id: str
    kind: str
    dependencies: tuple[str, ...]
    command: tuple[str, ...] | None
    inputs: tuple[str, ...]
    outputs: tuple[str, ...]
    evidence_claim_ids: tuple[str, ...]
    isolation: str
    container_image: str | None
    environment: dict[str, str]
    limits: WorkerLimits

    @classmethod
    def from_dict(cls, value: Any) -> "PipelineStage":
        """Build a :class:`PipelineStage` from a manifest stage mapping.

        Args:
            value: The parsed JSON object describing a single manifest stage.

        Returns:
            A frozen ``PipelineStage`` with validated fields and worker limits.

        Raises:
            ContractError: If ``value`` is not an object, the stage id is missing
                or unsafe, the kind is not ``command`` or ``evidence_gate``, a
                command stage lacks a non-empty command array, an evidence gate
                lacks claim ids, or any typed field violates its schema.
        """
        if not isinstance(value, dict):
            raise ContractError("pipeline stage must be an object")
        stage_id = value.get("id")
        if not isinstance(stage_id, str) or not stage_id or any(ch not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_" for ch in stage_id):
            raise ContractError("pipeline stage id must be a non-empty safe identifier")
        kind = value.get("kind")
        if kind not in ("command", "evidence_gate"):
            raise ContractError("pipeline stage kind must be command or evidence_gate")
        def strings(key: str) -> tuple[str, ...]:
            """Return the value at ``key`` as a tuple of non-empty strings.

            Args:
                key: The manifest field name to read.

            Returns:
                The field value coerced to a tuple of strings, empty if absent.

            Raises:
                ContractError: If the field is present but is not a list of
                    non-empty strings.
            """
            raw = value.get(key, [])
            if not isinstance(raw, list) or not all(isinstance(item, str) and item for item in raw):
                raise ContractError(f"pipeline stage {key} must be a string array")
            return tuple(raw)
        command_raw = value.get("command")
        command: tuple[str, ...] | None = None
        if kind == "command":
            if not isinstance(command_raw, list) or not command_raw or not all(isinstance(item, str) and item for item in command_raw):
                raise ContractError("command stage requires a non-empty command array")
            command = tuple(command_raw)
        claims = strings("evidence_claim_ids")
        if kind == "evidence_gate" and not claims:
            raise ContractError("evidence_gate requires evidence_claim_ids")
        environment = value.get("environment", {})
        if not isinstance(environment, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in environment.items()):
            raise ContractError("pipeline stage environment must be a string map")
        limits_raw = value.get("limits", {})
        if not isinstance(limits_raw, dict):
            raise ContractError("pipeline stage limits must be an object")
        limits = WorkerLimits(
            timeout_seconds=int(limits_raw.get("timeout_seconds", 300)),
            memory_bytes=int(limits_raw.get("memory_bytes", 2 * 1024 * 1024 * 1024)),
            cpu_seconds=int(limits_raw.get("cpu_seconds", 300)),
            max_output_bytes=int(limits_raw.get("max_output_bytes", 16 * 1024 * 1024)),
            max_processes=int(limits_raw.get("max_processes", 512)),
        )
        limits.validate()
        return cls(
            stage_id=stage_id,
            kind=kind,
            dependencies=strings("depends_on"),
            command=command,
            inputs=strings("inputs"),
            outputs=strings("outputs"),
            evidence_claim_ids=claims,
            isolation=str(value.get("isolation", "local_bounded")),
            container_image=value.get("container_image"),
            environment=dict(environment),
            limits=limits,
        )


@dataclass(frozen=True)
class PipelineManifest:
    """Store validated pipeline manifest fields used by toolkit reports and adapters."""
    pipeline_id: str
    project_root: Path
    stages: tuple[PipelineStage, ...]

    @classmethod
    def load(cls, path: Path) -> "PipelineManifest":
        """Load and validate a pipeline manifest from disk.

        Args:
            path: Filesystem path to the manifest JSON file.

        Returns:
            A frozen ``PipelineManifest`` with resolved project root and stages.

        Raises:
            ContractError: If the schema version is not 1, ``pipeline_id`` is
                missing, the stages array is empty, stage ids are not unique, a
                stage references an unknown dependency, or a dependency does not
                precede the stage in manifest order.
        """
        value = load_json(path)
        if not isinstance(value, dict) or value.get("schema_version") != 1:
            raise ContractError("pipeline manifest schema_version must be 1")
        pipeline_id = value.get("pipeline_id")
        if not isinstance(pipeline_id, str) or not pipeline_id:
            raise ContractError("pipeline_id is required")
        project_root = Path(value.get("project_root", "."))
        if not project_root.is_absolute():
            project_root = (path.parent / project_root).resolve()
        stages_raw = value.get("stages")
        if not isinstance(stages_raw, list) or not stages_raw:
            raise ContractError("pipeline stages must be a non-empty array")
        stages = tuple(PipelineStage.from_dict(item) for item in stages_raw)
        identifiers = [stage.stage_id for stage in stages]
        if len(set(identifiers)) != len(identifiers):
            raise ContractError("pipeline stage ids must be unique")
        seen: set[str] = set()
        for stage in stages:
            unknown = set(stage.dependencies) - set(identifiers)
            if unknown:
                raise ContractError(f"stage {stage.stage_id} has unknown dependencies: {sorted(unknown)}")
            if any(dep not in seen for dep in stage.dependencies):
                raise ContractError(f"stage {stage.stage_id} dependencies must precede it in manifest order")
            seen.add(stage.stage_id)
        return cls(pipeline_id, project_root, stages)


class Orchestrator:
    """Durable SQLite-backed executor for registering and running pipelines."""
    def __init__(self, project_root: Path):
        """Initialize Orchestrator with `project_root`."""
        self.project_root = project_root.resolve()
        self.path = self.project_root / "orchestration" / "orchestrator.sqlite3"
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.runner_id = f"runner-{os.getpid()}-{uuid.uuid4().hex[:16]}"
        self.connection = sqlite3.connect(self.path, timeout=30.0, isolation_level=None)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA busy_timeout=30000")
        last_error: sqlite3.OperationalError | None = None
        for _attempt in range(200):
            try:
                self.connection.execute("PRAGMA journal_mode=WAL")
                self.connection.execute("PRAGMA synchronous=FULL")
                self.connection.executescript(_SCHEMA)
                columns = {row[1] for row in self.connection.execute("PRAGMA table_info(jobs)")}
                if "runner_id" not in columns:
                    self.connection.execute("ALTER TABLE jobs ADD COLUMN runner_id TEXT")
                if "heartbeat_at" not in columns:
                    self.connection.execute("ALTER TABLE jobs ADD COLUMN heartbeat_at TEXT")
                last_error = None
                break
            except sqlite3.OperationalError as exc:
                if "locked" not in str(exc).lower():
                    raise
                last_error = exc
                time.sleep(0.025)
        if last_error is not None:
            self.connection.close()
            raise last_error

    def close(self) -> None:
        """Close the underlying SQLite connection."""
        self.connection.close()

    def __enter__(self) -> "Orchestrator":
        """Enter the managed runtime context and return the active resource."""
        return self

    def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None:
        """Exit the managed runtime context and release owned resources."""
        self.close()

    def _transaction(self) -> None:
        """Begin an immediate SQLite transaction to acquire a write lock."""
        self.connection.execute("BEGIN IMMEDIATE")

    def register(self, manifest_path: Path) -> dict[str, Any]:
        """Register a pipeline manifest and create its pending jobs.

        Args:
            manifest_path: Path to the manifest JSON file to register.

        Returns:
            The pipeline status mapping as produced by :meth:`status`.

        Raises:
            ContractError: If the manifest project root does not match the
                orchestrator project, or the pipeline id already exists with a
                different manifest digest.
        """
        manifest = PipelineManifest.load(manifest_path)
        if manifest.project_root != self.project_root:
            raise ContractError("pipeline project_root does not match orchestrator project")
        digest = sha256_file(manifest_path)
        now = utc_now()
        self._transaction()
        try:
            row = self.connection.execute("SELECT manifest_sha256 FROM pipelines WHERE pipeline_id=?", (manifest.pipeline_id,)).fetchone()
            if row is not None and row[0] != digest:
                raise ContractError("pipeline id already exists with a different manifest")
            self.connection.execute(
                "INSERT OR IGNORE INTO pipelines VALUES(?,?,?,?,?,?)",
                (manifest.pipeline_id, digest, str(manifest_path.resolve()), now, now, "pending"),
            )
            for index, stage in enumerate(manifest.stages):
                idempotency = self._idempotency_key(stage)
                job_id = f"job-{manifest.pipeline_id}-{stage.stage_id}"
                self.connection.execute(
                    "INSERT OR IGNORE INTO jobs(job_id,pipeline_id,stage_id,stage_index,kind,state,idempotency_key,command_json,dependencies_json,inputs_json,outputs_json,created_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                    (
                        job_id,
                        manifest.pipeline_id,
                        stage.stage_id,
                        index,
                        stage.kind,
                        JobState.PENDING.value,
                        idempotency,
                        None if stage.command is None else json.dumps(stage.command),
                        json.dumps(stage.dependencies),
                        json.dumps(stage.inputs),
                        json.dumps(stage.outputs),
                        now,
                    ),
                )
            self.connection.execute("COMMIT")
        except Exception:
            self.connection.execute("ROLLBACK")
            raise
        return self.status(manifest.pipeline_id)

    def _idempotency_key(self, stage: PipelineStage) -> str:
        """Compute a content hash identifying a stage's inputs and definition.

        The key hashes the stage definition together with the SHA-256 of each
        existing input file so a stage is re-run when its inputs change.

        Args:
            stage: The pipeline stage to key.

        Returns:
            The hex SHA-256 of the canonical JSON payload for the stage.

        Raises:
            ContractError: If an input path escapes the project root.
        """
        input_hashes: dict[str, str | None] = {}
        for item in stage.inputs:
            path = (self.project_root / item).resolve()
            try:
                path.relative_to(self.project_root)
            except ValueError as exc:
                raise ContractError(f"pipeline input escapes project root: {item}") from exc
            input_hashes[item] = sha256_file(path) if path.is_file() else None
        payload = {
            "stage": stage.stage_id,
            "kind": stage.kind,
            "command": stage.command,
            "dependencies": stage.dependencies,
            "inputs": input_hashes,
            "outputs": stage.outputs,
            "claims": stage.evidence_claim_ids,
            "isolation": stage.isolation,
            "container_image": stage.container_image,
            "environment": stage.environment,
            "limits": vars(stage.limits),
        }
        return sha256_bytes(canonical_json_bytes(payload))

    def _event(self, job_id: str, event: str, details: dict[str, Any]) -> None:
        """Append a job event row inside the current transaction.

        Args:
            job_id: Identifier of the job the event belongs to.
            event: Short event name recorded in the ``job_events`` table.
            details: JSON-serializable details stored with the event.
        """
        self.connection.execute(
            "INSERT INTO job_events(job_id,created_at,event,details_json) VALUES(?,?,?,?)",
            (job_id, utc_now(), event, json.dumps(details, sort_keys=True)),
        )

    def _completed_result_is_intact(self, row: sqlite3.Row) -> bool:
        """Verify materialized outputs before reusing a succeeded job."""
        if row["state"] != JobState.SUCCEEDED.value:
            return False
        try:
            payload = json.loads(row["result_json"] or "{}")
        except json.JSONDecodeError:
            return False
        materialized = payload.get("materialized_outputs", [])
        if not isinstance(materialized, list):
            return False
        for item in materialized:
            if not isinstance(item, dict):
                return False
            path = Path(str(item.get("path", "")))
            if not path.is_absolute():
                path = self.project_root / path
            try:
                path.resolve().relative_to(self.project_root)
            except ValueError:
                return False
            if not path.is_file() or path.is_symlink() or sha256_file(path) != item.get("sha256"):
                return False
        return True

    def _materialize_outputs(
        self, pipeline_id: str, stage: PipelineStage, job_id: str, work: Path
    ) -> list[dict[str, Any]]:
        """Copy a stage's declared outputs into the content store and project.

        Each output is copied atomically from the worker work directory into the
        durable results tree, ingested into the content store, and recorded as a
        project artifact reference.

        Args:
            pipeline_id: Identifier of the owning pipeline.
            stage: The stage whose outputs are being materialized.
            job_id: Identifier of the job that produced the outputs.
            work: The worker work directory containing an ``outputs`` subtree.

        Returns:
            A list of records describing each stored output, including its
            project-relative path, digest, size, and content-store reference.

        Raises:
            ContractError: If a declared output is missing or is an unsafe path
                after a successful worker run.
        """
        destination_root = self.project_root / "orchestration" / "results" / pipeline_id / stage.stage_id
        destination_root.mkdir(parents=True, exist_ok=True)
        store = ContentStore(self.project_root / "artifacts")
        records: list[dict[str, Any]] = []
        with ProjectStateDatabase(state_database_path(self.project_root)) as database:
            for item in stage.outputs:
                source = (work / "outputs" / item).resolve()
                source.relative_to((work / "outputs").resolve())
                if not source.is_file() or source.is_symlink():
                    raise ContractError(f"stage output missing or unsafe after successful worker run: {item}")
                destination = destination_root / item
                destination.parent.mkdir(parents=True, exist_ok=True)
                copy_file_atomic(source, destination)
                stored = store.put_file(
                    destination,
                    attributes={"pipeline_id": pipeline_id, "stage_id": stage.stage_id, "job_id": job_id},
                )
                reference = f"pipeline/{pipeline_id}/{stage.stage_id}/{item}"
                store.add_reference(reference, stored.digest, kind="pipeline_output", owner=job_id)
                database.upsert_artifact_reference(reference, stored.digest, "pipeline_output", job_id)
                records.append(
                    {
                        "output": item,
                        "path": str(destination.relative_to(self.project_root)),
                        "sha256": stored.digest,
                        "size": stored.size,
                        "content_store_reference": reference,
                    }
                )
        return records

    def _dependency_states(self, pipeline_id: str, dependencies: Iterable[str]) -> dict[str, str]:
        """Return the current state of each named dependency stage.

        Args:
            pipeline_id: Identifier of the owning pipeline.
            dependencies: Stage ids whose states should be resolved.

        Returns:
            A mapping of dependency stage id to its job state, or ``"missing"``
            if no job exists for that stage.
        """
        result: dict[str, str] = {}
        for dependency in dependencies:
            row = self.connection.execute(
                "SELECT state FROM jobs WHERE pipeline_id=? AND stage_id=?",
                (pipeline_id, dependency),
            ).fetchone()
            result[dependency] = "missing" if row is None else str(row[0])
        return result

    def run(self, manifest_path: Path, *, stop_on_failure: bool = True) -> dict[str, Any]:
        """Register and execute a pipeline's stages in manifest order.

        Stages with intact idempotent results are skipped. A stage is cancelled,
        blocked, or run depending on its cancel flag and dependency states.

        Args:
            manifest_path: Path to the manifest JSON file to run.
            stop_on_failure: If true, stop at the first stage that ends in a
                FAILED, BLOCKED, or CANCELLED state.

        Returns:
            The final pipeline status mapping as produced by :meth:`status`.
        """
        manifest = PipelineManifest.load(manifest_path)
        self.register(manifest_path)
        for stage in manifest.stages:
            row = self.connection.execute(
                "SELECT * FROM jobs WHERE pipeline_id=? AND stage_id=?",
                (manifest.pipeline_id, stage.stage_id),
            ).fetchone()
            assert row is not None
            if (
                row["state"] == JobState.SUCCEEDED.value
                and row["idempotency_key"] == self._idempotency_key(stage)
                and self._completed_result_is_intact(row)
            ):
                continue
            if row["cancel_requested"]:
                self._set_state(row["job_id"], JobState.CANCELLED, error="cancellation requested")
                if stop_on_failure:
                    break
                continue
            dependency_states = self._dependency_states(manifest.pipeline_id, stage.dependencies)
            if any(value != JobState.SUCCEEDED.value for value in dependency_states.values()):
                self._set_state(row["job_id"], JobState.BLOCKED, error=f"dependencies not satisfied: {dependency_states}")
                if stop_on_failure:
                    break
                continue
            result = self._run_stage(manifest, stage, row["job_id"])
            if result["state"] in (JobState.FAILED.value, JobState.BLOCKED.value, JobState.CANCELLED.value) and stop_on_failure:
                break
        self._update_pipeline_status(manifest.pipeline_id)
        return self.status(manifest.pipeline_id)

    def _set_state(self, job_id: str, state: JobState, *, result: dict[str, Any] | None = None, error: str | None = None) -> None:
        """Transition a job to a new state and record the change event.

        Terminal states set the job's ``finished_at`` timestamp and clear the
        runner assignment and heartbeat.

        Args:
            job_id: Identifier of the job to update.
            state: The new job state to persist.
            result: Optional result payload stored as JSON.
            error: Optional human-readable error recorded with the transition.
        """
        now = utc_now()
        finished = now if state in (JobState.SUCCEEDED, JobState.FAILED, JobState.BLOCKED, JobState.CANCELLED) else None
        self._transaction()
        try:
            self.connection.execute(
                "UPDATE jobs SET state=?,result_json=?,error=?,finished_at=COALESCE(?,finished_at),runner_id=NULL,heartbeat_at=NULL WHERE job_id=?",
                (state.value, None if result is None else json.dumps(result, sort_keys=True), error, finished, job_id),
            )
            self._event(job_id, "state_changed", {"state": state.value, "error": error})
            self.connection.execute("COMMIT")
        except Exception:
            self.connection.execute("ROLLBACK")
            raise

    def _run_stage(self, manifest: PipelineManifest, stage: PipelineStage, job_id: str) -> dict[str, Any]:
        """Claim and execute a single stage, persisting its terminal state.

        The job is atomically claimed by this runner. Evidence gates verify their
        claims through the evidence store, while command stages confine inputs and
        outputs to the work directory and run through the worker sandbox with
        heartbeat-based cancellation checks.

        Args:
            manifest: The manifest containing the stage.
            stage: The stage to execute.
            job_id: Identifier of the job backing the stage.

        Returns:
            A mapping describing the outcome, including the resulting job state
            and, when applicable, the worker result or blocking failures.

        Raises:
            ContractError: If the job id is unknown when claiming the stage.
        """
        now = utc_now()
        current_key = self._idempotency_key(stage)
        self._transaction()
        try:
            current = self.connection.execute("SELECT * FROM jobs WHERE job_id=?", (job_id,)).fetchone()
            if current is None:
                raise ContractError(f"unknown job: {job_id}")
            if current["state"] == JobState.RUNNING.value:
                self.connection.execute("COMMIT")
                return {"state": JobState.RUNNING.value, "claimed": False, "reason": "job is already running"}
            if current["state"] == JobState.SUCCEEDED.value and current["idempotency_key"] == current_key and self._completed_result_is_intact(current):
                self.connection.execute("COMMIT")
                return {"state": JobState.SUCCEEDED.value, "claimed": False, "reason": "intact idempotent result reused"}
            cursor = self.connection.execute(
                "UPDATE jobs SET state=?,attempt=attempt+1,started_at=?,finished_at=NULL,error=NULL,idempotency_key=?,cancel_requested=0,runner_id=?,heartbeat_at=? WHERE job_id=? AND state<>?",
                (JobState.RUNNING.value, now, current_key, self.runner_id, now, job_id, JobState.RUNNING.value),
            )
            if cursor.rowcount != 1:
                self.connection.execute("COMMIT")
                return {"state": JobState.RUNNING.value, "claimed": False, "reason": "job claim lost to another worker"}
            self._event(job_id, "started", {"stage_id": stage.stage_id})
            self.connection.execute("COMMIT")
        except Exception:
            self.connection.execute("ROLLBACK")
            raise
        if stage.kind == "evidence_gate":
            store = EvidenceStore(self.project_root)
            failures: list[str] = []
            for claim_id in stage.evidence_claim_ids:
                try:
                    store.require_verified(claim_id)
                except Exception as exc:
                    failures.append(f"{claim_id}: {exc}")
            if failures:
                self._set_state(job_id, JobState.BLOCKED, error="; ".join(failures))
                return {"state": JobState.BLOCKED.value, "failures": failures}
            result = {"claims_verified": list(stage.evidence_claim_ids)}
            self._set_state(job_id, JobState.SUCCEEDED, result=result)
            return {"state": JobState.SUCCEEDED.value, **result}
        work = self.project_root / "orchestration" / "work" / job_id
        logs = self.project_root / "orchestration" / "logs" / job_id
        work.mkdir(parents=True, exist_ok=True)
        # Inputs and outputs are relative to the project.  Symlink them into the
        # stage work directory only after path confinement checks.
        input_paths: list[Path] = []
        output_paths: list[Path] = []
        for item in stage.inputs:
            source = (self.project_root / item).resolve()
            source.relative_to(self.project_root)
            if not source.is_file() or source.is_symlink():
                self._set_state(job_id, JobState.BLOCKED, error=f"input missing or unsafe: {item}")
                return {"state": JobState.BLOCKED.value, "error": f"input missing or unsafe: {item}"}
            destination = work / "inputs" / item
            destination.parent.mkdir(parents=True, exist_ok=True)
            if not destination.exists():
                destination.write_bytes(source.read_bytes())
            input_paths.append(destination.relative_to(work))
        for item in stage.outputs:
            destination = work / "outputs" / item
            destination.parent.mkdir(parents=True, exist_ok=True)
            output_paths.append(destination.relative_to(work))
        command = tuple(
            item.replace("{project}", str(self.project_root)).replace("{work}", str(work))
            for item in (stage.command or ())
        )
        request = WorkerRequest(
            command=command,
            working_directory=work,
            environment=stage.environment,
            input_files=tuple(input_paths),
            expected_outputs=tuple(output_paths),
            isolation=stage.isolation,
            container_image=stage.container_image,
            limits=stage.limits,
        )
        last_heartbeat = [0.0]

        def cancellation_requested() -> bool:
            """Refresh the runner heartbeat and report any cancellation request.

            Returns:
                True if the job's ``cancel_requested`` flag is set.
            """
            now_monotonic = time.monotonic()
            if now_monotonic - last_heartbeat[0] >= 2.0:
                self.connection.execute(
                    "UPDATE jobs SET heartbeat_at=? WHERE job_id=? AND runner_id=? AND state=?",
                    (utc_now(), job_id, self.runner_id, JobState.RUNNING.value),
                )
                last_heartbeat[0] = now_monotonic
            row = self.connection.execute("SELECT cancel_requested FROM jobs WHERE job_id=?", (job_id,)).fetchone()
            return bool(row and row[0])

        result = execute_worker_request(
            request,
            log_directory=logs,
            report_path=logs / "worker-result.json",
            cancel_check=cancellation_requested,
        )
        if result.status == "passed":
            state = JobState.SUCCEEDED
        elif result.status == "cancelled":
            state = JobState.CANCELLED
        elif result.status == "error" and "requires" in (result.error or ""):
            state = JobState.BLOCKED
        else:
            state = JobState.FAILED
        payload = result.to_dict()
        if state == JobState.SUCCEEDED:
            payload["materialized_outputs"] = self._materialize_outputs(manifest.pipeline_id, stage, job_id, work)
        self._set_state(job_id, state, result=payload, error=result.error)
        return {"state": state.value, "worker": payload}

    def recover_stale_jobs(self, *, pipeline_id: str | None = None, stale_seconds: int = 600) -> dict[str, Any]:
        """Reset only RUNNING jobs whose durable heartbeat is older than the bound."""
        if stale_seconds <= 0:
            raise ContractError("stale_seconds must be positive")
        now = datetime.now(timezone.utc)
        if pipeline_id is None:
            rows = self.connection.execute(
                "SELECT job_id,pipeline_id,stage_id,heartbeat_at,started_at FROM jobs WHERE state=?",
                (JobState.RUNNING.value,),
            ).fetchall()
        else:
            rows = self.connection.execute(
                "SELECT job_id,pipeline_id,stage_id,heartbeat_at,started_at FROM jobs WHERE state=? AND pipeline_id=?",
                (JobState.RUNNING.value, pipeline_id),
            ).fetchall()
        stale: list[sqlite3.Row] = []
        for row in rows:
            timestamp = row["heartbeat_at"] or row["started_at"]
            if not timestamp:
                stale.append(row)
                continue
            parsed = datetime.fromisoformat(str(timestamp).replace("Z", "+00:00"))
            if (now - parsed).total_seconds() >= stale_seconds:
                stale.append(row)
        self._transaction()
        try:
            for row in stale:
                self.connection.execute(
                    "UPDATE jobs SET state=?,runner_id=NULL,heartbeat_at=NULL,cancel_requested=0,error=?,started_at=NULL,finished_at=NULL WHERE job_id=? AND state=?",
                    (JobState.PENDING.value, "recovered after stale runner heartbeat", row["job_id"], JobState.RUNNING.value),
                )
                self._event(row["job_id"], "stale_job_recovered", {"stale_seconds": stale_seconds})
            self.connection.execute("COMMIT")
        except Exception:
            self.connection.execute("ROLLBACK")
            raise
        for pid in sorted({str(row["pipeline_id"]) for row in stale}):
            self._update_pipeline_status(pid)
        return {
            "stale_seconds": stale_seconds,
            "pipeline_id": pipeline_id,
            "jobs_recovered": len(stale),
            "job_ids": [str(row["job_id"]) for row in stale],
        }

    def cancel(self, pipeline_id: str, stage_id: str | None = None) -> dict[str, Any]:
        """Request cancellation of pending or running jobs.

        Args:
            pipeline_id: Identifier of the pipeline to cancel.
            stage_id: If given, cancel only this stage; otherwise cancel every
                pending or running stage in the pipeline.

        Returns:
            A mapping recording the pipeline, stage, and number of cancel
            requests applied.
        """
        self._transaction()
        try:
            if stage_id is None:
                cursor = self.connection.execute(
                    "UPDATE jobs SET cancel_requested=1 WHERE pipeline_id=? AND state IN (?,?)",
                    (pipeline_id, JobState.PENDING.value, JobState.RUNNING.value),
                )
            else:
                cursor = self.connection.execute(
                    "UPDATE jobs SET cancel_requested=1 WHERE pipeline_id=? AND stage_id=? AND state IN (?,?)",
                    (pipeline_id, stage_id, JobState.PENDING.value, JobState.RUNNING.value),
                )
            self.connection.execute("COMMIT")
        except Exception:
            self.connection.execute("ROLLBACK")
            raise
        return {"pipeline_id": pipeline_id, "stage_id": stage_id, "cancel_requests": cursor.rowcount}

    def retry(self, pipeline_id: str, stage_id: str, *, cascade: bool = False) -> dict[str, Any]:
        """Reset a stage back to PENDING so it can run again.

        Args:
            pipeline_id: Identifier of the owning pipeline.
            stage_id: Identifier of the stage to retry.
            cascade: If true, also reset every stage at or after this stage's
                index; otherwise reset only the named stage.

        Returns:
            A mapping recording the pipeline, stage, cascade flag, and number of
            jobs reset.

        Raises:
            ContractError: If the pipeline stage is unknown.
        """
        row = self.connection.execute(
            "SELECT stage_index FROM jobs WHERE pipeline_id=? AND stage_id=?",
            (pipeline_id, stage_id),
        ).fetchone()
        if row is None:
            raise ContractError("unknown pipeline stage")
        self._transaction()
        try:
            if cascade:
                cursor = self.connection.execute(
                    "UPDATE jobs SET state=?,cancel_requested=0,error=NULL,result_json=NULL,started_at=NULL,finished_at=NULL WHERE pipeline_id=? AND stage_index>=?",
                    (JobState.PENDING.value, pipeline_id, row[0]),
                )
            else:
                cursor = self.connection.execute(
                    "UPDATE jobs SET state=?,cancel_requested=0,error=NULL,result_json=NULL,started_at=NULL,finished_at=NULL WHERE pipeline_id=? AND stage_id=?",
                    (JobState.PENDING.value, pipeline_id, stage_id),
                )
            self.connection.execute("COMMIT")
        except Exception:
            self.connection.execute("ROLLBACK")
            raise
        return {"pipeline_id": pipeline_id, "stage_id": stage_id, "cascade": cascade, "jobs_reset": cursor.rowcount}

    def _update_pipeline_status(self, pipeline_id: str) -> None:
        """Recompute and persist a pipeline's aggregate status from its jobs.

        The status is derived from the job states: ``succeeded`` only when all
        jobs succeed, otherwise the first of failed, blocked, running, cancelled,
        or pending that applies.

        Args:
            pipeline_id: Identifier of the pipeline to update.
        """
        states = [str(row[0]) for row in self.connection.execute("SELECT state FROM jobs WHERE pipeline_id=?", (pipeline_id,))]
        if states and all(state == JobState.SUCCEEDED.value for state in states):
            status = "succeeded"
        elif any(state == JobState.FAILED.value for state in states):
            status = "failed"
        elif any(state == JobState.BLOCKED.value for state in states):
            status = "blocked"
        elif any(state == JobState.RUNNING.value for state in states):
            status = "running"
        elif any(state == JobState.CANCELLED.value for state in states):
            status = "cancelled"
        else:
            status = "pending"
        self.connection.execute("UPDATE pipelines SET status=?,updated_at=? WHERE pipeline_id=?", (status, utc_now(), pipeline_id))

    def status(self, pipeline_id: str) -> dict[str, Any]:
        """Return a serializable status snapshot for a pipeline.

        Args:
            pipeline_id: Identifier of the pipeline to report.

        Returns:
            A mapping with the schema version, pipeline id, aggregate status,
            manifest digest, and a per-job summary ordered by stage index.

        Raises:
            ContractError: If the pipeline id is unknown.
        """
        pipeline = self.connection.execute("SELECT * FROM pipelines WHERE pipeline_id=?", (pipeline_id,)).fetchone()
        if pipeline is None:
            raise ContractError(f"unknown pipeline: {pipeline_id}")
        jobs = []
        for row in self.connection.execute("SELECT * FROM jobs WHERE pipeline_id=? ORDER BY stage_index", (pipeline_id,)):
            jobs.append(
                {
                    "job_id": row["job_id"],
                    "stage_id": row["stage_id"],
                    "kind": row["kind"],
                    "state": row["state"],
                    "attempt": row["attempt"],
                    "idempotency_key": row["idempotency_key"],
                    "error": row["error"],
                    "created_at": row["created_at"],
                    "started_at": row["started_at"],
                    "finished_at": row["finished_at"],
                    "runner_id": row["runner_id"],
                    "heartbeat_at": row["heartbeat_at"],
                }
            )
        return {
            "schema_version": ORCHESTRATOR_SCHEMA_VERSION,
            "pipeline_id": pipeline_id,
            "status": pipeline["status"],
            "manifest_sha256": pipeline["manifest_sha256"],
            "jobs": jobs,
        }


def create_default_pipeline(project_root: Path, output: Path, *, include_ghidra: bool = True) -> dict[str, Any]:
    """Generate a concrete pipeline for the current project.

    The generated stages invoke real toolkit commands.  Ghidra is included only
    when requested and becomes BLOCKED at runtime if its configured executable
    is unavailable; no fake analysis output is generated.
    """
    root = project_root.resolve()
    project = load_json(root / "project.json")
    binary = Path(project["binary"]["path"])
    if not binary.is_absolute():
        binary = root / binary
    stages: list[dict[str, Any]] = [
        {
            "id": "verify-project",
            "kind": "command",
            "command": [sys.executable, "-m", "x86decomp", "verify-project", "{project}"],
            "outputs": [],
        },
        {
            "id": "metadata-scan",
            "kind": "command",
            "depends_on": ["verify-project"],
            "command": [
                sys.executable,
                "-m",
                "x86decomp",
                "metadata-scan",
                str(binary),
                "--report",
                "{work}/outputs/metadata.json",
            ],
            "outputs": ["metadata.json"],
        },
        {
            "id": "image-profile",
            "kind": "command",
            "depends_on": ["verify-project"],
            "command": [
                sys.executable,
                "-m",
                "x86decomp",
                "image-profile",
                str(binary),
                "{work}/outputs/image-profile.json",
            ],
            "outputs": ["image-profile.json"],
        },
    ]
    if include_ghidra:
        stages.append(
            {
                "id": "ghidra-export",
                "kind": "command",
                "depends_on": ["verify-project"],
                "command": [
                    sys.executable,
                    "-m",
                    "x86decomp",
                    "ghidra-export",
                    str(binary),
                    "{project}/analysis/ghidra",
                    project["project_id"],
                    "{work}/outputs/ghidra-export",
                    "--scripts-dir",
                    "{project}/ghidra_scripts",
                ],
                "outputs": [],
            }
        )
    source_pythonpath = os.pathsep.join(filter(None, [str(Path(__file__).resolve().parents[1]), os.environ.get("PYTHONPATH", "")]))
    for stage in stages:
        stage.setdefault("environment", {})["PYTHONPATH"] = source_pythonpath
    manifest = {
        "schema_version": 1,
        "pipeline_id": f"default-{project['project_id']}",
        "project_root": str(root),
        "created_at": utc_now(),
        "stages": stages,
    }
    write_json(output, manifest)
    return manifest
