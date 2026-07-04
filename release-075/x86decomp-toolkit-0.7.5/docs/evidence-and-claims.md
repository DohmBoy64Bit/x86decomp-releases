# Evidence and claims

## Why claims are separate from observations

A machine instruction, a decompiler type, and a human interpretation are different
kinds of information. Combining them in one editable comment makes it difficult to
distinguish what was observed from what was inferred. The evidence store therefore
separates records from claims.

## Evidence kinds

- `binary_bytes`: immutable bytes or directly decoded values.
- `static_analysis`: Ghidra, Capstone, or another non-executing analysis result.
- `dynamic_trace`: observed execution in a controlled environment.
- `compiler_output`: compiler object, listing, diagnostics, or match report.
- `debug_symbol`: PDB or other symbol information tied to an identifiable build.
- `external_document`: authoritative format/compiler/tool documentation.
- `human_review`: a signed analyst review; useful but not independently machine-verifiable.

## Verification gate

A claim reaches `verified` only when all conditions pass:

1. At least three evidence records.
2. At least three independent groups.
3. At least two evidence kinds.
4. All file-backed evidence hashes still match.
5. No unresolved contradiction evidence.

A claim with two records may become `corroborated`; one or zero remains `proposed`.
The gate intentionally prevents one tool from self-corroborating through multiple
views of the same internal state.

## Examples

### Calling convention

Potentially independent support:

- raw bytes showing ECX consumed as an object pointer and callee stack behavior;
- Ghidra call-site analysis across multiple callers;
- a compiler experiment that reproduces the entry/return sequence.

### Original function name

A readable string or an AI suggestion is insufficient. Strong evidence could include:

- matching PDB symbol tied to the exact debug GUID and age;
- export table name;
- an authoritative map file for the same build.

Without such evidence, use a descriptive analyst name with source `USER_DEFINED` and
do not label it original.

### Structure layout

Repeated field offsets, dynamic access traces, and compiler layout experiments may
verify offsets and sizes. They do not establish the original type name.
