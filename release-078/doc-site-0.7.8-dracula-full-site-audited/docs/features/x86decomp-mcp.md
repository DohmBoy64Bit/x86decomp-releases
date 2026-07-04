---
title: x86decomp.mcp
description: Source module reference for x86decomp.mcp.
---

# `x86decomp.mcp`

**Source path:** `src/x86decomp/mcp.py`  
**SHA-256:** `72627e41c628c756443bc5d57e38b583b1744923902735b55a3d6c9e29f6cca9`  
**Documented symbols:** 27

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `MCPTool` | class | 23 | 26 | no docstring declared |
| `StdioMCPClient` | class | 29 | 136 | no docstring declared |
| `__init__` | function | 30 | 44 | no docstring declared |
| `_send` | function | 46 | 50 | no docstring declared |
| `_request` | function | 52 | 77 | no docstring declared |
| `initialize` | function | 79 | 90 | no docstring declared |
| `_ensure_initialized` | function | 92 | 94 | no docstring declared |
| `list_tools` | function | 96 | 113 | no docstring declared |
| `call_tool` | function | 115 | 117 | no docstring declared |
| `close` | function | 119 | 130 | no docstring declared |
| `__enter__` | function | 132 | 133 | no docstring declared |
| `__exit__` | function | 135 | 136 | no docstring declared |
| `StreamableHTTPMCPClient` | class | 139 | 213 | no docstring declared |
| `__init__` | function | 140 | 147 | no docstring declared |
| `_request` | function | 149 | 181 | no docstring declared |
| `_notify` | function | 183 | 190 | no docstring declared |
| `initialize` | function | 192 | 196 | no docstring declared |
| `_ensure_initialized` | function | 198 | 200 | no docstring declared |
| `list_tools` | function | 202 | 205 | no docstring declared |
| `call_tool` | function | 207 | 209 | no docstring declared |
| `close` | function | 211 | 213 | Streamable HTTP has no persistent local process to close. |
| `is_probable_mutation` | function | 221 | 223 | no docstring declared |
| `GhidraMCPGateway` | class | 226 | 288 | Separates read calls from hash-approved mutation transactions. |
| `__init__` | function | 229 | 234 | no docstring declared |
| `read` | function | 236 | 241 | no docstring declared |
| `propose_mutation` | function | 243 | 267 | no docstring declared |
| `commit_mutation` | function | 269 | 288 | no docstring declared |
