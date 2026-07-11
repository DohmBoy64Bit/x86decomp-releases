# MCP Commands

Commands for interacting with a Ghidra MCP (Model Context Protocol) server:
listing tools, invoking read-only queries, proposing mutations, and committing
approved changes.

## MCP Client Selection

All MCP commands require **exactly one** client transport selector:

| Option | Description |
|---|---|
| `--url URL` | Streamable HTTP MCP endpoint URL |
| `--command-json JSON` | Stdio MCP client; JSON array of command and arguments |

!!! failure "Exactly one required"
    `--url` and `--command-json` are mutually exclusive. Providing both or
    neither is a fatal error.

---

## `x86decomp mcp-tools`

List tools exposed by a configured MCP endpoint.

```console
x86decomp mcp-tools --url URL
x86decomp mcp-tools --command-json JSON
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `--url` | one of two | string | Streamable HTTP MCP endpoint |
| `--command-json` | one of two | JSON array | Stdio MCP command (e.g., `["python","-m","ghidra_mcp"]`) |

### Output

A JSON array of tool descriptors, each with `name`, `description`, and
`input_schema`.

### Example

```console
$ x86decomp mcp-tools --url http://127.0.0.1:8080/mcp
```

```console
$ x86decomp mcp-tools --command-json '["python","-m","ghidra_mcp"]'
```

---

## `x86decomp mcp-read`

Invoke a read-only MCP tool through the project gateway.

```console
x86decomp mcp-read PROJECT TOOL ARGUMENTS --url URL
x86decomp mcp-read PROJECT TOOL ARGUMENTS --command-json JSON
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PROJECT` | yes | path | Project root |
| `TOOL` | yes | string | MCP tool name to invoke |
| `ARGUMENTS` | yes | JSON object | Tool arguments as a JSON object |
| `--url` | one of two | string | Streamable HTTP MCP endpoint |
| `--command-json` | one of two | JSON array | Stdio MCP command |

### Safety

Read calls are memory-logged in the project. Tool-name heuristics reject probable
mutation tool names on the read path. No changes are made to the Ghidra project.

### Example

```console
$ x86decomp mcp-read my_project list_functions \
    '{"offset":0,"limit":100}' \
    --url http://127.0.0.1:8080/mcp
```

---

## `x86decomp mcp-propose`

Propose an evidence-linked MCP mutation for approval. Creates a persisted,
hash-verified proposal that must be committed via `mcp-commit`.

```console
x86decomp mcp-propose PROJECT TOOL ARGUMENTS \
    --allow-tool TOOL... \
    --rationale TEXT \
    --evidence EVID... \
    --url URL
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PROJECT` | yes | path | Project root |
| `TOOL` | yes | string | MCP tool name to invoke |
| `ARGUMENTS` | yes | JSON object | Tool arguments as a JSON object |
| `--allow-tool` | yes | string (repeatable) | Allowlist of permitted tool names |
| `--rationale` | yes | string | Human-readable rationale for the mutation |
| `--evidence` | yes | string (repeatable) | Evidence IDs linking the proposal to project evidence |
| `--url` | one of two | string | Streamable HTTP MCP endpoint |
| `--command-json` | one of two | JSON array | Stdio MCP command |

### Proposal Workflow

1. `mcp-propose` describes the intended mutation, rationale, and evidence
2. The proposal is hashed and persisted in the project
3. The approval hash is returned for use with `mcp-commit`
4. Mutations cannot be executed without the exact approval hash

!!! danger "Mutation guardrail"
    MCP writes require an explicit allowlist (`--allow-tool`), evidence,
    signed proposal, and exact commit hash. This prevents accidental or
    unauthorized modifications to the Ghidra project.

### Example

```console
$ x86decomp mcp-propose my_project rename_function \
    '{"address":"0x401000","name":"MainLoop"}' \
    --allow-tool rename_function \
    --rationale "Symbol confirmed via linker map public symbols" \
    --evidence ev-map-001 ev-crossref-042 \
    --url http://127.0.0.1:8080/mcp
```

---

## `x86decomp mcp-commit`

Commit an approved MCP mutation using the approval hash returned by `mcp-propose`.

```console
x86decomp mcp-commit PROJECT APPROVAL_HASH \
    --allow-tool TOOL... \
    --url URL
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PROJECT` | yes | path | Project root |
| `APPROVAL_HASH` | yes | string | Approval hash from `mcp-propose` |
| `--allow-tool` | yes | string (repeatable) | Allowlist of permitted tool names |
| `--url` | one of two | string | Streamable HTTP MCP endpoint |
| `--command-json` | one of two | JSON array | Stdio MCP command |

### Behavior

1. Looks up the persisted proposal by approval hash
2. Verifies the allowlist matches the proposal
3. Executes the mutation through the MCP gateway
4. Returns the mutation result

### Example

```console
$ x86decomp mcp-commit my_project abc123def456 \
    --allow-tool rename_function \
    --url http://127.0.0.1:8080/mcp
```

---

## Complete MCP Workflow

```console
# 1. Discover available tools
$ x86decomp mcp-tools --url http://127.0.0.1:8080/mcp

# 2. Read current state (read-only, no proposal needed)
$ x86decomp mcp-read my_project get_function \
    '{"address":"0x401000"}' \
    --url http://127.0.0.1:8080/mcp

# 3. Propose a change
$ x86decomp mcp-propose my_project set_function_name \
    '{"address":"0x401000","name":"MainLoop"}' \
    --allow-tool set_function_name \
    --rationale "MAP symbol at 0x401000 matches MainLoop" \
    --evidence ev-map-001 \
    --url http://127.0.0.1:8080/mcp

# 4. Review the proposal (external step by operator)

# 5. Commit the approved change
$ x86decomp mcp-commit my_project <approval_hash> \
    --allow-tool set_function_name \
    --url http://127.0.0.1:8080/mcp
```

### Related Commands

- [`ghidra-export`](export.md) — batch export Ghidra analysis artifacts
- [`artifact-import`](../artifacts/artifact.md) — import exported function artifacts
- [`evidence-add`](../workflow/evidence-claims.md) — register evidence records
