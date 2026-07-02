---
title: x86decomp.reconstruction.generated_tests
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-reconstruction-generated-tests.html
---

<a id="function-generatedtests-init"></a>
<a id="function-generatedtests-add"></a>
<a id="function-generatedtests-synthesize"></a>
<a id="function-generatedtests-promote-counterexample"></a>
<a id="function-generatedtests-get"></a>
<a id="function-generatedtests-list"></a>
<a id="function-generatedtests-explain"></a>

Section: Source-derived feature and function reference

# x86decomp.reconstruction.generated_tests

No module docstring is declared in the v0.7.4 source.

Metadata: reconstruction · current · 7 functions/methods

**Source:** `src/x86decomp/reconstruction/generated_tests.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `6822bf7dc5d508d8ee684f2a6c1f5eb0e141ef86dbb2c580c320561d2b760aaf`.

## Functions and methods

Metadata: internal · line 10

### GeneratedTests.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: ReconstructionStore)
```

**Catalog symbol:** `x86decomp.reconstruction.generated_tests:GeneratedTests.__init__`

Metadata: public · line 11

### GeneratedTests.add

No function or method docstring is declared in the v0.7.4 source.

```
def add(self, name: str, scope_kind: str, scope_id: str, test_kind: str, relative_path: str, content: str, *, applicability: dict[str, Any], evidence: list[dict[str, Any]], actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.generated_tests:GeneratedTests.add`

Metadata: public · line 20

### GeneratedTests.synthesize

No function or method docstring is declared in the v0.7.4 source.

```
def synthesize(self, scope_kind: str, scope_id: str, *, name: str | None = None, actor: str = 'planner') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.generated_tests:GeneratedTests.synthesize`

Metadata: public · line 27

### GeneratedTests.promote_counterexample

No function or method docstring is declared in the v0.7.4 source.

```
def promote_counterexample(self, counterexample_id: str, *, name: str | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.generated_tests:GeneratedTests.promote_counterexample`

Metadata: public · line 32

### GeneratedTests.get

No function or method docstring is declared in the v0.7.4 source.

```
def get(self, test_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.generated_tests:GeneratedTests.get`

Metadata: public · line 36

### GeneratedTests.list

No function or method docstring is declared in the v0.7.4 source.

```
def list(self) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.reconstruction.generated_tests:GeneratedTests.list`

Metadata: public · line 39

### GeneratedTests.explain

No function or method docstring is declared in the v0.7.4 source.

```
def explain(self, test_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.generated_tests:GeneratedTests.explain`
