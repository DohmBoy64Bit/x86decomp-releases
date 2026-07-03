---
title: x86decomp.ghidra
description: Safe command construction for Ghidra headless analysis.
---

# `x86decomp.ghidra`

Safe command construction for Ghidra headless analysis.

**Area:** Toolkit  
**Source:** `src/x86decomp/ghidra.py`  
**SHA-256:** `98657d48a9d3ebb79eaf951aa8676ffd7ca696c2ba2f07fe8a5c4f0ad622c2b3`  
**Functions/methods:** 2

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-build-export-command"></a>

### `build_export_command`

No function or method docstring is declared in the 0.7.5 source.

```python
def build_export_command(*, binary: Path, ghidra_project_dir: Path, ghidra_project_name: str, scripts_dir: Path, output_dir: Path, ghidra_home: Path | None=None, overwrite: bool=False, function_selector: str='all') -> list[str]
```

**Catalog symbol:** `x86decomp.ghidra:build_export_command`  
**Visibility:** public  
**Source line:** 14

<a id="function-run-export"></a>

### `run_export`

No function or method docstring is declared in the 0.7.5 source.

```python
def run_export(command: list[str], *, timeout_seconds: int, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.ghidra:run_export`  
**Visibility:** public  
**Source line:** 64
