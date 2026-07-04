---
title: x86decomp mcp-commit
description: Exact v0.7.8 parser-derived reference for `x86decomp mcp-commit`.
---


# `x86decomp mcp-commit`

## Usage

```text
usage: x86decomp mcp-commit [-h] [--url URL] [--command-json COMMAND_JSON]
                            --allow-tool ALLOW_TOOL
                            project approval_hash
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--url` | parser destination: `url`. No help text declared. |
| `--command-json` | parser destination: `command_json`. No help text declared. |
| `project` | required · type: `_path` · parser destination: `project`. No help text declared. |
| `approval_hash` | required · parser destination: `approval_hash`. No help text declared. |
| `--allow-tool` | required · parser destination: `allow_tool`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
