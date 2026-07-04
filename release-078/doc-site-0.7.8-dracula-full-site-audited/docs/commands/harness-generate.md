---
title: x86decomp harness-generate
description: Exact v0.7.8 parser-derived reference for `x86decomp harness-generate`.
---


# `x86decomp harness-generate`

## Usage

```text
usage: x86decomp harness-generate [-h]
                                  [--pointer-parameters POINTER_PARAMETERS]
                                  [--no-observe-pointers]
                                  [--max-instructions MAX_INSTRUCTIONS]
                                  [--timeout-ms TIMEOUT_MS]
                                  abi_contract output
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `abi_contract` | required · type: `_path` · parser destination: `abi_contract`. No help text declared. |
| `output` | required · type: `_path` · parser destination: `output`. No help text declared. |
| `--pointer-parameters` | type: `_path` · parser destination: `pointer_parameters`. No help text declared. |
| `--no-observe-pointers` | nargs: `0` · default: `False` · parser destination: `no_observe_pointers`. No help text declared. |
| `--max-instructions` | type: `int` · default: `100000` · parser destination: `max_instructions`. No help text declared. |
| `--timeout-ms` | type: `int` · default: `1000` · parser destination: `timeout_ms`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
