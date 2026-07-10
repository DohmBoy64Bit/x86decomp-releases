---
title: x86decomp mcp-tools
description: Parser-derived command reference page for `mcp-tools`.
---

# `x86decomp mcp-tools`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp mcp-tools [-h] [--url URL] [--command-json COMMAND_JSON]

options:
  -h, --help            show this help message and exit
  --url URL
  --command-json COMMAND_JSON
```
