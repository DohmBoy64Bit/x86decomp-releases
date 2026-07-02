---
title: x86decomp.reconstruction.provenance
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-reconstruction-provenance.html
---

<a id="function-provenanceledger-init"></a>
<a id="function-provenanceledger-record"></a>
<a id="function-provenanceledger-get"></a>
<a id="function-provenanceledger-source"></a>
<a id="function-provenanceledger-binary"></a>
<a id="function-provenanceledger-lock"></a>
<a id="function-provenanceledger-unlock"></a>
<a id="function-provenanceledger-reconcile"></a>
<a id="function-provenanceledger-impact"></a>
<a id="function-provenanceledger-export"></a>

Section: Source-derived feature and function reference

# x86decomp.reconstruction.provenance

No module docstring is declared in the v0.7.4 source.

Metadata: reconstruction · current · 10 functions/methods

**Source:** `src/x86decomp/reconstruction/provenance.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `03790dbcf2863491fa3c28e4cb96013dc73be03b87a038fcc367a6f27933f9e3`.

## Functions and methods

Metadata: internal · line 11

### ProvenanceLedger.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: ReconstructionStore)
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.__init__`

Metadata: public · line 12

### ProvenanceLedger.record

No function or method docstring is declared in the v0.7.4 source.

```
def record(self, source_path: str, line_start: int, line_end: int, binary_id: str, address_start: str, address_end: str, *, evidence: list[dict[str, Any]], confidence: float, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.record`

Metadata: public · line 22

### ProvenanceLedger.get

No function or method docstring is declared in the v0.7.4 source.

```
def get(self, provenance_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.get`

Metadata: public · line 26

### ProvenanceLedger.source

No function or method docstring is declared in the v0.7.4 source.

```
def source(self, path: str, line: int | None = None) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.source`

Metadata: public · line 32

### ProvenanceLedger.binary

No function or method docstring is declared in the v0.7.4 source.

```
def binary(self, binary_id: str, address: str | None = None) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.binary`

Metadata: public · line 37

### ProvenanceLedger.lock

No function or method docstring is declared in the v0.7.4 source.

```
def lock(self, path: str, *, reason: str, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.lock`

Metadata: public · line 43

### ProvenanceLedger.unlock

No function or method docstring is declared in the v0.7.4 source.

```
def unlock(self, path: str, *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.unlock`

Metadata: public · line 48

### ProvenanceLedger.reconcile

No function or method docstring is declared in the v0.7.4 source.

```
def reconcile(self, path: str, *, before_sha256: str | None = None, semantic: bool | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.reconcile`

Metadata: public · line 63

### ProvenanceLedger.impact

No function or method docstring is declared in the v0.7.4 source.

```
def impact(self, path: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.impact`

Metadata: public · line 66

### ProvenanceLedger.export

No function or method docstring is declared in the v0.7.4 source.

```
def export(self, path: str | Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.provenance:ProvenanceLedger.export`
