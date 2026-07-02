---
title: x86decomp.native.slots
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-native-slots.html
---

<a id="function-int"></a>
<a id="function-inventory-from-project"></a>
<a id="function-functionslots-init"></a>
<a id="function-functionslots-audit"></a>
<a id="function-functionslots-audit-project"></a>
<a id="function-functionslots-list"></a>
<a id="function-functionslots-show"></a>
<a id="function-functionslots-export-fixes"></a>

Section: Source-derived feature and function reference

# x86decomp.native.slots

No module docstring is declared in the v0.7.4 source.

Metadata: native · current · 8 functions/methods

**Source:** `src/x86decomp/native/slots.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `e0f7164fa040306cab458e4dfe811590375a3a49023de7a33736e07b44032d2c`.

## Functions and methods

Metadata: internal · line 12

### _int

No function or method docstring is declared in the v0.7.4 source.

```
def _int(value: Any, name: str) -> int
```

**Catalog symbol:** `x86decomp.native.slots:_int`

Metadata: public · line 23

### inventory_from_project

No function or method docstring is declared in the v0.7.4 source.

```
def inventory_from_project(project_root: Path) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.native.slots:inventory_from_project`

Metadata: internal · line 47

### FunctionSlots.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: NativeStore)
```

**Catalog symbol:** `x86decomp.native.slots:FunctionSlots.__init__`

Metadata: public · line 51

### FunctionSlots.audit

No function or method docstring is declared in the v0.7.4 source.

```
def audit(self, functions: Iterable[dict[str, Any]], *, text_end_rva: int | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.slots:FunctionSlots.audit`

Metadata: public · line 123

### FunctionSlots.audit_project

No function or method docstring is declared in the v0.7.4 source.

```
def audit_project(self, project_root: Path, binary: Path, *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.slots:FunctionSlots.audit_project`

Metadata: public · line 134

### FunctionSlots.list

No function or method docstring is declared in the v0.7.4 source.

```
def list(self, *, classification: str | None = None) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.native.slots:FunctionSlots.list`

Metadata: public · line 143

### FunctionSlots.show

No function or method docstring is declared in the v0.7.4 source.

```
def show(self, function_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.slots:FunctionSlots.show`

Metadata: public · line 153

### FunctionSlots.export_fixes

No function or method docstring is declared in the v0.7.4 source.

```
def export_fixes(self, output: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.slots:FunctionSlots.export_fixes`
