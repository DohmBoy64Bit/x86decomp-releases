---
title: x86decomp_testkit.adapters.capabilities
description: Module reference for x86decomp_testkit.adapters.capabilities.
---

# `x86decomp_testkit.adapters.capabilities`

- Area: `test-suite`
- Source path: `test-suite/src/x86decomp_testkit/adapters/capabilities.py`
- SHA-256: `e0ddf047e75550e1a2a0263951f9bc275753d355fa4b096d76d1c89a9da7b756`
- Size: `5859` bytes
- Lines: `139`

## Module docstring

Provide the installed test-suite implementation for the `x86decomp_testkit.adapters.capabilities` module.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `CapabilityResult` | 22 | Store validated capability result fields used by toolkit reports and adapters. |
| function | `to_dict` | 29 | Return a serializable dictionary representation. |
| function | `host_is_loopback` | 34 | Execute the host is loopback operation for the current toolkit workflow. |
| function | `endpoint_is_allowed` | 50 | Execute the endpoint is allowed operation for the current toolkit workflow. |
| function | `normalize_endpoint` | 58 | Normalize endpoint for the current toolkit workflow. |
| function | `probe_openai_compatible_endpoint` | 69 | Execute the probe openai compatible endpoint operation for the current toolkit workflow. |
| function | `capabilities_from_adapters` | 97 | Execute the capabilities from adapters operation for the current toolkit workflow. |
| function | `capability_map` | 129 | Execute the capability map operation for the current toolkit workflow. |
| function | `write_capability_report` | 134 | Write capability report for the current toolkit workflow. |
