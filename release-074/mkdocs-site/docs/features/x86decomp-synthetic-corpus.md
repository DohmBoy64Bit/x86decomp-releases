---
title: x86decomp.synthetic_corpus
description: Deterministic ground-truth source corpus generation.
original_path: features/x86decomp-synthetic-corpus.html
---

<a id="function-symbol"></a>
<a id="function-c-arithmetic"></a>
<a id="function-c-branches"></a>
<a id="function-c-loop"></a>
<a id="function-c-switch"></a>
<a id="function-c-struct-alias"></a>
<a id="function-c-bitfield"></a>
<a id="function-c-float"></a>
<a id="function-c-indirect"></a>
<a id="function-cpp-virtual"></a>
<a id="function-cpp-multiple-inheritance"></a>
<a id="function-cpp-exception"></a>
<a id="function-cpp-template"></a>
<a id="function-generate-synthetic-corpus"></a>
<a id="function-verify-synthetic-corpus"></a>

Section: Source-derived feature and function reference

# x86decomp.synthetic_corpus

Deterministic ground-truth source corpus generation.

Metadata: core · current · 15 functions/methods

**Source:** `src/x86decomp/synthetic_corpus.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `a0475235f70093de7171e32cbde918a9290569245efaa06f8549cd1ad480ece0`.

## Functions and methods

Metadata: internal · line 25

### _symbol

No function or method docstring is declared in the v0.7.4 source.

```
def _symbol(case_id: str) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_symbol`

Metadata: internal · line 34

### _c_arithmetic

No function or method docstring is declared in the v0.7.4 source.

```
def _c_arithmetic(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_c_arithmetic`

Metadata: internal · line 47

### _c_branches

No function or method docstring is declared in the v0.7.4 source.

```
def _c_branches(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_c_branches`

Metadata: internal · line 63

### _c_loop

No function or method docstring is declared in the v0.7.4 source.

```
def _c_loop(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_c_loop`

Metadata: internal · line 80

### _c_switch

No function or method docstring is declared in the v0.7.4 source.

```
def _c_switch(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_c_switch`

Metadata: internal · line 95

### _c_struct_alias

No function or method docstring is declared in the v0.7.4 source.

```
def _c_struct_alias(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_c_struct_alias`

Metadata: internal · line 118

### _c_bitfield

No function or method docstring is declared in the v0.7.4 source.

```
def _c_bitfield(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_c_bitfield`

Metadata: internal · line 137

### _c_float

No function or method docstring is declared in the v0.7.4 source.

```
def _c_float(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_c_float`

Metadata: internal · line 150

### _c_indirect

No function or method docstring is declared in the v0.7.4 source.

```
def _c_indirect(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_c_indirect`

Metadata: internal · line 161

### _cpp_virtual

No function or method docstring is declared in the v0.7.4 source.

```
def _cpp_virtual(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_cpp_virtual`

Metadata: internal · line 184

### _cpp_multiple_inheritance

No function or method docstring is declared in the v0.7.4 source.

```
def _cpp_multiple_inheritance(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_cpp_multiple_inheritance`

Metadata: internal · line 200

### _cpp_exception

No function or method docstring is declared in the v0.7.4 source.

```
def _cpp_exception(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_cpp_exception`

Metadata: internal · line 216

### _cpp_template

No function or method docstring is declared in the v0.7.4 source.

```
def _cpp_template(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_cpp_template`

Metadata: public · line 243

### generate_synthetic_corpus

Generate deterministic source cases and a compiler-corpus input manifest.

```
def generate_synthetic_corpus(output_directory: Path, *, cases_per_family: int = 8, seed: int = 2262745310, include_c: bool = True, include_cpp: bool = True, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.synthetic_corpus:generate_synthetic_corpus`

Metadata: public · line 331

### verify_synthetic_corpus

No function or method docstring is declared in the v0.7.4 source.

```
def verify_synthetic_corpus(report_path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.synthetic_corpus:verify_synthetic_corpus`
