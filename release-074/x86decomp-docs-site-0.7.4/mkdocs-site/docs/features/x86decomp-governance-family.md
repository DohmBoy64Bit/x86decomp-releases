---
title: x86decomp.governance.family
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-governance-family.html
---

<a id="function-binaryfamilystore-init"></a>
<a id="function-binaryfamilystore-create"></a>
<a id="function-binaryfamilystore-add"></a>
<a id="function-binaryfamilystore-block-fingerprints"></a>
<a id="function-binaryfamilystore-correlate"></a>
<a id="function-binaryfamilystore-get"></a>
<a id="function-binaryfamilystore-member"></a>
<a id="function-binaryfamilystore-correlation"></a>
<a id="function-binaryfamilystore-report"></a>

Section: Source-derived feature and function reference

# x86decomp.governance.family

No module docstring is declared in the v0.7.4 source.

Metadata: governance · current · 9 functions/methods

**Source:** `src/x86decomp/governance/family.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `be9c27b2174ab2e046fae2d9937d7df2b73353d738f794db9f923bc11c9ede7c`.

## Functions and methods

Metadata: internal · line 14

### BinaryFamilyStore.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.family:BinaryFamilyStore.__init__`

Metadata: public · line 19

### BinaryFamilyStore.create

No function or method docstring is declared in the v0.7.4 source.

```
def create(self, name: str, *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.family:BinaryFamilyStore.create`

Metadata: public · line 28

### BinaryFamilyStore.add

No function or method docstring is declared in the v0.7.4 source.

```
def add(self, family_id: str, label: str, path: str | Path, *, metadata: dict[str, Any] | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.family:BinaryFamilyStore.add`

Metadata: internal · line 50

### BinaryFamilyStore._block_fingerprints

No function or method docstring is declared in the v0.7.4 source.

```
def _block_fingerprints(data: bytes, block_size: int) -> set[bytes]
```

**Catalog symbol:** `x86decomp.governance.family:BinaryFamilyStore._block_fingerprints`

Metadata: public · line 55

### BinaryFamilyStore.correlate

No function or method docstring is declared in the v0.7.4 source.

```
def correlate(self, left_member_id: str, right_member_id: str, *, block_size: int = 64, actor: str = 'system') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.family:BinaryFamilyStore.correlate`

Metadata: public · line 77

### BinaryFamilyStore.get

No function or method docstring is declared in the v0.7.4 source.

```
def get(self, family_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.family:BinaryFamilyStore.get`

Metadata: public · line 84

### BinaryFamilyStore.member

No function or method docstring is declared in the v0.7.4 source.

```
def member(self, member_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.family:BinaryFamilyStore.member`

Metadata: public · line 93

### BinaryFamilyStore.correlation

No function or method docstring is declared in the v0.7.4 source.

```
def correlation(self, correlation_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.family:BinaryFamilyStore.correlation`

Metadata: public · line 102

### BinaryFamilyStore.report

No function or method docstring is declared in the v0.7.4 source.

```
def report(self, family_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.family:BinaryFamilyStore.report`
