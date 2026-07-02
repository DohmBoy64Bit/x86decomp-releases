---
title: x86decomp.mcp
description: MCP 2025-06-18 client and evidence-gated Ghidra mutation journal.
original_path: features/x86decomp-mcp.html
---

<a id="function-stdiomcpclient-init"></a>
<a id="function-stdiomcpclient-send"></a>
<a id="function-stdiomcpclient-request"></a>
<a id="function-stdiomcpclient-initialize"></a>
<a id="function-stdiomcpclient-ensure-initialized"></a>
<a id="function-stdiomcpclient-list-tools"></a>
<a id="function-stdiomcpclient-call-tool"></a>
<a id="function-stdiomcpclient-close"></a>
<a id="function-stdiomcpclient-enter"></a>
<a id="function-stdiomcpclient-exit"></a>
<a id="function-streamablehttpmcpclient-init"></a>
<a id="function-streamablehttpmcpclient-request"></a>
<a id="function-streamablehttpmcpclient-notify"></a>
<a id="function-streamablehttpmcpclient-initialize"></a>
<a id="function-streamablehttpmcpclient-ensure-initialized"></a>
<a id="function-streamablehttpmcpclient-list-tools"></a>
<a id="function-streamablehttpmcpclient-call-tool"></a>
<a id="function-streamablehttpmcpclient-close"></a>
<a id="function-is-probable-mutation"></a>
<a id="function-ghidramcpgateway-init"></a>
<a id="function-ghidramcpgateway-read"></a>
<a id="function-ghidramcpgateway-propose-mutation"></a>
<a id="function-ghidramcpgateway-commit-mutation"></a>

Section: Source-derived feature and function reference

# x86decomp.mcp

MCP 2025-06-18 client and evidence-gated Ghidra mutation journal.

Metadata: core · current · 23 functions/methods

**Source:** `src/x86decomp/mcp.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `72627e41c628c756443bc5d57e38b583b1744923902735b55a3d6c9e29f6cca9`.

## Functions and methods

Metadata: internal · line 30

### StdioMCPClient.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, command: list[str], *, cwd: Path | None = None)
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient.__init__`

Metadata: internal · line 46

### StdioMCPClient._send

No function or method docstring is declared in the v0.7.4 source.

```
def _send(self, message: dict[str, Any]) -> None
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient._send`

Metadata: internal · line 52

### StdioMCPClient._request

No function or method docstring is declared in the v0.7.4 source.

```
def _request(self, method: str, params: dict[str, Any] | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient._request`

Metadata: public · line 79

### StdioMCPClient.initialize

No function or method docstring is declared in the v0.7.4 source.

```
def initialize(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient.initialize`

Metadata: internal · line 92

### StdioMCPClient._ensure_initialized

No function or method docstring is declared in the v0.7.4 source.

```
def _ensure_initialized(self) -> None
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient._ensure_initialized`

Metadata: public · line 96

### StdioMCPClient.list_tools

No function or method docstring is declared in the v0.7.4 source.

```
def list_tools(self) -> list[MCPTool]
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient.list_tools`

Metadata: public · line 115

### StdioMCPClient.call_tool

No function or method docstring is declared in the v0.7.4 source.

```
def call_tool(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient.call_tool`

Metadata: public · line 119

### StdioMCPClient.close

No function or method docstring is declared in the v0.7.4 source.

```
def close(self) -> None
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient.close`

Metadata: internal · line 132

### StdioMCPClient.__enter__

No function or method docstring is declared in the v0.7.4 source.

```
def __enter__(self) -> 'StdioMCPClient'
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient.__enter__`

Metadata: internal · line 135

### StdioMCPClient.__exit__

No function or method docstring is declared in the v0.7.4 source.

```
def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None
```

**Catalog symbol:** `x86decomp.mcp:StdioMCPClient.__exit__`

Metadata: internal · line 140

### StreamableHTTPMCPClient.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, url: str, *, timeout: int = 60)
```

**Catalog symbol:** `x86decomp.mcp:StreamableHTTPMCPClient.__init__`

Metadata: internal · line 149

### StreamableHTTPMCPClient._request

No function or method docstring is declared in the v0.7.4 source.

```
def _request(self, method: str, params: dict[str, Any] | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.mcp:StreamableHTTPMCPClient._request`

Metadata: internal · line 183

### StreamableHTTPMCPClient._notify

No function or method docstring is declared in the v0.7.4 source.

```
def _notify(self, method: str) -> None
```

**Catalog symbol:** `x86decomp.mcp:StreamableHTTPMCPClient._notify`

Metadata: public · line 192

### StreamableHTTPMCPClient.initialize

No function or method docstring is declared in the v0.7.4 source.

```
def initialize(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.mcp:StreamableHTTPMCPClient.initialize`

Metadata: internal · line 198

### StreamableHTTPMCPClient._ensure_initialized

No function or method docstring is declared in the v0.7.4 source.

```
def _ensure_initialized(self) -> None
```

**Catalog symbol:** `x86decomp.mcp:StreamableHTTPMCPClient._ensure_initialized`

Metadata: public · line 202

### StreamableHTTPMCPClient.list_tools

No function or method docstring is declared in the v0.7.4 source.

```
def list_tools(self) -> list[MCPTool]
```

**Catalog symbol:** `x86decomp.mcp:StreamableHTTPMCPClient.list_tools`

Metadata: public · line 207

### StreamableHTTPMCPClient.call_tool

No function or method docstring is declared in the v0.7.4 source.

```
def call_tool(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.mcp:StreamableHTTPMCPClient.call_tool`

Metadata: public · line 211

### StreamableHTTPMCPClient.close

Streamable HTTP has no persistent local process to close.

```
def close(self) -> None
```

**Catalog symbol:** `x86decomp.mcp:StreamableHTTPMCPClient.close`

Metadata: public · line 221

### is_probable_mutation

No function or method docstring is declared in the v0.7.4 source.

```
def is_probable_mutation(tool_name: str) -> bool
```

**Catalog symbol:** `x86decomp.mcp:is_probable_mutation`

Metadata: internal · line 229

### GhidraMCPGateway.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, project_root: Path, client: StdioMCPClient | StreamableHTTPMCPClient, *, mutation_allowlist: set[str] | None = None)
```

**Catalog symbol:** `x86decomp.mcp:GhidraMCPGateway.__init__`

Metadata: public · line 236

### GhidraMCPGateway.read

No function or method docstring is declared in the v0.7.4 source.

```
def read(self, tool: str, arguments: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.mcp:GhidraMCPGateway.read`

Metadata: public · line 243

### GhidraMCPGateway.propose_mutation

No function or method docstring is declared in the v0.7.4 source.

```
def propose_mutation(self, *, tool: str, arguments: dict[str, Any], rationale: str, evidence_ids: list[str]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.mcp:GhidraMCPGateway.propose_mutation`

Metadata: public · line 269

### GhidraMCPGateway.commit_mutation

No function or method docstring is declared in the v0.7.4 source.

```
def commit_mutation(self, approval_hash: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.mcp:GhidraMCPGateway.commit_mutation`
