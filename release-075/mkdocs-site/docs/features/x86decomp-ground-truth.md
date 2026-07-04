---
title: x86decomp.ground_truth
description: Reproducible compiler/version ground-truth corpus builder.
---

# `x86decomp.ground_truth`

Reproducible compiler/version ground-truth corpus builder.

The corpus records source hashes, compiler hashes and versions, complete command
lines, environment policy, COFF structure, symbols, COMDAT metadata, and output
hashes.  It is designed to compare compiler generations without redistributing
proprietary toolchains: users register their own compiler executables.

**Area:** Toolkit  
**Source:** `src/x86decomp/ground_truth.py`  
**SHA-256:** `9684fbcda0fd5060b3c1f2d0efb83892900c69190d33e24fd7e49f91885181e2`  
**Functions/methods:** 7

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-resolve-executable"></a>

### `_resolve_executable`

No function or method docstring is declared in the 0.7.5 source.

```python
def _resolve_executable(value: str, base: Path) -> Path
```

**Catalog symbol:** `x86decomp.ground_truth:_resolve_executable`  
**Visibility:** internal  
**Source line:** 24

<a id="function-version"></a>

### `_version`

No function or method docstring is declared in the 0.7.5 source.

```python
def _version(executable: Path, arguments: list[str]) -> str
```

**Catalog symbol:** `x86decomp.ground_truth:_version`  
**Visibility:** internal  
**Source line:** 36

<a id="function-expand-flag-matrix"></a>

### `_expand_flag_matrix`

No function or method docstring is declared in the 0.7.5 source.

```python
def _expand_flag_matrix(matrix: dict[str, Any]) -> list[tuple[str, list[str]]]
```

**Catalog symbol:** `x86decomp.ground_truth:_expand_flag_matrix`  
**Visibility:** internal  
**Source line:** 46

<a id="function-build-ground-truth-corpus"></a>

### `build_ground_truth_corpus`

No function or method docstring is declared in the 0.7.5 source.

```python
def build_ground_truth_corpus(manifest_path: Path, output_directory: Path, *, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.ground_truth:build_ground_truth_corpus`  
**Visibility:** public  
**Source line:** 72

<a id="function-verify-ground-truth-corpus"></a>

### `verify_ground_truth_corpus`

No function or method docstring is declared in the 0.7.5 source.

```python
def verify_ground_truth_corpus(report_path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.ground_truth:verify_ground_truth_corpus`  
**Visibility:** public  
**Source line:** 191

<a id="function-compare-ground-truth-corpora"></a>

### `compare_ground_truth_corpora`

Compare successful corpus builds across compiler/version reports.

Builds are aligned by ``case_id`` and ``variant_id``.  Exact output hashes,
COFF section layouts, symbol sets, and compiler identities are reported.
No semantic-equivalence claim is inferred from identical or different
object bytes.

```python
def compare_ground_truth_corpora(report_paths: list[Path], *, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.ground_truth:compare_ground_truth_corpora`  
**Visibility:** public  
**Source line:** 211

<a id="function-create-builtin-manifest"></a>

### `create_builtin_manifest`

No function or method docstring is declared in the 0.7.5 source.

```python
def create_builtin_manifest(root: Path, *, output: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.ground_truth:create_builtin_manifest`  
**Visibility:** public  
**Source line:** 293
