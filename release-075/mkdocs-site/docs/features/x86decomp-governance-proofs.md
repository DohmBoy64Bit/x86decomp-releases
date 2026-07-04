---
title: x86decomp.governance.proofs
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.governance.proofs`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/governance/proofs.py`  
**SHA-256:** `6b0a3cd153c9d97c72654c503c61212c99cb6d0df2d776df2c7bfa6d4c68e994`  
**Functions/methods:** 11

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-proofledger-init"></a>

### `ProofLedger.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProofLedger.__init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofLedger.__init__`  
**Visibility:** internal  
**Source line:** 20

<a id="function-proofledger-create-obligation"></a>

### `ProofLedger.create_obligation`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProofLedger.create_obligation(self, scope_kind: str, scope_id: str, property_name: str, required_status: str, *, assumptions: list[str] | None=None, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofLedger.create_obligation`  
**Visibility:** public  
**Source line:** 24

<a id="function-proofledger-add-result"></a>

### `ProofLedger.add_result`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProofLedger.add_result(self, obligation_id: str, status: str, validator: str, report: dict[str, Any], *, artifact_sha256: str | None=None, actor: str='validator') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofLedger.add_result`  
**Visibility:** public  
**Source line:** 36

<a id="function-proofledger-obligation"></a>

### `ProofLedger.obligation`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProofLedger.obligation(self, obligation_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofLedger.obligation`  
**Visibility:** public  
**Source line:** 51

<a id="function-proofledger-result"></a>

### `ProofLedger.result`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProofLedger.result(self, result_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofLedger.result`  
**Visibility:** public  
**Source line:** 62

<a id="function-proofledger-evaluate"></a>

### `ProofLedger.evaluate`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProofLedger.evaluate(self, obligation_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofLedger.evaluate`  
**Visibility:** public  
**Source line:** 71

<a id="function-proofbundle-zip-info"></a>

### `ProofBundle._zip_info`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProofBundle._zip_info(name: str) -> zipfile.ZipInfo
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofBundle._zip_info`  
**Visibility:** internal  
**Source line:** 82

<a id="function-proofbundle-export"></a>

### `ProofBundle.export`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProofBundle.export(cls, store: GovernanceStore, output: str | Path, *, include_paths: list[str | Path] | None=None, hmac_key: bytes | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofBundle.export`  
**Visibility:** public  
**Source line:** 89

<a id="function-proofbundle-validate-member"></a>

### `ProofBundle._validate_member`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProofBundle._validate_member(name: str) -> None
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofBundle._validate_member`  
**Visibility:** internal  
**Source line:** 130

<a id="function-proofbundle-verify"></a>

### `ProofBundle.verify`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProofBundle.verify(cls, path: str | Path, *, hmac_key: bytes | None=None, max_members: int=10000, max_total_bytes: int=1024 * 1024 * 1024) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofBundle.verify`  
**Visibility:** public  
**Source line:** 136

<a id="function-proofbundle-inspect"></a>

### `ProofBundle.inspect`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProofBundle.inspect(cls, path: str | Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofBundle.inspect`  
**Visibility:** public  
**Source line:** 181
