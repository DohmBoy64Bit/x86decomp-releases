---
title: x86decomp.reconstruction.libraries
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.reconstruction.libraries`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/reconstruction/libraries.py`  
**SHA-256:** `4892d5e00011085e4befce6cff5a24c9d065c6647933acd4dcb4618a3f514152`  
**Functions/methods:** 5

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-libraryrecognition-init"></a>

### `LibraryRecognition.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def LibraryRecognition.__init__(self, store: ReconstructionStore)
```

**Catalog symbol:** `x86decomp.reconstruction.libraries:LibraryRecognition.__init__`  
**Visibility:** internal  
**Source line:** 8

<a id="function-libraryrecognition-identify"></a>

### `LibraryRecognition.identify`

No function or method docstring is declared in the 0.7.5 source.

```python
def LibraryRecognition.identify(self, subject_id: str, library_name: str, *, version_range: str | None=None, confidence: float, evidence: list[dict[str, Any]], actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.libraries:LibraryRecognition.identify`  
**Visibility:** public  
**Source line:** 9

<a id="function-libraryrecognition-get"></a>

### `LibraryRecognition.get`

No function or method docstring is declared in the 0.7.5 source.

```python
def LibraryRecognition.get(self, match_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.libraries:LibraryRecognition.get`  
**Visibility:** public  
**Source line:** 16

<a id="function-libraryrecognition-candidates"></a>

### `LibraryRecognition.candidates`

No function or method docstring is declared in the 0.7.5 source.

```python
def LibraryRecognition.candidates(self, subject_id: str) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.reconstruction.libraries:LibraryRecognition.candidates`  
**Visibility:** public  
**Source line:** 20

<a id="function-libraryrecognition-disposition"></a>

### `LibraryRecognition.disposition`

No function or method docstring is declared in the 0.7.5 source.

```python
def LibraryRecognition.disposition(self, match_id: str, disposition: str, *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.libraries:LibraryRecognition.disposition`  
**Visibility:** public  
**Source line:** 23
