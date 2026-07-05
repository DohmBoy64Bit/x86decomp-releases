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
    """Implement json files.
    
    Parameters and return values follow the signature and runtime validation in the body.
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
    """Create app.
    
    Parameters and return values follow the signature and runtime validation in the body.
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
        """Implement health.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        snapshot = service_snapshot(root)
        return {
            "toolkit_version": snapshot["toolkit_version"],
            "project_valid": bool(snapshot["verification"].get("valid")),
            "state_valid": None if snapshot["state_check"] is None else bool(snapshot["state_check"]["valid"]),
            "read_only": True,
        }

    @app.get("/api/project")
    def project() -> dict[str, Any]:
        """Implement project.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        return service_snapshot(root)

    @app.get("/api/target-pack")
    def target_pack() -> dict[str, Any]:
        """Implement target pack.
        
        Parameters and return values follow the signature and runtime validation in the body.
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
        """Implement pipelines.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        return service_snapshot(root)["pipelines"]

    @app.get("/api/convergence")
    def convergence() -> list[dict[str, Any]]:
        """Implement convergence.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        return service_snapshot(root)["convergence_reports"]

    @app.get("/api/reproducibility")
    def reproducibility() -> list[dict[str, Any]]:
        """Implement reproducibility.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        return service_snapshot(root)["reproducibility_reports"]

    @app.get("/api/security")
    def security() -> list[dict[str, Any]]:
        """Implement security.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        return service_snapshot(root)["security_reports"]

    @app.get("/api/functions")
    def functions() -> list[dict[str, Any]]:
        """Implement functions.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
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
        """Implement workflow.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        normalized = function_id.replace("pe-rva_", "pe-rva:")
        try:
            return load_function_workflow(root, normalized).to_dict()
        except Exception as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc

    @app.get("/api/work/next")
    def next_task(mode: str | None = None) -> dict[str, Any] | None:
        """Implement next task.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        queue = WorkQueue(root / "work" / "tasks.sqlite3")
        try:
            return queue.next(mode=mode)
        finally:
            queue.close()

    @app.get("/api/reports")
    def reports() -> list[str]:
        """Implement reports.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        return [str(path.relative_to(root)).replace("\\", "/") for path in sorted((root / "reports").rglob("*.json"))]

    @app.get("/", response_class=HTMLResponse)
    def index() -> str:
        """Implement index.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        return """<!doctype html><html><head><meta charset='utf-8'><title>x86decomp</title>
<style>body{font:15px system-ui;margin:2rem;max-width:1100px}pre{background:#eee;padding:1rem;overflow:auto}.ok{color:green}.bad{color:#b00}</style></head>
<body><h1>x86decomp project</h1><p>This local interface is read-only. Mutations remain evidence-gated through the CLI/MCP transaction journal.</p>
<div id='app'>Loading…</div><script>
fetch('/api/project').then(r=>r.json()).then(p=>{
 const valid=p.verification.valid;
 document.getElementById('app').innerHTML=`<h2>Integrity: <span class='${valid?'ok':'bad'}'>${valid}</span></h2><p>${p.pipelines.length} durable pipeline(s)</p><pre>${JSON.stringify(p,null,2)}</pre>`;
});</script></body></html>"""
    return app


def run_service(project_root: Path, *, host: str = "127.0.0.1", port: int = 8765) -> None:
    """Run service.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    try:
        import uvicorn
    except ImportError as exc:
        raise ExternalToolError("Uvicorn is required; install x86decomp-toolkit[service]") from exc
    uvicorn.run(create_app(project_root), host=host, port=port)
