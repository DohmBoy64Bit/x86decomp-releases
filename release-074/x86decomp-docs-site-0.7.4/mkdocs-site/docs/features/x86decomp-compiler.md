---
title: x86decomp.compiler
description: Deterministic external compiler profile execution and cache keys.
original_path: features/x86decomp-compiler.html
---

<a id="function-load-profile"></a>
<a id="function-tool-version"></a>
<a id="function-resolve-executable"></a>
<a id="function-compiler-cache-key"></a>
<a id="function-run-compiler-profile"></a>

Section: Source-derived feature and function reference

# x86decomp.compiler

Deterministic external compiler profile execution and cache keys.

Metadata: core · current · 5 functions/methods

**Source:** `src/x86decomp/compiler.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `f21f38f6ed0804a959188e31f5c9fa498d7d0740536fbb82594a375b12353944`.

## Functions and methods

Metadata: public · line 19

### load_profile

No function or method docstring is declared in the v0.7.4 source.

```
def load_profile(path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.compiler:load_profile`

Metadata: internal · line 58

### _tool_version

No function or method docstring is declared in the v0.7.4 source.

```
def _tool_version(executable: str, version_arguments: list[str] | None = None) -> str | None
```

**Catalog symbol:** `x86decomp.compiler:_tool_version`

Metadata: internal · line 73

### _resolve_executable

No function or method docstring is declared in the v0.7.4 source.

```
def _resolve_executable(value: str) -> str
```

**Catalog symbol:** `x86decomp.compiler:_resolve_executable`

Metadata: public · line 85

### compiler_cache_key

No function or method docstring is declared in the v0.7.4 source.

```
def compiler_cache_key(profile: dict[str, Any], *, executable_sha256: str, source_sha256: str, extra_arguments: list[str]) -> str
```

**Catalog symbol:** `x86decomp.compiler:compiler_cache_key`

Metadata: public · line 101

### run_compiler_profile

No function or method docstring is declared in the v0.7.4 source.

```
def run_compiler_profile(profile_path: Path, source: Path, output: Path, *, report_path: Path | None = None, extra_arguments: list[str] | None = None, working_directory: Path | None = None, cache_directory: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.compiler:run_compiler_profile`
