---
title: x86decomp.abi
description: Explicit x86 ABI contracts and bounded static compatibility checks.
original_path: features/x86decomp-abi.html
---

<a id="function-abicontract-from-dict"></a>
<a id="function-load-abi-contract"></a>
<a id="function-analyze-abi"></a>
<a id="function-validate-abi"></a>

Section: Source-derived feature and function reference

# x86decomp.abi

Explicit x86 ABI contracts and bounded static compatibility checks.

Metadata: core · current · 4 functions/methods

**Source:** `src/x86decomp/abi.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `e69b8d4ba247b2e3dbd3553cd207ee8fbe24fe244878c4dabb4afffbebb33903`.

## Functions and methods

Metadata: public · line 46

### ABIContract.from_dict

No function or method docstring is declared in the v0.7.4 source.

```
def from_dict(cls, value: Any) -> 'ABIContract'
```

**Catalog symbol:** `x86decomp.abi:ABIContract.from_dict`

Metadata: public · line 87

### load_abi_contract

No function or method docstring is declared in the v0.7.4 source.

```
def load_abi_contract(path: Path) -> ABIContract
```

**Catalog symbol:** `x86decomp.abi:load_abi_contract`

Metadata: public · line 91

### analyze_abi

No function or method docstring is declared in the v0.7.4 source.

```
def analyze_abi(code: bytes, *, architecture: str = 'x86', base_address: int = 0) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.abi:analyze_abi`

Metadata: public · line 153

### validate_abi

No function or method docstring is declared in the v0.7.4 source.

```
def validate_abi(code: bytes, contract: ABIContract, *, base_address: int = 0, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.abi:validate_abi`
