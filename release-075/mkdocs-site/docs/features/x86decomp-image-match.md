---
title: x86decomp.image_match
description: Target-specific whole-image matching and deterministic normalization.
---

# `x86decomp.image_match`

Target-specific whole-image matching and deterministic normalization.

A layout profile records which PE fields are expected to match exactly and which
build-produced fields may be normalized.  The matcher never promotes a
normalized match to an exact byte-identical match.

**Area:** Toolkit  
**Source:** `src/x86decomp/image_match.py`  
**SHA-256:** `a9c72f376532369da77440496a1ea07564da5071ef8e6108e29c58e33e96fcf4`  
**Functions/methods:** 9

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-byterange-to-dict"></a>

### `ByteRange.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def ByteRange.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.image_match:ByteRange.to_dict`  
**Visibility:** public  
**Source line:** 26

<a id="function-pe-offsets"></a>

### `_pe_offsets`

No function or method docstring is declared in the 0.7.5 source.

```python
def _pe_offsets(data: bytes) -> dict[str, int]
```

**Catalog symbol:** `x86decomp.image_match:_pe_offsets`  
**Visibility:** internal  
**Source line:** 30

<a id="function-derive-layout-profile"></a>

### `derive_layout_profile`

No function or method docstring is declared in the 0.7.5 source.

```python
def derive_layout_profile(reference: Path, *, output: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.image_match:derive_layout_profile`  
**Visibility:** public  
**Source line:** 52

<a id="function-mask-ranges"></a>

### `_mask_ranges`

No function or method docstring is declared in the 0.7.5 source.

```python
def _mask_ranges(data: bytes, ranges: Iterable[ByteRange]) -> bytes
```

**Catalog symbol:** `x86decomp.image_match:_mask_ranges`  
**Visibility:** internal  
**Source line:** 91

<a id="function-rva-to-file-offset"></a>

### `_rva_to_file_offset`

No function or method docstring is declared in the 0.7.5 source.

```python
def _rva_to_file_offset(image: Any, rva: int, file_size: int) -> int | None
```

**Catalog symbol:** `x86decomp.image_match:_rva_to_file_offset`  
**Visibility:** internal  
**Source line:** 100

<a id="function-profile-ranges"></a>

### `_profile_ranges`

No function or method docstring is declared in the 0.7.5 source.

```python
def _profile_ranges(data: bytes, profile: dict[str, Any], image: Any) -> list[ByteRange]
```

**Catalog symbol:** `x86decomp.image_match:_profile_ranges`  
**Visibility:** internal  
**Source line:** 110

<a id="function-apply-rebase"></a>

### `_apply_rebase`

No function or method docstring is declared in the 0.7.5 source.

```python
def _apply_rebase(data: bytes, *, target_base: int, candidate_base: int, image: Any) -> bytes
```

**Catalog symbol:** `x86decomp.image_match:_apply_rebase`  
**Visibility:** internal  
**Source line:** 145

<a id="function-mismatches"></a>

### `_mismatches`

No function or method docstring is declared in the 0.7.5 source.

```python
def _mismatches(left: bytes, right: bytes, limit: int=256) -> tuple[int, list[dict[str, int]]]
```

**Catalog symbol:** `x86decomp.image_match:_mismatches`  
**Visibility:** internal  
**Source line:** 173

<a id="function-compare-whole-images"></a>

### `compare_whole_images`

No function or method docstring is declared in the 0.7.5 source.

```python
def compare_whole_images(reference: Path, candidate: Path, *, profile_path: Path | None=None, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.image_match:compare_whole_images`  
**Visibility:** public  
**Source line:** 186
