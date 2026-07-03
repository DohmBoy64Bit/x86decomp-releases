---
title: x86decomp.reconstruction.provenance
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.reconstruction.provenance`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/reconstruction/provenance.py`  
**SHA-256:** `03790dbcf2863491fa3c28e4cb96013dc73be03b87a038fcc367a6f27933f9e3`  
**Functions/methods:** 10

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-provenanceledger-init"></a>

### `ProvenanceLedger.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProvenanceLedger.__init__(self, store: ReconstructionStore)
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.__init__`  
**Visibility:** internal  
**Source line:** 11

<a id="function-provenanceledger-record"></a>

### `ProvenanceLedger.record`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProvenanceLedger.record(self, source_path: str, line_start: int, line_end: int, binary_id: str, address_start: str, address_end: str, *, evidence: list[dict[str, Any]], confidence: float, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.record`  
**Visibility:** public  
**Source line:** 12

<a id="function-provenanceledger-get"></a>

### `ProvenanceLedger.get`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProvenanceLedger.get(self, provenance_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.get`  
**Visibility:** public  
**Source line:** 22

<a id="function-provenanceledger-source"></a>

### `ProvenanceLedger.source`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProvenanceLedger.source(self, path: str, line: int | None=None) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.source`  
**Visibility:** public  
**Source line:** 26

<a id="function-provenanceledger-binary"></a>

### `ProvenanceLedger.binary`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProvenanceLedger.binary(self, binary_id: str, address: str | None=None) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.binary`  
**Visibility:** public  
**Source line:** 32

<a id="function-provenanceledger-lock"></a>

### `ProvenanceLedger.lock`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProvenanceLedger.lock(self, path: str, *, reason: str, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.lock`  
**Visibility:** public  
**Source line:** 37

<a id="function-provenanceledger-unlock"></a>

### `ProvenanceLedger.unlock`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProvenanceLedger.unlock(self, path: str, *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.unlock`  
**Visibility:** public  
**Source line:** 43

<a id="function-provenanceledger-reconcile"></a>

### `ProvenanceLedger.reconcile`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProvenanceLedger.reconcile(self, path: str, *, before_sha256: str | None=None, semantic: bool | None=None, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.reconcile`  
**Visibility:** public  
**Source line:** 48

<a id="function-provenanceledger-impact"></a>

### `ProvenanceLedger.impact`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProvenanceLedger.impact(self, path: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.impact`  
**Visibility:** public  
**Source line:** 63

<a id="function-provenanceledger-export"></a>

### `ProvenanceLedger.export`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProvenanceLedger.export(self, path: str | Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.export`  
**Visibility:** public  
**Source line:** 66
