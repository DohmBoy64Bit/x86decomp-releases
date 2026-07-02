---
title: x86decomp.worker
description: Bounded command workers with explicit isolation and provenance.
original_path: features/x86decomp-worker.html
---

<a id="function-workerlimits-validate"></a>
<a id="function-workerresult-to-dict"></a>
<a id="function-discover-worker-capabilities"></a>
<a id="function-bounded-environment"></a>
<a id="function-preexec"></a>
<a id="function-confined-paths"></a>
<a id="function-container-command"></a>
<a id="function-execute-worker-request"></a>

Section: Source-derived feature and function reference

# x86decomp.worker

Bounded command workers with explicit isolation and provenance.

Metadata: core · current · 8 functions/methods

**Source:** `src/x86decomp/worker.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `811287668595febda7c8a186d83e1683ad7c58fcc44259efe7271bf5d7b8249c`.

## Functions and methods

Metadata: public · line 34

### WorkerLimits.validate

No function or method docstring is declared in the v0.7.4 source.

```
def validate(self) -> None
```

**Catalog symbol:** `x86decomp.worker:WorkerLimits.validate`

Metadata: public · line 69

### WorkerResult.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.worker:WorkerResult.to_dict`

Metadata: public · line 89

### discover_worker_capabilities

No function or method docstring is declared in the v0.7.4 source.

```
def discover_worker_capabilities() -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.worker:discover_worker_capabilities`

Metadata: internal · line 103

### _bounded_environment

No function or method docstring is declared in the v0.7.4 source.

```
def _bounded_environment(extra: dict[str, str], working_directory: Path) -> dict[str, str]
```

**Catalog symbol:** `x86decomp.worker:_bounded_environment`

Metadata: internal · line 138

### _preexec

Return the legacy resource-limit callback for API compatibility.

```
def _preexec(limits: WorkerLimits) -> Any
```

**Catalog symbol:** `x86decomp.worker:_preexec`

Metadata: internal · line 164

### _confined_paths

No function or method docstring is declared in the v0.7.4 source.

```
def _confined_paths(root: Path, values: tuple[Path, ...], *, must_exist: bool) -> tuple[Path, ...]
```

**Catalog symbol:** `x86decomp.worker:_confined_paths`

Metadata: internal · line 180

### _container_command

No function or method docstring is declared in the v0.7.4 source.

```
def _container_command(request: WorkerRequest, runtime: str) -> tuple[str, ...]
```

**Catalog symbol:** `x86decomp.worker:_container_command`

Metadata: public · line 205

### execute_worker_request

No function or method docstring is declared in the v0.7.4 source.

```
def execute_worker_request(request: WorkerRequest, *, log_directory: Path, report_path: Path | None = None, cancel_check: Callable[[], bool] | None = None) -> WorkerResult
```

**Catalog symbol:** `x86decomp.worker:execute_worker_request`
