---
title: x86decomp.mcp
description: Module reference for x86decomp.mcp.
---

# `x86decomp.mcp`

- Area: `toolkit`
- Source path: `src/x86decomp/mcp.py`
- SHA-256: `061836293bf188b96de9dca62dfda3710fd51c313a5eff738224eed135fd5e59`
- Size: `14390` bytes
- Lines: `314`

## Module docstring

MCP 2025-06-18 client and evidence-gated Ghidra mutation journal.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `MCPTool` | 23 | Store validated m c p tool fields used by toolkit reports and adapters. |
| class | `StdioMCPClient` | 30 | Coordinate stdio m c p client behavior for the current toolkit workflow. |
| function | `__init__` | 32 | Initialize the instance with validated constructor state. |
| function | `_send` | 49 | Support send processing for internal toolkit callers. |
| function | `_request` | 56 | Support request processing for internal toolkit callers. |
| function | `initialize` | 84 | Initialize initialize for the current toolkit workflow. |
| function | `_ensure_initialized` | 98 | Support ensure initialized processing for internal toolkit callers. |
| function | `list_tools` | 103 | Execute the list tools operation for the current toolkit workflow. |
| function | `call_tool` | 123 | Execute the call tool operation for the current toolkit workflow. |
| function | `close` | 128 | Execute the close operation for the current toolkit workflow. |
| function | `__enter__` | 142 | Enter the managed runtime context and return the active resource. |
| function | `__exit__` | 146 | Exit the managed runtime context and release owned resources. |
| class | `StreamableHTTPMCPClient` | 151 | Coordinate streamable h t t p m c p client behavior for the current toolkit workflow. |
| function | `__init__` | 153 | Initialize the instance with validated constructor state. |
| function | `_request` | 163 | Support request processing for internal toolkit callers. |
| function | `_notify` | 198 | Support notify processing for internal toolkit callers. |
| function | `initialize` | 208 | Initialize initialize for the current toolkit workflow. |
| function | `_ensure_initialized` | 215 | Support ensure initialized processing for internal toolkit callers. |
| function | `list_tools` | 220 | Execute the list tools operation for the current toolkit workflow. |
| function | `call_tool` | 226 | Execute the call tool operation for the current toolkit workflow. |
| function | `close` | 231 | Streamable HTTP has no persistent local process to close. |
| function | `is_probable_mutation` | 241 | Execute the is probable mutation operation for the current toolkit workflow. |
| class | `GhidraMCPGateway` | 247 | Separates read calls from hash-approved mutation transactions. |
| function | `__init__` | 250 | Initialize the instance with validated constructor state. |
| function | `read` | 258 | Read read for the current toolkit workflow. |
| function | `propose_mutation` | 266 | Execute the propose mutation operation for the current toolkit workflow. |
| function | `commit_mutation` | 293 | Execute the commit mutation operation for the current toolkit workflow. |
