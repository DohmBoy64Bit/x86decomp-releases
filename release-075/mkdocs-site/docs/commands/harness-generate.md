---
title: x86decomp harness-generate
description: Exact parser-derived reference for x86decomp harness-generate in 0.7.5.
---

# `x86decomp harness-generate`

## `x86decomp harness-generate`

usage: x86decomp harness-generate [-h]

### Usage

```text
x86decomp harness-generate [-h]
                                  [--pointer-parameters POINTER_PARAMETERS]
                                  [--no-observe-pointers]
                                  [--max-instructions MAX_INSTRUCTIONS]
                                  [--timeout-ms TIMEOUT_MS]
                                  abi_contract output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `abi_contract` | required · type: `_path`. No help text is declared; parser destination is `abi_contract`. |
| `output` | required · type: `_path`. No help text is declared; parser destination is `output`. |
| `--pointer-parameters` | type: `_path`. No help text is declared; parser destination is `pointer_parameters`. |
| `--no-observe-pointers` | default: `False` · nargs: `0`. No help text is declared; parser destination is `no_observe_pointers`. |
| `--max-instructions` | default: `100000` · type: `int`. No help text is declared; parser destination is `max_instructions`. |
| `--timeout-ms` | default: `1000` · type: `int`. No help text is declared; parser destination is `timeout_ms`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
