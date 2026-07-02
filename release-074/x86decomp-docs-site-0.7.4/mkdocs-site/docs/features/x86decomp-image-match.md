---
title: x86decomp.image_match
description: Target-specific whole-image matching and deterministic normalization.
original_path: features/x86decomp-image-match.html
---

<a id="function-byterange-to-dict"></a>
<a id="function-pe-offsets"></a>
<a id="function-derive-layout-profile"></a>
<a id="function-mask-ranges"></a>
<a id="function-rva-to-file-offset"></a>
<a id="function-profile-ranges"></a>
<a id="function-apply-rebase"></a>
<a id="function-mismatches"></a>
<a id="function-compare-whole-images"></a>

Section: Source-derived feature and function reference

# x86decomp.image_match

Target-specific whole-image matching and deterministic normalization.

Metadata: core · current · 9 functions/methods

**Source:** `src/x86decomp/image_match.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `a9c72f376532369da77440496a1ea07564da5071ef8e6108e29c58e33e96fcf4`.

## Functions and methods

Metadata: public · line 26

### ByteRange.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.image_match:ByteRange.to_dict`

Metadata: internal · line 30

### _pe_offsets

No function or method docstring is declared in the v0.7.4 source.

```
def _pe_offsets(data: bytes) -> dict[str, int]
```

**Catalog symbol:** `x86decomp.image_match:_pe_offsets`

Metadata: public · line 52

### derive_layout_profile

No function or method docstring is declared in the v0.7.4 source.

```
def derive_layout_profile(reference: Path, *, output: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.image_match:derive_layout_profile`

Metadata: internal · line 91

### _mask_ranges

No function or method docstring is declared in the v0.7.4 source.

```
def _mask_ranges(data: bytes, ranges: Iterable[ByteRange]) -> bytes
```

**Catalog symbol:** `x86decomp.image_match:_mask_ranges`

Metadata: internal · line 100

### _rva_to_file_offset

No function or method docstring is declared in the v0.7.4 source.

```
def _rva_to_file_offset(image: Any, rva: int, file_size: int) -> int | None
```

**Catalog symbol:** `x86decomp.image_match:_rva_to_file_offset`

Metadata: internal · line 110

### _profile_ranges

No function or method docstring is declared in the v0.7.4 source.

```
def _profile_ranges(data: bytes, profile: dict[str, Any], image: Any) -> list[ByteRange]
```

**Catalog symbol:** `x86decomp.image_match:_profile_ranges`

Metadata: internal · line 145

### _apply_rebase

No function or method docstring is declared in the v0.7.4 source.

```
def _apply_rebase(data: bytes, *, target_base: int, candidate_base: int, image: Any) -> bytes
```

**Catalog symbol:** `x86decomp.image_match:_apply_rebase`

Metadata: internal · line 173

### _mismatches

No function or method docstring is declared in the v0.7.4 source.

```
def _mismatches(left: bytes, right: bytes, limit: int = 256) -> tuple[int, list[dict[str, int]]]
```

**Catalog symbol:** `x86decomp.image_match:_mismatches`

Metadata: public · line 186

### compare_whole_images

No function or method docstring is declared in the v0.7.4 source.

```
def compare_whole_images(reference: Path, candidate: Path, *, profile_path: Path | None = None, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.image_match:compare_whole_images`
