---
title: x86decomp.reconstruction.libraries
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-reconstruction-libraries.html
---

<a id="function-libraryrecognition-init"></a>
<a id="function-libraryrecognition-identify"></a>
<a id="function-libraryrecognition-get"></a>
<a id="function-libraryrecognition-candidates"></a>
<a id="function-libraryrecognition-disposition"></a>

Section: Source-derived feature and function reference

# x86decomp.reconstruction.libraries

No module docstring is declared in the v0.7.4 source.

Metadata: reconstruction · current · 5 functions/methods

**Source:** `src/x86decomp/reconstruction/libraries.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `4892d5e00011085e4befce6cff5a24c9d065c6647933acd4dcb4618a3f514152`.

## Functions and methods

Metadata: internal · line 8

### LibraryRecognition.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: ReconstructionStore)
```

**Catalog symbol:** `x86decomp.reconstruction.libraries:LibraryRecognition.__init__`

Metadata: public · line 9

### LibraryRecognition.identify

No function or method docstring is declared in the v0.7.4 source.

```
def identify(self, subject_id: str, library_name: str, *, version_range: str | None = None, confidence: float, evidence: list[dict[str, Any]], actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.libraries:LibraryRecognition.identify`

Metadata: public · line 16

### LibraryRecognition.get

No function or method docstring is declared in the v0.7.4 source.

```
def get(self, match_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.libraries:LibraryRecognition.get`

Metadata: public · line 20

### LibraryRecognition.candidates

No function or method docstring is declared in the v0.7.4 source.

```
def candidates(self, subject_id: str) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.reconstruction.libraries:LibraryRecognition.candidates`

Metadata: public · line 23

### LibraryRecognition.disposition

No function or method docstring is declared in the v0.7.4 source.

```
def disposition(self, match_id: str, disposition: str, *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.libraries:LibraryRecognition.disposition`
