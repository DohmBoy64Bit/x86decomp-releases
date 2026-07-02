---
title: x86decomp.tools
description: External-tool discovery and version capture.
original_path: features/x86decomp-tools.html
---

<a id="function-capture"></a>
<a id="function-discover-analyze-headless"></a>
<a id="function-snapshot-tools"></a>

Section: Source-derived feature and function reference

# x86decomp.tools

External-tool discovery and version capture.

Metadata: core · current · 3 functions/methods

**Source:** `src/x86decomp/tools.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `8e068c2ef41fb99fd53f45b28808fd2bf3366978bffc6ba22e46207497f08f34`.

## Functions and methods

Metadata: internal · line 22

### _capture

No function or method docstring is declared in the v0.7.4 source.

```
def _capture(path: str, args: list[str]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.tools:_capture`

Metadata: public · line 39

### discover_analyze_headless

No function or method docstring is declared in the v0.7.4 source.

```
def discover_analyze_headless(explicit_ghidra_home: Path | None = None) -> Path | None
```

**Catalog symbol:** `x86decomp.tools:discover_analyze_headless`

Metadata: public · line 59

### snapshot_tools

No function or method docstring is declared in the v0.7.4 source.

```
def snapshot_tools(output: Path | None = None, ghidra_home: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.tools:snapshot_tools`
