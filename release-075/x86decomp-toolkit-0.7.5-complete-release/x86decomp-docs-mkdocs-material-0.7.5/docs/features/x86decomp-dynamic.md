---
title: x86decomp.dynamic
description: Bounded differential execution using Unicorn.
---

# `x86decomp.dynamic`

Bounded differential execution using Unicorn.

This validator is intentionally explicit about its execution envelope. It can
compare leaf routines and routines whose external calls are represented by
user-supplied deterministic stubs. It does not model a complete Windows process.

**Area:** Toolkit  
**Source:** `src/x86decomp/dynamic.py`  
**SHA-256:** `a09cbba16f498158cf30191397884f0a70051c767b778cd520ac229b6e85e451`  
**Functions/methods:** 9

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-unicorn"></a>

### `_unicorn`

No function or method docstring is declared in the 0.7.5 source.

```python
def _unicorn() -> tuple[Any, Any, Any]
```

**Catalog symbol:** `x86decomp.dynamic:_unicorn`  
**Visibility:** internal  
**Source line:** 21

<a id="function-align-down"></a>

### `_align_down`

No function or method docstring is declared in the 0.7.5 source.

```python
def _align_down(value: int) -> int
```

**Catalog symbol:** `x86decomp.dynamic:_align_down`  
**Visibility:** internal  
**Source line:** 32

<a id="function-align-up"></a>

### `_align_up`

No function or method docstring is declared in the 0.7.5 source.

```python
def _align_up(value: int) -> int
```

**Catalog symbol:** `x86decomp.dynamic:_align_up`  
**Visibility:** internal  
**Source line:** 36

<a id="function-load-execution-spec"></a>

### `load_execution_spec`

No function or method docstring is declared in the 0.7.5 source.

```python
def load_execution_spec(path: Path) -> ExecutionSpec
```

**Catalog symbol:** `x86decomp.dynamic:load_execution_spec`  
**Visibility:** public  
**Source line:** 64

<a id="function-register-map"></a>

### `_register_map`

No function or method docstring is declared in the 0.7.5 source.

```python
def _register_map(architecture: str, x86_const: Any) -> dict[str, int]
```

**Catalog symbol:** `x86decomp.dynamic:_register_map`  
**Visibility:** internal  
**Source line:** 151

<a id="function-map-region"></a>

### `_map_region`

No function or method docstring is declared in the 0.7.5 source.

```python
def _map_region(uc: Any, mapped: list[tuple[int, int]], address: int, size: int, permissions: int) -> None
```

**Catalog symbol:** `x86decomp.dynamic:_map_region`  
**Visibility:** internal  
**Source line:** 168

<a id="function-execute-code"></a>

### `execute_code`

No function or method docstring is declared in the 0.7.5 source.

```python
def execute_code(code: bytes, spec: ExecutionSpec, *, code_base: int | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.dynamic:execute_code`  
**Visibility:** public  
**Source line:** 180

<a id="function-differential-validate"></a>

### `differential_validate`

No function or method docstring is declared in the 0.7.5 source.

```python
def differential_validate(target: bytes, candidate: bytes, spec: ExecutionSpec, *, target_base: int | None=None, candidate_base: int | None=None, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.dynamic:differential_validate`  
**Visibility:** public  
**Source line:** 280

<a id="function-differential-validate-files"></a>

### `differential_validate_files`

No function or method docstring is declared in the 0.7.5 source.

```python
def differential_validate_files(target_path: Path, candidate_path: Path, harness_path: Path, *, target_base: int | None=None, candidate_base: int | None=None, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.dynamic:differential_validate_files`  
**Visibility:** public  
**Source line:** 328
