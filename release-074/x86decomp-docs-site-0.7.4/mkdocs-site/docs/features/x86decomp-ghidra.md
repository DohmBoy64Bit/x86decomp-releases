---
title: x86decomp.ghidra
description: Safe command construction for Ghidra headless analysis.
original_path: features/x86decomp-ghidra.html
---

<a id="function-build-export-command"></a>
<a id="function-run-export"></a>

Section: Source-derived feature and function reference

# x86decomp.ghidra

Safe command construction for Ghidra headless analysis.

Metadata: core · current · 2 functions/methods

**Source:** `src/x86decomp/ghidra.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `98657d48a9d3ebb79eaf951aa8676ffd7ca696c2ba2f07fe8a5c4f0ad622c2b3`.

## Functions and methods

Metadata: public · line 14

### build_export_command

No function or method docstring is declared in the v0.7.4 source.

```
def build_export_command(*, binary: Path, ghidra_project_dir: Path, ghidra_project_name: str, scripts_dir: Path, output_dir: Path, ghidra_home: Path | None = None, overwrite: bool = False, function_selector: str = 'all') -> list[str]
```

**Catalog symbol:** `x86decomp.ghidra:build_export_command`

Metadata: public · line 64

### run_export

No function or method docstring is declared in the v0.7.4 source.

```
def run_export(command: list[str], *, timeout_seconds: int, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.ghidra:run_export`
