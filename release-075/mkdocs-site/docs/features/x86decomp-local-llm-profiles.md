---
title: x86decomp.local_llm.profiles
description: Provider profiles for bounded local-model inference.
---

# `x86decomp.local_llm.profiles`

Provider profiles for bounded local-model inference.

Profiles deliberately contain only transport and inference settings. Secrets are
referenced by environment-variable name and are never persisted in generated
profiles or reports.

**Area:** Toolkit  
**Source:** `src/x86decomp/local_llm/profiles.py`  
**SHA-256:** `5bce6554b8d5dbccd0a18c965bae92e82cc8517f7c86997621d662f3bcff1ca2`  
**Functions/methods:** 8

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-provider-catalog"></a>

### `provider_catalog`

Return the immutable built-in provider preset catalog.

```python
def provider_catalog() -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.local_llm.profiles:provider_catalog`  
**Visibility:** public  
**Source line:** 73

<a id="function-normalized-base-url"></a>

### `_normalized_base_url`

No function or method docstring is declared in the 0.7.5 source.

```python
def _normalized_base_url(value: str) -> str
```

**Catalog symbol:** `x86decomp.local_llm.profiles:_normalized_base_url`  
**Visibility:** internal  
**Source line:** 89

<a id="function-is-loopback-host"></a>

### `is_loopback_host`

Return whether a hostname is an explicit local loopback identity.

```python
def is_loopback_host(hostname: str) -> bool
```

**Catalog symbol:** `x86decomp.local_llm.profiles:is_loopback_host`  
**Visibility:** public  
**Source line:** 105

<a id="function-resolved-addresses-are-loopback"></a>

### `resolved_addresses_are_loopback`

Resolve a host and require every result to be loopback.

This is an additional diagnostic check. The default policy still requires an
explicit loopback hostname, avoiding a DNS name whose answer may change
between validation and request execution.

```python
def resolved_addresses_are_loopback(hostname: str) -> bool
```

**Catalog symbol:** `x86decomp.local_llm.profiles:resolved_addresses_are_loopback`  
**Visibility:** public  
**Source line:** 116

<a id="function-create-profile"></a>

### `create_profile`

Create and persist a validated provider profile.

```python
def create_profile(provider: str, output: Path, *, model: str, base_url: str | None=None, profile_id: str | None=None, api_key_env: str | None=None, allow_remote: bool=False) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.local_llm.profiles:create_profile`  
**Visibility:** public  
**Source line:** 138

<a id="function-load-profile"></a>

### `load_profile`

No function or method docstring is declared in the 0.7.5 source.

```python
def load_profile(path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.local_llm.profiles:load_profile`  
**Visibility:** public  
**Source line:** 178

<a id="function-validate-profile"></a>

### `validate_profile`

Validate and normalize a local-model profile.

```python
def validate_profile(raw: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.local_llm.profiles:validate_profile`  
**Visibility:** public  
**Source line:** 185

<a id="function-public-profile"></a>

### `public_profile`

Return report-safe profile metadata without secret values.

```python
def public_profile(profile: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.local_llm.profiles:public_profile`  
**Visibility:** public  
**Source line:** 246
