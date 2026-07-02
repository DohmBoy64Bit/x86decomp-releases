---
title: x86decomp.reconstruction.abi_contracts
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-reconstruction-abi-contracts.html
---

<a id="function-abicontracts-init"></a>
<a id="function-abicontracts-recover"></a>
<a id="function-abicontracts-get"></a>
<a id="function-abicontracts-verify"></a>
<a id="function-abicontracts-compare"></a>
<a id="function-abicontracts-export"></a>
<a id="function-abicontracts-shim"></a>

Section: Source-derived feature and function reference

# x86decomp.reconstruction.abi_contracts

No module docstring is declared in the v0.7.4 source.

Metadata: reconstruction · current · 7 functions/methods

**Source:** `src/x86decomp/reconstruction/abi_contracts.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `3a604b7e2a1519a524942ec0aa4cc06fa2281bea86cba2b2a29136ba04ab5bf0`.

## Functions and methods

Metadata: internal · line 11

### ABIContracts.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: ReconstructionStore)
```

**Catalog symbol:** `x86decomp.reconstruction.abi_contracts:ABIContracts.__init__`

Metadata: public · line 12

### ABIContracts.recover

No function or method docstring is declared in the v0.7.4 source.

```
def recover(self, subject_kind: str, subject_id: str, architecture: str, contract: dict[str, Any], *, evidence: list[dict[str, Any]], actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.abi_contracts:ABIContracts.recover`

Metadata: public · line 27

### ABIContracts.get

No function or method docstring is declared in the v0.7.4 source.

```
def get(self, contract_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.abi_contracts:ABIContracts.get`

Metadata: public · line 31

### ABIContracts.verify

No function or method docstring is declared in the v0.7.4 source.

```
def verify(self, contract_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.abi_contracts:ABIContracts.verify`

Metadata: public · line 37

### ABIContracts.compare

No function or method docstring is declared in the v0.7.4 source.

```
def compare(self, left_id: str, right_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.abi_contracts:ABIContracts.compare`

Metadata: public · line 40

### ABIContracts.export

No function or method docstring is declared in the v0.7.4 source.

```
def export(self, contract_id: str, path: str | Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.abi_contracts:ABIContracts.export`

Metadata: public · line 42

### ABIContracts.shim

No function or method docstring is declared in the v0.7.4 source.

```
def shim(self, contract_id: str, source_path: str, *, shim_kind: str = 'wrapped', actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.abi_contracts:ABIContracts.shim`
