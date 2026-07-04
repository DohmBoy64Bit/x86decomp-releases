---
title: x86decomp.synthetic_corpus
description: Deterministic ground-truth source corpus generation.
---

# `x86decomp.synthetic_corpus`

Deterministic ground-truth source corpus generation.

The generator expands a small, reviewed family of source templates into a
configurable set of C and C++ translation units.  Every generated file is
content-hashed and described by parameters in a manifest.  The output is
source evidence only: generation does not claim that any compiler, optimization
level, or resulting binary has been tested until ``ground-truth-build`` records
a successful build.

**Area:** Toolkit  
**Source:** `src/x86decomp/synthetic_corpus.py`  
**SHA-256:** `a0475235f70093de7171e32cbde918a9290569245efaa06f8549cd1ad480ece0`  
**Functions/methods:** 15

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-symbol"></a>

### `_symbol`

No function or method docstring is declared in the 0.7.5 source.

```python
def _symbol(case_id: str) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_symbol`  
**Visibility:** internal  
**Source line:** 25

<a id="function-c-arithmetic"></a>

### `_c_arithmetic`

No function or method docstring is declared in the 0.7.5 source.

```python
def _c_arithmetic(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_c_arithmetic`  
**Visibility:** internal  
**Source line:** 34

<a id="function-c-branches"></a>

### `_c_branches`

No function or method docstring is declared in the 0.7.5 source.

```python
def _c_branches(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_c_branches`  
**Visibility:** internal  
**Source line:** 47

<a id="function-c-loop"></a>

### `_c_loop`

No function or method docstring is declared in the 0.7.5 source.

```python
def _c_loop(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_c_loop`  
**Visibility:** internal  
**Source line:** 63

<a id="function-c-switch"></a>

### `_c_switch`

No function or method docstring is declared in the 0.7.5 source.

```python
def _c_switch(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_c_switch`  
**Visibility:** internal  
**Source line:** 80

<a id="function-c-struct-alias"></a>

### `_c_struct_alias`

No function or method docstring is declared in the 0.7.5 source.

```python
def _c_struct_alias(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_c_struct_alias`  
**Visibility:** internal  
**Source line:** 95

<a id="function-c-bitfield"></a>

### `_c_bitfield`

No function or method docstring is declared in the 0.7.5 source.

```python
def _c_bitfield(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_c_bitfield`  
**Visibility:** internal  
**Source line:** 118

<a id="function-c-float"></a>

### `_c_float`

No function or method docstring is declared in the 0.7.5 source.

```python
def _c_float(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_c_float`  
**Visibility:** internal  
**Source line:** 137

<a id="function-c-indirect"></a>

### `_c_indirect`

No function or method docstring is declared in the 0.7.5 source.

```python
def _c_indirect(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_c_indirect`  
**Visibility:** internal  
**Source line:** 150

<a id="function-cpp-virtual"></a>

### `_cpp_virtual`

No function or method docstring is declared in the 0.7.5 source.

```python
def _cpp_virtual(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_cpp_virtual`  
**Visibility:** internal  
**Source line:** 161

<a id="function-cpp-multiple-inheritance"></a>

### `_cpp_multiple_inheritance`

No function or method docstring is declared in the 0.7.5 source.

```python
def _cpp_multiple_inheritance(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_cpp_multiple_inheritance`  
**Visibility:** internal  
**Source line:** 184

<a id="function-cpp-exception"></a>

### `_cpp_exception`

No function or method docstring is declared in the 0.7.5 source.

```python
def _cpp_exception(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_cpp_exception`  
**Visibility:** internal  
**Source line:** 200

<a id="function-cpp-template"></a>

### `_cpp_template`

No function or method docstring is declared in the 0.7.5 source.

```python
def _cpp_template(case_id: str, rng: random.Random) -> str
```

**Catalog symbol:** `x86decomp.synthetic_corpus:_cpp_template`  
**Visibility:** internal  
**Source line:** 216

<a id="function-generate-synthetic-corpus"></a>

### `generate_synthetic_corpus`

Generate deterministic source cases and a compiler-corpus input manifest.

The operation refuses a non-empty output directory to prevent accidental
mixing of source corpora with different parameters.

```python
def generate_synthetic_corpus(output_directory: Path, *, cases_per_family: int=8, seed: int=2262745310, include_c: bool=True, include_cpp: bool=True, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.synthetic_corpus:generate_synthetic_corpus`  
**Visibility:** public  
**Source line:** 243

<a id="function-verify-synthetic-corpus"></a>

### `verify_synthetic_corpus`

No function or method docstring is declared in the 0.7.5 source.

```python
def verify_synthetic_corpus(report_path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.synthetic_corpus:verify_synthetic_corpus`  
**Visibility:** public  
**Source line:** 331
