---
title: x86decomp.linker_layout
description: MSVC linker-map parsing and object contribution layout reconstruction.
original_path: features/x86decomp-linker-layout.html
---

<a id="function-mapsegment-to-dict"></a>
<a id="function-mapcontribution-to-dict"></a>
<a id="function-mappublic-to-dict"></a>
<a id="function-linkermap-to-dict"></a>
<a id="function-parse-msvc-map-text"></a>
<a id="function-parse-msvc-map"></a>
<a id="function-normalize-object-key"></a>
<a id="function-reconstruct-linker-layout"></a>

Section: Source-derived feature and function reference

# x86decomp.linker_layout

MSVC linker-map parsing and object contribution layout reconstruction.

Metadata: core · current · 8 functions/methods

**Source:** `src/x86decomp/linker_layout.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `e212e73f09b9559f17e0251eba8260a50b52931091a4972a2deabc462cd68682`.

## Functions and methods

Metadata: public · line 42

### MapSegment.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.linker_layout:MapSegment.to_dict`

Metadata: public · line 59

### MapContribution.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.linker_layout:MapContribution.to_dict`

Metadata: public · line 77

### MapPublic.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.linker_layout:MapPublic.to_dict`

Metadata: public · line 100

### LinkerMap.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.linker_layout:LinkerMap.to_dict`

Metadata: public · line 118

### parse_msvc_map_text

No function or method docstring is declared in the v0.7.4 source.

```
def parse_msvc_map_text(text: str, *, path: Path | None = None) -> LinkerMap
```

**Catalog symbol:** `x86decomp.linker_layout:parse_msvc_map_text`

Metadata: public · line 215

### parse_msvc_map

No function or method docstring is declared in the v0.7.4 source.

```
def parse_msvc_map(path: Path) -> LinkerMap
```

**Catalog symbol:** `x86decomp.linker_layout:parse_msvc_map`

Metadata: internal · line 222

### _normalize_object_key

No function or method docstring is declared in the v0.7.4 source.

```
def _normalize_object_key(value: str) -> str
```

**Catalog symbol:** `x86decomp.linker_layout:_normalize_object_key`

Metadata: public · line 229

### reconstruct_linker_layout

No function or method docstring is declared in the v0.7.4 source.

```
def reconstruct_linker_layout(pe_path: Path, map_path: Path, *, object_paths: Iterable[Path] = (), report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.linker_layout:reconstruct_linker_layout`
