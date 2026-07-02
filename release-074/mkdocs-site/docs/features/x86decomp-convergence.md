---
title: x86decomp.convergence
description: Target-specific whole-image convergence analysis.
original_path: features/x86decomp-convergence.html
---

<a id="function-section-kind"></a>
<a id="function-analyze-image-convergence"></a>
<a id="function-append-convergence-history"></a>

Section: Source-derived feature and function reference

# x86decomp.convergence

Target-specific whole-image convergence analysis.

Metadata: core · current · 3 functions/methods

**Source:** `src/x86decomp/convergence.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `2b943e9c8c2399089e1b8c2815c0de4cb1bcf0468c09e64a647fef3508922f74`.

## Functions and methods

Metadata: internal · line 20

### _section_kind

No function or method docstring is declared in the v0.7.4 source.

```
def _section_kind(name: str, characteristics: int) -> str
```

**Catalog symbol:** `x86decomp.convergence:_section_kind`

Metadata: public · line 35

### analyze_image_convergence

No function or method docstring is declared in the v0.7.4 source.

```
def analyze_image_convergence(reference: Path, candidate: Path, *, profile_path: Path | None = None, previous_report: Path | None = None, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.convergence:analyze_image_convergence`

Metadata: public · line 165

### append_convergence_history

No function or method docstring is declared in the v0.7.4 source.

```
def append_convergence_history(history_path: Path, report: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.convergence:append_convergence_history`
