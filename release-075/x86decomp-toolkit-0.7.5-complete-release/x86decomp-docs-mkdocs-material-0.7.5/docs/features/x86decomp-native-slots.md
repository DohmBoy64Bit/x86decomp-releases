---
title: x86decomp.native.slots
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.native.slots`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/native/slots.py`  
**SHA-256:** `e0f7164fa040306cab458e4dfe811590375a3a49023de7a33736e07b44032d2c`  
**Functions/methods:** 8

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-int"></a>

### `_int`

No function or method docstring is declared in the 0.7.5 source.

```python
def _int(value: Any, name: str) -> int
```

**Catalog symbol:** `x86decomp.native.slots:_int`  
**Visibility:** internal  
**Source line:** 12

<a id="function-inventory-from-project"></a>

### `inventory_from_project`

No function or method docstring is declared in the 0.7.5 source.

```python
def inventory_from_project(project_root: Path) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.native.slots:inventory_from_project`  
**Visibility:** public  
**Source line:** 23

<a id="function-functionslots-init"></a>

### `FunctionSlots.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def FunctionSlots.__init__(self, store: NativeStore)
```

**Catalog symbol:** `x86decomp.native.slots:FunctionSlots.__init__`  
**Visibility:** internal  
**Source line:** 47

<a id="function-functionslots-audit"></a>

### `FunctionSlots.audit`

No function or method docstring is declared in the 0.7.5 source.

```python
def FunctionSlots.audit(self, functions: Iterable[dict[str, Any]], *, text_end_rva: int | None=None, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.slots:FunctionSlots.audit`  
**Visibility:** public  
**Source line:** 51

<a id="function-functionslots-audit-project"></a>

### `FunctionSlots.audit_project`

No function or method docstring is declared in the 0.7.5 source.

```python
def FunctionSlots.audit_project(self, project_root: Path, binary: Path, *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.slots:FunctionSlots.audit_project`  
**Visibility:** public  
**Source line:** 123

<a id="function-functionslots-list"></a>

### `FunctionSlots.list`

No function or method docstring is declared in the 0.7.5 source.

```python
def FunctionSlots.list(self, *, classification: str | None=None) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.native.slots:FunctionSlots.list`  
**Visibility:** public  
**Source line:** 134

<a id="function-functionslots-show"></a>

### `FunctionSlots.show`

No function or method docstring is declared in the 0.7.5 source.

```python
def FunctionSlots.show(self, function_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.slots:FunctionSlots.show`  
**Visibility:** public  
**Source line:** 143

<a id="function-functionslots-export-fixes"></a>

### `FunctionSlots.export_fixes`

No function or method docstring is declared in the 0.7.5 source.

```python
def FunctionSlots.export_fixes(self, output: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.slots:FunctionSlots.export_fixes`  
**Visibility:** public  
**Source line:** 153
