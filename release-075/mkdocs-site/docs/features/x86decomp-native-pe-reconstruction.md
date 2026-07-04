---
title: x86decomp.native.pe_reconstruction
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.native.pe_reconstruction`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/native/pe_reconstruction.py`  
**SHA-256:** `32c4ba5082d59f88439efe2af68c26f8820aaa82d6f551d506a0d7c63b517558`  
**Functions/methods:** 10

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-section-header-records"></a>

### `_section_header_records`

No function or method docstring is declared in the 0.7.5 source.

```python
def _section_header_records(data: bytes) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:_section_header_records`  
**Visibility:** internal  
**Source line:** 18

<a id="function-plan-patch"></a>

### `plan_patch`

No function or method docstring is declared in the 0.7.5 source.

```python
def plan_patch(original: bytes, operations: Iterable[dict[str, Any]]) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:plan_patch`  
**Visibility:** public  
**Source line:** 37

<a id="function-apply-operations"></a>

### `apply_operations`

No function or method docstring is declared in the 0.7.5 source.

```python
def apply_operations(original: bytes, operations: Iterable[dict[str, Any]]) -> bytes
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:apply_operations`  
**Visibility:** public  
**Source line:** 54

<a id="function-pereconstruction-init"></a>

### `PEReconstruction.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEReconstruction.__init__(self, store: NativeStore)
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:PEReconstruction.__init__`  
**Visibility:** internal  
**Source line:** 65

<a id="function-pereconstruction-inventory"></a>

### `PEReconstruction.inventory`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEReconstruction.inventory(self, image_path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:PEReconstruction.inventory`  
**Visibility:** public  
**Source line:** 67

<a id="function-pereconstruction-export-sections"></a>

### `PEReconstruction.export_sections`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEReconstruction.export_sections(self, image_path: Path, output_root: Path, *, names: Iterable[str] | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:PEReconstruction.export_sections`  
**Visibility:** public  
**Source line:** 71

<a id="function-pereconstruction-export-coff"></a>

### `PEReconstruction.export_coff`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEReconstruction.export_coff(self, image_path: Path, output_root: Path, *, names: Iterable[str] | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:PEReconstruction.export_coff`  
**Visibility:** public  
**Source line:** 85

<a id="function-pereconstruction-create-plan"></a>

### `PEReconstruction.create_plan`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEReconstruction.create_plan(self, original_path: Path, output_path: Path, operations: Iterable[dict[str, Any]], *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:PEReconstruction.create_plan`  
**Visibility:** public  
**Source line:** 98

<a id="function-pereconstruction-apply-plan"></a>

### `PEReconstruction.apply_plan`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEReconstruction.apply_plan(self, plan_id: str, *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:PEReconstruction.apply_plan`  
**Visibility:** public  
**Source line:** 105

<a id="function-pereconstruction-text-swap"></a>

### `PEReconstruction.text_swap`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEReconstruction.text_swap(self, original_path: Path, replacement_path: Path, output_path: Path, *, section_name: str='.text', actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:PEReconstruction.text_swap`  
**Visibility:** public  
**Source line:** 116
