---
title: x86decomp.benchmarks
description: Ground-truth corpus runner and decomposed benchmark metrics.
original_path: features/x86decomp-benchmarks.html
---

<a id="function-classification-metrics"></a>
<a id="function-resolve"></a>
<a id="function-run-benchmark-corpus"></a>

Section: Source-derived feature and function reference

# x86decomp.benchmarks

Ground-truth corpus runner and decomposed benchmark metrics.

Metadata: core · current · 3 functions/methods

**Source:** `src/x86decomp/benchmarks.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `b9b28fbcb2f38723b274e4150b1c3914ddcbceab1b49461fc5797a84f9e13fb3`.

## Functions and methods

Metadata: public · line 17

### classification_metrics

No function or method docstring is declared in the v0.7.4 source.

```
def classification_metrics(expected: set[Hashable], observed: set[Hashable]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.benchmarks:classification_metrics`

Metadata: internal · line 34

### _resolve

No function or method docstring is declared in the v0.7.4 source.

```
def _resolve(base: Path, value: Any) -> Path
```

**Catalog symbol:** `x86decomp.benchmarks:_resolve`

Metadata: public · line 40

### run_benchmark_corpus

No function or method docstring is declared in the v0.7.4 source.

```
def run_benchmark_corpus(manifest_path: Path, *, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.benchmarks:run_benchmark_corpus`
