---
title: x86decomp.local_llm.profiles
description: Module reference for x86decomp.local_llm.profiles.
---

# `x86decomp.local_llm.profiles`

- Area: `toolkit`
- Source path: `src/x86decomp/local_llm/profiles.py`
- SHA-256: `6d956f6d013147c86d2ca4ff16d110b648871c7f78e31bb7426d268995521da2`
- Size: `10051` bytes
- Lines: `258`

## Module docstring

Provider profiles for bounded local-model inference.

Profiles deliberately contain only transport and inference settings. Secrets are
referenced by environment-variable name and are never persisted in generated
profiles or reports.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `provider_catalog` | 73 | Return the immutable built-in provider preset catalog. |
| function | `_normalized_base_url` | 89 | Support normalized base url processing for internal toolkit callers. |
| function | `is_loopback_host` | 106 | Return whether a hostname is an explicit local loopback identity. |
| function | `resolved_addresses_are_loopback` | 117 | Resolve a host and require every result to be loopback. |
| function | `create_profile` | 139 | Create and persist a validated provider profile. |
| function | `load_profile` | 179 | Load profile for the current toolkit workflow. |
| function | `validate_profile` | 187 | Validate and normalize a local-model profile. |
| function | `public_profile` | 248 | Return report-safe profile metadata without secret values. |
