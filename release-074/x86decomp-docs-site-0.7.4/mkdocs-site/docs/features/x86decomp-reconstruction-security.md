---
title: x86decomp.reconstruction.security
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-reconstruction-security.html
---

<a id="function-securityreview-init"></a>
<a id="function-securityreview-finding"></a>
<a id="function-securityreview-get"></a>
<a id="function-securityreview-scan"></a>
<a id="function-securityreview-policy"></a>
<a id="function-securityreview-report"></a>

Section: Source-derived feature and function reference

# x86decomp.reconstruction.security

No module docstring is declared in the v0.7.4 source.

Metadata: reconstruction · current · 6 functions/methods

**Source:** `src/x86decomp/reconstruction/security.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `0959bd8e9edb807a04058a9b81857c096e9c91ffb6f8591a885d56ae048760ba`.

## Functions and methods

Metadata: internal · line 9

### SecurityReview.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: ReconstructionStore)
```

**Catalog symbol:** `x86decomp.reconstruction.security:SecurityReview.__init__`

Metadata: public · line 10

### SecurityReview.finding

No function or method docstring is declared in the v0.7.4 source.

```
def finding(self, rule_id: str, severity: str, subject_id: str, summary: str, *, evidence: list[dict[str, Any]], actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.security:SecurityReview.finding`

Metadata: public · line 17

### SecurityReview.get

No function or method docstring is declared in the v0.7.4 source.

```
def get(self, finding_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.security:SecurityReview.get`

Metadata: public · line 21

### SecurityReview.scan

No function or method docstring is declared in the v0.7.4 source.

```
def scan(self, observations: list[dict[str, Any]], *, actor: str = 'scanner') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.security:SecurityReview.scan`

Metadata: public · line 28

### SecurityReview.policy

No function or method docstring is declared in the v0.7.4 source.

```
def policy(self, name: str, policy: dict[str, Any], *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.security:SecurityReview.policy`

Metadata: public · line 33

### SecurityReview.report

No function or method docstring is declared in the v0.7.4 source.

```
def report(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.security:SecurityReview.report`
