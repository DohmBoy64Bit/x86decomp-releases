---
title: x86decomp.native.pe_reconstruction
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-native-pe-reconstruction.html
---

<a id="function-section-header-records"></a>
<a id="function-plan-patch"></a>
<a id="function-apply-operations"></a>
<a id="function-pereconstruction-init"></a>
<a id="function-pereconstruction-inventory"></a>
<a id="function-pereconstruction-export-sections"></a>
<a id="function-pereconstruction-export-coff"></a>
<a id="function-pereconstruction-create-plan"></a>
<a id="function-pereconstruction-apply-plan"></a>
<a id="function-pereconstruction-text-swap"></a>

Section: Source-derived feature and function reference

# x86decomp.native.pe_reconstruction

No module docstring is declared in the v0.7.4 source.

Metadata: native · current · 10 functions/methods

**Source:** `src/x86decomp/native/pe_reconstruction.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `32c4ba5082d59f88439efe2af68c26f8820aaa82d6f551d506a0d7c63b517558`.

## Functions and methods

Metadata: internal · line 18

### _section_header_records

No function or method docstring is declared in the v0.7.4 source.

```
def _section_header_records(data: bytes) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:_section_header_records`

Metadata: public · line 37

### plan_patch

No function or method docstring is declared in the v0.7.4 source.

```
def plan_patch(original: bytes, operations: Iterable[dict[str, Any]]) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:plan_patch`

Metadata: public · line 54

### apply_operations

No function or method docstring is declared in the v0.7.4 source.

```
def apply_operations(original: bytes, operations: Iterable[dict[str, Any]]) -> bytes
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:apply_operations`

Metadata: internal · line 65

### PEReconstruction.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: NativeStore)
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:PEReconstruction.__init__`

Metadata: public · line 67

### PEReconstruction.inventory

No function or method docstring is declared in the v0.7.4 source.

```
def inventory(self, image_path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:PEReconstruction.inventory`

Metadata: public · line 71

### PEReconstruction.export_sections

No function or method docstring is declared in the v0.7.4 source.

```
def export_sections(self, image_path: Path, output_root: Path, *, names: Iterable[str] | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:PEReconstruction.export_sections`

Metadata: public · line 85

### PEReconstruction.export_coff

No function or method docstring is declared in the v0.7.4 source.

```
def export_coff(self, image_path: Path, output_root: Path, *, names: Iterable[str] | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:PEReconstruction.export_coff`

Metadata: public · line 98

### PEReconstruction.create_plan

No function or method docstring is declared in the v0.7.4 source.

```
def create_plan(self, original_path: Path, output_path: Path, operations: Iterable[dict[str, Any]], *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:PEReconstruction.create_plan`

Metadata: public · line 105

### PEReconstruction.apply_plan

No function or method docstring is declared in the v0.7.4 source.

```
def apply_plan(self, plan_id: str, *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:PEReconstruction.apply_plan`

Metadata: public · line 116

### PEReconstruction.text_swap

No function or method docstring is declared in the v0.7.4 source.

```
def text_swap(self, original_path: Path, replacement_path: Path, output_path: Path, *, section_name: str = '.text', actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.pe_reconstruction:PEReconstruction.text_swap`
