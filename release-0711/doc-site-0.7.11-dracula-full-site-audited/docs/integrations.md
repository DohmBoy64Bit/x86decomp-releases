---
title: Integrations
description: Source-synchronized 0.7.11 documentation page.
---

# Ghidra integration

## Baseline and verification

The scripts use public Ghidra decompiler/listing/P-code APIs. Run
`scripts/verify-ghidra.sh` against the exact installed release before project adoption;
Ghidra analysis output can change across versions.

## Exports

`ExportProjectManifest.java` writes:

- `program.json` and `sections.json`;
- `functions.jsonl` with exact body-range lists;
- `symbols.jsonl`;
- `types.jsonl`;
- `metrics.json`.

`ExportFunctionArtifacts.java` writes for every selected non-external function:

- exact bytes for every discontiguous range;
- rendered disassembly and structured instruction/flow records;
- references;
- decompiler C;
- a structured Clang token/group tree with address bounds;
- raw instruction P-code JSONL;
- high P-code JSONL and text;
- conservative context header;
- function manifest selecting matching and functional modes.

`QueryAnalysis.java` provides read-only function, callers, references and disassembly
queries.

## Interpretation rules

- Ghidra function bodies are address sets, not one assumed interval.
- decompiler C is a source candidate, not original source.
- P-code and token-tree formats are versioned toolkit exports; Ghidra internal behavior
  remains tool-version dependent.
- imported names/types retain Ghidra source/provenance.
- suspicious instruction boundaries must be cross-checked with the independent decoder.

## MCP

The Python MCP client supports stdio and Streamable HTTP. Read calls are memory-logged.
Tool-name mutation heuristics prevent accidental writes through the read path. Writes
require an explicit allowlist and a hash-verified persisted proposal containing
rationale and evidence IDs.
