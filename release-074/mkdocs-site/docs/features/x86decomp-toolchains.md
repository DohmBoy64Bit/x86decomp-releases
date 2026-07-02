---
title: x86decomp.toolchains
description: User-owned compiler toolchain registry; proprietary binaries are never
  copied.
original_path: features/x86decomp-toolchains.html
---

<a id="function-register-toolchain"></a>
<a id="function-verify-toolchain"></a>

Section: Source-derived feature and function reference

# x86decomp.toolchains

User-owned compiler toolchain registry; proprietary binaries are never copied.

Metadata: core · current · 2 functions/methods

**Source:** `src/x86decomp/toolchains.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `9dde5962b67d30fec64266313f5488a4e5501de9db26605d4719cbe276cde03f`.

## Functions and methods

Metadata: public · line 12

### register_toolchain

No function or method docstring is declared in the v0.7.4 source.

```
def register_toolchain(registry_path: Path, *, toolchain_id: str, family: str, version: str, executables: dict[str, Path], metadata: dict[str, Any] | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.toolchains:register_toolchain`

Metadata: public · line 46

### verify_toolchain

No function or method docstring is declared in the v0.7.4 source.

```
def verify_toolchain(registry_path: Path, toolchain_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.toolchains:verify_toolchain`
