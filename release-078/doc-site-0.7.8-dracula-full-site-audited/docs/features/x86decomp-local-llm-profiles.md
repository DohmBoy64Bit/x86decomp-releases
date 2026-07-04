---
title: x86decomp.local_llm.profiles
description: Source module reference for x86decomp.local_llm.profiles.
---

# `x86decomp.local_llm.profiles`

**Source path:** `src/x86decomp/local_llm/profiles.py`  
**SHA-256:** `5bce6554b8d5dbccd0a18c965bae92e82cc8517f7c86997621d662f3bcff1ca2`  
**Documented symbols:** 8

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `provider_catalog` | function | 73 | 86 | Return the immutable built-in provider preset catalog. |
| `_normalized_base_url` | function | 89 | 102 | no docstring declared |
| `is_loopback_host` | function | 105 | 113 | Return whether a hostname is an explicit local loopback identity. |
| `resolved_addresses_are_loopback` | function | 116 | 135 | Resolve a host and require every result to be loopback. |
| `create_profile` | function | 138 | 175 | Create and persist a validated provider profile. |
| `load_profile` | function | 178 | 182 | no docstring declared |
| `validate_profile` | function | 185 | 243 | Validate and normalize a local-model profile. |
| `public_profile` | function | 246 | 255 | Return report-safe profile metadata without secret values. |
