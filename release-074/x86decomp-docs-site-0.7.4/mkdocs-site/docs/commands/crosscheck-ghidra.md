---
title: x86decomp crosscheck-ghidra
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/crosscheck-ghidra.html
---

<a id="command-crosscheck-ghidra"></a>

Section: Command reference

# `x86decomp crosscheck-ghidra`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp crosscheck-ghidra --help
```

Metadata: current · core

## `x86decomp crosscheck-ghidra`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp crosscheck-ghidra [-h] --base BASE
                                   [--architecture {x86,x86_64}]
                                   [--report REPORT]
                                   instructions_jsonl code
```

### Syntax example

```
x86decomp crosscheck-ghidra ./instructions.jsonl ./function.bin --base 0x400000
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `instructions_jsonl` required · type: _path | No argument help text is declared; parser destination is `instructions_jsonl`. |
| `code` required · type: _path | No argument help text is declared; parser destination is `code`. |
| `--base` required · type: _int | No argument help text is declared; parser destination is `base`. |
| `--architecture` default: 'x86' · choices: x86, x86_64 | No argument help text is declared; parser destination is `architecture`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.
