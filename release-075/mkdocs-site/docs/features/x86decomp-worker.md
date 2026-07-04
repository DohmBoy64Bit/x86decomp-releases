---
title: x86decomp.worker
description: Bounded command workers with explicit isolation and provenance.
---

# `x86decomp.worker`

Bounded command workers with explicit isolation and provenance.

The local worker provides resource and output bounds without pretending to be a
security boundary.  Container mode invokes Docker or Podman with a read-only
root, no network, dropped capabilities, and explicit mounts.

**Area:** Toolkit  
**Source:** `src/x86decomp/worker.py`  
**SHA-256:** `811287668595febda7c8a186d83e1683ad7c58fcc44259efe7271bf5d7b8249c`  
**Functions/methods:** 8

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-workerlimits-validate"></a>

### `WorkerLimits.validate`

No function or method docstring is declared in the 0.7.5 source.

```python
def WorkerLimits.validate(self) -> None
```

**Catalog symbol:** `x86decomp.worker:WorkerLimits.validate`  
**Visibility:** public  
**Source line:** 34

<a id="function-workerresult-to-dict"></a>

### `WorkerResult.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def WorkerResult.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.worker:WorkerResult.to_dict`  
**Visibility:** public  
**Source line:** 69

<a id="function-discover-worker-capabilities"></a>

### `discover_worker_capabilities`

No function or method docstring is declared in the 0.7.5 source.

```python
def discover_worker_capabilities() -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.worker:discover_worker_capabilities`  
**Visibility:** public  
**Source line:** 89

<a id="function-bounded-environment"></a>

### `_bounded_environment`

No function or method docstring is declared in the 0.7.5 source.

```python
def _bounded_environment(extra: dict[str, str], working_directory: Path) -> dict[str, str]
```

**Catalog symbol:** `x86decomp.worker:_bounded_environment`  
**Visibility:** internal  
**Source line:** 103

<a id="function-preexec"></a>

### `_preexec`

Return the legacy resource-limit callback for API compatibility.

The production launcher no longer passes this callback to ``Popen`` because
Python code executed between fork and exec can deadlock in a process that
has already initialized threads.  the exec-based resource wrapper applies the
same limits in a fresh Python interpreter immediately before ``exec``.

```python
def _preexec(limits: WorkerLimits) -> Any
```

**Catalog symbol:** `x86decomp.worker:_preexec`  
**Visibility:** internal  
**Source line:** 138

<a id="function-confined-paths"></a>

### `_confined_paths`

No function or method docstring is declared in the 0.7.5 source.

```python
def _confined_paths(root: Path, values: tuple[Path, ...], *, must_exist: bool) -> tuple[Path, ...]
```

**Catalog symbol:** `x86decomp.worker:_confined_paths`  
**Visibility:** internal  
**Source line:** 164

<a id="function-container-command"></a>

### `_container_command`

No function or method docstring is declared in the 0.7.5 source.

```python
def _container_command(request: WorkerRequest, runtime: str) -> tuple[str, ...]
```

**Catalog symbol:** `x86decomp.worker:_container_command`  
**Visibility:** internal  
**Source line:** 180

<a id="function-execute-worker-request"></a>

### `execute_worker_request`

No function or method docstring is declared in the 0.7.5 source.

```python
def execute_worker_request(request: WorkerRequest, *, log_directory: Path, report_path: Path | None=None, cancel_check: Callable[[], bool] | None=None) -> WorkerResult
```

**Catalog symbol:** `x86decomp.worker:execute_worker_request`  
**Visibility:** public  
**Source line:** 205
