"""Optional read-only FastAPI service for project, pipeline, and validation state.

The service never mutates project state.  It exposes durable records produced by
CLI workers and validators so an analyst can inspect a project without granting
the web process write authority.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

from . import __version__
from .errors import ExternalToolError
from .project import verify_project
from .project_state import check_project_state
from .util import load_json
from .work_queue import WorkQueue
from .workflow import load_function_workflow
from .worker import discover_worker_capabilities


def _json_files(directory: Path) -> list[dict[str, Any]]:
    """Load every JSON file under a directory into a list of report entries.

    Args:
        directory: Directory searched recursively for ``*.json`` files; a missing directory
            yields an empty list.

    Returns:
        One entry per file, each containing its ``path`` plus either the parsed ``document``
        or a ``read_error`` message if parsing failed.
    """
    result: list[dict[str, Any]] = []
    if not directory.is_dir():
        return result
    for path in sorted(directory.rglob("*.json")):
        try:
            value = load_json(path)
        except Exception as exc:
            result.append({"path": str(path), "read_error": str(exc)})
            continue
        result.append({"path": str(path), "document": value})
    return result


def service_snapshot(project_root: Path) -> dict[str, Any]:
    """Return a read-only, serializable project-control-plane snapshot."""
    root = project_root.resolve()
    manifest = load_json(root / "project.json")
    state_check = check_project_state(root).to_dict() if manifest.get("schema_version") == 3 else None
    target_pack_path = root / "target-pack" / "target.toml"
    pipeline_database = root / "orchestration" / "orchestrator.sqlite3"
    pipelines: list[dict[str, Any]] = []
    if pipeline_database.is_file():
        connection = sqlite3.connect(f"file:{pipeline_database}?mode=ro", uri=True)
        connection.row_factory = sqlite3.Row
        try:
            pipelines = [dict(row) for row in connection.execute("SELECT * FROM pipelines ORDER BY created_at,pipeline_id")]
            for pipeline in pipelines:
                pipeline["jobs"] = [
                    dict(row)
                    for row in connection.execute(
                        "SELECT stage_id,state,attempt,error,started_at,finished_at,result_json FROM jobs WHERE pipeline_id=? ORDER BY stage_index",
                        (pipeline["pipeline_id"],),
                    )
                ]
        finally:
            connection.close()
    return {
        "toolkit_version": __version__,
        "project_root": str(root),
        "manifest": manifest,
        "verification": verify_project(root),
        "state_check": state_check,
        "target_pack_present": target_pack_path.is_file(),
        "pipelines": pipelines,
        "convergence_reports": _json_files(root / "reports" / "convergence"),
        "reproducibility_reports": _json_files(root / "reports" / "reproducibility"),
        "security_reports": _json_files(root / "reports" / "security"),
        "worker_capabilities": discover_worker_capabilities(),
        "read_only": True,
    }


def create_app(project_root: Path) -> Any:
    """Build the read-only FastAPI application exposing project state.

    Args:
        project_root: Project root whose durable records the routes read.

    Returns:
        A configured FastAPI application instance.

    Raises:
        ExternalToolError: If FastAPI is not installed.
    """
    try:
        from fastapi import FastAPI, HTTPException
        from fastapi.responses import HTMLResponse
    except ImportError as exc:
        raise ExternalToolError("FastAPI is required; install x86decomp-toolkit[service]") from exc
    root = project_root.resolve()
    app = FastAPI(title="x86decomp toolkit", version=__version__)

    @app.get("/api/health")
    def health() -> dict[str, Any]:
        """Return a lightweight health summary of toolkit version and validity flags."""
        snapshot = service_snapshot(root)
        return {
            "toolkit_version": snapshot["toolkit_version"],
            "project_valid": bool(snapshot["verification"].get("valid")),
            "state_valid": None if snapshot["state_check"] is None else bool(snapshot["state_check"]["valid"]),
            "read_only": True,
        }

    @app.get("/api/project")
    def project() -> dict[str, Any]:
        """Return the full read-only project snapshot."""
        return service_snapshot(root)

    @app.get("/api/target-pack")
    def target_pack() -> dict[str, Any]:
        """Return the target pack TOML and any recorded observations.

        Raises:
            HTTPException: With status 404 if no target pack is present.
        """
        target = root / "target-pack" / "target.toml"
        observations = root / "target-pack" / "observations.json"
        if not target.is_file():
            raise HTTPException(status_code=404, detail="target pack is not present")
        return {
            "target_toml": target.read_text(encoding="utf-8"),
            "observations": load_json(observations) if observations.is_file() else None,
        }

    @app.get("/api/pipelines")
    def pipelines() -> list[dict[str, Any]]:
        """Return the durable orchestration pipelines recorded for the project."""
        return service_snapshot(root)["pipelines"]

    @app.get("/api/convergence")
    def convergence() -> list[dict[str, Any]]:
        """Return the stored convergence reports."""
        return service_snapshot(root)["convergence_reports"]

    @app.get("/api/reproducibility")
    def reproducibility() -> list[dict[str, Any]]:
        """Return the stored reproducibility reports."""
        return service_snapshot(root)["reproducibility_reports"]

    @app.get("/api/security")
    def security() -> list[dict[str, Any]]:
        """Return the stored security reports."""
        return service_snapshot(root)["security_reports"]

    @app.get("/api/functions")
    def functions() -> list[dict[str, Any]]:
        """Return each function manifest, merging its workflow record when present."""
        result = []
        for directory in sorted((root / "functions").glob("pe-rva_*")):
            manifest = directory / "function.json"
            if manifest.is_file():
                item = load_json(manifest)
                workflow_path = directory / "workflow.json"
                if workflow_path.is_file():
                    item["workflow"] = load_json(workflow_path)
                result.append(item)
        return result

    @app.get("/api/functions/{function_id:path}/workflow")
    def workflow(function_id: str) -> dict[str, Any]:
        """Return the reconstruction workflow for a single function.

        Args:
            function_id: Function identifier from the URL, with ``pe-rva_`` normalized back
                to ``pe-rva:``.

        Raises:
            HTTPException: With status 404 if the workflow cannot be loaded.
        """
        normalized = function_id.replace("pe-rva_", "pe-rva:")
        try:
            return load_function_workflow(root, normalized).to_dict()
        except Exception as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc

    @app.get("/api/work/next")
    def next_task(mode: str | None = None) -> dict[str, Any] | None:
        """Return the next queued work task, or ``None`` when the queue is empty.

        Args:
            mode: Optional queue mode filter forwarded to the work queue.
        """
        queue = WorkQueue(root / "work" / "tasks.sqlite3")
        try:
            return queue.next(mode=mode)
        finally:
            queue.close()

    @app.get("/api/reports")
    def reports() -> list[str]:
        """Return project-relative, forward-slash paths of every JSON report."""
        return [str(path.relative_to(root)).replace("\\", "/") for path in sorted((root / "reports").rglob("*.json"))]

    @app.get("/", response_class=HTMLResponse)
    def index() -> str:
        """Return the read-only browser UI without injecting project data as HTML."""
        return """<!doctype html><html><head><meta charset='utf-8'><title>x86decomp</title>
