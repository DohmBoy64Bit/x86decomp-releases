---
title: x86decomp mcp-commit
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/mcp-commit.html
---

<a id="command-mcp-commit"></a>

Section: Command reference

# `x86decomp mcp-commit`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp mcp-commit --help
```

Metadata: current · core

## `x86decomp mcp-commit`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp mcp-commit [-h] [--url URL] [--command-json COMMAND_JSON]
                            --allow-tool ALLOW_TOOL
                            project approval_hash
```

### Syntax example

```
x86decomp mcp-commit ./work example --allow-tool example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `--url` | No argument help text is declared; parser destination is `url`. |
| `--command-json` | No argument help text is declared; parser destination is `command_json`. |
| `project` required · type: _path | No argument help text is declared; parser destination is `project`. |
| `approval_hash` required | No argument help text is declared; parser destination is `approval_hash`. |
| `--allow-tool` required | No argument help text is declared; parser destination is `allow_tool`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.
