---
title: x86decomp.compiler
description: Deterministic external compiler profile execution and cache keys.
---

# `x86decomp.compiler`

Deterministic external compiler profile execution and cache keys.

**Area:** Toolkit  
**Source:** `src/x86decomp/compiler.py`  
**SHA-256:** `f21f38f6ed0804a959188e31f5c9fa498d7d0740536fbb82594a375b12353944`  
**Functions/methods:** 5

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-load-profile"></a>

### `load_profile`

No function or method docstring is declared in the 0.7.5 source.

```python
def load_profile(path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.compiler:load_profile`  
**Visibility:** public  
**Source line:** 19

<a id="function-tool-version"></a>

### `_tool_version`

No function or method docstring is declared in the 0.7.5 source.

```python
def _tool_version(executable: str, version_arguments: list[str] | None=None) -> str | None
```

**Catalog symbol:** `x86decomp.compiler:_tool_version`  
**Visibility:** internal  
**Source line:** 58

<a id="function-resolve-executable"></a>

### `_resolve_executable`

No function or method docstring is declared in the 0.7.5 source.

```python
def _resolve_executable(value: str) -> str
```

**Catalog symbol:** `x86decomp.compiler:_resolve_executable`  
**Visibility:** internal  
**Source line:** 73

<a id="function-compiler-cache-key"></a>

### `compiler_cache_key`

No function or method docstring is declared in the 0.7.5 source.

```python
def compiler_cache_key(profile: dict[str, Any], *, executable_sha256: str, source_sha256: str, extra_arguments: list[str]) -> str
```

**Catalog symbol:** `x86decomp.compiler:compiler_cache_key`  
**Visibility:** public  
**Source line:** 85

<a id="function-run-compiler-profile"></a>

### `run_compiler_profile`

No function or method docstring is declared in the 0.7.5 source.

```python
def run_compiler_profile(profile_path: Path, source: Path, output: Path, *, report_path: Path | None=None, extra_arguments: list[str] | None=None, working_directory: Path | None=None, cache_directory: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.compiler:run_compiler_profile`  
**Visibility:** public  
**Source line:** 101