<meta http-equiv='Content-Security-Policy' content="default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'unsafe-inline'; object-src 'none'; base-uri 'none'">
<style>body{font:15px system-ui;margin:2rem;max-width:1100px}pre{background:#eee;padding:1rem;overflow:auto}.ok{color:green}.bad{color:#b00}</style></head>
<body><h1>x86decomp project</h1><p>This local interface is read-only. Mutations remain evidence-gated through the CLI/MCP transaction journal.</p>
<div id='app'>Loading…</div><script>
fetch('/api/project').then(r=>r.json()).then(p=>{
 const valid=Boolean(p.verification && p.verification.valid);
 const app=document.getElementById('app');
 app.replaceChildren();
 const heading=document.createElement('h2');
 heading.append('Integrity: ');
 const status=document.createElement('span');
 status.className=valid?'ok':'bad';
 status.textContent=String(valid);
 heading.append(status);
 const pipelines=document.createElement('p');
 pipelines.textContent=String((p.pipelines||[]).length)+' durable pipeline(s)';
 const dump=document.createElement('pre');
 dump.textContent=JSON.stringify(p,null,2);
 app.append(heading,pipelines,dump);
});</script></body></html>"""
    return app


def run_service(project_root: Path, *, host: str = "127.0.0.1", port: int = 8765) -> None:
    """Serve the read-only project application with Uvicorn.

    Args:
        project_root: Project root passed to the FastAPI application factory.
        host: Interface address to bind; defaults to loopback.
        port: TCP port to listen on.

    Raises:
        ExternalToolError: If Uvicorn is not installed.
    """
    try:
        import uvicorn
    except ImportError as exc:
        raise ExternalToolError("Uvicorn is required; install x86decomp-toolkit[service]") from exc
    uvicorn.run(create_app(project_root), host=host, port=port)
