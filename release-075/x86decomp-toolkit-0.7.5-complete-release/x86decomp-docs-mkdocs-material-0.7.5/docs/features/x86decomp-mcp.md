---
title: x86decomp.mcp
description: MCP 2025-06-18 client and evidence-gated Ghidra mutation journal.
---

# `x86decomp.mcp`

MCP 2025-06-18 client and evidence-gated Ghidra mutation journal.

**Area:** Toolkit  
**Source:** `src/x86decomp/mcp.py`  
**SHA-256:** `72627e41c628c756443bc5d57e38b583b1744923902735b55a3d6c9e29f6cca9`  
**Functions/methods:** 23

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-stdiomcpclient-init"></a>

### `StdioMCPClient.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def StdioMCPClient.__init__(self, command: list[str], *, cwd: Path | None=None)
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient.__init__`  
**Visibility:** internal  
**Source line:** 30

<a id="function-stdiomcpclient-send"></a>

### `StdioMCPClient._send`

No function or method docstring is declared in the 0.7.5 source.

```python
def StdioMCPClient._send(self, message: dict[str, Any]) -> None
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient._send`  
**Visibility:** internal  
**Source line:** 46

<a id="function-stdiomcpclient-request"></a>

### `StdioMCPClient._request`

No function or method docstring is declared in the 0.7.5 source.

```python
def StdioMCPClient._request(self, method: str, params: dict[str, Any] | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient._request`  
**Visibility:** internal  
**Source line:** 52

<a id="function-stdiomcpclient-initialize"></a>

### `StdioMCPClient.initialize`

No function or method docstring is declared in the 0.7.5 source.

```python
def StdioMCPClient.initialize(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient.initialize`  
**Visibility:** public  
**Source line:** 79

<a id="function-stdiomcpclient-ensure-initialized"></a>

### `StdioMCPClient._ensure_initialized`

No function or method docstring is declared in the 0.7.5 source.

```python
def StdioMCPClient._ensure_initialized(self) -> None
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient._ensure_initialized`  
**Visibility:** internal  
**Source line:** 92

<a id="function-stdiomcpclient-list-tools"></a>

### `StdioMCPClient.list_tools`

No function or method docstring is declared in the 0.7.5 source.

```python
def StdioMCPClient.list_tools(self) -> list[MCPTool]
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient.list_tools`  
**Visibility:** public  
**Source line:** 96

<a id="function-stdiomcpclient-call-tool"></a>

### `StdioMCPClient.call_tool`

No function or method docstring is declared in the 0.7.5 source.

```python
def StdioMCPClient.call_tool(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient.call_tool`  
**Visibility:** public  
**Source line:** 115

<a id="function-stdiomcpclient-close"></a>

### `StdioMCPClient.close`

No function or method docstring is declared in the 0.7.5 source.

```python
def StdioMCPClient.close(self) -> None
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient.close`  
**Visibility:** public  
**Source line:** 119

<a id="function-stdiomcpclient-enter"></a>

### `StdioMCPClient.__enter__`

No function or method docstring is declared in the 0.7.5 source.

```python
def StdioMCPClient.__enter__(self) -> 'StdioMCPClient'
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient.__enter__`  
**Visibility:** internal  
**Source line:** 132

<a id="function-stdiomcpclient-exit"></a>

### `StdioMCPClient.__exit__`

No function or method docstring is declared in the 0.7.5 source.

```python
def StdioMCPClient.__exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient.__exit__`  
**Visibility:** internal  
**Source line:** 135

<a id="function-streamablehttpmcpclient-init"></a>

### `StreamableHTTPMCPClient.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def StreamableHTTPMCPClient.__init__(self, url: str, *, timeout: int=60)
```

**Catalog symbol:** `x86decomp.mcp:StreamableHTTPMCPClient.__init__`  
**Visibility:** internal  
**Source line:** 140

<a id="function-streamablehttpmcpclient-request"></a>

### `StreamableHTTPMCPClient._request`

No function or method docstring is declared in the 0.7.5 source.

```python
def StreamableHTTPMCPClient._request(self, method: str, params: dict[str, Any] | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.mcp:StreamableHTTPMCPClient._request`  
**Visibility:** internal  
**Source line:** 149

<a id="function-streamablehttpmcpclient-notify"></a>

### `StreamableHTTPMCPClient._notify`

No function or method docstring is declared in the 0.7.5 source.

```python
def StreamableHTTPMCPClient._notify(self, method: str) -> None
```

**Catalog symbol:** `x86decomp.mcp:StreamableHTTPMCPClient._notify`  
**Visibility:** internal  
**Source line:** 183

<a id="function-streamablehttpmcpclient-initialize"></a>

### `StreamableHTTPMCPClient.initialize`

No function or method docstring is declared in the 0.7.5 source.

```python
def StreamableHTTPMCPClient.initialize(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.mcp:StreamableHTTPMCPClient.initialize`  
**Visibility:** public  
**Source line:** 192

<a id="function-streamablehttpmcpclient-ensure-initialized"></a>

### `StreamableHTTPMCPClient._ensure_initialized`

No function or method docstring is declared in the 0.7.5 source.

```python
def StreamableHTTPMCPClient._ensure_initialized(self) -> None
```

**Catalog symbol:** `x86decomp.mcp:StreamableHTTPMCPClient._ensure_initialized`  
**Visibility:** internal  
**Source line:** 198

<a id="function-streamablehttpmcpclient-list-tools"></a>

### `StreamableHTTPMCPClient.list_tools`

No function or method docstring is declared in the 0.7.5 source.

```python
def StreamableHTTPMCPClient.list_tools(self) -> list[MCPTool]
```

**Catalog symbol:** `x86decomp.mcp:StreamableHTTPMCPClient.list_tools`  
**Visibility:** public  
**Source line:** 202

<a id="function-streamablehttpmcpclient-call-tool"></a>

### `StreamableHTTPMCPClient.call_tool`

No function or method docstring is declared in the 0.7.5 source.

```python
def StreamableHTTPMCPClient.call_tool(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.mcp:StreamableHTTPMCPClient.call_tool`  
**Visibility:** public  
**Source line:** 207

<a id="function-streamablehttpmcpclient-close"></a>

### `StreamableHTTPMCPClient.close`

Streamable HTTP has no persistent local process to close.

```python
def StreamableHTTPMCPClient.close(self) -> None
```

**Catalog symbol:** `x86decomp.mcp:StreamableHTTPMCPClient.close`  
**Visibility:** public  
**Source line:** 211

<a id="function-is-probable-mutation"></a>

### `is_probable_mutation`

No function or method docstring is declared in the 0.7.5 source.

```python
def is_probable_mutation(tool_name: str) -> bool
```

**Catalog symbol:** `x86decomp.mcp:is_probable_mutation`  
**Visibility:** public  
**Source line:** 221

<a id="function-ghidramcpgateway-init"></a>

### `GhidraMCPGateway.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def GhidraMCPGateway.__init__(self, project_root: Path, client: StdioMCPClient | StreamableHTTPMCPClient, *, mutation_allowlist: set[str] | None=None)
```

**Catalog symbol:** `x86decomp.mcp:GhidraMCPGateway.__init__`  
**Visibility:** internal  
**Source line:** 229

<a id="function-ghidramcpgateway-read"></a>

### `GhidraMCPGateway.read`

No function or method docstring is declared in the 0.7.5 source.

```python
def GhidraMCPGateway.read(self, tool: str, arguments: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.mcp:GhidraMCPGateway.read`  
**Visibility:** public  
**Source line:** 236

<a id="function-ghidramcpgateway-propose-mutation"></a>

### `GhidraMCPGateway.propose_mutation`

No function or method docstring is declared in the 0.7.5 source.

```python
def GhidraMCPGateway.propose_mutation(self, *, tool: str, arguments: dict[str, Any], rationale: str, evidence_ids: list[str]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.mcp:GhidraMCPGateway.propose_mutation`  
**Visibility:** public  
**Source line:** 243

<a id="function-ghidramcpgateway-commit-mutation"></a>

### `GhidraMCPGateway.commit_mutation`

No function or method docstring is declared in the 0.7.5 source.

```python
def GhidraMCPGateway.commit_mutation(self, approval_hash: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.mcp:GhidraMCPGateway.commit_mutation`  
**Visibility:** public  
**Source line:** 269
