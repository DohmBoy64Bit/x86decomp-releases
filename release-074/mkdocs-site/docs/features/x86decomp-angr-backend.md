---
title: x86decomp.angr_backend
description: Optional angr comparative symbolic execution backend for bounded code
  blobs.
original_path: features/x86decomp-angr-backend.html
---

<a id="function-load-angr"></a>
<a id="function-arch-name"></a>
<a id="function-summaries"></a>
<a id="function-counterexample"></a>
<a id="function-angr-bounded-compare"></a>
<a id="function-angr-bounded-compare-files"></a>
<a id="function-load-memory-harness"></a>
<a id="function-memory-summaries"></a>
<a id="function-memory-counterexample"></a>
<a id="function-angr-memory-alias-compare"></a>
<a id="function-angr-memory-alias-compare-files"></a>

Section: Source-derived feature and function reference

# x86decomp.angr_backend

Optional angr comparative symbolic execution backend for bounded code blobs.

Metadata: core · current · 11 functions/methods

**Source:** `src/x86decomp/angr_backend.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `b3f95fbeec7f4d726ba52f50df9d4d7986cfad9ed5c789ab0a3932c0dea8b7a3`.

## Functions and methods

Metadata: internal · line 18

### _load_angr

No function or method docstring is declared in the v0.7.4 source.

```
def _load_angr() -> tuple[Any, Any]
```

**Catalog symbol:** `x86decomp.angr_backend:_load_angr`

Metadata: internal · line 27

### _arch_name

No function or method docstring is declared in the v0.7.4 source.

```
def _arch_name(architecture: str) -> str
```

**Catalog symbol:** `x86decomp.angr_backend:_arch_name`

Metadata: internal · line 35

### _summaries

No function or method docstring is declared in the v0.7.4 source.

```
def _summaries(code: bytes, *, architecture: str, input_registers: tuple[str, ...], stack_argument_words: int, output_registers: tuple[str, ...], max_steps: int, max_paths: int) -> tuple[list[dict[str, Any]], dict[str, Any]]
```

**Catalog symbol:** `x86decomp.angr_backend:_summaries`

Metadata: internal · line 110

### _counterexample

No function or method docstring is declared in the v0.7.4 source.

```
def _counterexample(left: list[dict[str, Any]], right: list[dict[str, Any]], output_registers: tuple[str, ...]) -> dict[str, int] | None
```

**Catalog symbol:** `x86decomp.angr_backend:_counterexample`

Metadata: public · line 128

### angr_bounded_compare

No function or method docstring is declared in the v0.7.4 source.

```
def angr_bounded_compare(target: bytes, candidate: bytes, *, architecture: str = 'x86', input_registers: tuple[str, ...] = (), stack_argument_words: int = 0, output_registers: tuple[str, ...] | None = None, max_steps: int = 1000, max_paths: int = 64, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.angr_backend:angr_bounded_compare`

Metadata: public · line 173

### angr_bounded_compare_files

No function or method docstring is declared in the v0.7.4 source.

```
def angr_bounded_compare_files(target: Path, candidate: Path, **kwargs: Any) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.angr_backend:angr_bounded_compare_files`

Metadata: internal · line 181

### _load_memory_harness

No function or method docstring is declared in the v0.7.4 source.

```
def _load_memory_harness(path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.angr_backend:_load_memory_harness`

Metadata: internal · line 208

### _memory_summaries

No function or method docstring is declared in the v0.7.4 source.

```
def _memory_summaries(code: bytes, *, harness: dict[str, Any], side: str) -> tuple[list[dict[str, Any]], dict[str, Any]]
```

**Catalog symbol:** `x86decomp.angr_backend:_memory_summaries`

Metadata: internal · line 375

### _memory_counterexample

No function or method docstring is declared in the v0.7.4 source.

```
def _memory_counterexample(left: list[dict[str, Any]], right: list[dict[str, Any]]) -> dict[str, int] | None
```

**Catalog symbol:** `x86decomp.angr_backend:_memory_counterexample`

Metadata: public · line 404

### angr_memory_alias_compare

No function or method docstring is declared in the v0.7.4 source.

```
def angr_memory_alias_compare(target: bytes, candidate: bytes, harness: dict[str, Any], *, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.angr_backend:angr_memory_alias_compare`

Metadata: public · line 442

### angr_memory_alias_compare_files

No function or method docstring is declared in the v0.7.4 source.

```
def angr_memory_alias_compare_files(target_path: Path, candidate_path: Path, harness_path: Path, *, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.angr_backend:angr_memory_alias_compare_files`
