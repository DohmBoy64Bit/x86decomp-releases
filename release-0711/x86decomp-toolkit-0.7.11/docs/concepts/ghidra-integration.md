# Ghidra Integration

The toolkit integrates with Ghidra through three channels: Java-based export scripts
that run inside Ghidra, an MCP client that communicates with Ghidra's MCP server, and
the `crosscheck-ghidra` command that validates toolkit disassembly against Ghidra output.

## Java Exporters

Three bundled Ghidra scripts (in `ghidra_scripts/`) produce structured project data:

| Script | Purpose | Output |
|---|---|---|
| `ExportProjectManifest.java` | Full program manifest | Function list, entry points, sections, imports, exports, data types, memory map |
| `ExportFunctionArtifacts.java` | Per-function exports | Disassembly, decompiled C, control flow graph, data references, cross-references |
| `QueryAnalysis.java` | Targeted analysis queries | RTTI, vtable, string, or symbol queries with bounded results |

### Running Exports

```bash
x86decomp ghidra-export \
  --ghidra-home /opt/ghidra \
  --project /home/user/ghidra-projects/GameAnalysis \
  --program game.exe \
  --output-dir ./analysis/ghidra \
  --exporters manifest,functions
```

The command builds a headless Ghidra invocation:

```
{PATH}/analyzeHeadless {project_dir} {project_name} \
  -process {program_name} \
  -scriptPath {ghidra_scripts_dir} \
  -postScript ExportProjectManifest.java {output_dir} \
  -postScript ExportFunctionArtifacts.java {output_dir}
```

### Export Arguments

| Argument | Required | Description |
|---|---|---|
| `--ghidra-home` | Yes | Path to Ghidra installation root |
| `--project` | Yes | Path to Ghidra project directory |
| `--program` | Yes | Program name within the project |
| `--output-dir` | Yes | Directory for export files |
| `--exporters` | No | Comma-separated list: `manifest`, `functions`, `analysis` (default: all three) |
| `--timeout` | No | Timeout in seconds (default: 600) |
| `--java-args` | No | Additional JVM arguments |

### Export Output

`ExportProjectManifest` produces `project_manifest.json`:

```json
{
  "program": "game.exe",
  "architecture": "x86:LE:32:default",
  "compiler_spec": "windows",
  "image_base": 4194304,
  "functions": [
    {"name": "FUN_00401000", "entry": "0x00401000", "signature": "void __stdcall FUN_00401000(int param_1)"},
    {"name": "FUN_00401050", "entry": "0x00401050", "signature": "int __cdecl FUN_00401050(void)"}
  ],
  "entry_points": ["0x00401000"],
  "sections": [
    {"name": ".text", "start": "0x00401000", "end": "0x00420000"}
  ]
}
```

## MCP Client

The toolkit implements the MCP 2025-06-18 protocol with two transports:

### Stdio Transport

Launches an MCP server as a subprocess:

```bash
x86decomp mcp-tools --transport stdio --command python,-m,ghidra_mcp.server
```

```python
from x86decomp.mcp import StdioMCPClient, GhidraMCPGateway

# In code:
client = StdioMCPClient(["python", "-m", "ghidra_mcp.server"])
gateway = GhidraMCPGateway(project_root, client)
```

### Streamable HTTP Transport

Connects to an already-running MCP server over HTTP:

```bash
x86decomp mcp-tools --transport http --url http://127.0.0.1:8080/mcp
```

Uses `Mcp-Session-Id` headers for session management and supports both plain JSON and
Server-Sent Events (`text/event-stream`) response modes.

## Read-Only Gateway

The `GhidraMCPGateway` enforces a read/write separation:

### Read Operations

```bash
x86decomp mcp-read \
  --project . \
  --transport stdio \
  --command python,-m,ghidra_mcp.server \
  --tool get_function \
  --arguments '{"address": "0x401000"}'
```

Read operations are unrestricted but logged to project memory:

```
ProjectMemory: actor=ghidra-mcp, category=mcp-read,
summary="Called read-only MCP tool get_function.",
details={"tool": "get_function", "arguments": {"address": "0x401000"}}
```

### Mutation Detection

The gateway classifies tools as mutations based on name patterns:

```
rename, create, delete, set_, update, apply, write, save,
comment, type, structure, enum, function_signature, prototype
```

Any tool matching these patterns is blocked from `mcp-read` and must go through the
propose/commit path:

```bash
# This fails:
x86decomp mcp-read --tool rename_function --arguments '{"address": "0x401000", "name": "main"}'
# Error: probable mutation tool must use propose/commit: rename_function
```

## Mutation Proposals

Mutations require an allowlist, evidence, and a hash-signed proposal:

### Step 1: Propose

