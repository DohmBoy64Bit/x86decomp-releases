---
title: x86decomp.toolchains
description: User-owned compiler toolchain registry; proprietary binaries are never
  copied.
---

# `x86decomp.toolchains`

User-owned compiler toolchain registry; proprietary binaries are never copied.

**Area:** Toolkit  
**Source:** `src/x86decomp/toolchains.py`  
**SHA-256:** `9dde5962b67d30fec64266313f5488a4e5501de9db26605d4719cbe276cde03f`  
**Functions/methods:** 2

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-register-toolchain"></a>

### `register_toolchain`

No function or method docstring is declared in the 0.7.5 source.

```python
def register_toolchain(registry_path: Path, *, toolchain_id: str, family: str, version: str, executables: dict[str, Path], metadata: dict[str, Any] | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.toolchains:register_toolchain`  
**Visibility:** public  
**Source line:** 12

<a id="function-verify-toolchain"></a>

### `verify_toolchain`

No function or method docstring is declared in the 0.7.5 source.

```python
def verify_toolchain(registry_path: Path, toolchain_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.toolchains:verify_toolchain`  
**Visibility:** public  
**Source line:** 46
