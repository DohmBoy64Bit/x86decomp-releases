---
title: x86decomp.angr_backend
description: Optional angr comparative symbolic execution backend for bounded code
  blobs.
---

# `x86decomp.angr_backend`

Optional angr comparative symbolic execution backend for bounded code blobs.

The built-in symbolic engine remains the default deterministic backend. This
module integrates angr when installed and performs finite path comparison over
explicit input/output registers and stack arguments. Results are scoped to the
selected architecture, code blobs, path/step limits, and observable registers.

**Area:** Toolkit  
**Source:** `src/x86decomp/angr_backend.py`  
**SHA-256:** `b3f95fbeec7f4d726ba52f50df9d4d7986cfad9ed5c789ab0a3932c0dea8b7a3`  
**Functions/methods:** 11

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-load-angr"></a>

### `_load_angr`

No function or method docstring is declared in the 0.7.5 source.

```python
def _load_angr() -> tuple[Any, Any]
```

**Catalog symbol:** `x86decomp.angr_backend:_load_angr`  
**Visibility:** internal  
**Source line:** 18

<a id="function-arch-name"></a>

### `_arch_name`

No function or method docstring is declared in the 0.7.5 source.

```python
def _arch_name(architecture: str) -> str
```

**Catalog symbol:** `x86decomp.angr_backend:_arch_name`  
**Visibility:** internal  
**Source line:** 27

<a id="function-summaries"></a>

### `_summaries`

No function or method docstring is declared in the 0.7.5 source.

```python
def _summaries(code: bytes, *, architecture: str, input_registers: tuple[str, ...], stack_argument_words: int, output_registers: tuple[str, ...], max_steps: int, max_paths: int) -> tuple[list[dict[str, Any]], dict[str, Any]]
```

**Catalog symbol:** `x86decomp.angr_backend:_summaries`  
**Visibility:** internal  
**Source line:** 35

<a id="function-counterexample"></a>

### `_counterexample`

No function or method docstring is declared in the 0.7.5 source.

```python
def _counterexample(left: list[dict[str, Any]], right: list[dict[str, Any]], output_registers: tuple[str, ...]) -> dict[str, int] | None
```

**Catalog symbol:** `x86decomp.angr_backend:_counterexample`  
**Visibility:** internal  
**Source line:** 110

<a id="function-angr-bounded-compare"></a>

### `angr_bounded_compare`

No function or method docstring is declared in the 0.7.5 source.

```python
def angr_bounded_compare(target: bytes, candidate: bytes, *, architecture: str='x86', input_registers: tuple[str, ...]=(), stack_argument_words: int=0, output_registers: tuple[str, ...] | None=None, max_steps: int=1000, max_paths: int=64, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.angr_backend:angr_bounded_compare`  
**Visibility:** public  
**Source line:** 128

<a id="function-angr-bounded-compare-files"></a>

### `angr_bounded_compare_files`

No function or method docstring is declared in the 0.7.5 source.

```python
def angr_bounded_compare_files(target: Path, candidate: Path, **kwargs: Any) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.angr_backend:angr_bounded_compare_files`  
**Visibility:** public  
**Source line:** 173

<a id="function-load-memory-harness"></a>

### `_load_memory_harness`

No function or method docstring is declared in the 0.7.5 source.

```python
def _load_memory_harness(path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.angr_backend:_load_memory_harness`  
**Visibility:** internal  
**Source line:** 181

<a id="function-memory-summaries"></a>

### `_memory_summaries`

No function or method docstring is declared in the 0.7.5 source.

```python
def _memory_summaries(code: bytes, *, harness: dict[str, Any], side: str) -> tuple[list[dict[str, Any]], dict[str, Any]]
```

**Catalog symbol:** `x86decomp.angr_backend:_memory_summaries`  
**Visibility:** internal  
**Source line:** 208

<a id="function-memory-counterexample"></a>

### `_memory_counterexample`

No function or method docstring is declared in the 0.7.5 source.

```python
def _memory_counterexample(left: list[dict[str, Any]], right: list[dict[str, Any]]) -> dict[str, int] | None
```

**Catalog symbol:** `x86decomp.angr_backend:_memory_counterexample`  
**Visibility:** internal  
**Source line:** 375

<a id="function-angr-memory-alias-compare"></a>

### `angr_memory_alias_compare`

No function or method docstring is declared in the 0.7.5 source.

```python
def angr_memory_alias_compare(target: bytes, candidate: bytes, harness: dict[str, Any], *, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.angr_backend:angr_memory_alias_compare`  
**Visibility:** public  
**Source line:** 404

<a id="function-angr-memory-alias-compare-files"></a>

### `angr_memory_alias_compare_files`

No function or method docstring is declared in the 0.7.5 source.

```python
def angr_memory_alias_compare_files(target_path: Path, candidate_path: Path, harness_path: Path, *, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.angr_backend:angr_memory_alias_compare_files`  
**Visibility:** public  
**Source line:** 442
