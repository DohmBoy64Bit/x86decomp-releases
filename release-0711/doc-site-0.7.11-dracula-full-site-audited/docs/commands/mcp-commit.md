---
title: x86decomp mcp-commit
description: Parser-derived command reference page for `mcp-commit`.
---

# `x86decomp mcp-commit`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp mcp-commit [-h] [--url URL] [--command-json COMMAND_JSON]
                            --allow-tool ALLOW_TOOL
                            project approval_hash

positional arguments:
  project
  approval_hash

options:
  -h, --help            show this help message and exit
  --url URL
  --command-json COMMAND_JSON
  --allow-tool ALLOW_TOOL
```
