---
title: x86decomp.governance.family
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.governance.family`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/governance/family.py`  
**SHA-256:** `be9c27b2174ab2e046fae2d9937d7df2b73353d738f794db9f923bc11c9ede7c`  
**Functions/methods:** 9

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-binaryfamilystore-init"></a>

### `BinaryFamilyStore.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def BinaryFamilyStore.__init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.family:BinaryFamilyStore.__init__`  
**Visibility:** internal  
**Source line:** 14

<a id="function-binaryfamilystore-create"></a>

### `BinaryFamilyStore.create`

No function or method docstring is declared in the 0.7.5 source.

```python
def BinaryFamilyStore.create(self, name: str, *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.family:BinaryFamilyStore.create`  
**Visibility:** public  
**Source line:** 19

<a id="function-binaryfamilystore-add"></a>

### `BinaryFamilyStore.add`

No function or method docstring is declared in the 0.7.5 source.

```python
def BinaryFamilyStore.add(self, family_id: str, label: str, path: str | Path, *, metadata: dict[str, Any] | None=None, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.family:BinaryFamilyStore.add`  
**Visibility:** public  
**Source line:** 28

<a id="function-binaryfamilystore-block-fingerprints"></a>

### `BinaryFamilyStore._block_fingerprints`

No function or method docstring is declared in the 0.7.5 source.

```python
def BinaryFamilyStore._block_fingerprints(data: bytes, block_size: int) -> set[bytes]
```

**Catalog symbol:** `x86decomp.governance.family:BinaryFamilyStore._block_fingerprints`  
**Visibility:** internal  
**Source line:** 50

<a id="function-binaryfamilystore-correlate"></a>

### `BinaryFamilyStore.correlate`

No function or method docstring is declared in the 0.7.5 source.

```python
def BinaryFamilyStore.correlate(self, left_member_id: str, right_member_id: str, *, block_size: int=64, actor: str='system') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.family:BinaryFamilyStore.correlate`  
**Visibility:** public  
**Source line:** 55

<a id="function-binaryfamilystore-get"></a>

### `BinaryFamilyStore.get`

No function or method docstring is declared in the 0.7.5 source.

```python
def BinaryFamilyStore.get(self, family_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.family:BinaryFamilyStore.get`  
**Visibility:** public  
**Source line:** 77

<a id="function-binaryfamilystore-member"></a>

### `BinaryFamilyStore.member`

No function or method docstring is declared in the 0.7.5 source.

```python
def BinaryFamilyStore.member(self, member_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.family:BinaryFamilyStore.member`  
**Visibility:** public  
**Source line:** 84

<a id="function-binaryfamilystore-correlation"></a>

### `BinaryFamilyStore.correlation`

No function or method docstring is declared in the 0.7.5 source.

```python
def BinaryFamilyStore.correlation(self, correlation_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.family:BinaryFamilyStore.correlation`  
**Visibility:** public  
**Source line:** 93

<a id="function-binaryfamilystore-report"></a>

### `BinaryFamilyStore.report`

No function or method docstring is declared in the 0.7.5 source.

```python
def BinaryFamilyStore.report(self, family_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.family:BinaryFamilyStore.report`  
**Visibility:** public  
**Source line:** 102
