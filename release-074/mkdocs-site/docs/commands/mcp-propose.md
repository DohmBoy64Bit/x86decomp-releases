---
title: x86decomp mcp-propose
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/mcp-propose.html
---

<a id="command-mcp-propose"></a>

Section: Command reference

# `x86decomp mcp-propose`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp mcp-propose --help
```

Metadata: current · core

## `x86decomp mcp-propose`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp mcp-propose [-h] [--url URL] [--command-json COMMAND_JSON]
                             --allow-tool ALLOW_TOOL --rationale RATIONALE
                             --evidence EVIDENCE
                             project tool arguments
```

### Syntax example

```
x86decomp mcp-propose ./work example {} --allow-tool example --rationale reviewed-change --evidence example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `--url` | No argument help text is declared; parser destination is `url`. |
| `--command-json` | No argument help text is declared; parser destination is `command_json`. |
| `project` required · type: _path | No argument help text is declared; parser destination is `project`. |
| `tool` required | No argument help text is declared; parser destination is `tool`. |
| `arguments` required · type: _json_object | No argument help text is declared; parser destination is `arguments`. |
| `--allow-tool` required | No argument help text is declared; parser destination is `allow_tool`. |
| `--rationale` required | No argument help text is declared; parser destination is `rationale`. |
| `--evidence` required | No argument help text is declared; parser destination is `evidence`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.
