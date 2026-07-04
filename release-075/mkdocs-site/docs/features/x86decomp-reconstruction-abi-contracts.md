---
title: x86decomp.reconstruction.abi_contracts
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.reconstruction.abi_contracts`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/reconstruction/abi_contracts.py`  
**SHA-256:** `3a604b7e2a1519a524942ec0aa4cc06fa2281bea86cba2b2a29136ba04ab5bf0`  
**Functions/methods:** 7

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-abicontracts-init"></a>

### `ABIContracts.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def ABIContracts.__init__(self, store: ReconstructionStore)
```

**Catalog symbol:** `x86decomp.reconstruction.abi_contracts:ABIContracts.__init__`  
**Visibility:** internal  
**Source line:** 11

<a id="function-abicontracts-recover"></a>

### `ABIContracts.recover`

No function or method docstring is declared in the 0.7.5 source.

```python
def ABIContracts.recover(self, subject_kind: str, subject_id: str, architecture: str, contract: dict[str, Any], *, evidence: list[dict[str, Any]], actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.abi_contracts:ABIContracts.recover`  
**Visibility:** public  
**Source line:** 12

<a id="function-abicontracts-get"></a>

### `ABIContracts.get`

No function or method docstring is declared in the 0.7.5 source.

```python
def ABIContracts.get(self, contract_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.abi_contracts:ABIContracts.get`  
**Visibility:** public  
**Source line:** 27

<a id="function-abicontracts-verify"></a>

### `ABIContracts.verify`

No function or method docstring is declared in the 0.7.5 source.

```python
def ABIContracts.verify(self, contract_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.abi_contracts:ABIContracts.verify`  
**Visibility:** public  
**Source line:** 31

<a id="function-abicontracts-compare"></a>

### `ABIContracts.compare`

No function or method docstring is declared in the 0.7.5 source.

```python
def ABIContracts.compare(self, left_id: str, right_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.abi_contracts:ABIContracts.compare`  
**Visibility:** public  
**Source line:** 37

<a id="function-abicontracts-export"></a>

### `ABIContracts.export`

No function or method docstring is declared in the 0.7.5 source.

```python
def ABIContracts.export(self, contract_id: str, path: str | Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.abi_contracts:ABIContracts.export`  
**Visibility:** public  
**Source line:** 40

<a id="function-abicontracts-shim"></a>

### `ABIContracts.shim`

No function or method docstring is declared in the 0.7.5 source.

```python
def ABIContracts.shim(self, contract_id: str, source_path: str, *, shim_kind: str='wrapped', actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.abi_contracts:ABIContracts.shim`  
**Visibility:** public  
**Source line:** 42
