# Execution Harness

Generate an execution harness from binary functions for differential validation.

## `x86decomp harness-generate`

```console
x86decomp harness-generate ABI_CONTRACT OUTPUT \
    --pointer-parameters PATH \
    --no-observe-pointers \
    --max-instructions 100000 \
    --timeout-ms 1000
```

### Purpose

Generate an execution harness that can invoke a binary function under controlled
conditions, observe its behavior, and compare it against a candidate implementation.
The harness is guided by an ABI contract and optional pointer-parameter metadata.

### Arguments

| Argument | Required | Type | Default | Description |
|---|---|---|---|---|
| `ABI_CONTRACT` | yes | path | — | ABI contract JSON defining calling convention, registers, stack layout |
| `OUTPUT` | yes | path | — | Output harness file path |
| `--pointer-parameters` | no | path | — | JSON file describing pointer parameters (regions, aliases) |
| `--no-observe-pointers` | no | flag | — | Disable pointer-parameter observation in the harness |
| `--max-instructions` | no | integer | `100000` | Maximum instructions to execute before forcing termination |
| `--timeout-ms` | no | integer | `1000` | Wall-clock timeout in milliseconds |

### Pointer Parameters

When `--pointer-parameters` is provided, the JSON must describe memory regions that
the harness will initialize and observe:

- Which parameters are pointers
- Expected region sizes and alignments
- Alias relationships between regions

When `--no-observe-pointers` is set, the harness treats all parameters as opaque
values (no memory is allocated or compared).

### Example

```console
$ x86decomp harness-generate abi_contracts/func_1234.json harness.bin \
    --pointer-parameters pointers.json \
    --max-instructions 50000 \
    --timeout-ms 2000
```

### Related Commands

- [`dynamic-validate`](../validation/dynamic.md) — differentially execute with a harness
- [`abi-check`](../validation/abi.md) — validate behavior against an ABI contract
- [`symbolic-validate`](../validation/symbolic.md) — symbolic comparison (no harness needed)
