---
title: x86decomp mcp-read
description: Exact parser-derived reference for x86decomp mcp-read in 0.7.5.
---

# `x86decomp mcp-read`

## `x86decomp mcp-read`

usage: x86decomp mcp-read [-h] [--url URL] [--command-json COMMAND_JSON]

### Usage

```text
x86decomp mcp-read [-h] [--url URL] [--command-json COMMAND_JSON]
                          project tool arguments
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--url` | declared. No help text is declared; parser destination is `url`. |
| `--command-json` | declared. No help text is declared; parser destination is `command_json`. |
| `project` | required · type: `_path`. No help text is declared; parser destination is `project`. |
| `tool` | required. No help text is declared; parser destination is `tool`. |
| `arguments` | required · type: `_json_object`. No help text is declared; parser destination is `arguments`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
