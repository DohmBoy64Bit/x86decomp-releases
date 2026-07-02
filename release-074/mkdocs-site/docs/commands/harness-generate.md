---
title: x86decomp harness-generate
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/harness-generate.html
---

<a id="command-harness-generate"></a>

Section: Command reference

# `x86decomp harness-generate`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp harness-generate --help
```

Metadata: current · core

## `x86decomp harness-generate`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp harness-generate [-h]
                                  [--pointer-parameters POINTER_PARAMETERS]
                                  [--no-observe-pointers]
                                  [--max-instructions MAX_INSTRUCTIONS]
                                  [--timeout-ms TIMEOUT_MS]
                                  abi_contract output
```

### Syntax example

```
x86decomp harness-generate ./contract.json ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `abi_contract` required · type: _path | No argument help text is declared; parser destination is `abi_contract`. |
| `output` required · type: _path | No argument help text is declared; parser destination is `output`. |
| `--pointer-parameters` type: _path | No argument help text is declared; parser destination is `pointer_parameters`. |
| `--no-observe-pointers` nargs: 0 · default: False | No argument help text is declared; parser destination is `no_observe_pointers`. |
| `--max-instructions` default: 100000 · type: int | No argument help text is declared; parser destination is `max_instructions`. |
| `--timeout-ms` default: 1000 · type: int | No argument help text is declared; parser destination is `timeout_ms`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.
