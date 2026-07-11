# Ghidra Export

Run the bundled Ghidra export workflow to extract function artifacts, symbols,
types, and disassembly from a Ghidra project.

## `x86decomp ghidra-export`

```console
x86decomp ghidra-export BINARY GHIDRA_PROJECT_DIR GHIDRA_PROJECT_NAME OUTPUT_DIR \
    --scripts-dir ghidra_scripts \
    --ghidra-home PATH \
    --overwrite \
    --selector all \
    --timeout 3600 \
    --report REPORT \
    --print-command
```

### Purpose

Execute the bundled Ghidra headless export workflow against a binary imported into a
Ghidra project. Exports program metadata, per-function artifacts, and analysis
results as structured JSON.

### Arguments

| Argument | Required | Type | Default | Description |
|---|---|---|---|---|
| `BINARY` | yes | path | — | Original binary that was imported into Ghidra |
| `GHIDRA_PROJECT_DIR` | yes | path | — | Ghidra project directory |
| `GHIDRA_PROJECT_NAME` | yes | string | — | Name of the Ghidra project |
| `OUTPUT_DIR` | yes | path | — | Output directory for exported artifacts |
| `--scripts-dir` | no | path | `ghidra_scripts` | Directory containing the bundled Ghidra export scripts |
| `--ghidra-home` | no | path | — | Path to Ghidra installation (or auto-detected) |
| `--overwrite` | no | flag | — | Overwrite existing export output |
| `--selector` | no | string | `all` | Function selector filter (`all` or specific pattern) |
| `--timeout` | no | integer | `3600` | Maximum execution time in seconds |
| `--report` | no | path | — | Write export report as JSON |
| `--print-command` | no | flag | — | Print the constructed Ghidra command without executing |

### Exported Artifacts

The export workflow writes two categories of output:

#### Project Manifest (`ExportProjectManifest.java`)

| File | Content |
|---|---|
| `program.json` | Program metadata and image base |
| `sections.json` | Section headers and RVA ranges |
| `functions.jsonl` | Function list with exact body-range lists |
| `symbols.jsonl` | Symbol names, addresses, and types |
| `types.jsonl` | Recovered type definitions |
| `metrics.json` | Analysis and export metrics |

#### Function Artifacts (`ExportFunctionArtifacts.java`)

For every selected non-external function:

| Artifact | Content |
|---|---|
| Exact bytes | Raw code bytes for every discontiguous range |
| Disassembly | Structured instruction and flow records |
| References | Cross-references (code, data, calls) |
| Decompiler C | Ghidra decompiler output |
| Token tree | Clang token/group tree with address bounds |
| P-code raw | Raw instruction P-code as JSONL |
| P-code high | High-level P-code as JSONL and text |
| Context header | Conservative calling-convention context |

!!! warning "Ghidra version sensitivity"
    Ghidra analysis output can change across versions. Run `scripts/verify-ghidra.sh`
    against the exact installed release before adopting exports for matching work.

### Example

```console
$ x86decomp ghidra-export original/game.exe \
    projects/ghidra GameProject \
    exports/game_export \
    --scripts-dir ghidra_scripts \
    --ghidra-home /opt/ghidra_11.0_PUBLIC \
    --overwrite \
    --timeout 7200 \
    --report export-report.json
```

Dry-run (print the command without executing):

```console
$ x86decomp ghidra-export original/game.exe projects/ghidra GameProject \
    exports/out --print-command
```

### Related Commands

- [`mcp-tools`](mcp.md#x86decomp-mcp-tools) — list MCP tools in Ghidra
- [`mcp-read`](mcp.md#x86decomp-mcp-read) — invoke read-only Ghidra queries via MCP
- [`crosscheck-ghidra`](../analysis/disassembly.md) — compare toolkit disassembly with Ghidra export
- [`artifact-import`](../artifacts/artifact.md) — import exported function artifacts
