---
title: x86decomp.integration
description: Module reference for x86decomp.integration.
---

# `x86decomp.integration`

- Area: `toolkit`
- Source path: `src/x86decomp/integration.py`
- SHA-256: `1dd501274cd70e4e97ee72667c488439d1cdd651e92a6306995e5c5655b39779`
- Size: `20437` bytes
- Lines: `487`

## Module docstring

Manifest-driven integration scenario runner.

This module performs real target/candidate process executions with explicit host
execution consent or an external isolation wrapper. It compares only declared
observations and never treats finite scenarios as universal equivalence proof.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_require_string_list` | 24 | Support require string list processing for internal toolkit callers. |
| function | `_resolve_existing` | 33 | Support resolve existing processing for internal toolkit callers. |
| function | `_parse_stdin` | 43 | Support parse stdin processing for internal toolkit callers. |
| function | `_copy_fixtures` | 66 | Support copy fixtures processing for internal toolkit callers. |
| function | `_substitute_command` | 98 | Support substitute command processing for internal toolkit callers. |
| function | `_bounded_output` | 113 | Support bounded output processing for internal toolkit callers. |
| function | `_run_side` | 125 | Support run side processing for internal toolkit callers. |
| function | `_observe_file` | 204 | Support observe file processing for internal toolkit callers. |
| function | `_compare_stream` | 259 | Support compare stream processing for internal toolkit callers. |
| function | `run_integration_scenarios` | 282 | Execute and compare all declared integration scenarios. |
