# Document and state contracts

Every component in the toolkit operates under formal contracts. This page documents each one.

## Stable identity

* Function ID: `pe-rva:XXXXXXXX`.
* Directory ID: `pe-rva_XXXXXXXX`.
* RVA ranges are half-open `[start_rva, end_rva)`.
* A function may have multiple discontiguous ranges.
* A VA/address string is display/provenance; the RVA is the project key.

## Mode contract

Every function selects one or both modes:

| Mode | Measures |
|---|---|
| `matching` | Reproduction of machine representation |
| `functional` | Behavior under declared models/tests |

One mode never promotes the other. `byte_matched` does not imply runtime coverage;
`differentially_validated` does not imply instruction match.

## Matching status contract

| Status | Meaning |
|---|---|
| `not_started` | No mode work |
| `decompiled` | Analysis candidate exists |
| `compiles` | Named profile emitted an artifact |
| `abi_compatible` | All declared ABI checks passed |
| `instruction_similar` | Versioned normalizer passed its configured threshold/equality |
| `byte_matched` | Raw bytes in the exact stated scope are identical |
| `image_integrated` | Hash-gated patch/integration report passed |
| `full_relink_validated` | Declared linker completed and the project-defined image gate passed |
| `blocked` | Work cannot advance; blocker text is mandatory in practice |

## Functional status contract

| Status | Meaning |
|---|---|
| `not_started`, `decompiled`, `compiles`, `abi_compatible` | Same narrow meanings as matching |
| `differentially_validated` | All declared concrete harnesses passed |
| `symbolically_bounded` | Selected solver/backend returned equality within its explicit model |
| `integration_validated` | Named application scenarios passed in a recorded environment |
| `blocked` | Explicit side state |

## Evidence contract

Evidence contains source, locator, assertion, kind, independence group, observation
time, optional metadata and an immutable file hash.

!!! warning
    Tool output is evidence of what the tool reported, not automatic evidence that the
    report is correct.

## Claim contract

A verified claim requires three evidence records, three independent failure domains,
two evidence kinds, intact hashes and no unresolved contradiction. The claim wording
must match exactly what the evidence establishes.

## Compiler contract

A compiler report records profile, executable path/hash/version, complete argument
array, work directory, environment policy, source/output hashes, timeout, return code,
stdout and stderr. No shell string is used.

## Comparison contract

| Comparison | Rule |
|---|---|
| Raw byte equality | Exact |
| Relocation-normalized equality | Names every masked interval and reason |
| Instruction similarity | Records decoder and normalization policy |
| ABI compatibility | Records each necessary observation |
| Dynamic equality | Tied to one harness state |
| Symbolic equality | Tied to instruction/model/path bounds |
| Integration equality | Tied to named scenarios, exact commands, inputs, environment, isolation declaration and observed outputs |

## MCP mutation contract

A mutation is valid only if its tool is allowlisted, rationale and evidence IDs exist,
the proposal document hash verifies, its status is still `proposed`, and the committed
arguments are byte-for-byte the signed arguments.

## Work-task contract

A task cannot be proposed before claim; a proposal cannot omit evidence IDs; acceptance
requires every named validator to have a passing report.

!!! danger
    AI authorship never counts as a validator or independent evidence group.

## Integration scenario contract

Host execution requires both `execution.mode=host_explicit`, a manifest acknowledgement,
and the runtime `--allow-host-execution` flag. External-wrapper mode requires a non-empty
argument prefix. Each target/candidate process runs in a separate temporary work tree.
Only declared exit codes, streams, and files are compared. Paths are confined beneath
the work tree, fixture copies are hashed, and timeouts are failures.

## objdiff adapter contract

The manifest supplies the exact executable and argument array. `{target}` and
`{candidate}` are mandatory tokens; `{output}` and `{workdir}` are optional. The report
records executable and input hashes, complete command, return code, stdout/stderr, and
parsed output.

!!! note
    The adapter proves only that the configured objdiff process ran and reported the
    captured result.

## Local decomp.me packet contract

The packet is generated from a function artifact and never uploads data. It contains
Ghidra listing text, decompiler C, context, references and hashes. Listing syntax is
explicitly labeled non-canonical and must be converted and independently validated.
