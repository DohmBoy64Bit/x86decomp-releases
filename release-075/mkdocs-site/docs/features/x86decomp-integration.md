---
title: x86decomp.integration
description: Manifest-driven integration scenario runner.
---

# `x86decomp.integration`

Manifest-driven integration scenario runner.

This module performs real target/candidate process executions with explicit host
execution consent or an external isolation wrapper. It compares only declared
observations and never treats finite scenarios as universal equivalence proof.

**Area:** Toolkit  
**Source:** `src/x86decomp/integration.py`  
**SHA-256:** `cb8157c8210544e2ed4730e8bdb01f0a77dc9d05f683d43154cba1bf93c1e845`  
**Functions/methods:** 10

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-require-string-list"></a>

### `_require_string_list`

No function or method docstring is declared in the 0.7.5 source.

```python
def _require_string_list(value: Any, name: str, *, nonempty: bool=False) -> list[str]
```

**Catalog symbol:** `x86decomp.integration:_require_string_list`  
**Visibility:** internal  
**Source line:** 24

<a id="function-resolve-existing"></a>

### `_resolve_existing`

No function or method docstring is declared in the 0.7.5 source.

```python
def _resolve_existing(base: Path, value: Any, name: str) -> Path
```

**Catalog symbol:** `x86decomp.integration:_resolve_existing`  
**Visibility:** internal  
**Source line:** 32

<a id="function-parse-stdin"></a>

### `_parse_stdin`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_stdin(base: Path, value: Any) -> bytes
```

**Catalog symbol:** `x86decomp.integration:_parse_stdin`  
**Visibility:** internal  
**Source line:** 41

<a id="function-copy-fixtures"></a>

### `_copy_fixtures`

No function or method docstring is declared in the 0.7.5 source.

```python
def _copy_fixtures(base: Path, workdir: Path, fixtures: Any) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.integration:_copy_fixtures`  
**Visibility:** internal  
**Source line:** 63

<a id="function-substitute-command"></a>

### `_substitute_command`

No function or method docstring is declared in the 0.7.5 source.

```python
def _substitute_command(command: list[str], *, artifact: Path, workdir: Path) -> list[str]
```

**Catalog symbol:** `x86decomp.integration:_substitute_command`  
**Visibility:** internal  
**Source line:** 94

<a id="function-bounded-output"></a>

### `_bounded_output`

No function or method docstring is declared in the 0.7.5 source.

```python
def _bounded_output(data: bytes, limit: int) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.integration:_bounded_output`  
**Visibility:** internal  
**Source line:** 108

<a id="function-run-side"></a>

### `_run_side`

No function or method docstring is declared in the 0.7.5 source.

```python
def _run_side(*, base: Path, scenario_id: str, side_name: str, spec: Any, wrapper_prefix: list[str], timeout_seconds: int, stdin_data: bytes, fixtures: Any, output_limit: int) -> tuple[dict[str, Any], Path]
```

**Catalog symbol:** `x86decomp.integration:_run_side`  
**Visibility:** internal  
**Source line:** 119

<a id="function-observe-file"></a>

### `_observe_file`

No function or method docstring is declared in the 0.7.5 source.

```python
def _observe_file(workdir: Path, item: Any, *, side: str, index: int, output_limit: int) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.integration:_observe_file`  
**Visibility:** internal  
**Source line:** 197

<a id="function-compare-stream"></a>

### `_compare_stream`

No function or method docstring is declared in the 0.7.5 source.

```python
def _compare_stream(name: str, mode: Any, target: bytes, candidate: bytes) -> dict[str, Any] | None
```

**Catalog symbol:** `x86decomp.integration:_compare_stream`  
**Visibility:** internal  
**Source line:** 251

<a id="function-run-integration-scenarios"></a>

### `run_integration_scenarios`

Execute and compare all declared integration scenarios.

Host execution is rejected unless both the manifest selects ``host_explicit`` and
the caller supplies ``allow_host_execution=True``. ``external_wrapper`` requires a
non-empty wrapper command but the toolkit cannot independently prove the wrapper is
a complete sandbox; this limitation is recorded in the report.

```python
def run_integration_scenarios(manifest_path: Path, *, allow_host_execution: bool=False, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.integration:run_integration_scenarios`  
**Visibility:** public  
**Source line:** 273
