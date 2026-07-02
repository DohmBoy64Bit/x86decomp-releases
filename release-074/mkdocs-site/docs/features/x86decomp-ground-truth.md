---
title: x86decomp.ground_truth
description: Reproducible compiler/version ground-truth corpus builder.
original_path: features/x86decomp-ground-truth.html
---

<a id="function-resolve-executable"></a>
<a id="function-version"></a>
<a id="function-expand-flag-matrix"></a>
<a id="function-build-ground-truth-corpus"></a>
<a id="function-verify-ground-truth-corpus"></a>
<a id="function-compare-ground-truth-corpora"></a>
<a id="function-create-builtin-manifest"></a>

Section: Source-derived feature and function reference

# x86decomp.ground_truth

Reproducible compiler/version ground-truth corpus builder.

Metadata: core · current · 7 functions/methods

**Source:** `src/x86decomp/ground_truth.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `9684fbcda0fd5060b3c1f2d0efb83892900c69190d33e24fd7e49f91885181e2`.

## Functions and methods

Metadata: internal · line 24

### _resolve_executable

No function or method docstring is declared in the v0.7.4 source.

```
def _resolve_executable(value: str, base: Path) -> Path
```

**Catalog symbol:** `x86decomp.ground_truth:_resolve_executable`

Metadata: internal · line 36

### _version

No function or method docstring is declared in the v0.7.4 source.

```
def _version(executable: Path, arguments: list[str]) -> str
```

**Catalog symbol:** `x86decomp.ground_truth:_version`

Metadata: internal · line 46

### _expand_flag_matrix

No function or method docstring is declared in the v0.7.4 source.

```
def _expand_flag_matrix(matrix: dict[str, Any]) -> list[tuple[str, list[str]]]
```

**Catalog symbol:** `x86decomp.ground_truth:_expand_flag_matrix`

Metadata: public · line 72

### build_ground_truth_corpus

No function or method docstring is declared in the v0.7.4 source.

```
def build_ground_truth_corpus(manifest_path: Path, output_directory: Path, *, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.ground_truth:build_ground_truth_corpus`

Metadata: public · line 191

### verify_ground_truth_corpus

No function or method docstring is declared in the v0.7.4 source.

```
def verify_ground_truth_corpus(report_path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.ground_truth:verify_ground_truth_corpus`

Metadata: public · line 211

### compare_ground_truth_corpora

Compare successful corpus builds across compiler/version reports.

```
def compare_ground_truth_corpora(report_paths: list[Path], *, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.ground_truth:compare_ground_truth_corpora`

Metadata: public · line 293

### create_builtin_manifest

No function or method docstring is declared in the v0.7.4 source.

```
def create_builtin_manifest(root: Path, *, output: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.ground_truth:create_builtin_manifest`
