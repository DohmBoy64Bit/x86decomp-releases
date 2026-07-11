# Ghidra scripts

The toolkit ships three Java exporter scripts that use the public Ghidra decompiler, listing,
and P-code APIs.

## Verification

Run `scripts/verify-ghidra.sh` against the exact installed Ghidra release before project adoption.

!!! warning "Version dependency"
    Ghidra analysis output can change across versions. Benchmark against a pinned release.

## ExportProjectManifest.java

Writes project-wide metadata:

| Output file | Content |
|---|---|
| `program.json` | Program-level properties |
| `sections.json` | Section layout |
| `functions.jsonl` | Every function with exact body-range lists |
| `symbols.jsonl` | Exported symbol records |
| `types.jsonl` | Type definitions |
| `metrics.json` | Aggregate metrics |

## ExportFunctionArtifacts.java

Writes per-function artifacts for every selected non-external function:

| Artifact | Description |
|---|---|
| Exact bytes | For every discontiguous range |
| Disassembly | Rendered text and structured instruction/flow records |
| References | Cross-references extracted from the listing |
| Decompiler C | Ghidra decompiler output |
| Clang token tree | Structured token/group tree with address bounds |
| P-code | Raw instruction P-code JSONL, high P-code JSONL and text |
| Context header | Conservative calling-convention and type context |
| Function manifest | Mode selection (matching and functional) |

## QueryAnalysis.java

Provides read-only queries:

* Function listing by address or name
* Caller/callee enumeration
* Cross-reference resolution
* Disassembly queries

## Interpretation rules

* Ghidra function bodies are address sets, not one assumed interval.
* Decompiler C is a source candidate, not original source.
* P-code and token-tree formats are versioned toolkit exports; Ghidra internal behavior
  remains tool-version dependent.
* Imported names/types retain Ghidra source/provenance.

!!! warning "Cross-check boundaries"
    Suspicious instruction boundaries must be cross-checked with the independent Capstone
    decoder via `crosscheck-ghidra`.

## MCP gateway

The Python MCP client supports stdio and Streamable HTTP. Read calls are memory-logged.
Tool-name mutation heuristics prevent accidental writes through the read path. Writes
require an explicit allowlist and a hash-verified persisted proposal containing
rationale and evidence IDs.
