---
title: x86decomp.mcp
description: Source module reference for x86decomp.mcp.
---

# `x86decomp.mcp`

**Source path:** `src/x86decomp/mcp.py`  
**Documented symbols:** 27

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `MCPTool` | class | 23 | 26 | — |
| `StdioMCPClient` | class | 29 | 136 | — |
| `__init__` | function | 30 | 44 | — |
| `_send` | function | 46 | 50 | — |
| `_request` | function | 52 | 77 | — |
| `initialize` | function | 79 | 90 | — |
| `_ensure_initialized` | function | 92 | 94 | — |
| `list_tools` | function | 96 | 113 | — |
| `call_tool` | function | 115 | 117 | — |
| `close` | function | 119 | 130 | — |
| `__enter__` | function | 132 | 133 | — |
| `__exit__` | function | 135 | 136 | — |
| `StreamableHTTPMCPClient` | class | 139 | 213 | — |
| `__init__` | function | 140 | 147 | — |
| `_request` | function | 149 | 181 | — |
| `_notify` | function | 183 | 190 | — |
| `initialize` | function | 192 | 196 | — |
| `_ensure_initialized` | function | 198 | 200 | — |
| `list_tools` | function | 202 | 205 | — |
| `call_tool` | function | 207 | 209 | — |
| `close` | function | 211 | 213 | Streamable HTTP has no persistent local process to close. |
| `is_probable_mutation` | function | 221 | 223 | — |
| `GhidraMCPGateway` | class | 226 | 288 | Separates read calls from hash-approved mutation transactions. |
| `__init__` | function | 229 | 234 | — |
| `read` | function | 236 | 241 | — |
| `propose_mutation` | function | 243 | 267 | — |
| `commit_mutation` | function | 269 | 288 | — |
