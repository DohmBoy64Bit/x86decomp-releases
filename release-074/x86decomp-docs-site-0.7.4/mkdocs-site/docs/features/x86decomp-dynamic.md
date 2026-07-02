---
title: x86decomp.dynamic
description: Bounded differential execution using Unicorn.
original_path: features/x86decomp-dynamic.html
---

<a id="function-unicorn"></a>
<a id="function-align-down"></a>
<a id="function-align-up"></a>
<a id="function-load-execution-spec"></a>
<a id="function-register-map"></a>
<a id="function-map-region"></a>
<a id="function-execute-code"></a>
<a id="function-differential-validate"></a>
<a id="function-differential-validate-files"></a>

Section: Source-derived feature and function reference

# x86decomp.dynamic

Bounded differential execution using Unicorn.

Metadata: core · current · 9 functions/methods

**Source:** `src/x86decomp/dynamic.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `a09cbba16f498158cf30191397884f0a70051c767b778cd520ac229b6e85e451`.

## Functions and methods

Metadata: internal · line 21

### _unicorn

No function or method docstring is declared in the v0.7.4 source.

```
def _unicorn() -> tuple[Any, Any, Any]
```

**Catalog symbol:** `x86decomp.dynamic:_unicorn`

Metadata: internal · line 32

### _align_down

No function or method docstring is declared in the v0.7.4 source.

```
def _align_down(value: int) -> int
```

**Catalog symbol:** `x86decomp.dynamic:_align_down`

Metadata: internal · line 36

### _align_up

No function or method docstring is declared in the v0.7.4 source.

```
def _align_up(value: int) -> int
```

**Catalog symbol:** `x86decomp.dynamic:_align_up`

Metadata: public · line 64

### load_execution_spec

No function or method docstring is declared in the v0.7.4 source.

```
def load_execution_spec(path: Path) -> ExecutionSpec
```

**Catalog symbol:** `x86decomp.dynamic:load_execution_spec`

Metadata: internal · line 151

### _register_map

No function or method docstring is declared in the v0.7.4 source.

```
def _register_map(architecture: str, x86_const: Any) -> dict[str, int]
```

**Catalog symbol:** `x86decomp.dynamic:_register_map`

Metadata: internal · line 168

### _map_region

No function or method docstring is declared in the v0.7.4 source.

```
def _map_region(uc: Any, mapped: list[tuple[int, int]], address: int, size: int, permissions: int) -> None
```

**Catalog symbol:** `x86decomp.dynamic:_map_region`

Metadata: public · line 180

### execute_code

No function or method docstring is declared in the v0.7.4 source.

```
def execute_code(code: bytes, spec: ExecutionSpec, *, code_base: int | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.dynamic:execute_code`

Metadata: public · line 280

### differential_validate

No function or method docstring is declared in the v0.7.4 source.

```
def differential_validate(target: bytes, candidate: bytes, spec: ExecutionSpec, *, target_base: int | None = None, candidate_base: int | None = None, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.dynamic:differential_validate`

Metadata: public · line 328

### differential_validate_files

No function or method docstring is declared in the v0.7.4 source.

```
def differential_validate_files(target_path: Path, candidate_path: Path, harness_path: Path, *, target_base: int | None = None, candidate_base: int | None = None, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.dynamic:differential_validate_files`
