---
title: x86decomp.abi
description: Explicit x86 ABI contracts and bounded static compatibility checks.
---

# `x86decomp.abi`

Explicit x86 ABI contracts and bounded static compatibility checks.

**Area:** Toolkit  
**Source:** `src/x86decomp/abi.py`  
**SHA-256:** `e69b8d4ba247b2e3dbd3553cd207ee8fbe24fe244878c4dabb4afffbebb33903`  
**Functions/methods:** 4

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-abicontract-from-dict"></a>

### `ABIContract.from_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def ABIContract.from_dict(cls, value: Any) -> 'ABIContract'
```

**Catalog symbol:** `x86decomp.abi:ABIContract.from_dict`  
**Visibility:** public  
**Source line:** 46

<a id="function-load-abi-contract"></a>

### `load_abi_contract`

No function or method docstring is declared in the 0.7.5 source.

```python
def load_abi_contract(path: Path) -> ABIContract
```

**Catalog symbol:** `x86decomp.abi:load_abi_contract`  
**Visibility:** public  
**Source line:** 87

<a id="function-analyze-abi"></a>

### `analyze_abi`

No function or method docstring is declared in the 0.7.5 source.

```python
def analyze_abi(code: bytes, *, architecture: str='x86', base_address: int=0) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.abi:analyze_abi`  
**Visibility:** public  
**Source line:** 91

<a id="function-validate-abi"></a>

### `validate_abi`

No function or method docstring is declared in the 0.7.5 source.

```python
def validate_abi(code: bytes, contract: ABIContract, *, base_address: int=0, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.abi:validate_abi`  
**Visibility:** public  
**Source line:** 153
