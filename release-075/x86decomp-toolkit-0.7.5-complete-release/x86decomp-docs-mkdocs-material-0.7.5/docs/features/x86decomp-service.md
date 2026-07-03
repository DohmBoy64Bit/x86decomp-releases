---
title: x86decomp.service
description: Optional read-only FastAPI service for project, pipeline, and validation
  state.
---

# `x86decomp.service`

Optional read-only FastAPI service for project, pipeline, and validation state.

The service never mutates project state.  It exposes durable records produced by
CLI workers and validators so an analyst can inspect a project without granting
the web process write authority.

**Area:** Toolkit  
**Source:** `src/x86decomp/service.py`  
**SHA-256:** `ef74988c5b19f8d2925ea07fb75a6cb3bea4304348bc9419e82f9ffddbd19584`  
**Functions/methods:** 4

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-json-files"></a>

### `_json_files`

No function or method docstring is declared in the 0.7.5 source.

```python
def _json_files(directory: Path) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.service:_json_files`  
**Visibility:** internal  
**Source line:** 24

<a id="function-service-snapshot"></a>

### `service_snapshot`

Return a read-only, serializable project-control-plane snapshot.

```python
def service_snapshot(project_root: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.service:service_snapshot`  
**Visibility:** public  
**Source line:** 38

<a id="function-create-app"></a>

### `create_app`

No function or method docstring is declared in the 0.7.5 source.

```python
def create_app(project_root: Path) -> Any
```

**Catalog symbol:** `x86decomp.service:create_app`  
**Visibility:** public  
**Source line:** 77

<a id="function-run-service"></a>

### `run_service`

No function or method docstring is declared in the 0.7.5 source.

```python
def run_service(project_root: Path, *, host: str='127.0.0.1', port: int=8765) -> None
```

**Catalog symbol:** `x86decomp.service:run_service`  
**Visibility:** public  
**Source line:** 173
