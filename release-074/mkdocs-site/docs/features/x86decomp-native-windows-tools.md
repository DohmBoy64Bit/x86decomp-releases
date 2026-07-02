---
title: x86decomp.native.windows_tools
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-native-windows-tools.html
---

<a id="function-discover-ghidra-launcher"></a>
<a id="function-write-response-file"></a>
<a id="function-windowstools-init"></a>
<a id="function-windowstools-doctor"></a>

Section: Source-derived feature and function reference

# x86decomp.native.windows_tools

No module docstring is declared in the v0.7.4 source.

Metadata: native · current · 4 functions/methods

**Source:** `src/x86decomp/native/windows_tools.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `0de581d6f2316540f99e7daf3d64fbd925e1998f786b3099488d766ed71bb2c0`.

## Functions and methods

Metadata: public · line 13

### discover_ghidra_launcher

No function or method docstring is declared in the v0.7.4 source.

```
def discover_ghidra_launcher(ghidra_home: Path | None = None, *, platform_name: str | None = None) -> Path | None
```

**Catalog symbol:** `x86decomp.native.windows_tools:discover_ghidra_launcher`

Metadata: public · line 28

### write_response_file

No function or method docstring is declared in the v0.7.4 source.

```
def write_response_file(path: Path, arguments: list[str]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.windows_tools:write_response_file`

Metadata: internal · line 38

### WindowsTools.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: NativeStore)
```

**Catalog symbol:** `x86decomp.native.windows_tools:WindowsTools.__init__`

Metadata: public · line 40

### WindowsTools.doctor

No function or method docstring is declared in the v0.7.4 source.

```
def doctor(self, *, ghidra_home: Path | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.windows_tools:WindowsTools.doctor`
