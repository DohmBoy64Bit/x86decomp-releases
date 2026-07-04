---
title: x86decomp.convergence
description: Target-specific whole-image convergence analysis.
---

# `x86decomp.convergence`

Target-specific whole-image convergence analysis.

The engine classifies observed differences and ranks next actions.  It never
claims causality unless the mismatch falls inside a declared PE field or
normalization range.

**Area:** Toolkit  
**Source:** `src/x86decomp/convergence.py`  
**SHA-256:** `2b943e9c8c2399089e1b8c2815c0de4cb1bcf0468c09e64a647fef3508922f74`  
**Functions/methods:** 3

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-section-kind"></a>

### `_section_kind`

No function or method docstring is declared in the 0.7.5 source.

```python
def _section_kind(name: str, characteristics: int) -> str
```

**Catalog symbol:** `x86decomp.convergence:_section_kind`  
**Visibility:** internal  
**Source line:** 20

<a id="function-analyze-image-convergence"></a>

### `analyze_image_convergence`

No function or method docstring is declared in the 0.7.5 source.

```python
def analyze_image_convergence(reference: Path, candidate: Path, *, profile_path: Path | None=None, previous_report: Path | None=None, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.convergence:analyze_image_convergence`  
**Visibility:** public  
**Source line:** 35

<a id="function-append-convergence-history"></a>

### `append_convergence_history`

No function or method docstring is declared in the 0.7.5 source.

```python
def append_convergence_history(history_path: Path, report: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.convergence:append_convergence_history`  
**Visibility:** public  
**Source line:** 165
