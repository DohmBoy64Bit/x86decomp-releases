---
title: x86decomp.service
description: Optional read-only FastAPI service for project, pipeline, and validation
  state.
original_path: features/x86decomp-service.html
---

<a id="function-json-files"></a>
<a id="function-service-snapshot"></a>
<a id="function-create-app"></a>
<a id="function-run-service"></a>

Section: Source-derived feature and function reference

# x86decomp.service

Optional read-only FastAPI service for project, pipeline, and validation state.

Metadata: core · current · 4 functions/methods

**Source:** `src/x86decomp/service.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `ef74988c5b19f8d2925ea07fb75a6cb3bea4304348bc9419e82f9ffddbd19584`.

## Functions and methods

Metadata: internal · line 24

### _json_files

No function or method docstring is declared in the v0.7.4 source.

```
def _json_files(directory: Path) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.service:_json_files`

Metadata: public · line 38

### service_snapshot

Return a read-only, serializable project-control-plane snapshot.

```
def service_snapshot(project_root: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.service:service_snapshot`

Metadata: public · line 77

### create_app

No function or method docstring is declared in the v0.7.4 source.

```
def create_app(project_root: Path) -> Any
```

**Catalog symbol:** `x86decomp.service:create_app`

Metadata: public · line 173

### run_service

No function or method docstring is declared in the v0.7.4 source.

```
def run_service(project_root: Path, *, host: str = '127.0.0.1', port: int = 8765) -> None
```

**Catalog symbol:** `x86decomp.service:run_service`
