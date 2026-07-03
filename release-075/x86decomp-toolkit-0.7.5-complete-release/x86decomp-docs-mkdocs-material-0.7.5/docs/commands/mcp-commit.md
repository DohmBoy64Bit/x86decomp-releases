---
title: x86decomp mcp-commit
description: Exact parser-derived reference for x86decomp mcp-commit in 0.7.5.
---

# `x86decomp mcp-commit`

## `x86decomp mcp-commit`

usage: x86decomp mcp-commit [-h] [--url URL] [--command-json COMMAND_JSON]

### Usage

```text
x86decomp mcp-commit [-h] [--url URL] [--command-json COMMAND_JSON]
                            --allow-tool ALLOW_TOOL
                            project approval_hash
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--url` | declared. No help text is declared; parser destination is `url`. |
| `--command-json` | declared. No help text is declared; parser destination is `command_json`. |
| `project` | required · type: `_path`. No help text is declared; parser destination is `project`. |
| `approval_hash` | required. No help text is declared; parser destination is `approval_hash`. |
| `--allow-tool` | required. No help text is declared; parser destination is `allow_tool`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
