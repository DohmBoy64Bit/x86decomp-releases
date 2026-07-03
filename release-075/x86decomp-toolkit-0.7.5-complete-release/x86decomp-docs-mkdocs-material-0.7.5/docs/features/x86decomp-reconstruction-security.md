---
title: x86decomp.reconstruction.security
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.reconstruction.security`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/reconstruction/security.py`  
**SHA-256:** `0959bd8e9edb807a04058a9b81857c096e9c91ffb6f8591a885d56ae048760ba`  
**Functions/methods:** 6

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-securityreview-init"></a>

### `SecurityReview.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def SecurityReview.__init__(self, store: ReconstructionStore)
```

**Catalog symbol:** `x86decomp.reconstruction.security:SecurityReview.__init__`  
**Visibility:** internal  
**Source line:** 9

<a id="function-securityreview-finding"></a>

### `SecurityReview.finding`

No function or method docstring is declared in the 0.7.5 source.

```python
def SecurityReview.finding(self, rule_id: str, severity: str, subject_id: str, summary: str, *, evidence: list[dict[str, Any]], actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.security:SecurityReview.finding`  
**Visibility:** public  
**Source line:** 10

<a id="function-securityreview-get"></a>

### `SecurityReview.get`

No function or method docstring is declared in the 0.7.5 source.

```python
def SecurityReview.get(self, finding_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.security:SecurityReview.get`  
**Visibility:** public  
**Source line:** 17

<a id="function-securityreview-scan"></a>

### `SecurityReview.scan`

No function or method docstring is declared in the 0.7.5 source.

```python
def SecurityReview.scan(self, observations: list[dict[str, Any]], *, actor: str='scanner') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.security:SecurityReview.scan`  
**Visibility:** public  
**Source line:** 21

<a id="function-securityreview-policy"></a>

### `SecurityReview.policy`

No function or method docstring is declared in the 0.7.5 source.

```python
def SecurityReview.policy(self, name: str, policy: dict[str, Any], *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.security:SecurityReview.policy`  
**Visibility:** public  
**Source line:** 28

<a id="function-securityreview-report"></a>

### `SecurityReview.report`

No function or method docstring is declared in the 0.7.5 source.

```python
def SecurityReview.report(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.security:SecurityReview.report`  
**Visibility:** public  
**Source line:** 33
