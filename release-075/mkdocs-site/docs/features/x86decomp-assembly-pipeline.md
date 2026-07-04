---
title: x86decomp.assembly.pipeline
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.assembly.pipeline`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/assembly/pipeline.py`  
**SHA-256:** `f6ffb8a8282636b4f07854e6665bbe250b7bb405ceba0587e872d72d91dae04c`  
**Functions/methods:** 8

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-load-json"></a>

### `_load_json`

No function or method docstring is declared in the 0.7.5 source.

```python
def _load_json(path: Path) -> Any
```

**Catalog symbol:** `x86decomp.assembly.pipeline:_load_json`  
**Visibility:** internal  
**Source line:** 25

<a id="function-resolve-path"></a>

### `_resolve_path`

No function or method docstring is declared in the 0.7.5 source.

```python
def _resolve_path(base: Path, raw: str | Path) -> Path
```

**Catalog symbol:** `x86decomp.assembly.pipeline:_resolve_path`  
**Visibility:** internal  
**Source line:** 32

<a id="function-function-bytes"></a>

### `_function_bytes`

No function or method docstring is declared in the 0.7.5 source.

```python
def _function_bytes(item: Mapping[str, Any], *, base: Path) -> bytes
```

**Catalog symbol:** `x86decomp.assembly.pipeline:_function_bytes`  
**Visibility:** internal  
**Source line:** 37

<a id="function-symbol-map"></a>

### `_symbol_map`

No function or method docstring is declared in the 0.7.5 source.

```python
def _symbol_map(functions: list[Mapping[str, Any]], supplemental: Mapping[str, Any] | list[Mapping[str, Any]] | None=None) -> dict[str, dict[str, Any]]
```

**Catalog symbol:** `x86decomp.assembly.pipeline:_symbol_map`  
**Visibility:** internal  
**Source line:** 56

<a id="function-assemblypipeline-init"></a>

### `AssemblyPipeline.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def AssemblyPipeline.__init__(self, store: AssemblyStore)
```

**Catalog symbol:** `x86decomp.assembly.pipeline:AssemblyPipeline.__init__`  
**Visibility:** internal  
**Source line:** 80

<a id="function-assemblypipeline-batch"></a>

### `AssemblyPipeline.batch`

No function or method docstring is declared in the 0.7.5 source.

```python
def AssemblyPipeline.batch(self, manifest_path: Path, output_root: Path, *, asm_format: str='bytes', assembler_command: Sequence[str] | None=None, image_base: int | None=None, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.assembly.pipeline:AssemblyPipeline.batch`  
**Visibility:** public  
**Source line:** 84

<a id="function-assemblypipeline-report"></a>

### `AssemblyPipeline.report`

No function or method docstring is declared in the 0.7.5 source.

```python
def AssemblyPipeline.report(self, run_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.assembly.pipeline:AssemblyPipeline.report`  
**Visibility:** public  
**Source line:** 311

<a id="function-assemblypipeline-list-runs"></a>

### `AssemblyPipeline.list_runs`

No function or method docstring is declared in the 0.7.5 source.

```python
def AssemblyPipeline.list_runs(self) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.assembly.pipeline:AssemblyPipeline.list_runs`  
**Visibility:** public  
**Source line:** 327