```bash
x86decomp mcp-propose \
  --project . \
  --transport stdio \
  --command python,-m,ghidra_mcp.server \
  --allowlist rename_function,set_function_prototype \
  --tool rename_function \
  --arguments '{"address": "0x401000", "name": "main"}' \
  --rationale "PDB symbol 'main' confirms function at 0x401000" \
  --evidence ev-abc123,ev-def456
```

The proposal is stored as a hash-signed JSON file:

```
analysis/mcp-transactions/
└── a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6...json
```

### Proposal Structure

```json
{
  "schema_version": 1,
  "created_at": "2026-07-11T10:00:00Z",
  "tool": "rename_function",
  "arguments": {"address": "0x401000", "name": "main"},
  "rationale": "PDB symbol 'main' confirms function at 0x401000",
  "evidence_ids": ["ev-abc123", "ev-def456"],
  "status": "proposed",
  "approval_hash": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0"
}
```

### Step 2: Commit

```bash
x86decomp mcp-commit \
  --project . \
  --transport stdio \
  --command python,-m,ghidra_mcp.server \
  --approval-hash a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0
```

The commit step:

1. Re-hashes the proposal to verify it wasn't tampered with.
2. Checks the proposal hasn't already been committed.
3. Executes the tool call against Ghidra.
4. Records the result and commit timestamp.
5. Logs to project memory.

### Commitment Result

```json
{
  "schema_version": 1,
  "tool": "rename_function",
  "status": "committed",
  "committed_at": "2026-07-11T10:05:00Z",
  "result": {"success": true, "previous_name": "FUN_00401000", "new_name": "main"}
}
```

!!! warning "Allowlist is required"
    Only tools in the `--allowlist` can be proposed for mutation. This prevents accidental
    or malicious changes to Ghidra's analysis database. Add tools to the allowlist
    cautiously and only after reviewing their behavior.

## Listing Tools

```bash
# Stdio transport
x86decomp mcp-tools --transport stdio --command python,-m,ghidra_mcp.server

# HTTP transport
x86decomp mcp-tools --transport http --url http://127.0.0.1:8080/mcp
```

Returns all MCP tools advertised by the server:

```json
[
  {
    "name": "list_functions",
    "description": "List all functions in the program",
    "inputSchema": {
      "type": "object",
      "properties": {
        "offset": {"type": "integer"},
        "limit": {"type": "integer"}
      }
    }
  }
]
```

## Cross-Check: Toolkit vs Ghidra

Validate toolkit disassembly against Ghidra's instruction decoding:

```bash
x86decomp crosscheck-ghidra \
  --code <hex_bytes> \
  --base-address 0x401000 \
  --ghidra-export analysis/ghidra/functions/FUN_00401000.json
```

See [Static Analysis](static-analysis.md#cross-check-toolkit-vs-ghidra) for the
comparison categories and severity levels.

## Project Integration

### Export → Evidence

Ghidra exports can be imported as evidence:

```bash
x86decomp evidence-add --project . \
  --kind external_document \
  --source "Ghidra 11.0 ExportProjectManifest" \
  --locator "ghidra:export:project_manifest.json" \
  --assertion "Ghidra identified 342 functions in game.exe" \
  --independent-group "ghidra-analysis" \
  --file "./analysis/ghidra/project_manifest.json"
```

### Ghidra in Project Memory

Every MCP interaction is logged to the project memory ledger:

```bash
x86decomp memory-render --project . --output memory.md
```

Produces a chronological record of all Ghidra interactions alongside other project events.

## Typical Setup

```bash
# 1. Export from Ghidra
x86decomp ghidra-export \
  --ghidra-home "C:\ghidra_11.0_PUBLIC" \
  --project "C:\ghidra-projects\GameAnalysis" \
  --program game.exe \
  --output-dir ./analysis/ghidra

# 2. Start Ghidra MCP server (outside the toolkit)
python -m ghidra_mcp.server

# 3. List tools
x86decomp mcp-tools --transport stdio --command python,-m,ghidra_mcp.server

# 4. Read function info
x86decomp mcp-read --project . --transport stdio \
  --command python,-m,ghidra_mcp.server \
  --tool get_function --arguments '{"address": "0x401000"}'

# 5. Cross-check disassembly
x86decomp crosscheck-ghidra \
  --code <hex> --base-address 0x401000 \
  --ghidra-export analysis/ghidra/functions/FUN_00401000.json
```

!!! tip "MCP server management"
    The toolkit does not start or stop the Ghidra MCP server. You are responsible for
    launching the server before using MCP commands and shutting it down afterward.
    The stdio transport launches a subprocess per-command; for persistent use,
    prefer the Streamable HTTP transport with a long-running server.
