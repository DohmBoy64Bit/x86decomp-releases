---
title: x86decomp.governance.proofs
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-governance-proofs.html
---

<a id="function-proofledger-init"></a>
<a id="function-proofledger-create-obligation"></a>
<a id="function-proofledger-add-result"></a>
<a id="function-proofledger-obligation"></a>
<a id="function-proofledger-result"></a>
<a id="function-proofledger-evaluate"></a>
<a id="function-proofbundle-zip-info"></a>
<a id="function-proofbundle-export"></a>
<a id="function-proofbundle-validate-member"></a>
<a id="function-proofbundle-verify"></a>
<a id="function-proofbundle-inspect"></a>

Section: Source-derived feature and function reference

# x86decomp.governance.proofs

No module docstring is declared in the v0.7.4 source.

Metadata: governance · current · 11 functions/methods

**Source:** `src/x86decomp/governance/proofs.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `4a7cc3e36784a2cfb375b573b253737c0afb18671bd6f7a6a9eec5b3ee50ffec`.

## Functions and methods

Metadata: internal · line 20

### ProofLedger.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofLedger.__init__`

Metadata: public · line 24

### ProofLedger.create_obligation

No function or method docstring is declared in the v0.7.4 source.

```
def create_obligation(self, scope_kind: str, scope_id: str, property_name: str, required_status: str, *, assumptions: list[str] | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofLedger.create_obligation`

Metadata: public · line 36

### ProofLedger.add_result

No function or method docstring is declared in the v0.7.4 source.

```
def add_result(self, obligation_id: str, status: str, validator: str, report: dict[str, Any], *, artifact_sha256: str | None = None, actor: str = 'validator') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofLedger.add_result`

Metadata: public · line 51

### ProofLedger.obligation

No function or method docstring is declared in the v0.7.4 source.

```
def obligation(self, obligation_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofLedger.obligation`

Metadata: public · line 62

### ProofLedger.result

No function or method docstring is declared in the v0.7.4 source.

```
def result(self, result_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofLedger.result`

Metadata: public · line 71

### ProofLedger.evaluate

No function or method docstring is declared in the v0.7.4 source.

```
def evaluate(self, obligation_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofLedger.evaluate`

Metadata: internal · line 82

### ProofBundle._zip_info

No function or method docstring is declared in the v0.7.4 source.

```
def _zip_info(name: str) -> zipfile.ZipInfo
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofBundle._zip_info`

Metadata: public · line 89

### ProofBundle.export

No function or method docstring is declared in the v0.7.4 source.

```
def export(cls, store: GovernanceStore, output: str | Path, *, include_paths: list[str | Path] | None = None, hmac_key: bytes | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofBundle.export`

Metadata: internal · line 130

### ProofBundle._validate_member

No function or method docstring is declared in the v0.7.4 source.

```
def _validate_member(name: str) -> None
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofBundle._validate_member`

Metadata: public · line 136

### ProofBundle.verify

No function or method docstring is declared in the v0.7.4 source.

```
def verify(cls, path: str | Path, *, hmac_key: bytes | None = None, max_members: int = 10000, max_total_bytes: int = 1024 * 1024 * 1024) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofBundle.verify`

Metadata: public · line 181

### ProofBundle.inspect

No function or method docstring is declared in the v0.7.4 source.

```
def inspect(cls, path: str | Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.proofs:ProofBundle.inspect`
