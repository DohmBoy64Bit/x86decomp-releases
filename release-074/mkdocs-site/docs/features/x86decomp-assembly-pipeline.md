---
title: x86decomp.assembly.pipeline
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-assembly-pipeline.html
---

<a id="function-load-json"></a>
<a id="function-resolve-path"></a>
<a id="function-function-bytes"></a>
<a id="function-symbol-map"></a>
<a id="function-assemblypipeline-init"></a>
<a id="function-assemblypipeline-batch"></a>
<a id="function-assemblypipeline-report"></a>
<a id="function-assemblypipeline-list-runs"></a>

Section: Source-derived feature and function reference

# x86decomp.assembly.pipeline

No module docstring is declared in the v0.7.4 source.

Metadata: assembly · current · 8 functions/methods

**Source:** `src/x86decomp/assembly/pipeline.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `f6ffb8a8282636b4f07854e6665bbe250b7bb405ceba0587e872d72d91dae04c`.

## Functions and methods

Metadata: internal · line 25

### _load_json

No function or method docstring is declared in the v0.7.4 source.

```
def _load_json(path: Path) -> Any
```

**Catalog symbol:** `x86decomp.assembly.pipeline:_load_json`

Metadata: internal · line 32

### _resolve_path

No function or method docstring is declared in the v0.7.4 source.

```
def _resolve_path(base: Path, raw: str | Path) -> Path
```

**Catalog symbol:** `x86decomp.assembly.pipeline:_resolve_path`

Metadata: internal · line 37

### _function_bytes

No function or method docstring is declared in the v0.7.4 source.

```
def _function_bytes(item: Mapping[str, Any], *, base: Path) -> bytes
```

**Catalog symbol:** `x86decomp.assembly.pipeline:_function_bytes`

Metadata: internal · line 56

### _symbol_map

No function or method docstring is declared in the v0.7.4 source.

```
def _symbol_map(functions: list[Mapping[str, Any]], supplemental: Mapping[str, Any] | list[Mapping[str, Any]] | None = None) -> dict[str, dict[str, Any]]
```

**Catalog symbol:** `x86decomp.assembly.pipeline:_symbol_map`

Metadata: internal · line 80

### AssemblyPipeline.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: AssemblyStore)
```

**Catalog symbol:** `x86decomp.assembly.pipeline:AssemblyPipeline.__init__`

Metadata: public · line 84

### AssemblyPipeline.batch

No function or method docstring is declared in the v0.7.4 source.

```
def batch(self, manifest_path: Path, output_root: Path, *, asm_format: str = 'bytes', assembler_command: Sequence[str] | None = None, image_base: int | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.assembly.pipeline:AssemblyPipeline.batch`

Metadata: public · line 311

### AssemblyPipeline.report

No function or method docstring is declared in the v0.7.4 source.

```
def report(self, run_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.assembly.pipeline:AssemblyPipeline.report`

Metadata: public · line 327

### AssemblyPipeline.list_runs

No function or method docstring is declared in the v0.7.4 source.

```
def list_runs(self) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.assembly.pipeline:AssemblyPipeline.list_runs`
