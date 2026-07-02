---
title: x86decomp.governance.counterexamples
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-governance-counterexamples.html
---

<a id="function-counterexamplestore-init"></a>
<a id="function-counterexamplestore-add"></a>
<a id="function-counterexamplestore-minimize"></a>
<a id="function-counterexamplestore-promote-to-regression"></a>
<a id="function-counterexamplestore-get"></a>
<a id="function-counterexamplestore-list"></a>
<a id="function-ddmin-bytes"></a>

Section: Source-derived feature and function reference

# x86decomp.governance.counterexamples

No module docstring is declared in the v0.7.4 source.

Metadata: governance · current · 7 functions/methods

**Source:** `src/x86decomp/governance/counterexamples.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `2223bd0eec9a09b58739850670b5d3434dfce554a3578cbe2ab870e43e698096`.

## Functions and methods

Metadata: internal · line 15

### CounterexampleStore.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.counterexamples:CounterexampleStore.__init__`

Metadata: public · line 20

### CounterexampleStore.add

No function or method docstring is declared in the v0.7.4 source.

```
def add(self, scope_kind: str, scope_id: str, payload: bytes | str | Path, *, predicate: dict[str, Any], provenance: dict[str, Any] | None = None, actor: str = 'validator') -> str
```

**Catalog symbol:** `x86decomp.governance.counterexamples:CounterexampleStore.add`

Metadata: public · line 38

### CounterexampleStore.minimize

No function or method docstring is declared in the v0.7.4 source.

```
def minimize(self, counterexample_id: str, predicate: Predicate, *, actor: str = 'validator', max_tests: int = 10000) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.counterexamples:CounterexampleStore.minimize`

Metadata: public · line 63

### CounterexampleStore.promote_to_regression

No function or method docstring is declared in the v0.7.4 source.

```
def promote_to_regression(self, counterexample_id: str, destination_root: str | Path, *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.counterexamples:CounterexampleStore.promote_to_regression`

Metadata: public · line 79

### CounterexampleStore.get

No function or method docstring is declared in the v0.7.4 source.

```
def get(self, counterexample_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.counterexamples:CounterexampleStore.get`

Metadata: public · line 90

### CounterexampleStore.list

No function or method docstring is declared in the v0.7.4 source.

```
def list(self) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.governance.counterexamples:CounterexampleStore.list`

Metadata: public · line 96

### ddmin_bytes

Delta-debug a byte string while preserving predicate(data) == True.

```
def ddmin_bytes(data: bytes, predicate: Predicate, *, max_tests: int = 10000) -> tuple[bytes, int]
```

**Catalog symbol:** `x86decomp.governance.counterexamples:ddmin_bytes`
