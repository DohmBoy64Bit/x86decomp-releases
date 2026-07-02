---
title: x86decomp.decompme
description: Create local decomp.me-style function packets without uploading data.
original_path: features/x86decomp-decompme.html
---

<a id="function-copy-required"></a>
<a id="function-create-decompme-packet"></a>

Section: Source-derived feature and function reference

# x86decomp.decompme

Create local decomp.me-style function packets without uploading data.

Metadata: core · current · 2 functions/methods

**Source:** `src/x86decomp/decompme.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `440f011b1a60d6a9549cd558927a158ce34f1377f699a58b922c696619172fe2`.

## Functions and methods

Metadata: internal · line 14

### _copy_required

No function or method docstring is declared in the v0.7.4 source.

```
def _copy_required(source: Path, destination: Path, name: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.decompme:_copy_required`

Metadata: public · line 23

### create_decompme_packet

Build a local, reviewable function packet.

```
def create_decompme_packet(function_artifact: Path, output_directory: Path, *, overwrite: bool = False) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.decompme:create_decompme_packet`
